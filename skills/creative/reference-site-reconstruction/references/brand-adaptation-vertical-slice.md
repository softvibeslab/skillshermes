# Brand adaptation through a cinematic vertical slice

## Case context

The conversation adapted the interaction concept of Moooi's A Life Extraordinary to Cisne Negro, an independent brewery. This is a design-method example, not a current deployment report or a specification to apply to every brand.

The useful distinction: borrow a spatial journey, not the reference brand's social positioning. A neighborhood brewery needs approachable atmosphere and immediate menu/location access rather than distant luxury.

## Reusable sequence

1. Inspect both sites and read the destination project's README, design guidelines and content schema.
2. Map a compact journey: cover → one scene → one meaningful product interaction. Do not build all proposed rooms before this slice is visually reviewed.
3. Isolate the prototype on a separate route. Preserve the current landing and reuse its navigation destinations.
4. Consume the canonical catalog. In this case it was `sitio/data/menu.json`; discover the actual source in each project. Keep names, sizes and prices synchronized rather than duplicating them in page markup or scripts.
5. Compose background, scenery, products and foreground as depth layers. CSS variables updated through requestAnimationFrame are sufficient for modest parallax; pause offscreen updates and disable motion in JS and CSS for reduced-motion users.
6. Use native form controls for mutually exclusive product selection (fieldset, legend, radios). Do not replace keyboard semantics with clickable decorative images.
7. Review a screenshot at the real reading size before expanding the journey. Check descriptions, portion labels, prices and CTA contrast against every overlapping layer.

## Assets and fidelity gate

- A CSS-illustrated glass is a layout placeholder, not a product photograph.
- Label illustrative compositions visibly when they might be mistaken for actual products.
- Photographic immersion requires coordinated cutouts, perspective, illumination and contact shadows; adding a renderer does not solve mismatched art.
- Preserve source aspect ratios. Choose crop intentionally and verify mobile crops.
- Resolve art direction with one scene before generating or sourcing many expensive assets.

## Verification matrix

Reuse the project's test runner when present. Keep one reproducible journey check plus screenshots:

- Desktop and mobile: enter, reach the scene, select each product, follow the menu action.
- Keyboard: visible focus and native selection behavior.
- Reduced motion: no parallax, no hidden content awaiting animation.
- JavaScript disabled: readable core content and working business links.
- Catalog request failure: explicit fallback, no fabricated prices or blank essential navigation.
- Product change: displayed price/portion/name matches the loaded source record.

Functional tests and visual review are separate gates. A passing interaction test does not prove visual fidelity, and a screenshot cannot establish keyboard behavior or animation quality.

## Honest handoff

State what was implemented, what remains placeholder art, whether it is local or published, and exactly which checks ran. Do not broaden a summarized test count into unsupported claims about keyboard, network failure or every breakpoint. After a handoff or compaction, verify server availability and the actual test assertions before presenting a local URL or detailed pass claims as current.
