from pathlib import Path
import zipfile,json,hashlib
R=Path(__file__).parent;z=R/'野狗逃班-v5.2-源码与验收.zip'
with zipfile.ZipFile(z) as a:
 assert a.testzip() is None
 for name in a.namelist():
  assert not any(x in name for x in ['qa-profile','codex-session','codex-worker','codex-round2-request']),name
 m=json.loads(a.read('build-manifest.json'));q=json.loads(a.read('验收-v5.2/验收总览-v5.2.json'));assert q['rebuild_verified'];assert m['sha256']==q['artifact_sha256']
 assert hashlib.sha256(a.read('源码-v5.2/game-v51.js')).hexdigest()=='4537bb5fa69dcadf809e7819b9b29d3d3541d98a27e4cf86d999e227a8412474'
 for report in q['reports']:
  body=a.read('验收-v5.2/'+report['file']);d=json.loads(body);assert d['success'] and d['artifact_sha256']==m['sha256'];assert hashlib.sha256(body).hexdigest()==report['sha256']
 print('Zipped sources frozen baseline, no profiles/credentials, rebuilt summary, all report hashes PASS',q['passed'],q['report_count'])
