# Cross-host installer and knowledge-sync preflight

## Installer scope is determined by code, not flag names

Review the installer and every invoked helper before execution. Trace config writes, generated files, replacement/deletion targets, and how HERMES_HOME and --profile combine. A --profile option can add a second config write while still modifying the main config; it does not establish isolation.

In the Sales Academy squad installer inspected during reconnaissance, the script always enabled the plugin in HERMES_HOME/config.yaml, optionally enabled it in HERMES_HOME/profiles/NAME/config.yaml, and replaced existing plugin/squad directories. Treat this as an inspection example, not a permanent claim about future revisions. Re-read the current script before use. Do not blindly combine a profile-local HERMES_HOME with --profile if that constructs a nested profiles path.

Inventory both hosts and resolve the intended profile mapping before mutations. A matching project name is a candidate, not authorization to modify it. Back up exact replacement targets and affected config before installation; restart only the selected gateway. Cloning and shell syntax validation do not prove installation or runtime function.

## Separate SSH authentication from optional remote probes

SSH normally returns the remote command's exit status. A successful login followed by a missing optional executable can make an identity-selection loop continue and ultimately appear to fail authentication.

Use an authentication-only probe first:

```sh
ssh -i "$KEY" -o IdentitiesOnly=yes -o BatchMode=yes \
  -o StrictHostKeyChecking=yes -o ConnectTimeout=10 "$DEST" true
```

Then collect capabilities separately, guarding optional probes with `|| true`. Preserve genuine required-command failures. Use only a destination obtained from current authorized configuration or user input; never reconstruct redacted connection details from a summary. Verify unknown host keys through a trusted channel rather than disabling host checking. Prefer existing authorized identities without printing their contents or handling passwords supplied in chat.

## Synchronization is a separate deliverable

Installing the same plugin on two hosts does not synchronize their knowledge. Define a small explicit allowlist of shared project artifacts (documents, decisions, tasks, results), the host/profile mapping, transport, refresh trigger, and conflict policy. Keep tokens, auth files, environment/config files, session databases, and unrelated profile state out of the bridge. Never mirror all of ~/.hermes as a knowledge-sync shortcut.

Reuse an existing project repository or coordination mechanism when it meets the requirement. GitHub Issue/PR dispatch coordinates work but does not by itself prove document freshness. Before enabling automation, prove a manual round trip and choose one owner for any shared long-polling bot.

Verification gates for a claimed two-way bridge:
- A harmless artifact created on each host reaches the other.
- Concurrent edits preserve both versions or produce an explicit conflict, not silent overwrite.
- Disconnect/reconnect catches up without loss; offline hosts are reported as stale.
- Excluded secrets/config/session state never enter the shared payload.
- Report a last-success timestamp and distinguish installed, runtime-tested, and sync-tested.

These are implementation gates, not outcomes established by the reconnaissance session. No bridge was implemented or validated there.
