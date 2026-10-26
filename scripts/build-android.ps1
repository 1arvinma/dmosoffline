param([Parameter(Mandatory=$true)][string]$SdkRoot,[Parameter(Mandatory=$true)][string]$JavaHome,[Parameter(Mandatory=$true)][string]$Keystore,[Parameter(Mandatory=$true)][string]$Alias,[string]$PasswordEnvironmentVariable='DMOS_SIGNING_PASSWORD',[string]$Bundletool)
$ErrorActionPreference='Stop'
$root=Split-Path $PSScriptRoot -Parent
$build=Join-Path $root 'dist/android-build'
$out=Join-Path $root 'dist'
$source=Join-Path $root 'native/android'
$tools=Join-Path $SdkRoot 'build-tools/35.0.0'
$android=Join-Path $SdkRoot 'platforms/android-36/android.jar'
$java=Join-Path $JavaHome 'bin'
New-Item -ItemType Directory -Force "$build/classes","$build/dex" | Out-Null
node "$PSScriptRoot/assemble.cjs"
$version=(Get-Content (Join-Path $root "release.json") -Raw | ConvertFrom-Json).version
& "$java/javac.exe" -encoding UTF-8 -source 8 -target 8 -bootclasspath "$android;$tools/core-lambda-stubs.jar" -d "$build/classes" "$source/MainActivity.java" "$source/SheetProvider.java"
if($LASTEXITCODE){throw 'Java compilation failed'}
Compress-Archive -Path "$build/classes/*" -DestinationPath "$build/classes.zip" -Force
Copy-Item "$build/classes.zip" "$build/classes.jar" -Force
& "$java/java.exe" -cp "$tools/lib/d8.jar" com.android.tools.r8.D8 --min-api 26 --lib $android --output "$build/dex" "$build/classes.jar"
if($LASTEXITCODE){throw 'DEX compilation failed'}
& "$tools/aapt2.exe" compile --dir "$source/res" -o "$build/resources.zip"
& "$tools/aapt2.exe" link -o "$build/base.apk" -I $android --manifest "$source/AndroidManifest.xml" --min-sdk-version 26 --target-sdk-version 36 "$build/resources.zip"
if($LASTEXITCODE){throw 'Resource link failed'}
python "$PSScriptRoot/repack-android.py" $build "$root/app"
if($LASTEXITCODE){throw 'APK packing failed'}
& "$tools/zipalign.exe" -f -P 16 4 "$build/repacked.apk" "$build/aligned.apk"
if($LASTEXITCODE){throw 'APK alignment failed'}
& "$java/java.exe" -cp "$tools/lib/apksigner.jar" com.android.apksigner.ApkSignerTool sign --ks $Keystore --ks-key-alias $Alias --ks-pass "env:$PasswordEnvironmentVariable" --key-pass "env:$PasswordEnvironmentVariable" --v4-signing-enabled false --out "$out/DMOS-OpenSource-$version.apk" "$build/aligned.apk"
if($LASTEXITCODE){throw 'APK signing failed'}
& "$java/java.exe" -cp "$tools/lib/apksigner.jar" com.android.apksigner.ApkSignerTool verify --verbose "$out/DMOS-OpenSource-$version.apk"
if($LASTEXITCODE){throw 'APK verification failed'}
if($Bundletool){
 & "$tools/aapt2.exe" link --proto-format -o "$build/proto.apk" -I $android --manifest "$source/AndroidManifest.xml" --min-sdk-version 26 --target-sdk-version 36 "$build/resources.zip"
 python "$PSScriptRoot/bundle-android.py" $build "$root/app"
 & "$java/java.exe" "-Djava.io.tmpdir=$build" -jar $Bundletool build-bundle --modules="$build/module.zip" --output="$out/DMOS-OpenSource-$version.aab" --overwrite
 if($LASTEXITCODE){throw 'Bundle build failed'}
 & "$java/jarsigner.exe" -keystore $Keystore -storepass:env $PasswordEnvironmentVariable -keypass:env $PasswordEnvironmentVariable "$out/DMOS-OpenSource-$version.aab" $Alias
 if($LASTEXITCODE){throw 'Bundle signing failed'}
 & "$java/java.exe" -jar $Bundletool validate --bundle="$out/DMOS-OpenSource-$version.aab"
 if($LASTEXITCODE){throw 'Bundle verification failed'}
}
