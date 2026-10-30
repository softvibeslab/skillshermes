---
name: provider-auth-operations
description: Diagnose and repair provider authentication failures in agent gateways and multi-credential OAuth pools. Use for persistent 401/403 errors, invalidated or consumed refresh tokens, reauthentication that does not take effect, and suspected duplicate channel consumers serving stale responses.
---

# Provider Authentication Operations

Repair authentication at the actual failure boundary while keeping provider, gateway, and messaging-channel faults separate.

## Workflow

1. Read the raw provider error from current gateway logs. Record provider, model, endpoint, HTTP status, provider code, and timestamp; redact secrets.
2. Trace the credential-selection path. Inspect pool metadata, priority, active entry, status, and renewal age—not token values.
3. Treat `logged in` as inventory, not proof. Reauthentication may append a new credential while stale higher-priority entries remain selectable. Likewise, `exhausted` alone does not prove revoked credentials or quota depletion. Correlate current gateway errors with provider-state and pool metadata; stored `last_auth_error` may predate the current failure. A missing provider access token can coexist with token-bearing pool entries.
4. Remove only credentials proven invalid or revoked, or confirmed obsolete and explicitly selected for cleanup. A cooldown/`exhausted` marker or old refresh timestamp alone is not deletion evidence. Preserve recoverable and working entries; adding a usable OAuth entry does not require deleting the original.
5. Restart/reload the long-running gateway so it rereads authentication state.
6. Make one real model request through the affected profile.
7. Observe fresh logs and verify that no new authentication failure appears.
8. For a multi-host channel handoff, stop the old consumer first and verify it is actually stopped before starting/restarting the elected owner.
9. Observe a short conflict-free window, then test from the exact user-facing channel with a unique message and correlate inbound processing plus reply timestamps with the elected gateway.
10. Keep the migration/work item open until that end-to-end channel probe passes; process status and a direct CLI model call are necessary but not sufficient.

## Remote OAuth attempts over SSH

An SSH disconnect or killing the local SSH client does not prove the remote OAuth process exited. Before retrying, inventory remote processes for the exact profile/provider, inspect credential metadata, and reconcile the existing attempt. Keep only one authorization attempt in flight; terminate only verified task-owned duplicates and confirm their exit. Never use broad process-name kills against a multi-profile host.

Blank background output is not proof of failure or success. Check the tracked process log and remote process state before launching another attempt. PTY/unbuffered output may help visibility, but is not an established fix for every silent attempt. Share only a device code actually emitted by the current attempt, never reuse a previous code after abandoning its process. If no code is observable, report authorization as blocked rather than starting a retry loop.

Keep the destination gateway stopped during authorization. An auth-list entry is inventory, and a stored 429 is a quota marker—not proof that the newest authorization failed or that credentials are invalid. Verify a real model request before any channel handoff; verify both hosts before claiming which one currently serves the bot.

## No selectable credential is not the same as no stored credential

When `No Codex credentials stored` follows `credential pool: no available entries (all exhausted or empty)`, inspect pool eligibility before concluding that authentication material is absent. A turn ending with `api_calls=0` supports a failure before model execution; it does not establish a fresh provider HTTP rejection. Check current status/cooldown and nullable error metadata without printing tokens. Do not infer revocation or insufficient balance from the generic gateway warning.

Bound log inspection to the failing message and the latest restart. Bare searches for `401|403` can match timestamp milliseconds or memory statistics; require HTTP/error context. Historical polling conflicts and auxiliary-provider errors are separate evidence, not automatic explanations for the current primary-provider failure.

For an authorized reauthentication, keep one tracked OAuth process in flight, confirm its exit, inspect the selected pool entry, and run a minimal real request before restarting only the affected gateway. After restart, verify its new process and fresh channel-connection logs. If the user has not yet sent a channel probe, report “provider verified; Telegram end-to-end pending” rather than claiming the whole bot is verified.

## Fault Separation

- Provider 401/403: credential or provider-policy path.
- Gateway lifecycle failure: process/configuration path.
- Channel polling/webhook conflict: duplicate consumer or routing path.
- User sees an error absent from current logs: likely another instance or stale delivery path.

Do not let a Telegram polling conflict masquerade as the cause of an OAuth 401. It may only explain why the user still sees a response from an older instance.

## Verification Contract

A repair is complete only when:

- a real provider request succeeds;
- the current gateway emits no fresh auth error;
- the exact user-facing channel reaches that gateway;
- secrets never appear in output or logs produced during diagnosis.

## Reference

See `references/oauth-pool-and-duplicate-consumer.md` for the detailed cleanup, missing-token versus pool-state diagnosis, device-code authorization handoff, and channel-correlation playbook.

## Pitfalls

- Reauthenticating repeatedly without inspecting the pool.
- Deleting the whole pool instead of isolated bad entries.
- Trusting an auth-status command without a model call.
- Assuming a persistent `getUpdates` conflict is a harmless retry.
- Printing tokens to compare consumers; compare redacted fingerprints instead.
- Guessing CLI subcommands instead of consulting live help.
