import hashlib,json,pathlib,re,sys
ROOT=pathlib.Path(__file__).resolve().parent.parent
SECRET_EXT={'.p12','.pfx','.jks','.keystore','.key','.pem','.env'}
# Personal audit markers belong in an external, unpublished JSON array.
# Keep generic path/key checks in the distributable scanner.
import os
PRIVATE=[('C:'+chr(92)+'Users'+chr(92)),('C:/'+ 'Users/'),('BEGIN '+'PRIVATE KEY'),('BEGIN '+'RSA PRIVATE KEY')]
if os.environ.get('DMOS_PRIVATE_MARKERS_FILE'):
 marker_path=pathlib.Path(os.environ['DMOS_PRIVATE_MARKERS_FILE']).resolve()
 if marker_path.is_relative_to(ROOT.resolve()):raise RuntimeError('Keep private marker configuration outside the published source tree.')
 markers=json.loads(marker_path.read_text(encoding='utf-8-sig'))
 if not isinstance(markers,list) or len(markers)>1000 or any(not isinstance(x,str) or not x or len(x)>1000 for x in markers):raise RuntimeError('Private marker configuration must be an array of nonempty strings.')
 PRIVATE+=markers
SKIP_PARTS={'dist','.git','node_modules','__pycache__'}
def sha(p):
 h=hashlib.sha256()
 with p.open('rb') as f:
  for chunk in iter(lambda:f.read(1048576),b''):h.update(chunk)
 return h.hexdigest()
errors=[];checked=0
for p in ROOT.rglob('*'):
 if not p.is_file() or any(part in SKIP_PARTS for part in p.relative_to(ROOT).parts):continue
 rel=p.relative_to(ROOT).as_posix();checked+=1
 if p.suffix.lower() in SECRET_EXT or p.name.lower().startswith('.env'):errors.append('Disallowed secret file: '+rel)
 if p.name in ['party-data.js','compatibility-data.js'] or '/Imports/' in '/'+rel:errors.append('Excluded data file: '+rel)
 if p.suffix.lower() in {'.js','.cjs','.mjs','.json','.html','.md','.txt','.py','.ps1','.java','.cs','.yml','.yaml','.iss'}:
  text=p.read_text(encoding='utf-8-sig',errors='replace')
  for token in PRIVATE:
   if token.lower() in text.lower():errors.append('Private marker in '+rel)
  if re.search(r'(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|AKIA[A-Z0-9]{16})',text):errors.append('Credential pattern in '+rel)
  if re.search(r'DMOS_STARTER\s*=',text):errors.append('Bundled starter assignment: '+rel)
specs=json.loads((ROOT/'content/sources.json').read_text(encoding='utf-8-sig'))
allowed={s['file'] for s in specs}
for p in (ROOT/'app').rglob('*.pdf'):
 if p.relative_to(ROOT/'app').as_posix() not in allowed:errors.append('Unapproved PDF')
for s in specs:
 p=ROOT/'app'/s['file']
 if p.exists() and sha(p)!=s['sha256']:errors.append('Content hash mismatch: '+s['file'])
for marker in ['Quest LLC / quest.rasht','Mopodraws','CC BY 4.0']:
 if marker not in (ROOT/'ATTRIBUTION.md').read_text(encoding='utf-8-sig'):errors.append('Missing credit: '+marker)
if errors:
 print('\n'.join(errors));sys.exit(1)
print('Release privacy/content audit passed:',checked,'files; approved PDFs:',len(specs))
