# Creator footprint research: Apify evidence → commercial strategy

## Scope and discovery

For public creator accounts plus an owned brand, locate the existing project, read its report and corpus manifest, and reuse its dashboard before creating replacements. Resolve official handles and ownership through first-party links; do not expand into private life or unrelated third parties.

Inspect available tools at runtime. When Apify is requested and available, use its dedicated web fetch/search tools for URLs and discovery, and platform Actors for bounded structured collection. Discover Actors by platform and inspect the current input schema before calling them. If unavailable, use permitted public web sources and report reduced coverage, rather than silently claiming equivalent scraping.

## Reproducible collection

- Define limits per account/platform and date window before submission.
- Record Actor name, run ID, dataset ID, parameters excluding secrets, retrieval time, outcome, and returned row count at submission/completion.
- Save raw JSON separately from normalized CSVs and report/dashboard data.
- Poll existing runs rather than starting duplicate paid jobs. Retrieve dataset pages until the selected scope is covered; a successful run alone is not proof all rows were downloaded.
- For blocked/empty pages, try another permitted public source or a dedicated fetch tool. Search snippets are discovery leads, not equivalent to reading a post.
- Normalize stable platform IDs, canonical URLs, timestamps, captions, public metrics, coauthors, tagged accounts and ad-related fields. Missing metrics are null, not zero.
- Deduplicate by platform and stable post ID. Distinguish a cross-post from a duplicate record. Report totals by account/platform, date coverage, and corpus expansion so later dashboard counts can reconcile with the initial sample.

## Commercial evidence ledger

Keep one row per entity–post relationship: entity, account, post URL/ID, publication date, observation, raw field or short excerpt, evidence class, and caveat.

| Class | Label | Supports | Does not establish |
|---|---|---|---|
| A | Señal publicitaria | Observed platform ad/branded-content field or disclosure; record its exact meaning | Payment, fee, contract, sales, or current relationship |
| B | Coordinación observable | Coauthored post or other clear joint-publishing evidence | Paid sponsorship or continuing agreement |
| C | Mención editorial | Caption, ordinary tag, location or product mention | Commercial collaboration |

An ordinary tag is not enough for B. Record explicit sponsorship statements separately as sourced claims; do not force every field into stronger evidence. Say “señal publicitaria,” not “publicidad declarada,” for an ambiguous technical flag.

Keep historical relationships, new prospects, owned brands, and unresolved entities separate. An extracted commercial entity count is not a client count. Audit ambiguous handles and top-ranked entities manually.

## Niches and audience hypotheses

Code content into explicit topic rules and inspect representative positives and false positives. If multilabel, note that percentages can sum above 100%. Use platform-specific engagement denominators and disclose missing values; do not combine views, followers and likes into an unexplained score.

For each avatar write: job-to-be-done, relevant content evidence, purchase context, objection, CTA, confidence, and a voluntary validation question. Public content indicates intended appeal, not verified follower composition. Do not infer income, sensitive characteristics, residency, demographics or subscriber behavior from appearance or isolated comments. Aggregate comments without exposing commenters or claiming they represent the whole audience.

## Strategy and delivery

Separate competitors for attention from product substitutes and adjacent references. Every proposed brand activation needs its evidence tier, historical/current status, idea, CTA, KPI, unknown terms and next validation step. Link creator and owned-brand content without making every recommendation a sales pitch. Drafting strategy does not authorize contacting brands or publishing.

For a requested local dashboard, reuse the existing template, embed only minimized derived data, avoid external fonts/scripts/images, and omit unrelated personal bios and mentions. Escape scraped text and validate outgoing links. Keep raw research private and separate.

Verification: reconcile displayed counts with normalized files; sample evidence links and classifications; exercise combined filters, search, empty states, keyboard and mobile layouts; check browser console and network requests. Leave a runnable smoke test for nontrivial filters/rendering. Deliver the absolute HTML path for CLI use, not an attachment tag.
