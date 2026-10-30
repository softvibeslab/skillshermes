# Hermes CLI Matrix Dashboard Reference

Condensed implementation notes for a local Hermes operations dashboard. Re-check `--help` before relying on mutation flags because CLI contracts can evolve.

## Useful read commands

```text
hermes profile list
hermes sessions stats
hermes insights --days 7
hermes cron list --all
hermes kanban list
```

Prefer these narrow commands over `hermes status --all`; the broad status view can include credential/configuration details that a dashboard neither needs nor should process.

## Stable parser anchors

- Profiles: profile-name token + model token + `running|stopped`.
- Tasks: `t_<hex>` + status + assignee + remaining title.
- Board: `Board: <slug>` header.
- Cron count: occurrences of `[active]`.
- Session/insight values: named labels followed by comma-formatted integers.
- Strip ANSI escape sequences before every parser.

Do not parse profile tables by splitting on two or more spaces. Long profile names can collapse visual column spacing; anchor the regex on the status token instead.

## Scoped writes

Typical task creation:

```text
hermes kanban create <title> --assignee <profile> --created-by hermes-matrix --json
```

Typical completion:

```text
hermes kanban complete <task-id> --result <short-result>
```

Never pass browser input through a shell. Build an argv list after validation.

## Business metrics file

A single JSON document is sufficient for manual metrics and editable project progress:

```json
{
  "metrics": {
    "leads": 0,
    "qualified": 0,
    "proposals": 0,
    "closed": 0,
    "revenue": 0,
    "contentPlanned": 0,
    "contentPublished": 0,
    "reach": 0
  },
  "projects": [
    {"name": "Example", "type": "Product", "phase": "Build", "progress": 50}
  ]
}
```

Compute conversion in the UI from `closed / leads`; do not store redundant derived values.

## Minimal verification

- API state returns at least one profile and the expected top-level collections.
- Invalid one-character task title returns HTTP 400 and creates nothing.
- Business save returns 200 and the JSON file reads back with the same values.
- Create-task dialog lists `manual` plus discovered Hermes profiles.
- Completing a task requires a browser confirmation.
- Browser console is clean after the final server start.
