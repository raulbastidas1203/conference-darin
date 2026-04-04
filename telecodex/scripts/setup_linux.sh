#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python3 -m venv .venv
. .venv/bin/activate
pip install -U pip
pip install -r requirements.txt

echo
echo 'telecodex Linux listo.'
echo 'Exporta tu token:'
echo "  export CODEX_TELEGRAM_BOT_TOKEN='TU_BOT_TOKEN'"
echo 'Luego prueba:'
echo '  python scripts/telegram_bridge.py get-me'
echo '  python scripts/telegram_bridge.py get-updates'
