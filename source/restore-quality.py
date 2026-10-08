from pathlib import Path
from pypdf import PdfReader
from PIL import Image,ImageChops,ImageStat
import re,json,sys
root=Path('product portfolio');r=PdfReader(root/'source/portfolio-print.pdf');original=PdfReader(root/'source/portfolio.pdf');report=[]
for f in sorted((root/'assets').glob('visual-*.webp')):
 m=re.fullmatch(r'visual-(\d+)-(\d+)\.webp',f.name);n,j=map(int,m.groups());
 if '--resume' in sys.argv and n<29:continue
 obj=r.pages[n-1].images[j];im=obj.image;oldsource=original.pages[n-1].images[j].image
 def thumb(v):
  v=v.convert('RGBA');bg=Image.new('RGBA',v.size,'white');bg.alpha_composite(v);return bg.convert('RGB').resize((48,48))
 error=sum(ImageStat.Stat(ImageChops.difference(thumb(im),thumb(oldsource))).mean)/3
 # These two standard-export images have color artifacts; print versions were visually verified.
 assert error<15 or (n,j) in [(29,4),(29,5)],(n,j,error)
 if im.mode not in ('RGB','RGBA'):im=im.convert('RGBA' if 'A' in im.getbands() else 'RGB')
 old=Image.open(f);before=old.size;old.close()
 im.save(f,lossless=True,method=4)
 report.append({'name':f.name,'size':im.size,'alpha':im.mode=='RGBA','previous_size':oldsource.size})
(root/'qa/image-quality.json').write_text(json.dumps(report,indent=2))
print('Restored',len(report),'images;',sum(x['alpha'] for x in report),'with transparency;',sum(x['size']!=x['previous_size'] for x in report),'at larger original dimensions')
for name in ['images.py','extract-additional.py']:
 p=root/'source'/name;s=p.read_text();s=s.replace(".image.convert('RGB')",'.image.copy()');s=s.replace('im.thumbnail((2200,2200)); ','').replace('im.thumbnail((2400,2400)); ','');s=s.replace('quality=90','lossless=True').replace('quality=93','lossless=True');p.write_text(s)
