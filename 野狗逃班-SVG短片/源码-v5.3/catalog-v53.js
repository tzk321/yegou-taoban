// Registered before persisted ownership validation; migrations never discard newly purchased IDs.
LEGEND_SKINS.push(
{id:'mecha',name:'机械信使',price:1680,tier:'新装',desc:'信使护甲 / 铆钉邮包',detail:'铜绿护甲、折翼邮包、机械护目镜与齿轮脚印。模型、倒影和残影同步；纯外观不改碰撞。',coat:['#bed4cf','#4e7f80','#25434f'],hood:'#7ea6a0',trim:'#ffe1b1',pocket:'#57777d',scarf:'#f2bc76',accent:'#9d7356',fx:'#c0eee1'},
{id:'nebula',name:'星云潜航',price:3680,tier:'新装',desc:'透明星罩 / 彗星航带',detail:'紫蓝航行服、透明星罩、双尾彗星披带与轨道脚印。模型、倒影和残影同步；纯外观不改碰撞。',coat:['#c5c6f7','#686bb5','#30335e'],hood:'#9a9ed7',trim:'#e2f8ff',pocket:'#696b9e',scarf:'#9feaf4',accent:'#8fb4dd',fx:'#d8ccff'});
CATALOG.skins.push(...LEGEND_SKINS.slice(-2));
CATALOG.skills.push(
{id:'prism',name:'折返棱镜',price:420,tier:'新技',desc:'冲后留镜 / 挡弹0.9秒',detail:'每次冲刺留下一块0.9秒棱镜，拦截经过镜面的真实Boss弹体；跑图代挡一处近身障碍后消失。不增加永久无敌，单槽。'},
{id:'echo',name:'落地回响',price:680,tier:'新技',desc:'二段落地 / 160清弹波',detail:'二段跳后落地触发160半径回响，清除真实弹体；跑图只破最近一障，不回能。6秒间隔，落地不会免伤，单槽。'},
{id:'crane',name:'纸鹤护航',price:1200,tier:'新技',desc:'折鹤护航 / 自动拦弹',detail:'每3秒折出一只纸鹤（最多2只在场），自动扑向最近的敌弹并拦截；跑图时扑向最近障碍撞掉一个。不是无敌帧，单槽。'},
{id:'nightvision',name:'夜视航图',price:260,tier:'新技',desc:'弹道预测线 / 吸附+40',detail:'敌弹显示飞行预测线；金币与咖啡吸附范围各+40。不改伤害与无敌，单槽。'});
