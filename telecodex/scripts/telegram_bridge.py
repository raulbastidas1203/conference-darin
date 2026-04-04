#!/usr/bin/env python3
import argparse
import json
import os
import sys
from pathlib import Path

import requests

BASE_DIR = Path(__file__).resolve().parents[1]
CONFIG_PATH = BASE_DIR / 'config' / 'telegram.settings.json'


def load_config():
    data = {}
    if CONFIG_PATH.exists():
        try:
            data = json.loads(CONFIG_PATH.read_text())
        except Exception:
            data = {}
    token = os.getenv('CODEX_TELEGRAM_BOT_TOKEN') or data.get('botToken')
    chat_id = os.getenv('CODEX_TELEGRAM_CHAT_ID') or data.get('chatId')
    return token, chat_id, data


def api(token, method, **params):
    url = f'https://api.telegram.org/bot{token}/{method}'
    r = requests.get(url, params=params, timeout=30)
    r.raise_for_status()
    return r.json()


def cmd_get_me(token):
    print(json.dumps(api(token, 'getMe'), indent=2, ensure_ascii=False))


def cmd_get_updates(token, offset=None):
    params = {}
    if offset is not None:
        params['offset'] = offset
    print(json.dumps(api(token, 'getUpdates', **params), indent=2, ensure_ascii=False))


def cmd_send(token, chat_id, text):
    if not chat_id:
        raise SystemExit('Missing chat_id. Set CODEX_TELEGRAM_CHAT_ID or config value.')
    print(json.dumps(api(token, 'sendMessage', chat_id=chat_id, text=text), indent=2, ensure_ascii=False))


def main():
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest='cmd', required=True)

    sub.add_parser('get-me')
    gu = sub.add_parser('get-updates')
    gu.add_argument('--offset', type=int)

    send = sub.add_parser('send')
    send.add_argument('--text', required=True)
    send.add_argument('--chat-id')

    args = parser.parse_args()
    token, default_chat_id, _ = load_config()
    if not token or token == 'SET_VIA_ENV_OR_LOCAL_ONLY':
        raise SystemExit('Missing bot token. Set CODEX_TELEGRAM_BOT_TOKEN or local config.')

    if args.cmd == 'get-me':
        cmd_get_me(token)
    elif args.cmd == 'get-updates':
        cmd_get_updates(token, args.offset)
    elif args.cmd == 'send':
        cmd_send(token, args.chat_id or default_chat_id, args.text)


if __name__ == '__main__':
    main()
