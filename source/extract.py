from pathlib import Path
import pypdfium2 as pdfium
from PIL import Image,ImageOps,ImageDraw
root=Path('product portfolio'); doc=pdfium.PdfDocument(str(root/'source/portfolio.pdf'))
thumbs=[]
for i,page in enumerate(doc):
    im=page.render(scale=1800/page.get_width()).to_pil().convert('RGB')
    im.save(root/f'assets/page-{i+1:02}.webp',quality=88)
    tile=Image.new('RGB',(310,245),'#e5e8ed'); small=ImageOps.contain(im,(300,213));tile.paste(small,((310-small.width)//2,24)); ImageDraw.Draw(tile).text((10,5),str(i+1),fill='black');thumbs.append(tile)
for offset in range(0,len(thumbs),15):
    sheet=Image.new('RGB',(1550,735),'white')
    for j,t in enumerate(thumbs[offset:offset+15]):sheet.paste(t,((j%5)*310,(j//5)*245))
    sheet.save(root/f'qa/contact-{offset//15+1}.jpg')
print('Rendered',len(thumbs),'pages')
