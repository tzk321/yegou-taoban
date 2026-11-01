"""Twelve reachable vector postcards. No embedded raster, filler, or duplicated frames.
Each location has its own architecture, perspective, palette, street objects and people.
The detail belongs to the gallery, not the gameplay render loop.
"""
import random, math
from pathlib import Path
P=Path(__file__).parent
COLORS=[('#071327','#183848','#efbda0'),('#101733','#305269','#e794be'),('#142338','#31594e','#f4d38d'),('#181c36','#484a60','#d6c7a1'),('#152532','#3a5964','#d8b07d'),('#12162a','#34435d','#afd3ef'),('#142332','#40576a','#e9c69a'),('#142146','#414361','#d6c5fc'),('#162c45','#597577','#f2c799'),('#14212f','#3b5660','#e4b985'),('#162341','#436879','#badfe5'),('#263449','#9c8981','#ffe0b0')]
TITLE=['雨夜门口','凌晨骑楼','冰美式窗口','旧书铺','机修棚','地铁末班','高架底下','屋顶电台','邕江南岸','码头仓库','纸鲸灯会','天亮早市']
parts=[];out=[];R=None

def add(s): out.append(s)
def rect(x,y,w,h,c,rx=0,stroke=None,op=1):
 add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{c}"'+(f' stroke="{stroke}"' if stroke else '')+(f' opacity="{op}"' if op!=1 else '')+'/>')
def path(d,c='none',s=None,sw=1,op=1):
 add(f'<path d="{d}" fill="{c}"'+(f' stroke="{s}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"' if s else '')+(f' opacity="{op}"' if op!=1 else '')+'/>')
def circle(x,y,r,c,s=None,op=1):
 add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{c}"'+(f' stroke="{s}"' if s else '')+(f' opacity="{op}"' if op!=1 else '')+'/>')
def text(x,y,s,size=14,c='#cce3d9'):
 add(f'<text x="{x}" y="{y}" fill="{c}" font-size="{size}" font-family="system-ui,sans-serif">{s}</text>')
def building(x,y,w,h,style=0):
 cs=['#203448','#243e50','#294352','#31495c','#1c3040'];rect(x,y,w,h,cs[style%5]);rect(x+w-8,y+8,8,h-8,'#132538')
 for yy in range(int(y+16),int(y+h-12),22):
  for xx in range(int(x+10),int(x+w-12),17):
   col=R.choice(['#638485','#779693','#9aad99','#efc28a','#354c60','#47616c']);rect(xx,yy,9,13,col,1,op=R.choice([.3,.5,.7]))
 path(f'M{x:.1f} {y:.1f}h{w:.1f}M{x+w-8:.1f} {y+8:.1f}v{h-8:.1f}',s='#718a92',op=.35)
 if style%3==0:path(f'M{x+8:.1f} {y:.1f}v-17h{w-16:.1f}v17',s='#637b86',sw=2)
def person(x,y,scale=1,coat='#78a8a5',pose=0):
 add(f'<g transform="translate({x:.1f},{y:.1f}) scale({scale:.2f})">');circle(0,-36,5,'#c5b5a2');path('M-6-29Q0-34 6-29L9-10H-9Z',coat,s='#10263a');path('M-4-9L-6 5M4-9L9 4',s='#0e1e2e',sw=4);path('M-7-25L-13-11M7-25L16-16',s=coat,sw=3)
 if pose%3==0:path('M-26-41Q0-65 26-41Z',R.choice(['#6da59b','#b48896','#baab85']),s='#c5cdb8');path('M0-44V-17q0 9 7 5',s='#d9ccb0',sw=1.5)
 elif pose%3==1:rect(13,-21,10,16,'#ccb37d',2);path('M14-21q5-9 8 0',s='#d8c89f')
 add('</g>')
def tree(x,y,s=1):
 add(f'<g transform="translate({x},{y}) scale({s})">');path('M0 0L-4-85L7-86L9 0Z','#334448');path('M2-45L-34-107M3-65L30-122M2-78L-5-148',s='#485950',sw=5)
 for i in range(100):
  xx=R.gauss(0,31);yy=R.gauss(-117,20);a=R.uniform(-60,60);col=R.choice(['#375b57','#3c6860','#447366','#557f6e','#749485']);add(f'<path d="M-4 0Q-2-8 6-9Q9-2 0 3Z" fill="{col}" transform="translate({xx:.1f},{yy:.1f}) rotate({a:.1f})" opacity="{R.uniform(.5,.9):.2f}"/>')
 add('</g>')
def lamp(x,y,c='#e0c18e'):
 path(f'M{x} {y}v-151q0-12 14-12h21',s='#6d8787',sw=4);rect(x+26,y-170,26,11,c,3);path(f'M{x+30} {y-156}l-68 147h164l-78-147Z',c,op=.035)
def sign(x,y,w,label,c='#e6c391'):
 rect(x,y,w,34,'#162e3f',4,stroke=c);text(x+11,y+24,label,17,c)
def shelf(x,y,w,rows=5):
 rect(x,y,w,rows*26+10,'#172938',2)
 for row in range(rows):
  xx=x+5
  while xx<x+w-8:
   bw=R.randint(5,11);bh=R.randint(16,24);col=R.choice(['#997588','#7d9a93','#b6a87f','#6f8b9f','#c3b595']);rect(xx,y+row*26+26-bh,bw,bh,col,1);path(f'M{xx+2} {y+row*26+8}v10',s='#e6dec4',op=.4);xx+=bw+2
  path(f'M{x} {y+(row+1)*26+2}h{w}',s='#a79d81',sw=2)
def crate(x,y,w=47,h=33,c='#536564'):
 rect(x,y,w,h,c,2,stroke='#7e8e83');path(f'M{x+3} {y+3}l{w-6} {h-6}M{x+w-3} {y+3}l-{w-6} {h-6}',s='#aab39b',sw=1.2,op=.6);path(f'M{x+5} {y+7}h{w-10}',s='#d3c9a4',op=.6)
def paperwhale(x,y,s=1,c='#bfe8dc'):
 add(f'<g transform="translate({x},{y}) scale({s})">');path('M-102 0Q-99-50-45-52Q19-56 61-21L99-44L91-13L113 17L67 4Q42 39-16 31Q-69 31-102 0Z',c,s='#a2cfcc',sw=2);path('M-102 0L-27-9L67 4M-45-52L-27-9L-16 31M-27-9L19-41M-16 31L5-3M61-21L67 4L91-13',s='#6cabb2',sw=1.5);circle(-64,-20,3,'#356576');add('</g>')
for idx in range(12):
 R=random.Random(546603+idx*971);out=[];sky,wall,light=COLORS[idx]
 add(f'<symbol id="postcard{idx}" viewBox="0 0 800 480"><title>{TITLE[idx]} / 纯矢量夜游明信片</title>');rect(0,0,800,480,sky)
 # Sky points are composed constellations; varying each location's moon position.
 for n in range(32):circle(R.uniform(12,788),R.uniform(12,132),R.uniform(.6,1.4),'#cee3dd',op=.35)
 circle(650 if idx%2==0 else 160,55,26,'#ead6b6',op=.55);circle(658 if idx%2==0 else 169,48,25,sky)
 for x in range(-20,801,52):building(x,R.randint(107,185),R.randint(43,67),R.randint(92,172),idx+x//52)
 rect(0,300,800,180,'#142d3a');path('M0 369Q220 360 415 373T800 365V480H0Z','#192e3b')
 # Wet perspective paving and reflected shop lights, every mark has a scene position.
 for y in range(375,480,16):path(f'M0 {y}H800',s='#446264',op=.18)
 for x in range(-600,1500,90):path(f'M400 300L{x} 480',s='#3c5860',op=.2)
 for i in range(76):
  x=R.uniform(0,800);y=R.uniform(354,475);w=R.uniform(3,40);path(f'M{x:.1f} {y:.1f}h{w:.1f}',s=R.choice([light,'#74adab','#83a6b3']),sw=R.uniform(.6,1.8),op=R.choice([.15,.22,.3]))
 if idx==0:
  rect(32,174,328,181,wall);rect(65,218,79,137,'#0b1f2e');rect(179,216,120,74,'#628381',3);path('M238 216v74M179 252h120',s='#d1c5a3',sw=3);sign(70,167,172,'不返工 / EXIT');rect(150,284,16,21,'#559a91',2);circle(157,292,2,'#b8e6cf');path('M32 211H360M32 319H360',s='#689193',sw=2);tree(420,359,.91);tree(714,359,1.23);lamp(522,366);person(285,380,1.5,'#d6af63');crate(18,340,42,30);text(185,333,'门禁 / 已下线',12)
 elif idx==1:
  for j in range(5):
   x=18+j*155;rect(x,178,145,159,wall);rect(x+13,190,119,48,'#5d7779');path(f'M{x+70} 191v45M{x+14} 214h118',s='#a7b7aa',sw=2);path(f'M{x+8} 336V284Q{x+73} 221 {x+137} 284V336Z','#102536',s='#87948a',sw=3);rect(x+9,281,16,91,'#688389');rect(x+121,281,16,91,'#688389');sign(x+22,243,104,['夜游','花店','唱片','无米','不催'][j],light)
  path('M0 173H800M0 340H800',s='#a4a499',sw=4);person(245,379,1.3,'#98b59b');person(597,389,1.5,'#a383a7',1);tree(62,406,.65);tree(741,391,.71)
 elif idx==2:
  rect(85,160,441,198,wall);rect(130,236,298,104,'#0d2430');sign(156,169,248,'02:17 冰美式',light);rect(117,222,330,16,'#bbab82',2);path('M118 221l18-43h291l21 43Z','#68988c');rect(137,311,288,15,'#bca681');shelf(143,244,75,2)
  for k in range(7):rect(244+k*22,278,13,27,R.choice(['#c9dbc0','#c6ab8d','#80b4ac']),2);rect(242+k*22,274,17,5,'#e9e4c6',1)
  person(379,312,1.13,'#9ac2b6',2);person(506,386,1.6,'#d4b270');person(570,395,1.2,'#b98a8f');tree(687,381,1.1);lamp(45,376);crate(104,341,51,35);text(218,347,'不加糖 / 今夜照常',13)
 elif idx==3:
  rect(76,159,540,204,wall);sign(181,174,252,'未读旧书 / OPEN','#d6c9a2');shelf(104,230,143,5);shelf(294,230,134,5);shelf(482,230,105,5);rect(258,222,24,141,'#162937');rect(445,222,23,141,'#162937');path('M96 219H596',s='#b8b397',sw=4);person(637,392,1.4,'#96aaa1',1);person(208,382,1.35,'#b19786',1);tree(702,378,.95);lamp(42,378)
 elif idx==4:
  rect(65,160,558,194,wall);path('M46 171L96 136H587L648 171Z','#65726e',s='#9aa399',sw=2);sign(201,176,236,'野狗机修 / 不接催单');rect(103,228,478,123,'#162a35')
  for k in range(8):path(f'M{118+k*56} 230v112',s='#506c72',sw=2)
  for k in range(14):
   x=R.randint(132,540);y=R.randint(240,290);path(f'M{x} {y}v20m-5-24l5 4 5-4',s='#a9bbb0',sw=2)
  for x in [202,365,530]:circle(x,342,23,'#10202a',s='#8fa6a0');circle(x,342,13,'none',s='#b0bbaa');path(f'M{x-15} 315l15-19 36 42h-51l15-23m0-19h12',s='#a39c77',sw=3)
  person(455,354,1.2,'#6c918c',2);tree(716,386,1.04);lamp(38,380);crate(94,344,51,36)
 elif idx==5:
  rect(36,186,736,128,'#263f53');rect(63,215,680,64,'#617e87',4)
  for j in range(9):
   x=75+j*74;rect(x,221,55,47,'#132a3d',3);rect(x+6,226,43,4,'#839b9a',1,op=.5);path(f'M{x+28} 222v44',s='#658389',sw=2)
  rect(160,208,43,97,'#506b76');rect(602,208,43,97,'#506b76');path('M36 298H772',s='#b7a788',sw=3);path('M0 327H800M0 337H800',s='#adc3b9',sw=2);sign(335,115,231,'末班 / 仍然到站','#bcd2df');path('M65 130H755M65 130V322M755 130V322',s='#7f979d',sw=4);person(203,374,1.4,'#9daeb0',1);person(553,374,1.4,'#ac8699');person(679,381,1.1,'#b5a679',1);lamp(39,390)
 elif idx==6:
  path('M-30 174Q330 140 830 182V241Q345 200-30 246Z','#4c626f',s='#8fa3a9',sw=2);path('M-20 175Q330 143 820 184M-20 217Q355 173 820 227',s='#b0b7a8',sw=3);path('M210 231L187 357H232L249 225ZM621 230L638 366H682L660 234Z','#667c7f');path('M0 389Q265 305 800 385',s='#c1b698',sw=3);tree(84,370,.75);tree(730,378,.85);person(338,396,1.5,'#cfae72');person(539,384,1.17,'#8cafaf',1);lamp(459,375)
  for i in range(8):path(f'M{40+i*93} {411+i%2*17}l51-5',s='#c0c9b6',sw=2,op=.4)
 elif idx==7:
  rect(31,296,737,87,wall);path('M23 296H778',s='#9a9cb0',sw=5);path('M42 285H759M50 258V285M184 258V285M315 258V285M447 258V285M581 258V285M749 258V285',s='#789195',sw=2);rect(493,237,99,59,'#4b6470',3,stroke='#8faca7');circle(517,266,17,'#243d52',s='#a6b7ac');circle(569,264,8,'#afc4ad');path('M505 249l-7-13m27 13 8-13M592 240L630 209',s='#c6c5b0',sw=2);path('M174 285V93m-28 12h56m-50 29h43m-36 28h31',s='#8fa1a3',sw=3);path('M174 97l-52 160M174 97l65 160',s='#607d88',sw=1.5);person(460,321,1.23,'#baa885',2);tree(730,366,.64);sign(275,321,201,'02:17 / FM FREE','#c5c1e8')
 elif idx==8:
  rect(0,295,800,121,'#3c646d');path('M-30 245Q230 86 431 245T830 245',s='#c2b9a3',sw=5);path('M0 251H800M0 264H800',s='#829e9c',sw=4)
  for x in range(10,800,33):path(f'M{x} 252V{R.randint(168,248)}',s='#a7b9ac',sw=1.2,op=.6)
  for i in range(91):
   xx=R.uniform(0,800);yy=R.uniform(303,411);path(f'M{xx:.1f} {yy:.1f}h{R.uniform(4,35):.1f}',s=R.choice(['#d8c398','#91bab8','#779dba']),op=.35)
  path('M0 409Q246 385 800 413V480H0Z','#29434b');path('M0 407Q246 383 800 411',s='#b3b79c',sw=3);tree(87,452,1.28);tree(714,443,1.12);person(420,438,1.32,'#d5ba76');paperwhale(525,179,.39)
 elif idx==9:
  for k in range(3):
   x=30+k*250;rect(x,190,224,147,wall);path(f'M{x-10} 190l40-42h164l31 42Z','#576f75',s='#8ba2a1',sw=2);rect(x+47,234,131,104,'#1b3443')
   for j in range(5):path(f'M{x+49} {238+j*19}h127',s='#52707b',sw=2)
  path('M542 190V71H718M575 71L697 167M575 71v118M575 112h42M575 149h81M709 73v128',s='#a5ac91',sw=4);path('M698 201q10 23 24 0',s='#d5c49e',sw=3)
  for j in range(12):crate(55+(j%6)*64,324+(j//6)*40,56,35,R.choice(['#677974','#5b6c6b','#7e7d68']))
  person(477,390,1.31,'#aab5a1',1);tree(736,423,.83);lamp(25,423);sign(324,202,184,'不催 / 夜仓')
 elif idx==10:
  path('M0 147Q400 245 800 151',s='#829d96',sw=2)
  for k in range(13):
   x=15+k*63;yy=174+math.sin(k/12*math.pi)*46;path(f'M{x} {yy-22}v27',s='#b7c6b8');circle(x,yy+11,13,R.choice(['#b7dcd0','#ddbaa3','#aca3d0']),s='#dde4c4',op=.85);path(f'M{x-7} {yy+24}h14m-7 0v11',s='#b1c3b0',sw=2)
  for k in range(4):paperwhale(116+k*177,271+(k%2)*12,.49,R.choice(['#a5d7d2','#c5dcd3','#b7cfdf']))
  path('M0 358H800M0 366H800',s='#9ab7ae',sw=3);person(148,409,1.4,'#b4a28a');person(345,412,1.2,'#92b6b2',1);person(522,402,1.15,'#af99b4');tree(53,421,.83);tree(740,426,.83)
 elif idx==11:
  rect(0,0,800,88,'#c7a297',op=.15)
  for k in range(6):
   x=12+k*131;path(f'M{x} 228l17-33h89l20 33Z',R.choice(['#bc9c79','#98b6a4','#b8a799']),s='#d2c5aa');path(f'M{x+12} 228v130M{x+121} 228v130',s='#8a9d91',sw=3);rect(x+10,290,114,52,'#667e76',2);crate(x+17,310,35,29);crate(x+73,309,35,30)
   for j in range(9):circle(x+R.uniform(19,108),R.uniform(280,290),R.uniform(3,5),R.choice(['#b7c592','#dfb183','#aaca9c','#d4c8a4']))
   person(x+70,285,.85,R.choice(['#93ad9d','#ac9485','#aaa990']),2)
  person(88,399,1.4,'#d2b589',1);person(564,395,1.35,'#8eb2a7',1);person(328,384,1.12,'#b7a397');tree(751,432,.84);sign(285,122,217,'早市 / 天亮了','#e8ce9e')
 # Foreground planting and small life: different leaf forms and colors at each location.
 for side in range(2):
  x0=12 if side==0 else 744
  rect(x0,422,46,44,'#354c52',4,stroke='#728b82')
  for n in range(80):
   x=x0+R.uniform(-8,50);y=R.uniform(384,428);col=R.choice(['#597c68','#6e9276','#7eaa88','#819b78']);path(f'M{x:.1f} {y:.1f}q-9-16-2-23q13 4 9 19Z',col,op=.75)
 # Draped wires and distinct rain streaks, not full-screen overdraw.
 path(f'M-20 {92+idx*3}Q340 {137+idx*2} 820 {71+idx*2}',s='#82959a',sw=1.2,op=.5)
 for i in range(23):
  x=R.uniform(20,780);y=R.uniform(30,390);path(f'M{x:.1f} {y:.1f}l-3 11',s='#bfd1d0',op=.18)
 # Close street placard: legible authorial micro-story and visual serial.
 rect(548,440,169,24,'#0a2332',4,stroke='#617c80');text(561,457,'夜游 '+str(idx+1).zfill(2)+' / 不返工',12,'#bacdb9')
 path('M8 8H792V472H8Z',s='#82a3a2',sw=1.5,op=.45)
 add('</symbol>');parts.append(''.join(out))
(P/'arcade-art.svgfrag').write_text('\n'.join(parts))
print('postcard vector bytes',sum(len(s.encode()) for s in parts),[len(s.encode()) for s in parts])
