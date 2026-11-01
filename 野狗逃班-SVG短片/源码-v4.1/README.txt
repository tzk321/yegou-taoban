野狗逃班4.1 · 镇店藏品

在4.0稳定运行基线上新增8套皮肤/7项技能商店（原4+3、新4+4），不重做主关。

单一修改源：
- game-v4.js：冻结4.0基线，不要再跑prepare-v4.py去覆盖。
- v4-features.js：冻结4.0功能供prepare-v41.py抽取；不是最终运行代码。
- prepare-v41.py：断言替换主关/Boss调用入口和商店替换，生成game-v41.js。
- legend-catalog.js：新货价格与完整详情。
- legend-runtime.js：真实技能、皮肤配件/仪轨与脚印。
- legend-shop.js：分页、免费动画预览、详情、昂贵购买二次确认。
- legend-art.svgfrag：固定美术组。
- build-v41.py：继承build-v4.py结构并加入新商店与详情/特效。

构建只运行：
python3 prepare-v41.py
python3 build-v41.py

生成night-off-out/night-off.html和night-off.svg；game-v41.js是生成件，不直接改。
build-v4.py → build-v3.py → build-v2-base.py → build-v1.py、boss-art.svgfrag/boss-ui.svgfrag仍是必要依赖。
无需npm和外链，运行成品不需要源码，单文件完全离线。

新存档仍用nightOffProgressV4，因此原金币/购买/技能直接保留。售价都是游戏内金币，没人民币充值。
单槽技能；角色主关/BossGate/BossResult本局装备锁定，防中途更换后重试Boss拿新技能。
新技能/美术限制：残影最多4、皮肤脚印8、技能爆裂约28、常规粒子92，减弱动画保留技能功能。

浏览器QA：Node24 WebSocket+Chromium150 CDP；qa-lib.mjs路径root按本机测试位置改。
qa-v41.mjs新货交易/存档/实际招式/造型/布局；qa-v41-regression.mjs旧30项回归；qa-v41-realtime.mjs普通入口真实120秒放映+实时Boss时停测试。
孤立贵货测试只在专属浏览器profile写测试钱包，不在用户存档里送钱。
截图验证OCR/字符画与DOM边界，不冒充实体手机整局实测。
