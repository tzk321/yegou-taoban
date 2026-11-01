#!/usr/bin/env python3
from pathlib import Path
import re,json,xml.etree.ElementTree as ET
ROOT=Path(__file__).parent
v2={'__file__':str(ROOT/'build-v2-base.py')}
exec((ROOT/'build-v2-base.py').read_text(encoding='utf-8').split("js=(ROOT/'game-v2.js')")[0],v2)
t=v2['t'];s=v2['scope']
t=t.replace('野狗逃班 2.0：今天不改了','野狗逃班 3.0：终审之夜').replace('65 秒霓虹雨夜短片','120 秒霓虹雨夜关卡与完美通关隐藏Boss')
t=t.replace('65 秒 · 纸鲸黎明 · 四种结局 · 完全离线','120 秒 · 四段夜游 · 零受击开隐藏 Boss')
t=t.replace('今天不改了 / DIRECTOR’S CUT','终审之夜 / PERFECT ROUTE')
t=t.replace('<g id="props">','<g id="overpassSlot"/><g id="props">')
art=(ROOT/'boss-art.svgfrag').read_text(encoding='utf-8')
overpass,arena=art.split('<g id="bossWorld"',1)
t=t.replace('<g id="overpassSlot"/>',overpass)
t=t.replace('<g id="items"/>','<g id="items"/>'+'<g id="bossWorld"'+arena)
t=t.replace('<g id="cover">',(ROOT/'boss-ui.svgfrag').read_text(encoding='utf-8')+'\n<g id="cover">')
t=t.replace('pointer-events:none}.ready','pointer-events:none}.ready')
t=t.replace(']]></style>','#bossWorld,#perfectBadge,#bossHud,#bossCallout{pointer-events:none}]]></style>')
js=(ROOT/'game-v3.js').read_text(encoding='utf-8')
svg=t.replace('@STARS@',s['stars']).replace('@BUILDINGS@',s['buildings']()).replace('@SHOPS@',s['shops']()).replace('@RAIN@',s['rain']).replace('@SCRIPT@',js)
r=ET.fromstring(svg);ids=[e.attrib['id'] for e in r.iter() if 'id'in e.attrib];assert len(ids)==len(set(ids))
OUT=ROOT/'night-off-out';OUT.mkdir(exist_ok=True)
(OUT/'night-off.svg').write_text(svg,encoding='utf-8')
inline=re.sub(r'<script><!\[CDATA\[[\s\S]*?\]\]></script>','',svg).replace('<style><![CDATA[','<style>').replace(']]></style>','</style>')+'<script>'+js+'</script>'
html='''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="theme-color" content="#080e1c"><title>野狗逃班 3.0 · 终审之夜</title><style>*{box-sizing:border-box}html,body{margin:0;min-height:100%;background:#050b14}body{min-height:100svh;display:flex;justify-content:center;align-items:center;overflow-x:hidden}#nightOff{max-width:100%;max-height:100svh;box-shadow:0 20px 100px #0008}noscript{position:fixed;bottom:0;color:white;background:#142b37;padding:1em}</style></head><body>'''+inline+'''<noscript>请用浏览器打开并允许 JavaScript。</noscript></body></html>'''
(OUT/'night-off.html').write_text(html,encoding='utf-8')
print(json.dumps({'out':str(OUT),'version':'3.0','svg_bytes':len(svg.encode()),'html_bytes':len(html.encode())},ensure_ascii=False))
