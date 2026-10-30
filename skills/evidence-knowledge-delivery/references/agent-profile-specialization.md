# Research-backed agent profile specialization

Use this recipe when turning a general agent profile into a domain expert from a source bundle.

## Boundary first

Treat these as separate deliverables and authorization scopes:

1. **Specialization:** profile identity, curated skills, research corpus, evidence map, and an offline smoke test.
2. **Integration:** credentials, MCP servers, databases, containers, ports, plugins, or paid services.
3. **Production activation:** writes, shared memory, public network exposure, scheduled jobs, and user-facing channels.

A request to create or explain a profile authorizes stage 1, not stages 2–3. “What next?” calls for the next smallest action and its prerequisites; it is not permission to provision infrastructure. A timeout or missing reply is not authorization for side effects.

## Minimal workflow

1. Inspect the target platform's native extension points before proposing adapters or forks.
2. Research supplied URLs using source priority: current code and schemas, first-party docs, release metadata, then community material.
3. Record URL, exact revision/date, observed facts, inferences, contradictions, and refresh targets.
4. Create a concise profile identity file that points to the canonical research instead of embedding the whole corpus in every prompt.
5. Install or select only the skills needed for the domain; avoid copying a full upstream catalog.
6. Run an offline smoke test proving the profile loads, follows its identity, and consults the intended skill/evidence map.
7. Report specialization as complete while naming external integrations as unverified until an E2E test succeeds.

## Integration gate

When integration is explicitly authorized:

- start read-only and least-privilege;
- bind development services to localhost unless broader exposure is requested;
- keep secrets in the profile's secret/env mechanism with restrictive permissions;
- use the platform's native plugin/provider/MCP interface rather than modifying its main loop;
- verify the exact path end to end: service health, protocol discovery, one harmless query, and agent-level invocation;
- distinguish “configured” from “connected and tested.”

## Neo4j × Hermes example

- Prefer Hermes' existing `MemoryProvider` lifecycle for persistent agent memory; do not rebuild the tool loop or context compressor.
- Prefer the official Neo4j MCP server as the first operational bridge, initially read-only.
- Keep knowledge graph, agent memory, GDS projections, and metadata catalog logically separate until a measured use case justifies convergence.
- Do not persist private chain-of-thought; store observable execution traces, decisions, provenance, outcomes, latency, and errors.
- Shared facts require explicit visibility scopes and promotion rules; private chat text becoming a graph fact does not make the fact safe to share.
- Evaluate retrieval with precision and temporal correctness as well as recall; include tenant leakage, stale facts, poisoning, deletion, latency, and cost.

## Verification checklist

- Profile exists and alias resolves.
- Identity file is loaded.
- Selected skills are discoverable.
- Canonical research and source index exist.
- Offline prompt smoke test passes.
- No unrequested service, credential, port, or write capability was activated.
- Any claimed integration has a recorded E2E result.
