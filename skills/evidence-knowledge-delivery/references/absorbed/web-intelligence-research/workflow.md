---
name: web-intelligence-research
description: Build an auditable knowledge base from public product or company websites, then use it for product, market, competitor, business-model, and architecture analysis. Use when scraping must feed a wiki, benchmark, executive report, or build decision.
---

# Web Intelligence Research

Turn public sites into reproducible evidence and decision-grade knowledge. Keep respectful crawling, structured extraction, claim verification and strategic synthesis in one workflow.

## Core rule

Raw pages are evidence, not conclusions. Marketing copy remains a first-party claim until independent sources corroborate it.

## Workflow

1. Frame the underlying decision and 3–5 falsifiable questions.
2. Fetch `robots.txt` and sitemap(s); count URLs by path family before crawling.
3. Define scope, rate limit, user agent and excluded private/authenticated surfaces.
4. Build two layers:
   - immutable evidence snapshots with URL, timestamp, status, canonical, hash, links, JSON-LD and clean text;
   - normalized entities such as products, agents, tasks, prices, use cases, comparisons, claims and sources.
5. Prefer JSON-LD/stable metadata over brittle CSS selectors. Use stdlib for static sites; render JavaScript only when required.
6. Generate an Obsidian index with Product, Market, Competition, Business Model, Architecture, Evidence and Decisions.
7. Validate corpus coverage and extraction invariants before analysis.
8. Research alternatives from current primary sources; separate direct competitors, infrastructure, builders, software substitutes and human/service substitutes.
9. Synthesize only what the request needs: benchmark, TAM/SAM/SOM, business model, unit economics, public architecture, risks, MVP and build/partner/differentiate/skip recommendation.

## Required quality gates

- Every sitemap URL attempted; failures preserved.
- Every allowed record has status, timestamp and hash.
- Claims, facts and inferences use separate fields.
- Collection roots count as pages but not entities.
- Important external claims are triangulated.
- Technical reconstruction has high/medium/low confidence.
- Counts and calculations come from runnable tooling.
- The wiki remains useful without the original chat.

## Phase communication

Research does not continue between turns unless a tracked background process or scheduled job exists. At every phase boundary state:

- completed and verified;
- currently running, if anything;
- next but not running.

Never imply unattended progress merely by saying “next” or “I continue.”

## Minimal structure

```text
<root>/
├── 00 - Plan.md
├── 01 - Índice.md
├── Producto/
├── Mercado/
├── Competencia/
├── Negocio/
├── Arquitectura/
├── Evidencia/{Páginas,Datasets}/
└── scripts/{capture,extract,validate}.py
```

## Pitfalls

- Guessed documentation routes can return 404; status-check rather than assume.
- Repeated FAQs inflate claim counts; preserve first, deduplicate during synthesis.
- Public repositories may be stale relative to production.
- On-chain, A2A, SDK, timing, user and revenue statements are claims until supported.
- Start with a curated first-party catalog when it can test demand; do not default to a two-sided marketplace.

## References

- `references/sitemap-to-wiki-corpus.md` — capture schema, extraction order, Obsidian layout and verification pattern.
