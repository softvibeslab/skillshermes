# Label-led scenes and trustworthy visual evidence

## Reusable implementation pattern

- Inspect existing artwork rather than inferring content from filenames. A square illustration that includes a glass and label is not a bottle cutout; show the complete composition with its real aspect ratio and an honest caption.
- Extract a small pigment set and distinct framing/type treatment for each product. In the brewery example, Alarma supplied cream, mustard, coral and black comic/newsprint framing; Agua Puerca supplied cream paper, deep coffee, caramel foam and hand-drawn marks. These are project examples, not global defaults.
- Keep canonical JSON authoritative for name, style, ABV, tasting notes and prices. Existing artwork can contain printed values; do not silently edit either source to reconcile them.
- Scope theme variables to a scene selected by stable ID. A native radio change updates that ID, one visible artwork, caption and live product detail. Remove abandoned placeholder selectors, DOM and JavaScript references.
- Static HTML should expose a meaningful initial illustration and a working menu link even if data fetch or JavaScript fails.

## Catalog coverage gate

A request for all label-bearing products requires an inventory, not just two representative designs. Join canonical product IDs to existing asset paths, then visually classify candidates; a matching filename alone does not establish that the image contains a label. Use explicit path mapping when filenames differ rather than renaming assets or assuming every ID has a JPEG.

Keep a compact working matrix: product ID | actual asset | visual classification | theme implemented | checks verified. Unknown artwork stays uninspected, not silently excluded. Complete verified label-bearing products before optional audio, extra transitions or decorative work. If only a slice is delivered, name covered and remaining products and explain missing assets without claiming catalog completion.

Do not infer coverage from a suite's total pass count: parameterize product selection checks over the eligible inventory, or enumerate which products the existing tests actually exercise.

## Acceptance checks

For every theme at desktop, mobile and narrow-mobile sizes:
1. Select via radio and assert checked value, scene ID, canonical details and caption agree.
2. Assert exactly one artwork is visible, its source matches the selected product, and it decodes with `complete && naturalWidth > 0`.
3. Compare computed scene background, text color, accent token and title treatment between products—not merely the selected-button style.
4. Switch both directions with arrow keys; verify focus and image/theme remain synchronized.
5. Check overflow in every theme, navigation, no-JavaScript fallback, failed fetch/retry and reduced-motion state.
6. Inspect generated images, including small text against texture. Regenerate screenshots after the final CSS change.

## Screenshot isolation: observed diagnostic, not a universal Playwright defect

In one Chromium/Playwright run, a mobile context initially reported `(pointer: coarse) = true` and `data-motion = off`. After `locator.screenshot()` captured a section taller than its viewport, the same context reported `coarse = false` and `data-motion = subtle`. A separate `page.screenshot({fullPage:true, clip})` experiment reproduced the observation. The screenshot operation was therefore an important variable; this was not evidence that the application ignored reduced-motion preferences.

When a media-dependent assertion fails after capture, record viewport, pointer and reduced-motion queries before and after the capture in a minimal reproduction. Do not weaken the assertion or hard-code the application's motion state to make a test pass. Keep behavioral assertions independent from potentially state-changing evidence collection, using fresh equivalent contexts when appropriate, and verify the chosen approach in the current browser/version.

No replacement capture technique was validated in that session: a proposed CDP diagnostic was denied before execution. Do not describe CDP capture as a proven workaround or retry a denied action through another tool.

## Evidence freshness

Use a fresh run-specific evidence directory, or an explicit run manifest/status, so an aborted run cannot leave an older `results.json` looking current. Record which captures belong to the final source revision. If a run stops, report the exact failed assertion and label earlier captures as stale when later visual edits exist. Artifact existence alone does not establish a passing run or final-state fidelity.
