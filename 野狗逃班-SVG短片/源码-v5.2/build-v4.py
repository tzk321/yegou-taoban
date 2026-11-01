#!/usr/bin/env python3
from pathlib import Path
import re,json,xml.etree.ElementTree as ET
R=Path(__file__).parent
scope={'__file__':str(R/'build-v3.py')}
exec((R/'build-v3.py').read_text().split("js=(ROOT/'game-v3.js')")[0],scope)
t=scope['t'];s=scope['s']
def swap(a,b):
 global t
 assert t.count(a)==1,(a[:80],t.count(a))
 t=t.replace(a,b)
t=t.replace('3.0','4.0').replace('终审之夜 / PERFECT ROUTE','夜游补给 / NIGHT RUN').replace('120 秒 · 四段夜游 · 零受击开隐藏 Boss','120 秒 · 四幕夜跑 · 金币商店 · 完美隐藏 Boss')
swap('</defs>', '''<symbol id="coin" viewBox="-20 -40 40 44"><ellipse cy="-17" rx="15" ry="19" fill="#ffc870" stroke="#fff0b4" stroke-width="2"/><ellipse cy="-17" rx="10" ry="14" fill="#c88844"/><path d="M0-28v22m-4-17h8m-8 12h8" stroke="#ffe6a1" stroke-width="2.5" stroke-linecap="round"/></symbol></defs>''')
# Explicit skin parts, retain original dog illustration.
for needle,ident,part in [('M-51-72q11-28','dogCoat','coat'),('M-43-50q41','dogTrim','trim'),('M-20-81l','dogPocket','pocket'),('M-44-42l','dogHem','hem'),('M23-88q','dogHood','hood'),('M31-83l','dogScarf','scarf'),('M29-76l','dogScarfTail','scarfTail')]:
 swap('<path d="'+needle, '<path id="'+ident+'" data-part="'+part+'" d="'+needle)
swap('<path d="M7-35l8 2"', '<g id="skinAccessory" data-part="accessory"/><path d="M7-35l8 2"')
swap('<g id="dog"', '''<g id="dashEchoes" pointer-events="none"/>
<g id="dashWind" opacity="0" stroke="#b9ffe6" fill="none" pointer-events="none"><path d="M102 470H276M75 501H265M96 542H277" stroke-width="3"/><path d="M185 456Q234 451 285 465M183 554Q239 564 286 547" stroke-width="2" opacity=".55"/></g><g id="dashNose" pointer-events="none"><path d="M-17-33Q15 0-17 33" stroke="#eefff1" stroke-width="3" fill="none"/><path d="M-7-43Q32 0-7 43" stroke="#96efcf" stroke-width="2" fill="none" opacity=".45"/></g>
<g id="guardRing" class="hide" pointer-events="none"><circle r="86" fill="#a6d8fa" fill-opacity=".025" stroke="#bce6f8" stroke-width="2" stroke-dasharray="13 9"/><path d="M-80-35l-8 12 9 8M80-35l8 12-9 8" fill="none" stroke="#d5f4ff" stroke-width="3"/></g>
<g id="dog"''')
swap('<g id="bossShots"/>', '<g id="beamImpact" opacity="0"><ellipse rx="93" ry="17" fill="#ffe8c5" opacity=".28"/><path d="M-75-17l-8 18 22-3m112-14 9 18 15-6" fill="none" stroke="#fff4da" stroke-width="3"/></g><g id="bossShots"/>')
# Separate bridge from river water. Tile geometry at 1800, behind shops, sustained slow depth motion.
a=t.index('<path d="M-80 367Q');b=t.index('</g></g>',a)+4
bridge=t[a:b]
swap(bridge, '<g id="riverBridge">'+bridge+'<g transform="translate(1800,0)">'+bridge+'</g></g><g id="riverShimmer"><path d="M-40 491h85m51 25h150m152-37h175m71 22h120m115-23h96m87 43h179m110-26h169" stroke="#f1c5a5" stroke-width="2" opacity=".22"/></g>')
# Extend bridge to close 230 pixel tile gap and symmetric support cable edges.
t=t.replace('T1570 367','T1720 367').replace('H1570M360','H1720M360')
# Static riverbank contour also becomes its own slow layer, no glued-on bridge illusion.
swap('<path d="M-100 470q240', '<path id="riverBank" d="M-100 470q240')
# Build shop cards from vector UI. Overlay sits after shelf and before script so it blocks every input.
ui='''<g id="coinHud" class="hide" pointer-events="none"><rect width="280" height="38" rx="19" fill="#192635" stroke="#c09b66"/><use href="#coin" x="12" y="4" width="26" height="28"/><text id="coinText" x="49" y="26" font-size="19" fill="#ffe1a3">金币 0</text></g><g id="equippedLabel" pointer-events="none"><text id="equippedText" x="0" y="0" font-size="15" fill="#92b0b7">原装 / 无技能</text></g>'''
swap('<g id="cover">',ui+'<g id="cover">')
button=lambda id,label: f'<g id="{id}" class="button" role="button" tabindex="0" aria-label="{label}"><rect width="230" height="66" rx="15" fill="#142c35" stroke="#79a49a"/><text x="115" y="41" text-anchor="middle" fill="#d7efe2" font-size="22" font-weight="750">{label}</text></g>'
swap('<text id="hintText"',button('shopBtn','商店 · 0').replace('<text x=','<text id="walletLabel" x=')+'<text id="hintText"')
panel='''<g id="shopPanel" class="hide" role="dialog" aria-modal="true" aria-label="夜游补给商店"><rect id="shopVeil" width="1280" height="940" fill="#050c16" opacity=".96"/><rect id="shopFrame" x="22" y="20" width="1236" height="898" rx="26" fill="#0b1827" stroke="#548276" stroke-width="2"/><text id="shopTitle" x="64" y="82" font-size="43" font-weight="850" fill="#f4e9ce">凌晨补给站</text><text id="shopSub" x="64" y="121" font-size="20" fill="#95b4b8">只卖自由，不卖加班</text><text id="shopWallet" x="1226" y="85" font-size="25" text-anchor="end" fill="#ffe1a1">金币 0</text>'''+button('skinTab','雨衣 / 皮肤')+button('skillTab','手艺 / 技能')
for i in range(4):
 panel+=f'''<g id="shopCard{i}"><rect class="card-bg" width="276" height="411" rx="19" fill="#112332" stroke="#36515f" stroke-width="2"/><path d="M18 161H258" stroke="#3f5b65" opacity=".4"/><g class="card-art"/><text class="card-name" y="198" text-anchor="middle" fill="#edeee0" font-size="25" font-weight="800"/><text class="card-desc" y="235" text-anchor="middle" fill="#a6bdbd" font-size="16"/><text class="card-status" y="276" text-anchor="middle" fill="#ffd499" font-size="19"/>'''+button('shopBuy'+str(i),'购买')+'</g>'
panel+=button('shopCloseBtn','回去兜风')+'''<text id="shopMessage" font-size="21" fill="#b2e8cd">本地金币，放心花。</text><text id="shopFoot" font-size="18" fill="#86a8ad">皮肤不加属性。技能只装一个。</text></g>'''
swap('<script><![CDATA[',panel+'\n<script><![CDATA[')
t=t.replace('#bossWorld,#perfectBadge,#bossHud,#bossCallout{pointer-events:none}', '#bossWorld,#perfectBadge,#bossHud,#bossCallout,#coinHud,#dashWind,#dashEchoes{pointer-events:none}.card-art{pointer-events:none}')
js=(R/'game-v4.js').read_text()
svg=t.replace('@STARS@',s['stars']).replace('@BUILDINGS@',s['buildings']()).replace('@SHOPS@',s['shops']()).replace('@RAIN@',s['rain']).replace('@SCRIPT@',js)
r=ET.fromstring(svg);ids=[e.attrib['id'] for e in r.iter() if 'id' in e.attrib];assert len(ids)==len(set(ids))
OUT=R/'night-off-out';OUT.mkdir(exist_ok=True)
(OUT/'night-off.svg').write_text(svg)
inline=re.sub(r'<script><!\[CDATA\[[\s\S]*?\]\]></script>','',svg).replace('<style><![CDATA[','<style>').replace(']]></style>','</style>')+'<script>'+js+'</script>'
html='''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="theme-color" content="#080e1c"><title>野狗逃班 4.0 · 夜游补给</title><style>*{box-sizing:border-box}html,body{margin:0;min-height:100%;background:#050b14}body{min-height:100svh;display:flex;justify-content:center;align-items:center;overflow-x:hidden}#nightOff{max-width:100%;max-height:100svh;box-shadow:0 20px 100px #0008}noscript{position:fixed;bottom:0;color:white;background:#142b37;padding:1em}</style></head><body>'''+inline+'''<noscript>请用浏览器打开并允许 JavaScript。</noscript></body></html>'''
(OUT/'night-off.html').write_text(html)
print(json.dumps({'version':'4.0','html':len(html.encode()),'svg':len(svg.encode()),'out':str(OUT)},ensure_ascii=False))
