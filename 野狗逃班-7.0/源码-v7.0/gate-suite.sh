set -eu
cd "$(dirname "$0")"
sh build-check.sh
node validate-audit.mjs
node qa-skillfx-v70.mjs
node qa-skillfx-raf-v70.mjs
node qa-tuning-v70.mjs
node qa-polish-v70.mjs
node qa-stick-fullscreen-v70.mjs
node qa-mechanisms-v70.mjs
node qa-audio-v70.mjs
node qa-bgm-level-v70.mjs
node qa-visual-v70.mjs
node qa-realtime-v70.mjs
node qa-movehud-v70.mjs
node qa-overlap-v70.mjs
node qa-hud-v70.mjs
node qa-bosses-v70.mjs
node qa-regression-v70.mjs
node qa-persistence-v70.mjs
node qa-observable-v70.mjs
node qa-gear-matrix-v70.mjs
node qa-newgear-matrix-v70.mjs
node qa-lastedges-v70.mjs
node qa-grant-quota-v70.mjs
python3 audit-proof.py
node qa-perf-v70.mjs
chmod -R a+rwX night-off-out
