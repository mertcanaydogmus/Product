from pypdf import PdfReader
from pathlib import Path
from PIL import Image,ImageOps,ImageDraw
r=PdfReader('product portfolio/source/portfolio-print.pdf'); root=Path('product portfolio'); tiles=[]
for n in [2,4,5,7,9,10,12,13,17,18,19,20,24,26,28,30,32,33,34,36,37,38,39,40]:
    for j,obj in enumerate(r.pages[n-1].images):
        im=obj.image.copy()
        if min(im.size)<160 or im.width*im.height<90000:continue
        name=f'visual-{n:02}-{j:02}'
        im.save(root/f'assets/{name}.webp',lossless=True)
        t=Image.new('RGB',(240,190),'#eceef0'); th=ImageOps.contain(im,(230,158));t.paste(th,((240-th.width)//2,27));ImageDraw.Draw(t).text((7,6),f'{name} {im.width}x{im.height}',fill='black');tiles.append(t)
for start in range(0,len(tiles),30):
    out=Image.new('RGB',(1440,950),'white')
    for j,t in enumerate(tiles[start:start+30]):out.paste(t,((j%6)*240,(j//6)*190))
    out.save(root/f'qa/assets-{start//30+1}.jpg')
print('Extracted',len(tiles),'images')
