#!/usr/bin/env python3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
INBOX_PATH = BASE_DIR / 'runtime' / 'inbox.jsonl'

if INBOX_PATH.exists():
    print(INBOX_PATH.read_text(encoding='utf-8'))
