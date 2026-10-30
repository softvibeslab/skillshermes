# MiroFish → Nexo/Radar Local: evaluation notes

## Upstream snapshot evaluated

- Repository: `666ghj/MiroFish`
- Architecture: Vue/Vite frontend + Flask backend + OASIS multi-agent social simulation.
- License: AGPL-3.0.
- Input: PDF/Markdown/text plus a natural-language simulation requirement.
- Pipeline: ontology generation → Zep graph → synthetic agent profiles → Twitter/Reddit-style OASIS simulation → report agent.

## Runtime facts

- Node 18+.
- Python `>=3.11,<3.13`; `uv sync` can provision a compatible project-local Python.
- OpenAI-compatible LLM endpoint supported through `LLM_API_KEY`, `LLM_BASE_URL`, and `LLM_MODEL_NAME`.
- Zep Cloud API key is mandatory in this version, so an Ollama LLM does **not** make the complete pipeline local.
- Default backend permits wildcard CORS and defaults to debug mode unless configured otherwise. Keep localhost-only for evaluation.
- The simulation is call-intensive; begin below 40 rounds. Small 3B local models may smoke-test transport but are unlikely to maintain strong structured generation and persona consistency.

## Verified installation pattern

```bash
git clone --depth 1 https://github.com/666ghj/MiroFish.git ~/Documents/GitHub/MiroFish
cd ~/Documents/GitHub/MiroFish
npm run setup:all
npm run build
cd backend && uv run pytest -q
```

For a health-only smoke test, use temporary placeholder keys and a localhost OpenAI-compatible URL, start `uv run python run.py`, probe `http://127.0.0.1:5001/health`, then stop it. Do not invoke graph or simulation routes with fake keys.

After installation, check `git status`; npm may rewrite an upstream lockfile even when no intentional dependency change was requested. Restore that tracked lockfile after verification and retain installed `node_modules`/`.venv`.

## Operational pilot recipe

Keep experiment inputs outside both repositories so upstream clones and Nexo remain clean:

```text
~/Documents/Experiments/<pilot>/
  README.md
  SIMULATION_PROMPT.md
  seed/<synthetic-brief>.md
  results/
```

Before running, scan the pilot directory for phone-like strings, WhatsApp JIDs/links, tokens, and API-key assignments. The seed should explicitly say that all actors are synthetic and results are hypotheses.

Create MiroFish's ignored `.env` with permissions `0600`:

```env
LLM_API_KEY=ollama
LLM_BASE_URL=http://127.0.0.1:11434/v1
LLM_MODEL_NAME=<local-model>
ZEP_API_KEY=<zep-key>
FLASK_DEBUG=false
OASIS_DEFAULT_MAX_ROUNDS=10
```

Verify Zep without creating or uploading anything:

```python
from zep_cloud.client import Zep
from app.config import Config
Zep(api_key=Config.ZEP_API_KEY).graph.list_all(page_size=1)
```

Start with `npm run dev`, verify frontend `:3000` and backend `/health` on `:5001`, and keep both bound to localhost. A deliberately terminated smoke-test server commonly exits with `-15`/SIGTERM; treat that as expected only when the evaluator initiated the shutdown.

For Zep onboarding, describe the product using only its privacy-safe purpose and desired synthetic memory. Explicitly prohibit real names, phones, chats, WhatsApp exports, credentials, and identifiable profiles; require human approval for matches, introductions, and outreach.

After “Graph build is complete,” the next UI stage creates the simulation instance, generates personas, and builds Twitter/Reddit simulation configuration. Before starting the run, inspect generated agent count, total rounds, names, platform count, and each agent's `active_hours`. For the first local pilot, target 10–20 synthetic agents, at most 10 rounds, and one platform when selectable. Stop and review rather than launching a larger generated configuration.

### Short-run guardrails and MiroFish state quirks

Generated configuration can be far larger than requested: one observed 30-day pricing experiment produced 108 hourly rounds. Apply both guards:

1. Set `time_config.total_simulation_hours`/`minutes_per_round` to the intended run length.
2. Pass `max_rounds` to `POST /api/simulation/start`; do not rely on only one guard.

The Twitter script maps round zero to simulated hour `00:00`. If a short run covers hours `00:00–07:00` but generated agents are active only at `09:00+`, the loop completes with zero actions. Before starting, leave a runnable invariant such as:

```python
hours = range(round_count)
assert all(any(h in agent["active_hours"] for h in hours) for agent in config["agent_configs"])
```

For a synthetic smoke test, align `active_hours` with the short window. For a behaviorally meaningful run, preserve realistic hours and configure a window that actually reaches them.

The runner intentionally enters an IPC wait loop after `模拟循环完成` so interviews remain available. Consequently `/run-status` may continue to say `running` with round zero even though the simulation loop finished. Diagnose from `simulation.log`, process CPU, and the presence of the completion marker; then call `/api/simulation/close-env` and `/api/simulation/stop`. Do not wait indefinitely on the stale status field.

Stopping can change `state.json` to `paused`, while MiroFish's prepared check accepts only `ready`; profiles and config may still be intact. Prefer the official close/stop flow, verify required artifacts, and avoid regenerating profiles blindly. If a retry is needed, repair only the state transition after confirming `config_generated`, profile count, config, and profile files.

### Report validity gate

A successful report task is not a valid report. A 3B local model completed the pipeline but:

- changed the domain from real estate to health;
- introduced unseeded students, media, and public institutions;
- invented a “60% of users” statistic;
- leaked internal report-agent instructions and tool names;
- wrote conclusions unsupported by observed actions.

Before presenting conclusions, reject or quarantine reports that show:

1. domain drift or unseeded actor classes;
2. percentages/counts with no traceable simulation query;
3. internal prompt/tool leakage;
4. claims without quoted actions or interviews;
5. wrong output language;
6. requested comparison dimensions missing from the result.

Rename invalid artifacts with an `INVALID-` prefix and write a short validation note; never salvage them into business advice. Treat a 3B model as transport-only. Use a stronger instruction-following model (14B+ as a starting point), rerun the same bounded fixture, and require the validity gate again.

## Nexo fit

Use MiroFish as a separate scenario laboratory, not Nexo's core matching engine.

Recommended flow:

```text
Radar/Nexo aggregates
  → synthetic, anonymized scenario brief
  → isolated MiroFish run
  → hypothetical scenario report
  → human review
  → optional Nexo insight record
```

Useful experiments:

1. Broker and property-manager adoption of Radar Local IA.
2. Privacy/spam objections to proposed positioning and outreach language.
3. Reactions to pricing and value propositions.
4. Fairness and trust in explainable Top-5 property/broker matches.
5. Market stress scenarios using aggregate zone, price-band, inventory, and intent counts.

## Data boundary

Never send MiroFish raw WhatsApp exports, CSV rows, phone numbers, names, private messages, or real-person profiles. Zep Cloud receives graph material. Seed files should contain aggregates and explicitly synthetic archetypes only.

## Integration boundary

If the experiment proves useful, expose MiroFish as an isolated, authenticated internal HTTP sidecar. Nexo may submit a versioned synthetic scenario and retrieve a report. Do not copy MiroFish source into Nexo without AGPL review. Never turn simulation output directly into outreach, lead ranking, or automated action.

## Interpretation

MiroFish generates plausible synthetic scenarios, not validated forecasts. Label every result accordingly and compare important claims against real interviews, observed outcomes, or controlled product experiments.
