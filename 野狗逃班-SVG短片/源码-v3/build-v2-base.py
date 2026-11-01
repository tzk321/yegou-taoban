#!/usr/bin/env python3
from pathlib import Path
import re, json, xml.etree.ElementTree as ET
ROOT=Path(__file__).parent
scope={'__file__':str(ROOT/'build-v1.py')}
exec((ROOT/'build-v1.py').read_text(encoding='utf-8').split('svg=svg_template.replace')[0],scope)
t=scope['svg_template']
def swap(a,b):
 global t
 assert t.count(a)==1,(a[:70],t.count(a))
 t=t.replace(a,b)
swap('<title>野狗逃班：无米之夜</title>','<title>野狗逃班 2.0：今天不改了</title>')
swap('65 秒 · 三幕雨夜 · 三种结局 · 不需要联网','65 秒 · 纸鲸黎明 · 四种结局 · 完全离线')
swap('<g id="shops">@SHOPS@</g>','''<g id="whaleReveal" opacity="0" transform="translate(880,280)">
<g id="paperWhale">
<path d="M-218-5Q-210-53-149-72Q-37-102 75-53L144-2L199-78L192-8L239 34L143 27Q83 94-56 69Q-183 49-218-5Z" fill="#74cec8" fill-opacity=".65" stroke="#bcffef" stroke-width="2.5"/>
<path d="M-218-5L-149-72L-62-3L75-53L144-2L83 29L-56 69Z" fill="#a6f1dc" opacity=".36"/>
<path d="M-149-72L-62-3L-56 69M-62-3L75-53L83 29L143 27M-218-5L-62-3L83 29M144-2L192-8L199-78M192-8L239 34" fill="none" stroke="#d6fff2" stroke-width="1.5" opacity=".7"/>
<path d="M-19 38L24 127L62 43Z" fill="#5fabba" stroke="#a6ebd8" stroke-width="2"/>
<path d="M-19 38L24 127L33 51" fill="#b7f8de" opacity=".22"/>
<path d="M-178 30Q-92 69-10 59" fill="none" stroke="#ddfff0" stroke-width="2" opacity=".6"/>
<circle cx="-156" cy="-17" r="6" fill="#173c53"/><circle cx="-154" cy="-19" r="2" fill="#f4fff0"/>
<path d="M-96-67q-17-25 0-54m-2 25q-16-8-31-7m34-3q10-17 31-23" fill="none" stroke="#ade5e0" stroke-width="2" opacity=".65"/>
<path d="M-70-141l10-5 4 12-9 4Zm-43 6l10-9 8 9-9 8ZM-138-107l10-7 3 8-8 4Z" fill="#edc6ad" opacity=".7"/>
</g><g id="whaleStars" stroke="#9bebda" stroke-width="2" opacity=".6"><path d="M-290-40h12m-6-6v12M275-24h10m-5-5v10M-30-170h10m-5-5v10"/><circle cx="-266" cy="25" r="2" fill="#fff4cf"/><circle cx="217" cy="-114" r="2" fill="#fff4cf"/></g>
</g>
<g id="shops">@SHOPS@</g>''')
swap('<g id="dogShadow">','''<g id="streetCat" opacity="0"><path d="M3 545q-14-24-28-14t-3 19" fill="none" stroke="#7f939d" stroke-width="5"/><path d="M-2 546q-7-16 2-30l-1-12 9 7 9-7-1 14q12 12 2 28Z" fill="#94a4a7"/><circle cx="5" cy="518" r="2" fill="#ffc494"/><circle cx="13" cy="518" r="2" fill="#ffc494"/><path d="M1 537v10m15-10v10" stroke="#c3cdc7" stroke-width="3"/></g>
<g id="dogReflection" opacity=".09"/>
<g id="freedomAura" opacity="0"><ellipse id="auraRing" cx="315" cy="502" rx="118" ry="92" fill="#76edd7" fill-opacity=".05" stroke="#76edd7" stroke-width="2"/><path d="M200 562h225m-190 11h166" stroke="#97f5cf" stroke-width="3" opacity=".5"/></g>
<g id="speedRays" opacity="0" stroke="#abf6df" stroke-linecap="round"><path d="M90 340h180M40 380h125M480 290h210M520 610h230M55 570h140M660 530h180" stroke-width="2"/><path d="M-10 450h190M600 405h190M980 365h150M410 215h140" stroke-width="1"/></g>
<g id="dogShadow">''')
swap('<g id="particles"/>','''<g id="landingRipples"/>
<g id="particles"/>''')
swap('<g id="cover">','''<g id="skillHud" class="hide"><rect id="skillBg" width="340" height="47" rx="23" fill="#07182a" opacity=".9"/><text id="comboText" x="20" y="31" font-size="20" fill="#a9f7dc">连击 0</text><path id="energyTrack" d="M137 25h119" stroke="#273e4f" stroke-width="10" stroke-linecap="round"/><path id="energyFill" d="M137 25h0" stroke="#ffc980" stroke-width="10" stroke-linecap="round"/><text id="energyText" x="279" y="31" font-size="17" fill="#ffc980">0 / 6</text></g>
<g id="revealCaption" class="hide"><text id="revealWord" x="640" y="190" font-size="36" text-anchor="middle" fill="#d7fff0" letter-spacing="8">把通知折成鲸，放回江里。</text></g>
<g id="cover">''')
swap('无米之夜 / NIGHT OFF','今天不改了 / DIRECTOR’S CUT')
swap('<g id="pauseVeil">','''<g id="freedomBanner" class="hide"><rect id="freedomBannerBg" x="400" y="103" width="480" height="52" rx="26" fill="#11352f" stroke="#7cf0ce"/><text id="freedomBannerText" x="640" y="137" font-size="24" text-anchor="middle" fill="#c5ffe4" font-weight="800">自由模式 / 全群消息已静音</text></g>
<g id="pauseVeil">''')
swap('<g id="againBtn"','''<text id="badgeText" x="640" y="444" font-size="18" text-anchor="middle" fill="#ffd79b">本地徽章 0 / 4</text><g id="againBtn"''')
swap('</g></g>\n<g id="shelf">','''</g><g id="ticketBtn" class="button" role="button" tabindex="0" aria-label="保存本局SVG票根"><rect width="230" height="60" rx="14" fill="#172532" stroke="#c3a078"/><text x="115" y="40" font-size="22" text-anchor="middle" fill="#ffe0b3">保存逃班票根 ↓</text></g><text id="ticketHint" x="640" y="630" text-anchor="middle" font-size="15" fill="#93aaa9">票根是一张 SVG，无需截图，也不上传数据。</text></g>
<g id="shelf">''')
swap('<g id="pauseBtn"','''<g id="superBtn" class="button" role="button" tabindex="0" aria-label="自由模式，六杯咖啡充能"><rect width="240" height="86" rx="16" fill="#2c2430" stroke="#aa8062"/><text id="superLabel" x="120" y="37" font-size="23" font-weight="800" text-anchor="middle" fill="#ffd395">自由模式</text><text id="superHint" x="120" y="63" font-size="16" text-anchor="middle" fill="#c6a892">冰美式 0 / 6</text><rect id="superMeter" x="16" y="77" width="0" height="3" rx="1.5" fill="#ffdc9a"/></g>
<g id="pauseBtn"''')
t=t.replace('touch-action:manipulation','touch-action:none').replace('.button:active rect{fill:#304b56}', '.button:active rect,.button.pressed rect{fill:#304b56}.ready rect{stroke:#ffe1a2;stroke-width:3}.ready text{fill:#ffe4b0}#skillHud,#revealCaption,#freedomBanner{pointer-events:none}')
t=t.replace('viewBox="0 0 1280 860" width="1280" height="860"','viewBox="0 0 1280 940" width="1280" height="940"')
t=t.replace('height="170" fill="#0b1422"','height="230" fill="#0b1422"')
t=t.replace('transform="translate(265,742)"','transform="translate(990,750)"').replace('transform="translate(40,742)"','transform="translate(40,750)"')
t=t.replace('<g id="superBtn" class="button"','<g id="superBtn" transform="translate(490,750)" class="button"')
for old,new in [(520,300),(665,442),(810,584),(955,726),(1100,868)]:
 t=t.replace(f'transform="translate({old},750)"',f'transform="translate({new},864)"')
t=t.replace('y="840"','y="932"')
t=t.replace('<text id="dashLabel"','<rect id="dashMeter" x="16" y="62" width="0" height="3" rx="1.5" fill="#8aefcf"/><text id="dashLabel"')
js=(ROOT/'game-v2.js').read_text(encoding='utf-8')
svg=t.replace('@STARS@',scope['stars']).replace('@BUILDINGS@',scope['buildings']()).replace('@SHOPS@',scope['shops']()).replace('@RAIN@',scope['rain']).replace('@SCRIPT@',js)
ET.fromstring(svg)
OUT=ROOT/'night-off-out';OUT.mkdir(exist_ok=True)
(OUT/'night-off.svg').write_text(svg,encoding='utf-8')
inline=re.sub(r'<script><!\[CDATA\[[\s\S]*?\]\]></script>','',svg).replace('<style><![CDATA[','<style>').replace(']]></style>','</style>')+'<script>'+js+'</script>'
html='''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="theme-color" content="#080e1c"><title>野狗逃班 2.0 · 今天不改了</title><style>*{box-sizing:border-box}html,body{margin:0;min-height:100%;background:#050b14}body{min-height:100svh;display:flex;justify-content:center;align-items:center;overflow-x:hidden}#nightOff{max-width:100%;max-height:100svh;box-shadow:0 20px 100px #0008}noscript{position:fixed;bottom:0;color:white;background:#142b37;padding:1em}</style></head><body>'''+inline+'''<noscript>请用浏览器打开并允许 JavaScript。</noscript></body></html>'''
(OUT/'night-off.html').write_text(html,encoding='utf-8')
(OUT/'README-zh.txt').write_text('''野狗逃班 2.0：今天不改了 / 导演剪辑版
65秒，三幕，全矢量，完全离线。

推荐浏览器打开 night-off.html。SVG在相册/img图片预览里不执行脚本，这是浏览器安全限制。

操作：左手跳跃（空格/↑），最右冲刺（Shift/X），中间自由模式（E）。
手机按钮按下即响应，支持双指同时操作；点击画面也能跳跃。
可二段跳。落地前按跳有130ms缓冲，冲刺冷却3.2秒。
六杯冰美式充满自由模式，持续3.8秒：吸咖啡、无敌、撞碎通知，结束后短暂保护。
擦身越过通知会加连击与充能；收集/撞飞也累计连击。连击在4.5秒没有得分或被撞时断开。

新增：纸鲸黎明分镜、咖啡磁吸大招、近距闪避、连击、四枚本地徽章、可下载SVG票根。
四个游戏结局与一个放映结局。最后几秒收工，不会碰一次就失败。
“放映”是自动完成，不用操作；“我来逃班”是亲自游玩。

P暂停，R重来，按钮返回封面。切后台自动暂停。
静音起步。打开音效有轻量合成音乐和反馈；无网络音频。
最佳分与徽章仅在本地浏览器存储，隐私模式受限不影响游玩。
片尾“保存逃班票根”生成独立SVG，可在浏览器保存，不上传任何信息。

新计分：咖啡×10 + 撞飞×20 + 擦身闪避×12 + 最高连击×5 - 被催×3，最低0分。
已保留旧版到“旧版-v1.1”，可随时回看。
''',encoding='utf-8')
print(json.dumps({'out':str(OUT),'version':'2.0','svg_bytes':len(svg.encode()),'html_bytes':len(html.encode())},ensure_ascii=False))
