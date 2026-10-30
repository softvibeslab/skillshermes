---
name: product-intelligence-research
description: Build an evidence-backed knowledge base about a public digital product from its website, docs, repositories, and market sources. Use for requests combining ethical scraping, wiki construction, competitive benchmark, market analysis, business model, public architecture reconstruction, and a build/partner/skip plan.
---

# Product Intelligence Research

Turn a public product footprint into a decision-grade corpus. Extraction, normalization, verification, analysis, and recommendation are separate stages.

## Principles

- Respect `robots.txt`, public access boundaries, rate limits, copyright, and terms. Never evade authentication or technical controls.
- Treat first-party copy as positioning evidence, not independent proof of adoption, performance, revenue, or quality.
- Separate observed, documented, and inferred architecture; attach confidence to every inference.
- Preserve raw evidence separately from normalized entities and analytical notes.
- Prefer primary sources; triangulate material claims.
- Research only what can change a build, differentiate, partner, or skip decision.

## Workflow

### 1. Frame the decision

Define the decision, users, geography, time horizon, and what evidence would reverse the answer.

### 2. Discover the public surface

1. Fetch `robots.txt` and sitemap(s).
2. Count URLs by route/template family.
3. Identify official docs, repositories, changelogs, social channels, stores, and public APIs.
4. Fetch one representative URL from every route family.
5. Derive the extraction schema before the full crawl.

Read `references/corpus-and-evidence-schema.md` for reusable records and acceptance checks.

### 3. Capture evidence

For each public URL retain canonical URL, status, content type, fetch time, content hash, raw content, metadata, JSON-LD, links, structured facts, and crawl errors. Use low concurrency and bounded retries.

### 4. Normalize and verify

Create explicit `Source`, `Claim`, `CatalogItem`, `Category`, `Price`, `UseCase`, `Competitor`, `Repository`, and `ArchitectureEvidence` records. Put source and date on the record.

Mark material statements as first-party claim, independently corroborated, contradicted, or not publicly verifiable. Record contradictions rather than averaging them away. Vendor-authored comparisons are positioning evidence, not neutral benchmarks.

### 5. Map the market

Separate direct products, adjacent products, enabling platforms/protocols, horizontal software substitutes, and human/service substitutes.

Benchmark consistently across buyer, job, offering, supply model, input channel, pricing, risk allocation, discovery, routing, quality, context, delivery, developer UX, payments, trust, distribution, and defensibility.

Size the market with at least two methods. Prefer bottom-up formulas with explicit assumptions over broad “AI market” headlines.

### 6. Model the business

Analyze both value creation and marketplace mechanics: buyer/supplier sides, activation, recurring use, ticket and frequency, take rate or gross margin, inference/tool cost, failed-output cost, support, fraud, liquidity, fill rate, routing success, acceptance/rerun rates, CAC, retention, LTV, contribution margin, cold start, reputation, and flywheels.

If data is unavailable, use editable conservative/base/high scenarios and label assumptions.

### 7. Reconstruct public architecture

Investigate channels, identity, catalog/discovery, task intake, classifier/router, queue, workers, tools/models, progress, artifacts, evaluation, acceptance, ledger/settlement, SDK/API/webhooks/protocols, observability, moderation, security, and privacy.

Never present an inferred production stack as fact. Public repositories may lag production.

### 8. Propose the minimum alternative

Do not copy code, brand, or protected content. Solve the underlying job. Prefer a curated first-party catalog over a new two-sided marketplace until demand, quality, and liquidity are demonstrated. Add open supply, reputation, complex settlement, or blockchain only when they solve measured constraints.

### 9. Build the wiki

Organize product, market, competition, business, architecture, evidence, claims, decisions, MVP, and roadmap. Every analytical note must trace to evidence; the wiki must work without the originating chat.

## Deliverables

- crawl manifest and structured dataset;
- catalog and taxonomy;
- claim ledger and contradiction report;
- market definition, TAM/SAM/SOM, trends, ICP/JTBD;
- competitive map, benchmark, and priority profiles;
- business model and unit-economics scenarios;
- architecture diagrams with confidence labels;
- risk register;
- build/differentiate/partner/skip recommendation;
- minimum MVP and measurable roadmap.

## Quality gates

- Every sitemap URL is attempted or explicitly excluded.
- Every route family has a manually reviewed sample.
- Material numbers carry source, date, formula, and assumptions.
- Claims, observations, and inferences are visibly distinct.
- Direct competitors and substitutes are not mixed into one ranking.
- The recommendation states what not to build and what evidence would reverse it.

## Pitfalls

- Crawling everything before understanding templates.
- Treating page counts or “online” labels as evidence of active supply.
- Repeating vendor comparisons as independent findings.
- Using one speculative report as TAM.
- Inferring production architecture directly from an old repository.
- Building protocol, blockchain, or marketplace complexity before it solves a measured constraint.
