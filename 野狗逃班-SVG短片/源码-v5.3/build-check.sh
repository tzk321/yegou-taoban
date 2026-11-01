set -eu
cd /mnt/data/user/0/me.rerere.rikkahub/files/tmp/night-off-v53
node prepare-v53.mjs
node --check game-v53.js
python3 build-v53.py
chmod -R a+rwX .
