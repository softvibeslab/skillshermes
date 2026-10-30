# Neo4j + Hermes profile pattern

Concrete pattern distilled from the `neo4jvibes` build. Treat names and counts as an example; re-discover live configuration before reuse.

## Source map

Use these sources by role rather than flattening them into one undifferentiated corpus:

- Neo4j product and developer surface: https://neo4j.com/
- Hermes Graphiti integration example: https://github.com/p1s4/hermes-graphiti-plugin
- Agent-memory concepts and patterns: https://neo4j.com/labs/agent-memory/
- Independent Hermes ecosystem context: https://github.com/thekaveh/atlas/blob/main/docs/research/rows/hermes.md
- Neo4j GenAI/MCP overview: https://neo4j.com/developer/genai-ecosystem/model-context-protocol-mcp/
- Official Neo4j MCP implementations: https://github.com/neo4j/mcp
- Graph Data Science agent pattern: https://github.com/neo4j-contrib/gds-agent
- Agent-framework integrations: https://github.com/neo4j-labs/neo4j-agent-integrations
- Reusable Neo4j agent skills: https://github.com/neo4j-contrib/neo4j-skills
- Data-modeling MCP workflow: https://neo4j.com/blog/developer/neo4j-data-modeling-mcp-server/
- Neo4j Labs graph exploration/application example: https://github.com/neo4j-labs/neocarta

Official docs and maintained repositories are evidence for capabilities. Blog posts and independent ecosystem rows provide patterns or context, not guarantees about the installed version. Record retrieval date and content hash during ingestion.

## Minimal model used

```text
(Source)-[:HAS_SECTION]->(Section)
(Section)-[:MENTIONS]->(Technology|Capability|Concept)
(Technology)-[:SUPPORTS]->(Capability)
(Decision)-[:INFORMED_BY]->(Source)
```

Typical stable IDs:

```text
Source.id    = canonical URL
Section.id   = source ID + heading path + ordinal
Entity.id    = normalized namespace + canonical name
Decision.id  = profile/import namespace + decision slug
```

Keep both `Source` and `Section`: source-level provenance is easy to cite, while section-level text prevents one giant document node from becoming the retrieval unit.

## Ingestion contract

A single Python script can use the official Neo4j driver and stdlib hashing/JSON support; no framework is required for a controlled corpus.

Order:

1. Open an administrative session.
2. Create uniqueness constraints for every stable ID.
3. Assign an `import_id` to all controlled nodes and relationships.
4. `MERGE` sources and update metadata/hash.
5. `MERGE` sections and `HAS_SECTION` relationships.
6. `MERGE` curated entities and semantic relationships.
7. Commit, collect counts, rerun, and compare counts.

Do not infer all relationships from keyword coincidence. Use deterministic rules for obvious mentions and explicit curated mappings for claims such as `SUPPORTS`, `DEPENDS_ON`, or `INFORMED_BY`.

Scoped rollback:

```cypher
MATCH (n {import_id: $import_id}) DETACH DELETE n
```

Only use that shape when every controlled node is namespaced and no unrelated node shares the import ID. If the import attaches relationships to pre-existing shared nodes, delete imported relationships first and remove only imported nodes owned by the loader.

## Runtime boundary

Normal profile operation should expose only:

- schema inspection;
- parameterized read Cypher.

Keep ingestion outside the agent's routine tool surface. Database privileges remain the enforcement layer even if MCP advertises read-only tools.

Read-only probe:

```cypher
CREATE (n:ReadOnlyProbe {id: $id}) RETURN n
```

Expected result: authorization denial. Follow with a read query for that exact ID and require a count of zero.

## Verification questions

Choose questions that force different paths, for example:

1. Which researched components connect Hermes to graph memory, and which sources support that answer?
2. Which capabilities are supported by Neo4j MCP-related technologies?
3. What implementation decisions were made for this profile, and from which sources were they derived?
4. Which sections discuss data modeling, agent memory, MCP, or graph analytics?

The verification script should assert non-empty cited results, not exact prose. Exact counts are useful as a snapshot but brittle as permanent acceptance criteria; use minimums plus uniqueness and referential-integrity checks when the corpus evolves.

## Verified artifact layout from the example

```text
~/.hermes/profiles/neo4jvibes/
  research/neo4j-hermes/KNOWLEDGE_GRAPH.md
  scripts/ingest_research_graph.py
  scripts/verify_research_graph.py
```

The example finished with a small curated graph and deliberately skipped embeddings, GraphRAG, and Graphiti runtime memory because relationship/text queries covered the chosen questions. Add those layers only after an evaluation query demonstrates the gap.
