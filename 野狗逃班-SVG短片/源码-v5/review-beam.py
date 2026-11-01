from pathlib import Path
from PIL import Image
import json
R=Path(__file__).parent/'night-off-out'
results=[]
for f in ['v4-boss-low-beam-desktop.png','v4-boss-high-beam-desktop.png','v4-boss-beam-mobile.png','v4-dash-desktop.png','v4-shop-mobile.png']:
 if not (R/f).exists(): continue
 im=Image.open(R/f).convert('RGB');w,h=im.size
 bright=[(x,y) for y in range(int(h*.28),int(h*.70)) for x in range(w) if min(im.getpixel((x,y)))>170 and max(im.getpixel((x,y)))-min(im.getpixel((x,y)))<95]
 rows={y:0 for y in range(int(h*.28),int(h*.70))}
 for x,y in bright:rows[y]+=1
 top=sorted(rows.items(),key=lambda v:v[1],reverse=True)[:6]
 results.append({'file':f,'size':[w,h],'bright_rows':top,'bright_pixels':len(bright)})
print(json.dumps(results,ensure_ascii=False,indent=2))
