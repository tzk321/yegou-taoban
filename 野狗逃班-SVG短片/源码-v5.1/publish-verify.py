from pathlib import Path
import json,hashlib
D=Path('/sdcard/Download');P=D/'野狗逃班-SVG短片';Q=P/'验收-v5.1'
h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
s=json.loads((Q/'验收总览-v5.1.json').read_text());assert h(D/'野狗逃班.html')==s['artifact_sha256'];assert (D/'野狗逃班.html').stat().st_size>=524288
for p in [D/'野狗逃班-5.1.html',P/'night-off.html']:assert h(p)==s['artifact_sha256'],str(p)
for r in s['reports']:
 p=Q/r['report'];d=json.loads(p.read_text());assert d['success'] and d['artifact_sha256']==s['artifact_sha256'],p;assert len(d['tests'])==r['tests']
source=P/'源码-v5.1';assert (source/'README.txt').stat().st_size>0
for n in ['game-v5.js','gallery-runtime.js','gallery-panel.js','arcade-art.py','arcade-art.svgfrag','prepare-v51.py','build-v51.py','voyage-ui.svgfrag','build-v5.py']:assert (source/n).stat().st_size>0,n
old=P/'旧版-v5.0';frozen=Path('/mnt/data/user/0/me.rerere.rikkahub/files/tmp/night-off-v5/交付-v5/野狗逃班-5.0.html');assert h(old/'野狗逃班-5.0.html')==h(frozen)
assert (P/'源码-v5/README.txt').stat().st_size>0;assert json.loads((P/'验收-v5/qa-v5.json').read_text())['success']
r={'success':True,'main_sha256':h(D/'野狗逃班.html'),'main_bytes':(D/'野狗逃班.html').stat().st_size,'tests_main_reports':s['tests_total'],'reports':len(s['reports']),'published_files_readable_nonempty':True,'old_v5_preserved':True,'v5_source_report_gap_restored':True,'entry':'/storage/emulated/0/Download/野狗逃班.html'}
stage=Path('/mnt/data/user/0/me.rerere.rikkahub/files/tmp/night-off-v51/交付-v5.1/验收-v5.1');(stage/'交付文件验证.json').write_text(json.dumps(r,ensure_ascii=False,indent=2));print(json.dumps(r,ensure_ascii=False))
