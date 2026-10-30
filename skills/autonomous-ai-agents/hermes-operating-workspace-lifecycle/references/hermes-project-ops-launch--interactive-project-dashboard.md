# Interactive project dashboard pattern

Use when a project needs action-taking, not just docs: team roles, owners, tasks, subtasks, content, rituals, and AI/Hermes operating prompts in one place.

Known-good lazy shape:

- Create `dashboard/index.html` as a single-file static dashboard.
- No backend at first. Use `localStorage` for edits and JSON export/import for backups.
- Include:
  - KPIs: total progress, open tasks, deliverables, blockers.
  - Kanban: Backlog, Doing, Review, Done, Blocked.
  - Task fields: title, area, owner, status, subtasks, notes/evidence.
  - Team view: member role, links, strengths/superpowers, owned work.
  - Plan view: tasks grouped by area with step-by-step subtasks.
  - Content calendar: content type, owner, idea, status.
  - AI/Hermes view: relevant skills/tooling map and a project prompt.
  - Rituals: weekly planning, build review, wins/pipeline, async check-in.
- Add `scripts/open_dashboard.sh` with `open "<workspace>/dashboard/index.html"` on macOS.
- Add a short `DASHBOARD_INTERACTIVO.md` with usage instructions.

When to upgrade:

- Keep it static while one person coordinates or the team can export/import JSON.
- Add Google Sheets/Drive sync when multiple users need shared state.
- Add a backend only when concurrent editing, permissions, or audit history becomes necessary.

Softvibes/AgenticOS example fields:

- Areas: Estrategia & Oferta, Growth & Eventos, Ventas & Partnerships, Contenido & Producción, Tech / Hermes / AI, Comunidad / Skool, Operaciones.
- Team mapping: Vivi = growth/eventos/comunidad; Omar = marketing/producción/edición/AI; Chris = ventas/workflows/video AI/HeyGen/Premiere; el operador = tech/Hermes/producto/liderazgo.
- Keep copy in natural Mexican Spanish, practical and action-oriented.
