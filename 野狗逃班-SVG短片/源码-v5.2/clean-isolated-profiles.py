from pathlib import Path
import shutil,subprocess
R=Path(__file__).parent.resolve()
procs=subprocess.run(['pgrep','-af','chromium'],capture_output=True,text=True).stdout
for p in R.rglob('qa-profile-*'):
 if not p.is_dir() or R not in p.resolve().parents:continue
 if str(p) in procs:print('KEEP active',p);continue
 print('REMOVE only closed isolated profile',p);shutil.rmtree(p)
print('No public/user browser profile touched')
