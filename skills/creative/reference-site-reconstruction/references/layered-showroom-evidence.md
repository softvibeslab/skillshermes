# Layered showroom: evidence example

Reference: https://www.moooi.com/en/a-life-extraordinary

These are observations from an inspection, not a guarantee of the site's current implementation. Recheck live before using them as requirements.

## Visual structure

- Cover: darkened floral/monkey artwork, large thin uppercase headline, italic serif subtitle, entry button and audio control.
- First room: patterned chairs, wall covering, rug, pig-shaped table, books, hanging lamps, flowers and basketball.
- Activating the visible scroll invitation displayed a different room with sectional sofa and coffee table. Ordinary automated scroll did not produce a verified change in the captured states.

## Technical observations

- Loaded scripts included Pixi and Pixi-particles.
- Two canvases were present; no video elements were present in the inspected state.
- Individual WebP resources represented furniture, wall, rug, objects and separate lamp-on/lamp-off states.
- The public JavaScript bundle contained GSAP markers. This supports investigating GSAP use, but does not identify the exact sequencing or prove ScrollTrigger use.
- The resource inventory was filtered and capped, not a complete asset manifest.

## What this supports

A layered image/DOM composition with canvas effects is a plausible reconstruction path. It is unnecessary to choose a full Three.js environment solely because the scene looks spatial or photorealistic.

## What it does not establish

- Exact easing, transition durations, scroll scrubbing or parallax values.
- Which specific effect uses Pixi or GSAP.
- Alpha transparency of every WebP.
- Audio playback merely from an icon or SOUND ON label.
- Mobile behavior without inspecting mobile.
- Permission to reuse public assets.

## Reconstruction acceptance checklist

1. Entry, object interaction and scene advance work via semantic controls.
2. Keyboard and touch retain all essential functionality.
3. Reduced motion disables JavaScript-driven effects without hiding content.
4. Art shares perspective, scale and lighting; placeholders are declared.
5. Desktop/mobile screenshots are reviewed for cropping and overflow.
6. The selected framework and libraries are labeled as proposed, not attributed to the reference without evidence.
