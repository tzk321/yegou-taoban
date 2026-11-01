from pathlib import Path
import re,json,xml.etree.ElementTree as ET
R=Path(__file__).parent
scope={'__file__':str(R/'build-v4.py')}
exec((R/'build-v4.py').read_text().split("js=(R/'game-v4.js')")[0],scope)
t=scope['t'];s=scope['s']
def swap(a,b):
 global t
 assert t.count(a)==1,(a[:80],t.count(a))
 t=t.replace(a,b)
t=t.replace('4.0','4.1').replace('夜游补给 / NIGHT RUN','镇店藏品 / LEGENDARY NIGHT')
swap('<g id="dog"',(R/'legend-art.svgfrag').read_text()+'\n<g id="dog"')
swap('<g id="cover">','<g id="legendHUD" class="hide" pointer-events="none"><rect width="280" height="37" rx="18" fill="#102132" stroke="#9587ad"/><text id="legendStatus" x="140" y="25" text-anchor="middle" fill="#d6d5ef" font-size="16">传说手艺</text></g><g id="cover">')
swap('<g id="pauseVeil">','<rect id="legendFlash" width="1280" height="710" fill="#c3e2f2" opacity="0" pointer-events="none"/><g id="pauseVeil">')
button=scope['button']
for i in range(4):
 swap(f'<g class="card-art"/>',f'<text class="card-tier" x="18" y="26" fill="#a8bcbd" font-size="15"/><g class="card-art"/>') if False else None
 # Distinct insertion points prevent match count ambiguity.
 swap(button('shopBuy'+str(i),'购买')+'</g>',button('shopBuy'+str(i),'购买')+button('shopInfo'+str(i),'预览')+'</g>')
t=t.replace('<g class="card-art"/>','<text class="card-tier" x="18" y="26" fill="#a8bcbd" font-size="15"/><g class="card-art"/>')
swap(button('shopCloseBtn','回去兜风'),button('shopPrevBtn','← 上页')+button('shopNextBtn','下页 →')+'<text id="shopPageText" x="448" y="850" text-anchor="middle" fill="#bad7d1" font-size="24">1 / 2</text>'+button('shopCloseBtn','回去兜风'))
detail='''<g id="shopDetail" class="hide" role="dialog" aria-modal="true" aria-label="藏品详情与免费预览"><rect id="detailVeil" width="1280" height="940" fill="#020916" opacity=".93"/><g id="detailContent"><rect id="detailFrame" width="780" height="766" rx="24" fill="#101e30" stroke="#b7a075" stroke-width="2"/><text id="detailTitle" x="32" y="63" fill="#f4ebd3" font-size="42" font-weight="850">镇店货</text><text id="detailPrice" x="32" y="105" fill="#f5ce8b" font-size="23">传说</text><text id="detailPreviewLabel" x="32" y="155" fill="#93b9bb" font-size="18">免费演示</text><rect id="detailDemoBG" x="26" y="179" width="728" height="282" rx="17" fill="#081528" stroke="#344f62"/><g id="detailStage"><path id="detailDemoLine" d="M-269 7H269M-260 24H-175M-116 24H-18M52 24H145M184 24H269" stroke="#40646a" stroke-width="2"/><g id="detailFX" pointer-events="none"/><g id="detailDog" pointer-events="none"/></g><text id="detailBody" x="0" y="0" fill="#c7deda" font-size="21"/><text id="detailNote" x="32" y="620" fill="#87abb4" font-size="18">预览不扣钱</text>'''+button('detailReplayBtn','重播演示')+button('detailCloseBtn','返回商店')+'''</g></g>'''
swap('<script><![CDATA[',detail+'\n<script><![CDATA[')
js=(R/'game-v41.js').read_text();svg=t.replace('@STARS@',s['stars']).replace('@BUILDINGS@',s['buildings']()).replace('@SHOPS@',s['shops']()).replace('@RAIN@',s['rain']).replace('@SCRIPT@',js)
r=ET.fromstring(svg);ids=[e.attrib['id'] for e in r.iter() if 'id'in e.attrib];assert len(ids)==len(set(ids)), 'duplicate IDs'
OUT=R/'night-off-out';OUT.mkdir(exist_ok=True);(OUT/'night-off.svg').write_text(svg)
inline=re.sub(r'<script><!\[CDATA\[[\s\S]*?\]\]></script>','',svg).replace('<style><![CDATA[','<style>').replace(']]></style>','</style>')+'<script>'+js+'</script>'
html='''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="theme-color" content="#080e1c"><title>野狗逃班 4.1 · 镇店藏品</title><style>*{box-sizing:border-box}html,body{margin:0;min-height:100%;background:#050b14}body{min-height:100svh;display:flex;justify-content:center;align-items:center;overflow-x:hidden}#nightOff{max-width:100%;max-height:100svh;box-shadow:0 20px 100px #0008}noscript{position:fixed;bottom:0;color:white;background:#142b37;padding:1em}</style></head><body>'''+inline+'''<noscript>请用浏览器打开并允许 JavaScript。</noscript></body></html>'''
(OUT/'night-off.html').write_text(html)
print(json.dumps({'version':'4.1','html_bytes':len(html.encode()),'svg_bytes':len(svg.encode()),'out':str(OUT)},ensure_ascii=False))
