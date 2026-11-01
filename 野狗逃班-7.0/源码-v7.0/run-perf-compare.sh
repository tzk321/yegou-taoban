set -eu
cd /mnt/data/user/0/me.rerere.rikkahub/files/tmp/night-off-v70
node bench-polish.mjs baseline /mnt/data/user/0/me.rerere.rikkahub/files/tmp/night-off-v60-before-skillfx/night-off-out/night-off.html
node bench-polish.mjs after
