# Local read-only operations dashboard pattern

Use this pattern when a user needs a local dashboard over CLI-driven systems such as Hermes profiles, sessions, cron jobs, or Kanban.

## Minimal architecture

- One dependency-free Python server using `ThreadingHTTPServer`.
- One static HTML file with embedded CSS/JavaScript.
- A read-only `/api/state` endpoint.
- Browser polling every 10 seconds; cache server-side collection for the same interval.
- Bind to `127.0.0.1` until authentication is added.

This is the first useful rung: it proves the information architecture and live data flow without adding a frontend framework, database, websocket stack, or deployment system.

## Safe collection rules

1. Execute only fixed, hard-coded CLI commands. Never accept command names or arguments from the browser.
2. Prefer narrow commands (`profile list`, `sessions stats`, `cron list`, `kanban list`, `insights`) over broad diagnostic commands that may print credentials or provider state.
3. Return only fields required by the UI. Do not proxy raw CLI output.
4. Add subprocess timeouts and treat failures as partial/unavailable data, not as permission to expose stderr wholesale.
5. Keep the API read-only until authorization, validation, and audit logging exist.

## Parsing human-readable CLI output

Human tables often align columns with variable whitespace. Do not parse them by fixed offsets or `split` counts when names can be long.

Prefer one of these, in order:

1. Native JSON output, when available.
2. A stable semantic anchor such as a known status token (`running|stopped`) in a regex.
3. A narrow label regex for scalar values (`Sessions:\s+([\d,]+)`).

After writing a parser, verify it against long names and compare parsed row count with the visible CLI total. A parser that silently drops long rows is worse than a loud failure.

## Dashboard information architecture

For an agent-operated software factory, a practical four-area matrix is:

1. Control/KPIs — health, agents online, sessions, tool calls, ready work, scheduled jobs, channel activity.
2. Tasks/profiles — current Kanban rows, status, assignee, search/filter.
3. Agents — profile name, model, gateway state, specialization/status.
4. Projects/growth — project portfolio plus the value chain: sales → research → strategy → content → software → optimization.

Keep strategy/project projections visibly labeled as draft or manually maintained until a real CRM, content system, and finance source are connected. Do not present decorative estimates as live telemetry.

## Verification

- Open the app through its HTTP URL, not only `file://`.
- Confirm each navigation area renders.
- Confirm live counts match source commands, especially profile totals and long profile names.
- Exercise one search/filter.
- Refresh data after the server is running and check the browser console from a clean buffer.
- Inspect the primary desktop viewport for overflow, card wrapping, contrast, and tiny secondary text.
- If a restart briefly caused a fetch error, clear the console, refresh once against the stable server, and verify no new errors.

## Upgrade thresholds

Add a framework only when state or routing complexity warrants it. Add WebSockets only when 10-second polling is materially too slow. Add authentication before binding beyond localhost or adding write actions. Add persistent storage only when the dashboard owns data rather than observing existing systems.
