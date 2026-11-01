from pathlib import Path
R=Path(__file__).parent
j=(R/'game-v4.js').read_text()
def rep(a,b):
 global j
 assert j.count(a)==1,(a[:90],j.count(a))
 j=j.replace(a,b)
rep('guard:0,safeGap:0};','guard:0,safeGap:0,chrono:0,legendPulse:0,orbitTick:0,paperTick:0,whaleTick:0,legendSerial:-1};')
rep('function clearWorld(){clearDashFX();','function clearWorld(){resetLegend();clearDashFX();')
rep('function dashCore(){S.dash=.57;','function dashCore(){S.dash=.57;') if False else None
rep("if(S.phase==='boss')shootBoss(S.freedom>0?2:1)","legendDash();if(S.phase==='boss')shootBoss(wallet.skill==='rail'?2:S.freedom>0?2:1)")
rep('S.energy=0;S.freedom=3.8;S.superUses++;S.inv=Math.max(S.inv,4.15);','S.energy=0;S.freedom=freeDuration();S.superUses++;S.inv=Math.max(S.inv,freeDuration()+.35);')
rep("if(S.phase==='boss'&&B.state==='open')shootBoss(2)","if(S.phase==='boss'&&B.state==='open'&&!['leviathan','orbit'].includes(wallet.skill))shootBoss(2);legendSuper()")
rep("if(S.phase!=='running')return;S.t=", "if(S.phase!=='running')return;const worldDt=tickLegend(dt);S.t=")
rep('S.distance+=speed*dt;', 'S.distance+=speed*worldDt;')
rep('S.spawn-=dt;', 'S.spawn-=worldDt;')
rep('for(const o of items){o.x-=speed*dt;', 'for(const o of items){if(o.done)continue;o.x-=speed*worldDt;')
rep("wallet.skill==='magnet'&&(o.coffee||o.coin)","['magnet','orbit'].includes(wallet.skill)&&(o.coffee||o.coin)")
rep("<(o.coin?170:100)","<(wallet.skill==='orbit'?210:o.coin?170:100)")
rep('function stepBoss(dt){if(!', 'function stepBoss(dt){if(!') if False else None
rep("||S.paused)return;B.t+=dt;B.elapsed+=dt;B.flash=Math.max(0,B.flash-dt);", "||S.paused)return;const worldDt=S.phase==='boss'?tickLegend(dt):dt;B.t+=worldDt;B.elapsed+=worldDt;B.flash=Math.max(0,B.flash-dt);")
rep('B.timer-=dt;if(B.state', 'B.timer-=worldDt;if(B.state')
rep("freedom:0,energy:3,offset:0,guard:","freedom:0,energy:3,offset:0,chrono:0,orbitTick:0,paperTick:0,whaleTick:0,legendSerial:-1,legendPulse:0,guard:")
rep("S.dash=0;S.offset=0;S.freedom=0;S.inv=0;", "S.dash=0;S.offset=0;S.freedom=0;S.chrono=0;S.inv=0;")
rep("S.paused=false;S.freedom=0;S.dash=0;show('bossResult'", "S.paused=false;S.freedom=0;S.chrono=0;S.dash=0;show('bossResult'")
rep("S.bossWon=true;S.freedom=0;S.dash=0;", "S.bossWon=true;S.freedom=0;S.chrono=0;S.dash=0;")
rep('renderBoss();renderV4();', 'renderBoss();renderV4();renderLegend();')
rep('idle+=Math.min(delta,.08);', 'idle+=Math.min(delta,.08);') if False else None
rep('last=now;if(!S.paused){idle', 'last=now;if(shopOpen&&detailId){demoClock+=Math.min(delta,.05);renderDemo()}if(!S.paused){idle')
rep("version:'4.0'", "version:'4.1'")
rep('shopOpen,storageOK,duration:', 'shopOpen,storageOK,shopPage,detailId,legendBolts:legendBolts.length,duration:')
rep("if(e.key==='Escape'&&shopOpen)","if(e.key==='Escape'&&shopOpen)") if False else None
# Replace v4 feature section, keeping all unrelated gameplay untouched.
a=j.index('// v4 permanent local progression');b=j.index('function renderBossBeam()',a)
f=(R/'v4-features.js').read_text()
f=f.replace("let wallet=",(R/'legend-catalog.js').read_text()+'\nlet wallet=',1)
# Old single-page shop functions replaced with pagination/details; bindings must use visible page.
for name,nextname in [('purchase','shopLayout'),('shopLayout','renderShop'),('renderShop','renderV4')]:
 x=f.index('function '+name+'(');y=f.index('function '+nextname+'(',x);f=f[:x]+f[y:]
f=f.replace("CATALOG[shopTab][i]?.id", "shopCards()[i]?.id")
f=f.replace("shopTab='skins';shopNotice='';", "shopTab='skins';shopPage=0;buyConfirm='';detailId='';show('shopDetail',false);shopNotice='';")
f=f.replace("shopOpen=false;show('shopPanel',false)", "shopOpen=false;detailId='';buyConfirm='';show('shopDetail',false);show('shopPanel',false)")
f=f.replace("shopTab='skins';shopLayout()", "shopTab='skins';shopPage=0;buyConfirm='';closeDetail();shopLayout()")
f=f.replace("shopTab='skills';shopLayout()", "shopTab='skills';shopPage=0;buyConfirm='';closeDetail();shopLayout()")
f=f.replace("e.preventDefault();toggleShop(false)", "e.preventDefault();detailId?closeDetail():toggleShop(false)")
f=f.replace("function dashCooldown(){return ","function dashCooldown(){if(wallet.skill==='chrono'&&S.chrono>0)return .45;if(wallet.skill==='rail')return S.phase==='boss'?.85:1.8;return ")
f=f.replace("function skinAccessory(g,id){if", "function skinAccessory(g,id){if(LEGEND_SKINS.some(c=>c.id===id)){legendAccessory(g,id);return}if")
f=f.replace("function emitEcho(){if", "function emitEcho(){if") if False else f
f=f.replace("pos('coinHud',mobile?390:1000,mobile?145:136);", "pos('coinHud',mobile?390:1000,mobile?145:136);pos('legendHUD',mobile?390:900,mobile?192:183);if(compact)pos('legendHUD',mobile?390:900,183);set('legendFlash','width',mobile?720:1280);set('legendFlash','height',mobile?810:compact?500:710);")
f=f.replace('applySkin();','')
j=j[:a]+f+'\n'+(R/'legend-runtime.js').read_text()+'\n'+(R/'legend-shop.js').read_text()+'\n'+j[b:]
rep('layout();last=performance.now();requestAnimationFrame(frame);','applySkin();layout();last=performance.now();requestAnimationFrame(frame);')
(R/'game-v41.js').write_text(j)
print('game-v41.js',len(j))
