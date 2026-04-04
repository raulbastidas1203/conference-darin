#!/usr/bin/env python3
import argparse
import json
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
RUNTIME = BASE_DIR / 'runtime'
OUTBOX = RUNTIME / 'outbox.jsonl'
EVENTS = RUNTIME / 'events.jsonl'
LOGS = BASE_DIR / 'logs'
STATE = RUNTIME / 'state.json'
def find_codex_bin():
    candidates = [
        Path.home() / '.vscode' / 'extensions' / 'openai.chatgpt-26.5401.11717-linux-x64' / 'bin' / 'linux-x86_64' / 'codex',
        Path.home() / '.cursor' / 'extensions' / 'openai.chatgpt-26.325.31654-linux-x64' / 'bin' / 'linux-x86_64' / 'codex',
    ]
    for p in candidates:
        if p.exists():
            return p
    return candidates[0]


CODEX_BIN = find_codex_bin()


def append_jsonl(path: Path, obj: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('a', encoding='utf-8') as f:
        f.write(json.dumps(obj, ensure_ascii=False) + '\n')


def load_processing_message_id(chat_id: str):
    if not STATE.exists():
        return None
    try:
        state = json.loads(STATE.read_text(encoding='utf-8'))
        return state.get(f'processing:{chat_id}')
    except Exception:
        return None


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--text', required=True)
    p.add_argument('--chat-id', required=True)
    p.add_argument('--cwd', required=True)
    args = p.parse_args()

    cwd = Path(args.cwd)
    processing_message_id = load_processing_message_id(args.chat_id)
    append_jsonl(EVENTS, {'type': 'progress', 'text': f'Sesión fresca Codex en {cwd}'})

    if not CODEX_BIN.exists():
        msg = 'No encontré el binario de Codex en la extensión de Cursor.'
        payload = {'kind': 'reply', 'chat_id': args.chat_id, 'text': msg}
        if processing_message_id:
            payload = {'kind': 'edit', 'chat_id': args.chat_id, 'message_id': processing_message_id, 'text': msg}
        append_jsonl(OUTBOX, payload)
        return

    LOGS.mkdir(parents=True, exist_ok=True)
    output_file = LOGS / 'codex-fresh-last.txt'
    cmd = [
        str(CODEX_BIN), 'exec',
        '-C', str(cwd),
        '--json',
        '--dangerously-bypass-approvals-and-sandbox',
        '-o', str(output_file),
        args.text,
    ]
    proc = subprocess.run(cmd, text=True, capture_output=True)

    if proc.returncode != 0:
        detail = (proc.stderr or proc.stdout or 'sin detalle').strip()[-1200:]
        append_jsonl(EVENTS, {'type': 'error', 'text': 'Falló sesión fresca Codex', 'stderr_tail': detail})
        payload = {'kind': 'reply', 'chat_id': args.chat_id, 'text': f'Falló sesión fresca.\n\n{detail}'}
        if processing_message_id:
            payload = {'kind': 'edit', 'chat_id': args.chat_id, 'message_id': processing_message_id, 'text': f'Falló sesión fresca.\n\n{detail}'}
        append_jsonl(OUTBOX, payload)
        return

    final_text = output_file.read_text(encoding='utf-8', errors='replace').strip() if output_file.exists() else 'Sin respuesta final.'
    append_jsonl(EVENTS, {'type': 'done', 'text': f'Respuesta de sesión fresca en {cwd}'})
    payload = {'kind': 'reply', 'chat_id': args.chat_id, 'text': f'Codex fresh · {cwd}\n\n{final_text[:3500]}'}
    if processing_message_id:
        payload = {'kind': 'edit', 'chat_id': args.chat_id, 'message_id': processing_message_id, 'text': f'Codex fresh · {cwd}\n\n{final_text[:3500]}'}
    append_jsonl(OUTBOX, payload)


if __name__ == '__main__':
    main()
