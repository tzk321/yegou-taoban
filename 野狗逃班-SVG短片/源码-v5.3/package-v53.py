from pathlib import Path
import hashlib,json,shutil,zipfile,subprocess
R=Path(__file__).parent;O=R/'night-off-out';D=R/'交付-v5.3';D.mkdir(exist_ok=True)
S=D/'源码-v5.3';A=D/'验收-v5.3';S.mkdir(exist_ok=True);A.mkdir(exist_ok=True)
source=['frozen-game-v52.js','frozen-v52.svg','catalog-v53.js','mobility-v53.js','bullets-v53.js','gear-v53.js','audio-v53.js','prepare-v53.mjs','build-v53.py','game-v53.js','README-v53.txt','DESIGN-v53.md','验收边界说明.md','先读我-交接-v5.3.md','CODEX-REVIEW-v53.md','CODEX-审查落实.md','下一轮-交接-v5.3.md','package-v53.py','qa-lib.mjs','qa-bots-v53.mjs','qa-bosses-v53.mjs','qa-mechanisms-v53.mjs','qa-audio-v53.mjs','qa-visual-v53.mjs','qa-realtime-v53.mjs','qa-regression-v53.mjs','qa-hud-v53.mjs','qa-movehud-v53.mjs','qa-persistence-v53.mjs','qa-observable-v53.mjs','qa-overlap-v53.mjs','qa-gear-matrix-v53.mjs','qa-lastedges-v53.mjs','qa-grant-quota-v53.mjs','qa-public-v53.mjs','qa-stick-fullscreen-v53.mjs','gate-suite.sh','build-check.sh','clean-profiles.py','validate-audit.mjs','release-verify.py','post-public-package.py','audit-proof.py','verify-artifacts-v53.py','升级-v5.3.txt']
for n in source:shutil.copy2(R/n,S/n)
shutil.copy2(R/'README-v53.txt',S/'README.txt')
reports=['qa-bosses-v53.json','qa-mechanisms-v53.json','qa-audio-v53.json','qa-visual-v53.json','qa-realtime-v53.json','qa-regression-v53.json','qa-hud-v53.json','qa-movehud-v53.json','qa-persistence-v53.json','qa-observable-v53.json','qa-overlap-v53.json','qa-gear-matrix-v53.json','qa-lastedges-v53.json','qa-grant-quota-v53.json','qa-audit-v53.json','qa-stick-fullscreen-v53.json']
h=hashlib.sha256((O/'night-off.html').read_bytes()).hexdigest();summary=[]
for n in reports:
 p=O/n;d=json.loads(p.read_text());assert d['success']and d['artifact_sha256']==h,(n,d.get('success'),d.get('artifact_sha256'),h);assert all(t['passed']for t in d['tests']);shutil.copy2(p,A/n);summary.append({'report':n,'tests':len(d['tests']),'success':True,'artifact_sha256':h})
I=R/'rebuild-v53-isolated'
if I.exists():shutil.rmtree(I)
shutil.copytree(S,I)
for cmd in [['node','prepare-v53.mjs'],['node','--check','game-v53.js'],['python3','build-v53.py']]:subprocess.run(cmd,cwd=I,check=True,capture_output=True)
proof={'success':True,'artifact_sha256':h,'html_equal':(I/'night-off-out/night-off.html').read_bytes()==(O/'night-off.html').read_bytes(),'svg_equal':(I/'night-off-out/night-off.svg').read_bytes()==(O/'night-off.svg').read_bytes(),'note':'Copied public source into independent directory and rebuilt only with packaged files'};assert proof['html_equal']and proof['svg_equal'];(A/'rebuild-proof-v53.json').write_text(json.dumps(proof,ensure_ascii=False,indent=2))
for n in ['night-off.html','night-off.svg','build-manifest.json']:shutil.copy2(O/n,D/n)
for n in ['README-v53.txt','先读我-交接-v5.3.md','升级-v5.3.txt']:shutil.copy2(R/n,D/n)
for p in O.glob('v53-*.png'):shutil.copy2(p,A/p.name)
summary={'version':'5.3','success':True,'artifact_sha256':h,'reports':summary,'report_count':len(summary),'test_count':sum(r['tests']for r in summary),'rebuild':proof,'note':'Isolated Chromium/CDP, not physical phone gameplay/FPS/speaker listening; ordinary public entry post-copy report added after release.'};(A/'总览-v5.3.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2))
zipPath=R/'野狗逃班-v5.3-源码与验收.zip'
with zipfile.ZipFile(zipPath,'w',zipfile.ZIP_DEFLATED,6)as z:
 for p in sorted(D.rglob('*')):
  if p.is_file():z.write(p,str(p.relative_to(D)))
print(json.dumps({'zip':str(zipPath),'hash':h,'reports':summary['report_count'],'tests':summary['test_count'],'rebuild':True},ensure_ascii=False))
