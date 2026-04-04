#!/usr/bin/env python3
import json
from pathlib import Path

RUNTIME = Path('/home/raul/CLAUDE/openclaw/telecodex/runtime')
PENDING_UI = RUNTIME / 'pending_ui_requests.json'
OUTBOX = RUNTIME / 'outbox.jsonl'


def append(obj):
    OUTBOX.parent.mkdir(parents=True, exist_ok=True)
    with OUTBOX.open('a', encoding='utf-8') as f:
        f.write(json.dumps(obj, ensure_ascii=False) + '\n')


def save_pending(data):
    PENDING_UI.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding='utf-8')


def load_pending():
    if PENDING_UI.exists():
        try:
            return json.loads(PENDING_UI.read_text(encoding='utf-8'))
        except Exception:
            pass
    return {}


def maybe_json(value):
    if isinstance(value, str):
        try:
            return json.loads(value)
        except Exception:
            return value
    return value


def send_question(chat_id: str, alias: str, state: dict):
    idx = state.get('current_index', 0)
    questions = state.get('questions', [])
    if idx >= len(questions):
        answers = state.get('answers', [])
        lines = [f'{alias} · respuestas capturadas:']
        for ans in answers:
            lines.append(f"- {ans['header']}: {ans['label']}")
            if ans.get('description'):
                lines.append(f"  {ans['description']}")
        append({'kind': 'reply', 'chat_id': chat_id, 'text': '\n'.join(lines)[:3500]})
        return

    q = questions[idx]
    header = q.get('header') or f'Pregunta {idx+1}'
    question = q.get('question') or q.get('prompt') or 'Sin pregunta visible'
    lines = [f'{alias} necesita tu respuesta.', '', f'{header}', question, '']
    keyboard = []
    for opt in q.get('options', []):
        label = opt.get('label') or opt.get('value') or 'Opción'
        desc = opt.get('description') or ''
        lines.append(f'- {label}')
        if desc:
            lines.append(f'  {desc}')
        keyboard.append([label])
    append({'kind': 'reply', 'chat_id': chat_id, 'text': '\n'.join(lines)[:3500], 'keyboard': keyboard if keyboard else None})


def emit_request(chat_id: str, alias: str, raw_text: str):
    payload = maybe_json(raw_text)
    if isinstance(payload, dict) and 'arguments' in payload:
        payload = maybe_json(payload['arguments'])
    if not isinstance(payload, dict):
        append({'kind': 'reply', 'chat_id': chat_id, 'text': f'{alias} te está pidiendo respuesta, pero no pude parsear las opciones.\n\n{str(raw_text)[:1800]}'} )
        return

    questions = payload.get('questions') or []
    if not questions:
        append({'kind': 'reply', 'chat_id': chat_id, 'text': f'{alias} te está pidiendo respuesta, pero no encontré preguntas estructuradas.\n\n{json.dumps(payload, ensure_ascii=False)[:1800]}'} )
        return

    normalized = []
    for q in questions:
        opts = []
        for opt in q.get('options', []):
            opts.append({
                'label': opt.get('label') or opt.get('value') or 'Opción',
                'value': opt.get('value') or opt.get('label') or 'Opción',
                'description': opt.get('description') or '',
            })
        normalized.append({
            'header': q.get('header') or 'Pregunta',
            'id': q.get('id'),
            'question': q.get('question') or q.get('prompt') or 'Sin pregunta visible',
            'options': opts,
        })

    pending = load_pending()
    pending[str(chat_id)] = {
        'alias': alias,
        'questions': normalized,
        'current_index': 0,
        'answers': [],
        'raw': payload,
    }
    save_pending(pending)
    send_question(chat_id, alias, pending[str(chat_id)])


if __name__ == '__main__':
    pass
