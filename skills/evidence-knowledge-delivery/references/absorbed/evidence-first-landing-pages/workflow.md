---
name: evidence-first-landing-pages
description: Plan and build corporate, product, and acquisition landing pages from mixed internal evidence, public research, brand assets, and reference templates without inventing claims, proof, or brand rules. Use when the user asks to research a company and create or plan a landing page, especially when sources are scattered or commercial status is uncertain.
---

# Evidence-First Landing Pages

Create persuasive landing pages whose strategy, copy, brand direction, proof, forms, and SEO are grounded in approved evidence.

This skill complements visual/code generators. Use it before implementation when a request includes company research, local documents, public profiles, images, existing sites, competitors, or templates.

## Core principle

A polished page is not trustworthy if its offer, audience, cases, or identity are assumed. Research first, separate facts from proposals, approve the commercial path, then build the smallest page that answers real objections.

## Workflow

### 1. Inventory the sources

Search relevant local documents, prior sessions, public pages, social profiles, supplied images, and existing project code. Record an as-of date and source path/URL.

Classify each finding:

- **Canonical / verified:** current operating docs, public facts, approved assets.
- **Verified with caveat:** real capability or artifact with limited production/commercial status.
- **Historical:** useful context, not automatically a current offer.
- **Proposed / inferred:** ICP, pricing, roadmap, metrics, or positioning awaiting validation.

Never turn a folder, demo, analysis, prospect, imported repository, or technical artifact into a claim of clients, revenue, traction, ownership, or production readiness.

Use `references/source-inventory-template.md` to structure the evidence bank.

### 2. Decide the page type

Choose one:

- **Corporate:** identity, capabilities, trust, and broad qualification.
- **Product:** one product, one user, one job, one conversion.
- **Vertical acquisition:** one segment, one painful scenario, one entry offer.
- **Campaign:** one source/audience, one promise, one action.

Do not combine a corporate overview and a vertical acquisition funnel without an explicit hierarchy. A broad corporate page can link to focused vertical pages later.

### 3. Analyze reference templates as patterns

For each reference, extract:

- information architecture and section order;
- visual hierarchy, density, typography, contrast, surfaces, and motion;
- useful interaction patterns;
- generic filler, fake proof, and unnecessary features.

Reuse structural principles only. Never copy template copy, logos, testimonials, awards, screenshots, customer marks, or stock imagery.

A hybrid is valid when intentional: e.g. a light conversion-oriented hero from one reference plus a dark product-demonstration section from another.

### 4. Treat brand assets as candidates until confirmed

Supplied images can establish a candidate palette, motifs, and typography direction, but not automatically a canonical brand system.

Confirm before final design:

- current logo/lockup and tagline;
- authorship and rights;
- colors and type choices;
- domain and public identity;
- approved photography, screenshots, or renders.

Preserve originals. Produce transparent, responsive, or vectorized derivatives only after approval. Auto-tracing requires visual review and must not be presented as the final logo by default.

### 5. Separate strategy approval from implementation approval

**Strategy gate:**

- page type;
- audience filter;
- positioning and primary outcome;
- entry offer;
- one primary CTA journey;
- at least one publishable case or demo.

**Implementation gate:**

- approved visual direction;
- stack based on the existing codebase;
- form recipient, retention, consent, and anti-spam;
- analytics and privacy;
- domain, SEO, preview, deployment, and rollback.

Do not start code while either gate contains a blocker. If the user asked only for a plan, make these decisions explicit rather than silently guessing.

### 6. Write one coherent story

Default corporate sequence:

1. Hero with audience filter and outcome.
2. Human or operational problem.
3. Product/solution flow.
4. What is built, framed as outcomes rather than disciplines.
5. Evidence.
6. Trust practices and limits.
7. One CTA.

Every section must answer a different objection. Remove sections that only repeat the promise.

Pricing, FAQ, methodology, integrations, blog, newsletter, marquees, carousels, and animated diagrams are optional. Add them only when approved content and a real user objection justify them.

### 7. Frame capabilities around outcomes

Avoid category dumps such as “strategy, design, AI, development, marketing, analytics.” Prefer an operational sequence:

1. Detect where continuity or attention is lost.
2. Build the minimum workflow/product that resolves it.
3. Connect only the assets needed to operate and measure it.

Technologies and disciplines support the story; they are not the story.

### 8. Label proof honestly

Distinguish:

- **Work and systems built:** technical artifacts, demos, development, internal testing.
- **Customer result:** approved name plus baseline, outcome, time window, and evidence.
- **Demo:** clearly labeled and never implied to be a client deployment.

One credible item beats three forced cards. Do not use “confidential case” unless concrete, visible evidence remains. Show state explicitly: demo, development, testing, preview, or production.

### 9. Make the CTA a real entry offer

“Book a call,” “send a form,” “request a diagnosis,” and “receive a map” are different conversion models. Pick one primary path and define:

- what happens next;
- who responds;
- expected response time;
- exact deliverable;
- free or paid status;
- required data and retention.

Use consistent CTA labels. Keep first contact to the minimum fields. Do not collect optional phone/business data until needed.

### 10. Choose the minimum technical implementation

Inspect the existing codebase before selecting a stack. Reuse its framework, components, tokens, form endpoint, analytics, and deployment path when suitable.

For a new simple page, prefer static HTML/Astro/native CSS and minimal JavaScript over a full client framework. Do not add a CMS, animation library, carousel, backend, or A/B framework without a current requirement.

Accessibility, security at trust boundaries, privacy, and data-loss prevention are never optional simplifications.

### 11. Ground SEO and analytics

Before canonical tags or schema, confirm:

- domain ownership;
- market and search intent;
- language/region;
- public name, logo, profiles, and business facts;
- ownership of legacy domains and redirect capability.

Use only structured data supported by confirmed public facts. Character counts for titles/descriptions are guidance, not acceptance criteria.

Prefer cookieless analytics when appropriate. Track business KPIs—qualified lead and scheduled session—not only clicks. Never send personal data or free-text form content to analytics.

Preview environments must:

- use `noindex`;
- avoid production analytics;
- avoid accepting real leads;
- use test recipients/endpoints.

Removing `noindex` is an explicit production release step.

### 12. Verify the result

For static-site publication, use `references/static-landing-release-verification.md`: discover the existing upload path before requesting new access, back up the current entry point, compare public/local hashes, test outbound forms without sending real messages, and rerun browser/Lighthouse checks on the canonical URL.

Minimum release checks:

- proposition is understandable in roughly ten seconds;
- one audience, one outcome, one primary CTA;
- claims trace to the evidence inventory;
- no unapproved logos, names, testimonials, or metrics;
- cases display honest states;
- responsive layout has no horizontal overflow;
- keyboard, focus, contrast, alt text, and reduced motion work;
- form succeeds and fails accessibly end-to-end;
- privacy and consent match actual handling;
- canonical, robots, sitemap, OG, and analytics are verified on the public URL;
- rollback is available.

## Common pitfalls

- Starting design before deciding corporate vs vertical acquisition.
- Treating a supplied historical logo as the canonical identity.
- Calling technical output a customer result.
- Offering a “diagnosis” or “map” without defining scope, price, owner, or response time.
- Using multiple CTA labels for the same action.
- Adding three cases because the template has three cards.
- Listing every capability until the positioning becomes generic.
- Adding schema before the domain and public identity are confirmed.
- Shipping preview with indexable pages, real analytics, or real lead collection.
- Copying template proof and replacing only the brand name.

## Output for a planning request

Deliver:

1. concise research synthesis with confidence labels;
2. strategic recommendation and rejected alternatives;
3. candidate visual direction, clearly marked pending approval;
4. content architecture and draft message hierarchy;
5. implementation tasks with dependencies and verification;
6. explicit blockers/gates;
7. saved plan path when file tools are available.

Do not scaffold the project when the user asked only for a plan.

## Related skills

- `landing-page-generator` for component generation after evidence gates are approved.
- `brand-guidelines` for formalizing an approved visual identity.
- `content-strategy` for broader demand and editorial planning.
- `software-development:writing-plans` for executable implementation steps.
