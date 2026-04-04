#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python3 scripts/sync_cursor_inbox.py
if command -v cursor >/dev/null 2>&1; then
  cursor -r .cursor-telegram/inbox.md || true
else
  echo '.cursor-telegram/inbox.md actualizado'
fi
