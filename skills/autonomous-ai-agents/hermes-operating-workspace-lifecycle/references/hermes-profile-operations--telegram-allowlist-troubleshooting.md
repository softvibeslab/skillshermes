# Telegram allowlist troubleshooting

Use when a Hermes profile's Telegram gateway is connected but a specific person cannot use the bot, or when an operator asks to add a Telegram user ID.

## Symptom

- `gateway status` shows the profile gateway loaded/running.
- Logs show Telegram connected, often polling mode.
- The user sends `/start` or a message and gets no response.
- Gateway log may contain:

```text
Unauthorized user: <telegram_id> (<display_name>) on telegram
```

## Root cause

Telegram transport is healthy. Hermes is rejecting that sender because their numeric Telegram user ID is absent from one or both profile allowlists.

## Fix

1. Inspect only the allowlist values; never dump the whole `.env`.
2. Add `<telegram_id>` to the target profile `.env`:
   - `TELEGRAM_ALLOWED_USERS=<existing_ids>,<telegram_id>`
3. Add the same numeric ID to `config.yaml`:
   - current profile shape: `platforms.telegram.extra.allowed_users`
   - legacy profile shape, if already present: `platforms.telegram.allowed_users`
   Preserve the profile's existing schema rather than creating both keys.
4. Restart the target profile gateway.
5. Parse both files and assert the same ID set appears in each.
6. Verify a current gateway PID and fresh `Connected to Telegram` / `Gateway running` log lines.
7. Ask the newly allowed user to send `/start`; a bot cannot initiate a DM before that user starts it.

## Redaction-safe editing

Do not use a generic patch operation on `.env` when its diff can include adjacent secret lines such as `TELEGRAM_BOT_TOKEN`. Prefer a small script that:

- reads `.env` internally;
- replaces only `TELEGRAM_ALLOWED_USERS`;
- writes the file without printing its contents;
- prints only the resulting numeric ID set;
- preserves or tightens file permissions to `0600`.

The same rule applies to verification: print booleans, usernames, bot IDs, allowlisted user IDs, or status—not tokens.

## Explicit public access

Only when the operator explicitly requests a public bot:

1. Set `TELEGRAM_ALLOW_ALL_USERS=true` in the profile-local `.env`.
2. Remove `TELEGRAM_ALLOWED_USERS` from `.env` and `platforms.telegram.extra.allowed_users` from `config.yaml` to avoid contradictory state.
3. Restart the target profile gateway.
4. Verify the flag parses as `true`, both allowlists are absent, the PID is current, and fresh logs show Telegram connected.

Public access authorizes every sender before allowlist or pairing checks. Warn that users can consume model quota and invoke every toolset exposed to Telegram; reduce Telegram toolsets if the bot should only chat.

## Config-shape pitfall

`platforms.telegram.home_channel` must be a YAML object, not a JSON string embedded in YAML. Known-good shape:

```yaml
platforms:
  telegram:
    enabled: true
    home_channel:
      platform: telegram
      chat_id: "<telegram_id>"
      name: <label>
    extra:
      allowed_users:
        - <telegram_id>
```

An embedded JSON string can pass YAML parsing but crash gateway startup with `TypeError: string indices must be integers, not 'str'` when Hermes expects an object.

## Safety

- Never print or preserve the Telegram bot token; refer to it as `[REDACTED]`.
- If the token was pasted in chat, recommend rotating it in BotFather because chat history is durable.
- Do not make the bot public unless explicitly requested; prefer known numeric user IDs.
- `Chat not found` during a proactive send usually means the person has not opened the bot and sent `/start`; it does not by itself mean the allowlist failed.
