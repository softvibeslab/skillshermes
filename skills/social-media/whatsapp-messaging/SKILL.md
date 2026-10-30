---
name: whatsapp-messaging
description: Send and receive WhatsApp messages via Hermes
category: social-media
tools: [send_message, session_search, cronjob, memory]
---

# WhatsApp Messaging Skill

## When to load this skill
Load this skill when you need to:
- Send a message to a WhatsApp contact or group via Hermes
- List available WhatsApp chats/contacts
- Receive or process inbound WhatsApp messages (via the conversation context)
- Automate WhatsApp notifications or reminders
- Back up or safely archive WhatsApp media before reclaiming local storage

## Prerequisites
- WhatsApp platform must be connected in Hermes (see `whatsapp: Connected ✓` in session context)
- The Hermes gateway must be running (`hermes gateway`) to maintain the WhatsApp connection.
- You must have the phone number associated with the WhatsApp account verified and able to send/receive messages through Hermes' WhatsApp bridge.

## Steps

### 1. List available WhatsApp targets
Use `send_message` with action='list' to see all WhatsApp chats/groups you can message.

```bash
send_message action='list'
```
Look for entries like:
- `whatsapp` (uses home channel)
- `whatsapp:-00000000000` (chat by ID)
- `whatsapp:-00000000000:thread_id` (if using topics/threads)

### 2. Send a WhatsApp message
To send a message, use `send_message` with the appropriate target.

**Example: send to home WhatsApp channel**
```bash
send_message target='whatsapp' message='¡Hola desde Hermes!'
```

If this fails with `No home channel set for whatsapp`, either set a home channel (`WHATSAPP_HOME_CHANNEL` / config) or use an explicit chat ID.

**Example: send to a specific chat known to Hermes (replace ID)**
```bash
send_message target='whatsapp:-00000000000' message='Reunión a las 15:00'
```

**Fallback: direct bridge send when Hermes has no WhatsApp targets cached**
Use only for diagnostics or when the user explicitly wants a test and provides/has a known chat ID. The chat ID must be a WhatsApp JID like `EXAMPLE_ID@EXAMPLE_DOMAIN`.

```bash
curl -sS --max-time 15 -X POST http://127.0.0.1:3000/send \
  -H 'Content-Type: application/json' \
  -d '{"chatId":"EXAMPLE_ID@EXAMPLE_DOMAIN","message":"Prueba de conexión desde Hermes por WhatsApp ✅"}'
```

A successful response looks like `{"success":true,"messageId":"..."}`. If `send_message` cannot resolve the WhatsApp target but this curl succeeds, the bridge is functional and Hermes needs WhatsApp channel-directory/home-channel configuration.

**Example: send with media**
Include `MEDIA:/path/to/file` in the message to attach images, audio, or video.
```bash
send_message target='whatsapp' message='Foto adjunta MEDIA:/tmp/photo.jpg'
```

**Fallback: direct bridge media send when `send_message` target resolution is broken**
If `send_message action='list'` shows a named WhatsApp target but sending to either `whatsapp:<name>` or `whatsapp:<jid>` still fails with `No home channel set for whatsapp`, bypass Hermes target resolution and call the bridge directly. This is useful after manually adding a contact to `~/.hermes/channel_directory.json` or before the gateway has fully reloaded the directory.

```bash
python3 - <<'PY'
import json, urllib.request
payload = {
  "chatId": "EXAMPLE_ID@EXAMPLE_DOMAIN",
  "filePath": "/absolute/path/to/file.pptx",
  "mediaType": "document",
  "caption": "Mensaje/caption aquí",
  "fileName": "file.pptx",
}
req = urllib.request.Request(
  "http://127.0.0.1:3000/send-media",
  data=json.dumps(payload).encode(),
  headers={"Content-Type": "application/json"},
  method="POST",
)
with urllib.request.urlopen(req, timeout=30) as r:
  print(r.status, r.read().decode())
PY
```

A successful response looks like `{"success":true,"messageId":"..."}`. For Mexico mobile numbers, normalize as `521` + 10 digits + `@s.whatsapp.net` (example `+52 55 0000 0000` → `REDACTED_LOCAL_VALUE@s.whatsapp.net`).

### 3. Receive and process inbound WhatsApp messages
Incoming WhatsApp messages appear in your conversation with Hermes just like any other platform. You can:
- Access them via the current session context (user's message).
- Use `session_search` to find past WhatsApp interactions.
- Trigger actions based on keywords or commands.

### 4. Automating WhatsApp notifications (cron jobs)
You can schedule periodic WhatsApp messages using `cronjob`.

**Example: daily reminder at 09:00**
```bash
cronjob action='create' name='daily-whatsapp-reminder' schedule='0 9 * * *' prompt="send_message target='whatsapp' message='Buenos días! Revisa tus tareas.'"
```

## Built-in Hermes WhatsApp vs external WhatsApp APIs/MCP

Use Hermes' built-in WhatsApp platform when the goal is for users to **chat with Hermes as a bot over WhatsApp**. It is a messaging gateway/channel: inbound messages become Hermes sessions; Hermes can reply, use tools, transcribe voice, and send media through the platform adapter.

Use an external API/MCP bridge (for example Open-WA Easy API with MCP) when the goal is **business-system automation over WhatsApp**: CRM follow-ups, webhooks, contact/chat/group/media operations, exposing WhatsApp methods as MCP tools, or letting Hermes/another app call WhatsApp like a backend API. Prefer a dedicated business/bot number rather than a personal account for either approach.

For CRM/agent assistants, start with Hermes' built-in WhatsApp as the **broker/operator interface** before building a production WhatsApp Business integration. Validate natural-language flows, backend API contracts, and scheduled nudges first; only then move to Cloud API/Twilio/360dialog for official multi-user production. See `references/conversational-crm-bot-rollout.md` for the recommended rollout pattern.

## Diagnosing which WhatsApp account is configured in Hermes

When the user asks "what WhatsApp account do I have configured?" or whether WhatsApp is actually connected, verify with live state instead of relying on session context:

1. `send_message action='list'` — if the WhatsApp section is empty or absent, no usable WhatsApp targets are registered in Hermes' channel directory.
2. Inspect `~/.hermes/channel_directory.json` — `platforms.whatsapp: []` means no cached WhatsApp chats/contacts, even if the bridge itself is connected.
3. Inspect `~/.hermes/gateway_state.json` — `platforms.whatsapp.state` shows connected/retrying/failed plus the latest error.
4. Check `~/.hermes/config.yaml` for the top-level `whatsapp:` section; `whatsapp: {}` means no platform-specific settings are configured.
5. Check for the Baileys linked-device session at `~/.hermes/whatsapp/session` (this is the default session path used by the built-in bridge; older notes may mention `~/.hermes/platforms/whatsapp/session`).
6. Check the bridge process and health endpoint:
   - `ps aux | grep -E 'whatsapp|bridge.js' | grep -v grep`
   - `curl -sS --max-time 5 http://127.0.0.1:3000/health`
7. Review logs with `grep -i "whatsapp\|bridge\|qr\|ready\|reconnect\|logged out\|allowlist" ~/.hermes/logs/gateway.log ~/.hermes/whatsapp/bridge.log | tail -120`.
8. Check `.env` for `WHATSAPP_ENABLED`, `WHATSAPP_MODE`, `WHATSAPP_ALLOWED_USERS`, and optional `WHATSAPP_HOME_CHANNEL`.

Interpretation:
- `gateway_state` + `/health` show `connected` + `send_message(action='list')` has no WhatsApp targets: the bridge is connected, but Hermes has no cached/default WhatsApp channel. Sending to bare `target='whatsapp'` will fail until `WHATSAPP_HOME_CHANNEL`/home channel is set or a channel is registered.
- Logs with `allowlist_mismatch` mean the bridge is connected but inbound messages from that number are ignored. Add the exact normalized number shown in the log to `WHATSAPP_ALLOWED_USERS` and restart the gateway.
- Logs with `Logged out. Delete session and restart to re-authenticate.` mean the linked-device session is invalid; re-pair with `hermes whatsapp`, then restart the gateway.

## Group messaging and capture workflows

### Sending to a WhatsApp group
Hermes/Baileys can send to a group when the connected WhatsApp account is already a member and you know the internal group JID (`...@g.us`). Do not send from an invite link alone; first resolve or join the group and verify metadata.

1. Discover candidate group JIDs from logs/channel directory:
```bash
python3 - <<'PY'
import re
from pathlib import Path
text=''
for p in [Path('~/.hermes/whatsapp/bridge.log').expanduser(), Path('~/.hermes/logs/gateway.log').expanduser(), Path('~/.hermes/channel_directory.json').expanduser()]:
    if p.exists(): text += '\n' + p.read_text(errors='ignore')
for g in sorted(set(re.findall(r'([0-9]{5,}(?:-[0-9]+)?@g\.us)', text))): print(g)
PY
```
2. Verify the group name/metadata:
```bash
curl -sS --max-time 5 "http://127.0.0.1:3000/chat/<GROUP_JID_URL_ENCODED>"
```
3. Send only after the user confirms the exact group/message:
```bash
curl -sS --max-time 15 -X POST http://127.0.0.1:3000/send \
  -H 'Content-Type: application/json' \
  -d '{"chatId":"EXAMPLE_ID@EXAMPLE_DOMAIN","message":"Mensaje de ejemplo autorizado"}'
```

### Capturing new group messages to JSONL for later analysis
Avoid polling `GET /messages` from a separate script for capture: that endpoint drains `messageQueue` and competes with the Hermes gateway. Preferred pattern is to modify/extend the bridge to append a copy of each incoming `event` to a JSONL file before `messageQueue.push(event)`, gated by env vars such as:

```bash
WHATSAPP_CAPTURE_GROUPS=EXAMPLE_ID@EXAMPLE_DOMAIN
WHATSAPP_CAPTURE_JSONL=/Users/USERNAME/.hermes/whatsapp/captures/example-group.jsonl
```

Implementation sketch in `scripts/whatsapp-bridge/bridge.js`:
- import `appendFileSync` from `fs`
- parse `CAPTURE_JSONL` and comma-separated `CAPTURE_GROUPS`
- build the normalized incoming `event` first
- append captures immediately after building `event`, before the allowlist `continue` and before `messageQueue.push(event)`, with `JSON.stringify({ capturedAt: new Date().toISOString(), ...event }) + '\n'` when the chat ID matches
- keep the allowlist gate after capture but before `messageQueue.push(event)` so monitored group members are archived without letting every sender talk to Hermes
- run `node --check bridge.js`, then restart the gateway so the bridge sees new env vars and code changes

For analysis, convert JSONL to JSON and derive summaries with a small Python script that reads each line, emits a JSON array, and computes sender/keyword counts.

See `references/group-capture-allowlist-ordering.md` for the session-derived debugging pattern when capture env vars are present but the JSONL file never appears.

## Pitfalls & Troubleshooting
- **Group replies still respect the allowlist**: when the user asks whether Hermes will answer newly added people in a WhatsApp group, explain that Hermes only responds to senders whose normalized phone/JID is allowed. Being in the same group is not enough. Add the new participant(s) to `WHATSAPP_ALLOWED_USERS` using the exact normalized ID seen in logs, then restart the gateway. For Mexico mobile numbers, include/check the common `521` + 10 digits form (for example `+52 55 0000 0000` → `REDACTED_LOCAL_VALUE@s.whatsapp.net`, or allowlist value `REDACTED_LOCAL_VALUE`).
- **Do not assume WhatsApp is connected from platform context alone**: verify `send_message action='list'`, `gateway_state.json`, bridge `/health`, and the session directory before answering account/status questions.
- **Connected bridge but no Hermes targets**: `gateway_state` and `/health` can say connected while `send_message(action='list')` has no WhatsApp entries. Bare `target='whatsapp'` then fails with `No home channel set`; set `WHATSAPP_HOME_CHANNEL` or use/directly register a specific chat ID.
- **Named target listed but `send_message` still says no home channel**: after manually adding a contact to `~/.hermes/channel_directory.json`, `send_message action='list'` may display the target while sending to `whatsapp:<name>` or `whatsapp:<jid>` still routes through home-channel resolution and fails. Use direct bridge `POST /send` or `POST /send-media` with the exact JID to complete the send, then verify the `success:true` response and `messageId`.
- **Bridge `success:true` is not proof of correct recipient**: Direct `POST /send` or `/send-media` can return a message ID for a valid-looking JID even if it was not the user's intended phone. Verify the intended JID from bridge logs/session data and, for Mexico mobile numbers, prefer `521` + 10 digits (example `+52 55 0000 0000` → `EXAMPLE_ID@EXAMPLE_DOMAIN`).
- **No WhatsApp target found**: Ensure WhatsApp is connected (check session context and live files). If not, link your WhatsApp account via `hermes whatsapp` and restart the gateway.
- **Allowlist mismatch**: Logs like `{"event":"ignored","reason":"allowlist_mismatch","chatId":"521...@s.whatsapp.net"}` mean inbound messages are being ignored. Add the exact normalized number (without suffix, e.g. `521...`) to `WHATSAPP_ALLOWED_USERS` and restart the gateway.
- **Group capture configured but JSONL never appears**: verify the running bridge process environment with `ps eww -p <pid> | tr ' ' '\n' | grep '^WHATSAPP_'`. If `WHATSAPP_CAPTURE_GROUPS`/`WHATSAPP_CAPTURE_JSONL` are present and the bridge code has capture support, inspect ordering: capture must happen before the allowlist `continue`. Otherwise group messages from non-allowlisted members are dropped before the append runs.
- **Logged out/device removed**: Logs saying `device_removed` or `Logged out. Delete session and restart to re-authenticate` mean the WhatsApp linked-device session is invalid; re-pair before troubleshooting message delivery.
- **Message not delivered**: Verify the target format. Use `send_message action='list'` to double-check the chat ID, then confirm the bridge with `curl http://127.0.0.1:3000/health`.
- **Media not sending**: Provide an absolute path to a file that Hermes can read. Use `write_file`/`read_file` to test file accessibility.
- **Rate limits**: WhatsApp may throttle bulk messages. Space out automated messages or use lower frequency.

## Verification
After sending a message, you should see:
- A success response from `send_message` containing `platform: "whatsapp"` and a `message_id`.
- The message appear in your WhatsApp chat (if you have the client open) or in the Hermes conversation log.
If you do not see the message, ensure the gateway is running (`hermes gateway`) and that the WhatsApp platform is still connected.

## Related tools
- `send_message` – primary tool for WhatsApp messaging.
- `session_search` – search past WhatsApp conversations.
- `cronjob` – schedule recurring WhatsApp notifications.
- `memory` – store preferences like default WhatsApp contact ID.

## References

- `references/group-capture-jsonl.md` — group JID discovery, safe group sending, and JSONL capture pattern that does not steal messages from the gateway.
- `references/group-capture-allowlist-ordering.md` — debugging checklist for group capture env vars present but no JSONL output because allowlist gating runs before capture.
- `references/macos-media-drive-backup.md` — resumable, chunked and checksum-verified WhatsApp media backup to Drive, including safe deletion and final verification.

## Extending this skill
If you have a custom WhatsApp CLI (e.g., `yowsup`, `whatsmeow`), you can wrap its commands in a `terminal` call within this skill and expose higher‑level actions (e.g., `whatsapp-send-template`). Add those as additional sections.