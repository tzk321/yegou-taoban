# 新会话专属交接 · 野狗逃班6.0技能特效重做

## 0. 用户最新任务（别走偏）
用户原话：「打包发给新会话，让他把技能特效做好咯」。
你接手后首要任务是把14个技能的【实际游戏特效】做好：出手、持续、生效命中/拦截/充能、结束/冷却各阶段有可读反馈，技能互有辨识度；商店动态预览与实战同一视觉语言。不是再加几个静态图标，不是改名交差。
先确认接手、读本文件及《下一轮-交接-v6.0.md》，然后按任务施工。原来源会话交接后停工，你是新唯一施工/回信会话，不联系旧会话/WSL/pi；本机Kali仅作为工具执行环境，不是外包代理。
用户没有授权重做操控/加价/加数值/洗存档。保留当前已经调好的摇杆、80%狗、密集Boss弹幕、BGM增响、14技能单槽等。视觉与机制一致，不为画面改平衡。

## 1. 可靠基线（已发布，不是半成品）
- 主入口 `/storage/emulated/0/Download/野狗逃班-6.0.html`
- SVG同路径同名 `.svg`；交付目录 `/storage/emulated/0/Download/野狗逃班-6.0/`
- HTML 1566454字节，SHA256 `78639afd827d23130d9263fb82799555b347e5ae6751741232eeaed6ef0536a5`
- SVG SHA256 `b3eee59889b87857b440a7e780227896f54bb5e0e6fcb7add1033d90da2bc057`
- 正式22报告431项全同hash，含公共普通入口10项；源码异目录重建HTML/SVG逐字节一致。
- 既有完整包 `/storage/emulated/0/Download/野狗逃班-v6.0-源码与验收.zip`，不是新特效成果，别误报。
- 专用接力包 `/storage/emulated/0/Download/野狗逃班-6.0-技能特效接力包.zip` 包含最新冻结基线和本任务。

## 2. 工地与工具（不要从旧5.3目录开工）
工地：`/data/user/0/me.rerere.rikkahub/files/tmp/night-off-v60`。
容器是kali-tzk / Kali Rolling / node24.19+acorn / Python3.14 / Chromium150。
APP shell里没有node/python，命令在本机Kali跑；先use_skill('device-exec')：
```
su -c '/data/local/exec-tool.sh arch kali' <<'KALI_RUN'
cd /mnt/data/user/0/me.rerere.rikkahub/files/tmp/night-off-v60
node prepare-v60.mjs
node --check game-v60.js
python3 build-v60.py
KALI_RUN
```
长任务 >30秒必须systemd-run后台+日志，不用工具硬等；复杂操作先APP file.write到工地脚本，再容器sh绝对路径执行。
读写APP/Download文件优先file工具；容器生成物写APP tmp，再APP file.copy发布，别容器root直接落公共存储属主坑。
当前没有本项目运行中的后台施工/QA，无要接着等的旧作业。

## 3. 真源结构与钩子
- 冻结 `frozen-game-v52.js` SHA256 `3cdfcbcc3613719e574f4edae091a52131c83741ff9a8d8214ccfd58ed1206ef`；`frozen-v52.svg` SHA256 `f295df4d9551159abfb31acb7751dc18f1532d2321c627a69e209b77c086caef`，禁止手改。
- `prepare-v60.mjs`：用acorn从冻结件删除作者模块覆盖的同名函数，再精确唯一字符串替换，生成game-v60.js。作者模块内同名函数也不能重复；所有增量从作者模块或prepare断言做，别手改生成物。
- `build-v60.py`：冻结SVG替换脚本/加节点→night-off-out/night-off.html/.svg及manifest，原SVG美术完整保留。
- `catalog-v60.js`：新技能/皮肤注册要在存档验证前；基础/传说技能原定义与BALANCE_COPY在冻结源末尾，运行真源以最终生成物和QA.catalog为准。
- `mobility-v60.js`：摇杆/手势/菜单、simClock/lastRailDash硬账本、counter、updateDashMotion、initV60；别拆操控。
- `polish-v60.js`：实际新技能机制+HUD/图标/性能。重点newDashGear/tickNewGear/gearWave/v60Land/v60CraneTick/renderNV/polishCoffee/polishAir/polishPreview/drawSkillIcon。
- `gear-v60.js`：spawnCrane/prismCollision/extraAccessory/newGearPreview，很多旧同名函数已经迁到polish。
- `bullets-v60.js`：真实敌弹、清弹、扫掠碰撞、追踪反击纸、Boss三阶段/两阶段事件；clearBullets、tickBullets、advanceCounterShots、stepBulletBoss。
- `tuning-v60.js`：PLAYER_SCALE=.8、PLAYER_BULLET_RADIUS=21.6、playerCenter/playerDrawTransform、runnerContact/playerBulletContact、BOSS_BULLET_LIMIT=64。
- `audio-v60.js`：7主题/同AudioContext/音量键，无需为了做特效改。
- 原有old技能效果在冻结源：legendDash/legendSuper/tickLegend/renderLegend/railShot/legendBurst/legendBreak/consumeShield/legendCollect；通过作者覆盖或精确钩子接入，别动冻结件。
可新增`skillfx-v60.js`作为统一特效调度/池，但必须加prepare模块表与package源清单；别搞旁路生成/运行期外链。

## 4. 14技能一览：保留机制，补齐实际视觉（候选画风，不是机械死命令）
|id/名字/价格|实际机制底线|建议做的实战特效|
|---|---|---|
|wind 回风步 45|冲刺reach142、跑图CD2.7/Boss1.2；不改原无敌|浅青回风弧/薄尾迹/起步冲击，区分普通冲刺，结束收束|
|magnet 拾荒磁场 65|已有币杯近距吸附；不自动破障|短吸力弧/拾取粒子汇向狗，范围仅表达真实吸附，别铺大实心圈|
|shield 纸盾协议 80|一次纸盾，受击消耗，短免伤；完美资格保留|折纸盾层、受击确实碎纸，没盾别继续亮|
|rail 雷贯穿街 800|实际冲CD8秒所有装备路线，最多破3障、不回能；F独立反击|分层雷弧/前沿电光/穿障断点，出手收尾清楚，别遮红弹|
|orbit 万纸归宗 1800|纸护每2.1秒近距拦一障耗1能量，Boss取消自动纸，大招双纸受每窗限额|纸张轨道/有能待命/拦截燃一纸/大招双纸，别假自动打Boss|
|leviathan 鲸落清场 3600|大招首拍480清场、鲸息4.4s且每1s扫180，Boss限额|折纸鲸体/水纹/扫场前沿，鲸息结束淡去，不要全屏白闪盖敌弹|
|chrono 拒绝时间 9800|六杯时停2.4s、实际世界时间冻结、主动冲反击限额|刻度钟环/轻量时间涟漪/停止与解冻反馈，避免大矩形色罩回归|
|prism 折返棱镜 420|冲后0.9s真实实体镜面，挡实际弹体，跑图代一障后消失|多面折射镜/轻碎屑/实际拦截点闪，没拦弹别假报命中|
|echo 落地回响 680|二跳后落地160清弹波、6sCD、跑图只破最近一障|落地有清晰边界的波纹/波前线，实际清弹碎点；CD中落地不放假波|
|crane 纸鹤护航 1200|3s出一只，最多2在场，真实追近弹/障拦截，用完移除|折鹤成形/翅膀/细航迹/撞散反馈；修过孤儿DOM，不能再泄漏|
|nightvision 夜视航图 260|实体弹道预测线，币杯吸附+40；不改伤害|细虚线/箭头/小锁点，线按bullet.id复用，不能每帧replaceChildren|
|capacitor 闪充电容 560|每3杯真实拾取额外充1能量、封顶6；不造币/杯|三段电容灯/第三杯闪充走线/能量入槽；满能不假装多充|
|glide 夜风滑翔 940|二跳后下落上限260，下拉立刻收翼急落，落地重置，不免伤|轻翼/滑翔弧/风丝：只在实际滑翔时存在，收翼和落地要消退|
|pulse 拒收脉冲 1500|冲刺120范围最多3已入场弹/一非甲障，独立8s，不重置dash|冲刺环/拒收符号/清弹点反馈，不清弹时不造爆炸，范围与机制相符|

共同目标：每种技能先看一眼能分清，实际生效点可读；商店重播有真实节拍，而不是拿同一圈换颜色。皮肤不改判定、技能仍单槽。没有装备时也要保留基础冲刺和大招反馈。

## 5. 绝不能倒退
1. 左摇杆右移32上移28 CSS像素后的左50px/下46px，透明可滑、上推跳/斜推走跳/回中再推二跳/下拉急落；小浮动dash/super/counter，无旧大跳跃急落按钮复活。
2. 狗80%、碰撞21.6、跑图敌障57.6、拾杯币宽容；倒影/残影同scale，别只把皮画小；新版FX应跟playerCenter()/真实世界坐标，别把旧GROUND+y-65当新碰撞中心。
3. 12图13Boss密集短簇，常规4/5、上路3、瞄准3扇形、最多64实体、4.5s绿窗/HP/伤害/三格耐心/雷8秒账本不变。
4. 一个钱包nightOffProgressV4，旧购和546603一次+100000标记/并发增量/检查点保护不变；音频nightOffAudioV53只偏好。禁止访问真实浏览器profile/清档/造钱。
5. BGM增益.8、新默认.55、5档20/35/55/80/100、旧偏好保留、音效没加大、暂停后台stopMusic无叠节点。
6. `v60ScreenFX`是全屏根坐标，`scene`是世界坐标，`v60PlayUI`是实玩HUD，`v60UI`等比菜单。特效尽量进scene世界效果层；别把全屏色罩放入缩放菜单制造中央暗框。
7. 不要遮红色危险弹体/绿窗/耐心/狗和摇杆；长闪、频繁强闪、满屏粒子不要。Reduced motion保留机制、减少视觉。

## 6. 性能/生命周期标准
- 只维护自己的FX实例数组/池，设置明确同时存在上限和寿命；warm reusable nodes、事件触发，避免每帧querySelectorAll/replaceChildren/克隆狗/读getBBox或innerHeight。
- 容器transform/opacity尽量更新、静态形状一次建，SVG滤镜尤其大blur谨慎，别给每粒子/每颗弹体上昂贵filter。
- 真实步进模拟dt与render分开，不能为视觉减碰撞频率/给无敌/改Boss资格。暂停视觉冻结、后台停调度；home/retry/关卡切换/Boss阶段/换装清理正确。
- 已缓存商店data-art、retainedNV按bullet.id、hudLayoutKey、screenH，别拆掉。纸鹤拦截后DOM移除是已修复项。
- 试玩/截图覆盖390×844、844×390、2400×1080等，新增技能FX截图/节点寿命/高负载实测，不要只拿商店图当实战特效完成。
- 前后性能短测可以做，但不能冒充实体手机60FPS；现报告有负载波动，诚实保留。

## 7. 验收和发布步骤
1. 新特效施工前先备份当前6.0（不得覆盖现有旧版目录），核对主入口hash等于本文件。
2. 每次构建 `node prepare-v60.mjs; node --check game-v60.js; python3 build-v60.py`。
3. 自建qa-skillfx-v60.mjs/报告：14技能实战可观察反馈、免费动态预览、触发条件/冷却/禁用、暂停/重开/后台/减弱动画、节点/粒子上限、密集Boss弹幕可读性；把新模块/QA加入package和gate清单，报告绑定新hash。
4. 全量`sh gate-suite.sh`（失败即停，当前21预发布报告421项，普通RAF和QA.advance分别记录）。Boss机器人只合法输入；隔离Boss检查点fixture不造HP/生命分数。
5. `run-perf-compare.sh`旧基线目前指night-off-v60-before-size-density（d462fe95…）；新轮比较应该用本轮78639afd…另建前测快照，并改write-perf-summary.py匹配基线，不照搬旧数字。package有bench-after新hash断言，不可删断言假过。
6. `python3 package-v60.py`→所有报告同新hash+异目录源码重建逐字节一致。
7. APP侧file.copy覆盖仅6.0入口/副本，复制完成再`node qa-public-v60.mjs`隔离profile打开真实Download普通RAF。
8. `python3 post-public-package.py`加公共报告再zip；APP侧复制交付目录/zip，全部复制完成再`release-verify.py`及`verify-artifacts-v60.py`。不要并行依赖步骤，之前踩过“复制未完先校验”假失败。
9. release-verify额外断言原入口/5.3字节未变及旧6.0备份还在；旧包/报告要保持历史与当前分开。
10. clean-profiles.py只清本工地关闭的qa-profile-*，不要真实profile。

## 8. 工地卫生与最后提醒
工地里有各轮调参脚本/日志/旧报告。作者真源与可复现发布源以`交付-v6.0/源码-v6.0/`和当前模块为准，先读构建/清单，别运行apply-polish.py/finish-perf-hooks.py/adjust-density.py等一次性旧补丁，会重复改坏。
禁止联系旧会话/WSL/pi。本来源会话交接完成停工，你是新唯一施工/回信会话；没有等待中的施工后台。先确认，然后直接把技能特效做扎实，别再问一遍用户已经明确的方向。
