# Multi-role pilot: contract and state-integrity audit

Use for a live pilot with member/operator/admin screens, shared task definitions, per-user submissions, and completion rewards. Derived from a BeGlobal miniapps review; the examples below are historical reproduction patterns, not assertions about the current code.

## Minimal review sequence

1. Identify the active application subtree from project instructions and callers; do not audit an archived backend as if it served the current UI.
2. Trace each critical action end to end: rendered control → JavaScript request and serialization → registered route → auth dependency → SQL predicate → reward/counter/audit writes → response/UI handling. Search sibling callers before proposing the shared fix.
3. Run existing tests, but classify what they exercise. Direct SQL fixtures can validate a schema without testing the browser/API contract. Green suites and a public homepage returning 200 do not establish an operable pilot.
4. Reproduce with an isolated temporary database and synthetic identities. Point every DB connection at it and mock outbound notifications. Do not exercise mutation routes against production. Use the actual HTTP request shape rather than only calling Python handlers.
5. Seed two distinct members sharing one task definition, plus one identity represented in multiple profiles. Replay completion and approval requests. Inspect all affected rows, not only status codes.
6. Assert target-only changes, first-transition-only rewards, consistent counters, persisted feedback/completion timestamps, and attributable audit events. Keep state transition and its side effects atomic. Concurrent replay is a separate check when transaction behavior is in scope.
7. Retain one runnable regression check per distinct reproduced failure or a compact combined check. Report the command, evidence, and boundaries; never weaken assertions to match defective behavior.

## High-value probes

- **Definition ID versus submission ID:** give members A and B the same mission. Approve A's submission and assert B remains unchanged. Ensure reward owner and updated row owner agree. Batch and individual paths should enforce the same transition rules.
- **Serialization mismatch:** compare actual frontend payload with backend declarations. A `dict` declared with FastAPI `Form(...)` must not be assumed to accept arbitrary form fields or a JSON string; test the installed implementation and choose one explicit contract. `new FormData(existingFormData)` is not cloning: the constructor expects a form element (or no argument).
- **Route drift:** compare the literal approve/reject URLs and methods in each UI with registered backend routes, including singular/plural prefixes and per-submission identifiers. A similarly named endpoint does not prove the UI route works.
- **Replay:** complete the same lesson twice; assert one completion and one reward/counter increment. Test both bulk and single approval paths for duplicate rewards.
- **Composite identity:** if the key is `(external_user_id, profile)`, query with both. Preserve the authenticated profile instead of taking the first row returned by user ID alone.
- **Review persistence:** verify feedback, completion date, reviewer/actor and audit record after an approval. Telemetry is not automatically a durable audit trail.
- **Python date helper:** a function-local import can shadow a module-level name before its first use and raise `UnboundLocalError`. Exercise the helper, including empty initial date and consecutive-day cases, rather than relying on compilation alone.

## Implementation checklist: transactional pilot repairs

These techniques extend the audit into an authorized fix; inspect the current schema and callers before adopting them.

### State transitions and concurrency

- For SQLite read-modify-write rewards, acquire `BEGIN IMMEDIATE` before reading eligibility, not merely before the final update. Keep the transition, XP, counters, achievements, telemetry and audit writes in the same transaction. This serializes database writers; retain the lock only as long as necessary and revisit if measured write contention matters.
- Route single and bulk approval through the same transition helper inside caller-owned transactions. Deduplicate batch IDs. Use a persisted submission/delivery ID, never the shared task-definition ID.
- Make repeat completion a documented no-op or conflict without reward changes. Reject resubmission while already under review or completed; permit a rejected submission to retry, clearing stale review metadata.
- Test single-versus-single, bulk-versus-bulk, single-versus-bulk and submit-versus-review races using separate connections. Assert final rows and total rewards, not just response codes.
- Inject a failure after a transition but before its side effects finish. Assert rollback of every write and a clean successful retry. For filesystem evidence, track the new destination and remove only that request's partial file after write/transaction/commit failure; retain older evidence.
- `with conn:` commits/rolls back but does not close a SQLite connection. Use an explicit close or `contextlib.closing` for ownership clarity.

### Durable IDs and migration safety

- If IDs exposed to clients came from implicit rowids, migrate to an explicit `INTEGER PRIMARY KEY` (and `AUTOINCREMENT` when non-reuse is required), copying legacy `rowid` into the new ID and preserving the existing business-key uniqueness constraint.
- Snapshot full historical rows and relevant indexes/triggers before a table rebuild. Recreate dependent objects, preserve sequence semantics where relevant, rerun initialization to prove idempotence, and run `VACUUM` in a disposable copy to verify published IDs remain stable.
- Foreign keys targeting a user/profile composite key must reference that key, not an individually non-unique user ID. Do not fabricate or delete historical actors to make checks pass; identify orphan data as a separate blocker.
- SQLite foreign-key toggles must happen outside an active transaction and be restored in `finally`. Perform the table replacement transactionally and check both structural and referential integrity; counts alone do not prove preservation.

### Frontend contract checks without a new framework

- A small Node `vm` harness can load the actual shared request helper and page handlers, supply native `FormData`, mock fetch and minimal DOM dependencies, and assert URL, method, serialized fields and error propagation. Avoid copying the handler into the test, which can hide source drift.
- If testing request contracts rather than toast rendering, override the toast binding after the shared helper is evaluated (otherwise the helper can overwrite the test stub). Error toasts must fail the test, not be silently swallowed. Verify toast/DOM rendering separately when it is in scope.
- Keep test DB/media environment variables pointed at a temporary directory before importing application modules or starting a subprocess. Run both new regressions and existing tests there; never reuse a production/default DB for convenience.
- Report Python API tests, JS VM contract checks, existing suite results and actual browser tests separately. A mock harness does not validate layout, DOM integration or deployed authentication.

### Review and PR handoff

- Use a clean scoped worktree when the active checkout contains unrelated edits. Give the independent reviewer the actual base branch, complete diff, new untracked tests, runnable commands and no-production-data boundary.
- After commit/push, read the PR back: requested base, head branch/SHA, open state, mergeability and check results. Compare remote SHA to the tested commit. An empty `statusCheckRollup` is no checks reported, not a green CI run.
- Describe migrations and identifier-contract changes in the PR body, especially aliases that now accept delivery IDs. Preserve the no-merge/no-deploy boundary when only publication for review was requested.

## Evidence boundaries

A dependency-overridden auth test proves downstream identity selection, not real signature validation or an exploitable privilege escalation. Label it accordingly. Likewise, frontend code inspection, synthetic API reproduction, browser execution, and deployed Telegram execution are different evidence levels.

When only reviewing, leave application source and its real database unchanged. Proposed fixes are not completed fixes. Historical line numbers, counts, temporary paths, and bug status must be rechecked rather than carried forward as live facts.
