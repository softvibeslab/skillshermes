# Multiformat Explainer Kit

Use this reference after the content and disclosure level are approved.

## Canonical source

Maintain one Markdown source containing:

- message and promise
- six-step workflow
- role families
- human-control boundary
- six video scenes
- exact infographic labels

All formats derive from this file.

## Minimal artifact set

```text
kit/
├── index.html
├── infographic.png
├── video.mp4
├── video.srt
└── source.md
```

Keep `index.html` self-contained except for sibling media files. Avoid dependencies unless the target project already has them.

## Deterministic infographic

When text accuracy matters, prefer HTML/SVG or Pillow over image generation. A reliable 1920×1080 layout is:

- top: category label + promise
- middle: six workflow boxes with arrows
- lower middle: two rows of four role families
- bottom: high-contrast human-control statement

Run a visual pass at full resolution and thumbnail size. Check accents, wrapping, margins, and arrow collisions.

## Narrated video

Generate one audio file per scene rather than one long narration. Then:

1. render one 1920×1080 image per scene
2. probe each audio duration with `ffprobe`
3. loop its matching image for that duration
4. encode each segment with H.264 video and AAC audio
5. concatenate segments
6. generate SRT timestamps from cumulative durations

Per-scene audio avoids manual timing arithmetic and keeps scene transitions aligned.

If FFmpeg lacks text/subtitle filters, render the narration into each scene image with Pillow. Still provide the SRT as a separate accessibility asset.

## Landing page

Embed the video and infographic near the top. Follow with:

1. chatbot vs agent
2. execution cycle
3. generic role families
4. conceptual evidence demo
5. human-control boundary
6. repeated CTA

Use real `<video controls>` and meaningful image alt text. Ensure mobile hit targets are at least 44px and respect `prefers-reduced-motion`.

## Verification checklist

### Disclosure

Search all textual files for forbidden product/client/project names. Also inspect:

- filenames
- subtitles
- image alt text
- video scene text
- HTML titles and footer
- ZIP manifest

### Media

Use `ffprobe` to confirm:

- video width and height
- duration
- H.264 or broadly supported video codec
- AAC or broadly supported audio codec
- non-empty audio stream

Create a six-frame contact sheet and inspect it visually for consistency and cropping.

### Web

Serve from a free localhost port, then verify:

- correct title and content
- media metadata loads
- no JavaScript/console errors
- video duration and dimensions are reported
- responsive CSS handles the workflow and role grids

### Package

ZIP only the public assets. Test the archive before delivery. Do not include source recordings, internal inventories, private screenshots, credentials, logs, or unrelated planning files.
