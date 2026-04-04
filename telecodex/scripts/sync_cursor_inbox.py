#!/usr/bin/env python3
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
RUNTIME_DIR = BASE_DIR / 'runtime'
INBOX_JSONL = RUNTIME_DIR / 'inbox.jsonl'
CURSOR_DIR = BASE_DIR / '.cursor-telegram'
CURSOR_INBOX = CURSOR_DIR / 'inbox.md'
STATE_PATH = RUNTIME_DIR / 'cursor_inbox_state.json'


def load_state():
    if STATE_PATH.exists():
        try:
            return json.loads(STATE_PATH.read_text(encoding='utf-8'))
        except Exception:
            pass
    return {'last_line': 0}


def save_state(state):
    STATE_PATH.write_text(json.dumps(state, indent=2), encoding='utf-8')


def main():
    CURSOR_DIR.mkdir(parents=True, exist_ok=True)
    RUNTIME_DIR.mkdir(parents=True, exist_ok=True)
    if not INBOX_JSONL.exists():
        INBOX_JSONL.write_text('', encoding='utf-8')

    state = load_state()
    lines = INBOX_JSONL.read_text(encoding='utf-8').splitlines()
    new = lines[state.get('last_line', 0):]
    if not new:
        return

    with CURSOR_INBOX.open('a', encoding='utf-8') as out:
        for line in new:
            line = line.strip()
            if not line:
                state['last_line'] = state.get('last_line', 0) + 1
                continue
            try:
                item = json.loads(line)
                who = item.get('from') or 'telegram'
                text = item.get('text') or ''
                ts = item.get('ts')
                out.write(f"\n## Mensaje desde Telegram\n- from: {who}\n- ts: {ts}\n\n{text}\n")
            except Exception:
                out.write(f"\n## Mensaje desde Telegram\n\n{line}\n")
            state['last_line'] = state.get('last_line', 0) + 1

    save_state(state)


if __name__ == '__main__':
    main()
