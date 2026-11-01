from pathlib import Path
R=Path(__file__).parent
# Keep test intent while replacing only explicitly authorized balanced numeric specs.
p=R/'qa-v5-boundaries.mjs'
s=p.read_text().replace("'qa-v5-boundaries.json'","'qa-v52-native-boundaries.json'")
(R/'qa-v52-native-boundaries.mjs').write_text(s)
p=R/'qa-v5-economy.mjs';s=p.read_text().replace("assert.equal(after.freedom,6.8)","assert.equal(after.freedom,4.4)").replace('whale-super-still-breaks-armored-no-skill-nerf','balanced-whale-super-breaks-armored').replace("'qa-v5-economy.json'","'qa-v52-native-economy.json'")
s=s.replace("__nightQA.scenario({t:65,inv:999});__nightQA.advance(2)","__nightQA.scenario({t:65,inv:999});(()=>{for(let i=0;i<6000;i++){const s=__nightOff,o=__nightQA.inspect().find(o=>o.armored&&o.x>300+s.offset-50&&o.x<300+s.offset+480);if(o)return;__nightQA.advance(1/120)}throw Error(\"No natural armored obstacle within whale480\")})()")
(R/'qa-v52-native-economy.mjs').write_text(s)
p=R/'qa-v5-balance.mjs';s=p.read_text().replace("'qa-v5-balance.json'","'qa-v52-native-balance.json'")
(R/'qa-v52-native-balance.mjs').write_text(s)
p=R/'qa-v51-integration.mjs';s=p.read_text().replace("s.version,'5.1'","s.version,'5.2'").replace("chrono,5","chrono,2.4").replace("__extraQA.start('wildrun');__nightQA.advance(61)","__extraQA.start('wildrun');__nightQA.scenario({inv:999});__nightQA.advance(61)").replace("__extraQA.start('endless');__nightQA.advance(61)","__extraQA.start('endless');__nightQA.scenario({inv:999});__nightQA.advance(61)").replace("'qa-v51-integration.json'","'qa-v52-native-integration.json'")
s=s.replace("pass('raw-endless-and-armored-supplied-v5-loop-both-retained',s.voyage)","pass('raw-endless-and-armored-supplied-v5-loop-both-retained-explicit-inv-rule-isolation',s.voyage)")
(R/'qa-v52-native-integration.mjs').write_text(s)
print('Old intents retained; new strength specs, no cancellation of nerfs. Explicit inv scenario only for independent shield-supply rule after orbit no longer guarantees survival. Whale test waits for natural armored obstacle within reduced480 range rather than assuming old900 range.')
