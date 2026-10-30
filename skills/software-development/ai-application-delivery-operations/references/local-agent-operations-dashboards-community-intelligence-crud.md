# Community Intelligence CRUD Pattern

Use this extension when a localhost operations dashboard manages imported community/group data, detected signals, consented contacts, and proposed matches.

## Minimal data model

Four entities are enough for an initial operating loop:

- `groups`: source communities and their operating status.
- `signals`: imported demand, supply, events, or capabilities.
- `contacts`: manually approved people or organizations.
- `opportunities`: candidate bridges/matches with evidence and next action.

Use stdlib SQLite when the records are relational, searchable, and edited concurrently by HTTP handlers. Keep one database file beside the dashboard; do not add an ORM.

## Safe import defaults

- Import groups with a stable `source_key` and `INSERT OR IGNORE` so restarts are idempotent.
- Import detected signals as `needs_review`, never `active`.
- Import generated opportunities as `draft` hypotheses.
- Do **not** infer or create contacts from phone numbers found in messages.
- Replace phone-like senders with a neutral label such as `Contacto no identificado`.
- Redact phone numbers in imported summaries; retain the original source files as the controlled evidence layer.
- Preserve source group and date so a human can verify freshness.
- Treat URLs containing long numeric product IDs separately from phone numbers when testing redaction; a generic “eight digits” assertion creates false positives.

## Consent-aware workflow

Recommended states:

- signals: `needs_review → active → matched → expired/discarded`
- opportunities: `draft → verify → active → introduced → meeting → closed/discarded`
- contacts: explicit consent field plus `active/paused/archived`

A dashboard record is not permission to contact someone. Keep contact creation manual and require explicit approval of person, message, channel, and quantity before outreach.

## HTTP boundary

- Allowlist tables and fields; never interpolate browser-supplied identifiers into SQL.
- Use one SQLite connection per request under `ThreadingHTTPServer`.
- Cap JSON bodies and require JSON objects.
- Validate status enums and numeric ranges.
- Escape or assign user data with `textContent`, not `innerHTML`.
- Use stable server-side source keys for imported rows.

## Verification

Leave one small stdlib `unittest` that checks:

1. create, search, update, and delete;
2. rejection of an unknown field with HTTP 400;
3. idempotent seed import;
4. zero automatically imported contacts;
5. phone-like senders are neutralized;
6. the live `/api/stats` endpoint and one invalid request.

Before launching, check whether the documented default port is already listening. If occupied, choose another localhost port and update both the server default and README so the advertised URL matches reality.
