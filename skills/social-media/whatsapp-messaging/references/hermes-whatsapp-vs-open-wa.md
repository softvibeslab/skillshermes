# Hermes WhatsApp vs Open-WA MCP

## Decision guide

Use **Hermes built-in WhatsApp** when WhatsApp is primarily a messaging channel for the agent:
- Users message the bot number and get Hermes responses.
- Hermes can use its normal tools, memory, media handling, voice transcription, and platform formatting.
- Setup is via `hermes whatsapp` and the Baileys linked-device bridge.

Use **Open-WA / Easy API / MCP** when WhatsApp is infrastructure for another system:
- CRM lead capture and follow-up workflows.
- Programmatic send/read/search/contact/group/media operations.
- Webhooks into a backend.
- Exposing WhatsApp methods as MCP tools to Hermes or another agent.

## Open-WA notes from repo review

The main repo is `open-wa/wa-automate-nodejs`.

Useful modes:
- Easy API: `npx @open-wa/wa-automate --port 8080 --api-key "..."`
- MCP: `npx @open-wa/wa-automate --port 8080 --api-key "..." --mcp`
- MCP endpoint: `http://localhost:8080/mcp`
- Dashboard: `http://localhost:8080/dashboard/mcp`
- API docs: `http://localhost:8080/api-docs/`

Hermes MCP config example:

```yaml
mcp_servers:
  open_wa:
    url: "http://localhost:8080/mcp"
    headers:
      X-API-Key: "your-secure-key"
    timeout: 120
    connect_timeout: 60
```

Important caveats:
- Open-WA is unofficial and not affiliated with WhatsApp/Meta.
- Prefer a dedicated business/bot number.
- Open-WA v5 README says v5 is alpha; stable production users may need v4.76.0, but the MCP surface is documented in the newer line.
- `localhost` only works if Hermes and Open-WA run on the same machine. For remote Hermes, expose the service securely (Cloudflare Tunnel/ngrok/Tailscale/reverse proxy) and keep API-key auth enabled.

## Status/account verification checklist for Hermes WhatsApp

- `send_message action='list'`: should show WhatsApp targets if connected and known.
- `~/.hermes/channel_directory.json`: `platforms.whatsapp` should contain chats/contacts; `[]` means no registered targets.
- `~/.hermes/gateway_state.json`: check `platforms.whatsapp.state` and error message.
- `~/.hermes/config.yaml`: top-level `whatsapp: {}` means no platform-specific behavior is set.
- `~/.hermes/platforms/whatsapp/session`: should exist after pairing; missing means no saved linked-device credentials.
- Logs: `grep -i "whatsapp\|bridge\|qr\|ready\|reconnect" ~/.hermes/logs/gateway.log | tail -80`.
