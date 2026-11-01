from pathlib import Path
import re,json,xml.etree.ElementTree as ET
R=Path(__file__).parent
scope={'__file__':str(R/'build-v41.py')}
exec((R/'build-v41.py').read_text().split("js=(R/'game-v41.js')")[0],scope)
t=scope['t'];s=scope['s'];button=scope['button']
def rep(a,b):
 global t
 assert t.count(a)==1,(a[:80],t.count(a))
 t=t.replace(a,b)
t=t.replace('4.1','5.0').replace('镇店藏品 / LEGENDARY NIGHT','自由夜航 / FREE NIGHT VOYAGE')
rep('</defs>','<linearGradient id="voyageGrad" x2="1" y2="1"><stop stop-color="#102533"/><stop offset="1" stop-color="#111a2c"/></linearGradient></defs>')
# Preserve SVG UI and add route buttons as siblings, not inside moving scene.
ui=(R/'voyage-ui.svgfrag').read_text()
ui=re.sub(r'@BUTTON:([^:]+):([^@]+)@',lambda m:button(m[1],m[2]),ui)
ui=ui.replace('<text x="115" y="41" text-anchor="middle" fill="#d7efe2" font-size="22" font-weight="750">解锁领米','<text id="devClaimText" x="115" y="41" text-anchor="middle" fill="#d7efe2" font-size="22" font-weight="750">解锁领米')
ui=ui.replace('<text x="115" y="41" text-anchor="middle" fill="#d7efe2" font-size="22" font-weight="750">动画 / 跟随系统','<text id="motionChoice" x="115" y="41" text-anchor="middle" fill="#d7efe2" font-size="22" font-weight="750">动画 / 跟随系统')
rep('<script><![CDATA[',ui+'\n<script><![CDATA[')
rep('</style>', '.button:focus{outline:none}.button:focus-visible>rect{stroke:#fff1b4;stroke-width:4}.gentle *{animation:none!important;transition:none!important}#voyageHUD{pointer-events:none}]]></style>') if False else None
rep(']]></style>', '.button:focus{outline:none}.button:focus-visible>rect{stroke:#fff1b4;stroke-width:4}.gentle *{animation:none!important;transition:none!important}#voyageHUD{pointer-events:none}]]></style>')
js=(R/'game-v5.js').read_text();svg=t.replace('@STARS@',s['stars']).replace('@BUILDINGS@',s['buildings']()).replace('@SHOPS@',s['shops']()).replace('@RAIN@',s['rain']).replace('@SCRIPT@',js)
r=ET.fromstring(svg);ids=[e.attrib['id'] for e in r.iter() if 'id' in e.attrib];assert len(ids)==len(set(ids)),'duplicate IDs'
OUT=R/'night-off-out';OUT.mkdir(exist_ok=True);(OUT/'night-off.svg').write_text(svg)
inline=re.sub(r'<script><!\[CDATA\[[\s\S]*?\]\]></script>','',svg).replace('<style><![CDATA[','<style>').replace(']]></style>','</style>')+'<script>'+js+'</script>'
html='''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="theme-color" content="#080e1c"><title>野狗逃班 5.0 · 自由夜航</title><style>*{box-sizing:border-box}html,body{margin:0;min-height:100%;background:#050b14}body{min-height:100svh;display:flex;justify-content:center;align-items:center;overflow-x:hidden}#nightOff{max-width:100%;max-height:100svh;box-shadow:0 20px 100px #0008}noscript{position:fixed;bottom:0;color:white;background:#142b37;padding:1em}</style></head><body>'''+inline+'''<noscript>请用浏览器打开并允许 JavaScript。</noscript></body></html>'''
(OUT/'night-off.html').write_text(html)
print(json.dumps({'version':'5.0','html_bytes':len(html.encode()),'svg_bytes':len(svg.encode()),'out':str(OUT)},ensure_ascii=False))
