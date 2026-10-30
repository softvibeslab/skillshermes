# Visual Analysis Framework

Use only with user-provided screenshots, exports, or other permitted visual evidence.

## Evidence labels

| Label | Meaning |
|---|---|
| `verified visual` | Directly observed in a supplied image |
| `page metadata` | Explicit text or structured metadata from the source page |
| `title-derived` | Classification inferred only from the project title |
| `interpretation` | Design judgment based on verified evidence |
| `not verified` | Evidence was unavailable; do not infer |

## Review card

For each visual, record:

1. Source project and exact image filename or screenshot number.
2. Product surface: mobile, web, dashboard, brand, motion, or mixed.
3. First-attention target and hierarchy.
4. Navigation model and information architecture.
5. Color roles: base, surface, text, accent, semantic states.
6. Type roles: display, heading, body, metadata, code/metrics.
7. Spacing, density, geometry, borders, shadows, and depth.
8. Components: cards, chat bubbles, agent tiles, task rows, workflow nodes, controls.
9. System states: empty, loading, running, approval, success, failure, recovery.
10. Motion cues: transition, progress, continuity, feedback, and reduced-motion risk.
11. Accessibility: contrast, target size, text size, color-only signals, cognitive load.
12. Trust: provenance, permissions, confirmation, reversibility, human override.
13. Signature element worth adapting as a principle.
14. Pattern to avoid.

## Agentic OS lens

Ask these questions:

- Can users distinguish agents by role, status, and responsibility without relying only on color?
- Can users see what an agent is doing, why, with what permissions, and what happened?
- Is there a clear separation between conversation, execution, results, and history?
- Are approval and recovery actions obvious?
- Does the interface reduce multitasking or merely visualize more multitasking?
- Can a nontechnical user understand multi-agent orchestration?
- Is the visual language trustworthy enough for business operations?

## Synthesis rules

- Reuse principles, not pixels.
- Describe color by role before proposing original tokens.
- Name a type role before choosing a typeface.
- Convert a source component into a product-specific interaction requirement.
- Triangulate a pattern across at least two references before calling it a trend.
- A visually polished case study is not evidence of accessibility, conversion, or implementation quality.
