#!/usr/bin/env python3
from pathlib import Path
import random, re, json, xml.etree.ElementTree as ET
OUT=Path(__file__).parent / 'night-off-out'
OUT.mkdir(exist_ok=True)
r=random.Random(17)

def buildings():
    s=[]
    for repeat in (0,1600):
        for i in range(17):
            x=repeat+i*100-15; h=r.randint(95,250); w=r.randint(55,92); y=475-h
            s.append(f'<g><path d="M{x} 475V{y}h{w}v{h}Z" fill="#152944"/><path d="M{x+12} {y}v-12h18v12" fill="#152944"/>')
            for row in range(4):
                for col in range(3):
                    if r.random()<.65:
                        s.append(f'<rect x="{x+10+col*22}" y="{y+20+row*38}" width="7" height="12" fill="{r.choice(["#729eaa","#96c7b0","#d9ac6b"])}" opacity=".35"/>')
            s.append('</g>')
    return ''.join(s)

def shops():
    s=[]
    names=['无米便利店','凌晨咖啡','今天不改了','下班修理铺','南宁 · 夜游']
    colors=['#5bf2d3','#ff78ba','#9eacff','#ffc467','#5bf2d3']
    for repeat in (0,1600):
        for i,(name,color) in enumerate(zip(names,colors)):
            x=repeat+i*320; h=[255,220,295,260,210][i]; y=552-h
            s.append(f'''<g transform="translate({x},0)"><path d="M0 552V{y}h306v{h}Z" fill="#1a2035" stroke="#324156" stroke-width="2"/>
<path d="M10 {y+9}h286" stroke="#496375" stroke-width="3"/>
<rect x="18" y="{y+29}" width="272" height="{h-160}" rx="4" fill="url(#windowGrid)"/>
<rect x="18" y="434" width="270" height="41" rx="5" fill="#101827" stroke="{color}" stroke-width="2"/>
<text x="153" y="462" fill="{color}" font-size="25" font-weight="700" text-anchor="middle">{name}</text>
<path d="M12 482h286l-15 21H24Z" fill="{color}" opacity=".3"/>
<rect x="25" y="507" width="110" height="44" fill="#2c5258"/><path d="M80 508v43" stroke="#101c2f" stroke-width="6"/>
<rect x="153" y="505" width="125" height="47" fill="#393749"/><path d="M170 518h72m-72 13h52" stroke="{color}" stroke-width="3" opacity=".5"/>
<path d="M30 565l-14 90h120l-10-90" fill="{color}" opacity=".055"/>
<path d="M175 565l-35 110h135l-18-110" fill="{color}" opacity=".04"/></g>''')
    return ''.join(s)

stars=''.join(f'<circle cx="{r.randrange(20,1450)}" cy="{r.randrange(-140,220)}" r="{r.choice([1,1.5,2])}" fill="#c1dded" opacity="{r.uniform(.15,.7):.2f}"/>' for _ in range(55))
rain=''.join(f'<path d="M{r.randrange(-100,1430)} {r.randrange(-350,700)}l-11 32"/>' for _ in range(72))
svg_template='''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" id="nightOff" viewBox="0 0 1280 860" width="1280" height="860" role="application" aria-label="野狗逃班，一部可玩的 SVG 短片">
<title>野狗逃班：无米之夜</title><desc>65 秒霓虹雨夜短片。可放映，或点击跳跃、冲刺撞飞加班通知。用浏览器打开以交互。</desc>
<defs>
<linearGradient id="nightSky" x2="0" y2="1"><stop stop-color="#070e20"/><stop offset=".62" stop-color="#172744"/><stop offset="1" stop-color="#45515e"/></linearGradient>
<linearGradient id="dawnSky" x2="0" y2="1"><stop stop-color="#192b51"/><stop offset=".57" stop-color="#68516e"/><stop offset="1" stop-color="#ecb590"/></linearGradient>
<linearGradient id="wetRoad" x2="0" y2="1"><stop stop-color="#172937"/><stop offset="1" stop-color="#080f1c"/></linearGradient>
<linearGradient id="coverShade"><stop stop-color="#080e1c" stop-opacity=".95"/><stop offset=".66" stop-color="#080e1c" stop-opacity=".6"/><stop offset="1" stop-color="#080e1c" stop-opacity="0"/></linearGradient>
<linearGradient id="vignette" x2="0" y2="1"><stop stop-color="#030815" stop-opacity=".38"/><stop offset=".35" stop-color="#030815" stop-opacity="0"/><stop offset=".83" stop-color="#030815" stop-opacity="0"/><stop offset="1" stop-color="#030815" stop-opacity=".68"/></linearGradient>
<linearGradient id="coatGrad" x2="0.7" y2="1"><stop stop-color="#ffe09a"/><stop offset=".5" stop-color="#ffc64e"/><stop offset="1" stop-color="#e6a72b"/></linearGradient>
<pattern id="windowGrid" width="36" height="40" patternUnits="userSpaceOnUse"><rect width="36" height="40" fill="#192c3e"/><rect x="7" y="8" width="19" height="25" fill="#51847e" opacity=".22"/><path d="M16 8v25M7 20h19" stroke="#142438" stroke-width="2"/></pattern>
<pattern id="riverRipple" width="180" height="35" patternUnits="userSpaceOnUse"><path d="M0 12h65m50 10h48M25 31h30" stroke="#80adac" stroke-width="2" opacity=".22"/></pattern>
<symbol id="coffee" viewBox="-30 -62 60 70"><ellipse cy="5" rx="21" ry="5" fill="#050d1b" opacity=".35"/><path d="M-20-44h40L15 0h-30Z" fill="#b18154" stroke="#d9f7ed" stroke-width="3"/><path d="M-18-37h36l-5 29h-26Z" fill="#422f33"/><path d="M-9-28l10-3 3 9-10 3Zm14 5 9-2 2 9-10 2Z" fill="#acccca" opacity=".75"/><rect x="-24" y="-50" width="48" height="8" rx="4" fill="#e0fbf5"/><path d="M8-49l5-19" stroke="#ff88b4" stroke-width="4"/><circle cy="-20" r="7" fill="#e2e8d2"/><path d="M-3-20h6" stroke="#688a73" stroke-width="2"/></symbol>
<symbol id="folder" viewBox="-42 -88 84 96"><ellipse cy="4" rx="37" ry="6" fill="#040b18" opacity=".4"/><path d="M-36-68v-12h29l8 12h34v66h-71Z" fill="#d76896" stroke="#ffa7cb" stroke-width="3"/><path d="M-27-61h53v43h-53Z" fill="#f5dfdc"/><path d="M-19-52h35m-35 9h25" stroke="#9d6076" stroke-width="3"/><path d="M-38-39h76l-7 39h-62Z" fill="#923b6a" stroke="#ffc0d5" stroke-width="3"/><text y="-13" text-anchor="middle" font-size="16" font-weight="800" fill="#fff3f3">加班</text></symbol>
<symbol id="notice" viewBox="-55 -94 110 100"><rect x="-51" y="-76" width="102" height="66" rx="10" fill="#243349" stroke="#ff88b4" stroke-width="3"/><circle cx="-34" cy="-59" r="6" fill="#ff8ba9"/><text x="4" y="-53" text-anchor="middle" font-size="15" fill="#f6b6ce">改一下</text><path d="M-34-37h64m-64 11h43" stroke="#91a8bf" stroke-width="3"/></symbol>
</defs>
<style><![CDATA[
#nightOff{display:block;background:#080e1c;font-family:system-ui,-apple-system,'Noto Sans CJK SC','Microsoft YaHei',sans-serif;color:#e5f3ef;user-select:none;-webkit-user-select:none}text{pointer-events:none}.button{cursor:pointer;touch-action:manipulation;outline:none}.button rect{transition:fill .15s,stroke .15s}.button:hover rect,.button:focus-visible rect{stroke:#d6fff2;stroke-width:3}.button:active rect{fill:#304b56}.label{font-weight:650;letter-spacing:1px}.muted{fill:#88a8b6}.pill{fill:#0d1b2a;stroke:#344c59;stroke-width:1.5}.caps{letter-spacing:5px;font-weight:650}.hide{display:none}.paused #pauseVeil{display:inline}.paused .world{opacity:.7}#pauseVeil{display:none}.tapArea{touch-action:none;cursor:crosshair}.ghost{opacity:.22}.accent{fill:#8aefd2}.credit{letter-spacing:2px}
]]></style>
<rect width="1280" height="1500" fill="#080e1c"/>
<svg id="scene" class="tapArea" x="0" y="0" width="1280" height="710" viewBox="0 0 1280 710" preserveAspectRatio="xMidYMid slice">
<g class="world" id="world">
<rect x="-1500" y="-1000" width="5000" height="1800" fill="url(#nightSky)"/>
<rect id="dawn" x="-1500" y="-1000" width="5000" height="1800" fill="url(#dawnSky)" opacity="0"/>
<g id="stars">@STARS@</g>
<g id="moon" transform="translate(1050,95)"><circle r="48" fill="#a9d5db" opacity=".045"/><circle r="30" fill="#c2e7df" opacity=".1"/><circle r="19" fill="#d5f3e6"/><circle cx="8" cy="-6" r="18" fill="#1b2b43"/></g>
<g id="sunrise" opacity="0"><circle cx="660" cy="369" r="110" fill="#efae80" opacity=".045"/><circle cx="660" cy="369" r="65" fill="#ffc697" opacity=".07"/><circle cx="660" cy="369" r="37" fill="#ffd5a3" opacity=".85"/><path d="M614 451h95m-87 14h81m-71 14h67m-55 14h45" stroke="#ffc49b" stroke-width="3" opacity=".15"/></g>
<g id="clouds" opacity=".24" fill="#496078"><path d="M-100 138q120-44 245 0t250 0 250 0 250 0 250 0 250 0v30H-100Z"/><path d="M-200 70q170-32 340 0t340 0 340 0 340 0v16H-200Z"/></g>
<g id="farCity">@BUILDINGS@</g>
<path d="M-100 470q240-45 430-15t320-4 400 0 420 0v110H-100Z" fill="#16353d" opacity=".5"/>
<g id="river" opacity="0"><rect x="-100" y="435" width="1600" height="132" fill="#395268"/><rect x="-100" y="435" width="1600" height="132" fill="url(#riverRipple)"/>
<path d="M0 437h1500M0 451h1500" stroke="#e1b596" opacity=".3" stroke-width="3"/>
<path d="M-80 367Q320 157 740 367T1570 367" fill="none" stroke="#b5b3bf" stroke-width="4"/>
<path d="M-80 378H1570M360 250v145M760 220v175M1150 256v140" stroke="#a2a3b9" stroke-width="7"/>
<path d="M160 291v87M250 258v120M450 253v125M550 278v100M650 314v64M850 277v101M950 298v80M1050 294v84M1250 268v110" stroke="#9098af" stroke-width="2"/>
<g fill="#ffd18f"><circle cx="360" cy="248" r="4"/><circle cx="760" cy="218" r="4"/><circle cx="1150" cy="254" r="4"/></g></g>
<g id="shops">@SHOPS@</g>
<path d="M-100 556H1500V850H-100Z" fill="url(#wetRoad)"/>
<path d="M-100 556h1600" stroke="#78adbd" stroke-width="3"/><path d="M-100 562h1600" stroke="#2c4d63" stroke-width="7"/>
<g id="roadMarks" stroke="#acd7cf" stroke-width="4" opacity=".25"><path d="M-100 659h80m110 0h80m110 0h80m110 0h80m110 0h80m110 0h80m110 0h80m110 0h80m110 0h80"/><path d="M-120 615h130m280 0h110m240 0h85m280 0h115" stroke-width="1"/></g>
<g id="reflections" opacity=".45"><path d="M40 576h115m-95 13h78m440 31h160m-148 9h82m192-57h88m-67 12h101m95 39h200m-184 10h100" stroke="#ff86bd" stroke-width="3"/><path d="M180 601h180m-144 12h94m630-33h153m-130 15h74m-555 53h96" stroke="#59bfae" stroke-width="3"/></g>
<g id="props"><g transform="translate(850,0)"><path d="M0 560V256q0-18-20-18h-49" fill="none" stroke="#182236" stroke-width="10"/><path d="M-82 237h33l7 11h-47Z" fill="#8ea5ab"/><path d="M-82 248l-72 307H25l-74-307Z" fill="#d6f7de" opacity=".045"/><ellipse cx="-65" cy="561" rx="98" ry="7" fill="#cbf6dd" opacity=".09"/></g><g transform="translate(1450,0)"><path d="M0 560V265h-82" fill="none" stroke="#182236" stroke-width="10"/><path d="M-82 264h30" stroke="#bcdfd1" stroke-width="6"/></g></g>
<g id="drone" transform="translate(540,190)"><ellipse cy="40" rx="35" ry="6" fill="#080e20" opacity=".25"/><path d="M-43-11h86" stroke="#8aa6b8" stroke-width="4"/><path d="M-35-18h-23m83 0h23" stroke="#94d3d5" stroke-width="3"/><path d="M-27-5h54l-5 22h-44Z" fill="#26314a" stroke="#92b4c2" stroke-width="2"/><circle cy="5" r="6" fill="#ff86b5"/><path d="M-8 25L-43 151H60L8 25" fill="#ff8aa8" opacity=".025"/><text y="-31" text-anchor="middle" font-size="13" fill="#d392ad" letter-spacing="3">KPI 巡航中</text></g>
<g id="items"/>
<g id="dogShadow"><ellipse cx="300" cy="564" rx="70" ry="9" fill="#040a12" opacity=".6"/><ellipse cx="300" cy="570" rx="57" ry="3" fill="#7fccba" opacity=".14"/></g>
<g id="dashTrail" opacity="0" stroke="#8af9de" stroke-linecap="round"><path d="M172 481h79M145 508h110M167 529h68" stroke-width="5"/><path d="M125 496h60M137 542h59" stroke-width="2"/></g>
<g id="dog" transform="translate(300,560)"><g id="dogBody">
<g id="tail"><path d="M-42-70q-31-4-39-30q-8-8-15 0q-1 34 38 52Z" fill="#b57850" stroke="#382b2b" stroke-width="3"/><path d="M-82-85q-12-24-18-9l3 16" fill="#f0ce9e"/></g>
<g id="legBack"><path d="M-26-43l-14 22 5 16" fill="none" stroke="#a9704b" stroke-width="13" stroke-linecap="round"/><path d="M-35-4h18" stroke="#edc797" stroke-width="12" stroke-linecap="round"/></g>
<g id="legFront"><path d="M27-44l6 23 10 15" fill="none" stroke="#b98254" stroke-width="13" stroke-linecap="round"/><path d="M42-5h16" stroke="#f0cf9e" stroke-width="12" stroke-linecap="round"/></g>
<path d="M-51-72q11-28 49-26l36 8 12 45q-46 24-94 4Z" fill="url(#coatGrad)" stroke="#6c502a" stroke-width="3"/>
<path d="M-43-50q41 12 80-6" fill="none" stroke="#fff0a8" stroke-width="3" opacity=".7"/><path d="M-20-81l-3 26h21l2-25Z" fill="#edb545" stroke="#bc8935" stroke-width="2"/><path d="M-44-42l-6 8q39 11 99-1l-6-11" fill="#f8c751" stroke="#ad7a2f" stroke-width="2"/>
<path d="M23-88q-5-34 15-43q29-10 49 13l-11 46Z" fill="#ffdd77" stroke="#987032" stroke-width="3"/>
<path d="M39-119q13-15 32-5l6 25-33 17Z" fill="#775041"/><path d="M39-110q5-24 16-26l10 21Z" fill="#a4724e" stroke="#4e3730" stroke-width="2"/>
<path d="M47-113q18-12 29 5l4 11 23 8q5 13-11 20l-34-5-14-14Z" fill="#d5a675" stroke="#4f3830" stroke-width="3"/>
<path d="M78-96l23 7q5 9-6 13l-22-3Z" fill="#f5d8af"/><ellipse cx="100" cy="-89" rx="7" ry="5" fill="#24303a"/><path d="M70-80q11 8 20 0" fill="none" stroke="#593a32" stroke-width="2"/>
<path d="M82-76q6 16 11 4v-8" fill="#ef8694"/><circle cx="70" cy="-103" r="4" fill="#12212c"/><circle cx="71" cy="-104" r="1.4" fill="#fff"/><path d="M60-111l11-2" stroke="#755037" stroke-width="2" stroke-linecap="round"/>
<path d="M31-83l28 12-10 8-22-8Z" fill="#5ee0c2"/><path d="M29-76l-13 17 17-3" fill="#45aa98"/><path d="M7-35l8 2" stroke="#e9fcf0" stroke-width="5" stroke-linecap="round"/>
</g></g>
<g id="feedback" opacity="0"><rect x="210" y="357" width="235" height="41" rx="20" fill="#122335" stroke="#75cfbc"/><text id="feedbackText" x="327" y="384" text-anchor="middle" font-size="20" fill="#b3f2db">自由 +1</text></g>
<g id="particles"/>
<g id="rain" stroke="#a3cadd" stroke-width="1" opacity=".22">@RAIN@</g>
</g>
<rect x="-1500" y="-1000" width="5000" height="1850" fill="url(#vignette)" pointer-events="none"/>
</svg>
<g id="hud" class="hide"><rect id="hudBg" x="28" y="22" width="610" height="54" rx="27" fill="#081624" opacity=".87"/><text id="chapterText" x="51" y="56" font-size="19" class="label accent">01 / 雨夜离席</text><text id="coffeeText" x="288" y="56" font-size="20" fill="#f6d18d">冰美式 0</text><text id="hitText" x="462" y="56" font-size="19" class="muted">被催 0 次</text></g>
<g id="cover">
<rect id="coverFade" x="0" y="75" width="1280" height="460" fill="url(#coverShade)"/>
<text id="kicker" x="80" y="143" font-size="18" fill="#8ee3cb" class="caps">一部可以乱来的 SVG 短片</text>
<text id="title1" x="73" y="259" font-size="112" font-weight="900" fill="#f6f0df" letter-spacing="-4">野狗逃班</text>
<text id="title2" x="81" y="307" font-size="24" class="caps" fill="#ffb997">无米之夜 / NIGHT OFF</text>
<text id="coverLine1" x="82" y="356" font-size="22" fill="#b7ccce">把加班留在身后，把凌晨还给自己。</text>
<g id="filmBtn" class="button" role="button" tabindex="0" aria-label="放映短片" transform="translate(80,390)"><rect width="235" height="67" rx="14" fill="#9bf2d1" stroke="#9bf2d1"/><text x="118" y="43" font-size="24" font-weight="800" fill="#142934" text-anchor="middle">▷ 放映</text></g>
<g id="playBtn" class="button" role="button" tabindex="0" aria-label="我来逃班" transform="translate(333,390)"><rect width="250" height="67" rx="14" fill="#172534" stroke="#8fbdba"/><text x="125" y="43" font-size="24" font-weight="750" fill="#e0f3e5" text-anchor="middle">我来逃班 →</text></g>
<text id="coverLine2" x="82" y="495" font-size="16" class="muted">65 秒 · 三幕雨夜 · 三种结局 · 不需要联网</text>
</g>
<g id="subtitle" class="hide"><rect id="subtitleBg" x="68" y="612" width="1144" height="72" rx="13" fill="#070f1e" opacity=".83"/><text id="subtitleLine" x="640" y="654" font-size="25" text-anchor="middle" fill="#e5eddf">凌晨 02:17。群里还在问：在吗？</text></g>
<rect id="transition" width="1280" height="710" fill="#d2e4d5" opacity="0" pointer-events="none"/>
<g id="pauseVeil"><rect id="pauseRect" width="1280" height="710" fill="#081324" opacity=".64"/><text id="pausedLabel" x="640" y="320" text-anchor="middle" font-size="62" fill="#e3f6ec" font-weight="800">先摸一会儿鱼</text><text id="pausedHint" x="640" y="367" text-anchor="middle" font-size="21" fill="#a0bcbf">按 P / 暂停按钮继续</text></g>
<g id="ending" class="hide"><rect id="endVeil" width="1280" height="710" fill="#091625" opacity=".9"/><text id="endKicker" x="640" y="162" text-anchor="middle" font-size="18" class="caps accent">片尾 / 你已离开工作群的射程</text><text id="endTitle" x="640" y="260" text-anchor="middle" font-size="70" font-weight="900" fill="#ffe1a0">无米，但自由</text><text id="endLine" x="640" y="325" text-anchor="middle" font-size="24" fill="#c9d8d8">钱可以明天再想，今天先把风吹够。</text><text id="endStats" x="640" y="380" text-anchor="middle" font-size="22" fill="#7edec9">冰美式 0 / 撞飞 KPI 0 / 被催 0 次</text><text id="bestText" x="640" y="420" text-anchor="middle" font-size="17" class="muted">最好的成绩：尚未开始</text><g id="againBtn" class="button" role="button" tabindex="0" aria-label="再逃一次" transform="translate(392,460)"><rect width="230" height="64" rx="14" fill="#9bf2d1" stroke="#9bf2d1"/><text x="115" y="41" text-anchor="middle" font-size="24" fill="#162b37" font-weight="800">再逃一次</text></g><g id="endHomeBtn" class="button" role="button" tabindex="0" aria-label="返回封面" transform="translate(650,460)"><rect width="230" height="64" rx="14" class="pill"/><text x="115" y="41" text-anchor="middle" font-size="24" fill="#c4ded8">回封面</text></g></g>
<g id="shelf"><rect id="shelfBg" x="0" y="710" width="1280" height="170" fill="#0b1422"/><path id="shelfEdge" d="M0 710H1280" stroke="#2d4856"/><rect id="progressTrack" x="40" y="711" width="1200" height="3" rx="1.5" fill="#273e4c"/><rect id="progressFill" x="40" y="711" width="0" height="3" rx="1.5" fill="#8af0d0"/>
<g id="jumpBtn" class="button" role="button" tabindex="0" aria-label="跳跃，可二段跳" transform="translate(40,742)"><rect width="210" height="69" rx="14" class="pill"/><text id="jumpLabel" x="105" y="44" font-size="25" text-anchor="middle" fill="#e1f2e6" font-weight="750">跳跃 ↗</text></g>
<g id="dashBtn" class="button" role="button" tabindex="0" aria-label="冲刺，冷却三秒" transform="translate(265,742)"><rect width="210" height="69" rx="14" fill="#173332" stroke="#467c70"/><text id="dashLabel" x="105" y="44" font-size="25" text-anchor="middle" fill="#8febce" font-weight="750">冲刺 →</text></g>
<g id="pauseBtn" class="button" role="button" tabindex="0" aria-label="暂停或继续" transform="translate(520,750)"><rect width="130" height="54" rx="12" class="pill"/><text id="pauseText" x="65" y="35" text-anchor="middle" font-size="20" fill="#bed8d6">暂停</text></g>
<g id="restartBtn" class="button" role="button" tabindex="0" aria-label="重新开始" transform="translate(665,750)"><rect width="130" height="54" rx="12" class="pill"/><text x="65" y="35" text-anchor="middle" font-size="20" fill="#bed8d6">重来</text></g>
<g id="homeBtn" class="button" role="button" tabindex="0" aria-label="回到封面" transform="translate(810,750)"><rect width="130" height="54" rx="12" class="pill"/><text x="65" y="35" text-anchor="middle" font-size="20" fill="#bed8d6">封面</text></g>
<g id="soundBtn" class="button" role="button" tabindex="0" aria-label="开关音效" transform="translate(955,750)"><rect width="130" height="54" rx="12" class="pill"/><text id="soundText" x="65" y="35" text-anchor="middle" font-size="20" fill="#bed8d6">音效：关</text></g>
<g id="fullBtn" class="button" role="button" tabindex="0" aria-label="全屏" transform="translate(1100,750)"><rect width="130" height="54" rx="12" class="pill"/><text x="65" y="35" text-anchor="middle" font-size="20" fill="#bed8d6">全屏</text></g>
<text id="hintText" x="40" y="840" font-size="16" class="muted">点击画面 / 空格 二段跳 · Shift 冲刺 · P 暂停 · R 重来 · 静音起步</text><text id="timerText" x="1230" y="840" text-anchor="end" font-size="16" fill="#a1bfbc">SVG / 原生矢量</text>
</g>
<script><![CDATA[
@SCRIPT@
]]></script></svg>'''

js=r'''
(()=>{'use strict';
const svg=document.getElementById('nightOff'),$=id=>document.getElementById(id),NS='http://www.w3.org/2000/svg';
const DURATION=65,GROUND=560,DOGX=300;let last=0,idle=0,mobile=false,compact=false,seed=71,sound=false,audio=null,best=0;
const reduced=typeof matchMedia==='function'&&matchMedia('(prefers-reduced-motion: reduce)').matches;
const S={phase:'cover',mode:'film',t:0,paused:false,y:0,vy:0,jumps:0,dash:0,cool:0,inv:0,coffee:0,hits:0,smashed:0,distance:0,spawn:0.5,chapter:0,ending:'',toast:0,shake:0};
let items=[],particles=[];try{best=Number(localStorage.getItem('nightOffBest'))||0}catch(e){}
const subtitles=[[0,'凌晨 02:17。群里还在问：在吗？'],[5,'在。但不在工位。'],[10,'野狗决定：今天不改了。'],[16,'雨很大。自由不用打伞。'],[21,'第二幕 / 一杯冰美式，续上命再说。'],[27,'左边是便利店。右边是又一个“改一下”。'],[33,'冲过去。不是每条通知都值得回。'],[39,'跑慢一点也行，别把自己交出去。'],[44,'第三幕 / 邕江的风，不查你的考勤。'],[50,'桥那头没什么大事。只是在天亮。'],[56,'有钱有有钱的活法。没钱也能兜风。'],[61,'嗯。今天先到这里。']];
const attr=(e,k,v)=>{v=String(v);if(e.getAttribute(k)!==v)e.setAttribute(k,v)};const set=(id,k,v)=>attr($(id),k,v);const text=(id,t)=>{const e=$(id);if(e.textContent!==t)e.textContent=t};
function show(id,yes){$(id).classList.toggle('hide',!yes)}
function rnd(){seed=(seed*1664525+1013904223)>>>0;return seed/4294967296}
function node(tag,attrs={}){const n=document.createElementNS(NS,tag);for(const[k,v]of Object.entries(attrs))attr(n,k,v);return n}
function beep(f=400,len=.1,type='sine',vol=.04){if(!sound)return;try{audio=audio||new(window.AudioContext||window.webkitAudioContext)();if(audio.state==='suspended')audio.resume().catch(()=>{});const o=audio.createOscillator(),g=audio.createGain();o.type=type;o.frequency.setValueAtTime(f,audio.currentTime);o.frequency.exponentialRampToValueAtTime(Math.max(40,f*.45),audio.currentTime+len);g.gain.setValueAtTime(vol,audio.currentTime);g.gain.exponentialRampToValueAtTime(.001,audio.currentTime+len);o.connect(g);g.connect(audio.destination);o.start();o.stop(audio.currentTime+len)}catch(e){sound=false;text('soundText','音效：关')}}
function clearWorld(){for(const o of items)o.el.remove();for(const p of particles)p.el.remove();items=[];particles=[];}
function start(mode){clearWorld();seed=71;Object.assign(S,{phase:'running',mode,t:0,paused:false,y:0,vy:0,jumps:0,dash:0,cool:0,inv:0,coffee:0,hits:0,smashed:0,distance:0,spawn:.5,chapter:0,ending:'',toast:0,shake:0});svg.classList.remove('paused');text('pauseText','暂停');show('cover',false);show('ending',false);show('hud',true);show('subtitle',true);last=performance.now();render();beep(620,.12)}
function home(){clearWorld();S.phase='cover';S.paused=false;S.t=0;S.y=0;S.dash=0;S.inv=0;S.toast=0;S.shake=0;svg.classList.remove('paused');show('cover',true);show('ending',false);show('hud',false);show('subtitle',false);text('pauseText','暂停');render()}
function pause(force){if(S.phase!=='running')return;S.paused=typeof force==='boolean'?force:!S.paused;svg.classList.toggle('paused',S.paused);text('pauseText',S.paused?'继续':'暂停');last=performance.now()}
function jump(){if(S.phase!=='running'||S.paused||S.mode==='film'||S.jumps>=2)return;jumpCore()}
function jumpCore(){S.vy=S.jumps===0?-635:-570;S.jumps++;puff(DOGX-17,GROUND+S.y,8,'#c8e1d1');beep(S.jumps===1?430:630,.09)}
function dash(){if(S.phase!=='running'||S.paused||S.mode==='film'||S.cool>0)return;dashCore()}
function dashCore(){S.dash=.55;S.cool=3.2;S.inv=Math.max(S.inv,.65);puff(DOGX-60,GROUND+S.y-55,10,'#8bf4d4');beep(180,.2,'sawtooth',.025)}
function puff(x,y,count,color){if(reduced)count=Math.min(count,3);for(let i=0;i<count;i++){const el=node('circle',{cx:x,cy:y,r:2+rnd()*4,fill:color});$('particles').appendChild(el);particles.push({el,x,y,vx:(rnd()-.75)*190,vy:(rnd()-.85)*160,life:.45+rnd()*.35,max:.8})}}
function toast(message,color='#b3f2db'){S.toast=.85;text('feedbackText',message);set('feedbackText','fill',color)}
function spawn(){const coffee=rnd()<.62;const height=coffee?[-54,-145,-245][Math.floor(rnd()*3)]:0;const type=coffee?'coffee':rnd()<.6?'folder':'notice';const x=mobile?930:1400;const el=node('use',{href:'#'+type,x:-40,y:coffee?-67:-90,width:80,height:coffee?80:96});const g=node('g');g.appendChild(el);$('items').appendChild(g);items.push({el:g,x,y:GROUND+height,coffee,type,done:false,phase:rnd()*7});}
function end(){S.phase='ending';S.paused=false;svg.classList.remove('paused');show('hud',false);show('subtitle',false);show('ending',true);let title,line;
if(S.mode==='film'){title='今天不改了';line='片尾没有彩蛋。风已经把答案吹过来了。'}
else if(S.coffee>=15){title='咖啡因自由人';line='账上未必有米，血里全是冰美式。'}
else if(S.hits>=9){title='带薪精神离职';line='人被催到了。灵魂已经在邕江边兜风。'}
else{title='无米，但自由';line='钱可以明天再想，今天先把风吹够。'}
S.ending=title;text('endTitle',title);text('endLine',line);text('endStats',`冰美式 ${S.coffee} / 撞飞 KPI ${S.smashed} / 被催 ${S.hits} 次`);
if(S.mode==='play'){best=Math.max(best,S.coffee*10+S.smashed*15-S.hits*3);try{localStorage.setItem('nightOffBest',String(best))}catch(e){}}
text('bestText',S.mode==='film'?'放映完毕 / 再试试亲自逃班？':`本局自由分 ${S.coffee*10+S.smashed*15-S.hits*3} · 最佳 ${best}`);beep(760,.28)}
function step(dt){if(S.phase!=='running'||S.paused)return;S.t=Math.min(DURATION,S.t+dt);S.chapter=S.t<21?0:S.t<44?1:2;const speed=(240+S.chapter*37)*(S.dash>0?1.75:1);S.distance+=speed*dt;S.cool=Math.max(0,S.cool-dt);S.dash=Math.max(0,S.dash-dt);S.inv=Math.max(0,S.inv-dt);S.toast=Math.max(0,S.toast-dt);S.shake=Math.max(0,S.shake-dt);
if(S.mode==='film'){const near=items.find(o=>!o.done&&o.x>DOGX+30&&o.x<DOGX+210);if(near&&!near.coffee&&S.cool===0)dashCore();if(near&&near.coffee&&near.y<GROUND-90&&S.y===0)jumpCore()}
S.vy+=1600*dt;S.y+=S.vy*dt;if(S.y>=0){S.y=0;S.vy=0;S.jumps=0}S.spawn-=dt;if(S.spawn<=0&&S.t<61){spawn();S.spawn=.59+rnd()*.55}
for(const o of items){o.x-=speed*dt;const dy=o.coffee?Math.sin(S.t*3+o.phase)*4:0;attr(o.el,'transform',`translate(${o.x},${o.y+dy})`);const dx=Math.abs(o.x-(DOGX+17)),dogCenter=GROUND+S.y-65,objCenter=o.y+(o.coffee?-29:-37);const coll=dx<(o.coffee?62:64)&&Math.abs(dogCenter-objCenter)<(o.coffee?57:64);
if(!o.done&&coll){if(o.coffee){S.coffee++;o.done=true;toast('冰美式 +1','#ffe0a1');puff(o.x,o.y-35,11,'#ffd89c');beep(980,.1)}else if(S.dash>0){S.smashed++;o.done=true;toast('KPI 已下线');S.shake=reduced?0:.14;puff(o.x,o.y-30,18,'#ff9ac1');beep(100,.14,'triangle')}else if(S.mode==='film'){o.done=true}else if(S.inv<=0){S.hits++;S.inv=1.35;o.done=true;toast('收到，但不改。','#ffb2ce');S.shake=reduced?0:.19;puff(DOGX+20,GROUND+S.y-70,12,'#ff9dba');beep(95,.18,'square',.02)}}
if(o.x<-120)o.done=true;}items=items.filter(o=>{if(o.done)o.el.remove();return!o.done});
particles=particles.filter(p=>{p.life-=dt;p.x+=p.vx*dt;p.y+=p.vy*dt;p.vy+=180*dt;attr(p.el,'cx',p.x);attr(p.el,'cy',p.y);attr(p.el,'opacity',Math.max(0,p.life/p.max));if(p.life<=0)p.el.remove();return p.life>0});if(S.t>=DURATION)end();}
function render(){const running=S.phase==='running',clock=running||S.phase==='ending'?S.t:idle,dist=S.phase==='cover'?idle*36:S.distance;const dawn=S.phase==='cover'?0:Math.max(0,Math.min(1,(S.t-42)/21));
set('world','transform',S.shake>0?`translate(${Math.sin(clock*140)*S.shake*15},${Math.cos(clock*110)*S.shake*9})`:'translate(0,0)');set('feedback','opacity',Math.min(1,S.toast*4));set('feedback','transform',`translate(0,${S.y-(.85-S.toast)*28})`);set('sunrise','opacity',dawn);set('sunrise','transform',`translate(0,${(1-dawn)*100})`);set('dawn','opacity',dawn);set('stars','opacity',1-dawn*.95);set('moon','opacity',1-dawn*.75);set('moon','transform',`translate(${mobile?675:1050},${mobile?-20:95})`);set('farCity','transform',`translate(${-dist*.12%1600},0)`);set('clouds','transform',`translate(${-dist*.026%200},0)`);set('shops','transform',`translate(${-dist*.48%1600},0)`);set('shops','opacity',Math.max(0,1-dawn*1.4));set('river','opacity',Math.min(1,dawn*1.7));set('props','transform',`translate(${-dist*.77%1150},0)`);set('props','opacity',1-dawn*.6);set('roadMarks','transform',`translate(${-dist%190},0)`);set('reflections','transform',`translate(${-dist*.3%180},0)`);
set('rain','opacity',reduced?0:.25*(1-dawn*.85));set('rain','transform',`translate(${-clock*44%120},${clock*380%260-190})`);set('drone','transform',`translate(${DOGX+245+Math.sin(clock*.8)*37},${205+Math.sin(clock*1.4)*18})`);set('drone','opacity',Math.max(0,1-dawn*1.4));
const beat=clock*(running?17:7),stride=S.y<0?0:Math.sin(beat)*24;set('dog','transform',`translate(${DOGX},${GROUND+S.y})`);set('dogBody','transform',`translate(0,${S.y<0?0:Math.abs(Math.sin(beat))*-3}) rotate(${S.dash>0?-7:S.y<0?-5:0})`);set('legBack','transform',`rotate(${stride},-25,-43)`);set('legFront','transform',`rotate(${-stride},28,-44)`);set('tail','transform',`rotate(${Math.sin(clock*12)*7},-45,-70)`);set('dog','opacity',S.inv>0&&S.dash===0?(Math.sin(clock*35)>0?.5:1):1);set('dogShadow','opacity',Math.max(.13,1+S.y/350));set('dashTrail','opacity',S.dash>0?.85:0);set('dashTrail','transform',`translate(0,${S.y})`);
text('coffeeText',`冰美式 ${S.coffee}`);text('hitText',`被催 ${S.hits} 次`);text('chapterText',['01 / 雨夜离席','02 / 街头续命','03 / 江风自由'][S.chapter]);text('dashLabel',S.cool>0?`冷却 ${S.cool.toFixed(1)}s`:'冲刺 →');set('jumpBtn','opacity',S.phase==='running'&&S.mode==='play'?1:.38);set('dashBtn','opacity',S.phase==='running'&&S.mode==='play'?(S.cool>0?.6:1):.38);set('progressFill','width',(mobile?640:1200)*S.t/DURATION);text('timerText',S.phase==='cover'?'SVG / 原生矢量':`${S.mode==='film'?'放映':'逃班'} / ${Math.floor(S.t).toString().padStart(2,'0')} : 65`);
if(running){let line=subtitles[0][1];for(const[t,s]of subtitles)if(S.t>=t)line=s; text('subtitleLine',line);const d=Math.min(Math.abs(S.t-21),Math.abs(S.t-44));set('transition','opacity',d<.32?(1-d/.32)*.75:0)}else set('transition','opacity',0);
text('hintText',S.phase==='cover'?'放映：自动看完 · 逃班：自己跳，撞飞 KPI，收集冰美式':S.mode==='film'?'自动放映中 · 可以暂停 / 开音效，或者切到逃班模式':mobile?'点画面也能跳 · 连点二段跳 · 冲刺能撞飞加班':'空格 / ↑ 二段跳 · Shift / X 冲刺 · P 暂停 · R 重来');
}
function frame(now){const dt=Math.min(.033,Math.max(0,(now-last)/1000||0));last=now;if(!S.paused){idle+=dt;if(S.phase==='running')step(dt)}render();requestAnimationFrame(frame)}
function pos(id,x,y){set(id,'transform',`translate(${x},${y})`)}
function buttonSize(id,w,h){const b=$(id),rect=b.querySelector('rect'),label=b.querySelector('text');attr(rect,'width',w);attr(rect,'height',h);attr(label,'x',w/2);attr(label,'y',h/2+9)}
function layout(){const w=innerWidth||1280,h=innerHeight||860;mobile=w/h<1.1;compact=!mobile&&h<520;const W=mobile?720:1280,H=mobile?1250:compact?690:860,sceneH=mobile?810:compact?500:710;attr(svg,'viewBox',`0 0 ${W} ${H}`);attr(svg,'width',W);attr(svg,'height',H);svg.style.width=Math.min(w,h*W/H)+'px';svg.style.height=Math.min(h,w*H/W)+'px';set('scene','width',W);set('scene','height',sceneH);set('scene','viewBox',mobile?'0 -140 800 900':'0 0 1280 710');for(const id of['transition','pauseRect','endVeil']){set(id,'width',W);set(id,'height',sceneH)}set('shelfBg','y',sceneH);set('shelfBg','width',W);set('shelfBg','height',H-sceneH+10);set('shelfEdge','d',`M0 ${sceneH}H${W}`);for(const id of['progressTrack','progressFill']){set(id,'x',40);set(id,'y',sceneH+1)}set('progressTrack','width',W-80);
set('coverFade','width',W);set('coverFade','y',mobile?140:75);set('coverFade','height',mobile?390:460);
const titleX=mobile?44:80;for(const[id,y]of[['kicker',mobile?177:143],['title1',mobile?286:259],['title2',mobile?337:307],['coverLine1',mobile?379:356],['coverLine2',mobile?518:495]]){set(id,'x',titleX);set(id,'y',y)}set('title1','font-size',mobile?104:112);set('coverLine1','font-size',mobile?23:22);set('kicker','font-size',mobile?20:18);set('coverLine2','font-size',mobile?18:16);
pos('filmBtn',mobile?44:80,mobile?412:390);pos('playBtn',mobile?360:333,mobile?412:390);buttonSize('filmBtn',mobile?295:235,mobile?86:67);buttonSize('playBtn',mobile?315:250,mobile?86:67);
set('hudBg','width',mobile?668:610);set('hudBg','x',mobile?26:28);set('hudBg','height',mobile?64:54);for(const[id,x]of[['chapterText',mobile?43:51],['coffeeText',mobile?317:288],['hitText',mobile?502:462]]){set(id,'x',x);set(id,'y',mobile?62:56);set(id,'font-size',mobile?22:19)}
set('subtitleBg','x',mobile?24:68);set('subtitleBg','y',mobile?704:612);set('subtitleBg','width',W-(mobile?48:136));set('subtitleBg','height',mobile?87:72);set('subtitleLine','x',W/2);set('subtitleLine','y',mobile?756:654);set('subtitleLine','font-size',mobile?23:25);for(const id of['pausedLabel','pausedHint'])set(id,'x',W/2);set('pausedLabel','y',mobile?350:320);set('pausedLabel','font-size',mobile?54:62);set('pausedHint','y',mobile?405:367);
for(const id of['endKicker','endTitle','endLine','endStats','bestText'])set(id,'x',W/2);set('endKicker','y',mobile?240:162);set('endTitle','y',mobile?341:260);set('endTitle','font-size',mobile?64:70);set('endLine','y',mobile?403:325);set('endLine','font-size',mobile?21:24);set('endStats','y',mobile?463:380);set('endStats','font-size',mobile?21:22);set('bestText','y',mobile?506:420);pos('againBtn',mobile?100:392,mobile?556:460);pos('endHomeBtn',mobile?390:650,mobile?556:460);buttonSize('againBtn',230,mobile?74:64);buttonSize('endHomeBtn',230,mobile?74:64);
pos('jumpBtn',40,mobile?854:742);pos('dashBtn',mobile?372:265,mobile?854:742);buttonSize('jumpBtn',mobile?308:210,mobile?107:69);buttonSize('dashBtn',mobile?308:210,mobile?107:69);set('jumpLabel','font-size',mobile?32:25);set('dashLabel','font-size',mobile?32:25);
const util=['pauseBtn','restartBtn','homeBtn','soundBtn','fullBtn'];util.forEach((id,i)=>{pos(id,mobile?40+(i%3)*222:520+i*145,mobile?988+Math.floor(i/3)*98:750);buttonSize(id,mobile?196:130,mobile?82:54);const t=$(id).querySelector('text');attr(t,'font-size',mobile?25:20)});set('hintText','x',40);set('hintText','y',mobile?1194:840);set('hintText','font-size',mobile?20:16);set('timerText','x',W-40);set('timerText','y',mobile?1230:840);set('timerText','font-size',mobile?18:16);
if(compact){set('scene','viewBox','0 150 1280 500');for(const[id,y]of[['kicker',74],['title1',181],['title2',229],['coverLine1',272],['coverLine2',387]])set(id,'y',y);set('title1','font-size',94);pos('filmBtn',80,298);pos('playBtn',333,298);buttonSize('filmBtn',235,80);buttonSize('playBtn',250,80);set('subtitleBg','y',408);set('subtitleBg','height',72);set('subtitleLine','y',452);set('pausedLabel','y',250);set('pausedHint','y',297);for(const[id,y]of[['endKicker',78],['endTitle',170],['endLine',229],['endStats',276],['bestText',314]])set(id,'y',y);set('endTitle','font-size',64);pos('againBtn',392,349);pos('endHomeBtn',650,349);buttonSize('againBtn',230,80);buttonSize('endHomeBtn',230,80);pos('jumpBtn',40,535);pos('dashBtn',265,535);buttonSize('jumpBtn',210,96);buttonSize('dashBtn',210,96);set('jumpLabel','font-size',28);set('dashLabel','font-size',28);util.forEach((id,i)=>{pos(id,520+i*145,543);buttonSize(id,130,80);attr($(id).querySelector('text'),'font-size',22)});set('hintText','y',674);set('timerText','y',674)}render()}
function bind(id,fn){const e=$(id);e.addEventListener('click',ev=>{ev.stopPropagation();fn()});e.addEventListener('keydown',ev=>{if(ev.key==='Enter'||ev.key===' '){ev.preventDefault();ev.stopPropagation();fn()}})}
bind('filmBtn',()=>start('film'));bind('playBtn',()=>start('play'));bind('jumpBtn',jump);bind('dashBtn',dash);bind('pauseBtn',()=>pause());bind('restartBtn',()=>start(S.mode));bind('homeBtn',home);bind('againBtn',()=>start(S.mode));bind('endHomeBtn',home);bind('soundBtn',()=>{sound=!sound;text('soundText',sound?'音效：开':'音效：关');if(sound)beep(720,.09)});bind('fullBtn',()=>{try{const p=document.fullscreenElement?document.exitFullscreen():document.documentElement.requestFullscreen?.();if(p&&p.catch)p.catch(()=>{})}catch(e){}});
$('scene').addEventListener('pointerdown',e=>{if(S.phase==='running'&&S.mode==='play'){e.preventDefault();jump()}});
window.addEventListener('keydown',e=>{if(e.target.closest&&e.target.closest('.button'))return;const k=e.key.toLowerCase();if(S.phase!=='running'&&k!=='r')return;if([' ','arrowup','shift','x','p','r'].includes(k)){e.preventDefault();if(e.repeat)return;if(k===' '||k==='arrowup')jump();else if(k==='shift'||k==='x')dash();else if(k==='p')pause();else if(k==='r')start(S.mode)}});
document.addEventListener('visibilitychange',()=>{if(document.hidden&&S.phase==='running')pause(true);last=performance.now()});window.addEventListener('resize',layout);
Object.defineProperty(window,'__nightOff',{get:()=>({...S,mobile,items:items.length,version:'1.1'})});
if(new URLSearchParams(location.search).has('qa'))window.__nightQA=Object.freeze({inspect(){return items.map(o=>({x:o.x,y:o.y,coffee:o.coffee,type:o.type}))},advance(seconds){for(let n=0;n<seconds*60;n++)step(1/60);render();return{...S}},jump:jump,dash:dash});
layout();last=performance.now();requestAnimationFrame(frame);
})();
'''
svg=svg_template.replace('@STARS@',stars).replace('@BUILDINGS@',buildings()).replace('@SHOPS@',shops()).replace('@RAIN@',rain).replace('@SCRIPT@',js)
ET.fromstring(svg)
(OUT/'night-off.svg').write_text(svg,encoding='utf-8')
inline=re.sub(r'<script><!\[CDATA\[[\s\S]*?\]\]></script>','',svg)
inline += '<script>'+js+'</script>'
inline=inline.replace('<style><![CDATA[','<style>').replace(']]></style>','</style>')
html='''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"><meta name="theme-color" content="#080e1c"><title>野狗逃班 · 可玩的 SVG 短片</title><style>*{box-sizing:border-box}html,body{margin:0;min-height:100%;background:#050b14}body{min-height:100svh;display:flex;justify-content:center;align-items:center;overflow-x:hidden}#nightOff{max-width:100%;max-height:100svh;box-shadow:0 20px 100px #0008}noscript{position:fixed;bottom:0;color:white;background:#142b37;padding:1em}</style></head><body>'''+inline+'''<noscript>请用浏览器打开并允许 JavaScript，即可播放和互动。</noscript></body></html>'''
(OUT/'night-off.html').write_text(html,encoding='utf-8')
(OUT/'README-zh.txt').write_text('''野狗逃班：无米之夜
一部可玩的原创 SVG 短片 / 65 秒 / 三幕 / 完全离线

推荐：用 Chrome、Edge 或支持 JavaScript 的浏览器打开 night-off.html。
HTML 是单文件，全部矢量画面和代码已经嵌入，不需要联网，不读取私人数据。

【放映】自动跑完故事，不用操作。
【我来逃班】点击画面 / 跳跃按钮 / 空格 / ↑：跳跃，可二段跳。
冲刺按钮 / Shift / X：短暂冲刺，可撞飞加班文件与“改一下”通知，冷却 3.2 秒。
收集冰美式。被催到不会失败，你仍然可以看完故事。
咖啡、被催次数会影响结局；放映有自己的片尾。
P 暂停；R 重来；按钮可随时返回封面。
默认静音，可开启合成音效。切后台会暂停，回前台需手动继续。

night-off.svg 为真正独立 SVG，可在支持的浏览器中作为文档打开。
注意：相册、文件管理器图片预览、或网页 <img> 会禁用 SVG 脚本，这是安全限制，不是文件坏了。
想稳妥地玩，请打开 HTML 入口。竖屏和横屏都有专门布局。

收集分 = 冰美式×10 + 撞飞KPI×15 - 被催×3。
历史最佳仅保存在本地浏览器，隐私模式无法保存也不影响游玩。
无外链、无字体下载、无跟踪、无 canvas、无视频贴图。
''',encoding='utf-8')
print(json.dumps({'out':str(OUT),'svg_bytes':len(svg.encode()),'html_bytes':len(html.encode())},ensure_ascii=False))
