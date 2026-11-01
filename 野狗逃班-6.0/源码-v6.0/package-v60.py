from pathlib import Path
import hashlib,json,shutil,zipfile,subprocess
R=Path(__file__).parent;O=R/'night-off-out';D=R/'交付-v6.0';D.mkdir(exist_ok=True)
S=D/'源码-v6.0';A=D/'验收-v6.0';S.mkdir(exist_ok=True);A.mkdir(exist_ok=True)
source=['frozen-game-v52.js','frozen-v52.svg','catalog-v60.js','mobility-v60.js','bullets-v60.js','gear-v60.js','audio-v60.js','polish-v60.js','tuning-v60.js','prepare-v60.mjs','build-v60.py','game-v60.js','FORK-v60.json','STATUS-v60.md','README-v60.txt','DESIGN-v60.md','验收边界说明.md','先读我-交接-v6.0.md','CODEX-REVIEW-v53.md','CODEX-审查落实.md','下一轮-交接-v6.0.md','package-v60.py','qa-lib.mjs','qa-bots-v60.mjs','qa-bosses-v60.mjs','qa-mechanisms-v60.mjs','qa-audio-v60.mjs','qa-bgm-level-v60.mjs','qa-visual-v60.mjs','qa-realtime-v60.mjs','qa-regression-v60.mjs','qa-hud-v60.mjs','qa-movehud-v60.mjs','qa-persistence-v60.mjs','qa-observable-v60.mjs','qa-overlap-v60.mjs','qa-gear-matrix-v60.mjs','qa-lastedges-v60.mjs','qa-grant-quota-v60.mjs','qa-public-v60.mjs','qa-stick-fullscreen-v60.mjs','qa-polish-v60.mjs','qa-tuning-v60.mjs','qa-newgear-matrix-v60.mjs','qa-perf-v60.mjs','bench-polish.mjs','write-perf-summary.py','gate-suite.sh','build-check.sh','clean-profiles.py','validate-audit.mjs','release-verify.py','post-public-package.py','audit-proof.py','verify-artifacts-v60.py','升级-v6.0.txt']
for n in source:shutil.copy2(R/n,S/n)
shutil.copy2(R/'README-v60.txt',S/'README.txt')
reports=['qa-bosses-v60.json','qa-mechanisms-v60.json','qa-audio-v60.json','qa-bgm-level-v60.json','qa-visual-v60.json','qa-realtime-v60.json','qa-regression-v60.json','qa-hud-v60.json','qa-movehud-v60.json','qa-persistence-v60.json','qa-observable-v60.json','qa-overlap-v60.json','qa-gear-matrix-v60.json','qa-lastedges-v60.json','qa-grant-quota-v60.json','qa-audit-v60.json','qa-stick-fullscreen-v60.json','qa-polish-v60.json','qa-tuning-v60.json','qa-newgear-matrix-v60.json','qa-perf-v60.json']
h=hashlib.sha256((O/'night-off.html').read_bytes()).hexdigest();summary=[]
for n in reports:
 p=O/n;d=json.loads(p.read_text());assert d['success']and d['artifact_sha256']==h,(n,d.get('success'),d.get('artifact_sha256'),h);assert all(t['passed']for t in d['tests']);assert not d.get('errors') and not d.get('externals');shutil.copy2(p,A/n);summary.append({'report':n,'tests':len(d['tests']),'success':True,'artifact_sha256':h})
I=R/'rebuild-v60-isolated'
if I.exists():shutil.rmtree(I)
shutil.copytree(S,I)
for cmd in [['node','prepare-v60.mjs'],['node','--check','game-v60.js'],['python3','build-v60.py']]:subprocess.run(cmd,cwd=I,check=True,capture_output=True)
proof={'success':True,'artifact_sha256':h,'html_equal':(I/'night-off-out/night-off.html').read_bytes()==(O/'night-off.html').read_bytes(),'svg_equal':(I/'night-off-out/night-off.svg').read_bytes()==(O/'night-off.svg').read_bytes(),'note':'Copied public source into independent directory and rebuilt only with packaged files'};assert proof['html_equal']and proof['svg_equal'];(A/'rebuild-proof-v60.json').write_text(json.dumps(proof,ensure_ascii=False,indent=2))
for n in ['night-off.html','night-off.svg','build-manifest.json']:shutil.copy2(O/n,D/n)
for n in ['README-v60.txt','下一轮-交接-v6.0.md','先读我-交接-v6.0.md','升级-v6.0.txt','FORK-v60.json','STATUS-v60.md']:shutil.copy2(R/n,D/n)
for p in O.glob('v60-*.png'):
 if 'probe' not in p.name and 'before' not in p.name:shutil.copy2(p,A/p.name)
for n in ['bench-baseline.json','bench-after.json','性能对照-v6.0.md']:
 p=O/n
 if p.exists():
  if n=='bench-after.json':assert json.loads(p.read_text())['artifact_sha256']==h,'performance benchmark stale'
  shutil.copy2(p,A/n)
summary={'version':'6.0','success':True,'artifact_sha256':h,'reports':summary,'report_count':len(summary),'test_count':sum(r['tests']for r in summary),'rebuild':proof,'note':'Isolated Chromium/CDP, not physical phone gameplay/FPS/speaker listening; ordinary public entry post-copy report added after release.'};(A/'总览-v6.0.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2))
zipPath=R/'野狗逃班-v6.0-源码与验收.zip'
with zipfile.ZipFile(zipPath,'w',zipfile.ZIP_DEFLATED,6)as z:
 for p in sorted(D.rglob('*')):
  if p.is_file():z.write(p,str(p.relative_to(D)))
print(json.dumps({'zip':str(zipPath),'hash':h,'reports':summary['report_count'],'tests':summary['test_count'],'rebuild':True},ensure_ascii=False))
