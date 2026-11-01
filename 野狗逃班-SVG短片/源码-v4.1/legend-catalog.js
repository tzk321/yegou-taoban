const LEGEND_SKINS=[
{id:'neon',name:'霓虹暴雨',price:880,tier:'珍藏',desc:'电路雨衣 / 霓虹尾迹',detail:'墨蓝机能雨衣，双色光纤、悬浮雨滴与雷光脚印。纯外观，不改碰撞。',coat:['#394b71','#162f48','#091526'],hood:'#213e57',trim:'#a1ffef',pocket:'#234666',scarf:'#f983ce',accent:'#a562bf',fx:'#69ffe0'},
{id:'eclipse',name:'月蚀巡游',price:2888,tier:'史诗',desc:'月白披风 / 星屑环',detail:'月白长披风、银月头冠、缓转月蚀环与漂浮碎星。纯外观，仍是那只野狗。',coat:['#fffcef','#c9d9f4','#7689b2'],hood:'#e1e7fc',trim:'#faffff',pocket:'#b2c6e4',scarf:'#a9a0e8',accent:'#7974bc',fx:'#ccd9ff'},
{id:'corona',name:'日冕金权',price:8888,tier:'传说',desc:'黑金礼装 / 日冕冠',detail:'黑金织纹礼装、日冕冠、太阳仪轨和金焰脚印。贵在造型，不靠数值加成。',coat:['#55492e','#25292e','#121a23'],hood:'#d4b164',trim:'#ffde91',pocket:'#6b5735',scarf:'#ffbf63',accent:'#c88135',fx:'#ffdb89'},
{id:'dragon',name:'邕江龙王',price:38888,tier:'镇店孤品',desc:'鎏金龙角 / 江潮长绫',detail:'江青鳞甲、鎏金双角、折纸龙脊、飘动长绫与水纹仪轨。最贵的不是狗，是排场。',coat:['#adecd9','#377e89','#193f57'],hood:'#71beb8',trim:'#ffe2a1',pocket:'#427986',scarf:'#f9d293',accent:'#b88a45',fx:'#a2f6dd'}];
const LEGEND_SKILLS=[
{id:'rail',name:'雷贯穿街',price:1200,tier:'珍藏',desc:'每次冲刺 / 雷弧穿街',detail:'冲刺发出一条真实前行雷弧，贯穿文件、卷走金币。主关冷却1.8秒；Boss开窗时反击威力2。'},
{id:'orbit',name:'万纸归宗',price:2800,tier:'史诗',desc:'三枚飞纸 / 自动护体',detail:'飞纸每0.4秒撕碎近身通知，吸附金币和咖啡；Boss开窗每0.75秒自动出纸。大招发三连纸剑。'},
{id:'leviathan',name:'鲸落清场',price:5800,tier:'传说',desc:'骑鲸大招 / 6.8秒横扫',detail:'六杯咖啡召来纸鲸，6.8秒自由模式。第一拍清空前方900范围，持续鲸息扫街；Boss每次开窗鲸炮威力3。'},
{id:'chrono',name:'拒绝时间',price:18888,tier:'镇店禁术',desc:'5秒时停 / 锁住破绽',detail:'大招让障碍与Boss攻击停5秒，你仍能跳、冲、反击。开窗时停住破绽；每次冲刺冷却0.45秒。闭盾仍要等。'}];
CATALOG.skins.push(...LEGEND_SKINS);CATALOG.skills.push(...LEGEND_SKILLS);
