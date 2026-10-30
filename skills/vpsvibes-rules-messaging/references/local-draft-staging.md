# Local draft staging: contract and verification reference

Scope: local implementation only; no deployment or SSH. This is historical
verification evidence, not a claim that the current workspace or production
matches it.

## Locate and inspect

Workspace used: `/Users/USERNAME/Documents/SoftvibesLab/vpsvibes-planning/implementation`.
Original sources: `app.py`, `index.html`, `memory_observer.py`,
`profile-inventory.py`, `README.md`. Added `rules.py` and `test_rules.py`;
`app.py` dispatches `/api/rules` to `RulesAPI` and initializes via `from_env()`.
Read those sources for actual configuration/authentication and directory schemas;
do not infer environment-variable names from this note.

`app.py` reads index.html at import time. Restart/reimport for fresh markup.
Keep the existing monitoring/collector separation and loopback binding.

## Contract exercised

- Rule fields: title, profile, scope, target_id, type, spec.
- Types: message, preference, resource_alert, resource_policy.
- Updates: PUT `/api/rules/<id>` with numeric version; stale writes return 409.
- Preview: `/api/rules/preview`; explicit audience, no delivery or execution.
- CRUD verification: persistence across store reopen, archive, duplicate, audit.
- Message fixture includes `<img src=x onerror=alert(1)> Hola` to test safe text
  handling; scheduled_at `2027-01-01T10:00:00-06:00`, timezone
  `America/Mexico_City`.
- Concurrent check: two updates from version 1, sorted statuses `[200, 409]`.
- UI acceptance markers: `id="rules"`, `id="rulesEditor"`,
  `id="rulesFields" disabled`, `src="/rules-ui.js"`; serve `/rules-ui.css` too.
  New JS uses textContent, no innerHTML. Marker tests are not browser smoke.

## Verification boundary at handoff

Six backend tests passed: CRUD/persistence/audit, invalid inventory and version
validation, pure preview, schedule/timezone/DST, fail-closed security plus legacy
endpoints, rule type/scope/unknown-field validation.

Two tests were subsequently added for UI assets/locked editor and concurrent
updates, but execution was not verified. The next test command was denied;
this is not evidence of a test assertion failure. UI JS/CSS, native editor,
browser/fake-proxy smoke and staging README were still outstanding.

On a newly authorized continuation, inspect current files and test class names,
then run the complete suite rather than relying on the historical six passes.
Finish native UI and verify its actual interactions before calling the delivery
complete. Never resume a denied command merely by changing its spelling.
