// User tuning: roomier thumb placement, smaller playable dog and denser readable Boss salvos.
const PLAYER_SCALE=.8,PLAYER_BULLET_RADIUS=27*PLAYER_SCALE;
const BOSS_BULLET_LIMIT=64;
function playerCenter(){return{x:dogX()+17,y:GROUND+S.y-65*PLAYER_SCALE}}
function runnerContact(o,dx,vertical){const reach=o.coin?42:o.coffee||o.token?62:32+32*PLAYER_SCALE;const height=o.coin?44:o.coffee||o.token?57:32+32*PLAYER_SCALE;return !o.ghost&&dx<reach&&vertical<height}
function playerBulletContact(b,ax,ay,bx,by){const p=playerCenter();return segmentDistance(p.x,p.y,ax,ay,bx,by)<b.r+PLAYER_BULLET_RADIUS}
function playerDrawTransform(x=dogX(),y=GROUND+S.y){return `translate(${x+17*(1-PLAYER_SCALE)},${y}) scale(${PLAYER_SCALE})`}
function tuningSnapshot(){return{playerScale:PLAYER_SCALE,playerRadius:PLAYER_BULLET_RADIUS,center:playerCenter(),runReach:32+32*PLAYER_SCALE,bulletLimit:BOSS_BULLET_LIMIT,bulletStats:{...bulletStats},profiles:BULLET_PROFILES.map(p=>({...p})),stick:{x:stickCX,y:stickCY,r:stickRadius,unit:uiUnit}}}
