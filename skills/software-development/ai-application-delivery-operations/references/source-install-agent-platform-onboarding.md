# Source installation and agent-platform onboarding

Use alongside the parent skill when a repository install includes an operator-facing HTML guide. These are source inspection findings, not a claim of a completed runtime test.

## Paperclip inspection anchors

Repository: https://github.com/paperclipai/paperclip

- `README.md`, `docs/start/quickstart.md`: source-install/start instructions and runtime requirements. Re-read the current versions rather than pinning this reference to a historical dependency set. The inspected source documented `pnpm dev`, UI/API on localhost:3100, and embedded PostgreSQL.
- `scripts/dev-runner-options.ts`: `--data-dir` sets `PAPERCLIP_HOME`; explicit `PAPERCLIP_CONFIG` and `PAPERCLIP_CONTEXT` can remain authoritative. A new data directory alone therefore does not prove isolation. Inspect resolved paths without printing credentials.
- `scripts/dev-runner.ts`: discover current `--bind loopback` handling and workspace build orchestration. Verify the actual listener after starting, not just the requested flag.
- `server/src/config-file.ts`: config is validated against the shared `paperclipConfigSchema`. Do not invent a minimal JSON config without checking required fields/defaults.
- `server/src/config.ts`: inspected controls included `HEARTBEAT_SCHEDULER_ENABLED=false` and `PAPERCLIP_ANNOUNCEMENTS_ENABLED=false`; the telemetry field used `fileConfig?.telemetry?.enabled ?? true`.
- `packages/shared/src/telemetry/config.ts`: a `DO_NOT_TRACK === "1"` check was found after a server-only search returned no matching environment switch. Read its surrounding code and callers to establish effective behavior; finding a string is not an end-to-end telemetry test.
- `docs/start/core-concepts.md`: companies, agents, tasks, heartbeats, approvals, budgets, and audit trails form the onboarding concept map. Scheduler off is not a universal execution stop: assignment, mentions, manual actions, and approvals may trigger work.

## Verification sequence

1. Read manifest, lockfile, startup scripts, configuration schema and trigger paths. Keep existing user edits intact.
2. Install with the repo-required package manager, scoped to the project. If frozen installation fails, establish the specific cause before proposing lockfile reconciliation; inspect the final dependency diff.
3. Select isolated storage/config and loopback exposure. Explicitly control telemetry and background scheduling using verified configuration mechanisms. Do not link accounts, add provider secrets, or launch an agent just to demonstrate the UI.
4. Start using a tracked process. Record a non-secret startup log and resolved URL; probe health, inspect the listener, and load the UI. Classify missing internal workspace executables by checking whether the supported startup path compiles them.
5. If activation is out of scope, stop before any onboarding action that creates or starts a live agent. Use explanation or clearly labeled screenshots instead of a paid execution demo.
6. Build the HTML guide from observed results. Distinguish installed dependencies, verified server, connected accounts, and successful agent execution as separate milestones.
7. Verify the guide in a browser. Include exact working paths and tested commands in the delivery artifact, not as reusable assumptions in this reference.

## Runtime pitfalls discovered during source installation

- The supported dev runner may build a Rust native binary even for an empty instance. Inspect `scripts/dev-runner-native-binary.mjs` and `server/src/dev-native-runner-status.ts`; do not fake a binary path to bypass compilation. If Cargo is missing, install a minimal toolchain with project-local `CARGO_HOME` / `RUSTUP_HOME` and rustup `--no-modify-path`; export those directories in the launcher rather than changing the user's global shell.
- A tested `dev:stop` invocation reported success but left the HTTP server and embedded PostgreSQL child alive when started through a background shell. Verify both listeners after stopping. Prefer a tracked PTY with Ctrl+C; for cleanup of an owned background job, verify its process group before sending SIGINT to that group. Never kill all Node/Postgres processes. Do not claim the upstream stop command works solely from its exit code.
- A healthy empty instance may report `database_backup_missing` before its first scheduled backup and an Agent JWT warning before onboarding. Record those limitations; do not create agents or run onboarding to hide them.

## Guide acceptance checklist

- Spanish when requested; concept explanations precede unfamiliar controls.
- A direct local-app link plus an absolute guide path.
- Start, stop and restart; persistent data location and backup caution.
- First exercise that cannot silently connect accounts or run paid agents.
- Explicit cost, credential, permission and external-exposure boundaries.
- Troubleshooting based on observed or documented behavior, with untested advice labeled.
- No secrets in snippets, screenshots, environment dumps or process listings.
- Status backed by checks, not cosmetic progress indicators.

If authorization is denied, stop the denied workflow. Report what has and has not been verified; do not label installation as operational or the guide as delivered while either acceptance gate remains incomplete.
