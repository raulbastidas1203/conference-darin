# telecodex

Puente local entre Telegram y sesiones de Codex para seguir chats, recibir progreso, responder cuestionarios y continuar trabajo remoto sin mirar la laptop todo el tiempo.

Repo privada actual:
- <https://github.com/raulbastidas1203/telecodex>

## Qué hace hoy

### Monitoreo de sesiones Codex
- lista sesiones reales desde `~/.codex/session_index.jsonl`
- mapea alias como `C1`, `C2`, `C3`
- permite conectarte a una sesión con `/connect C1`
- avisa por Telegram cuando el chat:
  - recibe un prompt nuevo
  - publica mensajes intermedios del agente
  - usa tools
  - termina un turno

### Envío de prompts
- `/codex C1 <mensaje>` → reanuda una sesión existente
- `/codexnew --cwd /ruta <mensaje>` → crea una ejecución fresca con cwd explícito
- confirmación previa antes de enviar cuando hace falta
- mensaje temporal de `Procesando...` con reemplazo por la respuesta final

### Cuestionarios y decisiones
- detecta `request_user_input` emitidos por Codex
- renderiza preguntas con:
  - header
  - pregunta
  - opciones
  - descripción extra
- muestra botones en Telegram
- soporta flujo secuencial de varias preguntas
- al terminar, reenvía automáticamente las respuestas al hilo de Codex

### Respuestas largas
- divide salidas largas en varios mensajes de Telegram
- usa chunks numerados para no truncar planes o respuestas extensas

## Comandos del bot
- `/help`
- `/status`
- `/inbox`
- `/last`
- `/chats`
- `/connect C1`
- `/disconnect`
- `/codex C1 <mensaje>`
- `/codexnew --cwd /ruta <mensaje>`

## Arquitectura local

Directorio principal:
- `telecodex/`

Piezas importantes:
- `scripts/watcher.py` → Telegram polling + outbox + edits
- `scripts/telegram_commands.py` → comandos del bot y flujo de respuestas
- `scripts/list_codex_sessions.py` → indexa sesiones Codex reales
- `scripts/session_monitor.py` → monitoriza progreso del chat conectado
- `scripts/send_codex_message.py` → reanuda una sesión existente
- `scripts/send_codex_fresh.py` → ejecución fresca con cwd controlado
- `scripts/request_ui.py` → render de cuestionarios estructurados
- `runtime/` → estado local del bridge
- `logs/` → logs y salidas capturadas

## Requisitos
- Linux
- Python 3
- bot de Telegram
- sesión de GitHub si quieres publicar cambios del repo
- instalación local de Codex vía VS Code o Cursor

El bridge hoy prioriza el binario de VS Code y cae al de Cursor si hace falta.

## Estado actual

El proyecto ya funciona para el flujo principal:
- seguir un chat de Codex desde Telegram
- ver progreso intermedio
- saber cuándo terminó
- responder cuestionarios estructurados
- reenviar respuestas al hilo

## Limitaciones abiertas
- responder `request_user_input` de forma realmente nativa por `call_id` sería mejor que reenviarlo como continuación textual; aún está pendiente explorar eso
- todavía puede haber casos finos de desincronización si Codex lanza varios bloques interactivos muy seguidos
- hay artefactos locales (`logs/`, `runtime/`, `.env`) que deben mantenerse fuera del repo versionado

## Resumen de trabajo
También hay un resumen más narrativo en:
- `WORKLOG_SUMMARY_2026-04-04.md`
