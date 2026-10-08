from pathlib import Path
import pypdfium2 as p
root=Path('product portfolio');doc=p.PdfDocument(str(root/'source/portfolio-print.pdf'));im=doc[4].render(scale=4).to_pil().convert('RGB');w,h=im.size
boxes=[(430,348,775,658),(780,348,1080,658),(1080,348,1390,658),(430,663,775,933),(780,663,1080,933),(1080,663,1390,933)]
for i,box in enumerate(boxes):
 tile=im.crop((int(box[0]/1800*w),int(box[1]/1276*h),int(box[2]/1800*w),int(box[3]/1276*h)));tile.save(root/f'assets/initial-transition-{i+1}.webp',lossless=True)
