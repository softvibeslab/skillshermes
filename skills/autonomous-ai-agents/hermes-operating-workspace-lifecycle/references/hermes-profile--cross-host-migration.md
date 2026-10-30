# Cross-host Hermes profile migration

Use this when moving a Hermes profile between a laptop, workstation, VPS, or another Hermes host.

## Migration gates

Treat these as separate gates; never collapse “package created” into “migration complete”:

1. Source profile inventory.
2. Secret-clean export.
3. Destination SSH/runtime preflight.
4. Transfer plus checksum verification.
5. Import and stale-runtime cleanup.
6. External dependency relocation.
7. Destination authentication and platform-secret setup.
8. One-shot model test.
9. Gateway activation and live-channel test.

## Source inventory

Before export, record without printing secrets:

```bash
hermes profile show <profile>
hermes -p <profile> config
hermes -p <profile> skills list
hermes -p <profile> gateway status
```

Inspect `SOUL.md`, profile-local skills, cron jobs, and configuration for absolute paths or references to repositories outside the profile directory. A profile archive cannot carry those external repositories automatically.

## Export and inspect

```bash
mkdir -p ~/Downloads/hermes-profile-migrations
hermes profile export <profile> -o ~/Downloads/hermes-profile-migrations/<profile>.tar.gz
tar -tzf ~/Downloads/hermes-profile-migrations/<profile>.tar.gz
shasum -a 256 ~/Downloads/hermes-profile-migrations/<profile>.tar.gz
```

Current profile exports may omit `.env`, provider credentials, and model auth while still containing runtime artifacts such as logs, PID/lock files, gateway state, and caches. Inspect the actual archive every time; do not infer its contents from the source directory.

Never add live `.env`, tokens, API keys, or private auth files to the archive just to make migration easier. Reconfigure them at the destination through the provider/platform’s supported authentication flow.

Inspect nested profile `home/` as well: export can include Codex/npm caches and materialize symlinked host binaries, dramatically inflating the archive. Keep the native export as a local source artifact; construct a portable, allowlisted archive excluding caches, host binaries, logs and stale locks. Preserve requested history with SQLite's backup API (not a raw copy of a live DB/WAL), validate integrity, scan for known credentials without printing them, and compare per-file hashes after import. Copy external knowledge separately and relocate active references rather than rewriting historical conversations.

For SSH device-code authentication, use a real PTY (`ssh -tt` and terminal `pty=true`) if the authorization code is buffered or not visible. Before restarting the flow, terminate only the exact previous login process. Do not start multiple simultaneous logins, reuse source refresh tokens, or claim activation while waiting for user authorization.

## Destination authentication checkpoint

For a staged pilot using a dedicated Linux runtime account:

1. Resolve the intended OS user, HOME, Hermes executable and profile directory before any configuration/auth command. Execute migration, login and probes under that same identity. Avoid combining a profile-local `HERMES_HOME` and profile selector unless the installed CLI confirms the resulting path.
2. If destination and source versions differ, preserve the original staged configuration and validate the destination's supported config-migration command against the staged copy only. A schema migration succeeding is not runtime compatibility proof; never overwrite source configuration with the migrated copy as an implicit rollback.
3. Keep one provider authorization process alive through the handoff, using a PTY or a bounded persistent terminal session when needed. Record its host, runtime account, session identifier and pending gate in a protected checkpoint, not its device code or tokens in skills or durable memory.
4. After interruption, inspect that exact process and its fresh output. A summarized or redacted code is unavailable evidence: never invent its replacement, reuse an earlier code without verification, or promise a fixed validity interval. If expired, end only the previous login process and initiate one fresh flow with the user's authorization.
5. Verify successful authentication under the runtime identity, then run a minimal real inference and a read-only mission probe. `info`, config display, file presence and SQLite integrity do not prove model access.
6. While waiting for user authorization, explicitly report “staged, authentication pending; source remains owner” only when supported by observed state. Do not activate destination messaging or proceed to the next fleet wave.

## Destination SSH preflight

First test non-interactively:

```bash
ssh -o BatchMode=yes -o ConnectTimeout=15 user@host 'hostname; command -v hermes; hermes --version'
```

A successful TCP probe to port 22 proves only that something accepted the socket. It does not prove SSH is healthy. If SSH times out during banner exchange, stop transfer attempts and repair/check `sshd`, host load, connection limits, firewall/proxy behavior, or the provider console. Do not misdiagnose a pre-banner timeout as a key/password failure.

## Transfer and verify

```bash
scp <profile>.tar.gz user@host:/tmp/
ssh user@host 'sha256sum /tmp/<profile>.tar.gz'
```

Compare the destination checksum with the source checksum before import.

## Import and sanitize

On the destination:

```bash
hermes profile import /tmp/<profile>.tar.gz
hermes profile show <profile>
```

Before starting the gateway, remove or ignore copied stale runtime state as appropriate: PID/lock files, gateway state, old logs, caches, and source-host launch/service assumptions. Audit cron jobs and keep them paused until the destination profile is validated.

## Relocate external dependencies

For every absolute path found in `SOUL.md`, skills, config, scripts, or cron prompts:

1. Clone/copy the required repository or data directory to a stable destination path.
2. Pin or record the intended branch/commit when reproducibility matters.
3. Rewrite profile references to the destination path.
4. Verify the referenced files exist before running the agent.

Prefer a stable project root such as `/opt/<project>` or `/srv/<project>` on a VPS rather than reproducing a macOS home-directory path.

## Reconfigure destination-only state

Set up separately on the destination:

- model/provider authentication;
- Telegram/Slack/Discord/WhatsApp tokens;
- allowlists and home channels;
- web/search API keys;
- OS-specific services, sandboxes, browser dependencies, and permissions.

Run `hermes -p <profile> doctor` and fix only capabilities required by the profile’s real mission.

## Fleet planning and scope

Planning authorizes read-only discovery, not service changes or private-state transfer. Record one row per profile: source/destination identity, bot username verified by redacted `getMe`, model authentication, external files, plugins/MCPs, schedules, OS-bound capabilities, isolation needs, acceptance probe, and rollback checkpoint. Label historical checks separately from fresh evidence.

Choose the lowest verified dependency surface as the pilot. A profile with no declared MCPs or a `cwd` of `.` can still depend on external skills, scripts, or documents. Group subsequent waves by dependency readiness, not business affinity alone. Inspect destination services and resource headroom; do not promise that a host can support a fleet before measuring load and intended concurrency. Keep Hermes versions compatible and defer upgrades to a separate change.

On macOS-to-Linux moves, rebuild virtual environments and native dependencies rather than copying them. Inventory links recursively without dereferencing unrelated trees. Preserve uncommitted project work and transfer approved external knowledge independently of profile state. Use non-root runtime accounts; separate profiles under one OS user are not filesystem isolation, especially across clients or third-party users.

For host-bound workers, inspect their actual mission and queue routing. Moving a Mac worker requires reviewing desktop dependencies, source paths, SOUL instructions, issue labels and the orchestrator that assigns work. Keep genuinely macOS-only execution local when necessary. Preserve the profile slug initially if renaming would break references; treat renaming as a separate change.

## Transactional activation sequence

1. Stage destination with gateway, scheduler and automatic workers disabled. Confirm no startup hook can consume production events during tests.
2. Run a one-shot model probe and a mission-specific read-only test. A generic greeting does not prove CRM, knowledge, specialist-router or build functionality.
3. At the approved cutover window, drain source work; stop source gateway and other autonomous consumers. Disable their automatic restart paths and verify live processes/services, not just a stop command's success message.
4. Capture and validate the final mutable-state snapshot after quiescence. Synchronize final sessions, memory, project changes and necessary messaging state according to the installed runtime's semantics; do not discard channel offsets blindly or transfer source PID/locks.
5. Start only the destination gateway using verified installed commands, then inspect fresh logs and one live platform exchange. Never allow simultaneous pollers for the same bot token.
6. Check identity, knowledge retrieval, allowlists and representative tools. Test unauthorized access only with an explicitly authorized test account; otherwise report configuration verification rather than claiming an end-to-end denial test.
7. Enable audited cron jobs and workers last. Review overdue schedules and previously executed actions before allowing catch-up; avoid duplicate deliveries.
8. Verify service restart and state persistence. Observe real workload for an agreed period before the next wave; duration is a proposed observation window, not a stability guarantee.

Use the native service manager, normally systemd on Linux, with per-profile service identity and logs. Verify service commands against the installed Hermes version rather than copying guessed units. CLI success, messaging success, schedule activation and restart recovery are separate gates.

## Rollback after destination activity

Stop destination gateway, schedules and workers first, preserving its latest state. Compare new sessions, memories, files and job executions against the cutover checkpoint before restoring source operation. Do not overwrite either host blindly or merge SQLite files at the filesystem level. Reconcile external side effects separately: reverting a host does not undo CRM mutations, Slack messages or Skool publication. Initial probes should therefore be read-only.

Reactivate the source only after state reconciliation and confirmation that the destination cannot restart itself. Verify one live channel exchange. Keep a redacted per-profile receipt of checkpoint, ownership, completed gates, outstanding gaps and exact recovery action; retain protected backups until acceptance.

## Completion evidence

Declare the migration complete only when all applicable evidence exists:

- source and destination archive checksums match;
- imported profile appears in `hermes profile list`;
- expected skills and identity files are present;
- external repositories/paths resolve on the destination;
- provider authentication succeeds;
- one-shot agent response succeeds;
- destination gateway has a current PID and fresh healthy logs;
- one live channel message succeeds;
- source and destination are not competing for the same bot token.