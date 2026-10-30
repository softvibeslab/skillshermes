# Facilitated workshop dashboard on an existing static app

Use this pattern when a project already has a planning/dashboard module and the user approves a workshop MVP after reviewing users, outcomes, sections, data, and scope.

## Minimal implementation pattern

1. Read the durable project context and existing workshop flow before editing.
2. Reuse the current module and persistence; do not create another app, backend, or data model unless collaboration is explicitly required.
3. Preserve unrelated dirty work, especially in shared stylesheets. Limit edits to the workshop component, additive styles, and one small check.
4. Add only missing decisions: expected outcome, one use case, first mission, role boundaries, handoffs with owner/result/SLA, KPI dictionary, and closing checklist.
5. Persist new fields through the existing local state/localStorage merge so old browser state remains compatible.
6. Label unproven baseline/current values **Sin datos**. Never present demo or aspirational values as evidence.
7. Scope readiness precisely. A three-field check means **Definición base completa**, not “piloto listo.” Trim text inputs before counting them.
8. Describe output honestly: without a consolidated export, call it a checklist or same-board record, not an exported package.

## Small runnable check

When there is no UI test runner, leave one dependency-free source smoke script asserting required section labels, stages, persisted fields, and accessibility markers. Name it honestly as a **source smoke check**; it complements rather than replaces typecheck, build, and browser verification.

Verification sequence:

1. Run the smoke script before implementation and confirm the expected failure.
2. Implement the minimum change.
3. Run smoke check, typecheck, static build, and `git diff --check`.
4. Open the workshop module in a browser.
5. Fill outcome, use case, and mission; verify the scoped readiness label.
6. Reload and verify persistence.
7. Inspect layout for overlap, clipping, small text, and weak contrast.
8. Run spec review before quality review; correct important findings and re-review.

## Boundaries

Skip multiuser sync, backend APIs, exports, voting, timers, gamification, and integrations until proven necessary. Local browser persistence is enough for a single-facilitator MVP; centralize only when multiple operators need shared authoritative state.
