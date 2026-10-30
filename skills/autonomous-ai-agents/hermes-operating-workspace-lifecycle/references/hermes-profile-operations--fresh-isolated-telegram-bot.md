# Fresh isolated Telegram profile: known-good sequence

Use when creating a new Hermes profile around a newly supplied BotFather token without cloning existing gateway secrets.

## Sequence

1. Create a fresh profile rather than `--clone-all`:

```bash
hermes profile create <profile> --description "<role>"
```

A fresh profile may not have `config.yaml` or `.env` until the first setting/write; do not assume those files exist immediately.

2. Apply only required config:

```bash
hermes --profile <profile> config set model.provider <provider>
hermes --profile <profile> config set model.default <model>
hermes --profile <profile> config set terminal.cwd /absolute/project/path
hermes --profile <profile> config set security.redact_secrets true
hermes --profile <profile> config set privacy.redact_pii true
```

3. Write `.env` with mode `0600` and only the target bot values:

```dotenv
TELEGRAM_BOT_TOKEN=REPLACE_WITH_BOTFATHER_TOKEN
TELEGRAM_ALLOWED_USERS=REPLACE_WITH_TELEGRAM_USER_ID
TELEGRAM_HOME_CHANNEL=REPLACE_WITH_TELEGRAM_CHAT_ID
```

Never print the token during verification. If it was pasted into a durable chat/log, finish setup if requested but tell the user to rotate it with BotFather `/revoke` and replace the stored value.

4. Use the structured Telegram config shape. A scalar `home_channel` causes startup failure (`TypeError: 'int' object is not subscriptable`):

```yaml
platforms:
  telegram:
    enabled: true
    home_channel:
      platform: telegram
      chat_id: '<chat-id>'
      name: '<display name>'
    extra:
      allowed_users:
        - <user-id>
      bot_username: <username-without-@>
```

Do not store `allowed_users` as a quoted JSON-looking string such as `'[123]'`.

5. Verify the token through Telegram `getMe`, returning only `ok`, bot ID, username, and display name.

6. Verify model auth separately before starting the gateway:

```bash
hermes --profile <profile> chat -q 'Responde únicamente: OK' -Q
```

7. Customize `SOUL.md`, then install/start the gateway:

```bash
hermes --profile <profile> gateway install
hermes --profile <profile> gateway start
hermes --profile <profile> gateway status
```

8. Verify success from all three signals:

- gateway status has a live PID;
- log contains `Connected to Telegram (polling mode)`;
- log contains `Gateway running with 1 platform(s)`.

On macOS launchd, `LastExitStatus` may describe the prior terminated/restarted process even while the new PID is healthy. Prefer current PID plus fresh connection logs over that field alone.

## Failure path

If startup fails, inspect both profile-local files before retrying:

```text
~/.hermes/profiles/<profile>/logs/gateway.error.log
~/.hermes/profiles/<profile>/logs/gateway.log
```

Correct config, restart once, and verify fresh log timestamps. Do not declare success merely because service installation succeeded.
