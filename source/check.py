from pathlib import Path
from html.parser import HTMLParser
import re,hashlib,json
root=Path('product portfolio');errors=[]
class Links(HTMLParser):
 def handle_starttag(self,tag,attrs):
  for key,v in attrs:
   if key not in ('src','href') or not v or v.startswith(('#','https:','http:','mailto:','tel:')):continue
   if not (root/v.split('#')[0]).exists():errors.append(str(current)+': '+v)
for current in root.glob('*.html'):Links().feed(current.read_text(encoding='utf-8'))
for f in ['index.html','styles.css','script.js']:
 assert (root/f).read_bytes()==Path(f).read_bytes(),f+' differs'
for f in ['xflare','harma','mobile-infirmary','prodesign']: assert (root/(f+'.html')).exists()
for f in ['commencium','teddy','metuvation','fintech']: assert not (root/(f+'.html')).exists()
print(json.dumps({'broken_local_links':errors,'preserved_files':['index.html','styles.css','script.js'],'new_case_studies':4},indent=2))
assert not errors
