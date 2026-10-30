# Recovering interrupted stateful simulations safely

Use when a stopped agent simulation retains social/event databases but lacks a complete process checkpoint.

## Evidence before continuation
1. Distinguish persisted `running` status from a live process. Inspect runner entry points and every reset/start caller before invocation: normal startup may delete existing databases or register duplicate users.
2. Separate recoverable layers: social rows, event logs, model conversation memory, RNG, selected agents/in-flight work, and simulation clock. Persisted actions do not prove persisted observations or conversational memory.
3. Inspect the actual memory backend and calls to export/import. An available `save_memory` method does not imply it was used.
4. Reconcile round-start/end events within the latest execution, not across concatenated runs. An open round is partial, not completed. Without per-agent commit markers, replay can duplicate actions and skipping can omit them. Obtain an explicit recovery policy and record partial closure in append-only sidecar evidence; never fabricate a historical completion event.

## Isolate and preserve
- Freeze/quiesce writers before snapshot. Treat SQLite WAL/journal sidecars as a coordinated-backup requirement, not disposable files. Do not use immutable reads on a potentially active WAL database.
- Preserve original and sealed snapshot; operate on a third independent copy, no hard links. Capture whole-directory hashes before/after and compare logical table rows, rowids and sqlite_sequence across schema repairs.
- Refuse overwrite and ambiguous live ownership. Verify manifests again after tests.

## Schema diagnosis
Run both `integrity_check` and `foreign_key_check`: physical integrity can pass while relational validation fails. Inspect actual CREATE TABLE SQL, FK metadata, parent uniqueness and all consumers.
- A FK to a nonunique parent may be repaired by a unique index only after confirming semantic correctness and absence of duplicates.
- A reference to an obsolete table name requires matching the intended parent table against actual write/read paths.
- Fixing schema can reveal existing orphan rows. Do not delete those silently, invent parents, or disable validation. Preserve evidence and agree on quarantine or reconciliation policy before changing active data.

## Approximate agent hydration
Restore identity mappings and channels without calling reset/signup/seed/step. Seed context from each agent's own persisted actions/authored material, labeled as quoted external evidence, not restored episodic memory. Do not invent exposure to others' posts.
Read clock implementation: round number may differ from active-step counter or scaled wall time. Record an explicit lower-bound/freeze-downtime policy; do not claim exact clock or RNG recovery.

## Offline validation and honest readiness
Use actual installed library graph/environment code on disposable clones with a noncalling model stub. Block model inference, reset/signup/step and network access. Assert identity/channel wiring, context injection, clock policy and unchanged rows/hashes. Test tampering, malformed events, overwrite refusal and repeat verification.
Library logs such as 'Simulation finished' on close or 'table already exists' on attach are not execution evidence. Report measured calls and database comparisons.
Distinguish: snapshot prepared; adapter tested offline; policy staged; executable loop implemented; real round verified. Passing preparation tests does not make a live runner ready. Keep readiness checks fail-closed on unresolved relational or continuation issues.

## Diagnosing a fail-closed continuation
- Read the redirected application log, run-state file and per-platform checkpoints together. A background process notification may show only shell lifecycle output; a wrapper warning does not establish why the application exited.
- Treat `UnsafeRecovery` or `failed_requires_review` as a safety outcome, not an explanation. Trace every raise site and its callers. If the top-level handler discards detail, preserve the exception chain/traceback and guard inputs in local diagnostics, redacting secrets; test the handler offline rather than rerunning paid inference just to obtain a traceback.
- Inspect the installed agent return contract before treating `None` as failure. OASIS 0.2.5 `perform_action_by_llm` returns inside its tool-call loop: a successful `astep` with no tool calls falls through to `None`. Reproduce using the installed method offline. Accept that case only after observing a successful nonterminated response with an empty tool list; continue rejecting unexplained None, returned exceptions and terminated responses. Do not invent a do_nothing trace or retry inference.
- Keep import-isolation recovery tests in separate Python processes when a suite explicitly asserts OASIS/CAMEL were never imported; combined unittest discovery can fail teardown because a different hydration test legitimately imported them.
- A whole-round timeout includes recommendation work, serial agents behind the OASIS semaphore, and potentially multiple CAMEL/tool/model requests; it is not a per-inference timeout. Inspect installed model client timeout/retry defaults and actual local routing before diagnosing deadlock. An expired outer deadline plus committed partial actions proves neither an infinite loop nor merely slow inference. If authorized, expose a finite positive validated round deadline, forward it from CLI through run to both loops, retain cancel-and-await and durable pending checkpoints, and test those paths offline. Never change models/prompts to hide the timeout. Archive each later partial round on a new clone using its actual checkpoint boundaries, not earlier hardcoded staging values.
- Historical hydration tests that verify a formerly pristine clone must use post-run verification once a run-state exists; keep pristine verification for the new unlaunched clone. Preserve whole-tree manifests and verify original witness hashes again after all tests.
- Reconcile each platform separately: last committed round, pending round, selected agents if recorded, pre/post trace high-water marks and committed actions. New trace rows prove actions occurred, not that a round completed. Passing SQLite integrity and FK checks does not prove replay is safe.
- Do not automatically retry a non-idempotent partial round. Preserve its evidence and apply an explicit skip/quarantine/reconciliation policy on a new clone. A prior policy accepting one partial round is not blanket permission to accept all later partial rounds.
- Progress reports should separate live evidence from last-known progress: process present/absent, checkpoint state, verified completed rounds, unresolved partial rounds and whether any repair/relaunch actually happened. Do not imply work continues in the background when no worker exists.
- If continuation was already authorized, proceed with read-only diagnosis and offline checks rather than repeatedly presenting the same next-step list. Ask again only when the recovery policy or side-effect scope materially changes.

## Live execution and completion gates
- Before paid or non-idempotent continuation, probe the configured model endpoint using the application's actual routing, not an assumed provider. Check service readiness and model availability without exposing credentials. A successful offline stub test does not verify the runtime dependency chain.
- Regression tests must exercise the execution loop and the real library's return semantics, not only snapshot creation and hydration. Include successful no-tool responses, tool actions, returned exceptions and terminated responses; assert that no branch repeats inference or fabricates persisted actions.
- After launching, verify the worker's command identity and fresh checkpoint advancement on each platform beyond the prior failure boundary. A PID or persisted `running` field alone is insufficient. Preserve redirected application diagnostics and use an explicit completion-notification mechanism for bounded background work.
- On worker exit, inspect exit code, per-platform committed rounds, unresolved pending markers, database validation and produced outputs. Target round reached on one platform is not whole-run completion. Do not relabel accepted partial rounds as completed.
- Reports generated before recovery remain historical. If final analysis is requested, regenerate it from the recovered outputs or clearly identify which run it describes; retain approximate-memory and partial-round limitations. Synthetic outcomes are hypotheses, not real-user validation.

## Example findings (MiroFish / OASIS / CAMEL)
The inspected installation stored CAMEL conversation history in process-local InMemoryKeyValueStorage. OASIS attached to existing users without reset, but clocks differed by platform. Its schema included group_messages referencing a nonunique user key and like/dislike/rec referencing an absent tweet table; correcting parent metadata exposed orphan follows. These are inspection examples, not assumptions about other versions. Re-read live schemas and implementations each time.
