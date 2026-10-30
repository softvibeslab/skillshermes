# OAuth pools and duplicate consumers

## Why sign-in may not fix authentication

In a multi-credential pool, a successful sign-in can append a new OAuth entry instead of replacing older entries. If selection favors an older high-priority credential, requests can continue failing with `401`, `token_invalidated`, or refresh-token reuse errors while status still reports `logged in`.

OAuth refresh tokens may rotate or be single-use. A CLI, IDE extension, second gateway, or remote worker can consume the refresh token first and invalidate another client's copy.

## Secret-safe cleanup

Inspect only metadata:

- credential ID or label;
- priority/order;
- active marker;
- state (`ok`, `exhausted`, `invalid`, etc.);
- added/renewed timestamp;
- last failure code/time.

Never print access tokens, refresh tokens, bot tokens, authorization headers, or complete credential files. To detect reuse, compare hashes/fingerprints in-process and output only match/no-match or a short non-reversible identifier.

Remove only entries supported by evidence. Restart the gateway and run a real provider request afterward.

## Hermes command pattern

```bash
hermes -p <profile> auth status <provider>
hermes -p <profile> auth list
hermes -p <profile> auth remove <provider> <id-or-label>
hermes -p <profile> gateway restart
hermes -p <profile> chat -q 'Responde únicamente: OK' --quiet
```

Use `hermes ... --help` before relying on a remembered subcommand. Authentication stores and command shapes can change between versions.

## Missing provider token with populated pool

A gateway can report `Codex auth is missing access_token` while `auth list` still shows OAuth credentials. Inspect both stores without printing secrets:

- `providers.openai-codex.tokens`: presence booleans only;
- `providers.openai-codex.last_auth_error`: code and timestamp;
- `credential_pool.openai-codex`: IDs, labels, priority, state, last-refresh timestamp, token-presence booleans.

An empty provider token map and exhausted pool entries establish that the current selection path cannot obtain usable authentication; they do not by themselves establish why. A historical `refresh_token_reused` is supporting evidence, not proof of a new refresh failure. Do not reset exhaustion or delete the whole pool blindly. Do not copy a working profile's rotating OAuth credentials as a shortcut.

## Device-code authorization handoff

After checking live command help, initiate an independent login scoped to the affected profile:

```bash
hermes -p <profile> auth add openai-codex --type oauth --label <distinct-label> --no-browser
```

Run this interactively with a tracked background process and completion notification. Poll until the authorization URL and short-lived code appear; present them to the user, who must complete sign-in themselves. Do not store codes, tokens, or process IDs in this skill. A waiting login is a blocker, not a repaired gateway; report that distinction explicitly. If the process expires, initiate a fresh flow rather than reusing the old code.

After authorization completes, verify process success and inspect pool selection again: adding a credential may leave old higher-priority entries. Remove only proven-invalid entries, restart only the affected gateway, make a real model request, and finish with the channel probe below. No repair should be claimed solely because the browser accepted the login.

## Telegram duplicate-poller proof

Repeated long-polling errors such as:

```text
Conflict: terminated by other getUpdates request; make sure that only one bot instance is running
```

indicate another consumer of the same bot token.

Search intended local profiles, process definitions, launch agents, containers, and known remote hosts without exposing the token. If local inspection finds one intended process but the conflict persists, another machine or remote deployment is likely.

To identify who answered:

1. Send a unique test string after cleanup.
2. Record the exact timestamp.
3. Confirm the current gateway logged the inbound message and reply.
4. Inspect current error logs for a matching provider failure.
5. If the user got a reply but this gateway logged nothing, another instance produced it.

Stop or update the duplicate. Rotate the bot token only if the unknown consumer cannot be located; then update the intended gateway and restart it.

## Telegram channel ownership handoff across hosts

Long polling has exactly one owner. For a deliberate Mac/VPS or old/new-host migration:

1. Elect the destination gateway as the sole channel owner.
2. Stop the source gateway and verify the service/process is stopped; do not rely on the stop command's exit status alone.
3. Start or restart the destination gateway only after the source is down.
4. Observe fresh destination logs for a short window and confirm no new polling conflict appears.
5. Run a direct model request through the destination profile to prove provider authentication independently of Telegram.
6. Ask the user to send a unique probe such as `VPS OK` to the real bot.
7. Correlate the destination log timestamps for inbound message, agent execution, and outbound reply.
8. Keep the migration ticket open until the user-facing probe succeeds. `active (running)` proves only lifecycle, not routing.

Do not copy bot or provider secrets between hosts as a synchronization mechanism. Each host owns its credentials; only one host owns a long-polling bot at a time.

## Success criteria

- Credential pool contains no known-invalid high-priority entries.
- Gateway has reloaded the updated pool.
- A real model call succeeds.
- No new provider-auth errors appear in the observation window.
- A fresh message from the actual channel is handled by the intended gateway.
