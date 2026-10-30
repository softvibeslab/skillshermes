---
name: collaboration-board-analysis
description: Analyze large visual collaboration boards (Miro, FigJam, whiteboards) as decision systems using content, geometry, hierarchy, and visual evidence.
version: 1.1.0
metadata:
  hermes:
    tags: [whiteboard, miro, figjam, audit, information-architecture, product-strategy]
---

# Collaboration Board Analysis

Use this skill when asked to inspect, summarize, audit, or restructure a large visual collaboration board. The goal is not to narrate every sticky note; it is to identify the current thesis, evidence, decisions, readiness, and information-architecture problems.

## Core workflow

1. **Resolve the canonical board identifier.** Invitation URLs may redirect to a normal board URL. Resolve the redirect before calling board APIs.
2. **Verify access without writing.** Read board metadata, membership/role, and a small item sample. Do not create a test object unless the user explicitly asks to validate writes.
3. **Fetch the complete dataset.** Follow the API's cursor links until exhausted. Do not assume an `offset` argument is honored just because a wrapper exposes it.
4. **Fetch separate object families.** Some APIs return connectors, comments, groups, or tags from separate endpoints. Do not infer “zero connectors” from an items-only response.
5. **Normalize content.** Strip HTML while retaining item ID, type, parent/frame, coordinates, dimensions, timestamps, and creator/modifier metadata.
6. **Inventory before interpreting.** Count object types, frames, titled/untitled frames, parented/orphaned objects, connectors, empty placeholders, duplicates, unsupported objects, and spatial bounds.
7. **Map spatial structure.** Identify dense clusters, outliers that distort fit-to-content, isolated decision areas, and the likely reading path. Geometry is evidence when rendered screenshots are unavailable.
8. **Separate content classes.** Distinguish:
   - current canonical material;
   - derived summaries;
   - historical versions;
   - templates/examples;
   - unrelated projects;
   - empty visual scaffolding.
9. **Audit the operating model.** Extract actors, phases, dependencies, deliverables, KPIs, owners, dates, evidence, decision gates, risks, and stop conditions.
10. **State readiness clearly.** Use `GO`, `EXAMPLE_SLACK_ID GO`, or `NO-GO`, and list the minimum evidence required to change that state.
11. **Recommend the smallest useful restructuring.** Prefer a navigation/cockpit layer over rebuilding the board. Preserve historical material in an archive area unless deletion is requested.
12. **Rebuild safely when explicitly requested.** Copy and verify the original board before destructive cleanup; then follow `references/collaboration-board-analysis-miro-board-restructuring.md` for dependency-aware deletion, frame construction, and post-write verification.
13. **Report write scope.** State exactly what changed, what was backed up, and any legacy object types that remain.

## Analysis lenses

### Strategic coherence

- What problem is being solved?
- For whom?
- What is the smallest testable intervention?
- What is explicitly out of scope?
- Does the experiment measure the promise being made?
- Are vision, MVP, and validated evidence being conflated?

### Operational readiness

Every action should have owner, due date, state, definition of done, and evidence.
Every metric should have baseline, target, current value, source, window, and owner.
Every decision should have question, options, criterion, deadline, decision-maker, and rationale.

### Information architecture

Measure whether a newcomer can answer within two minutes:

1. What are we validating?
2. What is out of scope?
3. What blocks progress?
4. Who owns each blocker?
5. What evidence exists?
6. What decision is required now?

If not, recommend a minimal cockpit:

- `00 — Current decision`
- `01 — Charter and scope`
- `02 — Readiness / blockers`
- `03 — Test or pilot execution`
- `04 — Metrics and Go/No-Go`
- `05 — Decisions and next actions`
- `90 — Archive / research`

## Pitfalls

- A successful list/read call validates authentication and read access, not write access.
- A wrapper's `list_resources` failure may concern optional MCP resource discovery while normal tools still work; validate the actual domain tools independently.
- Cursor APIs can silently return the first page repeatedly when callers vary only `offset`. Compare first/last IDs between pages.
- Items and connectors may paginate independently.
- Imported boards often have most objects created at one timestamp; treat this as a signal of bulk import, not ongoing collaboration.
- Repeated labels in matrices can be functional. Deduplicate only after classifying structural repetition versus duplicated strategy text.
- Do not attribute figures from templates or unrelated business examples to the active project.
- Do not claim a board has no flows solely because explicit connectors are absent; proximity and containment may encode the flow.
- Screenshots blocked by login modals are not grounds to stop if structured API data and geometry are available.
- Before destructive cleanup, create a board copy and verify its item total; a copy response alone is not sufficient proof of backup completeness.
- Delete container-owned objects through their container API: mind-map roots cascade descendants, and groups may need `deleteItems=true` for shapes that reject generic deletion.
- When creating children inside frames, Miro interprets coordinates relative to the parent frame's top-left; canvas coordinates can fail as outside parent boundaries.
- Sticky notes have fixed aspect ratio in raw REST writes: send only width or only height, and validate raw-API color names rather than trusting wrapper aliases.
- A failed partial rebuild can leave an orphan summary or frame. Remove the newly created frame before retrying, then verify all new text/cards have parents.

## Verification

Before finalizing:

- Confirm fetched count matches the API-reported total.
- Confirm invite URL and API board ID refer to the same board.
- Confirm connector totals separately when supported.
- Cross-check at least one canonical content cluster against item coordinates and metadata.
- Reconcile subagent or script findings with raw endpoint semantics before repeating them.
- Label inferred conclusions as inference, especially when a board mixes current work with templates.

## Provider notes

- See `references/collaboration-board-analysis-collaboration-board-analysis-miro-api-analysis.md` for Miro-specific pagination, token handling, and extraction guidance.
- See `references/collaboration-board-analysis-collaboration-board-analysis-miro-board-restructuring.md` for safe backup-first rebuilds, object-dependency deletion, parent-relative layout, and verification.
