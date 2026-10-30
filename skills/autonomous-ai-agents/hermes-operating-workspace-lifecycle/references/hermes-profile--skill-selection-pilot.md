# Evidence-first skill-selection pilot and IDE handoff

## Use case
A user wants to apply a video's decision-model architecture to one Hermes profile, reducing skill-catalog context without reducing task quality. The CAV planning session established these inspection and handoff patterns; this is not evidence that a selector was implemented.

## Inspect the real context path
Before designing a router, locate the installed implementation and its callers. Source landmarks observed in that session (re-check in the current revision):
- `agent/prompt_builder.py`: `build_skills_system_prompt`, compact catalog generation, filtering and caches.
- `agent/system_prompt.py`: caller inserting the catalog into stable system-prompt parts.
- `tools/skills_tool.py`: `skills_list(category=...)` for metadata and `skill_view` for full bodies.
- `tests/agent/test_prompt_builder.py`: existing regression coverage.

Distinguish the metadata index from full skill bodies. Do not claim every skill body is already in context. A SOUL instruction to read fewer skills does not remove an index inserted by the harness. Preserve platform/tool/disabled-skill filters, local-over-external precedence, and cache semantics when proposing changes.

## Experiment ladder
1. Establish a representative task set, including ambiguous and multi-skill cases. Separate tuning from held-out evaluation; approximately 30 tasks is a practical pilot, not a statistical guarantee.
2. Compare current behavior with simple lexical retrieval over existing names/descriptions. Reuse category listing and on-demand loading rather than duplicating them.
3. Introduce a decision model only if it demonstrably beats the simple baseline. Verify the exact model ID and provider through authoritative sources; transcript spellings alone are insufficient.
4. Allow multiple categories, no match, uncertainty, and a broadening fallback. Measure required-skill recall and final task quality, not just catalog compression.
5. Run in observation mode first: record recommendations without hiding skills or altering execution.
6. Measure total input/output/cached tokens, extra classifier calls, latency and available cost data. A smaller main prompt may lose cache benefits or add more classifier cost than it saves.
7. Activate only in the authorized pilot after evaluation, with explicit rollback. Keep permissions and approvals independent of routing; a classifier's safety label never authorizes a command.

Use Python stdlib, unittest and JSON/JSONL for the initial offline prototype when adequate. Do not add a vector store, framework, server or UI speculatively. Exclude secrets and unnecessary private task text from evaluation records.

## Plan-only delivery to Cursor
A request for an implementation plan is not permission to modify the running core, profile configuration or gateways. Write one plan in the project workspace with exact source landmarks, small tasks, executable checks, acceptance gates and rollback.

Verify the saved file and installed editor CLI before providing commands, e.g.:

```bash
cursor "/absolute/project/workspace"
cursor "/absolute/project/workspace/IMPLEMENTATION_PLAN.md"
```

Give a bounded initial prompt: read the plan, inspect the actual flow, document findings, and stop before implementation or runtime changes. If the user offers email OR editor commands, working editor commands satisfy delivery; do not claim an email was sent. Report plan saved, implementation pending and runtime unchanged as separate states.
