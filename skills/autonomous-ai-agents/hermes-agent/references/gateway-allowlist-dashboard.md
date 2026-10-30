# Gateway allowlist dashboard pattern

Session learning: a lightweight local dashboard is useful for CRUD management of Telegram and WhatsApp allowlists without manually editing `~/.hermes/config.yaml` and `~/.hermes/.env`.

Known-good MVP shape:
- Local-only HTTP server bound to `127.0.0.1`.
- Token-gated URL, token stored under the app directory.
- Read/write Telegram allowlist from both:
  - `~/.hermes/config.yaml` → `platforms.telegram.allowed_users`
  - `~/.hermes/.env` → `TELEGRAM_ALLOWED_USERS`
- Read/write WhatsApp allowlist from:
  - `~/.hermes/.env` → `WHATSAPP_ALLOWED_USERS`
- Create backups before every file write.
- Provide `POST /api/restart-gateway` that runs `hermes gateway restart` after edits.
- Provide status endpoint combining `~/.hermes/gateway_state.json`, process list, and WhatsApp bridge `/health`.
- Mine recent identities from `~/.hermes/channel_directory.json`, `~/.hermes/logs/gateway.log`, and `~/.hermes/whatsapp/bridge.log` so users can click “add from recent”.

Implemented locally for el operador at:
- `/Users/USERNAME/.hermes/admin-dashboard/server.py`
- `http://127.0.0.1:8787/?token=<contents of /Users/USERNAME/.hermes/admin-dashboard/.admin_token>`

Important pitfalls:
- `send_message target='whatsapp'` fails unless a WhatsApp home channel is configured. The bridge can still send directly via `POST http://127.0.0.1:3000/send` when connected.
- WhatsApp bridge may return `success:true` for a JID even if it was not the intended recipient. Verify the JID format from logs/session data.
- Mexico WhatsApp mobile numbers often need `521` + 10-digit number for direct JIDs, e.g. `+52 55 0000 0000` → `EXAMPLE_ID@EXAMPLE_DOMAIN`.
- Allowlist changes require gateway restart before inbound messages are accepted.
- For WhatsApp bot mode, `allowlist_mismatch` in `~/.hermes/whatsapp/bridge.log` means messages are received but ignored because `WHATSAPP_ALLOWED_USERS` does not include the sender.

Verification commands:
```bash
TOKEN=$(cat ~/.hermes/admin-dashboard/.admin_token)
curl -sS -H "X-Admin-Token: $TOKEN" http://127.0.0.1:8787/api/status
curl -sS -H "X-Admin-Token: $TOKEN" http://127.0.0.1:8787/api/allowlist
curl -sS http://127.0.0.1:3000/health
```
