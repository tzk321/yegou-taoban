import {boot,cmd,nav,view,ev,report,close,errors,externals} from './qa-lib.mjs';
import {routeBot} from './qa-v52-bots.mjs';
import assert from 'node:assert/strict';
const tests=[];
try {
 await boot(9532); await cmd('Page.addScriptToEvaluateOnNewDocument',{source:'window.requestAnimationFrame=()=>0'}); await view(390,844); await nav(); await ev('localStorage.clear()'); await nav();
 await ev('__mapsQA.start(0)'); const r=await ev(routeBot); assert.equal(r.state.phase,'bossGate');
 await ev('window.__nightPersistence||Promise.resolve()');const checkpoint=await ev('__mapsQA.store().checkpoint');
 // Only isolated fixture storage: resume a legal owned skin/skill, not minting coins.
 await ev(`(()=>{const p=JSON.parse(localStorage.getItem('nightOffProgressV4'));p.ownedSkills=['wind'];p.ownedSkins.push('neon');p.voyage.extras.maps.checkpoint.skill='wind';p.voyage.extras.maps.checkpoint.skin='neon';localStorage.setItem('nightOffProgressV4',JSON.stringify(p))})()`);
 await nav(); await ev('__mapsQA.start(0)');
 const s=await ev('__nightOff'); assert.equal(s.phase,'bossGate'); assert.equal(s.maps.runId,checkpoint.runId); assert.equal(s.voyage.gear,'equipped'); assert.equal(s.maps.skill,'wind');
 assert.equal(await ev("document.getElementById('dog').getAttribute('data-skin')"),'neon');
 await ev('__mapsQA.boss();__nightQA.advance(.3)');
 assert((await ev("document.getElementById('skinTrails').childElementCount"))>0);
 tests.push({name:'checkpoint reload locked equipped ranking and actual neon trails',passed:true});
 assert.equal(errors.length,0);assert.equal(externals.length,0);
 await report('qa-v52-codex.json',true,tests,{note:'Isolated CDP 9532; RAF disabled; legal route bot. Owned-gear fixture only for checkpoint test; not natural victory or device FPS.'});
} catch(e){await report('qa-v52-codex.json',false,tests,{error:String(e)});process.exitCode=1} finally {close()}
