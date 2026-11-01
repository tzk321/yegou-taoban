set -eu
cd "$(dirname "$0")"
sh build-check.sh
node validate-audit.mjs
node qa-tuning-v60.mjs
node qa-polish-v60.mjs
node qa-stick-fullscreen-v60.mjs
node qa-mechanisms-v60.mjs
node qa-audio-v60.mjs
node qa-bgm-level-v60.mjs
node qa-visual-v60.mjs
node qa-realtime-v60.mjs
node qa-movehud-v60.mjs
node qa-overlap-v60.mjs
node qa-hud-v60.mjs
node qa-bosses-v60.mjs
node qa-regression-v60.mjs
node qa-persistence-v60.mjs
node qa-observable-v60.mjs
node qa-gear-matrix-v60.mjs
node qa-newgear-matrix-v60.mjs
node qa-lastedges-v60.mjs
node qa-grant-quota-v60.mjs
python3 audit-proof.py
node qa-perf-v60.mjs
chmod -R a+rwX night-off-out
