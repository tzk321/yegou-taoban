// Same-wallet cross-page serialization. Local gains are deltas; spending is never merged by max(balance).
let persistBase=null,persistQueue=Promise.resolve(),persistPending=0;
const plain=x=>JSON.parse(JSON.stringify(x)),same=(a,b)=>JSON.stringify(a)===JSON.stringify(b);
try{persistBase=JSON.parse(localStorage.getItem('nightOffProgressV4')||'null')}catch(e){storageOK=false}
if(!persistBase||typeof persistBase!=='object')persistBase=plain(wallet);
function mergeSave(old,next,live,path=''){
 if(same(old,next))return live===undefined?(next===undefined?undefined:plain(next)):live;
 if(Array.isArray(next)){const current=Array.isArray(live)?live:[];if(['ownedSkins','ownedSkills','achievements','secrets','seen','contracts'].includes(path.split('.').at(-1))||path==='voyage.extras.maps.wins')return [...new Set([...current,...next])];return plain(next)}
 if(next&&typeof next==='object'){
  const result={...(live&&typeof live==='object'?live:{})};for(const[k,v]of Object.entries(next)){const p=path?path+'.'+k:k;result[k]=mergeSave(old?.[k],v,result[k],p)}return result
 }
 if(typeof next==='number'){
  if(path==='balance')return bounded((Number(live)||0)+next-(Number(old)||0),0,1e9);
  const k=path.split('.').at(-1);if(['runs','wins','storyRuns','bossWins','delivered'].includes(k))return Math.max(0,(Number(live)||0)+next-(Number(old)||0));
  if(['score','best','endlessBest'].includes(k))return Math.max(Number(live)||0,next);
  if(k==='time'&&path.startsWith('voyage.extras.maps.records.'))return live===undefined?next:Math.min(Number(live)||200,next);
  if(k==='time'||k==='t')return Math.max(Number(live)||0,next);
 }
 if(path==='voyage.devClaimed')return live===true||next===true;
 return next
}
function persistenceWrite(old,next){let live=null;try{live=JSON.parse(localStorage.getItem('nightOffProgressV4')||'null')}catch(e){storageOK=false}if(!live||typeof live!=='object')live=plain(old);
 const oldMaps=plain(old.voyage?.extras?.maps||{}),newMaps=plain(next.voyage?.extras?.maps||{}),liveMaps=plain(live.voyage?.extras?.maps||{}),merged=mergeSave(old,next,plain(live));let duplicate=0;
 if(old.voyage?.devClaimed!==true&&next.voyage?.devClaimed===true&&live.voyage?.devClaimed===true)duplicate+=Math.min(100000,Math.max(0,next.balance-old.balance));
 const added=(newMaps?.wins||[]).filter(i=>!(oldMaps?.wins||[]).includes(i));for(const i of added)if((liveMaps?.wins||[]).includes(i)){const entry=newMaps?.awards?.[String(i)];duplicate+=Math.min(entry?.amount||0,Math.max(0,next.balance-old.balance))}
 merged.balance=bounded((Number(live.balance)||0)+(Number(next.balance)||0)-(Number(old.balance)||0)-duplicate,0,1e9);
 if(newMaps&&merged.voyage?.extras?.maps){const dst=merged.voyage.extras.maps,c=newMaps.checkpoint,prev=oldMaps?.checkpoint,current=liveMaps?.checkpoint;if(same(c,prev))dst.checkpoint=current??c??null;else if(!c&&current&&prev?.runId!==current.runId)dst.checkpoint=current;else if(c&&current&&c.runId!==current.runId&&(c.createdAt||0)<(current.createdAt||0))dst.checkpoint=current;else dst.checkpoint=c??null}
 try{localStorage.setItem('nightOffProgressV4',JSON.stringify(merged));storageOK=true}catch(e){storageOK=false;return plain(next)}
 if(duplicate){if(isMap()&&M.settled){S.runCoins=Math.max(0,S.runCoins-duplicate);V.resultCoins=Math.max(0,V.resultCoins-duplicate)}toast('同存档已经领过 / 不重复发米','#c4ddbe')}return merged
}
function saveWallet(){const old=plain(persistBase||wallet),next=plain(wallet);persistBase=next;persistPending++;
 const work=()=>{const out=persistenceWrite(old,next);persistPending--;if(persistPending===0){wallet.balance=out.balance;persistBase.balance=out.balance;journey.devClaimed=journey.devClaimed||out.voyage?.devClaimed===true;persistBase.voyage.devClaimed=journey.devClaimed;if(!storageOK&&voyagePanel==='dev'&&journey.devClaimed)pinMessage='已领取 / 存储受限，仅本页有效';for(const i of out.voyage?.extras?.maps?.wins||[])if(NIGHTS[i]&&!mapStore.wins.includes(i))mapStore.wins.push(i);render()}return out};
 if(navigator.locks?.request){persistQueue=persistQueue.catch(()=>{}).then(()=>navigator.locks.request('nightOffProgressV4-write',work)).catch(()=>{storageOK=false;persistPending=Math.max(0,persistPending-1)});window.__nightPersistence=persistQueue}else{work();persistQueue=Promise.resolve();window.__nightPersistence=persistQueue}return persistQueue
}
window.addEventListener('storage',e=>{if(e.key!=='nightOffProgressV4'||persistPending)return;try{const raw=JSON.parse(e.newValue||'null');if(!raw||typeof raw!=='object')return;wallet.balance=bounded(raw.balance,0,1e9);wallet.ownedSkins=[...new Set(['original',...wallet.ownedSkins,...(raw.ownedSkins||[]).filter(i=>CATALOG.skins.some(c=>c.id===i))])];wallet.ownedSkills=[...new Set([...wallet.ownedSkills,...(raw.ownedSkills||[]).filter(i=>CATALOG.skills.some(c=>c.id===i))])];journey.devClaimed=journey.devClaimed||raw.voyage?.devClaimed===true;const mp=raw.voyage?.extras?.maps;if(mp){for(const i of Array.isArray(mp.wins)?mp.wins:[])if(Number.isInteger(i)&&NIGHTS[i]&&!mapStore.wins.includes(i))mapStore.wins.push(i);mapStore.checkpoint=mp.checkpoint??null}persistBase.balance=wallet.balance;persistBase.ownedSkins=[...wallet.ownedSkins];persistBase.ownedSkills=[...wallet.ownedSkills];persistBase.voyage.devClaimed=journey.devClaimed;if(!persistBase.voyage.extras)persistBase.voyage.extras={};if(!persistBase.voyage.extras.maps)persistBase.voyage.extras.maps={};persistBase.voyage.extras.maps.checkpoint=plain(raw.voyage?.extras?.maps?.checkpoint??null);render()}catch(x){}});
