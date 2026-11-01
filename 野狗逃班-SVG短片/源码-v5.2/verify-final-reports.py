from pathlib import Path
import json,hashlib
R=Path(__file__).parent;d=json.loads((R/'night-off-out/build-manifest.json').read_text());h=d['sha256']
reports=[]
for p in sorted((R/'night-off-out').glob('qa-v52*.json')):
 r=json.loads(p.read_text());print(p.name,r.get('success'),len(r.get('tests',[])),r.get('artifact_sha256')==h);reports.append((p.name,r.get('success') and r.get('artifact_sha256')==h))
assert all(x[1] for x in reports),reports
print('Final reports',len(reports),'all same',h)
