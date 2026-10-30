# Safe Hermes Core Upgrade with Local Customizations

Use this when the installed Hermes source tree is behind upstream and contains local edits that must survive, while profiles, gateway state, sessions, memories, and secrets must remain unchanged.

## Principle

Treat three assets separately:

1. **Runtime state** — `$HERMES_HOME`, profiles, sessions, memories, cron data, auth, and gateway configuration.
2. **Upstream core** — a clean checkout of the target Hermes revision.
3. **Local customizations** — a reviewed, secret-free Git branch containing only intentional source/test changes.

Do not run an in-place update against a dirty source tree. First preserve state and custom code independently; then port customizations onto a clean upstream checkout and test there.

## Phase 1 — Read-only inventory

Record, without printing secret values:

- `hermes version`, repository branch/HEAD, remotes, status, and upstream divergence;
- tracked modifications and untracked paths;
- all Hermes profiles;
- gateway/service state for every active profile;
- current Python/runtime environment and the relevant test commands.

Inspect every modified file and its callers before deciding which changes are intentional. Exclude generated files, caches, logs, archives, databases, `.env`, auth files, and session data.

## Phase 2 — Two independent backups

### Runtime-state backup

Use Hermes' supported backup/export path for configuration and data. Verify the archive exists and list its members without exposing file contents. Keep a second local copy outside both the source tree and `$HERMES_HOME` when practical.

A Hermes runtime backup may exclude the agent source repository; that is expected and is why the code backup below is separate.

### Custom-code backup

Use a dedicated Git repository as a bridge; recommend private by default without overriding explicit user instructions:

1. Verify the repository owner, current visibility, and requested visibility.
2. Change visibility only with authorization. If the user requires public, review all outgoing commits and reachable history, not just the working diff. If a safe public push cannot be established, preserve locally and offer a sanitized snapshot instead.
3. Add it as a separate remote such as `backup`; do not replace upstream `origin`.
4. Create a dated pre-upgrade branch from the installed commit.
5. Stage an explicit allowlist of intended source and test files—never `git add .`.
6. Review `git diff --cached --name-only` and `git diff --cached` for secrets and accidental files.
7. Commit and push the branch.
8. Verify the remote branch and commit exist.

The Git bridge is for source customizations only. Never push `.env`, auth/token stores, session databases, memories, runtime logs, or full `$HERMES_HOME` backups, even when the repository is private.

## Phase 3 — Quiesce runtime

Before copying mutable runtime state or changing the active installation:

1. Stop every running profile gateway/service.
2. Verify process/service state, not only command success messages.
3. Record which profiles were running so only those are restarted later.
4. Define the interruption path before stopping anything: if a later approval is denied or the maintenance window pauses, either restore the recorded gateways immediately or report an explicit maintenance state and one exact continuation action. Never leave the operator guessing whether services are intentionally offline.

## Approval boundaries and Git publication

Keep approval-sensitive operations in separate tool calls from reversible preparation and verification.

- Do not combine `rebase`, tests, backup verification, gateway recovery, and `git push --force-with-lease` in one shell command. A denial may prevent the entire batch from running, making it ambiguous which safe steps completed.
- Run read-only checks and local candidate validation first; verify their outputs independently.
- Prefer publishing the rebased candidate under a new immutable branch name. Use history rewriting only when the user explicitly requires the existing remote branch name and approves that single operation.
- If a rewrite is required, call only the rewrite command at the approval boundary, then verify remote HEAD in a separate read-only step.
- After any denial, assume the denied command made no change. Do not retry, rephrase, or bypass it; preserve the candidate locally and wait for a fresh user instruction.

## Phase 4 — Build the candidate in isolation

1. Fetch upstream without modifying the active checkout.
2. Create a clean worktree at the intended upstream revision.
3. Create a customization branch in that worktree.
4. Reapply the saved customization commit(s), preferring a cherry-pick when history is compatible and a reviewed patch when it is not.
5. Resolve conflicts against current upstream behavior, not by blindly choosing the old side.
6. Re-check every changed function's callers; move guards to the shared root cause when upstream structure changed.
7. Keep the resulting diff limited to intentional behavior and its smallest runnable checks.

Never copy the old source tree wholesale over the new version. That silently restores removed files and defeats the clean-core boundary.

## Phase 5 — Candidate verification

At minimum:

- run the focused tests for each customization;
- run Hermes' full supported test suite;
- run configuration migration/check commands against a disposable copy or isolated profile first;
- smoke-test CLI startup, profile listing, one representative profile, skill loading, and gateway startup without contacting unintended bots;
- compare the candidate customization diff against the pre-upgrade branch;
- verify no runtime state or secrets entered Git.

Do not alter production if the isolated candidate fails.

## Phase 6 — Transactional activation

Activate only after the candidate passes:

1. Record the old executable/source target.
2. Install or switch to the tested candidate using the project's supported mechanism.
3. Run config migration once, preserving a pre-migration copy.
4. Start only the gateways that were previously running.
5. Verify each with a live PID/service state and fresh logs.
6. Run one end-to-end message test on representative platforms.

Report the upgrade as complete only after version, profiles, gateways, and custom behavior all pass.

## Rollback

Rollback must restore both layers:

- switch the executable/source target back to the recorded old revision;
- restore runtime state only if a migration changed it or validation finds corruption;
- restart only the gateways that were running before maintenance;
- verify live status and fresh logs.

The reviewed Git branch is the durable source reference; the local Hermes backup is the runtime-state reference. Neither replaces the other. Before copying or declaring recoverability, follow `hermes-core--bounded-backup-and-recovery.md` for symlink boundaries, growth checks, and isolated restore validation.

## Common pitfalls

- Running `hermes update` while the source tree is dirty.
- Assuming `--backup` preserves source customizations.
- Changing repository visibility against the user's instruction, or pushing public history without reviewing it for private material.
- Using `git add .` and accidentally committing secrets or databases.
- Updating production first and treating rollback as the test plan.
- Restarting all profiles instead of only the previously active gateways.
- Bundling an approval-sensitive force-push with safe local validation; one denial can block the whole batch and obscure what ran.
- Leaving gateways stopped after a denied or paused maintenance step without restoring them or clearly reporting the maintenance state.
- Declaring success from a version string without validating profiles, gateway processes, fresh logs, and customized behavior.
