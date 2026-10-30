# Private chat bootstrap and delivery probe

Telegram bots cannot initiate a private conversation with a person who has never opened the bot and interacted with it.

## Minimal sequence

1. Verify identity with `getMe`.
2. Ask the user to open `https://t.me/<bot_username>` and send `/start`.
3. Confirm the numeric target is the private chat/user ID expected by the service.
4. Retry `sendMessage`.
5. Send a normal user message to verify the inbound agent path and allowlist—not only the raw Bot API.

## Interpret the response body

When `sendMessage` returns HTTP 400, inspect Telegram's JSON body rather than reporting only the status code. For example:

```json
{"ok":false,"error_code":400,"description":"Bad Request: chat not found"}
```

That response usually means one of two things:

- the bot has no private chat with that user yet, so the user must send `/start`; or
- the supplied numeric chat ID is wrong.

It does **not** prove the gateway or token is broken when `getMe` and the gateway transport are otherwise healthy.

## Completion criterion

Configured:
- valid bot identity
- service running
- transport active
- allowlist present

End-to-end verified:
- user has initiated the chat
- inbound message reaches the service
- service sends a successful reply

Keep these states distinct in user-facing reports.

## Security note

If the token was pasted into any conversation while diagnosing this flow, rotate it after configuration and rerun the complete verification ladder. Never preserve the token in this reference or in task summaries.
