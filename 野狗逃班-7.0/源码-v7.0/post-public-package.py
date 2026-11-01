from pathlib import Path
import json,shutil,zipfile,hashlib
R=Path(__file__).parent;D=R/'交付-v7.0';A=D/'验收-v7.0';O=R/'night-off-out';h=hashlib.sha256((O/'night-off.html').read_bytes()).hexdigest();p=O/'qa-public-v70.json';q=json.loads(p.read_text());assert q['success'] and q['artifact_sha256']==h and all(t['passed'] for t in q['tests']) and not q.get('errors') and not q.get('externals');shutil.copy2(p,A/p.name);s=json.loads((A/'总览-v7.0.json').read_text());s['reports']=[x for x in s['reports'] if x['report']!=p.name]+[{'report':p.name,'tests':len(q['tests']),'success':True,'artifact_sha256':h}];s['report_count']=len(s['reports']);s['test_count']=sum(x['tests']for x in s['reports']);s['public_entry_verified']=True;(A/'总览-v7.0.json').write_text(json.dumps(s,ensure_ascii=False,indent=2));shutil.copy2(R/'STATUS-v70.md',D/'STATUS-v70.md')
with zipfile.ZipFile(R/'野狗逃班-v7.0-源码与验收.zip','w',zipfile.ZIP_DEFLATED,6)as z:
 for p in sorted(D.rglob('*')):
  if p.is_file():z.write(p,str(p.relative_to(D)))
print(json.dumps({'success':True,'hash':h,'reports':s['report_count'],'tests':s['test_count']},ensure_ascii=False))
