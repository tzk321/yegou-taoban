from pathlib import Path
import json,hashlib
R=Path(__file__).parent; O=R/'night-off-out';h=hashlib.sha256((O/'night-off.html').read_bytes()).hexdigest()
b=json.loads((O/'bench-baseline.json').read_text());a=json.loads((O/'bench-after.json').read_text())
assert b['artifact_sha256']=='78639afd827d23130d9263fb82799555b347e5ae6751741232eeaed6ef0536a5'
assert a['artifact_sha256']==h
assert not a['errors'] and not b['errors']
rows=['# 7.0 性能前后短测','',f'新构建 SHA256 `{h}`。旧基线 `{b["artifact_sha256"]}`。','同机Kali Chromium headless，844×390触摸视口，每场景约3.2秒，普通RAF。先旧后新，未与其它QA同时运行。','CPU/设备负载与采样顺序影响结果，不是实体手机性能保证；不拿一次测量承诺稳定60FPS。','','|场景|旧脚本ms|新脚本ms|旧布局ms|新布局ms|旧p95帧间隔|新p95帧间隔|旧/新每秒帧数|','|---|---:|---:|---:|---:|---:|---:|---:|']
for x,y in zip(b['res'],a['res']):
 assert x['name']==y['name']
 rows.append(f'|{x["name"]}|{x["scriptMs"]:.1f}|{y["scriptMs"]:.1f}|{x["layoutMs"]:.1f}|{y["layoutMs"]:.1f}|{x["p95"]:.1f}|{y["p95"]:.1f}|{x["fps"]:.1f} / {y["fps"]:.1f}|')
rows+=['','## 结构性验证','qa-perf-v70.json验证：暂停菜单普通RAF不反复改SVG；商店空闲不重建克隆；同颗夜视弹体的预测线节点保留。','HUD几何仅在视口/阶段变化重排，摇杆不每帧读innerHeight；纸鹤拦截与重开均清DOM。物理子步/碰撞/伤害仍完整。','原始测量在bench-baseline.json和bench-after.json；add/remove含文本变更，并不全是图形节点，不把总计当纯节点泄漏。']
(O/'性能对照-v7.0.md').write_text('\n'.join(rows)+'\n')
print('\n'.join(rows))
