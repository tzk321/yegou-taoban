from pathlib import Path
R=Path(__file__).parent
j=(R/'game-v5.js').read_text()
def rep(a,b):
 global j
 assert j.count(a)==1,(a[:100],j.count(a))
 j=j.replace(a,b)
# Frozen 5.0 is the entire input. Native night voyage, grant, archive and armored loop remain.
a=j.index('// v4 permanent local progression');j=j[:a].replace('wallet.skill','playSkill()')+j[a:]
a=j.index('function dashCooldown()');b=j.index('function cleanClone(',a);j=j[:a]+j[a:b].replace('wallet.skill','playSkill()')+j[b:]
a=j.index('// Four single-slot legends:');b=j.index('let shopPage=',a);j=j[:a]+j[a:b].replace('wallet.skill','playSkill()')+j[b:]
rep("guard:playSkill()==='shield'&&mode==='play'?1:0", "guard:routeSkill(nextRoute)==='shield'&&mode==='play'?1:0")
rep('function start(mode){if(voyagePanel)', 'function start(mode){if(hubOpen)toggleHub(false);if(voyagePanel)')
rep('function home(){abandonVoyage();', 'function home(){if(hubOpen)toggleHub(false);abandonVoyage();')
rep('beginVoyage(mode);svg.classList', 'beginVoyage(mode);beginExtension(mode);svg.classList')
rep('function voyageSpeed(base){', 'function voyageSpeed(base){if(isExtra())return extraSpeed(base);')
rep('function voyageGap(base){', 'function voyageGap(base){if(isExtra())return extraGap();')
rep('function spawnVoyage(){const list=', 'function spawnVoyage(){if(isExtra()){spawnExtra();return}const list=')
rep('function voyageDamage(){', 'function voyageDamage(){extraDamage();')
rep('function tickVoyage(dt){', 'function tickVoyage(dt){if(isExtra()){tickExtra(dt);return}')
rep("function finishVoyage(reason='complete'){", "function finishVoyage(reason='complete'){if(isExtra()){finishExtra(reason);return}")
rep("function voyageCoinValue(){return V.route==='story'?1:3}", "function voyageCoinValue(){return isExtra()?1:V.route==='story'?1:3}")
rep("V.route==='dojo'||V.finished)return;", "['dojo','tutorial'].includes(V.route)||V.finished)return;")
# Both collection paths, including legend attraction, feed the bag from actual pickups.
j=j.replace('S.coffee++;', 'S.coffee++;extraCoffee();')
rep('function jumpCore(){S.vy=', "function jumpCore(){extraAction('jump');S.vy=")
rep('function dashCore(){S.dash=', "function dashCore(){extraAction('dash');S.dash=")
rep('S.energy=0;S.freedom=freeDuration();', "extraAction('super');S.energy=0;S.freedom=freeDuration();")
rep('function runDuration(){return ', 'function runDuration(){return ' ) if False else None
rep('function voyageTicket(){const c=', 'function voyageTicket(){if(isExtra())return extraTicket();const c=')
rep("for(const[id,c]of Object.entries(ROUTES)){", "for(const[id,c]of Object.entries(ROUTES).filter(([id])=>['story','cruise','contract','endless','dojo'].includes(id))){")
rep("if((shopOpen||voyagePanel)&&force!==true)", "if((shopOpen||voyagePanel||hubOpen)&&force!==true)")
# Native controls and input protect all extra dialogs too.
j=j.replace("S.mode==='film'||voyagePanel||shopOpen", "S.mode==='film'||voyagePanel||hubOpen||shopOpen")
rep("if(shopOpen||voyagePanel)return;if(e.target.closest", "if(shopOpen||voyagePanel||hubOpen)return;if(e.target.closest")
rep("if(!voyagePanel&&!shopOpen&&['running','boss']", "if(!hubOpen&&!voyagePanel&&!shopOpen&&['running','boss']")
rep('function openVoyagePanel(which){', 'function openVoyagePanel(which){if(hubOpen)toggleHub(false);')
rep('function toggleShop(force){if(voyagePanel)', 'function toggleShop(force){if(hubOpen)toggleHub(false);if(voyagePanel)')
rep("if(S.phase!=='cover'||shopOpen)return;const keys=", "if(hubOpen||S.phase!=='cover'||shopOpen)return;const keys=")
rep("renderVoyage()}", "renderVoyage();renderExtension()}")
rep('v4Layout();voyageLayout();render()', 'v4Layout();voyageLayout();extensionLayout();render()')
j=j.replace('mobile?1250','mobile?1350')
rep("version:'5.0'", "version:'5.1'")
rep('get:()=>({...S,score:score(),mobile', 'get:()=>({...S,score:isExtra()?extraScore():score(),mobile')
rep('voyage:voyageSnapshot(),shopOpen', 'extras:extraSnapshot(),voyage:voyageSnapshot(),shopOpen')
rep("const whale=S.t>92&&S.phase==='running'?", "const whale=V.route==='story'&&S.t>92&&S.phase==='running'?")
rep("show('revealCaption',S.phase==='running'&&S.t>94", "show('revealCaption',V.route==='story'&&S.phase==='running'&&S.t>94")
rep('applySkin();layout();last=performance.now();requestAnimationFrame(frame);', (R/'gallery-runtime.js').read_text()+'\n'+(R/'gallery-panel.js').read_text()+'\ninitExtension();applySkin();layout();last=performance.now();requestAnimationFrame(frame);')
(R/'game-v51.js').write_text(j)
print('game-v51.js',len(j.encode()))
