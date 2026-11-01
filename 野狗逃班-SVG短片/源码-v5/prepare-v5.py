from pathlib import Path
R=Path(__file__).parent
j=(R/'game-v41.js').read_text()
def rep(a,b):
 global j
 assert j.count(a)==1,(a[:100],j.count(a))
 j=j.replace(a,b)
rep('const reduced=','let reduced=')
assert j.count('Math.min(1000000,')==2
j=j.replace('Math.min(1000000,','Math.min(1000000000,')
rep("function start(mode){if(shopOpen)","function start(mode){if(voyagePanel)closeVoyagePanel(false);if(shopOpen)")
rep("svg.classList.remove('paused');text('pauseText','暂停');show('cover',false);", "beginVoyage(mode);svg.classList.remove('paused');text('pauseText','暂停');show('cover',false);")
rep('function home(){if(shopOpen)', 'function home(){abandonVoyage();if(voyagePanel)closeVoyagePanel(false);if(shopOpen)')
rep('function end(){if(S.bossWon',"function end(){if(V.route!=='story'){finishVoyage(S.bossWon?'victory':'complete');return}recordStory();if(S.bossWon")
rep("if(S.phase!=='running')return;const worldDt=tickLegend(dt);S.t=Math.min(DURATION,S.t+dt);S.chapter=S.t<27?0:S.t<58?1:S.t<87?2:3;const revealSlow=S.t>92&&S.t<101?.72:1,speed=(265+S.chapter*26)*revealSlow*(S.dash>0?1.23:S.freedom>0?1.16:1);", "if(S.phase!=='running')return;const worldDt=tickLegend(dt);S.t=Math.min(runDuration(),S.t+dt);S.chapter=V.route==='story'?(S.t<27?0:S.t<58?1:S.t<87?2:3):Math.min(3,Math.floor(S.t/24)%4);const revealSlow=V.route==='story'&&S.t>92&&S.t<101?.72:1,speed=voyageSpeed((265+S.chapter*26)*revealSlow)*(S.dash>0?1.23:S.freedom>0?1.16:1);")
rep("S.t<113){if(S.t<90||S.t>101)spawn();S.spawn=Math.max(S.safeGap,[1.03,.98,.91,1.19][S.chapter]+rnd()*.14)","canVoyageSpawn()){if(V.route!=='story'||S.t<90||S.t>101)spawn();S.spawn=Math.max(S.safeGap,voyageGap([1.03,.98,.91,1.19][S.chapter]+rnd()*.14))")
rep("S.mode==='film'||S.inv>0", "S.mode==='film'||V.route==='cruise'||S.inv>0")
rep('S.hits++;S.inv=1.35;', 'S.hits++;S.inv=1.35;voyageDamage();')
rep('updateFX(dt);if(S.t>=DURATION)finishMain()', 'updateFX(dt);tickVoyage(dt);if(S.t>=runDuration())finishMain()')
rep('function finishMain(){if(!S.mainReward)',"function finishMain(){if(V.route!=='story'){finishVoyage('complete');return}if(!S.mainReward)")
rep("function awardCoins(amount,source='金币'){if(S.mode!=='play')return;", "function awardCoins(amount,source='金币'){if(S.mode!=='play'||V.route==='dojo'||V.finished)return;")
assert j.count('awardCoins(1)')==2
j=j.replace('awardCoins(1)','awardCoins(voyageCoinValue())')
rep('function spawn(){const chapters=', "function spawn(){if(V.route!=='story'){spawnVoyage();return}const chapters=")
rep("function legendBreak(o,color='#b7fae4'){if(o.done)return;", "function legendBreak(o,color='#b7fae4'){if(o.done||(o.armored&&S.freedom<=0))return;")
rep("S.phase==='running'&&S.t<6?", "S.phase==='running'&&S.t<6?") if False else None
rep("'空格 二段跳 · Shift 冲刺 · E 自由模式 · P 暂停')}","'空格 二段跳 · Shift 冲刺 · E 自由模式 · P 暂停');renderVoyage()}")
rep('bossLayout(W,sceneH);v4Layout();render()', 'bossLayout(W,sceneH);v4Layout();voyageLayout();render()')
rep('let delta=Math.max(0,(now-last)/1000||0);', 'let delta=Math.max(0,(now-last)/1000||0);tickVoyageIdle(Math.min(delta,.08));')
rep("if(shopOpen)return;if(e.target.closest", "if(shopOpen||voyagePanel)return;if(e.target.closest")
rep("if(['running','boss'].includes(S.phase)&&S.mode==='play'){e.preventDefault();jump()}","if(!voyagePanel&&!shopOpen&&['running','boss'].includes(S.phase)&&S.mode==='play'){e.preventDefault();jump()}")
rep("version:'4.1'", "version:'5.0'")
rep('shopOpen,storageOK,shopPage,detailId,', 'voyage:voyageSnapshot(),shopOpen,storageOK,shopPage,detailId,')
rep('coin:o.coin,type:o.type','coin:o.coin,type:o.type,armored:!!o.armored')
rep('function pause(force){if(shopOpen&&force!==true)return;', 'function pause(force){if((shopOpen||voyagePanel)&&force!==true)return;')
# Action button guards also cover pointer/programmatic click behind overlays.
rep("S.mode==='film')return;if(S.jumps", "S.mode==='film'||voyagePanel||shopOpen)return;if(S.jumps")
rep("S.mode==='film'||S.cool>0)return;", "S.mode==='film'||voyagePanel||shopOpen||S.cool>0)return;")
rep("S.mode==='film')return;activateFreedom()", "S.mode==='film'||voyagePanel||shopOpen)return;activateFreedom()")
rep("bind('restartBtn',()=>['boss','bossVictory','bossResult'].includes(S.phase)?startBoss():start(S.mode));", "bind('restartBtn',()=>retryVoyage());")
rep("bind('againBtn',()=>start(S.mode));", "bind('againBtn',()=>retryVoyage());")
rep("else if(k==='r')(['boss','bossVictory','bossResult'].includes(S.phase)?startBoss():start(S.mode))", "else if(k==='r')retryVoyage()")
rep('function makeTicket(){const title=', "function makeTicket(){if(V.route!=='story')return voyageTicket();const title=")
rep("function toggleShop(force){const next=", "function toggleShop(force){if(voyagePanel)closeVoyagePanel();const next=")
# Keep panel guard close/resume independent from shop guard.
rep("applySkin();layout();last=performance.now();requestAnimationFrame(frame);", (R/'voyage-runtime.js').read_text()+"\napplySkin();layout();last=performance.now();requestAnimationFrame(frame);")
(R/'game-v5.js').write_text(j)
print('game-v5.js',len(j.encode()))
