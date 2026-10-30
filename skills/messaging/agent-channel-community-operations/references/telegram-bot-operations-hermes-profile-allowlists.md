# Hermes profile Telegram allowlists

Use this when a Telegram bot is attached to a named Hermes profile and one authorized user gets no reply.

## Effective configuration check

Hermes may receive the allowlist from both:

- profile `config.yaml`: normally `platforms.telegram.allowed_users` (inspect the live schema/config before assuming a legacy nesting);
- profile `.env`: `TELEGRAM_ALLOWED_USERS`.

The environment value can remain effective even after `config.yaml` is changed. Updating only one source can therefore leave the user unauthorized.

## New-profile bootstrap

1. Clone/create the profile, then remove inherited messaging variables (`TELEGRAM_*`, `DISCORD_*`, `WHATSAPP_*`, etc.) before starting its gateway. A cloned agent must never come up on another agent's bot.
2. Do not derive an authorized user ID from a bot token. The digits before `:` identify the bot, not the human who may message it.
3. Obtain the intended human's numeric Telegram user ID explicitly or from a verified inbound update; never hardcode an ID copied from another profile.
4. If the token was pasted into chat, logs, or shell history, do not install it. Revoke it in BotFather and collect the replacement through a hidden local prompt (`getpass`) or an approved secret store.
5. Keep the gateway stopped until token, bot identity, and allowlist are all verified.

## Safe add-user procedure

1. Resolve the profile config paths with `hermes -p <profile> config path` and `hermes -p <profile> config env-path`.
2. Read only the non-secret allowlist value from `.env`; never dump the entire file because it also contains the bot token.
3. Preserve all existing IDs and append the new numeric ID exactly once.
4. Keep formats compatible with their source:
   - `.env`: `TELEGRAM_ALLOWED_USERS=00000000000,00000000000`
   - YAML: `platforms.telegram.allowed_users: [00000000000, 00000000000]` (use the shape accepted by the profile's current config schema).
5. Run `hermes -p <profile> config check`.
6. Restart the profile gateway.
7. Verify with Bot API `sendMessage` to the newly added chat. A successful JSON response proves bot-to-chat delivery; then send a real user message to prove inbound agent handling.

## Pitfalls

- `hermes config get` is not a supported subcommand. Use `config path`, `config show`, `config set`, or inspect the resolved file narrowly.
- Bot ID, chat ID, and user ID are different identities even when private-chat IDs often equal user IDs.
- Do not replace the whole allowlist when adding one user.
- Do not print or read the complete `.env`; extract only `TELEGRAM_ALLOWED_USERS`.
- A setup script must request or accept the allowlist explicitly; a fixed `USER_ID` silently authorizes the wrong person when reused.
- Gateway status plus `getMe` is not enough. Test the newly authorized chat specifically.
