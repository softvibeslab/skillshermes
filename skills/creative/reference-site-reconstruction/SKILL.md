---
name: reference-site-reconstruction
description: Analyze interactive reference websites and turn verified visual and technical observations into a minimal recreation plan and coding-agent prompt. Use for recreating a website, reverse-engineering a visual experience, identifying animation techniques, selecting Claude Code or Codex skills, or planning cinematic showroom prototypes from URLs.
---

# Reference Site Reconstruction

Translate a reference into an evidence-backed implementation brief, not an assumed technology stack. Default deliverable is analysis plus a reusable prompt; do not build or publish unless requested.

## 1. Establish scope and available inspection tools

Normalize a malformed URL without changing its destination. Check available browser, screenshot and DOM-inspection tools. Prefer a live browser for interactive experiences; use HTTP extraction for static sources. If browser inspection is unavailable, use supplied screenshots or request them and explicitly limit claims about motion.

Defaults: inspect the supplied page, cover, first scene and one meaningful transition; propose one vertical slice, reuse the existing project stack, and do not download proprietary assets for publication.

## 2. Observe state changes

Capture the cover, activate entry and inspect the resulting scene. Test one object interaction and one navigation control where available. Refresh accessibility references after changes.

A successful scroll tool response does not prove the page advanced. If the screenshot is unchanged, try its visible next/scroll control. Report the distinction without declaring the site broken. Before/after screenshots establish different states, not transition timing or choreography; observe intermediate frames or record a sequence before describing the motion precisely.

## 3. Cross-check implementation evidence

Inspect scripts, DOM controls, canvas/video elements, image sources and relevant loaded resources. Label inventories as partial when filtered or capped.

Maintain three categories:
- Observed: a named script loaded, independent image URLs exist, a button changes rooms.
- Inferred: likely layered 2.5D composition or canvas particle effects.
- Proposed: the stack recommended for the new implementation.

A canvas is not proof of 3D. Bundle string matches are leads, not proof of a dependency's role; absence of a marker is not proof of absence. No video elements in one state does not establish that the entire site lacks video. Asset filenames do not prove alpha transparency. Read pixels and inspect actual formats before promising clean cutouts.

## 4. Design the smallest faithful slice

Map composition, typography, object layers, shadows, interactive states, audio and navigation. Start with cover → one complete scene → one transition. Prefer DOM/CSS and the project's current stack; add animation or rendering libraries only for a named requirement. Do not mistake photorealistic assets for a requirement to model an entire 3D environment.

Asset quality is a separate dependency: match perspective, scale, lighting and shadows. Use owned/licensed art for publication. Label placeholders and distinguish visual fidelity from functional completeness.

### Adapt the reference to an existing brand

When given both an inspiration URL and an existing business site, separate the inspiration's interaction grammar from the destination's identity. Read the destination's design guidelines and canonical content source first. Transfer scene progression, depth and object interaction—not automatically its luxury tone, palette or typography. Keep practical business actions accessible throughout the cinematic experience.

For an authorized prototype, prefer a separate route so the existing landing remains intact. Bind product names, portions and prices to the existing data source; never invent tasting notes or availability to fill a composition. Clearly distinguish editorial descriptions from verified product claims.

Use a small DOM/CSS depth stack and requestAnimationFrame-driven CSS variables when sufficient; rendering libraries remain options for requirements that actually need them. Make content readable without JavaScript and handle failed data loading explicitly. Approve one complete scene before multiplying scenes: illustrated placeholders can prove layout and interaction, but cannot establish photographic fidelity.

### Let real product artwork govern the scene

When the user supplies real labels or illustrations, inspect their pixels before designing. Prefer those assets over generic CSS vessels or invented bottle photography. Present an illustration honestly as illustration, preserve the original file, and derive the scene's palette, typography, framing and material treatment from it. For this user's label-led redesigns, a new image inside an otherwise generic scene is not enough: the surrounding experience must visibly belong to the selected product.

When the request covers all products with labels, inventory the canonical catalog against available artwork before choosing examples. Track each product as verified label/illustration, other imagery, missing asset, or not yet inspected. Two polished themes are a vertical slice, not completion of the whole catalog; state remaining products explicitly and do not add unrequested sound or cinematic refinements ahead of coverage. See `references/label-led-scenes-and-evidence.md` for the coverage gate.

Bind selection to one stable product ID (for example, `data-beer` on the scene) and scope CSS variables there. Update artwork visibility, accessible descriptions and canonical product details together; never transcribe potentially stale numbers from embedded artwork into the data source. Remove superseded decorative DOM, styles and callers instead of accumulating override layers. Preserve explicitly excluded hero/header/navigation and unrelated repository work; read complete affected files and callers before editing.

Use native radio controls and retain keyboard operation, visible focus, static artwork/menu access without JavaScript, network-failure recovery and reduced-motion behavior. Keep textures subordinate to small text; inspect the final pixels at actual mobile width.

## 5. Select skills and write the agent prompt

Choose a small relevant set: visual direction, cinematic composition if applicable, implementation, then testing/accessibility. Consult available skills dynamically. Skills visible in the current agent are not necessarily installed in Claude Code or Codex; verify paths before presenting setup commands.

The copyable prompt must include reference URL, scope, observed behaviors, missing assets, stack reuse, no unauthorized deployment, and acceptance criteria. Require semantic controls, keyboard/touch navigation, visible focus, optional audio and reduced-motion handling in JavaScript as well as CSS. Do not make essential interaction hover-only or trap scrolling.

## 6. Deliver and verify

For analysis: provide observations, evidence/uncertainty, minimal implementation plan, skill shortlist and ready-to-use prompt. Do not claim a full library audit when only its catalog was reviewed.

For an authorized build: run the build and a small journey test (enter → interact → advance), inspect desktop/mobile screenshots, test keyboard and reduced motion, and list remaining differences honestly. Pause effects outside the viewport and defer noncritical assets.

Report only checks whose assertions or outputs were inspected. A summarized pass count does not establish keyboard, network-failure or no-JavaScript coverage. After resuming from a handoff, recheck the local server before presenting its URL as available. Review text and price legibility at real viewport sizes separately from functional test results.

Keep visual evidence and behavioral assertions independent: if capture appears to change emulated media or viewport state, compare before/after state and reproduce before changing application logic. Use fresh run-specific evidence or a run manifest; do not report an old results file as a current pass. Regenerate evidence after final visual edits, or explicitly mark it stale.

## References

- `references/label-led-scenes-and-evidence.md` — Real-art theme mapping, radio/artwork acceptance checks, screenshot-state diagnostics and evidence freshness.
- `references/brand-adaptation-vertical-slice.md` — Brand-to-reference translation, canonical product data, layered prototype and verification matrix from the brewery adaptation.
- `references/layered-showroom-evidence.md` — Moooi example and evidence boundaries; historical observations, not a live specification.
