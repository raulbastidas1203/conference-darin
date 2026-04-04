#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
TYPE="${1:-progress}"
shift || true
TEXT="${*:-sin mensaje}"
python3 scripts/emit_event.py --type "$TYPE" --text "$TEXT"
python3 scripts/watcher.py --once
