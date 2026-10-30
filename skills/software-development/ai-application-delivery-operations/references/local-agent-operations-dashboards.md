---
name: local-agent-operations-dashboards
description: Build secure localhost dashboards over agent CLIs for live observability, scoped task actions, and editable business metrics without adding dependencies.
version: 1.0.0
created_by: agent
metadata:
  hermes:
    tags: [dashboard, observability, localhost, cli, kanban, operations]
---

# Local Agent Operations Dashboards

Use this skill when building a local web dashboard that reads operational state from an agent CLI and optionally exposes a small set of explicit mutations.

## Default architecture

Stop at the smallest rung that works:

1. Use a single static `index.html` with embedded CSS/JS.
2. Use Python stdlib `ThreadingHTTPServer` for the local API and static files.
3. Bind to `127.0.0.1`, never `0.0.0.0`, unless authentication is added first.
4. Poll a consolidated `/api/state` endpoint every 10 seconds.
5. Cache CLI-derived state server-side for the same interval so every browser refresh does not spawn redundant processes.
6. Persist manually entered business metrics in one local JSON file.

Do not add React, a database, a framework, WebSockets, or a chart dependency until the dashboard demonstrably needs them.

## Discovery before implementation

Read the actual CLI help and inspect representative output before writing parsers:

- profile/status listing
- session statistics and insights
- scheduled jobs
- task/Kanban list
- mutation subcommands and their validation rules

Avoid broad diagnostic commands when narrower commands expose the required state. Broad status output may include configured credential values or other sensitive details.

## Safe CLI adapter

- Commands must be fixed server-side argument arrays, never shell strings supplied by the browser.
- Use `subprocess.run([...], capture_output=True, text=True, timeout=N, check=False)` without `shell=True`.
- Strip ANSI sequences before parsing.
- Parse variable-width tables by stable semantic anchors such as IDs and status tokens, not by fixed column offsets or repeated-space splitting.
- Keep reads and writes separate. Read helpers may return normalized text; write helpers must inspect the exit code and return a sanitized error.
- Invalidate the state cache after every successful mutation.

## Scoped mutation API

Expose only operations the UI actually needs, for example:

- create a task with validated title and assignee
- complete a task by a strict task-ID regex
- save non-negative business metrics
- update project progress constrained to `0..100`

At the HTTP boundary:

- cap request body size
- require JSON objects
- allowlist keys
- validate strings, IDs, profile names, numeric ranges, and list lengths
- truncate user-provided result/reason text to a small maximum
- return `400` for validation, `404` for unknown routes, and `502` for CLI failures
- require an explicit browser confirmation before completing or otherwise closing work

## External engineering connectors

For GitHub, use the authenticated `gh` CLI as the credential boundary and fetch repository metadata with one GraphQL query. Do not copy tokens into the app or call every repository separately. Cache GitHub independently for about 60 seconds, use GraphQL `totalCount` for issues/PRs, map flagship projects to explicit `owner/repo` names, and represent missing status checks as `NONE` rather than success. Keep the connector read-only until explicit mutation controls are requested.

See `references/local-agent-operations-dashboards-local-agent-operations-dashboards-github-graphql-dashboard.md` for the one-call query, normalized schema, CI semantics, UI pattern, and verification steps.

## UI structure

For a software-factory/agency operating system, five views are usually enough:

1. Control and KPIs: agents online, sessions, tool calls, ready tasks, scheduled jobs, channels.
2. Tasks and profiles: searchable current board, create task, explicit completion action.
3. Agents: profile, model, and live/stopped state.
4. Code and GitHub: repository activity, open issues/PRs, default branches, last push, and CI state.
5. Projects and growth: sales funnel, revenue, content output, project progress, and operating projections.

Treat marketing as a value chain, not a decorative feature grid: demand → research → narrative → content production → software/product → learning.

Use native `<dialog>`, `<form>`, `<input type="number">`, and `<select>` before introducing UI libraries. Escape every string inserted through `innerHTML`.

## Community intelligence CRUD

For dashboards that import group histories, detected signals, consented contacts, and proposed matches, use the privacy-safe SQLite model in `references/local-agent-operations-dashboards-community-intelligence-crud.md`. The key defaults are: imported signals start unverified, generated matches start as drafts, and contacts are never inferred from phone numbers.

## Verification

Leave one runnable check for non-trivial logic and verify end to end:

1. Start the server as a tracked background process.
2. Open the local URL in a browser.
3. Confirm live state renders after the first poll.
4. Test navigation and search.
5. Open create/edit dialogs without performing destructive mutations.
6. Save business metrics and read the JSON back.
7. Probe one invalid request and verify `400` without side effects.
8. Check browser console after server restarts; clear transient restart errors before the final pass.
9. Visually inspect dense tables and responsive layouts for clipping, contrast, and overlap.

## Security ceiling

`localhost` is the security boundary for the MVP. Add authentication, CSRF protection, HTTPS, audit logging, and a real datastore before exposing the service to a LAN, tunnel, or public host.

## Reference

See `references/local-agent-operations-dashboards-local-agent-operations-dashboards-hermes-cli-matrix.md` for a concrete Hermes-oriented command map, parser anchors, and verification checklist.
