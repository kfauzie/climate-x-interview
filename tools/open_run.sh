#!/bin/bash
# Open a run's prototype in the browser, from any folder inside the repo.
# Usage: tools/open_run.sh        (the active run in CLAUDE.md)
#        tools/open_run.sh 3      (a specific run)
set -e
ROOT="$(git rev-parse --show-toplevel 2>/dev/null)" || { echo "Not inside the climate-x-interview folder. cd into it first."; exit 1; }
cd "$ROOT"
if git checkout -q main 2>/dev/null && git pull -q origin main 2>/dev/null; then echo "Got the latest version."
else echo "Couldn't get the latest version (not logged in to GitHub, or offline). Opening what's on this Mac."
     echo "To log in: gh auth login   (then run this again)"; fi
RUN="${1:-$(grep -o 'runs/run-[0-9]*' CLAUDE.md | head -1 | grep -o '[0-9]*$')}"
DIR="runs/run-$RUN"
[ -f "$DIR/build/mvp.html" ] || { echo "No prototype at $DIR/build/mvp.html"; exit 1; }
PORT=8000; while lsof -i :$PORT >/dev/null 2>&1; do PORT=$((PORT+1)); done   # first free port
URL="http://localhost:$PORT/build/mvp.html"
echo "Run $RUN prototype: $URL   (Control+C to stop)"
( sleep 1; open "$URL" 2>/dev/null || xdg-open "$URL" 2>/dev/null ) &
cd "$DIR" && exec python3 -m http.server $PORT
