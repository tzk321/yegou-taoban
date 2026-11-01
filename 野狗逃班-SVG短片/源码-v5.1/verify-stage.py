from pathlib import Path
import json,hashlib,shutil,xml.etree.ElementTree as ET
R=Path(__file__).parent;O=R/'night-off-out';D=R/'交付-v5.1';D.mkdir(exist_ok=True)
html=O/'night-off.html';hh=hashlib.sha256(html.read_bytes()).hexdigest();assert html.stat().st_size>=524288
reports=['qa-v41','qa-v41-regression','qa-v41-edges','qa-v41-realtime','qa-v5','qa-v5-boundaries','qa-v5-balance','qa-v5-archive','qa-v5-economy','qa-v5-visual','qa-v5-results','qa-v5-benchmark','qa-v5-realtime','qa-v51-new','qa-v51-layout','qa-v51-balance','qa-v51-integration','qa-v51-edges','qa-v51-results','qa-v51-realtime','qa-v51-gallery-perf']
qa=[];total=0
for name in reports:
 p=O/(name+'.json');d=json.loads(p.read_text());assert d['success'],name;assert d['artifact_sha256']==hh,(name,'hash mismatch');assert not d['errors'] and not d['externals'],name;assert all(t['passed'] for t in d['tests']),name;total+=len(d['tests']);qa.append({'report':p.name,'tests':len(d['tests']),'success':True})
svg=ET.fromstring((O/'night-off.svg').read_text());ids=[e.attrib['id'] for e in svg.iter() if 'id'in e.attrib];assert len(ids)==len(set(ids));assert len([e for e in svg.iter() if e.attrib.get('id','').startswith('postcard')])==12
for x in svg.iter():
 for k,v in x.attrib.items():
  if k.endswith('href'):assert not v.startswith(('http:','https:','data:')),v
S=D/'源码-v5.1';Q=D/'验收-v5.1';S.mkdir(exist_ok=True);Q.mkdir(exist_ok=True)
# Frozen complete chain and additive true sources; never ship browser profiles or other user data.
source_names=['README-v51.txt','README.txt','DESIGN-v5.md','game-v5.js','game-v41.js','game-v4.js','game-v3.js','game-v51.js','gallery-runtime.js','gallery-panel.js','arcade-art.py','arcade-art.svgfrag','prepare-v51.py','build-v51.py','build-v5.py','build-v41.py','build-v4.py','build-v3.py','build-v2-base.py','build-v1.py','boss-art.svgfrag','boss-ui.svgfrag','legend-art.svgfrag','legend-catalog.js','legend-runtime.js','legend-shop.js','voyage-ui.svgfrag','voyage-runtime.js','qa-lib.mjs','qa-planner.mjs','verify-stage.py','qa-v51-delivered.mjs']
source_names += [name+'.mjs' for name in reports]
for name in sorted(set(source_names)):shutil.copy2(R/name,S/name)
shutil.copy2(R/'README-v51.txt',S/'README.txt')
for name in reports:shutil.copy2(O/(name+'.json'),Q/(name+'.json'))
shots=['v51-final-cover-mobile.png','v51-final-newroutes-mobile.png','v51-final-river-postcard-mobile.png','v51-final-river-postcard-desktop.png','v51-final-oldroutes-desktop.png','v51-journalTab-390.png','v51-settingsTab-390.png','v51-real-daily-ending.png','v51-real-courier-ending.png','v5-real-developer.png','v5-real-cruise-end.png','v5-real-dojo-win.png','v41-realtime-chrono-win.png','v41-legend-skins-mobile.png','v41-dragon-preview-mobile.png']
for name in shots:
 if (O/name).exists():shutil.copy2(O/name,Q/name)
summary={'version':'5.1','artifact_sha256':hh,'html_bytes':html.stat().st_size,'size_floor_bytes':524288,'reports':qa,'tests_total':total,'postcards':12,'old_main':'preserved frozen 5.0 plus additive extensions','wallet':'single nightOffProgressV4 with original voyage.devClaimed','environment':'Kali Chromium150/Node24 CDP emulated viewports, not physical phone gameplay','ordinary_clock':'native 90s cruise+60s contract+dojo win; new75s daily+90s courier; original120s film+real-time chrono Boss; no forced QA clocks for ordinary-entry suites','note':'Explicit unit QA scenarios/isolated test wallets named in each report. Independent 4.2 branch reports NOT counted.'}
for doc in ['截图OCR复核.md','升级-v5.1.txt','先读我-交接-v5.1.md']:
 if (R/doc).exists():shutil.copy2(R/doc,D/doc if doc!='截图OCR复核.md' else Q/doc)
(Q/'验收总览-v5.1.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2));shutil.copy2(O/'build-manifest.json',Q/'build-manifest.json')
shutil.copy2(html,D/'野狗逃班.html');shutil.copy2(O/'night-off.svg',D/'野狗逃班.svg')
# Deterministic rebuild from package in a completely separate location.
manifest={str(p.relative_to(D)):hashlib.sha256(p.read_bytes()).hexdigest() for p in D.rglob('*') if p.is_file()}
(D/'文件清单-SHA256.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
print(json.dumps({'stage':str(D),'tests':total,'html_bytes':html.stat().st_size,'sha256':hh,'files':len(manifest)},ensure_ascii=False))
