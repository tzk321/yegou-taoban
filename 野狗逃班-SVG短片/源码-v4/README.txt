《野狗逃班 4.0：夜游补给》源码

本版是稳定3.0的增量版本，保留120秒四幕、纸鲸黎明、完美隐藏Boss及Boss单独重试。

唯一构建步骤（Python标准库）：
python3 prepare-v4.py
python3 build-v4.py

新版修改源：
- game-v3.js：冻结的3.0运行基线，不能运行upgrade-game.py去覆盖它。
- prepare-v4.py：有唯一匹配断言的4.0运行逻辑变更。
- v4-features.js：金币、本地钱包、皮肤、单槽技能、商店、冲刺位移/残影、关卡生成。
- v4-beams.js：Boss危险带、预警/发射光束绘制。
- build-v4.py：4.0美术与布局结构；继承build-v3.py → build-v2-base.py → build-v1.py。
- boss-art.svgfrag / boss-ui.svgfrag：基线Boss美术。
- game-v4.js：由prepare-v4.py生成，便于查看，不要直接改后再生成。

输出 night-off-out/night-off.html、night-off.svg，成品完全离线单文件。
3.0的game-v2-base.js、boss-code.js、upgrade-game.py在相邻源码-v3目录供历史对照，4.0不运行，也不需要。

实际浏览器QA：Node24自带WebSocket + Chromium CDP，无npm依赖。
qa-lib.mjs：CDP与截图基础。
qa-planner.mjs：只能观察障碍/状态、执行跳/冲/大招、推进QA时间；不改分、不改伤害。预测跳跃路线验证主关有解。
qa-v4-final.mjs：完整主关→Boss链、商店交易、存档、技能、布局、光束、暂停/多指、独立SVG与storage受限。
qa-v4-realtime.mjs：普通入口真实120秒放映；独立Boss入口后真实RAF+点击打赢。
qa-visual.mjs：截图/布局复核。
测试脚本root路径需修改到当前源码输出位置，CDP端口/profile互不共用。
