#!/usr/bin/env python3
import json
import time
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
RUNTIME = BASE_DIR / 'runtime'
SESSIONS_JSON = RUNTIME / 'codex_sessions.json'
MONITORS = RUNTIME / 'session_monitors.json'
OUTBOX = RUNTIME / 'outbox.jsonl'


def append(path: Path, obj: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('a', encoding='utf-8') as f:
        f.write(json.dumps(obj, ensure_ascii=False) + '\n')


def load_json(path: Path, default):
    if path.exists():
        try:
            return json.loads(path.read_text(encoding='utf-8'))
        except Exception:
            pass
    return default


def save_json(path: Path, data):
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8')


def load_sessions():
    return load_json(SESSIONS_JSON, [])


def resolve(alias: str):
    for s in load_sessions():
        if s.get('alias') == alias:
            return s
    return None


def extract_last_status(file_path: Path):
    if not file_path.exists():
        return None
    lines = file_path.read_text(encoding='utf-8', errors='replace').splitlines()
    last_completed = None
    agent_messages = []
    for line in reversed(lines[-120:]):
        try:
            obj = json.loads(line)
        except Exception:
            continue
        t = obj.get('type')
        payload = obj.get('payload') or {}
        if t == 'event_msg' and payload.get('type') == 'turn_completed' and not last_completed:
            last_completed = obj.get('timestamp')
        if t == 'event_msg' and payload.get('type') == 'agent_message':
            msg = payload.get('message')
            if msg:
                agent_messages.append(msg)
        if last_completed and len(agent_messages) >= 3:
            break
    agent_messages.reverse()
    return {'last_completed': last_completed, 'agent_messages': agent_messages[-3:], 'line_count': len(lines)}


def tick():
    monitors = load_json(MONITORS, {})
    changed = False
    for chat_id, mon in list(monitors.items()):
        alias = mon.get('alias')
        sess = resolve(alias)
        if not sess or not sess.get('file'):
            continue
        status = extract_last_status(Path(sess['file']))
        if not status:
            continue
        prev_completed = mon.get('last_completed')
        prev_lines = mon.get('line_count', 0)
        now_completed = status.get('last_completed')
        now_lines = status.get('line_count', 0)
        if now_lines != prev_lines:
            mon['line_count'] = now_lines
            changed = True
        if now_completed and now_completed != prev_completed:
            mon['last_completed'] = now_completed
            changed = True
            text = f"{alias} terminó de trabajar."
            msgs = status.get('agent_messages') or []
            if msgs:
                preview = '\n\n'.join(msgs[-3:])
                text += f"\n\nMensajes recientes:\n{preview[:2000]}"
            append(OUTBOX, {'kind': 'reply', 'chat_id': chat_id, 'text': text})
    if changed:
        save_json(MONITORS, monitors)


if __name__ == '__main__':
    tick()
