# Research-Backed Agent Knowledge Workspace

Use this pattern when a user wants to turn research material into a durable agent ecosystem inside an existing project, but has not yet approved installing or activating a Hermes profile.

## Minimum deliverable

Create one self-contained directory under the project's existing knowledge/data area rather than scattering files across the repo:

```text
<project>/<knowledge-area>/<agent-slug>/
├── README.md
├── PROJECT_CONTEXT.md
├── ECOSYSTEM.md
├── SOUL.md
├── IMPLEMENTATION_PLAN.md
├── sources/
└── wiki/
    ├── SCHEMA.md
    ├── index.md
    ├── log.md
    ├── concepts/
    └── comparisons/
```

- `README.md`: entry point and navigation.
- `PROJECT_CONTEXT.md`: how the agent fits the parent project and where future Hermes profile wiring belongs.
- `ECOSYSTEM.md`: research synthesis across skills, MCPs, CLIs, frameworks, and model/runtime choices.
- `SOUL.md`: profile-ready identity/instructions, kept inert until installation is approved.
- `IMPLEMENTATION_PLAN.md`: phased path from knowledge workspace to live profile.
- `sources/`: immutable originals plus provenance metadata/hashes.
- `wiki/`: schema-governed, interlinked concepts, comparisons, index, and changelog.

## Integration sequence

1. Read the parent project's README/context and locate its established dataset, analysis, or knowledge directory.
2. Copy source artifacts into `sources/`; do not mutate originals.
3. Record a hash for each copied source so later drift is detectable.
4. Build the wiki from the sources, using the project's vocabulary and linking concepts bidirectionally.
5. Link the new workspace from the parent README, the local dataset/knowledge index, and any directly related analysis page.
6. Validate in one pass:
   - expected files exist;
   - internal Markdown/wikilinks resolve;
   - every source hash matches;
   - parent-project backlinks point to the workspace.
7. Report two states separately:
   - **knowledge workspace ready**;
   - **Hermes profile installed/activated** only after the SOUL, skills, config, and gateway were actually applied and verified.

## Ponytail defaults

- Reuse the parent project's structure before inventing a new root-level convention.
- Keep one agent workspace and one wiki; do not create a new app, database, or framework for static research.
- Preserve source evidence and build only central concept pages; skip passing mentions.
- A profile-ready `SOUL.md` is not evidence that a profile exists.

## Verification evidence

The handoff should state the absolute workspace path, files/page counts, link/hash check result, backlinks added, and the exact deferred activation step. Never blur “documented” with “running.”
