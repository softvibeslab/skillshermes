# Cross-host Hermes coordination through GitHub

Use this when one Hermes host is the always-on messaging/orchestration node and another host performs local or specialized work.

## Minimal architecture

- One host owns each long-polling messaging bot. Never run the same Telegram token on two gateways.
- GitHub Issues are the durable task queue.
- Labels route work (`worker:mac`, `worker:vps`) and expose state (`status:ready`, `status:doing`, `status:blocked`).
- Each worker uses a dedicated branch such as `agent/<issue>-<slug>`.
- Pull requests carry the deliverable, verification evidence, and `Closes #<issue>`.
- The orchestrator reviews and merges; workers do not merge or deploy without explicit authorization.

Do not synchronize `.env`, OAuth, tokens, sessions, logs, active SQLite databases, or gateway runtime state through Git.

## Repository contract

Keep the first implementation small:

1. A `COLLABORATION.md` defining roles, claim flow, branch naming, evidence, conflicts, and blocking.
2. One GitHub Issue form requiring a result, acceptance criteria, context/files, constraints, and evidence.
3. One class-level profile skill that points to the collaboration protocol.
4. A small label set for host and state routing.

Do not add webhooks or pollers until both hosts are installed, authenticated, and manually complete one Issue-to-PR round trip. Automation before that creates duplicate claims and hides setup failures.

## Claim and delivery flow

1. Orchestrator creates one outcome per Issue and applies one worker label plus `status:ready`.
2. Worker reads the complete Issue and comments, then comments `CLAIM <host>` and changes state to `status:doing` before editing.
3. Worker fetches current `origin/main` and creates its branch from it.
4. Worker makes the minimum change and leaves one runnable check for non-trivial logic.
5. Worker pushes and opens a PR with evidence and `Closes #<issue>`.
6. If blocked, worker applies `status:blocked` and comments the cause, evidence, and exact unblock action.
7. Tasks touching the same files or depending on each other are serialized by the orchestrator.

## Telegram ownership cutover

Repeated `Conflict: terminated by other getUpdates request` means another process is polling the same bot token. Distinguish local duplication from another host without printing secrets:

1. Compute a short SHA-256 fingerprint of each profile-local Telegram token and report only profile names sharing the fingerprint.
2. If another local profile shares it, stop or reconfigure the unintended profile.
3. If no local duplicate exists, treat the competing poller as another host or service.
4. Once the intended owner is chosen, stop the source gateway before activating the destination.
5. Verify shutdown using process/service state; command success or stale service metadata alone is not enough.
6. Verify the destination with a fresh PID, fresh healthy logs, and one real inbound/outbound Telegram message.

Never request a server password. Continue remote activation only with an existing SSH key/alias or user-executed commands.

## Completion evidence

- Repository protocol and Issue form exist.
- Required labels exist.
- At least one bootstrap Issue is open or completed.
- Local and remote repository HEADs match after publication.
- The profile can explicitly load the coordination skill and pass a one-shot response test.
- Exactly one gateway owns the Telegram bot.
- One real Issue-to-branch-to-PR cycle succeeds before polling automation is enabled.
