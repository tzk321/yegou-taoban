import{boot,cmd,nav,view,ev,report,close,errors,externals,click,shot}from'./qa-lib.mjs';
import{routeBot}from'./qa-bots-v53.mjs';
import assert from'node:assert/strict';
const tests=[],pass=(name,data)=>{tests.push({name,passed:true,data});console.log('HUD',name)};
// Anything painted AFTER the dog that overlaps it would visually cover it. Full-screen tints/weather are exempt.
const IGNORE=new Set(['v53UI','rain','transition','legendFlash','streetTint','nightWeather','speedRays','particles','landingRipples','feedback','feedbackText','legendBolts','dashEchoes','skinTrails','dogReflection','dogShadow','dashWind','dashNose','freedomAura','auraRing','guardRing','skinHalo','chronoFX','legendOrbit','legendWhale']);
const over=`(()=>{const IGNORE=new Set(${JSON.stringify([...IGNORE])});const dog=document.getElementById('dog'),dr=dog.getBoundingClientRect(),bad=[];
for(const e of document.querySelectorAll('#nightOff [id]')){
 if(!e.id||IGNORE.has(e.id)||e===dog||dog.contains(e)||e.contains(dog))continue;
 if(e.closest('.hide'))continue;
 if(!(dog.compareDocumentPosition(e)&Node.DOCUMENT_POSITION_FOLLOWING))continue;
 const r=e.getBoundingClientRect();if(r.width*r.height===0)continue;
 const ox=Math.min(dr.right,r.right)-Math.max(dr.left,r.left),oy=Math.min(dr.bottom,r.bottom)-Math.max(dr.top,r.top);
 if(ox>1&&oy>1)bad.push({id:e.id,area:Math.round(ox*oy)});
}
return{bad,dog:[Math.round(dr.left),Math.round(dr.top),Math.round(dr.right),Math.round(dr.bottom)]}})()`;
const vitExpr=`(()=>{const g=document.getElementById('extraBadge'),bg=document.getElementById('extraBadgeBG'),t=document.getElementById('extraBadgeText'),r=g.getBoundingClientRect();
return{hide:!!g.closest('.hide'),text:t.textContent,font:Number(t.getAttribute('font-size')),textW:Math.round(t.getBBox().width),bgW:Number(bg.getAttribute('width')),bgH:Number(bg.getAttribute('height')),screenH:Math.round(r.height),screenW:Math.round(r.width),box:[Math.round(r.left),Math.round(r.top),Math.round(r.right),Math.round(r.bottom)]}})()`;
const vitals=()=>ev(vitExpr);
async function seed(skill=''){await nav();await ev(`localStorage.clear();localStorage.setItem('nightOffProgressV4',JSON.stringify({balance:5000,ownedSkins:['original','dragon'],ownedSkills:['wind','magnet','shield','rail','orbit','leviathan','chrono'],skin:'dragon',skill:${JSON.stringify(skill)},voyage:{devClaimed:true}}))`);await nav()}
try{await boot(9567);await cmd('Page.addScriptToEvaluateOnNewDocument',{source:'window.requestAnimationFrame=()=>0'});
for(const[w,h]of[[390,844],[844,390],[1365,900]]){
 await view(w,h);
 await seed('orbit');await ev('__mapsQA.start(0)');await ev('__nightQA.advance(4)');
 let v=await vitals(),o=await ev(over);
 assert(!v.hide,'vitals hidden in map run');assert.equal(o.bad.length,0,JSON.stringify(o));
 assert(v.textW<=v.bgW-24,'vitals text overflows box '+JSON.stringify(v));
 assert(v.font*Math.min(1,1)>=20,'vitals font too small '+JSON.stringify(v));
 pass(`map vitals clear of dog and readable ${w}x${h}`,v);
 await shot('v52-hud-vitals-'+w+'.png');
 await ev('__nightQA.jump();__nightQA.advance(.25)');o=await ev(over);
 assert.equal(o.bad.length,0,'apex '+JSON.stringify(o));
 pass(`map vitals clear of dog at jump apex ${w}x${h}`,o.dog);
 // spawn must enter from outside the visible viewBox, never pop mid-screen
 await click('homeBtn');await seed('orbit');await ev('__mapsQA.start(3);__nightQA.advance(.8)');
 const sp=await ev('__nightQA.inspect()');
 const right=mobile=>0;const edge=(await ev('__nightOff')).mobile?800:1280;
 assert(sp.length>0,'no spawn observed');assert(sp.every(x=>x.x>edge),'obstacle spawned inside viewport '+JSON.stringify(sp));
 pass(`obstacles spawn off-screen right ${w}x${h}`,{edge,xs:sp.map(x=>Math.round(x.x))});
 await click('homeBtn');
 // boss phase: player patience line readable
 await seed('shield');await ev('__mapsQA.start(0)');await ev(routeBot);await click('fightBtn');await ev('__nightQA.advance(5)');
 const bh=await ev(`(()=>{const e=document.getElementById('bossHeartText'),r=e.getBoundingClientRect();return{t:e.textContent,font:Number(e.getAttribute('font-size')),screenH:Math.round(r.height),box:[Math.round(r.left),Math.round(r.top)]}})()`);
 assert(/\d\/3/.test(bh.t),'boss patience has no explicit count '+bh.t);
 await click('homeBtn');
 await seed();await ev("__extraQA.start('courier');__nightQA.advance(3)");v=await vitals();
 assert(!v.hide);assert(v.textW<=v.bgW-24,'retained route badge overflows '+JSON.stringify(v));
 pass(`retained extra route badge fits ${w}x${h}`,v);
 await click('homeBtn');
}
assert.equal(errors.length,0);assert.equal(externals.length,0);
await report('qa-hud-v53.json',true,tests,{note:'Overlap measured on real DOM box geometry, painted-after-the-dog only, full-screen tints/weather/effects exempt. Not a physical phone.'});
}catch(e){console.error(e);await report('qa-hud-v53.json',false,tests,{error:String(e)});process.exitCode=1}finally{close()}
