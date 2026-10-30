# AgenticOS course dashboard + resources wiki pattern

Use this reference when launching a course/community project that needs a practical operating dashboard, not just markdown docs.

## Proven shape

Workspace example:
`/Users/USERNAME/Documents/SoftvibesLab/AgenticOS-Skool`

Useful files:
- `dashboard/index.html` — single-file interactive command center.
- `dashboard/resources.json` — seed data for resource/wiki cards.
- `RESOURCES_WIKI.md` — markdown copy of curated repos/sites/tools.
- `COURSE_CREATION_SYSTEM_PLAN.md` — implementation plan for turning research into course assets.
- `DASHBOARD_INTERACTIVO.md` — operator instructions.

## Dashboard sections that worked

- Kanban: Backlog, Doing, Review, Done, Blocked.
- Plan paso a paso: tasks/subtasks grouped by area.
- Equipo: roles, links, superpowers, owned tasks.
- Contenido: content ideas with owner/status.
- Hermes + Skills: map of useful skills and when to use them.
- Recursos / Wiki: searchable/filterable repository of tools, repos, MCPs, frameworks, and their relationship to course creation.
- Rituales: weekly/daily operating cadence.

## Resource/wiki card schema

Each resource should answer:
- `name`
- `url`
- `type`
- `area`
- `value` — what it contributes.
- `use` — how it relates to creating the course.

This prevents tool-hoarding. A resource that cannot explain what deliverable it accelerates stays in the wiki, not the operational stack.

## Course creation priority ladder

1. Design first: Community Canvas, curriculum benchmark repos, course-builder-style research synthesis.
2. Production second: course creation tools, YouTube transcripts, humanizer, slides/video helpers.
3. Community third: Skool setup, onboarding, rituals, pricing, engagement metrics.
4. Automation last: Skool MCP/API only after auth and read-only tests are validated.

## Skool MCP pitfall

Treat Skool MCP/API clients as a spike first:
- Start in read-only/reporting mode.
- Document auth/cookie/API requirements.
- Verify rate limits and fragility before enabling writes.
- Do not automate posts/member changes until the user approves exact actions.

## Lazy implementation note

A static HTML dashboard with localStorage + JSON export is enough for early action. Add backend or realtime collaboration only when the team actually needs simultaneous editing.
