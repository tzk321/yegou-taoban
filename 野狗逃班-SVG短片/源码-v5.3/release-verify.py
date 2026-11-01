from pathlib import Path
import json,hashlib,zipfile
R=Path(__file__).parent;P=Path('/sdcard/Download');D=P/'野狗逃班-SVG短片';O=R/'night-off-out';h=hashlib.sha256((O/'night-off.html').read_bytes()).hexdigest()
for p in [P/'野狗逃班.html',P/'野狗逃班-5.3.html',D/'night-off.html',D/'野狗逃班-5.3.html']:assert p.read_bytes()==(O/'night-off.html').read_bytes(),p
for p in [P/'野狗逃班.svg',P/'野狗逃班-5.3.svg',D/'night-off.svg',D/'野狗逃班-5.3.svg']:assert p.read_bytes()==(O/'night-off.svg').read_bytes(),p
assert hashlib.sha256((D/'旧版-v5.2-弹幕机动前/野狗逃班.html').read_bytes()).hexdigest()=='63e87b2f62b3ddc8bf720bbc95700650404079e88e93706f74080d0bd6c93be3'
assert hashlib.sha256((D/'旧版-v5.3-摇杆跳跃全屏前/野狗逃班.html').read_bytes()).hexdigest()=='a271e01f77896ae054898246089c88ea10837a5e9e3c724f4720a8fa52b0bdd6'
summary=json.loads((D/'验收-v5.3/总览-v5.3.json').read_text());assert summary['artifact_sha256']==h and summary['success']
for e in summary['reports']:
 d=json.loads((D/'验收-v5.3'/e['report']).read_text());assert d['success'] and d['artifact_sha256']==h
with zipfile.ZipFile(P/'野狗逃班-v5.3-源码与验收.zip')as z:
 assert z.read('night-off.html')==(O/'night-off.html').read_bytes();assert json.loads(z.read('验收-v5.3/总览-v5.3.json'))==summary
 assert not any(any(x in n for x in ['codex-review.sse','codex-review-request','qa-profile','codex-review-v53.py'])for n in z.namelist())
 for p in (D/'源码-v5.3').iterdir():
  if p.is_file():assert z.read('源码-v5.3/'+p.name)==p.read_bytes()
print(json.dumps({'success':True,'sha256':h,'html_bytes':(O/'night-off.html').stat().st_size,'reports':summary['report_count'],'tests':summary['test_count'],'public_normal_entry':True,'baseline_backup_verified':True,'zip_source_report_match':True},ensure_ascii=False))
