本轮真源：冻结game-v51.js → prepare-v52断言增量插入地图/Boss/平衡/场景/钱包持久化 → game-v52。Code-review候选工地不是发布真源，Codex改动合并后真实源码在根。
旧gallery模块来自冻结game-v51已在基线内，build-v51上层模板只依赖arcade-art.svgfrag等片段；不要用旧prepare-v51再生成基线。本版一刀一句rep唯一断言，新数据最后加载后initExtension/initMaps才启动。
源码白名单包不打包私有Codex API工作脚本/请求日志/账户信息。已保留真实审查.md（不含凭据）便于复核；原测试脚本保留并复制生成新版数值spec。
旧5.1公开备份和旧源码/验收全留，新成品可回退但继续同文件名浏览器，不清真钱。新的maps字段旧5.1忽略不能表示回退后新图仍可玩。
