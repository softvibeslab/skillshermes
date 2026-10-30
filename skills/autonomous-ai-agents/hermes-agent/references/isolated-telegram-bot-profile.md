# Isolated Telegram bot profile pattern

Use this when el operador wants a new Telegram bot connected to Hermes without disturbing the currently running default gateway.

## Known-good workflow

1. Inspect current profiles and gateway state:

```bash
which hermes
hermes --version
hermes profile list
```

2. Create an isolated profile by cloning the working default profile:

```bash
hermes profile create rovi-flow-bot --clone-all
```

This creates:

- profile directory: `~/.hermes/profiles/rovi-flow-bot`
- wrapper alias: `~/.local/bin/rovi-flow-bot`

3. Immediately neutralize cloned messaging credentials before starting the profile gateway. At minimum:

```env
TELEGRAM_BOT_TOKEN=
TELEGRAM_ALLOWED_USERS=<roger_telegram_user_id>
TELEGRAM_HOME_CHANNEL=<roger_telegram_user_id>
TELEGRAM_HOME_CHANNEL_NAME=el operador GV - ROVI Flow Bot
```

Also blank non-target platform credentials copied from default, especially:

- `DISCORD_*`
- `WHATSAPP_*`
- `SLACK_*`
- any other cloned bot tokens/webhook secrets

This prevents duplicate bot connections from the isolated gateway.

4. Put the new BotFather token only in the isolated profile env:

```bash
nano ~/.hermes/profiles/rovi-flow-bot/.env
# TELEGRAM_BOT_TOKEN=<new token from @BotFather>
```

5. Start only the isolated profile gateway:

```bash
rovi-flow-bot gateway start
```

6. Verify:

```bash
rovi-flow-bot gateway status
hermes profile list
```

7. Open the new Telegram bot and send `/start`.

## Product app pattern: provision one Hermes profile per end user/channel

Use this when a CRM/control-tower app needs to let an admin choose Telegram or WhatsApp for a user and generate isolated Hermes instructions automatically.

- Keep **role/orchestrator prompts** separate from **specialist prompts** in product data models:
  - role/orchestrator = system prompt, usually derived from the user's business role or selected orchestrator
  - specialists = user prompt fragments/capabilities the orchestrator can blend in
- On channel selection, generate a deterministic profile slug, e.g. `rovi-user-<email-or-name>`; write a profile spec JSON next to the generated env so it is auditable.
- Suggested generated files before copying into `~/.hermes/profiles/<profile>/`:
  - `rovi_user_profile.json`: user id, membership tier, role agents, specialist agents, enabled skills, channel, link code, orchestration mode
  - `.env`: platform-specific credentials/allowlists only for this user/channel
  - `SETUP.md`: exact copy/start/QR or `/start` steps shown back in the product UI
- Telegram flow:
  - collect the user's BotFather token in the product UI or secure admin flow
  - set only `TELEGRAM_BOT_TOKEN`, `TELEGRAM_ALLOWED_USERS`, `TELEGRAM_HOME_CHANNEL`, and `TELEGRAM_HOME_CHANNEL_NAME` for that profile
  - blank `WHATSAPP_*`, `DISCORD_*`, `SLACK_*` and non-target tokens
  - start with `<profile-alias> gateway start`, then have the user send `/start`
- WhatsApp flow:
  - set `WHATSAPP_ALLOWED_USERS` and a profile-local `WHATSAPP_SESSION_PATH`
  - blank Telegram/Discord/Slack tokens
  - start with `<profile-alias> gateway start`, then scan the QR shown by gateway logs/status
- Product UI should surface the profile name, local path, profile status, and setup steps. Do not claim a platform is linked until the gateway is actually started and Telegram `/start` or WhatsApp QR scan succeeds.

## Public tunnel pitfall while testing profile/control-tower UIs

If a temporary `localhost.run` URL returns `no tunnel here`, the app may still be healthy locally; the anonymous SSH tunnel died or rotated. Verify in this order before debugging the app:

```bash
curl -s http://localhost:<port>/api/health
curl -I http://localhost:<port>/<route>
ssh -o StrictHostKeyChecking=no -o ServerAliveInterval=15 -o ServerAliveCountMax=3 -o ExitOnForwardFailure=yes -R 80:localhost:<port> nokey@localhost.run
# Use only the URL printed with "tunneled with tls termination", then verify:
curl -s https://<new-host>/api/health
curl -I https://<new-host>/<route>
```

For demos that must remain stable, prefer an authenticated tunnel/domain (localhost.run account/custom domain, Cloudflare Tunnel, or ngrok) over anonymous localhost.run.

## Pitfalls

- `--clone-all` copies existing `.env` secrets. Do not start the cloned gateway until old Telegram/Discord/WhatsApp tokens are blanked or replaced.
- If `TELEGRAM_BOT_TOKEN` remains copied from default, both profiles can compete for the same bot updates.
- For per-user product provisioning, do not store or reuse one global Telegram/WhatsApp credential across all users; every generated profile should have its own env and allowlist/session path.
- Keep the default gateway running separately; profile gateway status should show default running and the new profile stopped until the new BotFather token is ready.
- Store setup notes inside the profile directory, e.g. `~/.hermes/profiles/rovi-flow-bot/ROVI_FLOW_BOT_SETUP.md`.

## el operador's current ROVI profile

As of 2026-05-22:

- profile: `rovi-flow-bot`
- path: `/Users/USERNAME/.hermes/profiles/rovi-flow-bot`
- alias: `rovi-flow-bot`
- setup note: `/Users/USERNAME/.hermes/profiles/rovi-flow-bot/ROVI_FLOW_BOT_SETUP.md`
- token state: `TELEGRAM_BOT_TOKEN` intentionally empty pending new BotFather token
