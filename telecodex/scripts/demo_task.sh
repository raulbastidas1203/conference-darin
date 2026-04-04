#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python3 scripts/run_task.py --label "demo ls telecodex" -- ls -la .
