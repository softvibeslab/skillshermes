---
name: experiment-operations
description: Build lightweight control surfaces for editing experiment inputs, monitoring runs, recording human decisions, and exporting auditable snapshots. Use for prompt experiments, synthetic simulations, model evaluations, and product pilots.
---

# Experiment Operations

Build the smallest operator surface that keeps an iterative experiment understandable without introducing another platform.

## When to use

Use when an operator repeatedly edits prompts, seeds, cohorts, hypotheses, or configuration; monitors run status; connects human observations to generated output; and needs downloadable snapshots. Skip it for a one-shot run whose files and CLI output are already sufficient.

## Design ladder

1. Reuse the experiment tool's UI and API.
2. If needed, add one static page to its existing frontend.
3. Use browser storage for a local single-operator lab.
4. Add backend persistence only for collaboration, cross-device access, auditability, or larger state.
5. Add real-time transport only when polling causes a measured problem.

## Read-only results dashboards

When the user explicitly asks for an intuitive HTML5 explanation of results, deliver a results-only view rather than the full operator contract below. Prefer one self-contained HTML file with embedded, sanitized snapshot data; it must work offline without a running simulator. State the snapshot time and make clear that it neither changes the experiment nor updates automatically.

Organize the view around the user's decision (for example, competing onboarding routes), not raw log chronology. Use plain-language labels, a compact comparison, visible uncertainty, and progressive disclosure for the original report. Separate generated report claims, verified execution facts, and human hypotheses. Before presenting a winner, compare the report against the original experiment requirements and the actual run status, completed/planned rounds, actions, and participant-level evidence. Missing measurements are unknown, not zero; partial synthetic runs do not establish real-world causal effects.

Keep credentials and environment values out of both visible content and embedded JSON. Checklist state may use localStorage, but must not mutate the frozen evidence. Leave one runnable browser smoke check for route controls, reload persistence if offered, startup errors, and mobile overflow; verify offline loading as well.

See `references/results-snapshot-evidence.md` for the BeGlobal × MiroFish case and delivery checklist.

## Minimum contract (editable operator surfaces only)

- Editable seed/input and prompt/configuration panels.
- Autosave with visible save status.
- Markdown import/export for authored text.
- Full JSON project export with schema version and timestamp.
- Run history/status from the existing API and active-run selection.
- Human log entries for observations, decisions, blockers, and next steps.
- CSV export of the human log.
- Clear separation among authored inputs, simulator state, generated findings, and human interpretation.

## Implementation

Prefer plain HTML, CSS, and JavaScript under the host frontend's public/static directory. Keep state in one versioned object and isolate storage, API, rendering, and export functions. Poll at a modest interval only while visible. Show connection state without turning temporary API failure into data loss.

Bundled seed and prompt files are first-run defaults. After edits, browser state remains authoritative until an explicit reset or import.

See `references/local-simulation-dashboard.md` for the concrete integration and verification recipe.

For multi-agent experiments, add an optional spatial projection only when it improves operator comprehension: fixed stages, one selectable avatar per agent, explicit visual states, and inspectable action history. Keep preview fixtures visibly separate from live data; prefer direct identity matching and label any order-based fallback as provisional. See `references/visual-agent-world.md` for the lightweight CSS pattern and verification checklist.

## Safety and evidence

- Never start a paid run from refresh, load, or monitoring code.
- Keep synthetic results labeled as exploratory hypotheses.
- Do not place private participant data in synthetic seeds.
- Never overwrite authored inputs because monitoring failed.
- Export before destructive reset or schema migration.

## Verification

Leave one runnable check for required controls, HTML/JavaScript ID consistency, expected unique actor IDs, round/cost caps, API reachability when the backend is active, and startup JavaScript errors. Run the host build and visually verify contrast, navigation, persistence after reload, imports/exports, run selection, and one log create/edit/delete cycle.

## Pitfalls

- Building a separate service when one static page suffices.
- Treating browser storage as collaborative or auditable persistence.
- Polling aggressively or while the tab is hidden.
- Scraping fragile host-UI DOM instead of consuming its API.
- Exporting results without the exact seed, prompt, notes, and selected run.
- Declaring the experiment complete because its dashboard is complete.
