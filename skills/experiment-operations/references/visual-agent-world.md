# Visual agent-world view

Use when an operator needs to understand a multi-agent run spatially rather than from logs alone.

## Model

Treat the visualization as a projection of existing experiment data:

- `agents[]`: stable synthetic ID, display label, profile summary;
- `stages[]`: fixed ordered milestones;
- `actions[]`: identity, timestamp/round, action text, optional status;
- `mode`: `preview` or `live`.

Derive avatar position from the latest action. Derive visual state separately so `advancing`, `working`, `blocked`, `waiting_review`, and `finished` do not become fake milestones.

## Preview versus live

Preview uses deterministic local fixtures, is visibly labeled, and never submits a run. Use it to test every stage, state, selection, inspection, and animation without cost.

Live mode reads the host API and preserves raw action history for inspection. Match explicit agent IDs first. If the source lacks stable IDs, an order-based fallback is acceptable only with a visible `correspondencia provisional por orden` warning; never present it as confirmed identity.

## Lightweight rendering

A static CSS diorama is enough:

1. Draw one route with fixed stage labels.
2. Position avatars using CSS properties such as `--x` and `--lane`.
3. Offset lanes so agents at one stage remain distinguishable.
4. Encode state with color plus text/icon, never color alone.
5. Selecting an avatar reveals its profile and chronological actions.
6. Respect `prefers-reduced-motion`; animation stays decorative.

Do not add canvas or a game engine until camera movement, collision, large crowds, or continuous physics are real requirements.

## Verification

Keep one runnable structural check for complete unique cohort IDs, all fixed stages, every supported state label, the live actions endpoint, and the provisional-mapping warning.

Visually verify both modes: first and last stages fit, exact avatar count appears, overlaps remain readable, agent selection opens the correct profile/history, and no preview control can start a paid run.
