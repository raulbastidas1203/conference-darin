# Telecodex - resumen de trabajo hasta hoy

## Objetivo
Montar un puente entre Telegram (`@darin02_bot`) y sesiones de Codex para:
- monitorear chats de Codex desde el celular
- recibir progreso y aviso de finalización
- enviar prompts al mismo hilo
- responder cuestionarios estructurados desde Telegram

## Lo construido
- Bridge Linux en `telecodex/`
- Watcher de Telegram con inbox/outbox
- Sincronización a archivo legible para Cursor/VS Code
- Detección de sesiones reales desde `~/.codex/session_index.jsonl`
- Comandos de bot: `/help`, `/status`, `/inbox`, `/last`, `/chats`, `/connect`, `/disconnect`, `/codex`, `/codexnew`
- Monitoreo de sesiones con eventos intermedios (`task_started`, `agent_message`, `tool_call`, `task_complete`)
- Detección de `request_user_input`
- Flujo secuencial de cuestionarios con botones en Telegram
- Reenvío automático del paquete final de respuestas al hilo de Codex

## Problemas encontrados y soluciones
- Conflictos `409` de Telegram polling -> tolerancia en watcher
- Loops al hablarle a una sesión que estaba construyendo el propio bridge -> guardrails y sesiones riesgosas
- `cwd` correcto pero contexto viejo contaminaba sesiones resumidas -> modo fresh y luego foco en monitorización del hilo real
- Parser roto / edits fallidos -> limpieza y reescritura de archivos clave
- El monitor no detectaba finalización en VS Code porque el evento real era `task_complete` -> corregido
- `request_user_input` se mostraba como nombre genérico -> parser del payload real con `questions/options/description`
- Cuestionarios con varias preguntas -> flujo secuencial implementado
- Respuestas largas truncadas en Telegram -> se añadió chunking por partes

## Estado actual
El sistema ya permite:
- conectarse a un chat de Codex con `/connect C1`
- ver progreso intermedio
- saber cuándo terminó
- ver preguntas estructuradas con opciones y descripciones
- responderlas desde Telegram
- reenviar esas respuestas al hilo
- arrancar automáticamente como servicio de usuario en Linux

## Pendientes
- Intentar responder `request_user_input` de forma más nativa al `call_id`, en vez de resumirlo como prompt nuevo
- Afinar deduplicación/estado cuando Codex genera varios bloques de preguntas seguidos
- Mejorar formateo y rate limiting de mensajes de progreso para evitar ruido
