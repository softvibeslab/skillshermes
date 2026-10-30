# Interactive Use-Case Simulator for Agent Explainers

Use this pattern when a static role card explains *what* an agent does but the user needs to see *how work moves*.

## Minimal interaction model

Add one shared simulator above the role cards rather than a separate animation engine per card:

1. Role tabs select a case.
2. Each case has four observable stages: `Entrada → Agente → Herramientas → Evidencia`.
3. A progress line and one active-stage pulse show continuity.
4. Each role card gets one “Ver caso en acción” control that selects its case and returns focus to the simulator.
5. Provide pause/play, restart, and a synchronized `Paso N de 4` label.

Keep case data in one JavaScript array. Generate tabs, stages, and card controls from it so labels do not drift.

## State contract

Use explicit classes instead of loosely timed opacity animations:

- `.is-active`: current step, highest contrast, restrained pulse.
- `.is-done`: completed step, visible success treatment.
- default: pending, still readable.
- `.paused`: sets `animation-play-state: paused` for the simulator subtree.

Drive the label and classes from the same timer. A progress bar that says step 2 while step 1 is highlighted is a failed verification.

On case change:

1. replace title and step content;
2. reset elapsed time;
3. clear paused state;
4. update step classes immediately, before the next timer tick;
5. restart CSS progress animations with a one-frame class toggle.

## Motion and accessibility

Motion must explain state, not decorate the page.

- Keep pending text readable; do not fade it below practical contrast.
- Minimum control target: 44×44 px.
- Add `aria-selected` to role tabs and `aria-label` to icon-only controls.
- Use `aria-live="polite"` for the case title/stage area.
- Honor `prefers-reduced-motion`; switch animated scrolling to `auto`.
- On mobile, collapse four stages to a 2×2 grid and remove connector lines that no longer map cleanly.
- Hide the live simulator in print/PDF unless a static print treatment is explicitly designed.

## Verification

Run the primary path, not just page load:

1. Select a non-default role and assert selected tab, case title, active card, and four stage nodes all change together.
2. Pause and assert the paused class and accessible button label change.
3. Restart and assert step 1 is active immediately.
4. Check exactly one active stage and one active role card.
5. Confirm no console errors.
6. Inspect the main viewport visually for contrast, alignment, and state ambiguity.
7. Check mobile overflow and reduced-motion behavior.

Preserve the previous HTML before a significant interaction redesign so rollback is one file copy away.
