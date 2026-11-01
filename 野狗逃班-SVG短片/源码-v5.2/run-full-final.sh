#!/bin/bash
set -e
cd /mnt/data/user/0/me.rerere.rikkahub/files/tmp/night-off-v52
python3 maps-art.py
python3 prepare-v52.py
node --check game-v52.js
python3 build-v52.py
python3 refresh-regressions.py
for test in qa-v52-smoke.mjs qa-v52-audit.mjs qa-v52-maps.mjs qa-v52-codex.mjs qa-v52-balance-new.mjs qa-v52-legacy.mjs qa-v52-gear-maps.mjs qa-v52-persistence.mjs qa-v52-branches.mjs qa-v52-matrix.mjs qa-v52-shop.mjs qa-v52-edges-new.mjs qa-v52-assets.mjs qa-v52-native-boundaries.mjs qa-v52-native-economy.mjs qa-v52-native-balance.mjs qa-v52-native-integration.mjs qa-v52-cosmetics.mjs qa-v52-cap.mjs qa-v52-hud.mjs qa-v52-readable.mjs qa-v52-realtime.mjs; do
 echo "===== FINAL $test ====="
 node "$test"
 python3 clean-isolated-profiles.py
 done
echo ALL_FINAL_DONE
