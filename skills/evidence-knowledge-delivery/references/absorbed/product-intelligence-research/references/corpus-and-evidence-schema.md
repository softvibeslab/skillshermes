# Corpus and evidence schema

## Crawl order

1. `robots.txt`
2. sitemap indexes and sitemaps
3. one representative URL per template family
4. extraction schema
5. bounded full crawl
6. QA sample per family
7. change detection by content hash

## Layering

```text
raw/          fetched HTML/Markdown/JSON-LD and metadata
entities/     normalized product records
claims/       claims with verification state
analysis/     market, business, architecture, recommendations
wiki/         human-readable linked synthesis
```

## Reusable records

```text
Source(url, publisher, source_type, fetched_at, http_status,
       content_type, canonical_url, content_hash)

Claim(text, entity, claim_type, source_url, observed_at,
      corroboration_status, confidence, contradiction_notes)

CatalogItem(slug, name, tier, status_claim, tagline, skills,
            categories, price_min, price_max, turnaround_claim,
            examples, related_items, channels, source_url)

Category(slug, name, item_count_claim, price_range,
         turnaround_claim, examples, methods_claimed, source_url)

Competitor(name, competitor_class, buyer, job, offering,
           supply_model, pricing, risk_model, quality_controls,
           integrations, distribution, trust, sources)

ArchitectureEvidence(component, evidence_type, source_url,
                     observation, inference, confidence, caveats)
```

## Claim rules

- “We have N agents” is a first-party claim until corroborated.
- A sitemap count is an observed page count, not active supply.
- “Online” in markup is displayed status, not uptime evidence.
- A public repository documents that repository, not necessarily production.
- A vendor comparison describes positioning; validate competitor facts at the competitor's primary source.

## Recommended wiki folders

```text
00 Index/
Product/
Market/
Competition/Profiles/
Business/
Architecture/
Evidence/Raw Sources/
Evidence/Claims/
Decisions/
```

## Acceptance checks

- Route-family counts reconcile with the crawl manifest.
- Broken, redirected, duplicated, and excluded URLs are listed.
- All analyzed competitors have current primary sources.
- Important calculations expose formulas and assumptions.
- Architecture diagrams use confidence labels or a legend.
- Executive summary links to supporting notes instead of repeating unsupported conclusions.
