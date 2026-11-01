from pathlib import Path
import shutil,json,hashlib,zipfile
R=Path(__file__).parent;P=R/'交付-v5.2';S=P/'源码-v5.2';Q=P/'验收-v5.2'
S.mkdir(parents=True,exist_ok=True);Q.mkdir(parents=True,exist_ok=True)
source=['game-v51.js','game-v5.js','game-v41.js','game-v4.js','game-v3.js','build-v1.py','build-v2-base.py','build-v3.py','build-v4.py','build-v41.py','build-v5.py','build-v51.py','build-v52.py','prepare-v52.py','maps-art.py','maps-art.svgfrag','arcade-art.py','arcade-art.svgfrag','boss-art.svgfrag','boss-ui.svgfrag','legend-art.svgfrag','voyage-ui.svgfrag','maps-catalog.js','maps-runtime.js','maps-panel.js','night-scenes.js','balance-runtime.js','persistence-v52.js','game-v52.js','qa-lib.mjs','qa-planner.mjs','qa-v52-bots.mjs','refresh-regressions.py','run-full-final.sh','README-v52.txt','DESIGN-v52.md','升级-v5.2.txt','先读我-交接-v5.2.md','CODEX-REVIEW-ROUND2.md','OCR-复核-v52.md','verify-final-reports.py','package-v52.py','rebuild-v52.py','SOURCE-RULES.md','verify-source-package.py','qa-v52-shared-specs.json']
source += [p.name for p in R.glob('qa-*.mjs')]
source += ['clean-isolated-profiles.py','run-full-final.sh','rebuild-v52.py','release-status.py']
for f in sorted(set(source)):shutil.copy2(R/f,S/f)
shutil.copy2(R/'README-v52.txt',S/'README.txt')
for p in (R/'night-off-out').glob('qa-v52-*.json'):shutil.copy2(p,Q/p.name)
for p in (R/'night-off-out').glob('v52-*.png'):shutil.copy2(p,Q/p.name)
for f in ['build-manifest.json','night-off.html','night-off.svg']:shutil.copy2(R/'night-off-out'/f,P/f)
for f in ['README-v52.txt','升级-v5.2.txt','先读我-交接-v5.2.md','CODEX-REVIEW-ROUND2.md','OCR-复核-v52.md']:shutil.copy2(R/f,P/f)
info=json.loads((P/'build-manifest.json').read_text());reports=[]
for p in Q.glob('qa*.json'):
 d=json.loads(p.read_text());assert d.get('success') and d.get('artifact_sha256')==info['sha256'],(p.name,d.get('success'),d.get('artifact_sha256'));reports.append({'file':p.name,'tests':len(d['tests']),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
previous={}
if (Q/'验收总览-v5.2.json').exists():previous=json.loads((Q/'验收总览-v5.2.json').read_text())
summary={'version':'5.2','artifact_sha256':info['sha256'],'html_bytes':info['html_bytes'],'reports':reports,'passed':sum(p['tests'] for p in reports),'report_count':len(reports),'rebuild_verified':False,'physical_phone_gameplay':False}
if previous.get('artifact_sha256')==info['sha256'] and previous.get('rebuild_verified'):
 summary['rebuild_verified']=True;summary['rebuild_comparisons']=previous.get('rebuild_comparisons',[])
(Q/'验收总览-v5.2.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2))
Z=R/'野狗逃班-v5.2-源码与验收.zip'
with zipfile.ZipFile(Z,'w',zipfile.ZIP_DEFLATED) as z:
 for p in P.rglob('*'):
  if p.is_file():z.write(p,str(p.relative_to(P)))
print('package reports',len(reports),'tests',summary['passed'],'zip',Z.stat().st_size)
