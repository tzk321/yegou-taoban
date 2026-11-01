from pathlib import Path
import re,json,hashlib,xml.etree.ElementTree as ET
R=Path(__file__).parent
t=(R/'frozen-v52.svg').read_text()
assert hashlib.sha256(t.encode()).hexdigest()=='f295df4d9551159abfb31acb7751dc18f1532d2321c627a69e209b77c086caef'
js=(R/'game-v53.js').read_text()
t=re.sub(r'<script><!\[CDATA\[[\s\S]*?\]\]></script>','@JS53@',t)
def swap(a,b):
 global t
 assert t.count(a)==1,(a[:80],t.count(a));t=t.replace(a,b)
filters='''<filter id="dangerRed53" color-interpolation-filters="sRGB"><feColorMatrix type="matrix" values=".35 .65 .1 0 .12 .13 .17 .03 0 .03 .12 .11 .05 0 .06 0 0 0 1 0"/></filter><filter id="safeGreen53" color-interpolation-filters="sRGB"><feColorMatrix type="matrix" values=".08 .12 .05 0 .02 .3 .6 .1 0 .14 .22 .38 .12 0 .12 0 0 0 1 0"/></filter>'''
swap('</defs>',filters+'</defs>')
swap('<g id="bossShots"','<g id="v53GearFX" pointer-events="none"/><g id="bossShots"')
def button(i,label):
 return f'<g id="{i}" class="button" role="button" tabindex="0" aria-label="{label}"><rect width="160" height="72" rx="16" fill="#142c39" stroke="#8db6b2" stroke-width="2"/><text id="{dict(counterBtn="counterLabel",bgmBtn="bgmLabel",volumeBtn="volumeLabel").get(i,i+"Text")}" x="80" y="45" text-anchor="middle" fill="#dcebd7" font-size="23">{label}</text></g>'
controls=''.join(button(i,l)for i,l in [('moveLeftBtn','← 走位'),('moveRightBtn','走位 →'),('fallBtn','↓ 急落'),('counterBtn','反击 / F'),('bgmBtn','BGM：关'),('volumeBtn','35%')])
swap('<g id="shopPanel"',controls+'<g id="shopPanel"')
t=t.replace('5.2','5.3').replace('十二夜路 / TWELVE NIGHT PATHS','弹幕夜行 / BULLET NIGHT')
svg=t.replace('@JS53@','<script><![CDATA['+js+']]></script>')
r=ET.fromstring(svg);ids=[x.attrib['id']for x in r.iter()if'id'in x.attrib];assert len(ids)==len(set(ids))
inline=t.replace('@JS53@','').replace('<style><![CDATA[','<style>').replace(']]></style>','</style>')+'<script>'+js+'</script>'
html='<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="theme-color" content="#080e1c"><title>野狗逃班 5.3 · 弹幕夜行</title><style>*{box-sizing:border-box}html,body{margin:0;width:100%;height:100%;background:#050b14;overflow:hidden;overscroll-behavior:none}body{position:fixed;inset:0;height:100vh;height:100dvh;touch-action:none}#nightOff{position:absolute;inset:0;display:block;max-width:none;max-height:none;width:100vw;height:100vh;height:100dvh;touch-action:none}html:fullscreen,html:-webkit-full-screen{width:100%;height:100%;background:#050b14}noscript{position:fixed;bottom:0;color:white;background:#142b37;padding:1em}</style></head><body>'+inline+'<noscript>请用浏览器打开并允许 JavaScript。</noscript></body></html>'
O=R/'night-off-out';O.mkdir(exist_ok=True)
(O/'night-off.html').write_text(html);(O/'night-off.svg').write_text(svg)
manifest={'version':'5.3','html_bytes':len(html.encode()),'svg_bytes':len(svg.encode()),'sha256':hashlib.sha256(html.encode()).hexdigest(),'svg_sha256':hashlib.sha256(svg.encode()).hexdigest(),'frozen_baseline':'5.2 published landscape/HUD repair','bosses':13,'skins':10,'skills':11,'tracks':7,'size_floor_bytes':524288}
assert manifest['html_bytes']>=524288
(O/'build-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2));print(json.dumps(manifest,ensure_ascii=False))
