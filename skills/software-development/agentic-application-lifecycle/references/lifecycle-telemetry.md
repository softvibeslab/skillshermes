# Validated, non-blocking lifecycle telemetry

## Contract and state mapping

For append-only event bridges, keep a fresh event UUID per transition and a separate invocation UUID shared by that invocation's records. If the schema has no correlation field, prefix the recorded task with `[invocation-UUID]`; never add that prefix to the task sent to the model.

Representative schema: `{id, node, at, agent, status, task, result?, error?}` with canonical UUID, timezone-aware ISO timestamp, and status in `pending/started/completed/failed`. Let the existing writer generate and validate these fields rather than reimplementing persistence.

- Emit pending for the attempt.
- Emit started only after lifecycle.launch returns successfully, never before it.
- A wrapper returning success with a composed-prompt fallback is not a successful subagent: emit failed.
- Emit completed only when result.ready is true and terminal state is SUCCEEDED.
- A result that is not ready or cancellation grace wait that leaves work running stays pending. Do not force it into failed or completed.
- This synchronous wrapper observes only until it returns; do not claim later completion tracking without a real callback/poller.

## Privacy and isolation

Use a short normalized task excerpt validated by the bridge. Truncation alone is not secret detection. Use short fixed result/error categories instead of serializing arbitrary outputs or exceptions. Catch bridge import, validation, secret-detector rejection, and write failures at the telemetry boundary; emit a generic local warning and preserve delegation behavior. Do not include rejected values or exception messages in that warning.

For optional integrations, load the trusted module with `importlib.util.spec_from_file_location`, `module_from_spec`, and `exec_module`; avoid global sys.path mutation. Perform exact profile gating before importing or writing. Do not infer authorization from a loose profile-name prefix.

## Offline verification matrix

Use stdlib unittest, mock lifecycle/context, and the real bridge validator/writer directed into a temporary private store. Assert:

1. Inside launch, only pending exists; inside wait, started already exists.
2. Success yields pending → started → completed; original goal remains unchanged.
3. Failed terminal state yields failed, with no raw output/error secret in events.
4. Runtime unavailable or launch exception yields pending → failed, never started.
5. Wait exception after launch yields pending → started → failed.
6. Not-ready result and unfinished cancellation each yield pending → started → pending.
7. Import/write failures and secret-bearing task rejection warn locally without failing delegation or leaking warning text.
8. Exact profile gate, node mapping, distinct invocation correlations, shared correlation within each invocation, unique event IDs, schema validation, and on-disk event count.
9. Fixed-path import leaves sys.path unchanged.

When the writer traverses with O_NOFOLLOW, resolve the **test-owned temporary root** before passing it to the writer. macOS temporary paths can contain the `/var` → `/private/var` alias, which secure traversal correctly rejects. Do not loosen the production writer's no-symlink policy or resolve arbitrary untrusted paths to make tests pass.

## Sales Academy reference contract

The implementation used `HERMES_HOME` basename exactly `salesacademy`, bridge at `Path.home()/src/sales-academy-squad/control/bridge.py`, node `mac` for sys.platform == darwin and `vps` otherwise, and a 240-character task excerpt. These are application-specific choices, not defaults for other applications. Targeted verification: `python3 -m unittest control.test_plugin -v`, plus `git diff --check`; no deployment or LLM execution is needed for this unit-level change.
