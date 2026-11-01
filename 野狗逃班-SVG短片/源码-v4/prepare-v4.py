from pathlib import Path
import re
R=Path(__file__).parent
j=(R/'game-v3.js').read_text()
def rep(a,b):
 global j
 assert j.count(a)==1,(a[:100],j.count(a))
 j=j.replace(a,b)
rep("bossWon:false};","bossWon:false,offset:0,runCoins:0,mainReward:false,bossReward:false,guard:0,safeGap:0};")
rep("function start(mode){resetBoss();", "function start(mode){if(shopOpen)toggleShop(false);resetBoss();")
rep("{phase:'running',mode});", "{phase:'running',mode,guard:wallet.skill==='shield'&&mode==='play'?1:0});")
rep("function home(){resetBoss();", "function home(){if(shopOpen)toggleShop(false);resetBoss();")
rep("function pause(force){if(!", "function pause(force){if(shopOpen&&force!==true)return;if(!")
rep("function clearWorld(){for", "function clearWorld(){clearDashFX();for")
rep("function dashCore(){S.dash=.57;S.cool=S.phase==='boss'?1.1:S.freedom>0?1.6:3.2;S.inv=Math.max(S.inv,.68);", "function dashCore(){S.dash=.57;S.cool=dashCooldown();echoTick=0;S.inv=Math.max(S.inv,wallet.skill==='wind'?1.05:.98);")
# All player-relative coordinates, including collision/near-miss/boss projectiles, share one physical X.
j=j.replace('DOGX-', 'dogX()-').replace('DOGX+', 'dogX()+').replace('puff(DOGX,', 'puff(dogX(),').replace('ripple();','ripple(dogX());')
j=j.replace('translate(${DOGX}', 'translate(${dogX()}')
# rendering reflection should follow exactly, and speed remains legible rather than fake displacement
rep("(235+S.chapter*27)","(265+S.chapter*26)")
rep("(S.dash>0?1.75:S.freedom>0?1.16:1)","(S.dash>0?1.23:S.freedom>0?1.16:1)")
rep("if(S.comboTime===0)S.combo=0;music();", "updateDashMotion(dt);if(S.comboTime===0)S.combo=0;music();")
rep("[1.48,1.34,1.17,1.42][S.chapter]+rnd()*.18", "Math.max(S.safeGap,[1.03,.98,.91,1.19][S.chapter]+rnd()*.14)")
# Replace old spawn with intentional chapter patterns / coin arcs in features.
j=re.sub(r'function spawn\(\)\{.*?\}\n\nfunction score', 'function score',j, count=1,flags=re.S)
rep("const magnetic=S.freedom>0&&o.coffee&&Math.abs(o.x-(dogX()+17))<360;", "const magnetic=((S.freedom>0&&(o.coffee||o.coin)&&Math.abs(o.x-(dogX()+17))<360)||(wallet.skill==='magnet'&&(o.coffee||o.coin)&&Math.abs(o.x-(dogX()+17))<(o.coin?170:100)));")
rep("const dy=o.coffee?Math.sin(S.t*3+o.phase)*4:0;", "const dy=o.coffee||o.coin?Math.sin(S.t*3+o.phase)*4:0;")
rep("objCenter=o.y+(o.coffee?-29:-37)", "objCenter=o.y+(o.coin?-17:o.coffee?-29:-37)")
rep("const coll=dx<(o.coffee?62:64)&&vertical<(o.coffee?57:64);", "const coll=dx<(o.coin?42:o.coffee?62:64)&&vertical<(o.coin?44:o.coffee?57:64);")
j=j.replace('if(!o.coffee&&dx<65)', 'if(!o.coffee&&!o.coin&&dx<65)').replace('if(!o.done&&!o.coffee&&!o.near', 'if(!o.done&&!o.coffee&&!o.coin&&!o.near')
rep("if(!o.done&&coll){if(o.coffee){", "if(!o.done&&coll){if(o.coin){o.done=true;awardCoins(1);puff(o.x,o.y-18,3,'#ffe1a0');beep(1100,.055,'sine',.015)}else if(o.coffee){")
rep("else{S.hits++;S.inv=1.35;", "else if(consumeShield()){o.done=true}else{S.hits++;S.inv=1.35;")
rep("if(near&&!near.coffee&&S.cool===0)", "if(near&&!near.coffee&&!near.coin&&S.cool===0)")
rep("set('dashTrail','transform',`translate(0,${S.y})`)", "set('dashTrail','transform',`translate(${S.offset},${S.y})`)")
rep("set('freedomAura','transform',`translate(0,${S.y})`)", "set('freedomAura','transform',`translate(${S.offset},${S.y})`)")
rep("set('feedback','transform',`translate(0,${S.y-(.85-S.toast)*28})`)", "set('feedback','transform',`translate(${S.offset},${S.y-(.85-S.toast)*28})`)")
rep("S.cool/(S.phase==='boss'?1.1:S.freedom>0?1.6:3.2)","S.cool/dashCooldown()")
rep("bossLayout(W,sceneH);render()", "bossLayout(W,sceneH);v4Layout();render()")
rep("renderBoss();", "renderBoss();renderV4();")
rep("function end(){S.phase='ending';", "function end(){if(S.bossWon&&!S.bossReward){S.bossReward=true;awardCoins(30,'拆机奖励')}S.phase='ending';")
rep("function finishMain(){S.completedMain=true;", "function finishMain(){if(!S.mainReward){S.mainReward=true;awardCoins(12,'收工奖励')}S.completedMain=true;")
rep("S.dash=0;S.freedom=0;S.inv=0;S.cool=0;if(S.bossEligible)", "S.dash=0;S.offset=0;S.freedom=0;S.inv=0;S.cool=0;if(S.bossEligible)")
rep("freedom:0,energy:3,jumpBuffer:0", "freedom:0,energy:3,offset:0,guard:wallet.skill==='shield'?1:0,jumpBuffer:0")
rep("function bossDamage(){if(S.inv>0||S.dash>0||S.freedom>0||B.player<=0)return;", "function bossDamage(){if(S.inv>0||S.dash>0||S.freedom>0||B.player<=0)return;if(consumeShield())return;")
rep("const wasAir=S.y<0;S.vy+=1600*dt;", "const wasAir=S.y<0;S.vy+=1600*dt;") if False else None
rep("if(S.comboTime===0)S.combo=0;const wasAir", "updateDashMotion(dt);if(S.comboTime===0)S.combo=0;const wasAir")
rep("function renderBoss(){show('skillHud',S.phase==='running');", "function renderBoss(){show('skillHud',['running','boss','bossVictory'].includes(S.phase));")
rep("version:'3.0'", "version:'4.0',wallet:{...wallet,ownedSkins:[...wallet.ownedSkins],ownedSkills:[...wallet.ownedSkills]},shopOpen,storageOK")
rep("advance(seconds){for(let n=0;n<seconds*60;n++)step(1/60);render();return{...S}}", "advance(seconds){let remain=Math.max(0,Math.min(240,seconds));while(remain>1e-8){const dt=Math.min(remain,1/60);step(dt);remain-=dt}render();return{...S}}")
# QA snapshots deep copy and static collision info, deterministic timestamps remain action based.
rep("coffee:o.coffee,type:o.type", "coffee:o.coffee,coin:o.coin,type:o.type")
rep("ticket:makeTicket,bossStart:startBoss,scenario", "ticket:makeTicket,bossStart:startBoss,scenario")
rep("window.addEventListener('keydown',e=>{if(e.target.closest", "window.addEventListener('keydown',e=>{if(shopOpen)return;if(e.target.closest")
# paused input on restart/home stays deliberate: no utility buttons operate behind modal.
rep("function startBoss(){if(!S.bossEligible", "function startBoss(){if(shopOpen)return;if(!S.bossEligible")
# Ticket keeps new progression and skin visible, escape all labels.
rep("最高连击 ${S.maxCombo}  / 自由模式 ${S.superUses}  / 自由分 ${score()}", "最高连击 ${S.maxCombo} / 自由分 ${score()} / 金币 +${S.runCoins}")
rep("把加班留在身后，把凌晨还给自己。</text><text x=\"62\" y=\"547\"", "皮肤 ${escapeXML(CATALOG.skins.find(c=>c.id===wallet.skin).name)} / ${escapeXML(wallet.skill?CATALOG.skills.find(c=>c.id===wallet.skill).name:'原装野狗')} · 把凌晨还给自己。</text><text x=\"62\" y=\"547\"")
# Boss rendering is replaced below: no washed out hairline, true bounded danger band.
a=j.index("const key=B.state+':'+B.pattern+");b=j.index("set('bossBurst','transform'",a)
j=j[:a]+"renderBossBeam();"+j[b:]
features=(R/'v4-features.js').read_text()
# Fix accidental remaining DOGX-dependent effect anchor; function dogX itself is in separate features.
j=j.replace("layout();last=performance.now();requestAnimationFrame(frame);", features+"\n"+(R/'v4-beams.js').read_text()+"\nlayout();last=performance.now();requestAnimationFrame(frame);")
(R/'game-v4.js').write_text(j)
print('game-v4.js',len(j))
