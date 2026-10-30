# Reference-led landing redesign for agent explainers

Use this when a user asks for an explainer “like” a live AI/SaaS site. The goal is to transfer effective patterns without cloning identity or unsupported claims.

## 1. Analyze the reference

Capture both the accessibility structure and a full-page visual. Record:

- promise and hero hierarchy;
- whether the product UI itself is the hero;
- palette roles, typography posture, surfaces, borders, radii, spacing and motion;
- narrative order from promise to proof to CTA;
- trust devices and whether their claims are verifiable;
- weaknesses such as excessive length, repeated CTAs, tiny type or fake-looking proof.

Write two short lists: **patterns to transform** and **elements not to copy**.

## 2. Choose an original differentiator

For agent capability pages, make the page visually about:

- role;
- context;
- authorized tools;
- evidence;
- approval boundary.

A useful interactive hero accepts a desired outcome and returns those four fields. Show a seeded example before interaction so the concept survives disabled JavaScript, screenshots and impatient visitors.

## 3. Build with progressive enhancement

- Essential content is visible by default.
- JavaScript enhances demos, accordions and motion but does not reveal the entire page.
- Respect `prefers-reduced-motion`.
- Use semantic headings, real labels, visible focus states and 44px touch targets.
- Do not invent metrics, testimonials or operational status.
- Preserve the previous artifact as a versioned file before replacing the main entry point.

## 4. Responsive verification recipe

Check at least 390×844, 768×1024 and 1440×900.

For every viewport:

1. load until network idle;
2. collect JavaScript errors;
3. assert `document.documentElement.scrollWidth === document.documentElement.clientWidth`;
4. exercise the primary demo and verify its output changes;
5. open an accordion item;
6. play embedded video and verify `currentTime > 0`;
7. capture a full-page screenshot and inspect headline wrapping, card density, video controls and final CTA.

If mobile width is inflated, inspect elements and pseudo-elements extending outside the viewport. Oversized radial glows and off-canvas card ornaments commonly cause it. Clip or contain them at the owning section/component; do not rely only on `body { overflow-x: hidden; }`.

## 5. Full-page capture pitfall

Scroll-triggered `IntersectionObserver` reveals may remain at `opacity: 0` in automated full-page captures because the tool does not scroll like a person. The result looks like huge blank sections. Prefer content visible by default; if reveal motion is required, add it as a nonessential enhancement rather than the visibility gate.

## 6. Packaging gate

Before replacing the shareable archive:

- search all text assets for forbidden brands/projects;
- verify the promoted `index.html` is the intended version;
- include only approved assets and documentation;
- run an archive integrity test;
- reopen the packaged main page once before delivery.
