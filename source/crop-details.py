from pathlib import Path
import pypdfium2 as p
root=Path('product portfolio'); d=p.PdfDocument(str(root/'source/portfolio-print.pdf'))
crops=[(8,'technical-watch',(.03,.28,.225,.8)),(8,'technical-controller',(.225,.29,.48,.81)),(8,'exploded-watch',(.48,.13,.70,.43)),(8,'exploded-controller',(.71,.1,.98,.44)),(8,'system-diagram',(.53,.56,.98,.97)),(16,'route-map',(.66,.54,.865,.80)),(15,'field-observations',(.02,.48,.98,.95))]
for n,name,box in crops:
 im=d[n-1].render(scale=3).to_pil().convert('RGB');w,h=im.size;im=im.crop(tuple(int(v*(w if k%2==0 else h)) for k,v in enumerate(box)));im.thumbnail((2000,2000));im.save(root/f'assets/{name}.webp',lossless=True)
for n,kind,boxes in [(21,'stroller',[(.052,.40,.334,.645),(.362,.40,.635,.645),(.67,.40,.943,.645),(.052,.693,.334,.937),(.362,.693,.635,.937),(.67,.693,.943,.937)]),(22,'luggage',[(.185,.387,.489,.659),(.514,.387,.812,.659),(.185,.675,.489,.958),(.514,.675,.812,.958)])]:
 im=d[n-1].render(scale=3).to_pil().convert('RGB');w,h=im.size
 for i,box in enumerate(boxes):
  tile=im.crop(tuple(int(v*(w if k%2==0 else h)) for k,v in enumerate(box)));tile.thumbnail((1400,1400));tile.save(root/f'assets/{kind}-{i+1}.webp',lossless=True)
print('Technical and scenario illustrations prepared.')
