from pathlib import Path
import subprocess,json,hashlib
R=Path(__file__).parent;O=R/'night-off-out'
r=subprocess.run(['node','validate-audit.mjs'],cwd=R,capture_output=True,text=True,check=True);d=json.loads(r.stdout)
assert d['hostileDamageCallers']==['bossDamage','mapBossDamage','tickBullets'];assert not d['duplicateFunctions']
assert hashlib.sha256((R/'frozen-game-v52.js').read_bytes()).hexdigest()=='3cdfcbcc3613719e574f4edae091a52131c83741ff9a8d8214ccfd58ed1206ef'
p=Path('/sdcard/Download/野狗逃班-SVG短片/旧版-v5.2-弹幕机动前/野狗逃班.html');assert hashlib.sha256(p.read_bytes()).hexdigest()=='63e87b2f62b3ddc8bf720bbc95700650404079e88e93706f74080d0bd6c93be3'
proof={'success':True,'artifact_sha256':hashlib.sha256((O/'night-off.html').read_bytes()).hexdigest(),'tests':[{'name':'All hostile damage call sites originate only in visible bullet integrator','passed':True,'data':d},{'name':'Frozen 5.2 source and actual pre-release baseline backup hash verified','passed':True}],'environment':'Static AST callsite audit plus SHA256 byte checks, complementary to actual Chromium collision tests.'}
(O/'qa-audit-v53.json').write_text(json.dumps(proof,ensure_ascii=False,indent=2));print(json.dumps(proof,ensure_ascii=False))
