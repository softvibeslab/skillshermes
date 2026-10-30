# Telegram profile clone checklist

Use after creating a Hermes profile for Telegram from another profile, especially with `--clone-all`.

## Fast checks

1. Does the target profile exist?
2. Is it the active profile?
3. Is the target profile gateway running?
4. Did the profile inherit the source `.env`?
5. Is `TELEGRAM_BOT_TOKEN` shared with the source profile?
6. Does `TELEGRAM_ALLOWED_USERS` include the intended operator(s)?
7. Does `TELEGRAM_HOME_CHANNEL` still point to the source chat/group?

## Interpretation

- **Gateway stopped** → profile will not answer even if activation succeeded.
- **Shared bot token** → same Telegram bot identity, different Hermes profile/context.
- **Different bot token** → separate Telegram bot identity.
- **Wrong home channel** → notifications, shutdown notices, or proactive messages may go to the wrong chat.

## Known-good recovery sequence

1. `hermes profile use <target>`
2. `<target> gateway status`
3. If stopped: `<target> gateway start`
4. Re-check status
5. Inspect target `.env` for token/allowlist/home-channel values
6. Tell the user explicitly whether this is a shared bot or a separate bot
