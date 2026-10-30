---
name: knowledge-graph-agent-profiles
description: Build and verify specialized AI-agent profiles grounded in a property graph or graph-memory backend. Use when turning a researched domain into a reusable agent profile with controlled ingestion, explicit provenance, read-only retrieval tools, and end-to-end answer checks. Covers Neo4j-like databases and Hermes-style profiles without being tied to one vendor. Not for generic vector-only RAG or ordinary database schema design.
---

# Knowledge-Graph Agent Profiles

Build the smallest graph-grounded profile that can answer the user's real questions with traceable evidence. Load the platform-specific profile/configuration skill first (for Hermes, load `hermes-agent`) and use this skill for the graph-grounding layer.

## Outcome contract

A completed profile has:

1. an isolated agent profile with a narrow tool surface;
2. a curated, cited research corpus stored outside the prompt;
3. a minimal property-graph model derived from representative questions;
4. repeatable, idempotent ingestion with uniqueness constraints;
5. read-only graph access for normal agent operation;
6. machine-run checks for counts, relationships, authorization, and representative answers;
7. update and rollback instructions recoverable from disk.

## Workflow

### 1. Start from questions, not ontology

Write 3-5 questions the profile must answer. Derive only the node labels, relationship types, and properties needed for those queries. Prefer a compact graph such as:

- `Source` — URL, title, publisher, retrieval date, content hash;
- `Section` — heading, text, ordinal, source identity;
- domain entities such as `Technology`, `Capability`, `Concept`, or `Decision`;
- relationships such as `HAS_SECTION`, `MENTIONS`, `SUPPORTS`, `DEPENDS_ON`, and `INFORMS`.

Do not model every noun. Add a label or relationship only when a real query needs it.

### 2. Research with provenance

Fetch authoritative sources first: official documentation, maintained repositories, specifications, and project READMEs. Preserve source URL, retrieval date, and a content hash. Distinguish:

- sourced facts;
- synthesis inferred across sources;
- implementation decisions made for this profile.

Store synthesis and decisions as explicit graph entities or documented metadata rather than presenting them as quotations.

### 3. Keep ingestion deterministic

Use one rerunnable ingestion script. It should:

- create uniqueness constraints before loading data;
- use stable natural or namespaced IDs;
- use `MERGE` for nodes and relationships;
- update mutable properties with `SET`;
- record an import/version identifier;
- avoid deleting unrelated graph data;
- expose a scoped rollback by import/version identifier.

A second run against unchanged inputs must preserve counts and relationships.

### 4. Separate write-time and run-time authority

Use administrative write credentials only for ingestion. The profile's normal MCP/tool connection should expose schema inspection and parameterized read queries only. Verify denial with a harmless write attempt and confirm it leaves zero artifacts.

Treat generated Cypher as untrusted input. Enforce read-only access at the database role/tool boundary, not only in the system prompt.

### 5. Use graph retrieval before adding embeddings

For a small, curated corpus, exact identifiers, labels, relationships, and full-text predicates are usually enough. Add vector indexes, embeddings, GraphRAG, or temporal memory only after representative questions show measurable retrieval gaps.

`# ponytail: graph-first retrieval; add vectors when query evaluation proves relation/text lookup is insufficient.`

### 6. Verify end to end

Leave one runnable verification script that checks:

1. expected node and relationship counts or minimum bounds;
2. no duplicate stable IDs;
3. every section links to a source;
4. representative multi-hop queries return cited results;
5. a rerun is idempotent;
6. the run-time identity cannot write;
7. the agent can answer the original 3-5 questions through its actual read-only tool path.

A successful database import alone is not completion.

### 7. Document operations

Document exact commands for ingest, verify, refresh one source, rebuild the controlled import, and rollback only that import. Keep research notes, scripts, and operational docs inside the profile or project so a fresh session can resume without chat history.

## Common pitfalls

- Huge ontology before any query exists — derive the model from questions.
- Pasting the whole research corpus into the system prompt — keep durable evidence in the graph.
- Giving the live agent write access because ingestion needed it — split identities or tool surfaces.
- Claiming read-only safety without testing a denied write and checking for residue.
- Adding embeddings by default — measure retrieval failure first.
- Verifying only counts — run the actual multi-hop questions through the same path the agent uses.
- Mixing sourced claims with synthesis — label provenance and decision records explicitly.

## Related skills

- `hermes-agent`: profile creation, configuration, providers, MCP servers, and Hermes-specific commands.
- `deep-research` / `evidence-knowledge-delivery`: source acquisition, citation, and evidence synthesis.
- `rag-architect`: vector/hybrid retrieval and retrieval metrics after graph-only retrieval reaches its ceiling.
- `database-designer`: broader schema design outside this agent-grounding workflow.
- `agentic-application-lifecycle`: deployment and production verification after the profile works locally.

## References

- `references/neo4j-hermes-pattern.md` — concrete Neo4j + Hermes implementation pattern distilled from a verified profile build.
