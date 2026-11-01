import fs from 'node:fs';import crypto from 'node:crypto';import {createRequire}from'node:module';const require=createRequire(import.meta.url),acorn=require('acorn'),R=new URL('.',import.meta.url);const read=n=>fs.readFileSync(new URL(n,R),'utf8');let t=read('frozen-game-v52.js');if(crypto.createHash('sha256').update(t).digest('hex')!=='3cdfcbcc3613719e574f4edae091a52131c83741ff9a8d8214ccfd58ed1206ef')throw Error('frozen 5.2 hash mismatch');const modules=['mobility-v60.js','bullets-v60.js','gear-v60.js','audio-v60.js','polish-v60.js','tuning-v60.js'].map(read);const ast=s=>acorn.parse(s,{ecmaVersion:'latest'}),names=new Set(modules.flatMap(s=>ast(s).body.filter(x=>x.type==='FunctionDeclaration').map(x=>x.id.name)));const nodes=ast(t).body[0].expression.callee.body.body.filter(x=>x.type==='FunctionDeclaration'&&names.has(x.id.name));for(const n of nodes.sort((a,b)=>b.start-a.start))t=t.slice(0,n.start)+t.slice(n.end);function swap(a,b){if(t.split(a).length!==2)throw Error('unique patch '+a.slice(0,140)+' count '+(t.split(a).length-1));t=t.replace(a,b)}
swap("const defaults={phase:","const defaults={move:0,moveVX:0,phase:");
swap("let wallet={balance:",read('catalog-v60.js')+'\nlet wallet={balance:');
swap("function clearWorld(){resetLegend();","function clearWorld(){clearBullets();clearNewGear();releaseMove();S.move=0;S.moveVX=0;counterCool=0;resetLegend();");
swap("function dashCore(){extraAction('dash');","function dashCore(){if(playSkill()==='rail'&&simClock-lastRailDash<8-1e-8)return;if(playSkill()==='rail'){lastRailDash=simClock;railHistory.push(simClock);if(railHistory.length>100)railHistory.shift()}extraAction('dash');");
swap("legendDash();if(S.phase==='boss')shootBoss(1)","legendDash();newDashGear();if(S.phase==='boss')shootBoss(1)");
swap("S.superUses++;S.inv=Math.max(S.inv,freeDuration()+.35);S.cool=0;","S.superUses++;S.inv=Math.max(S.inv,freeDuration()+.35);if(playSkill()!=='rail')S.cool=0;");
swap("S.jumps++;S.jumpBuffer=0;","S.jumps++;if(S.jumps===2&&playSkill()==='echo')landArmed=true;S.jumpBuffer=0;");
swap("ripple(dogX());puff(dogX(),GROUND,5", "ripple(dogX());v60Land();puff(dogX(),GROUND,5");
swap("mapObjects(worldDt);S.chapter", "mapObjects(worldDt);refreshDanger();S.chapter");
swap("mapDecorate(obj);items.push(obj)","mapDecorate(obj);decorateDanger(obj);items.push(obj)");
swap("renderVoyage();renderExtension();renderMaps()}","renderVoyage();renderExtension();renderMaps();renderV60()}");
swap("extensionLayout();render()}","extensionLayout();v60Layout();render()}");
swap("if(sound)unlockAudio();render();beep(620,.12)","if(sound||musicOn)unlockAudio();render();beep(620,.12)");
swap("if(sound&&audio){try{(S.paused?audio.suspend():audio.resume()).catch(()=>{})}catch(e){}}else if(sound&&!S.paused)unlockAudio();last=performance.now()", "if((sound||musicOn)&&audio){try{(S.paused?audio.suspend():audio.resume()).catch(()=>{})}catch(e){}}else if((sound||musicOn)&&!S.paused)unlockAudio();if(S.paused){releaseMove();stopMusic()}audioLifecycle();last=performance.now();render()");
swap("else if(audio)audio.suspend().catch(()=>{})", "else if(audio&&!musicOn)audio.suspend().catch(()=>{})");
swap("sceneH=mobile?810:compact?500:710","sceneH=mobile?900:compact?560:780");
swap("set('scene','viewBox',mobile?'0 -140 800 900':'0 0 1280 710')","set('scene','viewBox',mobile?'0 -100 800 1000':'0 40 1280 780')");
swap("set('scene','viewBox','0 150 1280 500')","set('scene','viewBox','0 190 1280 560')");
swap("['magnet','orbit'].includes(playSkill())","['magnet','orbit','nightvision'].includes(playSkill())");
swap("(playSkill()==='orbit'?135:o.coin?140:85)","(playSkill()==='orbit'?135:o.coin?140:85)+(playSkill()==='nightvision'?40:0)");
swap("function bossFail(){if(isMap())", "function bossFail(){clearBullets();if(isMap())");
swap("function mapBossFail(){S.phase=", "function mapBossFail(){clearBullets();S.phase=");
swap("S.cool=0;S.inv=Math.max(S.inv,.5)","if(playSkill()!=='rail')S.cool=0;S.inv=Math.max(S.inv,.5)");
swap("openAtLaunch:B.state==='open'", "serial:B.openSerial,openAtLaunch:B.state==='open'");
swap("serial:B.openSerial});B.notice=''", "serial:B.openSerial});B.notice=''");
swap("function legendAccessory(g,id){const add=", "function legendAccessory(g,id){if(['mecha','nebula'].includes(id)){extraAccessory(g,id);return}const add=");
swap("function drawPreviewFX(c){const g=", "function drawPreviewFX(c){if(polishPreview(c))return;if(['prism','echo'].includes(c.id)){newGearPreview(c);return}const g=");
swap("const t=reduced?0:demoClock,p=(t%(c.id==='rail'?2.6:c.id==='orbit'?2.1:2.6))/(c.id==='orbit'?2.1:2.6);", "const t=reduced?0:demoClock,cycle=c.id==='rail'?8:c.id==='echo'?6:c.id==='orbit'?2.1:3.2,p=(t%cycle)/cycle;if(['prism','echo'].includes(c.id)){set('detailFX','transform',c.id==='echo'?`translate(0,-15) scale(${.25+p*.8}) translate(0,15)`:`translate(${-Math.min(1,p*3)*55},0)`);set('detailFX','opacity',reduced?1:c.id==='prism'?(t%3.2<.9?1:.18):(t%6<.5?1:.18));set('detailDog','transform',c.id==='echo'?`translate(0,${p<.35?-Math.sin(p/.35*Math.PI)*80:0})`:'translate(0,0)');return}");
swap("rail:{price:800,desc:'手动雷弧 / 最多穿三障',detail:'冲刺真实雷弧，最多穿三障，沿途收币；跑图冷却2.6秒、Boss1.6秒且反击1伤。每窗最多2伤。雷弧破障不回能。'}", "rail:{price:800,desc:'雷冲8秒 / 最多穿三障',detail:'所有装备路线雷冲实际冷却8秒，大招、绿窗、转阶段都不重置。真实雷弧最多破三障，不回能；Boss可用独立反击/F，每窗最多2伤。'}");
t=t.replaceAll("version:'5.2'","version:'6.0'").replaceAll(/野狗逃班 5\.[0123]/g,'野狗逃班 6.0');
// Enlarge control shelf only; scene coordinate system and previous patience HUD fix remain frozen.
swap("const W=mobile?720:1280,H=mobile?1350:compact?800:940,sceneH=", "const W=mobile?720:1280,H=mobile?1380:compact?860:1040,sceneH=");
swap("function layout(){const w=", "function layout(){const oldMobile=mobile;const w=");
swap("bossLayout(W,sceneH);v4Layout();", "if(oldMobile!==mobile&&V.route!=='daily'){const before=oldMobile?800:1280,after=mobile?800:1280;for(const o of items)if(o.x>before)o.x+=after-before}bossLayout(W,sceneH);v4Layout();");
// Full-window root + native fullscreen from trusted start gestures, never crop or stretch the controls.
swap("svg.style.width=Math.min(w,h*W/H)+'px';svg.style.height=Math.min(h,w*H/W)+'px';", "svg.style.width=w+'px';svg.style.height=h+'px';");
swap("bind('fullBtn',()=>{try{const p=document.fullscreenElement?document.exitFullscreen():document.documentElement.requestFullscreen?.();if(p&&p.catch)p.catch(()=>{})}catch(e){}});", "bind('fullBtn',toggleGameFullscreen);");
swap("function layout(){const oldMobile=mobile;const w=", "function layout(){releaseMove();const oldMobile=mobile;const w=");
swap("function start(mode){if(hubOpen)", "function start(mode){requestGameFullscreen(false);if(hubOpen)");
// Narrow performance hooks; physics/collision clocks stay exact.
swap("const show=(id,yes)=>$(id).classList.toggle('hide',!yes);", "const show=(id,yes)=>{const e=$(id);if(POLISH_HIDDEN.has(id))yes=false;if(e.classList.contains('hide')===yes)e.classList.toggle('hide',!yes)};");
if(t.split('extraCoffee();gainEnergy();').length!==3)throw Error('coffee hook count');t=t.replaceAll('extraCoffee();gainEnergy();','extraCoffee();gainEnergy();polishCoffee();');
swap("S.vy+=1600*dt;S.y+=S.vy*dt;", "S.vy+=1600*dt;polishAir();S.y+=S.vy*dt;");
swap("const x=dogX();if(['boss','bossVictory'].includes(S.phase)){pos('skillHud',mobile?26:28,mobile?120:126);pos('bossCallout',mobile?55:400,mobile?180:126)}else pos('skillHud',mobile?26:884,mobile?98:27);", "const x=dogX();");
// Static HUD geometry is authored once per resize/phase, not alternated by legacy HUDs each frame.
for(const target of ["set('energyFill','d','M137 25h'+(119*(S.freedom>0?S.freedom/3.8:S.energy/6)));", "set('energyFill','d','M137 25h'+(119*(S.freedom>0?S.freedom/freeDuration():S.energy/6)));", "text('superLabel',S.freedom>0?'自由 '+S.freedom.toFixed(1)+'s':'自由模式');", "text('superHint',S.energy===6?'点击 / E 释放':'冰美式 '+Math.floor(S.energy)+' / 6');", "if(playSkill()==='leviathan')text('superLabel',S.freedom>0?'鲸落 '+S.freedom.toFixed(1)+'s':'鲸落清场');if(playSkill()==='chrono')text('superLabel',S.chrono>0?'时停 '+S.chrono.toFixed(1)+'s':'拒绝时间');if(playSkill()==='orbit')text('superLabel',S.freedom>0?'万纸 '+S.freedom.toFixed(1)+'s':'万纸归宗')"]){swap(target,'')}
// The playable dog, reflection and dash echo share one scale; pickups stay forgiving, hostile hitboxes shrink.
swap("set('dog','transform',`translate(${dogX()},${GROUND+S.y})`)","set('dog','transform',playerDrawTransform())");
swap("set('dogReflection','transform',`translate(${dogX()},${572-S.y*.35}) scale(1,-.34)`)","set('dogReflection','transform',`translate(${dogX()+17*(1-PLAYER_SCALE)},${572-S.y*.35}) scale(${PLAYER_SCALE},${-.34*PLAYER_SCALE})`)");
swap("transform:`translate(${dogX()-15},${GROUND+S.y})`,opacity:.3", "transform:playerDrawTransform(dogX()-15),opacity:.3");
swap("const dogCenter=GROUND+S.y-65;", "const dogCenter=playerCenter().y;");
swap("const coll=!o.ghost&&dx<(o.coin?42:o.coffee||o.token?62:64)&&vertical<(o.coin?44:o.coffee||o.token?57:64);", "const coll=runnerContact(o,dx,vertical);");
// Original shadow/trail effects follow both walking and dash displacement.
t=t.replaceAll('translate(${S.offset},','translate(${(S.move||0)+S.offset},');
swap("initExtension();initMaps();applySkin();layout();", modules.join('\n')+"\ninitV60();initExtension();initMaps();applySkin();layout();");
ast(t);fs.writeFileSync(new URL('game-v60.js',R),t);console.log('6.0 prepared',Buffer.byteLength(t),'bytes');
