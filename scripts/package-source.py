import pathlib,zipfile,json,hashlib
root=pathlib.Path(__file__).resolve().parent.parent
release=json.loads((root/'release.json').read_text(encoding='utf-8-sig'));version=release['version'];dist=root/'dist';dist.mkdir(exist_ok=True)
out=dist/f'DMOS-OpenSource-{version}-Source.zip'
with zipfile.ZipFile(out,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for p in root.rglob('*'):
  if not p.is_file() or any(x in {'dist','.git','node_modules','__pycache__'} for x in p.relative_to(root).parts):continue
  z.write(p,'DMOS-OpenSource/'+p.relative_to(root).as_posix())
files=[dist/f'DMOS-OpenSource-{version}{suffix}' for suffix in ['-Windows-Setup.exe','.apk','.aab','-Source.zip']]
rows=[];downloads={}
for p in files:
 if not p.exists():raise RuntimeError('Missing built artifact: '+p.name)
 h=hashlib.sha256()
 with p.open('rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 digest=h.hexdigest();rows.append(digest+'  '+p.name)
 downloads[p.name]={'url':release['repository']+'/releases/download/'+release['releaseTag']+'/'+p.name,'sha256':digest,'size':p.stat().st_size}
manifest={'version':version,'androidVersionCode':release['androidVersionCode'],'schemaVersion':release['schemaVersion'],'channel':release['channel'],'automaticInstall':False,'releaseUrl':release['repository']+'/releases/tag/'+release['releaseTag'],'downloads':downloads}
(dist/'update-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
rows.append(hashlib.sha256((dist/'update-manifest.json').read_bytes()).hexdigest()+'  update-manifest.json')
(dist/'SHA256SUMS.txt').write_text('\n'.join(rows)+'\n')
print('Packaged source, update manifest and checksums for',version)
