# Mutable fleet control planes: security and evidence gates

Use when a dashboard manages real Hermes profiles, sessions, channels, models, SOUL, skills, integrations, or schedules.

## Reuse before building

Inspect the installed Hermes dashboard/plugin contract and existing Profile Hub before adding another web service. A static snapshot is appropriate for an audit, not a substitute for requested live CRUD. Prefer a native extension when the installed runtime supports the required scope; verify its current manifest, API routing, authentication, and frontend bundle contracts.

## Scope and completion

Track each requested capability separately: inventory/read, preview, mutation, recovery, and end-to-end verification. Inventorying cron or MCP configuration does not implement their CRUD. Editing SOUL does not establish profile lifecycle support. Distinguish built, tested with synthetic profiles, installed, authenticated remotely, and verified against the intended runtime. On resumption, inspect artifacts and rerun relevant checks before converting historical reports into fresh success claims.

## Mutation boundary

- Deny profile access by default and authorize each target on the backend; hidden UI controls are not authorization.
- Return allowlisted metadata rather than raw configuration, logs, secrets, or message bodies.
- Validate filesystem targets and parent directories; reject symlink traversal. No-follow on the final file alone does not secure its ancestors.
- For configuration/identity changes, use revision checks, explicit confirmation for consequential actions, atomic writes, backups and a redacted audit trail. Never overwrite newer state silently.
- Test with disposable synthetic profiles before touching real profiles.

## Concurrent lock creation

A macOS implementation exposed a first-creation race around `os.open` with `O_CREAT | O_NOFOLLOW`. The repair separated atomic creation (`O_CREAT | O_EXCL | O_NOFOLLOW`) from reopening an existing lock on `FileExistsError`, then ran the existing concurrent-write regression.

Treat this as a reproduction-driven pattern, not a universal macOS diagnosis. Validate the reopened file via its descriptor, preserve no-follow protection, and acquire the actual lock before checking revisions or mutating data. Avoid unlinking a shared lock file while contenders may still hold its inode; exclusive creation alone is not mutual exclusion for the critical section.

Minimum regression: two writers submit the same expected revision; exactly one succeeds, the other reports a conflict, final content is valid, and no lock-creation exception escapes. Repeat on each supported OS.

## Remote release gates

Check DNS, non-interactive SSH command execution, runtime/plugin compatibility, and intended host/profile mapping before transfer. Keep deployment artifacts separate from credentials and runtime state; permission to deploy an app does not imply permission to export every local profile.

A localhost Host guard is not a remote authentication scheme. Before publishing through a proxy, verify application authentication, backend authorization, trusted proxy/Host handling, TLS, and CSRF protection where cookie-based authentication requires it. Do not remove local guards merely to make the public URL load.

Verify independently: build, backend tests, browser behavior, plugin loading, unauthorized access rejection, authorized read/write with recovery, service startup, and HTTPS. Unit tests plus a bundle do not prove UI integration or deployment readiness. Record unmet gates without presenting a partial inventory as a complete mission-control system.
