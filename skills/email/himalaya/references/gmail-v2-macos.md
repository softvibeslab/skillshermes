# Gmail + Himalaya v2.1 on macOS

Use this when configuring Gmail with Himalaya v2 on macOS.

## Known-good account block

```toml
[accounts.gmail]
default = true
email = "user@example.com"
display-name = "Your Name"

imap.server = "imaps://imap.gmail.com:993"
imap.sasl.plain.username = "user@example.com"
imap.sasl.plain.password.command = ["security", "find-generic-password", "-a", "user@example.com", "-s", "himalaya-gmail", "-w"]

smtp.server = "smtps://smtp.gmail.com:465"
smtp.sasl.plain.username = "user@example.com"
smtp.sasl.plain.password.command = ["security", "find-generic-password", "-a", "user@example.com", "-s", "himalaya-gmail", "-w"]
```

Keep `display-name` inside the account block.

## Safe credential flow

1. Enable Google 2-Step Verification.
2. Create a Google App Password; normal Gmail passwords are rejected.
3. Never ask the user to paste it into chat or pass it as a command argument.
4. Let the user enter it directly into a local prompt:

```bash
security add-generic-password -U -a user@example.com -s himalaya-gmail -w
```

If a password is pasted into chat, do not use it. Tell the user to revoke it, generate a fresh one, and enter the replacement only in the local prompt.

## Validate

```bash
himalaya account list --json
himalaya account check --json
```

Both IMAP and SMTP must report `ok: true`.

## Localized Gmail folders

Do not assume English names such as `[Gmail]/Sent Mail`. Discover the live names first:

```bash
himalaya mailbox list --json
```

Then map aliases to the exact returned IDs. Example for Spanish Gmail:

```toml
mailbox.alias.inbox = "INBOX"
mailbox.alias.sent = "[Gmail]/Enviados"
mailbox.alias.drafts = "[Gmail]/Borradores"
mailbox.alias.trash = "[Gmail]/Papelera"
mailbox.alias.archive = "[Gmail]/Todos"
```

Verify alias resolution read-only:

```bash
himalaya envelope list --mailbox sent --page-size 1 --json
himalaya envelope list --mailbox drafts --page-size 1 --json
himalaya envelope list --mailbox trash --page-size 1 --json
```

Himalaya v2.1 uses `--mailbox`, not `--folder`, and `--json`, not `--output json`.

## Send test

Gmail automatically stores SMTP mail in Sent, so do not also pass `--save sent` or a duplicate may be created.

```bash
himalaya message compose \
  --to user@example.com \
  --subject "Himalaya test" \
  --body "Himalaya IMAP and SMTP are configured." \
  --send --json
```

Confirm it appears in Sent with `himalaya envelope list --mailbox sent --page-size 3 --json`.
