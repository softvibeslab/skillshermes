# Local simulation dashboard recipe

Use when a simulator already exposes a frontend and run-history API but lacks an experiment-operations view.

## Placement

Place a dependency-free page under the host frontend's public/static directory: `index.html`, `styles.css`, `app.js`, plus optional bundled `seed.md` and `prompt.md`. This reuses the existing server and avoids a second app.

## State

Use one versioned object containing experiment ID, title, seed, prompt, selected run ID, notes, and update timestamp. Persist under a namespaced browser-storage key. Notes need ID, timestamp, type, round, body, and optional run ID.

## API behavior

- Read history/status from the simulator's existing endpoint.
- Poll about every 15 seconds and refresh on demand.
- Suspend polling while the page is hidden.
- Show disconnected state without clearing cached runs or authored inputs.
- Never call a paid start/run endpoint from monitoring code.

For MiroFish-style backends, inspect the live API first; a common history surface is `/api/simulation/history`.

## Export contract

Project JSON includes full state, schema version, export timestamp, and useful cached run metadata. Markdown downloads preserve seed and prompt separately. CSV correctly quotes timestamp, type, round, run ID, and note body.

## Initialization

1. Cache and validate required DOM elements.
2. Load versioned browser state.
3. If absent, fetch bundled seed/prompt defaults.
4. Attach listeners.
5. Render.
6. Fetch history and begin polling.

A missing element should identify its selector instead of failing as `null.addEventListener`.

## Verification

Use the host runtime and standard library only. Check file presence, HTML/JavaScript ID consistency, unique expected actor IDs, round/cost caps, hypothesis guardrails, and parseable history JSON when the backend is available. Run the host build, then verify edit/reload persistence, imports/exports, run selection, log CRUD, connection state, and readable contrast.

## Upgrade thresholds

Move from browser storage to backend persistence only for collaboration, auditability, cross-device access, or browser-profile-loss protection. Replace polling with server events or WebSockets only when latency or request volume is measurably harmful.
