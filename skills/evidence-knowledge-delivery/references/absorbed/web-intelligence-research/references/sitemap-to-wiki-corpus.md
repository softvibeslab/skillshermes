# Sitemap-to-Wiki Corpus Pattern

## Capture

1. Read `robots.txt`.
2. Fetch sitemap XML and enumerate `<loc>` values.
3. Group by first path segment to discover templates.
4. Crawl allowed pages slowly with an identifiable user agent.
5. Save audit fields plus a clean Markdown snapshot.
6. Store nested records in JSONL and normalized tables in CSV/JSON.

Recommended record:

```json
{
  "url": "https://example.com/item/x/",
  "family": "item",
  "status": 200,
  "captured_at": "ISO-8601",
  "content_type": "text/html",
  "sha256": "...",
  "title": "...",
  "description": "...",
  "canonical": "...",
  "links": [],
  "json_ld": [],
  "text": "..."
}
```

## Extract

- Parse JSON-LD by `@type` first: Product, Service, Offer/AggregateOffer, FAQPage, BreadcrumbList and Organization.
- Use URL family to choose the extractor; avoid per-page selectors.
- Exclude collection roots from entity totals.
- Convert FAQ answers and quantitative marketing statements into a claim ledger with source, date, evidence status and confidence.

## Obsidian

```text
Research/<Subject>/
├── 00 - Plan maestro.md
├── 01 - Índice.md
├── Producto/
├── Mercado/
├── Competencia/
├── Negocio/
├── Arquitectura/
├── Evidencia/{Páginas,Datasets}/
└── scripts/
```

Raw snapshots are immutable; synthesis pages evolve and link back to evidence.

## Verify

```python
assert len(corpus) == sitemap_count
assert all(r.get("captured_at") and r.get("sha256") for r in corpus if r["allowed"])
assert all(r["status"] == 200 or r.get("error") for r in corpus)
assert required_datasets <= {p.name for p in dataset_dir.iterdir()}
```

Report family counts, failures, non-empty text, empty notes and required dataset presence.

## Competitive handoff

After QA, prioritize candidates. Require primary evidence for buyer, product, pricing, supply model, task flow, quality controls, developer surface, payments and adoption. Label direct, adjacent, substitute or complement only after validation.

## Progress boundary

Good: `Phase 1 completed and verified. Nothing is running in the background. Phase 2 is prepared but not started.`

Bad: `Next I am researching competitors.` This sounds active even after the turn ended.
