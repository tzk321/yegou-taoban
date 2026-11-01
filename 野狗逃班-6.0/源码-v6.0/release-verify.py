from pathlib import Path
import json,hashlib,zipfile
R=Path(__file__).parent; P=Path('/sdcard/Download'); D=P/'野狗逃班-6.0'; O=R/'night-off-out'
hashof=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
h=hashof(O/'night-off.html')
for ext in ['html','svg']:
 for p in [P/f'野狗逃班-6.0.{ext}',D/f'night-off.{ext}']:
  assert p.read_bytes()==(O/f'night-off.{ext}').read_bytes(),str(p)
# Independent 6.0 release MUST NOT replace either the legacy original entry or 5.3 copies.
for p in [P/'野狗逃班.html',P/'野狗逃班-5.3.html',P/'野狗逃班-SVG短片/night-off.html',P/'野狗逃班-SVG短片/野狗逃班-5.3.html']:
 assert hashof(p)=='e598bab91e88711decee3eac7d79b2df55bee624168ba68645ec6b99d4ad1811',str(p)
for p in [P/'野狗逃班.svg',P/'野狗逃班-5.3.svg',P/'野狗逃班-SVG短片/night-off.svg',P/'野狗逃班-SVG短片/野狗逃班-5.3.svg']:
 assert hashof(p)=='0dd9fa36ee6565258cefe4c511df93ae020f2bcdfe42046f6da5bf4f7563ee36',str(p)
assert hashof(D/'旧版-删按钮加技能优化前/野狗逃班-6.0.html')=='56d2d59d3eb42ce020bb3d78bf3185b2a7fdbe4b76021d35fa1862d7a386ea79'
assert hashof(D/'旧版-摇杆缩狗弹幕前/野狗逃班-6.0.html')=='d462fe95e2d9983f06b589b2edb42b752dd24660ff594aa42608af63b21cbf9d'
summary=json.loads((D/'验收-v6.0/总览-v6.0.json').read_text());assert summary['artifact_sha256']==h and summary['success'] and summary['public_entry_verified']
for e in summary['reports']:
 d=json.loads((D/'验收-v6.0'/e['report']).read_text());assert d['success'] and d['artifact_sha256']==h and all(t['passed'] for t in d['tests'])
with zipfile.ZipFile(P/'野狗逃班-v6.0-源码与验收.zip')as z:
 assert z.read('night-off.html')==(O/'night-off.html').read_bytes()
 assert json.loads(z.read('验收-v6.0/总览-v6.0.json'))==summary
 assert not any(x in n for n in z.namelist() for x in ['.sse','codex-review-request','qa-profile','codex-review-v53.py'])
 for p in (D/'源码-v6.0').iterdir():
  if p.is_file():assert z.read('源码-v6.0/'+p.name)==p.read_bytes(),p.name
print(json.dumps({'success':True,'version':'6.0','sha256':h,'html_bytes':(O/'night-off.html').stat().st_size,'reports':summary['report_count'],'tests':summary['test_count'],'public_normal_entry':True,'original_and_53_unchanged':True,'zip_source_report_match':True},ensure_ascii=False))
