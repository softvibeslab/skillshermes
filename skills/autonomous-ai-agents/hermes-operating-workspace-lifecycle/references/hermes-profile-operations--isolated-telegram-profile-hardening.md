# Isolated Telegram Profile Hardening

Use after cloning a Hermes profile for a dedicated Telegram bot.

## Minimum safe sequence

1. Write the new `TELEGRAM_BOT_TOKEN` into the target profile `.env` without echoing it back.
2. Verify the token with Telegram `getMe`; redact the token in all output.
3. Set/confirm `TELEGRAM_ALLOWED_USERS` and, if known, `TELEGRAM_HOME_CHANNEL`.
4. Blank unrelated cloned platform secrets, especially Discord/Slack tokens, set `WHATSAPP_ENABLED=false`, and disable every non-target platform in `config.yaml`.
5. Disable unused cloned webhook config:

```yaml
platforms:
  webhook:
    enabled: false
```

6. Audit inherited scheduled jobs **before starting the gateway**. `--clone-all` copies cron state; pause or remove jobs belonging to the source profile so the new bot does not run or deliver unrelated automations.
7. Set the project workspace (`terminal.cwd`) and add profile-local `SOUL.md` plus workspace `AGENTS.md` when the bot is meant to operate one project tree.
8. Start or restart the target gateway.
9. Verify profile-specific logs, not only service status:
   - `Active profile: <target>`
   - `Connected to Telegram (polling mode)`
   - `✓ telegram connected`
   - `Gateway running with 1 platform(s)` for Telegram-only profiles
10. Because cloned logs contain source-profile history, inspect only fresh lines after the target profile's current startup marker. Do not infer current platform state from earlier copied log entries.
11. Test outbound delivery. A new bot cannot initiate a DM until the user opens `https://t.me/<username>` and presses **Start**; Telegram's `Bad Request: chat not found` means the gateway may be healthy but the user has not initiated the chat. Give that one manual step, then retest.

## Common cloned-profile failure

A profile cloned with `--clone-all` may inherit `platforms.webhook.enabled: true` on default port `8644`. If another Hermes profile already owns that port, the new gateway may run Telegram but keep retrying webhook reconnects.

Lazy fix for Telegram-only profiles: disable webhook in the cloned profile config. Do not hunt the port owner unless webhooks are actually needed.

## Token safety

If the user pasted a bot token into chat, configure it, but mention that rotating it in BotFather is the clean security follow-up if they care about exposure.