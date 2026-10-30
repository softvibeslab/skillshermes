---
name: agent-portfolio-communication
description: Turn a portfolio of AI agents, projects, demos, and voice notes into a simple buyer-facing explanation, visual map, demo sequence, and content roadmap. Use when someone asks for a pamphlet, explainer video, infographic, podcast, dashboard, pitch, or “mundane” explanation of what an agent ecosystem does.
version: 0.1.0
metadata:
  hermes:
    tags: [agents, portfolio, storytelling, explainer, infographic, demo, pitch]
---

# Agent Portfolio Communication

Convert a technically messy agent portfolio into a short, evidence-based story a non-specialist can repeat.

## Core principle

Explain capabilities and outcomes, not profile directories, model names, or architecture trivia.

A useful default distinction:

> A chatbot answers questions. An agent has a job, uses tools, works from project context, and leaves evidence.

## Workflow

### 1. Recover the real request

Read or transcribe every source completely. Extract:

- audience and prior knowledge;
- decision they are considering;
- time available to understand;
- requested medium;
- implicit job-to-be-done.

A request for a “podcast, infographic, dashboard, or whatever works” is usually a request for rapid comprehension, not four deliverables.

### 2. Inventory the portfolio

Inspect the durable definitions for each agent or project before writing the story. Capture:

- business line;
- user problem;
- agent role;
- tools or channels;
- observable output;
- approval boundary;
- status confidence.

Separate facts from inference. “Configured,” “recent activity observed,” and “currently running” are different claims. Never expose tokens, private contact data, customer data, or internal credentials.

### 3. Consolidate before presenting

Do not market one technical profile as one product. Group overlapping profiles into 5–8 understandable business lines. Mark generic, duplicate, legacy, or undocumented profiles for internal cleanup instead of inflating the public count.

For each line, use this sentence shape:

> For [user], the agent [does concrete work] and delivers [observable evidence], while a person approves [sensitive decision].

### 4. Pick the smallest medium that solves comprehension

Use this ladder:

1. one-sentence message;
2. one-page visual map;
3. 90-second explainer video;
4. five-minute live demo with evidence;
5. lightweight landing page;
6. podcast for authority and reusable content;
7. dashboard only when reliable metrics exist.

Do not start with a podcast when the audience needs a quick explanation. Do not build a dashboard from estimated or decorative numbers.

### 5. Build the rapid explainer kit

Default kit:

- **Message:** one paragraph suitable for chat.
- **Infographic:** person → channel → agent → tools → evidence, with business lines around the center.
- **Video:** problem, distinction, 3–5 cases, process, human boundary, call to action.
- **Demo:** two cases only; show request → execution → evidence → approval.
- **Landing page:** hero, chatbot-vs-agent, process, three cases, proof, replication path, CTA.

See `references/agent-portfolio-communication-agent-portfolio-communication-rapid-explainer-kit.md` for a reusable structure and validation questions.

### 6. Lead with evidence

Prefer screenshots, reports, tests, diffs, prioritized leads, published content, or completed workflows over claims such as “autonomous” or “powerful.”

Every case should answer:

1. What was the human trying to accomplish?
2. What did the agent actually do?
3. What evidence was produced?
4. What remained under human control?

### 7. Validate comprehension

Ask a fresh viewer to explain, without help:

- the difference between chatbot and agent;
- one job an agent performs;
- one decision a person retains;
- one use case they would replicate.

If they cannot, simplify the story before adding more media.

### 8. Build a content control tower only when requested

When the deliverable combines content strategy, a visual map, and agent coordination, model the strategy as canonical structured data before drawing the interface. For the common strict method, verify exactly 4 pillars × 4 topics × at least 10 themes: 160 themes is the minimum complete inventory. A taxonomy-only dashboard is a scaffold, not a finished strategy.

Use the lotus as navigation, Design Thinking as the editorial feedback loop, and agents as explicit jobs with visible human approval boundaries. See `references/agent-portfolio-communication-agent-portfolio-communication-content-strategy-control-tower.md` for the data model, role map, minimal implementation, and verification checks.

## Dashboard gate

Only recommend a public dashboard when the project consistently records at least:

- tasks received and completed;
- evidence-backed completion;
- escalations or failures;
- a project-specific business result;
- an honest measurement method.

Estimated time saved may be labeled as estimated; never present it as measured.

## Podcast gate

Use a podcast after there are at least three narratable cases with a problem, action, evidence, and lesson. Treat each episode as a source for clips, a carousel, an infographic, short posts, and a refreshed case page.

When the podcast's purpose is understanding a newly analyzed agent catalog rather than proving market authority, a source-grounded educational episode is valid earlier. Anchor every repository fact to the analyzed commit, distinguish upstream facts from local proposals, include one complete workflow example, and finish with glossary plus comprehension questions.

## External catalogs, knowledge bases, and Wikis

When incorporating a large external agent catalog:

1. pin the analyzed commit and verify its license, attribution, catalog structure, and native integration;
2. prefer lazy search/load/delegate routing over one persistent profile per specialist;
3. keep canonical explanations in a versioned knowledge base and use the Wiki only as a concise navigation layer;
4. stage Wiki pages locally before publishing to the platform's separate Wiki repository;
5. verify the public remote before saying the Wiki is published.

See `references/agent-portfolio-communication-agent-portfolio-communication-source-grounded-agent-wiki-and-podcast.md` for the reusable inspection fields, minimal document set, podcast-prompt structure, and publication sequence.

## Pitfalls

- Listing every agent profile instead of telling a business story.
- Calling recent logs proof that a service is live now.
- Using model names and orchestration jargon before explaining value.
- Showing more than two cases in a live demo.
- Building a dashboard before instrumentation.
- Treating a podcast as the fastest onboarding medium.
- Turning every upstream specialist into a permanent profile instead of routing lazily.
- Copying a changing upstream catalog into the portfolio without pinning commit, license, and attribution.
- Duplicating long canonical text in a platform Wiki until the two versions drift.
- Calling locally staged Wiki pages “published” before remote verification.
- Claiming replacement of people instead of making approval boundaries explicit.
- Publishing internal or customer data as “evidence.”

## Verification checklist

- [ ] All sources were read or transcribed completely.
- [ ] Audience, decision, and time-to-understand are explicit.
- [ ] Portfolio facts are separated from status inference.
- [ ] Overlapping profiles are consolidated into business lines.
- [ ] Every featured case includes observable evidence.
- [ ] Human approval boundaries are visible.
- [ ] The chosen medium is the smallest one that solves the request.
- [ ] Podcast and dashboard gates were applied.
- [ ] External catalog claims are tied to a verified commit and license.
- [ ] Persistent profiles are justified by memory, credentials, channel, workspace, or recurrence.
- [ ] Canonical knowledge and Wiki navigation are separated.
- [ ] Public Wiki/repository claims were verified remotely after publication.
- [ ] A fresh-viewer comprehension test is included.
