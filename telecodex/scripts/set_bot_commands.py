#!/usr/bin/env python3
import json
import os
from pathlib import Path

import requests

BASE_DIR = Path(__file__).resolve().parents[1]
ENV_PATH = BASE_DIR / '.env'
CONFIG_PATH = BASE_DIR / 'config' / 'telegram.settings.json'


def load_dotenv():
    if not ENV_PATH.exists():
        return
    for raw in ENV_PATH.read_text(encoding='utf-8').splitlines():
        line = raw.strip()
        if not line or line.startswith('#') or '=' not in line:
            continue
        k, v = line.split('=', 1)
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def load_token():
    load_dotenv()
    token = os.getenv('CODEX_TELEGRAM_BOT_TOKEN') or os.getenv('TELECODEX_BOT_TOKEN')
    if token:
        return token
    if CONFIG_PATH.exists():
        data = json.loads(CONFIG_PATH.read_text(encoding='utf-8'))
        token = data.get('botToken')
        if token and token != 'SET_VIA_ENV_OR_LOCAL_ONLY':
            return token
    return None


def main():
    token = load_token()
    if not token:
        raise SystemExit('Missing Telegram bot token')

    commands = [
        {'command': 'help', 'description': 'Muestra ayuda y comandos'},
        {'command': 'status', 'description': 'Ver últimos eventos útiles'},
        {'command': 'inbox', 'description': 'Ver mensajes recientes recibidos'},
        {'command': 'last', 'description': 'Ver el último evento'},
        {'command': 'chats', 'description': 'Listar sesiones Codex recientes'},
    ]

    url = f'https://api.telegram.org/bot{token}/setMyCommands'
    r = requests.post(url, json={'commands': commands}, timeout=30)
    r.raise_for_status()
    print(r.text)


if __name__ == '__main__':
    main()
