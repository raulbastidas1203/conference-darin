#!/usr/bin/env python3
import argparse
import json
import subprocess
import sys
import time
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
RUNTIME = BASE_DIR / 'runtime'
EVENTS = RUNTIME / 'events.jsonl'


def emit(event_type: str, text: str, extra: dict | None = None):
    payload = {'ts': int(time.time()), 'type': event_type, 'text': text}
    if extra:
        payload.update(extra)
    RUNTIME.mkdir(parents=True, exist_ok=True)
    with EVENTS.open('a', encoding='utf-8') as f:
        f.write(json.dumps(payload, ensure_ascii=False) + '\n')


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--label', required=True)
    p.add_argument('cmd', nargs=argparse.REMAINDER)
    args = p.parse_args()

    cmd = args.cmd
    if cmd and cmd[0] == '--':
        cmd = cmd[1:]
    if not cmd:
        raise SystemExit('Usage: run_task.py --label "nombre" -- <comando> [args...]')

    emit('progress', f"Iniciando: {args.label}", {'command': cmd})
    start = time.time()
    proc = subprocess.run(cmd, capture_output=True, text=True)
    duration = round(time.time() - start, 2)

    stdout = (proc.stdout or '').strip()
    stderr = (proc.stderr or '').strip()
    extra = {'returncode': proc.returncode, 'duration_sec': duration}
    if stdout:
        extra['stdout_tail'] = stdout[-600:]
    if stderr:
        extra['stderr_tail'] = stderr[-600:]

    if proc.returncode == 0:
        emit('done', f"Completado: {args.label}", extra)
    else:
        emit('error', f"Falló: {args.label}", extra)

    print(json.dumps({'label': args.label, 'returncode': proc.returncode, 'duration_sec': duration}, ensure_ascii=False))
    raise SystemExit(proc.returncode)


if __name__ == '__main__':
    main()
