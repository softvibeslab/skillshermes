# Existing project wiki refresh

Use when a broad project-knowledge request encounters an existing corpus, portal or graph. The deliverable may be a master synthesis rather than a new ingestion pipeline.

## Minimal workflow

1. Inspect the current README, source manifest, chapter index and canonical product definitions. Retrieve narrow session-history windows for decisions not represented on disk. Treat summaries as retrieval hints, not uncited evidence.
2. Read focused sections of primary sources. Avoid huge batched reads: truncation hides contradictions and does not count as reviewed coverage.
3. Build a topic map: identity/users, product and limitations, distinct implementations, integrations, people, budgets, acceptance gates, operations, communication rules and open questions. Omit irrelevant sections.
4. Add one dated master entry with citations and links to existing chapters. Add an inbound link from the established index. Preserve historical files and distinguish newly written synthesis from previously generated graph content.
5. Compare included manifest records against current files using SHA-256. Classify absent expected hashes as unverifiable; missing files as missing. Hash equality is not semantic validity. Detecting newly added files requires a separate bounded discovery pass.
6. Validate links, nonempty outputs and graph endpoints. Count simplified graph links separately from extracted directed/multiple relations. Never overwrite the previous validation report with a new, narrower check: use a distinct report with scope and timestamp.
7. Deliver the master path, existing portal path, verification performed and freshness caveat. Do not claim a comprehensive new extraction, runtime certification or complete conversation archive.

## Link and validator details

- Resolve relative paths from each document's parent, not the repository root or shell working directory. Compute paths rather than manually counting parent segments.
- Test ordinary Markdown links if that is the corpus convention; do not force Obsidian syntax on a browser-oriented base.
- External local links can be valid but nonportable. Flag that distinction before export or publication.
- If the report links to itself, write it before the final link pass and verify it exists; avoid a permanent exception that hides missing output.
- An assertion or small stdlib validator is sufficient for a bounded Markdown corpus. State parser limitations; a regex for simple links is not a universal Markdown parser.
- Secret scans are heuristic. Review actual generated text and rerun scans after edits. Never upload private sources merely to make links portable.

## Evidence distinctions illustrated by Sales Academy

A project can simultaneously have a documented MVP, a separate implementation, proposed partner integration, synthetic demos, investment calculators and a supervisor roster. None makes the others production-ready.

Useful distinctions from this case:

- A local goal sheet is not backend synchronization.
- A sample tour is not an authenticated working endpoint.
- An investment scenario is not cash received or an approved budget.
- A one-room pilot proposal is not a signed partnership or multi-room rollout.
- A roster of specialists is not a set of permanent running processes.
- A hash-verified September corpus plus an October synthesis is still a historical graph unless new extraction ran.

Retain these evidence patterns, not the session's counts, temporary paths, or claimed current operational state.
