from pathlib import Path
from pypdf import PdfReader
from PIL import Image,ImageOps,ImageDraw
root=Path('product portfolio');r=PdfReader(root/'source/portfolio-print.pdf');tiles=[]
for n in [3,6,8,14,15,16,21,22,25,27,29,31]:
 for j,o in enumerate(r.pages[n-1].images):
  im=o.image.copy()
  if min(im.size)<140 or im.width*im.height<60000:continue
  name=f'visual-{n:02}-{j:02}'; im.save(root/f'assets/{name}.webp',lossless=True)
  t=Image.new('RGB',(300,225),'#eef0f3');th=ImageOps.contain(im,(290,190));t.paste(th,((300-th.width)//2,30));ImageDraw.Draw(t).text((8,7),name,fill='black');tiles.append(t)
for start in range(0,len(tiles),20):
 sheet=Image.new('RGB',(1500,900),'white')
 for j,t in enumerate(tiles[start:start+20]):sheet.paste(t,((j%5)*300,(j//5)*225))
 sheet.save(root/f'qa/additional-{start//20+1}.jpg')
print(len(tiles))
