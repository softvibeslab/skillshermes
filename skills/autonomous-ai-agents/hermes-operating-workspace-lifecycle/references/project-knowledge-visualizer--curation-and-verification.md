# Multi-project knowledge visualizers: curation and verification

Use when extending an existing local knowledge globe to multiple project repositories. Reuse its app, categories, and history rather than creating a second viewer.

## Source selection

1. Resolve approved project variants and real source roots. One product family can contain an app, agent squad, community, or third-party framework; label these distinctions explicitly rather than implying common ownership.
2. Prefer an explicit file manifest of strategic documentation (README, PRD, architecture, selected plans) over recursive indexing of entire repositories. Record category, source path, and selection rationale in local data artifacts.
3. Different categories can share a repository but select different files. Check accidental overlap before treating categories as separate coverage.
4. A README is not inherently safe. Review selected content for embedded credentials and private conversations before ingestion. Exclude secret-bearing files or ingest sanitized local copies without editing the originals.
5. Validate real paths and symlinks against authorized roots. Keep intake, voice samples, raw assistant memories, unrelated projects, and credentials out unless explicitly authorized and appropriate.
6. Verify exclusions across generated graph content, search data, node detail/API responses, and any raw-source endpoint. Removing a token from search does not prove it cannot be served elsewhere. Keep private manifests, graph data, reports, and backups out of version control; ignore rules do not untrack existing files.

## Verification gates

- Build: rebuild through the existing entry point and run the repository's packaged checks.
- Content: verify representative nodes from every category against their selected source or sanitized copy. Check both intended inclusion and excluded content.
- Runtime: verify loopback binding and an actual HTTP response independently of process-start output.
- UI: exercise search, category isolation/filtering, inventory, and growth/demo/Cinema where present. Inspect the rendered globe to confirm spherical composition and category colors remain intact.
- Coverage: record mobile layout, drag/zoom during animation, console checks, and other interactions as passed only when actually tested. A package test does not prove those interactions.
- Delivery: state that the graph represents selected documentation, not live project health or complete code coverage. Separate third-party framework content from user-owned products.

## AIS-OS source landmarks

In the reviewed workspace, the visualizer lives under `apps/3d-brain/`, with `brain.config.json`, `build.mjs`, `serve.mjs`, and generated `data/graph.json`. The repository-native skill is `.claude/skills/3d-brain/SKILL.md`; its package check was `.claude/skills/3d-brain/scripts/test-package.mjs`. Reinspect these paths and scripts before use, rather than assuming a Hermes registry alias exists.

A local `data/source-selection.json` can hold the allowlist and `data/project-mapping-verification.md` can record dated evidence and untested interactions. Do not encode session node counts, running PIDs, or project paths as permanent skill facts.
