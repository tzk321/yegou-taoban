from pathlib import Path
import re,json,hashlib,xml.etree.ElementTree as ET
R=Path(__file__).parent
scope={'__file__':str(R/'build-v51.py')}
exec((R/'build-v51.py').read_text().split("js=(R/'game-v51.js')")[0],scope)
t=scope['t'];s=scope['s']
def swap(a,b):
 global t
 assert t.count(a)==1,(a[:100],t.count(a));t=t.replace(a,b)
t=t.replace('5.1','5.2').replace('合流夜游 / OPEN NIGHT ROUTES','十二夜路 / TWELVE NIGHT PATHS')
swap('</defs>',(R/'maps-art.svgfrag').read_text()+'</defs>')
bg='<g id="nightLiveBG" class="hide" pointer-events="none"><rect id="liveNightSky" x="-50" y="-160" width="1450" height="900" fill="#102737"/><use id="liveFarA"/><use id="liveFarB"/><use id="liveMidA"/><use id="liveMidB"/><rect id="nightRoad" y="529" width="1350" height="210" fill="#162d38"/><path d="M0 556H1350M0 606H1350" stroke="#6b9491" stroke-width="2" opacity=".32"/><rect id="nightGlow" width="1350" height="530" fill="#ffd398" opacity=".06"/><g id="nightWeather" stroke="#c0e3d5">'+''.join(f'<path d="M{x} {y}l-9 25"/>' for x in range(0,1350,130) for y in range(0,530,160))+'</g></g>'
swap('<g id="items"',bg+'<g id="items"')
swap('<g id="feedback"','<g id="nightLiveFG" class="hide" pointer-events="none"><use id="liveFrontA"/><use id="liveFrontB"/></g><g id="feedback"')
swap('<g id="bossWorld"','<g id="bossWorld"') if False else None
swap('<g id="bossShots"', '<g id="mapBossActor" pointer-events="none"/><g id="mapBossWarnings" pointer-events="none"/><g id="mapBossAttacks" pointer-events="none"/><g id="bossShots"')
js=(R/'game-v52.js').read_text();svg=t.replace('@STARS@',s['stars']).replace('@BUILDINGS@',s['buildings']()).replace('@SHOPS@',s['shops']()).replace('@RAIN@',s['rain']).replace('@SCRIPT@',js)
r=ET.fromstring(svg);ids=[e.attrib['id']for e in r.iter()if'id'in e.attrib];assert len(ids)==len(set(ids)), 'duplicate IDs'
OUT=R/'night-off-out';OUT.mkdir(exist_ok=True);(OUT/'night-off.svg').write_text(svg)
inline=re.sub(r'<script><!\[CDATA\[[\s\S]*?\]\]></script>','',svg).replace('<style><![CDATA[','<style>').replace(']]></style>','</style>')+'<script>'+js+'</script>'
html='<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="theme-color" content="#080e1c"><title>野狗逃班 5.2 · 十二夜路</title><style>*{box-sizing:border-box}html,body{margin:0;min-height:100%;background:#050b14}body{min-height:100svh;display:flex;justify-content:center;align-items:center;overflow-x:hidden}#nightOff{max-width:100%;max-height:100svh;box-shadow:0 20px 100px #0008}noscript{position:fixed;bottom:0;color:white;background:#142b37;padding:1em}</style></head><body>'+inline+'<noscript>请用浏览器打开并允许 JavaScript。</noscript></body></html>'
(OUT/'night-off.html').write_text(html)
info={'version':'5.2','base':'frozen game-v51 + authored maps/bosses/balance/scenes','html_bytes':len(html.encode()),'svg_bytes':len(svg.encode()),'sha256':hashlib.sha256(html.encode()).hexdigest(),'maps':12,'guardians':12,'unique_ids':len(ids),'size_floor_bytes':524288};assert info['html_bytes']>=524288
(OUT/'build-manifest.json').write_text(json.dumps(info,ensure_ascii=False,indent=2));print(json.dumps(info,ensure_ascii=False))
