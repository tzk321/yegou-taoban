set -eu
cd "$(dirname "$0")"
node prepare-v60.mjs
node --check game-v60.js
python3 build-v60.py
chmod -R a+rwX .
