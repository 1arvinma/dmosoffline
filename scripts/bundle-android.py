import sys,os,zipfile
build,assets=sys.argv[1:]
with zipfile.ZipFile(build+'/proto.apk') as src,zipfile.ZipFile(build+'/module.zip','w',compression=zipfile.ZIP_DEFLATED) as dst:
 for n in src.namelist():
  dst.writestr('manifest/AndroidManifest.xml' if n=='AndroidManifest.xml' else n,src.read(n))
 dst.write(build+'/dex/classes.dex','dex/classes.dex')
 for folder,dirs,files in os.walk(assets):
  for name in files:
   p=os.path.join(folder,name);dst.write(p,'assets/'+os.path.relpath(p,assets).replace(os.sep,'/'))
