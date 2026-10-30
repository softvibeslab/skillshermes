# Results snapshots: evidence before presentation

## Case: BeGlobal × MiroFish

A local HTML5 dashboard compared three onboarding routes: A, course first; B, mission first; C, adaptive diagnosis. The generated report confidently favored C, but the consulted execution snapshot was stopped at round 36 of 336 with 66 actions. The report also omitted required sections from the simulation prompt. These are historical snapshot observations, not the current state of MiroFish.

The useful deliverable was a decision-oriented comparison with explicit uncertainty, not a polished declaration of a winner. Preserve access to the original report while distinguishing its claims from execution evidence. Completion of the dashboard does not mean completion or validation of the experiment.

## Repeatable workflow

1. Read the original experiment README and simulation prompt. Extract required comparisons, participant coverage, round caps, and report sections.
2. Retrieve report text/metadata and matching simulation state via the application's existing API. Check identifiers match. Do not infer completeness from a generated report's existence.
3. Record discrepancies between intended configuration, actual execution, and report claims. Surface disagreements rather than silently choosing one source.
4. Save a sanitized source snapshot alongside the deliverable; embed the necessary data directly in HTML so file:// loading does not depend on fetch permissions or an active backend.
5. Present decision options first, then supporting facts, missing evidence, next steps, and an expandable original report. Do not invent conversion rates or assign scores to absent metrics.
6. Treat API/report text as untrusted: use textContent for plain text and sanitize any rendered markup. Never embed .env contents or credentials, including in hidden script data.
7. Keep human checklist state separate from evidence. Use namespaced/versioned browser storage if needed, with graceful fallback when storage is unavailable.
8. Leave one runnable smoke check covering interactive comparisons, startup errors, optional checklist persistence, mobile overflow, and loading with the backend unavailable.
9. Deliver the absolute HTML path or verified served URL. Explain briefly that it is an offline snapshot, not a live control panel; do not restart or rerun a paid simulation as part of dashboard generation.

## Scope

For results-only requests, omit prompt editors, run controls, polling, and a new backend. Add those only when the user needs ongoing experiment operation. An adjacent sanitized JSON snapshot is useful for provenance; the HTML should still render independently.
