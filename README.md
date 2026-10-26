# DMOS Offline 1.2.0 — open source

Offline campaign management for Windows, Android and the browser. Party sheets, legacy imports, player forms with unique score assignment, combat, journals, generators, touch dice, sheet export/share and native media commands. No Ollama, cloud AI, account or runtime server required by the packaged apps.

**EF Alpha Races is original work in progress by Quest LLC / quest.rasht. Artwork by Mopodraws.** EF content/artwork: CC BY 4.0, as authorized by the project owner. Preserve both credits and indicate adaptations. See ATTRIBUTION.md and content/EF-LICENSE.md.

Application code remains under this repository's existing Unlicense. SRD 5.1 and SRD 5.2.1 are separately licensed CC BY 4.0. PDF.js/Electron retain their own licenses and dependency notices. No commercial rulebook PDFs, extracted commercial-book text/images, personal campaigns, device paths, personal support contacts, signing keys or passwords are published.

## Run

The full release source ZIP includes ready-to-open `app/DMOS.html`, licensed PDFs and the local PDF viewer. Open that file for browser use; native features require a native package. Export backups before changing browser/origin.

Git checkouts omit generated indexes and binary dependencies. Prepare them with Node 22+, Python 3.11+ and PowerShell:

```powershell
python -m pip install -r requirements.txt
python scripts/prepare_content.py --download
node scripts/prepare-viewer.cjs
node scripts/assemble.cjs
node scripts/serve.cjs
```

Then open the printed localhost URL. Initial preparation downloads the official SRDs, this project's EF release PDF and PDF.js. The resulting app operates offline. Alternatively supply an already downloaded EF PDF with `--ef-pdf PATH`.

## Build

Windows: `node scripts/package-windows.cjs` retrieves and verifies pinned Electron, compiles the C# media helper and builds `dist/Windows/DMOS.exe`. Requires Windows x64, PowerShell and the .NET Framework C# compiler. Inno Setup 6.7+ can compile `native/windows/installer.iss` for an installer.

Android requires JDK 17+, Android SDK platform 36 and build-tools 35.0.0:

```powershell
./scripts/build-android.ps1 -SdkRoot YOUR_SDK -JavaHome YOUR_JDK -Keystore YOUR_KEYSTORE -Alias YOUR_ALIAS -PasswordEnvironmentVariable DMOS_SIGNING_PASSWORD
```

Set the named password environment variable locally. Add `-Bundletool PATH_TO_JAR` for an AAB. Maintainer signing keys are intentionally absent. See script parameters. Build tooling needs network access only when downloading dependencies.

Run `node --test tests/*.test.cjs` and `python scripts/audit_release.py` before publication. See docs/RELEASE-AUDIT.md for testing limits.

## Privacy and support

Fresh installs begin empty. The optional Lantern Road sample is fictional and loaded only on request. Data stays in local app storage; exports/shared copies remain where the user sends them. Exports are not encrypted. Android has no INTERNET permission. Windows blocks external renderer requests/navigation. Media controls send standard commands to the active music player; not every player supports them. No notification-reading access.

Use GitHub issues for support. Never post private campaigns, credentials or keys. Windows sheet sharing copies readable text to the clipboard; Android uses the OS share chooser for HTML attachments. Native sheet printing supports PDF save through the desktop/native print workflow.

## Why the original private edition is not distributed

The private Windows/Android builds already exist. Public release was blocked by bundled commercial books and private starter data, not by the ability to finish the app. The SRD's Creative Commons license does not cover the complete commercial books. Wizards' Fan Content Policy excludes verbatim book redistribution even for free. The separate third-party guide has no verified redistribution grant; its compatibility dataset is excluded too. EF content and SRDs provide a shareable alternative.

Google Play separately needs a verified developer account, testing, listing declarations and review. GitHub release does not complete those steps. Physical Android and external-music-player testing remain necessary.

References: [official SRD](https://www.dndbeyond.com/srd), [Fan Content Policy](https://company.wizards.com/en/legal/fancontentpolicy).
