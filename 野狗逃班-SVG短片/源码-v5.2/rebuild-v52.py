from pathlib import Path
import shutil,subprocess,hashlib,json
R=Path(__file__).parent;S=R/'交付-v5.2'/'源码-v5.2';T=R/'rebuild-v52-isolated'
if T.exists():shutil.rmtree(T)
shutil.copytree(S,T)
for c in [['python3','maps-art.py'],['python3','prepare-v52.py'],['node','--check','game-v52.js'],['python3','build-v52.py']]:subprocess.run(c,cwd=T,check=True)
comp=[]
for f in ['night-off.html','night-off.svg','build-manifest.json']:
 a=(R/'night-off-out'/f).read_bytes();b=(T/'night-off-out'/f).read_bytes();assert a==b,f;comp.append({'file':f,'identical':True,'sha256':hashlib.sha256(a).hexdigest()})
p=R/'交付-v5.2'/'验收-v5.2'/'验收总览-v5.2.json';d=json.loads(p.read_text());d['rebuild_verified']=True;d['rebuild_comparisons']=comp;p.write_text(json.dumps(d,ensure_ascii=False,indent=2))
(R/'rebuild-proof-v52.json').write_text(json.dumps(comp,indent=2));print('Independent packaged sources rebuild byte-for-byte PASS')
