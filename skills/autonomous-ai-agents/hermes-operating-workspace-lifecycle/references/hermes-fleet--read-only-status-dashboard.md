# Read-only Hermes fleet status dashboard

## Scope and recovery

Use for local fleet inventory and update-readiness reporting, not fleet administration. Inspect an existing collector/dashboard before replacing it. Writes belong only in the report workspace. Do not invoke update, migration, doctor --fix, restarts, permission fixes, or profile edits as part of collection. Keep approval-sensitive commands out of diagnostic batches. A request to continue a read-only audit does not revive an earlier update authorization.

After an interrupted session, read the actual files, rerun permitted checks, and distinguish planned, created, and verified artifacts. A todo marked complete or an earlier assistant summary is not evidence of browser tests or file existence.

## Collection contract

- Record generation time, host scope, collection errors, source timestamps, and limitations. Do not reuse historical profile counts or release numbers as live facts.
- Use explicit config field allowlists; missing/inherited values remain unknown rather than false. Never dump whole config sections, MCP arguments, auth files, or environment values.
- Access-control reporting exports flags and counts, not user IDs. Distinguish explicit disk declarations from effective runtime policy, including environment overrides and config inheritance.
- Read session databases with SQLite read-only mode. Select aggregate metadata only, never messages. Missing DB, unsupported schema, and zero sessions must be distinguishable.
- State the window semantics: sessions started in seven days are not all activity in seven days; old resumed sessions are excluded. Cloned databases may duplicate totals. Missing cost data is not zero spend.
- Validate saved PID against live process identity and available profile/service evidence. Avoid classifying every Python PID as a gateway. Distinguish confidence levels if attribution cannot be proven.
- gateway_state.json is event state, not a heartbeat. Display its age; never promote an old connected state to current connectivity. End-to-end message delivery requires a separate authorized probe.
- Count symlinked skills with resolved-directory cycle detection. Label per-profile availability versus unique installed skills so shared libraries do not inflate a global unique total.
- Storage should name included categories and distinguish logical file bytes from physical/reclaimable space. Avoid following symlinks for size accounting.
- For log analysis, process a bounded tail locally; export dated aggregate counts/categories, never raw messages or traces. Label sample size, period, and exclusions; line counts are not incident counts.
- Compare installed version and Git state separately against a dated official release/source query. A cached behind-commits banner is not an update risk assessment. Do not fetch or modify local Git refs when a strictly read-only remote API lookup suffices.

## Dashboard shape

Prefer an existing compatible hub or a dependency-free static report. Include overview, searchable/filterable profile table, profile detail, channels with evidence age, sessions/usage caveats, cron/MCP/skills metadata, resource footprint, prioritized findings, and staged update/rollback recommendations. Escape all strings at the HTML boundary; embedded JSON must safely escape script-closing characters. Support unknown and empty states, keyboard focus, readable mobile overflow, and visible snapshot time.

Security findings are review items, not silent fixes. Public-access declarations require intent confirmation; permissive secret-file modes warrant remediation approval. Do not copy secrets into the report to substantiate either finding.

## Update-readiness recommendations

Require fresh runtime and source backups, archive integrity and restore checks, reviewed source customizations, a clean isolated candidate, tests, migration validation on disposable state, and explicit activation approval. Preserve the exact previously running gateway set. An old backup is evidence of an old state, not coverage of changes since then. Never change GitHub visibility merely because private is the default recommendation; obey the requested visibility and keep secrets/runtime backups out of Git regardless.

## Verification and delivery

Leave a runnable minimal check for the collector's non-trivial parsing/classification, including malformed/missing data and secret sentinel exclusion. Run it. Verify generated file existence and schema, reconcile displayed totals with the snapshot, and test filters/detail/empty states and mobile layout in a browser when available. Check for console errors and unexpected external requests. A local dashboard should not need analytics, CDNs, or remote fonts.

Deliver the exact local path and refresh command only after verifying them. Report verified tests separately from untested capabilities. Do not claim no external requests or successful UI tests merely from reviewing the source. Keep the report private; public deployment needs separate approval even after secret filtering.
