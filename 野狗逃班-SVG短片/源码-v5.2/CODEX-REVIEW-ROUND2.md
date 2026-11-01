仅对所给快照静态审查，未执行测试、修改代码或发布；未触及真实钱包。

### 1. 高：首胜去重与钱包写入不是同一事务
位置：`maps-runtime.js::mapSettle/saveMaps`

结算只刷新持久化的 `maps.wins`，没有同步钱包、records 或其他存档字段。
- 两页同时结算可都读到“未首胜”，各自在旧钱包上发奖。
- 旧页发现另一页已首胜后，仍调用 `saveMaps()`；若 `saveField()`整体写入内存存档，会把新钱包增量、records 或已清除的 checkpoint 覆盖回去。**具体覆盖方式需看未提供的 `saveField()`，不能宣称已证明其实现。**

**最小修复：**所有同钱包写入入口统一进入同一个跨页锁，例如 `navigator.locks.request('nightOffProgressV4-write', …)`；锁内重新读取完整最新存档，在最新对象上判首胜、加奖励、合并 records，再一次写回。仅给地图结算加锁不足以保护购物、旧玩法奖励、devClaimed；后者必须保持一次10万语义。不要用“余额取最大值”，那会抹掉合法消费。

### 2. 高：旧局可以删掉另一局的新 checkpoint
位置：`mapSettle`
```js
if(mapStore.checkpoint?.id===n.id)mapStore.checkpoint=null;
```
仅按地图 id 清除。另一页已为同地图创建不同 `runId` 的检查点，旧局结算仍可能将它删除；`mapGate()`也会无条件写入旧内存的整个 maps。

**最小修复：**在上述存档事务内读取最新 checkpoint，仅在
```js
c?.id === M.id && c.runId === M.runId
```
时清除。写 checkpoint 也必须基于最新存档更新，不能顺带覆盖最新 wins/records。

### 3. 中：checkpoint 不足以保证重载后排名一致
位置：`mapGate`、checkpoint 读取、`playMap`

只保存 coins/tokens/coffee/hits/smashed/maxCombo，没有保存跑图基础分或确定的计分快照；重载通过 `playRoute()`重新初始化，再恢复少量字段，却仍以 `score()`计算最终排名。**未提供 `score()`，无法确定差额，但当前模块没有保证其全部输入得到恢复。**

**最小修复：**明确地图计分函数：过门时冻结、保存并验证 `routePoints`；结算仅用 `routePoints + tokens奖励 + Boss奖励`，不得重新计算已结束跑图的隐式状态。records 分组统一由锁定的 `M.skill`推导，而非依赖可变的 `V.gear`。

### 4. 中：结算模型/仪轨可能与票根锁装不一致
位置：`night-scenes.js::lookSkin`
```js
isMap()&&!['cover','ending'].includes(S.phase)?M.skin:wallet.skin
```
进入 ending 就切回钱包皮肤，而 `mapTicket()`仍使用 `M.skin`。跨页改装备或局中改钱包皮肤后，结算模型及后续调用的 trail 选择与票根不一致。

**最小修复：**
```js
const lookSkin=()=>isMap()&&S.phase!=='cover'?M.skin:wallet.skin;
```
结束阶段继续显示本局锁定皮肤；回封面再切回钱包皮肤。若结算渲染未调用 `applySkin()`，还须在相位切换处显式调用，不能只修选择器。

### 5. 中：危险预警与实际命中区域不完全一致
位置：`renderMapWarnings`、`stepMapBoss`

- lock 实际判定 `|dx|<85`，预警却仅画 `x±78`：两侧各7像素会在亮区外受击。
- floor 判定 `S.y>-89`，预警固定从411开始，没有共享碰撞边界。
- 飞弹在 active 分支没有预警绘制；现有路径仅在 telegraph 显示。orb 随时间上下摆动，所画水平线也不覆盖真实轨迹。

**最小修复：**lock 改成 `x:a.x-85,width:170`；floor 以 `GROUND-65-89`作为玩家中心危险边界，并标明按中心判定。飞弹预警保留到发射，orb 画 `e.y±23`的轨迹带，另计碰撞容差，不再用单水平线表达危险区。

### 未发现可成立的绕过
- **地图 Boss 时停窗口上限：**`mapHit()`同时校验 open 状态、窗口 serial，并按累计 `M.openDamage`截断。时停延长窗口不重置累计伤害，当前代码不能据此绕过每窗2/3伤。
- **token：**给出的碰撞补丁及 orbit/鲸/雷路径均显式排除自动破坏 token，接触才进入 `mapToken()`。但未提供 `legendCollect()`及完整吸附循环，不能保证所有旧路径。
- **票根出口回路：**只给出 `mapTicket()`生成函数，没有下载分发入口，不能确认地图结算实际导出此票根。
- 价格符合指定数值；该段仅更新商品目录，未见补差价逻辑。