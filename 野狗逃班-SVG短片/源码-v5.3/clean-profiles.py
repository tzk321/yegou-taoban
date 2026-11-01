from pathlib import Path
import shutil,subprocess
R=Path(__file__).parent/'night-off-out'
active=subprocess.run(['pgrep','-af','chromium'],capture_output=True,text=True).stdout
for p in R.glob('qa-profile-*'):
 if str(p)in active or 'qa-'+p.name.split('-')[-1]in active:print('SKIP active',p.name);continue
 size=sum(x.stat().st_size for x in p.rglob('*')if x.is_file());shutil.rmtree(p);print('Clean isolated closed profile',p.name,size)
