# Executive presentations from synthetic experiment evidence

## Reusable delivery recipe

1. Read the supplied narrative/source analysis completely. Inspect the canonical JSON schema, report methodology, and existing check script before authoring. Obey the write allowlist; source reports stay untouched.
2. Map each displayed claim to a source and category: product intention, implemented parameter, observed synthetic output, historical technical evidence, or proposed human-pilot metric.
3. Build a decision narrative: value → role journey → experiment variants → platform-specific results → intended versus effective variables → use cases → growth hypotheses → viability gates → sources.
4. Copy only necessary canonical fields into a small local snapshot. Avoid full posts, biographies, private identifiers, and duplicate recovery backups. Preserve source timestamp and experiment identifier. If copying a source analysis, preserve its body and prepend a separately labeled verification note rather than silently rewriting its original evidence status.
5. Show raw counts alongside CSS bars and textual labels. Define the denominator beside the selector and update it when switching platforms. Distinguish trace operations from users, original posts, accepted missions, and model calls. Do not calculate unsupported conversion or causal effect.
6. Table effective selector inputs and declared-but-unused dimensions separately. Cite formulas to the source report/code; include filtering and caps rather than presenting an intermediate formula as the whole algorithm.
7. Keep product roles and experiment actors in separate diagrams. Present each untested route as hypothesis + risk + proposed metric + validation gate. Catalog alternatives and commercial content examples must be marked untested if not simulated.
8. Use system fonts and native HTML/CSS/JS when a static artifact is requested. For local external data, use textContent or escaping, validate expected fields, and show a useful unavailable-data state.

## Minimal runnable verification

A dependency-free Node checker can read source JSON and the snapshot, evaluate a trusted locally generated snapshot assignment in node:vm (not a sandbox for untrusted code), and use assert.deepEqual on each selected field. Assert platform counts, sample sizes, action denominator consistency, unique section IDs, matching navigation anchors, local resource existence, and source/download links. An optional HTTP flag checks resources against an existing server; it does not imply browser rendering succeeded.

Then use an available browser surface for: desktop and narrow viewports, platform selector, presentation enter/exit, previous/next boundary behavior, counter, hash navigation, keyboard focus, and print visibility. Ensure one chapter observer is used in reading mode and cannot fight explicit presentation navigation. Re-run the checker after the last edit. Report which layers actually ran, and any remaining unverified behavior.

## BeGlobal evidence example (session-specific, not defaults)

Canonical report directory: `frontend/public/beglobal-final-336/`; presentation directory: `frontend/public/beglobal-presentacion/`; check: `frontend/scripts/check-beglobal-presentacion.mjs`.

Experiment `sim_373dcc2ddf2f`, source cut `2026-09-12T21:45:50.746692-05:00`:

| Platform | Actors | Traces | Posts | Comments | Refresh |
|---|---:|---:|---:|---:|---:|
| Twitter | 4 | 254 | 113 | 0 | 126 |
| Reddit | 4 | 350 | 5 | 14 | 322 |

Both reached terminal round/index 336, with historical partials and approximate recovery context; this is not 336 independent user journeys. Ten planned profiles were not ten executed independent trajectories. Product roles were Orchestrator/Member/Team/Corporate; simulated actors were Corporate/Telegram/Member/BeGlobal.

Action-share formula: action records / platform traces × 100. Report selector formulas included nominal hour = floor((round−1) × minutes_per_round / 60) mod 24 and target_count = int(uniform(base_min, base_max) × multiplier), followed by active-hours/activity filtering and capped sampling without replacement. Re-read authoritative sources before reuse.

The principal human-pilot metric proposed was members with an accepted mission per week, not chat volume. A/B/C did not establish a causal winner or demonstrated growth. Historical technical feasibility did not verify current production; operational and commercial feasibility remained to be measured.
