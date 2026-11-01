野狗逃班3.0源码

在这个目录执行：
python3 upgrade-game.py
python3 build-v3.py

upgrade-game.py 基于 game-v2-base.js 进行明确替换并加入 boss-code.js，生成 game-v3.js。
build-v3.py 复用 build-v2-base.py 的SVG结构、美术生成（以及build-v1.py），加入boss-art.svgfrag/boss-ui.svgfrag，然后嵌入 game-v3.js，生成 night-off-out/night-off.svg 与 .html。
仅Python标准库，无外部构建依赖。游戏运行时不需要这些源码。

测试脚本是Node24自带WebSocket的CDP客户端，使用WSL的/usr/bin/chromium。
路径需调整到你自己的项目目录；不要同时复用同一个Chromium端口或profile。
qa-v3.mjs：21项核心，包含自然操作完整主关与Boss整链。
qa-v3-extra.mjs：12项边界，包括真实120秒完整放映。
qa-realtime.mjs：真实帧率+CDP点击Boss全阶段打赢，不加速战斗时钟。
