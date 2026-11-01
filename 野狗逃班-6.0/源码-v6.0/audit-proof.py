from pathlib import Path
import subprocess,json,hashlib
R=Path(__file__).parent;O=R/'night-off-out'
r=subprocess.run(['node','validate-audit.mjs'],cwd=R,capture_output=True,text=True,check=True);d=json.loads(r.stdout)
assert d['hostileDamageCallers']==['bossDamage','mapBossDamage','tickBullets'];assert not d['duplicateFunctions']
assert hashlib.sha256((R/'frozen-game-v52.js').read_bytes()).hexdigest()=='3cdfcbcc3613719e574f4edae091a52131c83741ff9a8d8214ccfd58ed1206ef'
p=Path('/sdcard/Download/野狗逃班-SVG短片/旧版-v5.2-弹幕机动前/野狗逃班.html');assert hashlib.sha256(p.read_bytes()).hexdigest()=='63e87b2f62b3ddc8bf720bbc95700650404079e88e93706f74080d0bd6c93be3'
proof={'success':True,'artifact_sha256':hashlib.sha256((O/'night-off.html').read_bytes()).hexdigest(),'tests':[{'name':'All hostile damage call sites originate only in visible bullet integrator','passed':True,'data':d},{'name':'Frozen 5.2 source and actual pre-release baseline backup hash verified','passed':True}],'environment':'Static AST callsite audit plus SHA256 byte checks, complementary to actual Chromium collision tests.'}
html=(O/'night-off.html').read_text();js=(R/'game-v60.js').read_text();manifest=json.loads((O/'build-manifest.json').read_text())
assert manifest['version']=='6.0' and "version:'6.0'" in js and '<title>野狗逃班 6.0' in html
assert '6.0 / 全屏夜行' in js and '野狗逃班 5.' not in js
assert 'nightOffProgressV4' in js and "localStorage.getItem('nightOffAudioV53')" in js
assert not any(s in js for s in ['nightOffProgressV6',"nightOffAudioV60"])
assert hashlib.sha256(Path('/sdcard/Download/野狗逃班.html').read_bytes()).hexdigest()=='e598bab91e88711decee3eac7d79b2df55bee624168ba68645ec6b99d4ad1811'
assert hashlib.sha256(Path('/sdcard/Download/野狗逃班.svg').read_bytes()).hexdigest()=='0dd9fa36ee6565258cefe4c511df93ae020f2bcdfe42046f6da5bf4f7563ee36'
assert manifest['skills']==14 and 'const BGM_GAIN=.8' in js
proof['tests'] += [{'name':'6.0 title cover runtime manifest and ticket branding consistent','passed':True},{'name':'Legacy wallet and audio keys retained without second wallet','passed':True},{'name':'5.3 original HTML and SVG remain byte-identical during independent 6.0 construction','passed':True}]
(O/'qa-audit-v60.json').write_text(json.dumps(proof,ensure_ascii=False,indent=2));print(json.dumps(proof,ensure_ascii=False))
