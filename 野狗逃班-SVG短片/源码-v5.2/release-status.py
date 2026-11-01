from pathlib import Path
import json,subprocess
R=Path(__file__).parent;O=R/'night-off-out';h=json.loads((O/'build-manifest.json').read_text())['sha256'];d=[]
for p in O.glob('qa-v52*.json'):
 r=json.loads(p.read_text());d.append((p.name,r.get('success'),len(r.get('tests',[])),r.get('artifact_sha256')==h))
print('CURRENT',h);print('REPORTS',sorted(d));print('PASS_SAME',sum(x[2] for x in d if x[1] and x[3]),'/',len(d))
print(subprocess.run(['systemctl','list-units','nightoff52*','--all','--no-pager'],capture_output=True,text=True).stdout)
