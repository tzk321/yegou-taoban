from pathlib import Path
import hashlib,json,shutil,zipfile,subprocess
R=Path(__file__).parent;O=R/'night-off-out';D=R/'交付-v7.0';D.mkdir(exist_ok=True)
S=D/'源码-v7.0';A=D/'验收-v7.0';S.mkdir(exist_ok=True);A.mkdir(exist_ok=True)
source=['frozen-game-v52.js','frozen-v52.svg','catalog-v70.js','mobility-v70.js','bullets-v70.js','gear-v70.js','audio-v70.js','polish-v70.js','tuning-v70.js','skillfx-v70.js','qa-skillfx-v70.mjs','qa-skillfx-raf-v70.mjs','SKILLFX-v70.md','run-perf-compare.sh','prepare-v70.mjs','build-v70.py','game-v70.js','FORK-v70.json','STATUS-v70.md','README-v70.txt','单文件分享说明.txt','DESIGN-v70.md','验收边界说明.md','先读我-交接-v7.0.md','CODEX-REVIEW-v53.md','CODEX-审查落实.md','下一轮-交接-v7.0.md','package-v70.py','qa-lib.mjs','qa-bots-v70.mjs','qa-bosses-v70.mjs','qa-mechanisms-v70.mjs','qa-audio-v70.mjs','qa-bgm-level-v70.mjs','qa-visual-v70.mjs','qa-realtime-v70.mjs','qa-regression-v70.mjs','qa-hud-v70.mjs','qa-movehud-v70.mjs','qa-persistence-v70.mjs','qa-observable-v70.mjs','qa-overlap-v70.mjs','qa-gear-matrix-v70.mjs','qa-lastedges-v70.mjs','qa-grant-quota-v70.mjs','qa-public-v70.mjs','qa-stick-fullscreen-v70.mjs','qa-polish-v70.mjs','qa-tuning-v70.mjs','qa-newgear-matrix-v70.mjs','qa-perf-v70.mjs','bench-polish.mjs','write-perf-summary.py','gate-suite.sh','build-check.sh','clean-profiles.py','validate-audit.mjs','release-verify.py','post-public-package.py','audit-proof.py','verify-artifacts-v70.py','升级-v7.0.txt']
for n in source:shutil.copy2(R/n,S/n)
shutil.copy2(R/'README-v70.txt',S/'README.txt')
reports=['qa-bosses-v70.json','qa-mechanisms-v70.json','qa-audio-v70.json','qa-bgm-level-v70.json','qa-visual-v70.json','qa-realtime-v70.json','qa-regression-v70.json','qa-hud-v70.json','qa-movehud-v70.json','qa-persistence-v70.json','qa-observable-v70.json','qa-overlap-v70.json','qa-gear-matrix-v70.json','qa-lastedges-v70.json','qa-grant-quota-v70.json','qa-audit-v70.json','qa-stick-fullscreen-v70.json','qa-polish-v70.json','qa-tuning-v70.json','qa-newgear-matrix-v70.json','qa-perf-v70.json','qa-skillfx-v70.json','qa-skillfx-raf-v70.json']
h=hashlib.sha256((O/'night-off.html').read_bytes()).hexdigest();summary=[]
for n in reports:
 p=O/n;d=json.loads(p.read_text());assert d['success']and d['artifact_sha256']==h,(n,d.get('success'),d.get('artifact_sha256'),h);assert all(t['passed']for t in d['tests']);assert not d.get('errors') and not d.get('externals');shutil.copy2(p,A/n);summary.append({'report':n,'tests':len(d['tests']),'success':True,'artifact_sha256':h})
I=R/'rebuild-v70-isolated'
if I.exists():shutil.rmtree(I)
shutil.copytree(S,I)
for cmd in [['node','prepare-v70.mjs'],['node','--check','game-v70.js'],['python3','build-v70.py']]:subprocess.run(cmd,cwd=I,check=True,capture_output=True)
proof={'success':True,'artifact_sha256':h,'html_equal':(I/'night-off-out/night-off.html').read_bytes()==(O/'night-off.html').read_bytes(),'svg_equal':(I/'night-off-out/night-off.svg').read_bytes()==(O/'night-off.svg').read_bytes(),'note':'Copied public source into independent directory and rebuilt only with packaged files'};assert proof['html_equal']and proof['svg_equal'];(A/'rebuild-proof-v70.json').write_text(json.dumps(proof,ensure_ascii=False,indent=2))
for n in ['night-off.html','night-off.svg','build-manifest.json']:shutil.copy2(O/n,D/n)
for n in ['README-v70.txt','下一轮-交接-v7.0.md','先读我-交接-v7.0.md','升级-v7.0.txt','FORK-v70.json','STATUS-v70.md']:shutil.copy2(R/n,D/n)
shutil.copy2(R/'SKILLFX-v70.md',D/'SKILLFX-v70.md')
shutil.copy2(R/'单文件分享说明.txt',D/'单文件分享说明.txt')
for p in O.glob('v70-*.png'):
 if 'probe' not in p.name and 'before' not in p.name:shutil.copy2(p,A/p.name)
# No release can be packaged with a missing or stale performance after-sample.
assert (O/'bench-after.json').exists(),'missing final performance benchmark'
assert json.loads((O/'bench-baseline.json').read_text())['artifact_sha256']=='78639afd827d23130d9263fb82799555b347e5ae6751741232eeaed6ef0536a5'
for n in ['bench-baseline.json','bench-after.json','性能对照-v7.0.md']:
 p=O/n
 if p.exists():
  if n=='bench-after.json':assert json.loads(p.read_text())['artifact_sha256']==h,'performance benchmark stale'
  shutil.copy2(p,A/n)
summary={'version':'7.0','success':True,'artifact_sha256':h,'reports':summary,'report_count':len(summary),'test_count':sum(r['tests']for r in summary),'rebuild':proof,'note':'Isolated Chromium/CDP, not physical phone gameplay/FPS/speaker listening; ordinary public entry post-copy report added after release.'};(A/'总览-v7.0.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2))
zipPath=R/'野狗逃班-v7.0-源码与验收.zip'
with zipfile.ZipFile(zipPath,'w',zipfile.ZIP_DEFLATED,6)as z:
 for p in sorted(D.rglob('*')):
  if p.is_file():z.write(p,str(p.relative_to(D)))
print(json.dumps({'zip':str(zipPath),'hash':h,'reports':summary['report_count'],'tests':summary['test_count'],'rebuild':True},ensure_ascii=False))
