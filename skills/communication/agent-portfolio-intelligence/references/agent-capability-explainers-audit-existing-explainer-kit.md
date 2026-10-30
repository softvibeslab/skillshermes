# Audit an Existing Agent-Explainer Kit

Use this when reviewing a folder of presentations, landing pages, brochures, infographics, guides, or 3D demos before public sharing.

## 1. Inventory and classify

List every artifact and label it:

- presenter-only/internal index
- primary public explainer
- follow-up/shareable asset
- optional experimental experience

Flag repeated assets that tell the same story. Prefer one canonical source and the smallest public set that covers presentation, exploration, and follow-up.

## 2. Audit claims before aesthetics

Search all files for percentages, multipliers, absolutes, time savings, ROI, “real case,” “typical result,” “zero errors,” and “24/7.”

For each claim require:

- source or case identifier
- measurement period and baseline
- what was measured
- whether it is observed, estimated, or illustrative

If evidence is unavailable, remove the number or relabel the material as an illustrative scenario. Never call a composite or invented example a real case. Avoid absolute operational promises.

## 3. Separate internal and public language

Internal pages may contain filenames, presenter timings, keyboard shortcuts, disclosure notes, and audience cues. Public pages should not expose those details. Give each public asset a clear owner/brand, purpose, CTA, scope, and human-control statement.

## 4. Verify every dynamic page

For each HTML page:

1. Open it through a local HTTP server, not only `file://`.
2. Read browser console output.
3. Exercise the main CTA and one secondary interaction.
4. Capture the initial viewport and a full-page screenshot.
5. Verify essential content remains visible if animation libraries fail or JavaScript is disabled.
6. Check desktop, tablet, and mobile overflow.
7. Confirm external CDN/font dependencies are intentional.

Content should be visible by default; JavaScript may add animation classes but should not be required to reveal core sections.

## 5. WebGL/Three.js pitfall

Do not pass the result of a transform setter into `Object3D.add()`:

```js
// Wrong: position.set() returns Vector3
scene.add(new THREE.PointLight().position.set(9, 7, 0));

// Correct
const light = new THREE.PointLight();
light.position.set(9, 7, 0);
scene.add(light);
```

Treat any console warning from a 3D scene as a failed verification even when the rest of the scene appears to render.

## 6. Recommended output

Report in this order:

1. verdict and public-readiness
2. strongest reusable assets
3. critical trust/content problems
4. functional defects with file/line evidence
5. minimum correction sequence
6. what was deliberately left unchanged
