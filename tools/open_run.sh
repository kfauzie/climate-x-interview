#!/bin/bash
# Open a run's prototype in the browser, from any folder inside the repo.
# Usage: tools/open_run.sh 3      (run 3)
set -e
RUN="${1:?Which run? e.g. tools/open_run.sh 3}"
ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "Not inside the climate-x-interview folder. cd into it first."; exit 1; }
cd "$ROOT"
git checkout -q main && git pull -q origin main || echo "(Couldn't get the latest version; opening what's on this Mac.)"
DIR="runs/run-$RUN"
[ -f "$DIR/build/mvp.html" ] || { echo "No prototype at $DIR/build/mvp.html"; exit 1; }
PORT=8000; while lsof -i :$PORT >/dev/null 2>&1; do PORT=$((PORT+1)); done   # first free port
URL="http://localhost:$PORT/build/mvp.html"
echo "Run $RUN prototype: $URL   (Control+C to stop)"
( sleep 1; open "$URL" 2>/dev/null || xdg-open "$URL" 2>/dev/null ) &
cd "$DIR" && exec python3 -m http.server $PORT
