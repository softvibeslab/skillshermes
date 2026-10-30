---
name: telegram-bot-operations
description: Set up, verify, secure, and troubleshoot Telegram bots used by agents or services. Use for bot tokens, polling/webhooks, allowlists, chat initiation, delivery tests, and credential rotation.
---

# Telegram Bot Operations

Operate Telegram bots with the smallest secure workflow that proves end-to-end delivery.

## Setup

1. Identify the exact bot account and expected username; never infer identity from a token.
2. Store the token in the service's secret store or local environment file. Never print, quote, summarize, or commit it.
3. Restrict inbound access with explicit Telegram user IDs when the host supports allowlists.
4. Configure exactly one update transport: polling or webhook.
5. Start/restart the owning service and inspect its own health/status output.

## Verification ladder

Stop at the first failing rung and fix that layer:

1. **Identity:** call Bot API `getMe`; confirm `ok`, bot ID, and username.
2. **Transport:** confirm polling is active or webhook status is healthy; avoid two consumers using the same token.
3. **Conversation bootstrap:** the human must open the bot and send `/start` before the bot can initiate a private chat.
4. **Authorization:** confirm the sender's numeric Telegram user ID is in the service allowlist.
5. **Delivery:** call `sendMessage` to the intended chat and inspect the JSON response body, including on HTTP errors.
6. **Agent response:** send a real user message through Telegram and verify the service processes and replies to it.

Bot API identity success is not end-to-end success. A connected gateway can still lack a private chat, reject the user by allowlist, or have a competing poller.

## Common failure interpretation

- `400 Bad Request: chat not found`: verify the numeric chat ID, then have the user open the bot and send `/start`; retry delivery afterward.
- `401 Unauthorized`: token is invalid, revoked, malformed, or belongs to a different bot.
- `403 Forbidden: bot was blocked by the user`: the user must unblock the bot before retrying.
- `409 Conflict`: another poller is consuming updates, or polling conflicts with an active webhook.

Read `references/telegram-bot-operations-private-chat-bootstrap.md` for the private-chat initiation probe and safe response handling.

For named Hermes profiles, read `references/telegram-bot-operations-hermes-profile-allowlists.md` before changing access. Hermes can source the allowlist from both profile YAML and `TELEGRAM_ALLOWED_USERS`; preserve existing IDs, update the effective source, restart, and test the newly added chat.

## Secret exposure response

If a token appears in chat, logs, terminal history, screenshots, or a committed file:

1. Treat it as compromised even if the audience seems private.
2. Revoke/regenerate it with BotFather.
3. Replace it in the local secret source without repeating it in conversation.
4. Restart the service.
5. Re-run identity and end-to-end delivery checks.
6. Search relevant logs/history for accidental copies and redact where feasible.

Do not postpone rotation merely because the bot currently works.

## Safety and reporting

- Report bot username, profile/service name, transport, allowlist status, and test result; omit token fragments.
- Never include credentials in commands that will be echoed into shared logs when a safer environment-file or prompt mechanism exists.
- Do not claim the bot is operational until a real inbound message and outbound reply both succeed.
- If `/start` is still required, report the setup as configured but not yet end-to-end verified.
