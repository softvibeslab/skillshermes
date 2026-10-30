---
name: agent-capability-explainers
description: Create stakeholder-facing explainers for AI-agent capabilities across video, infographic, demo, and web formats while controlling brand/project disclosure.
version: 1.0.0
metadata:
  hermes:
    tags: [agents, explainer, infographic, video, landing-page, anonymization]
---

# Agent Capability Explainers

Use when someone needs a simple, fast explanation of what AI agents do, how they differ from chatbots, or how an agent ecosystem can apply across businesses.

## Default communication posture

Start with **capabilities, roles, workflow, evidence, and human control**. Do not lead with an inventory of internal project names, client names, bots, repositories, or technical profiles.

Before producing externally shareable material, decide the disclosure level:

1. **Generic** — no product, client, project, bot, repository, or platform-instance names.
2. **Portfolio** — approved product/project names, but no private operational detail.
3. **Case study** — one approved case with evidence and redacted data.

If the user says to focus on agents without names, apply **Generic** across every artifact, including filenames, captions, narration, alt text, subtitles, metadata, examples, and embedded media.

## Core framing

Prefer:

> Un chatbot responde. Un agente tiene un rol, entiende el contexto, utiliza herramientas y entrega trabajo verificable.

Explain the system as:

> Solicitud → Contexto → Herramientas → Ejecución → Evidencia → Decisión humana

Emphasize that people retain sensitive decisions such as publishing, paying, signing, sharing private data, or committing the business.

## Recommended deliverable ladder

Stop at the first set that meets the audience's need:

1. **Fast understanding:** 16:9 infographic + 60–90 second video.
2. **Trust:** add a five-minute demo showing request → action → evidence.
3. **Exploration:** add a lightweight self-contained web page embedding the first two assets.
4. **Authority:** add a podcast only after several narratable cases exist.
5. **Measurement:** add a dashboard only after metrics are instrumented and verifiable.

Do not start with a podcast when the audience asked to understand quickly. Do not build a dashboard full of estimates or decorative numbers.

## Workflow

### 1. Extract the real request

For audio or informal messages, transcribe first and identify:

- audience and prior knowledge
- decision they need to make
- time available
- requested level of simplicity
- disclosure constraints

### 2. Define one message

Use one sentence that explains:

- what an agent is
- what it can execute
- what evidence it leaves
- what remains under human control

### 3. Describe roles generically

Use role families rather than project labels, for example:

- commercial
- operations
- software
- marketing
- executive
- experiences
- learning/community
- consent-based connections

Describe observable work, not vague benefits.

### 4. Build once, derive formats

Create a single approved content source, then derive:

- infographic labels
- video narration and scene text
- demo script
- landing-page copy
- subtitles and alt text

This prevents drift between formats.

### 5. Verify disclosure, claims, and fidelity

Before delivery:

- inventory every artifact and separate presenter-only/internal pages from public assets
- search all text assets for forbidden names
- audit every percentage, multiplier, absolute promise, “typical result,” and “real case”; require a source, baseline, period, and observed/estimated/illustrative label, otherwise remove or relabel it
- inspect infographic and video frames for cropped text
- verify video dimensions, duration, and audio stream
- open every dynamic page through a local HTTP server and check console output; a console warning in a 3D/WebGL experience is a failed check even if the scene appears to render
- confirm essential content is visible by default when JavaScript, animation libraries, or scroll observers fail
- confirm embedded media loads and actually advances during playback
- exercise the primary interaction and one FAQ/accordion path
- test desktop, tablet, and mobile viewports; assert `scrollWidth === clientWidth`
- inspect full-page screenshots at each breakpoint
- verify public pages do not expose filenames, presenter timings, keyboard shortcuts, or internal disclosure notes
- package only approved deliverables and run an archive integrity check

Do not rely on a single full-page browser screenshot when content uses scroll-triggered reveal. Capture tools may not fire `IntersectionObserver`, making valid sections look empty. Prefer progressive enhancement: content visible by default, animation optional. Decorative glows and pseudo-elements can also inflate mobile `scrollWidth`; use clipping/containment at the section or component boundary and verify programmatically.

## Visual guidance

A strong default is a dark technical-schematic style with one accent color and high contrast. Use precise typography and a clear process line. Avoid fake dashboards, decorative metrics, generic stock photography, and icon-heavy SaaS grids.

When the user supplies a reference site, extract **principles rather than identity**:

1. inspect the live page visually and structurally;
2. name the reusable patterns (hero hierarchy, product UI as proof, spacing rhythm, surface system, CTA posture);
3. explicitly list what must not be copied (logo, copy, exact palette/gradient, proprietary illustrations, testimonials, metrics, distinctive layouts);
4. transform the patterns around the explainer’s own differentiator — usually evidence, traceability, and human approval;
5. preserve the previous version before promoting the redesign.

For agent explainers, prefer a functional hero over a decorative one: let visitors describe a desired outcome and reveal a role, authorized tools, and expected evidence. Seed the result so the page still explains itself before interaction.

When the user asks for more animation, do not merely add loops to every card. Add one shared, controllable use-case simulator that shows `Entrada → Agente → Herramientas → Evidencia`, synchronizes visible step state with its progress label, and lets each role card open its own case. Keep pending states readable, include pause/restart, and verify a non-default case end to end. See `references/agent-capability-explainers-agent-capability-explainers-interactive-use-case-simulator.md`.

For a 16:9 explainer:

- one dominant promise
- one six-step workflow
- up to eight role families
- one human-control statement
- no internal architecture unless requested

## Video guidance

Default to six scenes:

1. multitasking problem
2. chatbot vs agent
3. specialized roles
4. execution cycle
5. human control
6. outcome

Use per-scene narration so scene durations match audio naturally. Render essential narration into the scene when platform subtitle support is uncertain, and also provide an SRT file.

## Demo guidance

A demo must show evidence, not only conversation:

1. person asks for a result
2. agent consults context/rules
3. agent performs an authorized action
4. agent returns files, changes, prioritized work, or alerts
5. person approves any sensitive next step

## Pitfalls

- **Portfolio dump:** listing every internal agent makes the explanation harder. Group by role and outcome.
- **Name leakage:** removing names from headings is insufficient; inspect narration, subtitles, alt text, filenames, metadata, posters, and ZIP contents.
- **Chat simulation without evidence:** a smart-sounding reply is not a convincing agent demo.
- **Metrics without instrumentation:** use cases and artifacts until measurements are trustworthy.
- **Format-first planning:** choose the communication goal before choosing podcast, dashboard, video, or infographic.
- **Inconsistent derivatives:** approve one canonical content source before rendering multiple formats.
- **Reference-site cloning:** borrow hierarchy and interaction posture, never brand identity, claims, distinctive assets, or exact composition.
- **Invisible-by-default content:** scroll reveals that require JavaScript can turn exports, crawlers, or failed observers into blank pages; keep essential content visible without animation.
- **Decorative mobile overflow:** oversized glows and clipped card ornaments can silently widen the document even when the body hides overflow; assert viewport width at mobile and tablet sizes.
- **Unverified interactions:** a page loading is not proof that the demo, video, and accordion work; execute each primary path before packaging.

## Supporting material

See `references/agent-capability-explainers-agent-capability-explainers-multiformat-kit.md` for a compact production and verification recipe for a video + infographic + standalone HTML kit.
See `references/agent-capability-explainers-agent-capability-explainers-reference-led-landing-redesign.md` for a compact recipe to adapt a live reference site into an original, responsive agent explainer and verify it across breakpoints.
See `references/agent-capability-explainers-agent-capability-explainers-audit-existing-explainer-kit.md` for auditing an existing multi-asset kit, validating claims, separating internal/public materials, and catching animation or WebGL failures.
See `references/agent-capability-explainers-agent-capability-explainers-interactive-use-case-simulator.md` for turning static role cards into a synchronized, accessible Entrada → Agente → Herramientas → Evidencia demo with pause/restart controls.
