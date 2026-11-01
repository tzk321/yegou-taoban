from pathlib import Path
P=Path(__file__).parent
out=[]
C=['#79b9ab','#b48ba6','#c5aa71','#a3997c','#9db8ad','#92b3cc','#aabdbb','#b6a3db','#8dd0c5','#b7ae8a','#b8dcd4','#e7caa5']
def path(d,f='none',s='#b9d9cd',w=2):return f'<path d="{d}" fill="{f}" stroke="{s}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"/>'
def rect(x,y,w,h,c,r=0):return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{c}"/>'
def circ(x,y,r,f,s='none',w=2):return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{f}" stroke="{s}" stroke-width="{w}"/>'
def txt(x,y,t,c='#c5ddd0',sz=18):return f'<text x="{x}" y="{y}" fill="{c}" font-size="{sz}" font-family="system-ui,sans-serif">{t}</text>'
for i in range(12):
 c=C[i];far='';mid='';front=''
 # Continuous 1280-unit modular geometry, rendered as moving pairs, not static postcards.
 for x in range(0,1280,160):
  h=110+(x//160*31+i*17)%100;far+=rect(x,320-h,132,h,'#193c51')
  for y in range(340-h,305,32):
   for xx in range(x+12,x+124,28):far+=rect(xx,y,12,16,c)
 if i==0:
  for x in range(0,1280,320):mid+=rect(x,200,282,327,'#214553')+rect(x+24,335,87,192,'#102634')+rect(x+134,326,115,87,c)+path(f'M{x+190} 326v87M{x+134} 369h115')+txt(x+28,293,'不返工 / EXIT',c,22)+rect(x+115,406,13,29,'#64cba9')
 elif i==1:
  for x in range(0,1280,256):mid+=rect(x,205,248,299,'#3c435e')+path(f'M{x+18} 507V355Q{x+122} 229 {x+230} 355V507Z','#112b3e',c,3)+rect(x+6,340,17,175,c)+rect(x+229,340,17,175,c)+rect(x+43,225,156,52,'#67818b')+txt(x+77,301,['夜游','唱片','花店','无米','不催'][x//256],c,21)
 elif i==2:
  for x in range(0,1280,426):mid+=rect(x,211,405,313,'#284d4c')+path(f'M{x+12} 330l35-64h292l52 64Z','#709788',c,3)+rect(x+27,333,325,170,'#122b37')+rect(x+30,460,321,20,'#c4af8c')+txt(x+79,246,'02:17 / 冰美式',c,22)
  for x in range(73,1280,39):mid+=rect(x,433,18,25,'#cddccb',3)+path(f'M{x-2} 428h22',s=c,w=3)
 elif i==3:
  for x in range(0,1280,320):
   mid+=rect(x,200,310,327,'#3c4254')+txt(x+48,245,'未读旧书 / OPEN',c,21)
   for y in range(291,489,47):
    mid+=rect(x+13,y+35,284,5,c)
    for xx in range(x+17,x+292,19):mid+=rect(xx,y+(xx//19%3)*3,13,34-(xx//19%3)*3,['#b8a27d','#759c95','#987e98'][xx//19%3])
 elif i==4:
  for x in range(0,1280,426):
   mid+=rect(x,211,413,320,'#334c55')+path(f'M{x-7} 218l50-48h296l72 48Z','#687571',c,3)+rect(x+28,325,346,194,'#142c35')+txt(x+65,292,'野狗机修 / 慢慢修',c,21)
   for xx in range(x+45,x+363,48):mid+=path(f'M{xx} 337v48m-7-57 7 9 7-9',s=c,w=3)+circ(xx,488,22,'#182933',c)+circ(xx,488,10,'none',c)
 elif i==5:
  mid+=rect(0,213,1280,252,'#36536a',20)+path('M0 436H1280',s=c,w=5)+path('M0 518H1280M0 539H1280',s=c,w=3)
  for x in range(0,1280,160):mid+=rect(x+11,261,118,114,'#152f42',8)+rect(x+16,267,109,10,c)+path(f'M{x+70} 267v102',s='#557b90',w=3)
  mid+=rect(260,242,69,213,'#668896')+rect(982,242,69,213,'#668896')+txt(530,180,'末班 / 往自由方向',c,25)
 elif i==6:
  mid+=path('M-10 204Q620 130 1290 212V302Q600 225-10 310Z','#536b76',c,4)+path('M0 231Q640 172 1280 246',s='#afbab0',w=4)
  for x in [190,680,1170]:mid+=path(f'M{x} 292l-28 239h66l-7-247Z','#6e8182',c,3)
  mid+=path('M0 505Q390 429 1280 489',s='#bdb59b',w=4)
 elif i==7:
  mid+=rect(0,476,1280,53,'#475168')+path('M0 470H1280M0 430H1280',s=c,w=3)
  for x in range(0,1280,160):mid+=path(f'M{x} 430v42',s=c)
  for x in [180,890]:mid+=path(f'M{x} 463V92m-36 15h72m-58 37h43m-33 35h27M{x} 108l-106 350m106-350 115 350',s='#a3afb5',w=3)
  mid+=rect(480,371,176,99,'#344d61',8)+circ(534,419,32,'#172e46',c)+circ(614,409,16,c)+txt(716,408,'FM / 02:17',c,24)
 elif i==8:
  far+=path('M-30 267Q340 20 677 267T1340 267',s='#d2c3a2',w=6)+path('M0 279H1280M0 296H1280',s=c,w=5)
  for x in range(0,1280,43):far+=path(f'M{x} 276V{110+abs(320-x%677)//3}',s=c)
  mid+=rect(0,333,1280,162,'#386874')+path('M0 511Q600 482 1280 508',s=c,w=6)
  for x in range(0,1280,80):mid+=path(f'M{x} {360+x%53}h55m-20 45h44',s=c,w=2)
 elif i==9:
  for x in range(0,1280,426):
   mid+=rect(x,230,406,300,'#344f5b')+path(f'M{x-8} 234l53-75h286l81 75Z','#627575',c,3)+rect(x+51,333,300,196,'#152f3b')+txt(x+102,304,'不催 / 夜仓',c,22)
   for y in range(345,521,27):mid+=path(f'M{x+56} {y}h289',s='#547882',w=3)
  far+=path('M780 282V40H1190M817 40L1150 258M818 72v228M1180 40v219',s=c,w=6)+path('M1170 219q24 61 47 0',s=c,w=5)
 elif i==10:
  mid+=path('M0 224Q640 398 1280 224',s=c,w=3)+path('M0 517H1280',s=c,w=5)
  for x in range(50,1280,130):
   y=247+int((1-abs(640-x)/640)*75);mid+=path(f'M{x} {y-33}v29',s=c)+circ(x,y,22,['#c4ded4','#dbb5a0','#b8a8cd'][x//130%3],c)+path(f'M{x-10} {y+23}h20m-10 0v17',s=c)
  for x in [160,590,1020]:mid+=path(f'M{x-83} 412q-1-76 84-69l75 44 48-28-12 30 21 32-61-4q-82 62-155-5Z','#bfe2dd',c,3)
 elif i==11:
  for x in range(0,1280,256):mid+=path(f'M{x+4} 322l32-61h181l32 61Z',['#b49c80','#90ada0'][x//256%2],c,3)+path(f'M{x+25} 322v207M{x+226} 322v207',s=c,w=5)+rect(x+27,464,199,57,'#758e7b')+txt(x+51,377,'早市 / 不催',c,22)
  for x in range(35,1260,25):mid+=circ(x,453,8,['#c8d495','#e5b37a','#9fc99f'][x//25%3],c)
 # Foreground below feet only: visually overlays road but never masks a hazard or model.
 for x in range(0,1280,160):front+=path(f'M{x} 593l81 23m-30-14h98',s=c,w=3)
 out += [f'<g id="nightFar{i}">{far}</g>',f'<g id="nightMid{i}">{mid}</g>',f'<g id="nightFront{i}">{front}</g>']
 # Map obstacles and tokens: bounding area consistent, appearance specific.
 ground=[path('M-33-6V-72H31V-6Z','#274d51',c,3)+path('M-27-67l52 56M25-67l-51 56',s=c),path('M-32-4V-50H33V-4Z','#6b536b',c,3)+circ(-23,-4,8,'#203847',c)+circ(23,-4,8,'#203847',c),path('M-25-4l-7-60h63l-8 60Z','#84a49c',c,3)+path('M-36-68h74',s=c,w=5),path('M-33-5v-68h63v68Z','#897862',c,3)+path('M-30-35h56m-54-15h55m-50-20v60',s=c),circ(0,-34,31,'#182e37',c,5)+circ(0,-34,15,'none',c,3),path('M-31-4v-70h62v70Z','#435d73',c,3)+rect(-21,-62,42,19,'#142b3e'),circ(0,-35,31,'#526a74',c,3)+path('M-28-35h56m-43-22v44m29-45v47',s=c),path('M-30-4v-40l14-20h34l12 20v40Z','#55546b',c,3)+path('M0-59v-36m-20 13h40',s=c),path('M-35-4q-11-48 17-62q22-9 47 21l-4 41Z','#698f88',c,3),path('M-34-3v-68h68v68Z','#6e7a6b',c,3)+path('M-31-65l62 58m0-58-62 58',s=c),path('M-30-4l-8-53L0-78l38 21-8 53Z','#849eab',c,3)+path('M-36-57h71M0-75v68',s=c),path('M-32-4v-47h64v47Z','#8fa57a',c,3)+circ(-26,-4,8,'#263d40',c)+circ(26,-4,8,'#263d40',c)]
 high=path('M-33-6v-65h66v65Z','#334b61',c,3)+path('M-31-58h62m-48 12h34m-34 14h34',s=c)
 token=[path('M0-76l-19 33 11 20h16l11-20Z',c,'#eff5de',2),circ(0,-42,23,c,'#fff2cd')+path('M-20-22h40M0-65v-12',s='#fff2cd'),path('M-19-18l-6-47h50l-6 47Z',c,'#fff4d4')+path('M-25-68h50m-19 0 5-16',s=c,w=3),path('M-23-20v-49h34l14 13v36Z',c,'#f4edda')+path('M11-69v15h14m-38 6h24m-24 11h21',s='#557883'),circ(0,-42,24,'none',c,8)+path('M0-72v60m-30-30h60m-51-21 42 42m0-42-42 42',s=c,w=5),path('M-29-20v-44h58v44Z',c,'#ecf8ed')+path('M-17-44h34m-34 11h24',s='#44677a'),circ(0,-42,27,'none',c,3)+circ(0,-42,17,'none',c,3)+circ(0,-42,7,c),path('M-28-27l28-40 28 40-28 16Z',c,'#f6eaff')+path('M-17-26l17-25 17 25',s='#746690'),path('M-27-20q-5-47 27-48q32 1 27 48Z',c,'#eff8db')+path('M0-65v43m-16-37 9 37m22-37-9 37',s='#4d8b89'),path('M-28-26l13-39h37v43l-23 9Z',c,'#f1e8d4')+circ(11,-52,5,'#47766f'),path('M-30-25v-39h60v39Z',c,'#f0f8ed')+path('M-28-62l28 20 28-20',s='#528587'),circ(0,-41,24,c,'#f9efca')+path('M-5-62q6-21 23-15',s='#8bad82',w=4)]
 def sym(kind,body):out.append(f'<symbol id="m{i}{kind}" viewBox="-40 -90 80 96">{body}</symbol>')
 sym('ground',ground[i]);sym('high',high);sym('token',token[i]);sym('swing',path('M0-88v29',s=c,w=3)+circ(0,-31,26,'#577f86',c,3));sym('bubble',circ(0,-35,29,'#69a7b2',c,3)+path('M-18-43q8-13 21-10',s='#ddf4ec',w=4));sym('leaf',path('M-34-45L24-71L31-16L-28-2Z','#b8ccc6',c,3)+path('M-22-43l33-9m-28 22 28-10',s='#62898a'));sym('wheel',circ(0,-35,31,'#29414c',c,5)+circ(0,-35,14,'none',c,3)+path('M0-63v56m-28-28h56',s=c,w=3));sym('gate',path('M-33-3v-77h66v77Z','#314f55',c,3)+path('M-20-64h40m-40 19h40m-40 19h40',s=c,w=5))
# Twelve different guardian silhouettes: no reused machine.
B=[
 path('M-94 58V-73l40-47 48 44 48-44 47 48v129Z','#2c555d','#87dfca',4)+path('M-75-75l18 31 32-4m42 0 34 4 17-31',s='#bdebd9',w=4)+path('M-75 16h150m-116 0v52m38-52v52m37-52v52',s='#88bfb3',w=6),
 path('M-53-16Q-81-81 0-110Q85-74 53-16L0 61Z','#554165','#e4a3ca',4)+circ(0,-51,32,'#b686ba')+''.join(path(f'M{a} -30Q{a*2} -90 {a*3} -30L{a*3+20} 69',s='#dcaacb',w=7) for a in [-45,-25,25,45])+path('M-25 16L0 58 25 16',s='#ffe2d9',w=3),
 path('M-63-10Q-105-114 0-133Q113-100 68-11Z','#4e7e83','#ffdb96',4)+rect(-42,-103,84,43,'#83b5b7',12)+''.join(path(f'M{a} -8q{a} 35 {a*2} 71q22 18 34-3',s='#9dcfc4',w=12) for a in [-44,-22,3,24])+path('M-68-42h136',s='#ffe2a4',w=5),
 path('M0-109L-90-142L-122 43L-23 81L0 49L26 82L119 41L91-142Z','#7b7183','#ddd0aa',4)+path('M0-108v157m-24-139-70-21-19 125 87 30m49-134 67-21 15 122-83 34',s='#efe5c6',w=3)+path('M-21-60l21 22 24-22',s='#b8dbcf',w=4),
 path('M-80 46q-55-122 19-154h117q69 49 28 151Z','#647b72','#e8b789',4)+path('M-64-86l-33-44 51 17m86 0 53-15-28 43',s='#e3c599',w=8)+circ(-60,50,31,'#263e44','#cbd8b8',5)+circ(64,50,31,'#263e44','#cbd8b8',5)+rect(-77,-23,153,42,'#233e48',8)+path('M-26-13v37m54-37v37',s='#ddb588',w=6),
 ''.join(path(f'M{x-35} -69q30-48 63 0V41q-27 31-64 0Z','#486b84','#adcde8',4)+rect(x-25,-43,43,40,'#142e47',4)+path(f'M{x-26} 43l-17 30m51-30 15 30',s='#a5c8d3',w=6) for x in [-77,0,77])+path('M-112-69q11-89 47-43m146 50 15-43',s='#e0e5c5',w=3),
 path('M-12-59Q-113-151-143-1l48-32 14 61 66-38Q-4 58 16-9L78 28l15-61 49 32Q111-151 14-59Z','#4d637c','#e6c499',4)+path('M-100-76l30 53 53 15m34 0 52-15 30-53',s='#b4cbc6',w=3)+path('M-14-60l-9-41 24 19 24-19-8 42Z','#849da3','#efd9ae',3),
 path('M0-83l-117-66 14 55-41 38 119 10-12 51 37-19 38 19-14-52 118-9-40-38 14-55Z','#657194','#d5bcff',4)+path('M-109-131l66 69m156-69-69 69M0-83v78',s='#e6d9ff',w=3)+path('M-17-71l16-34 20 34-18 20Z','#b9ccdc','#ebe6ff',3)+path('M-70 43l70 30 70-30',s='#bda3e8',w=5),
 path('M-106 20q-9-133 106-150q125 13 106 152Z','#497f87','#9debdc',4)+path('M-101 18L-50-60 0-87 51-60 100 18M-50-60v78m50-102v102m51-78v78',s='#c1eadd',w=3)+path('M-88 14l-32 48 49 5 26-40m90 0 27 40 51-5-32-48M-18-109l-23-33 41-9 42 9-23 34',s='#d8e7b9',w=7),
 path('M-72 11q-45-99 72-109q117 10 73 109Z','#797b68','#d7b289',4)+''.join(path(f'M{a} 7l{a*2} 30 25 32',s='#c3caa5',w=7) for a in [-41,-25,25,41])+path('M-64-45Q-151-104-140-139l-44-21 1 47 55 22m192 45Q150-104 139-139l44-21-1 47-55 22',s='#d5b99a',w=12)+path('M-24-82v-20m48 20v-20',s='#ddd7aa',w=5),
 path('M-127-27q16-87 134-83q82 8 122 79l48-35-8 42 19 40-65-18Q47 94-127-27Z','#b5d4d2','#bce9e1',4)+path('M-126-27L-9-37 120-2M7-109L-9-37 18 61M-9-37L65-78',s='#689ca8',w=3)+path('M-12 63l24 44 20-53',s='#dbe9d9',w=5)+path('M-73-56l34 12',s='#365f74',w=6),
 path('M-62 37q-37-89 14-129h84q62 37 29 129Z','#c3aa87','#ffe0ad',4)+path('M-27-90l-29-26-9-37-19-15m28 52 20-34M23-90l39-28 8-35 19-13m-27 48-18-36',s='#e3d3ab',w=7)+path('M-26 38v43m53-43v43',s='#e8d7ae',w=9)+path('M-87-40H88M0-81v42m-85 3-22 65h47l-25-65m171 0-23 65h47l-24-65',s='#e9dcb0',w=4)
]
for i,b in enumerate(B):out.append(f'<g id="guardianArt{i}">{b}<circle cx="-18" cy="-43" r="5" fill="#f4f7dc"/><circle cx="18" cy="-43" r="5" fill="#f4f7dc"/>{circ(0,0,14,C[i],"#effddd",3)}</g>')
(P/'maps-art.svgfrag').write_text('\n'.join(out))
print('authored live art bytes',len('\n'.join(out).encode()))
