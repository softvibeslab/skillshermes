# Secure local Telegram token handoff for a Hermes profile

Use when a dedicated Hermes profile is ready but the user has not securely supplied a new BotFather token. The goal is to finish every non-secret step, then let the user enter the token locally without placing it in chat, shell history, process arguments, logs, or diffs.

## Pre-token preparation

1. Create or clone the profile, but do not start its gateway.
2. If cloning, immediately remove inherited messaging variables for every non-target platform, not only Telegram. Common prefixes include `TELEGRAM_`, `DISCORD_`, `SLACK_`, `WHATSAPP_`, `SIGNAL_`, and `MATRIX_`.
3. Audit inherited config, webhooks, and cron jobs before any gateway command.
4. Install the specialized identity into `SOUL.md` and verify it with a one-shot `chat -q` smoke test.
5. Set the intended numeric Telegram allowlist in structured YAML and verify its parsed type. Keep the environment allowlist synchronized later.

## Local bootstrap script pattern

Create a small profile-specific Python script outside secret-bearing profile files. It should:

1. Read the token with `getpass.getpass()` so it is hidden and absent from shell history.
2. Validate only the token shape; never print the token.
3. Call Telegram `getMe` from inside Python rather than putting the token in a `curl` command line.
4. Call `getWebhookInfo`; if a webhook URL already exists, stop rather than hijacking a bot used elsewhere.
5. Atomically upsert these values into the profile-local `.env`:
   - `TELEGRAM_BOT_TOKEN`
   - `TELEGRAM_ALLOWED_USERS`
   - `TELEGRAM_HOME_CHANNEL`
   - `TELEGRAM_HOME_CHANNEL_NAME`
   - `TELEGRAM_BOT_USERNAME`
6. Write through a temporary file, apply mode `0600`, then `os.replace()` it.
7. Install/start the target profile gateway and print only the bot username plus redacted status.
8. Give the user the `https://t.me/<username>` link and require `/start` before outbound-delivery verification.

## Minimal verification gates

- `getMe.ok` is true and the returned username matches the intended bot.
- `getWebhookInfo.result.url` is empty when Hermes will use long polling.
- No inherited messaging credentials remain for unused platforms.
- `.env` mode is `0600`.
- Target gateway has a current PID and fresh Telegram connection logs.
- The user pressed Start and the bot produced one real inbound reply.

## Content-specialist profile design correction

When specializing a profile around videos, audios, or texts, first distinguish the requested analytical object:

- **Meaning/content:** thesis, argument, assumptions, worldview, evidence status, implications, and competing interpretations.
- **Production/media:** editing, visuals, audio, persuasion mechanics, distribution, and likely AI assistance.

If the user says they care about “lo que transmite”, encode the first mode in `SOUL.md` and explicitly make production analysis opt-in. Do not turn a conceptual interpreter into a video-forensics profile merely because the input happens to be a video.
