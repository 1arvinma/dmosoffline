import argparse,hashlib,json,pathlib,shutil,urllib.request
from pypdf import PdfReader
ROOT=pathlib.Path(__file__).resolve().parent.parent

def digest(path):
 h=hashlib.sha256()
 with open(path,'rb') as f:
  for b in iter(lambda:f.read(1048576),b''):h.update(b)
 return h.hexdigest()

def prepare(download=False,ef_pdf=None):
 assets=ROOT/'app';books=assets/'Books';books.mkdir(exist_ok=True)
 specs=json.loads((ROOT/'content/sources.json').read_text(encoding='utf-8-sig'))
 entries=[]
 for spec in specs:
  dest=assets/spec['file']
  if spec['id']=='book-oracle-alpha' and ef_pdf:shutil.copyfile(ef_pdf,dest)
  if not dest.exists():
   if not download:raise RuntimeError('Missing content: '+spec['file']+'; run with --download or supply --ef-pdf')
   with urllib.request.urlopen(spec['url']) as source,dest.open('wb') as out:shutil.copyfileobj(source,out)
  if digest(dest)!=spec['sha256']:raise RuntimeError('Content checksum mismatch: '+spec['file'])
  if spec['id']=='book-oracle-alpha':
   entry=json.loads((ROOT/'content/ef-alpha-index.json').read_text(encoding='utf-8-sig'))
   # Preview images are optional for Git builds; the original PDF is always present.
   if not (assets/'art/ef-alpha/1.jpg').exists():entry.pop('images',None)
  else:
   reader=PdfReader(dest);entry={k:spec[k] for k in ['id','title','file','edition','kind']}
   entry.update(pages=[p.extract_text() or '' for p in reader.pages],pageCount=len(reader.pages),searchablePages=len(reader.pages),errors=[],indexMethod='pypdf extraction from the openly licensed original PDF')
  entries.append(entry)
 (assets/'book-data.js').write_text('window.DMOS_BOOKS='+json.dumps({'books':entries},ensure_ascii=False,separators=(',',':'))+';',encoding='utf-8')
 (assets/'book-manifest.json').write_text(json.dumps({'version':1,'localOnly':True,'books':specs},indent=2),encoding='utf-8')
 print('Prepared licensed content:',', '.join(s['title'] for s in specs))

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--download',action='store_true');p.add_argument('--ef-pdf');args=p.parse_args();prepare(args.download,args.ef_pdf)
