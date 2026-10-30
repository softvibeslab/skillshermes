# Content Strategy Control Tower

Use this pattern when an agent portfolio or starter kit needs a content strategy dashboard rather than only a sales explainer.

## Canonical content model

Treat the strategy as structured data first:

```text
4 pillars
└── 4 topics per pillar
    └── at least 10 post themes per topic
```

Minimum complete inventory: 4 pillars, 16 topics, 160 themes. Do not call the strategy complete while any theme list is missing. Show honest progress such as `73/160 themes developed`.

Each theme should be a concrete post idea, not a renamed topic. Store optional channel adaptations separately so one core idea can become Instagram, LinkedIn, TikTok, email, or video without inflating the theme count.

## Visual mapping

A lotus diagram is a navigation layer, not the source of truth:

- center: brand promise or transformation;
- first ring: four pillars;
- second ring: four topics per pillar;
- detail panel: ten themes for the selected topic.

Keep the full hierarchy available as an accessible list/table and on narrow screens. Clicking a petal should update the detail panel and preserve a visible selected state.

## Design Thinking loop

Map editorial work to a small loop:

1. Empathize: audience tensions, rituals, language, emotional load.
2. Define: communication problem and desired audience decision.
3. Ideate: pillars, topics, themes, hooks, and formats.
4. Prototype: produce a small batch across channels.
5. Test: collect observable signals and qualitative feedback.
6. Iterate: update themes and briefs; do not invent performance claims.

## Agent control tower

Assign jobs, not decorative personas:

- Research: gathers audience evidence and source material.
- Strategist: owns pillars, topics, and editorial coherence.
- Ideator: expands approved topics into themes.
- Adapter: converts themes into channel-specific formats.
- Producer: creates drafts and assets.
- Reviewer: checks brand, evidence, safety, and quality.
- Publisher: schedules only approved work.
- Analyst: records measured outcomes and feeds learning back.

Make human approval boundaries visible before publishing, customer contact, spend, or sensitive claims.

## Minimal implementation

For a portable starter kit, prefer one self-contained HTML file with embedded CSS/JS and a single JSON object as the canonical strategy. Derive cards, counts, detail panels, and JSON export from that object. Use native print styles for PDF/share before adding dependencies.

## Verification

- Assert exactly 4 pillars.
- Assert exactly 4 topics under each pillar.
- Assert at least 10 themes under every topic.
- Assert unique IDs for pillars and topics.
- Render and click every topic programmatically or through the browser.
- Check console errors and a narrow viewport.
- Confirm exported JSON matches the rendered counts.
- Label estimates and scenarios explicitly; never present them as measured results.
