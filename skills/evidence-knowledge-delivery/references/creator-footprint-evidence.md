# Creator footprint and brand-relationship research

Use for public influencer audits spanning a personal profile, owned brand, websites, and third-party collaborations. This is public professional research, not investigation of private life.

## 1. Discover before extracting

Find the existing project and inspect its index, reports, raw datasets, manifests, and review notes. After a handoff or context compression, repeat this inventory before writing a final synthesis: later source files can supersede earlier limitations. Do not replace a richer report with an older summary.

Resolve handles through explicit cross-links and first-party statements. Maintain separate entities for creator, owned brand, studio, collaborator, and similarly named unrelated organizations. Public association does not establish legal ownership; a changed-looking handle does not establish renaming history.

## 2. Bounded extraction with provenance

If Apify is requested and available, discover relevant Actors, inspect current schemas, and set explicit item limits. Use dedicated URL fetch for supplied websites and search for external corroboration. Follow run status to completion and paginate datasets where needed. Existing native APIs or authorized browser extraction can supplement coverage; identify the method actually used.

Preserve Actor name, run/dataset identifier, sanitized input, retrieval timestamp/timezone, raw results and errors in a manifest. Never retain tokens in manifests or report URLs. An HTTP success with empty extracted text is not evidence that the page has no content: try rendered DOM or another available extraction route and preserve the meaningful extract.

Separate retrieval date, publication date, and event date. A historic event page is not a current agenda. A page displaying “404” is not necessarily an HTTP 404 response.

## 3. Attribution and metric schema

Minimum post record:

- platform, native post ID, URL, publication timestamp;
- input/profile URL used to retrieve it;
- original author and all coauthors;
- caption, hashtags, observed metrics, retrieval timestamp;
- raw commercial-disclosure fields when present.

Deduplicate analytical posts by `(platform, native ID)` while retaining all retrieval origins. Instagram collaborative posts may occur under a creator's profile with a brand or third party as original author. Report by retrieval profile and by original author separately; do not silently assign all interactions to the creator or count one shared post as two campaigns. Check inverse relationships too: creator as coauthor on a brand-owned post.

Report valid denominators, date ranges, medians and distribution/outliers. Null or negative sentinel counts are missing, not zero. Keep videos separate from still posts when computing video statistics. Recent posts have had less accumulation time; capped samples are not a random sample or complete publishing history.

Public views are not unique reach. Do not sum followers across platforms as unique audience. Profile bio claims and live counters are separate observations, not a growth trend. Do not invent ROI from arbitrary dollar values per like: require attributable commercial outcomes and appropriate costs. If calculating engagement, state exactly which interactions and denominator are used; summed actions per reached account are not a probability bounded by 100%.

## 4. Brand relationship evidence ladder

| Evidence | Safe conclusion | Unsupported leap |
|---|---|---|
| Explicit joint giveaway, prize redemption, invitation, credited production | Described activation/invitation/creative work exists in public record | Payment, fee, exclusivity or ongoing contract |
| Platform coauthor metadata | Shared publication | Paid sponsorship or confirmed client |
| Scraper `isAd`, `isSponsored`, `paidPartnership` | Technical signal requiring interpretation | Contract, payer identity or organic-only performance |
| Tag, hashtag, location, product use, recommendation | Mention/use/recommendation | Brand partnership |
| Creator says “hire me” | Solicitation | Existing agreement |
| Marketplace, ecommerce provider, shared event venue | Platform/provider/contextual association | Sponsor |

Keep raw technical fields and user-visible disclosure separate. A false flag does not prove no payment; a true flag alone does not identify who paid whom. Label payment and current relationship status unknown unless supported. Group campaigns with multiple counterparties rather than multiplying results.

For each relationship retain counterparty, type, exact quote or metadata field, source URL, publication date, confidence and unknowns. Suppliers, creative collaborators, owned brands, venues and paying clients need separate categories.

## 5. Niches and audience hypotheses

Qualitative content themes do not establish demographic composition. Describe avatars through needs, occasion, attractive content, purchase friction, plausible offer and a validation method. Avoid invented ages, income, gender shares, residence or sensitive traits.

Distinguish followers, newsletter subscribers, paid members, video subscribers and customers. A subscription CTA or newsletter field does not disclose subscriber count or composition. A B2B buyer who might hire the creator is a separate hypothesis from the follower persona.

State whether evidence covers captions only, visual sampling, complete video review or transcripts. Do not claim exhaustive audiovisual analysis when only metadata was examined. Theme percentages require an explicit coding scheme, denominator, overlap rule and classification checks.

Use aggregated authorized platform Insights and consented interviews/surveys to validate hypotheses; do not harvest individual follower profiles as a substitute.

## 6. Reconcile, verify, deliver

Before synthesis, reconcile late-arriving source notes against earlier conclusions. Mark first-party evidence, counterpart evidence and independent reporting; three owned pages are not three independent confirmations.

Leave the smallest reproducible analysis script with checks for uniqueness, row counts and missing-value handling. Confirm every cited post ID appears in primary data or an identified external source; verify referenced CSVs and reports actually exist. A local citation check proves traceability, not current remote availability or contractual truth.

Deliver a decision-oriented report, raw datasets, unified content table, relationship evidence table, metric definitions and a short critical review. Lead the user-facing reply with the useful finding and canonical path/URL. Include coverage and audience/payment limitations without making them obscure the result.

## Case-derived pitfalls

The workflow emerged from a creator-plus-apparel-brand audit: shared-post ownership changed account-level counts; explicit invitations and commercial scraper flags did not align perfectly; a later browser capture established a public guide and rounded Facebook counter after an earlier note said they were unverified. These are reasons to preserve attribution, raw flags and evidence chronology—not permanent conclusions about those accounts or extraction tools.
