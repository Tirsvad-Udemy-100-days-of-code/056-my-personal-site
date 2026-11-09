#!/usr/bin/env bash
# Take a screenshot of the running site in a Docker container.
#
# The application and a headless Chromium both run in containers on a private
# Docker network, so no window opens on the host desktop and no host port is
# exposed (framework/process/gui-testing.md).
#
# Usage:   scripts/take-screenshot.sh <file-name.png> [url-path] [width] [height]
# Example: scripts/take-screenshot.sh lecture-1.png / 1280 800
# Output:  docs/screenshots/<file-name.png>
# Needs:   bash, Docker (running). The first run pulls python:3.13-slim and
#          zenika/alpine-chrome.
# Exit:    0 the screenshot was written; 1 an error
set -euo pipefail

name="${1:?usage: $0 <file-name.png> [url-path] [width] [height]}"
path="${2:-/}"
width="${3:-1280}"
height="${4:-800}"

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
if command -v cygpath >/dev/null 2>&1; then
  root_host="$(cygpath -m "$root")"
else
  root_host="$root"
fi
export MSYS_NO_PATHCONV=1

network="personal-site-shot"
app="personal-site-app"

cleanup() {
  docker rm -f "$app" >/dev/null 2>&1 || true
  docker network rm "$network" >/dev/null 2>&1 || true
}
trap cleanup EXIT
cleanup

mkdir -p "$root/docs/screenshots"
docker network create "$network" >/dev/null

# Copy the project inside the container so that nothing is written to the repository.
docker run -d --name "$app" --network "$network" \
  -v "$root_host:/source:ro" python:3.13-slim sh -c \
  'cp -r /source /app && cd /app && python -m pip install -q . && \
   python -m flask --app personal_site.presentation.server run --host 0.0.0.0 --port 5000' \
  >/dev/null

for _ in $(seq 1 90); do
  if docker logs "$app" 2>&1 | grep -q "Running on"; then
    break
  fi
  sleep 2
done
docker logs "$app" 2>&1 | grep -q "Running on" || { docker logs "$app" >&2; echo "app did not start" >&2; exit 1; }

docker run --rm --network "$network" \
  -v "$root_host/docs/screenshots:/out" zenika/alpine-chrome:latest \
  --no-sandbox --hide-scrollbars --disable-gpu \
  --window-size="$width,$height" --virtual-time-budget=5000 \
  --screenshot="/out/$name" "http://$app:5000$path" >/dev/null

echo "wrote docs/screenshots/$name"
