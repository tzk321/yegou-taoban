from pathlib import Path
import hashlib
R=Path(__file__).parent
base=(R/'game-v51.js').read_text();j=base
assert hashlib.sha256(base.encode()).hexdigest()=='4537bb5fa69dcadf809e7819b9b29d3d3541d98a27e4cf86d999e227a8412474', '5.1 frozen baseline modified'
def rep(a,b):
 global j
 assert j.count(a)==1,(a[:120],j.count(a))
 j=j.replace(a,b)
def function(name,nextname,new):
 global j
 a=j.index('function '+name+'(');b=j.index('function '+nextname+'(',a);j=j[:a]+new+'\n'+j[b:]
balance=(R/'balance-runtime.js').read_text()
for name,nxt in [('freeDuration','resetLegend'),('dashCooldown','updateDashMotion'),('legendSuper','tickLegend'),('tickLegend','legendAccessory')]:
 a=balance.index('function '+name+'(');b=balance.find('\nfunction ',a+1)
 if b<0:b=balance.index('\nconst BALANCE_COPY',a)
 function(name,nxt,balance[a:b])
rep('beginExtension(mode);svg.classList','beginExtension(mode);beginMap();applySkin();svg.classList')
rep('function home(){if(hubOpen)', 'function home(){clearMapFight();if(hubOpen)')
rep('function finishMain(){if(V.route', "function finishMain(){if(isMap()){if(S.phase==='running')mapGate();return}if(V.route")
rep('function makeTicket(){if(V.route', 'function makeTicket(){if(isMap())return mapTicket();if(V.route')
rep('clock*145', 'clock*85')
rep('function end(){if(V.route',"function end(){if(isMap()){mapSettle(false);return}if(V.route")
rep('function stepBoss(dt){','function stepBoss(dt){if(isMap()){stepMapBoss(dt);return}')
rep('function startBoss(){','function startBoss(){if(isMap()){mapBossStart();return}')
rep('function bossFail(){','function bossFail(){if(isMap()){mapBossFail();return}')
rep('function shootBoss(power){','function shootBoss(power){if(isMap()){mapShoot(power);return}')
rep('function hitBoss(power,openAtLaunch=false){','function hitBoss(power,openAtLaunch=false){')
rep("B.hp=Math.max(0,B.hp-power);B.landed++", "const cap=['orbit','leviathan','chrono'].includes(playSkill())?3:2;power=Math.min(power,cap-(B.windowDamage||0));if(power<=0)return;B.windowDamage=(B.windowDamage||0)+power;B.hp=Math.max(0,B.hp-power);B.landed++")
rep("B.openSerial++;B.notice='';S.cool", "B.openSerial++;B.windowDamage=0;B.notice='';S.cool")
rep("if(S.phase==='boss')shootBoss(playSkill()==='rail'?2:S.freedom>0?2:1)","if(S.phase==='boss')shootBoss(1)")
rep("if(S.phase==='boss'&&B.state==='open'&&!['leviathan','orbit'].includes(playSkill()))shootBoss(2)","if(S.phase==='boss'&&B.state==='open'&&!['leviathan','orbit'].includes(playSkill()))shootBoss(isMap()?1:2)")
rep('function renderBoss(){','function renderBoss(){if(isMap()){renderMapBoss();return}')
# Landscape: the bottom caption bar sat exactly on the dog's feet; drop it clear of the player.
rep("set('subtitleBg','y',408);set('subtitleBg','height',72);set('subtitleLine','y',452);",
    "set('subtitleBg','y',420);set('subtitleBg','height',72);set('subtitleLine','y',464);")
# gallery-panel.js is frozen inside the 5.1 baseline, so badge layout is patched here, not in the file.
rep("pos('extraBadge',mobile?26:28,mobile?245:233);set('extraBadgeBG','width',mobile?668:690);set('extraBadgeText','font-size',mobile?21:23);",
    "pos('extraBadge',mobile?26:compact?420:28,mobile?246:compact?104:150);set('extraBadgeBG','width',mobile?620:470);set('extraBadgeBG','height',mobile?78:compact?72:64);set('extraBadgeText','x',mobile?24:22);set('extraBadgeText','y',mobile?52:compact?48:44);set('extraBadgeText','font-size',mobile?34:compact?33:26);")
# Player patience must be readable: pips plus an explicit remaining count on the player line.
rep("text('bossHeartText','耐心 '+('◆ '.repeat(B.player))+('◇ '.repeat(3-B.player)));","text('bossHeartText','耐心 '+('◆'.repeat(B.player))+('◇'.repeat(3-B.player))+' '+B.player+'/3');")
rep('renderVoyage();renderExtension()}','renderVoyage();renderExtension();renderMaps()}')
rep("function retryVoyage(){if(voyagePanel)return;", "function retryVoyage(){if(voyagePanel)return;if(isMap()&&S.phase==='bossGate'){mapBossStart();return}if(isMap()&&S.phase==='ending'){playMap(M.id);return}")
rep('function voyageSpeed(base){if(isExtra())','function voyageSpeed(base){if(isMap())return mapSpeed();if(isExtra())')
rep('function voyageGap(base){if(isExtra())','function voyageGap(base){if(isMap())return night().gap+rnd()*.12;if(isExtra())')
rep('function spawnVoyage(){if(isExtra())','function spawnVoyage(){if(isMap()){spawnMap();return}if(isExtra())')
rep('function voyageDamage(){extraDamage();','function voyageDamage(){mapDamage();extraDamage();')
rep('function tickVoyage(dt){if(isExtra())','function tickVoyage(dt){if(isMap()){tickMap();return}if(isExtra())')
rep("function finishVoyage(reason='complete'){if(isExtra())","function finishVoyage(reason='complete'){if(isMap()){if(S.phase==='running')mapGate();else mapSettle(false);return}if(isExtra())")
rep("function voyageCoinValue(){return isExtra()?1:","function voyageCoinValue(){return isMap()?1:isExtra()?1:")
rep("function awardCoins(amount,source='金币'){", "function awardCoins(amount,source='金币'){if(mapAward(amount))return;")
rep("function route", "function route") if False else None
rep("routeSkill=route=>['daily','tutorial'].includes(route)?'':wallet.skill,playSkill=()=>routeSkill(V.route)","routeSkill=route=>['daily','tutorial'].includes(route)?'':wallet.skill,playSkill=()=>isMap()?M.skill:routeSkill(V.route)")
rep("S.chapter=V.route==='story'?", "mapObjects(worldDt);S.chapter=V.route==='story'?")
rep("const coll=dx<(o.coin?42:o.coffee?62:64)&&vertical<(o.coin?44:o.coffee?57:64)","const coll=!o.ghost&&dx<(o.coin?42:o.coffee||o.token?62:64)&&vertical<(o.coin?44:o.coffee||o.token?57:64)")
rep('if(!o.done&&coll){if(o.coin)', 'if(!o.done&&coll){if(o.token){mapToken(o)}else if(o.coin)')
# Token is a distinct interaction, never smashed or auto-collected.
rep('if(!o.coffee&&!o.coin&&dx<65)', 'if(!o.coffee&&!o.coin&&!o.token&&dx<65)')
rep('if(!o.done&&!o.coffee&&!o.coin&&!o.near', 'if(!o.done&&!o.coffee&&!o.coin&&!o.token&&!o.ghost&&!o.near')
rep("playSkill()==='orbit'?210:o.coin?170:100", "playSkill()==='orbit'?135:o.coin?140:85")
rep("S.smashed++;gainEnergy(.5);combo();legendBurst", "S.smashed++;combo();legendBurst")
rep("if(o.done||(o.armored&&S.freedom<=0))return", "if(o.done||o.token||o.ghost||(o.armored&&S.freedom<=0))return")
rep("items.push({el:g,x,y:GROUND+height,coffee,coin,type,done:false,phase:rnd()*7,minDy:1000,near:false})", "const obj={el:g,x,y:GROUND+height,coffee,coin,type,done:false,phase:rnd()*7,minDy:1000,near:false};mapDecorate(obj);items.push(obj)")
# Player visuals are tagged and updated at every route start; all clones carry the actual coat, not HUD-only state.
rep("paintSkin($('dogBody'),c,true);", "paintSkin($('dogBody'),c,true);attr($('dog'),'data-skin',c.id);attr($('dogBody'),'data-skin',c.id);set('dogCoat','fill','url(#coatGrad)');")
rep("const c=CATALOG.skins.find(c=>c.id===wallet.skin)||CATALOG.skins[0];paintSkin", "const c=CATALOG.skins.find(c=>c.id===lookSkin())||CATALOG.skins[0];paintSkin")
rep("playSkill()==='wind'?152:118", "playSkill()==='wind'?142:118")
rep("function tickSkinTrails(dt){const c=LEGEND_SKINS.find(c=>c.id===wallet.skin)", "function tickSkinTrails(dt){const c=LEGEND_SKINS.find(c=>c.id===lookSkin())")
rep("const skin=LEGEND_SKINS.find(c=>c.id===wallet.skin)", "const skin=LEGEND_SKINS.find(c=>c.id===lookSkin())")
rep("text('pauseText','暂停');render()}", "text('pauseText','暂停');applySkin();render()}")
rep("playSkill()==='orbit'?'万纸归宗 / 护体中'", "playSkill()==='orbit'?`纸护 / ${S.orbitTick>0?S.orbitTick.toFixed(1)+'s':'待拦截'}`")
rep("(5-S.chrono)*24", "(2.4-S.chrono)*24")
rep('openSerial:0};', 'openSerial:0,windowDamage:0};')
# Native detail previews use timed bursts reflecting the new intervals, no always-on passive advertisement.
rep("const t=reduced?0:demoClock,p=(t%2.6)/2.6", "const t=reduced?0:demoClock,p=(t%(c.id==='rail'?2.6:c.id==='orbit'?2.1:2.6))/(c.id==='orbit'?2.1:2.6)")
rep("set('detailFX','opacity',c.id==='rail'?reduced?.7:.28+Math.sin(p*Math.PI)*.68:1)","set('detailFX','opacity',reduced?.85:c.id==='rail'?p<.3?.95:.18:c.id==='orbit'?p<.3?1:.24:c.id==='chrono'?t%4<2.4?.9:.22:c.id==='leviathan'?t%6<4.4?.9:.15:1)")
# Gallery retains SVG download; new button enters an authored gameplay route.
function('drawMap','downloadLocal','function drawMap(g){drawPlayableMap(g)}')
function('saveWallet','awardCoins','// Wallet persistence is installed after all progression modules.')
rep("version:'5.1'", "version:'5.2'")
rep('score:isExtra()?extraScore():score(),mobile', "score:isMap()&&S.phase==='ending'?S.score:isExtra()?extraScore():score(),mobile")
rep('extras:extraSnapshot(),voyage:', 'maps:mapSnapshot(),extras:extraSnapshot(),voyage:')
rep("text('hubSubtitle','夜航全留 / 5.1 合流 · 地图与新支线')", "text('hubSubtitle','5.2 十二夜路 / 十二关 · 十二守夜者 · 旧玩法全留')")
rep('initExtension();applySkin();layout();last=performance.now();requestAnimationFrame(frame);', '\n'.join((R/f).read_text() for f in ['maps-catalog.js','maps-runtime.js','night-scenes.js','maps-panel.js','persistence-v52.js'])+'\n'+balance[balance.index('const BALANCE_COPY'):]+ '\ninitExtension();initMaps();applySkin();layout();last=performance.now();requestAnimationFrame(frame);')
(R/'game-v52.js').write_text(j)
print('frozen input',hashlib.sha256(base.encode()).hexdigest(),'5.2 runtime bytes',len(j.encode()))
