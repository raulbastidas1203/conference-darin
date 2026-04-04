#!/usr/bin/env python3
import json
from datetime import datetime
from pathlib import Path

INDEX = Path.home() / '.codex' / 'session_index.jsonl'
OUT = Path('/home/raul/CLAUDE/openclaw/telecodex/runtime/codex_sessions.json')


def parse_dt(value: str):
    try:
        return datetime.fromisoformat(value.replace('Z', '+00:00'))
    except Exception:
        return datetime.min


def main():
    sessions = []
    if INDEX.exists():
        for line in INDEX.read_text(encoding='utf-8').splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                item = json.loads(line)
            except Exception:
                continue
            sessions.append({
                'id': item.get('id'),
                'thread_name': item.get('thread_name') or '(sin título)',
                'updated_at': item.get('updated_at'),
            })
    sessions.sort(key=lambda x: parse_dt(x.get('updated_at') or ''), reverse=True)
    mapped = []
    for i, s in enumerate(sessions[:20], start=1):
        mapped.append({
            'alias': f'C{i}',
            **s,
        })
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(mapped, indent=2, ensure_ascii=False), encoding='utf-8')
    print(json.dumps(mapped[:10], ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
