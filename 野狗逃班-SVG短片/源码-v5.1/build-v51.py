from pathlib import Path
import re,json,xml.etree.ElementTree as ET,hashlib
R=Path(__file__).parent
scope={'__file__':str(R/'build-v5.py')}
exec((R/'build-v5.py').read_text().split("js=(R/'game-v5.js')")[0],scope)
t=scope['t'];s=scope['s'];button=scope['button']
def swap(a,b):
 global t
 assert t.count(a)==1,(a[:80],t.count(a))
 t=t.replace(a,b)
t=t.replace('5.0','5.1').replace('自由夜航 / FREE NIGHT VOYAGE','合流夜游 / OPEN NIGHT ROUTES')
swap('</defs>',(R/'arcade-art.svgfrag').read_text()+'</defs>')
swap('<g id="cover">','<g id="extraBadge" class="hide" pointer-events="none"><rect id="extraBadgeBG" width="690" height="49" rx="16" fill="#122b36" stroke="#88aaab"/><text id="extraBadgeText" x="18" y="32" fill="#dcdfbe" font-size="23"/></g><g id="cover">')
swap('<g id="pauseVeil">','<rect id="streetTint" pointer-events="none" width="1280" height="710" fill="#7bbcac" opacity="0"/><g id="pauseVeil">')
swap('<g id="voyageOverlay"',button('arcadeBtn','地图 / 新支线')+'<g id="voyageOverlay"')
swap('<g id="voyageMenu">','<g id="voyageMenu">'+button('extraMenuBtn','地图 / 新支线 / 手账'))
# Cover clues in scene coordinates; no external image resources.
secrets='''<g id="secretHotspots"><g id="secretMoon" class="button secret" role="button" tabindex="0" aria-label="月亮上的暗号"><circle cx="1028" cy="84" r="27" fill="#cbe0ce" fill-opacity=".08"/><path d="M1017 83q10-9 20 0m-17 4h14" stroke="#d8e7c6" stroke-width="1" opacity=".5"/></g><g id="secretCat" class="button secret" role="button" tabindex="0" aria-label="问问路边猫"><path d="M159 518v-18l8 7 9-7 3 20q16 9 7 22h-28q-14-12 1-24Z" fill="#769d96" stroke="#98b5a8"/><circle cx="167" cy="518" r="2" fill="#dfdfbd"/></g><g id="secretCoffee" class="button secret" role="button" tabindex="0" aria-label="窗边冰美式"><path d="M623 462h25l-4 31h-17Z" fill="#b4c8ae" stroke="#d9d5b4"/><path d="M620 459h31m-13 0 5-12" stroke="#b6d2c4" stroke-width="3"/></g><g id="secretLetter" class="button secret" role="button" tabindex="0" aria-label="没寄出的信"><rect x="503" y="501" width="32" height="20" rx="3" fill="#b6d6bf"/><path d="M504 502l15 10 15-10" fill="none" stroke="#558f88"/></g><g id="secretWhale" class="button secret" role="button" tabindex="0" aria-label="街边纸鲸"><path d="M710 443q13-16 30-4l14-8-4 15 7 9-20-2q-24 13-27-10Z" fill="#a3c3bd" opacity=".6"/></g></g>'''
swap('<g id="dogReflection"',secrets+'<g id="dogReflection"')
panel='''<g id="arcadePanel" class="hide" role="dialog" aria-modal="true" aria-label="夜游地图和新支线"><rect id="hubVeil" width="1280" height="940" fill="#040c17" opacity=".97"/><rect id="hubFrame" x="22" y="20" width="1236" height="898" rx="26" fill="#0a1929" stroke="#668a85" stroke-width="2"/><g id="hubHead"><text id="hubTitle" x="0" y="0" fill="#f4e5c8" font-size="44" font-weight="850">夜游地图 / 新支线</text><text id="hubSubtitle" x="0" y="41" fill="#8fbdba" font-size="18"/></g>'''+button('routeTab','玩法')+button('mapTab','夜游地图')+button('journalTab','手账')+button('settingsTab','设置')+'''<g id="hubBody"><rect id="hubBodyBG" width="1156" height="523" rx="22" fill="#0c1c2d"/><g id="hubDynamic"/></g>'''+button('hubNativeBtn','原夜航 / 开发者')+button('hubCloseBtn','回去兜风')+'''<text id="hubMessage" fill="#b7d9cd" font-size="20"/><text id="hubFoot" fill="#779da5" font-size="17"/></g>'''
swap('<script><![CDATA[',panel+'<script><![CDATA[')
swap(']]></style>', '.secret{cursor:pointer;pointer-events:all}.secret:focus{outline:none;filter:drop-shadow(0 0 4px #b1eed3)}#coverFade,#cover text,#hubDynamic text{pointer-events:none}#streetTint,#extraBadge{pointer-events:none}]]></style>')
js=(R/'game-v51.js').read_text();svg=t.replace('@STARS@',s['stars']).replace('@BUILDINGS@',s['buildings']()).replace('@SHOPS@',s['shops']()).replace('@RAIN@',s['rain']).replace('@SCRIPT@',js)
r=ET.fromstring(svg);ids=[e.attrib['id'] for e in r.iter() if 'id'in e.attrib];assert len(ids)==len(set(ids)),'duplicate IDs'
OUT=R/'night-off-out';OUT.mkdir(exist_ok=True);(OUT/'night-off.svg').write_text(svg)
inline=re.sub(r'<script><!\[CDATA\[[\s\S]*?\]\]></script>','',svg).replace('<style><![CDATA[','<style>').replace(']]></style>','</style>')+'<script>'+js+'</script>'
html='''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="theme-color" content="#080e1c"><title>野狗逃班 5.1 · 合流夜游</title><style>*{box-sizing:border-box}html,body{margin:0;min-height:100%;background:#050b14}body{min-height:100svh;display:flex;justify-content:center;align-items:center;overflow-x:hidden}#nightOff{max-width:100%;max-height:100svh;box-shadow:0 20px 100px #0008}noscript{position:fixed;bottom:0;color:white;background:#142b37;padding:1em}</style></head><body>'''+inline+'''<noscript>请用浏览器打开并允许 JavaScript。</noscript></body></html>'''
(OUT/'night-off.html').write_text(html)
info={'version':'5.1','base':'frozen 5.0 + playground extras','html_bytes':len(html.encode()),'svg_bytes':len(svg.encode()),'sha256':hashlib.sha256(html.encode()).hexdigest(),'postcards':12,'unique_ids':len(ids),'size_floor_bytes':524288};assert info['html_bytes']>=524288,'HTML must contain at least 512 KiB real content';(OUT/'build-manifest.json').write_text(json.dumps(info,ensure_ascii=False,indent=2));print(json.dumps(info,ensure_ascii=False))
