# MiroFish local experiment execution

Use for MiroFish-style multi-stage simulations where “app is running” is not the same as “experiment is running.”

## Locate the runnable clone

When duplicate clones exist, compare prerequisites before choosing:

- `.env` exists and required values are set (never print secrets).
- root/frontend dependencies and backend virtualenv exist.
- configured LLM endpoint is listening.
- project ports are free or already serving the expected app.
- `git status --short` is understood before edits.

Prefer the configured runnable clone over installing/configuring a fresh duplicate unless the user explicitly wants the other copy repaired.

## Start and verify services

From the runnable clone:

```bash
npm run dev
```

Expected defaults:

- Frontend: `http://127.0.0.1:3000`
- Backend health: `http://127.0.0.1:5001/health`

Verify both independently. Keep the tracked server process alive while the experiment runs.

## API pipeline

The durable sequence is:

1. `POST /api/graph/ontology/generate` as multipart form:
   - `files`: seed `.md`, `.txt`, or `.pdf`
   - `simulation_requirement`: full experiment prompt
   - `project_name`
   - optional `additional_context`
2. Quality gate the returned ontology before spending on later stages:
   - domain-specific entity types exist;
   - expected relationship types exist;
   - `analysis_summary` is not unexpectedly empty.
   Generic fallback-only types such as `Person` and `Organization` are a degraded result. Do not silently call that a good ontology.
3. `POST /api/graph/build` with `project_id`, `graph_name`, `chunk_size`, and `chunk_overlap`.
4. Poll `GET /api/graph/task/<task_id>` until `completed` or `failed`. Record `graph_id`, node count, edge count, and chunk count.
5. `POST /api/simulation/create` with `project_id`, `graph_id`, and enabled platforms.
6. `POST /api/simulation/prepare` with `simulation_id`; poll `POST /api/simulation/prepare/status` using both `task_id` and `simulation_id`.
7. Verify prepared agent count and entity types match the experiment design. A graph with many nodes may yield only a few eligible agents.
8. `POST /api/simulation/start` with `simulation_id`, platform, a conservative `max_rounds`, and graph-memory setting.
9. Verify actual execution with `GET /api/simulation/<simulation_id>/run-status`; require `runner_status=running` or a completed state plus advancing rounds/actions.

## Interpret the UI and generated artifacts

- `ready` means profiles/configuration exist; it does **not** mean rounds ran.
- A counter such as `0/72 轮` means zero of 72 rounds executed (`轮` = rounds).
- `current_round: 0` plus platform states such as `not_started` proves there are no simulation outcomes yet.
- The run-status counter can remain stale at round 0 while OASIS is producing actions; verify `simulation.log`, `social.agent.log`, and SQLite table counts before calling it stuck.
- If every configured `active_hours` falls outside the simulated hours, the loop skips every round and completes in 0 seconds. Align active hours with the smoke-test window (or use 0–23).
- Twitter-only simulations may still fail the prepared-state check after stop/restart if `reddit_profiles.json` is absent; an empty `[]` file is sufficient when Reddit is disabled.
- The first active round may pause on Hugging Face retries for `Twitter/twhin-bert-base`; inspect logs before restarting.
- `simulation_config.json` and profile files are setup artifacts. Results require run-state/actions and, if requested, a generated report.
- When explaining results to a non-technical user, separate: what was prepared, what actually ran, what can be concluded, and what cannot yet be concluded.

## Recover service and inspect an existing report

1. Check listeners before starting a duplicate stack. Start the configured clone with `npm run dev` as a tracked, long-lived background process; verify `/health` on port 5001 and the exact frontend URL separately.
2. For `/interaction/<report_id>`, query `GET /api/report/<report_id>`. Extract only `status`, `simulation_id`, `created_at`, `completed_at`, and `error` initially; avoid dumping both `markdown_content` and duplicated outline sections into context.
3. Query `GET /api/simulation/<simulation_id>/run-status` using the association returned by the report, rather than assuming a remembered simulation ID.
4. Inspect `updated_at`, `started_at`, `process_pid`, platform round counters and completion flags. Confirm the PID's command identity with `ps`, not merely its existence (PIDs can be reused). Re-query progress before claiming an active worker.
5. A persisted `runner_status=running` with an absent worker and unchanged counters is stale state, not a resumed simulation. Starting the web/backend services alone does not resume that worker. Do not rewrite state or launch a new run merely to make the indicator consistent.
6. If report `completed_at` precedes the current run's `started_at`, label it an earlier report even when the simulation ID matches. Read its content only for a clearly labeled historical summary; synthetic recommendations remain hypotheses, not measured user outcomes.
7. Report three distinct statuses: application availability, current simulation progress/liveness, and report freshness. State explicitly whether only services were started or a simulation was also launched. Do not assume resume/checkpoint support without tracing the implementation first.

## Model quality and rerun semantics

- Small local models can return schema-valid but semantically degraded output. A observed failure pattern with `qwen2.5:3b` was fallback-only ontology, channels represented as agents, fewer profiles than requested, and contradictory country/language metadata.
- For an Apple Silicon machine with 24 GB unified memory, `qwen2.5:14b` is a practical local step up for MiroFish structured extraction; a 32B model leaves little headroom for Ollama, Node, Python, and simulation processes. Treat this as a sizing starting point and recheck live hardware.
- MiroFish's documented cloud baseline is `qwen-plus` through an OpenAI-compatible DashScope endpoint when output quality matters more than local-only execution.
- Configuration uses `LLM_API_KEY`, `LLM_BASE_URL`, and `LLM_MODEL_NAME` in the runnable clone's `.env`; preserve `ZEP_API_KEY` and never print it.
- A model change is not retroactive: restart MiroFish and create a new project from the seed so ontology, graph, profiles, and simulation config are regenerated. Reusing a degraded graph preserves the original extraction errors.

## Operational rules

- Keep and report all handles: `project_id`, graph task ID, `graph_id`, preparation task ID, and `simulation_id`.
- Do not report “executed” after ontology generation, graph completion, or preparation alone. Report the exact stage: service running, graph built, simulation ready, simulation running, or completed.
- For local/cheap smoke tests, cap rounds conservatively first; increase only after profile quality and actions look sane.
- If ontology/profile quality is poor because the configured model is too small, either switch to an already-authorized stronger model or report the quality limitation. Do not hide it behind successful HTTP status codes.
- Never expose `.env` values; report only whether required keys are set and non-empty.
