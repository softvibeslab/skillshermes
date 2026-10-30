---
name: knowledge-graph-visualization
description: Diagnose and improve interactive knowledge graph visualization. Use for invisible connections, faint edges, apparently disconnected notes, 3D brain legibility, graph rendering filters, and validating displayed versus actual relationships without altering source knowledge.
---

# Knowledge Graph Visualization

Repair the presentation of existing knowledge before changing its substance. Scope: interactive graph viewers and their data-to-render pipeline, not corpus ingestion or speculative relationship generation.

## 1. Establish scope and inspect the available application

Use the authorized project and its existing viewer. Discover its data endpoint or local export, renderer source, build command, and available browser tools. Prefer the running browser plus its served payload; if unavailable, inspect local data and source and explicitly leave visual verification pending. Do not expand into other projects or private note stores.

Defaults: preserve source documents and relationships; retain existing intentional filters; keep private viewers local-only; add no rendering dependency when existing settings suffice.

## 2. Separate data from presentation

Count nodes, edges, connected components, and degree-zero nodes from the payload actually used by the viewer. Then trace shared edge-visibility logic and callers, including sampling, opacity, width, category colors, selection, and camera state.

Classify the symptom before editing:
- Missing in the payload: investigate data construction within authorized scope.
- Present but suppressed: fix visibility logic.
- Rendered but hard to see: calibrate contrast and geometry.

Do not infer missing data from an empty-looking screenshot. Orphan notes are not necessarily errors.

## 3. Make the smallest shared correction

When the user requests visible connections, prioritize legibility over decorative minimalism. On small graphs, show every existing relationship by default rather than silently sampling. Preserve useful selection emphasis and deliberate user filters. For dense graphs, use an explicit filtering or sampling mode with displayed-versus-total counts.

Tune line width and opacity against the actual background and initial camera position. Values are scene-dependent, not universal tokens. Do not add inferred edges just to make the picture look connected.

## 4. Verify both behavior and perception

- Leave one small runnable regression check for changed visibility logic.
- Rebuild the served bundle using the existing project command and reload it.
- Inspect live renderer state and displayed versus payload edge counts.
- Visually inspect a screenshot at the default view; adjust if lines remain illegible.
- Exercise selection/deselection, zoom, and drag before claiming those interactions work. Test mobile separately when requested.

A clean console, passing unit test, or nonzero edge count alone is not proof of visual legibility. Distinguish rendered edges from edges actually unoccluded in a particular camera view.

## 5. Deliver evidence briefly

Report the correction, what verification actually passed, the current entry point, and remaining unconnected notes or untested interactions. Never reuse historical counts or URLs as current evidence without checking.

## Reference

See `references/edge-legibility.md` for a concrete calibration example and a reusable regression checklist.
