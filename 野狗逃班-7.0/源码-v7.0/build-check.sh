set -eu
cd "$(dirname "$0")"
node prepare-v70.mjs
node --check game-v70.js
python3 build-v70.py
chmod -R a+rwX .
