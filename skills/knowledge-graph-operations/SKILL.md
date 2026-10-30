---
name: knowledge-graph-operations
description: Build, operate, and verify evidence-backed knowledge graphs and their agent and visualization interfaces. Use for graph-grounded agent profiles, cited corpus ingestion, property-graph modeling, read-only graph retrieval, idempotent refresh and rollback, interactive graph viewers, invisible or faint edges, disconnected notes, and displayed-versus-actual relationship checks. Covers the data-to-query-to-render pipeline without inventing relationships or expanding access.
---

# Knowledge Graph Operations

Treat corpus, graph, agent retrieval, and visual presentation as separate layers of one evidence system. Build only what representative questions require; repair the failing layer rather than compensating in another layer.

## 1. Discover scope and available interfaces

Identify the authorized project/profile, source corpus, graph store or export, ingestion entry point, runtime identity, and any viewer. Discover installed tools and existing build/test commands rather than assuming a vendor or live service.

- With a live database and supported driver/tool, inspect schema and representative read queries.
- With a local graph export only, inspect its nodes/edges and provenance offline; mark database authorization and live retrieval unverified.
- With a running viewer and browser tools, inspect its served payload and renderer state. Otherwise inspect local data/source and leave visual verification pending.
- For platform configuration, load the relevant platform skill first (`hermes-agent` for Hermes). Graph work does not authorize changes to other profiles.

Defaults: read-only discovery; preserve source documents and existing relationships; keep private viewers local-only; retain intentional filters; no new framework, embeddings, or inferred links unless evidence establishes the need.

Deliverable: authorized scope, available inspection path, and the layer being built or repaired.

## 2. Establish the evidence and acceptance contract

For a new graph-grounded agent, write 3–5 representative questions before designing the ontology. Derive minimal labels, relationships, and properties from those questions. A useful baseline is Source → Section → domain entity, with explicit support/dependency relationships and separately labeled decisions.

Capture authoritative source URL, title, retrieval date, and content hash. Separate sourced facts, cross-source synthesis, and implementation decisions. Keep the durable corpus outside the system prompt.

For an existing viewer, count nodes, edges, components, and degree-zero nodes from the payload actually served. Trace visibility predicates, sampling, category filters, opacity, width, selection, and camera state.

| Finding | Work at this layer |
|---|---|
| Required evidence absent from corpus | Source acquisition and provenance |
| Evidence present but missing or malformed in graph | Scoped construction/ingestion |
| Graph has evidence but agent misses it | Read query/tool path and evaluation |
| Payload has edges but viewer suppresses them | Shared visibility/filter logic |
| Edges render but remain difficult to see | Contrast, geometry, and camera calibration |

An empty-looking screenshot does not establish missing relationships; an orphan note is not automatically an error.

## 3. Build and refresh the graph deterministically

Use a rerunnable loader with uniqueness constraints, stable namespaced IDs, idempotent node/relationship upserts, mutable-property updates, and an import/version identifier. Prefer the existing driver or import mechanism; a controlled corpus does not require a framework.

Rerunning unchanged inputs must preserve counts and relationships. Scope rollback to loader-owned entities and relationships. Never remove shared nodes merely because an imported relationship points to them.

Use relationship and text queries first. Add embeddings, GraphRAG, or temporal memory only when representative evaluations demonstrate a retrieval gap. Do not infer semantic support from keyword coincidence.

Detailed agent construction: `references/agent-grounding-workflow.md`.
Concrete implementation and guarded rollback examples: `references/neo4j-hermes-pattern.md`.

## 4. Expose a bounded agent retrieval interface

Separate administrative ingestion authority from runtime access. Normal agent operation should expose schema inspection and parameterized reads, with read-only enforcement at the database role/tool boundary—not merely in a prompt. Treat generated query text as untrusted input.

With authorization to test this boundary, use a harmless uniquely identified write probe, require denial, and verify zero residue. If it unexpectedly succeeds, stop normal use and report the failed boundary; do not silently broaden access or claim read-only safety.

Run the original questions through the actual agent tool path and require traceable citations. A successful import or direct database query alone does not prove the agent works.

## 5. Make graph views legible without changing knowledge

Change the smallest shared rendering function. For small graphs, show existing edges by default rather than silently sampling. For dense graphs, expose filtering/sampling explicitly and display shown-versus-total counts. Preserve intentional filters and useful selection emphasis.

Calibrate width, opacity, category colors, background contrast, and the default camera together. Historical scene values are examples, not universal design tokens. Never generate extra edges just to make the picture appear connected.

Rebuild the existing bundle and reload the served application. Test the real shared visibility function rather than a copied implementation.

Detailed diagnostic procedure: `references/visualization-workflow.md`.
Calibration case and regression checklist: `references/edge-legibility.md`.

## 6. Verify the complete changed path

Leave runnable checks appropriate to the work performed:

- Graph integrity: expected bounds, unique stable IDs, section-to-source links, and representative cited multi-hop results.
- Ingestion: unchanged-input rerun is idempotent; rollback ownership is documented.
- Runtime authority: denied write with zero artifacts and actual agent-path answer checks.
- Rendering: default view, selection/deselection, intentional filters, and displayed-versus-payload edge counts.
- Perception: screenshot at default camera, plus exercised zoom and drag. Test mobile separately when requested.

A passing unit test, clean console, or nonzero rendered-edge count does not prove visible contrast or that every edge is unoccluded. State which checks were not possible; never substitute historical counts or URLs for current evidence.

## 7. Deliver an operational handoff

Report:
1. Changed layer and exact scope, including preserved source knowledge.
2. Evidence and verification actually completed.
3. Current entry point and commands for ingest, verify, refresh, and scoped rollback where applicable.
4. Remaining orphans, retrieval gaps, access limitations, or untested interactions.

Keep research notes, scripts, and operating instructions in the authorized project so a fresh session can resume without chat history.

## References

- `references/agent-grounding-workflow.md` — full graph-grounded profile workflow and pitfalls.
- `references/neo4j-hermes-pattern.md` — concrete source map, schema, ingestion, authorization, and verification pattern.
- `references/visualization-workflow.md` — full data-to-render troubleshooting workflow.
- `references/edge-legibility.md` — historical calibration example and reusable checks.

## Related boundaries

Use research skills for source acquisition, database design skills for general schemas, RAG architecture for measured hybrid-retrieval needs, and application lifecycle skills for deployment. Experiment dashboards belong in `experiment-operations`; rendering a knowledge graph does not by itself authorize experiment execution.
