#!/usr/bin/env bash
# Regenerate the Tron backgrounds from scratch. Requires ImageMagick 7 and python3.
#
#   ./tools/generate-backgrounds.sh
#
# gen_mvg.py emits ImageMagick vector graphics for each scene; every scene is
# then drawn on black, blurred into a glow layer, and screened back over a dark
# gradient so the lines read as emissive rather than painted.
set -euo pipefail

cd "$(dirname "$0")/.."
out="backgrounds"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

draw() { magick -size 3840x2160 xc:black -draw "@$1" PNG24:"$2"; }

python3 tools/gen_mvg.py grid >"$tmp/grid.mvg"
python3 tools/gen_mvg.py circuits >"$tmp/circuits.mvg"
python3 tools/gen_mvg.py disc >"$tmp/disc.mvg"

draw "$tmp/grid.mvg" "$tmp/grid.png"
draw "$tmp/circuits.mvg" "$tmp/circuits.png"
draw "$tmp/disc.mvg" "$tmp/disc.png"

# 1 - the grid plane, with a soft horizon bloom behind the vanishing point
magick -size 960x540 xc:black -fill '#39a6c8' -draw "ellipse 480,295 235,52 0,360" \
  -blur 0x42 -resize 3840x2160\! PNG24:"$tmp/horizon.png"
magick "$tmp/grid.png" -blur 0x28 -modulate 100,110 PNG24:"$tmp/grid-glow.png"
magick -size 3840x2160 gradient:'#020a10'-'#010405' \
  "$tmp/horizon.png" -compose screen -composite \
  "$tmp/grid-glow.png" -compose screen -composite \
  "$tmp/grid.png" -compose screen -composite \
  \( -size 3840x2160 radial-gradient:'#ffffff'-'#6e6e6e' \) -compose multiply -composite \
  -modulate 100,112 PNG24:"$out/1-grid.png"

# 2 - circuit traces
magick "$tmp/circuits.png" -blur 0x22 PNG24:"$tmp/circuits-glow.png"
magick -size 3840x2160 gradient:'#03101a'-'#010507' \
  "$tmp/circuits-glow.png" -compose screen -composite \
  "$tmp/circuits.png" -compose screen -composite \
  \( -size 3840x2160 radial-gradient:'#ffffff'-'#454545' \) -compose multiply -composite \
  PNG24:"$out/2-circuits.png"

# 3 - identity disc
magick "$tmp/disc.png" -blur 0x34 PNG24:"$tmp/disc-glow.png"
magick -size 3840x2160 gradient:'#04121c'-'#01060a' \
  "$tmp/disc-glow.png" -compose screen -composite \
  "$tmp/disc.png" -compose screen -composite \
  \( -size 3840x2160 radial-gradient:'#ffffff'-'#3c3c3c' \) -compose multiply -composite \
  -modulate 100,108 PNG24:"$out/3-identity-disc.png"

echo "Wrote $out/1-grid.png $out/2-circuits.png $out/3-identity-disc.png"
