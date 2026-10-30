---
name: designrush-app-inspiration
description: Researches current, award-winning mobile app design references from DesignRush and converts them into evidence-backed UI/UX direction without copying. Always use when planning, designing, redesigning, building, reviewing, or improving a mobile app; when the user asks for modern app inspiration, winning app designs, visual benchmarks, competitor UI references, moodboards, design systems, screens, flows, or polished mobile UI. Pair with mobile-app-ui-design and ui-ux-pro-max.
---

# DesignRush App Inspiration

Use live DesignRush references before committing to a mobile app direction. Inspiration is evidence; never clone another product's trade dress, assets, copy, or exact screen composition.

Canonical source: `https://www.designrush.com/best-designs/apps`

## Defaults

| Parameter | Default |
|---|---|
| References | 5 relevant designs |
| Detail pages | 3 strongest matches |
| Priority | award winner > relevant featured > latest/popular |
| Freshness | live fetch during the current task |
| Output | benchmark + principles + proposed direction |
| Copying | prohibited; synthesize patterns only |

## Step 1: Detect the research path

1. Detect a dedicated URL-fetch tool, browser automation, vision analysis, and networked terminal fallback.
2. Fetch `https://www.designrush.com/robots.txt` before multi-page exploration.
3. Prefer dedicated fetch for listing/detail pages; use browser automation if rendering is required; use a polite single-page HTTP fetch only when web tools are unavailable.
4. If live access fails, say so and continue with `mobile-app-ui-design` plus `ui-ux-pro-max`; never present cached examples as current.

Gate: the canonical page succeeds or the live-access limitation is explicit.

## Step 2: Translate the brief into filters

Identify product category, closest DesignRush industry, audience, usage context, platform, primary job, critical flow, desired tone, density, accessibility, and trust level. Use only category/tag routes exposed by the current listing; do not invent URLs or crawl broad pagination.

Gate: one sentence defines a relevant reference.

## Step 3: Build the evidence set

Select up to five references and record design name, URL, industry/tag, visible winner/featured status and score, studio, preview image, and relevance. Do not equate view counts or featured placement with a jury award; label each signal exactly as shown.

Gate: every reference has a DesignRush URL and an explicit relevance reason.

## Step 4: Deep-review the strongest references

Open up to three detail pages. Inspect images with vision instead of inferring appearance from titles or alt text. Apply `references/app-design-review-framework.md` to hierarchy, navigation, typography/color roles, spacing/density, components, visible motion cues, accessibility risks, signature element, and exclusions. Mark unavailable evidence `not verified`.

Gate: observed facts and interpretations are separate.

## Step 5: Synthesize one coherent direction

Extract transferable principles—hierarchy, rhythm, navigation, feedback, or controlled visual tension—not exact palettes, logos, illustrations, copy, assets, or layouts. Name one signature idea and one deliberate restraint. An award is not proof of usability, accessibility, or conversion.

Pair with:

- `mobile-app-ui-design` for flows and native conventions;
- `ui-ux-pro-max` for the design system;
- `vercel-react-native-skills` for React Native/Expo;
- `apple-hig-expert` for Apple-platform compliance.

## Step 6: Deliver and continue

Use this exact structure:

```text
1. DesignRush references — name, evidence signal, relevance, URL
2. Observed patterns — visually verified facts
3. Transferable principles — what to adapt and why
4. Recommended direction — color roles, type, rhythm, navigation, components, motion, signature
5. Do not copy — explicit exclusions
6. Confidence and gaps — fetch date and unverified evidence
```

For implementation tasks, continue into the actual design/code after the benchmark; do not stop at inspiration research.

## Reference Files

- `references/app-design-review-framework.md` — visual review rubric and evidence vocabulary.
