#!/usr/bin/env python3
import argparse
import json
import time
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
RUNTIME_DIR = BASE_DIR / 'runtime'
EVENTS_PATH = RUNTIME_DIR / 'events.jsonl'


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--type', required=True, choices=['progress', 'waiting', 'done', 'error', 'event'])
    p.add_argument('--text', required=True)
    args = p.parse_args()

    RUNTIME_DIR.mkdir(parents=True, exist_ok=True)
    payload = {
        'ts': int(time.time()),
        'type': args.type,
        'text': args.text,
    }
    with EVENTS_PATH.open('a', encoding='utf-8') as f:
        f.write(json.dumps(payload, ensure_ascii=False) + '\n')
    print(json.dumps(payload, ensure_ascii=False))


if __name__ == '__main__':
    main()
