import sys,os,zipfile,shutil
build,assets=sys.argv[1:]
with zipfile.ZipFile(build+'/base.apk') as src,zipfile.ZipFile(build+'/repacked.apk','w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as dst:
 for item in src.infolist():
  with src.open(item) as a,dst.open(item,'w') as b:shutil.copyfileobj(a,b)
 dst.write(build+'/dex/classes.dex','classes.dex')
 for folder,dirs,files in os.walk(assets):
  for name in files:
   p=os.path.join(folder,name);dst.write(p,'assets/'+os.path.relpath(p,assets).replace(os.sep,'/'),compress_type=zipfile.ZIP_STORED if name.lower().endswith(('.pdf','.wasm')) else zipfile.ZIP_DEFLATED)
print('Repacked APK:',build)
