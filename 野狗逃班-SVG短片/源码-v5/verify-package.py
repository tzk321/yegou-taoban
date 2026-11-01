from pathlib import Path
import hashlib,json,xml.etree.ElementTree as ET,re
R=Path(__file__).parent;O=R/'night-off-out'
names=['qa-v5.json','qa-v5-boundaries.json','qa-v5-balance.json','qa-v5-visual.json','qa-v5-results.json','qa-v5-economy.json','qa-v5-archive.json','qa-v5-benchmark.json','qa-v5-realtime.json','qa-v41.json','qa-v41-regression.json','qa-v41-edges.json','qa-v41-realtime.json']
sha=hashlib.sha256((O/'night-off.html').read_bytes()).hexdigest();reports=[]
for name in names:
 if not (O/name).exists():print('WAIT',name);continue
 d=json.loads((O/name).read_text());assert d['success'],(name,d.get('error'));assert d['artifact_sha256']==sha,(name,'stale artifact');assert all(t.get('passed') for t in d['tests']),name;assert not d['errors'] and not d['externals'],name
 reports.append({'name':name,'tests':len(d['tests'])})
 print(name,len(d['tests']),'OK')
root=ET.fromstring((O/'night-off.svg').read_text());ids=[e.get('id') for e in root.iter() if e.get('id')];assert len(ids)==len(set(ids));assert '@BUTTON:' not in (O/'night-off.html').read_text()
html=(O/'night-off.html').read_text();assert not re.search(r'<(?:img|script|link)\b[^>]*(?:src|href)=[\"\']https?://',html)
result={'version':'5.0','success':len(reports)==len(names),'artifact_sha256':sha,'svg_sha256':hashlib.sha256((O/'night-off.svg').read_bytes()).hexdigest(),'reports':reports,'total_tests':sum(x['tests']for x in reports),'xml_unique_ids':len(ids),'environment':'Kali Chromium150 / Node24 CDP. DOM + OCR + real wall clock. Not physical phone gameplay.'}
(O/'验收总览-v5.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print(json.dumps(result,ensure_ascii=False))
assert result['success'],'reports incomplete'
