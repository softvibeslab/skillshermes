# Upgrade preflight: approval routing and scoped skill synchronization

## Approval diagnosis

A denied command is not evidence that an approval dialog malfunctioned. Inspect the installed version's approval call path and configuration before attributing cause:

- Interactive approval can expire and return a denial. Read the configured timeout rather than hardcoding a value.
- A delegated operation may be rejected by subagent policy before any interactive prompt exists. Inspect the delegation helper and its callers (the investigated release used `_subagent_auto_deny` in `tools/delegate_tool.py`). Names and defaults are version-dependent.
- Distinguish user denial, expiry, and policy denial in the report. Preserve manual approval settings and do not bypass a denied operation through another execution path.

## Disposable skill-sync probe

1. Inspect the candidate's sync API and tests rather than guessing a function signature.
2. Launch the probe with `HERMES_HOME` pointed at a `TemporaryDirectory` before importing modules that resolve profile paths. Do not use a real profile as the fixture.
3. Add `.no-bundled-skills` to the temporary skills directory; include a sentinel custom skill.
4. Run candidate synchronization and assert the sentinel remains unchanged. Compare the resulting skill set to the candidate's documented essential-skill policy.
5. Run the candidate's focused skills-sync and profile-scope tests. Record the tested revision and exact commands in the upgrade workspace, not persistent memory.
6. Inventory affected production profiles read-only. If essential skills would be newly seeded into deliberately limited profiles, surface that delta and obtain approval before applying it. Do not silently patch upstream or remove opt-out markers.

Observed in the v2026.9.11 candidate: synchronization seeded `hermes-agent` despite `.no-bundled-skills`. Treat this as a release-specific observation to recheck, not a universal meaning of the marker.

## Independent readiness gates

- Dependency consistency: with uv available, `uv pip check --python <candidate-venv>/bin/python`; no need to add pip merely for this check.
- Focused tests: validate only the paths exercised, not the whole deployment.
- Backup: an archive or partial copy is not proof of recoverability; extract and validate the required state in isolation.
- Rollback: preserve both old source and runtime state; verify the restoration procedure before activation.
- Runtime: after authorized cutover, verify fresh service processes/logs and representative profile behavior.

Keep these statuses separate. After compaction or interruption, re-read the upgrade evidence and verify current state before repeating historical pass claims. A passing test subset never implies that production was updated or rollback validated.
