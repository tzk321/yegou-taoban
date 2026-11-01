from pathlib import Path
import hashlib,json,zipfile
R=Path(__file__).parent;O=R/'night-off-out';D=R/'交付-v6.0';h=hashlib.sha256((O/'night-off.html').read_bytes()).hexdigest();a=D/'验收-v6.0';s=json.loads((a/'总览-v6.0.json').read_text());assert s['success']and s['artifact_sha256']==h
for e in s['reports']:
 d=json.loads((a/e['report']).read_text());assert d['success']and d['artifact_sha256']==h
for p in (D/'源码-v6.0').iterdir():
 if p.is_file()and p.name!='README.txt':assert p.read_bytes()==(R/p.name).read_bytes(),p.name
with zipfile.ZipFile(R/'野狗逃班-v6.0-源码与验收.zip')as z:
 assert z.read('night-off.html')==(O/'night-off.html').read_bytes();assert z.read('night-off.svg')==(O/'night-off.svg').read_bytes()
 assert json.loads(z.read('验收-v6.0/rebuild-proof-v60.json'))['html_equal'];bad=[n for n in z.namelist()if n.endswith('.sse')or 'codex-review-request' in n or 'qa-profile-' in n or n.endswith('codex-session.json')or n.endswith('codex-status.json')];assert not bad,('zip leak',bad)
print(json.dumps({'success':True,'hash':h,'reports':s['report_count'],'tests':s['test_count'],'public_source_matches_current':True,'zip':True,'independent_rebuild':s['rebuild']},ensure_ascii=False))
