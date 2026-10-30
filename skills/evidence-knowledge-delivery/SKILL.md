---
name: evidence-knowledge-delivery
description: >
  Run evidence-first knowledge work from source discovery through verified delivery. Use for local or web research, product/company intelligence, privacy-aware archives, durable agent handoffs, evidence-backed landing pages, PDF generation, and sending a final document. Triggers include “research this product,” “search my computer,” “build a dossier or wiki,” “prepare a handoff,” “plan a landing page without inventing claims,” and “render and send this document.”
---

# Evidence-to-Deliverable Operations

This is the class-level umbrella for evidence acquisition, knowledge packaging, and verified delivery.

Route mixed-source knowledge work through one auditable lifecycle: discover, classify, preserve, synthesize, package, and deliver. Use only the stages the request needs, but never skip provenance, privacy, or final verification.

## Step 1: Detect the operating surface

Check what the request and runtime actually provide:

- source classes: local files, Git repositories, supplied documents, authenticated cloud stores, public websites, or prior-session context;
- available discovery/extraction tools: native file search, PDF/OCR/vision tools, browser/web fetch, Git/GitHub, converters, and delivery channels;
- authorization boundaries: read-only research, file creation, upload, or explicit sending;
- destination: internal corpus, shareable archive, agent handoff, landing-page plan, PDF, email, or messaging attachment.

Prefer native structured tools, then installed CLIs, then browser/GUI fallbacks. Never silently broaden source roots, recipients, publication scope, or authentication.

## Step 2: Frame the decision and acceptance gate

Write the decision or outcome first. Define subject aliases, geography/time horizon, exclusions, target audience, required artifact, and what evidence would reverse the recommendation.

Default gates:

| Mode | Required gate |
|---|---|
| Research/wiki | Falsifiable questions and source scope |
| Local archive | Subject identifiers, destination excluded from search, privacy level |
| Handoff | Receiving task, authoritative artifacts, exact revision when relevant |
| Landing page | Page type, audience, offer, one CTA, publishable proof |
| Delivery | Canonical source, exact recipient/channel, explicit send authorization |

## Step 3: Discover and preserve evidence

### Public web and product intelligence

Inspect robots/sitemaps, group URLs by route family, sample each family, then define the extraction schema before a full crawl. Retain URL, timestamp, status, canonical, content hash, raw content, metadata, structured data, links, and errors. Use low concurrency and bounded retries.

### Local and cloud information

Search in layers: indexed metadata/content, filenames, focused text search, then exact identifiers. Inspect before copying. Exclude caches, dependencies, destination folders, and generic false positives. Make mixed local/cloud collection resumable and keep manifests separate until both sources finish.

### Restricted local inventories and identity graphs

When a user supplies a filesystem allowlist/denylist, apply both allowed roots and allowed content classes before opening anything. Prune denied paths and refuse symlink traversal; keep a ledger of actual reads. Sanitize excerpts before tool output, not only before delivery. Do not copy raw sources or write extra artifacts when only the report is authorized.

Keep operational skill reads separate from subject evidence, but include them when evaluating a whole-session zero-out-of-scope test. Disclose exceptions rather than declaring PASS under a narrower definition. Treat memory and operator-provided identity as search hints, not disk proof. Identity merges remain proposals; local configuration does not establish ownership or active service use.

Prefer concise synthesis with complete requested path inventories, not bulk source dumps. Check citation meaning as well as line-range validity, distinguish project counts from file counts, rerun privacy checks after the last edit, and describe zero detected secret matches without promising absolute absence.

See `references/restricted-local-inventories.md` for scope gates, MCP/agent metadata limits, privacy filtering, report checks, and binary-format ambiguity handling.

### Git and handoff evidence

Record repository, remote, branch/PR, exact commit, verification time, and checks run now. Preserve dirty trees; use isolated worktrees for exact-revision analysis.

## Step 4: Classify claims, privacy, and authority

Label every material item as one of:

- directly observed or independently verified;
- first-party/documented claim;
- verified with caveat;
- inferred/proposed with confidence;
- historical pending revalidation;
- contradicted or not publicly verifiable.

Separate evidence from analysis. A demo, local artifact, repository, folder, or repeated claim is not proof of production use, customers, revenue, ownership, or performance.

Minimize privacy exposure. Extract relevant chat windows rather than bulk archives; separate private identifiers; redact unrelated credentials and PII; rerun secret scans after edits. Build a separate shareable staging layer instead of uploading an internal archive directly.

## Step 5: Normalize and synthesize

Use explicit records such as Source, Claim, Entity, Product, Price, Competitor, Repository, ArchitectureEvidence, and Decision. Attach source and date to each record and preserve contradictions.

For product/company research, distinguish direct competitors, adjacent products, infrastructure, software substitutes, and human/service substitutes. Label public architecture reconstruction by confidence. Use explicit assumptions for market sizing and unit economics. End with build/differentiate/partner/skip guidance and evidence that would change it.

For landing pages, convert approved evidence into one coherent story: audience/outcome, problem, solution flow, capabilities framed as outcomes, honest proof state, trust limits, and one real CTA. Keep strategy approval separate from implementation approval. Do not copy template proof or turn technical output into customer results.

### Creator footprints, owned brands, and collaboration evidence

For influencer/public-creator research, preserve retrieval profile, original author, and coauthors separately; deduplicate posts without losing provenance. Shared content is not proof of paid sponsorship, technical ad flags do not establish a contract, and an absent flag does not prove organic content. Distinguish explicit activations, coauthorship, technical signals, and mere mentions; keep owned brands and creative suppliers separate from clients.

Build audience personas as testable needs-based hypotheses, not inferred demographics. Distinguish followers, subscribers, members and customers; public views are not unique reach. Report sample windows, valid metric denominators and whether analysis covered captions, sampled visuals or complete videos. Do not monetize likes into purported ROI without attributable outcomes and costs.

Before resuming from a summary or integrating delegated work, inspect existing artifacts and later source notes: reconcile superseded limitations before publishing. Verify cited post IDs and all promised derivative files, while distinguishing local traceability checks from live URL or contract verification.

See `references/creator-footprint-evidence.md` for the Apify extraction/provenance workflow, coauthor schema, relationship evidence ladder, audience validation and delivery checks.

### Narrative-inspired operational methods and agent skills

When a film, biography, or success story inspires a proposed workflow, separate depicted dialogue, retrospective testimony, historical verification, and your operational interpretation. Do not present interview quotes as film transcripts or a locally coined principle as established science. Reconstruct chronology and distinguish source publication dates from event dates.

Translate comparison into a falsifiable gap hypothesis, not a mandate to copy winners. Inspect existing assets and observable failures; compare resources and human support; require a rival explanation and a minimal reversible test. Missing permissions, unavailable evidence, and external constraints are not automatically skill deficits. More agents are an intervention to test, not the default answer.

Validate two claims separately: the proposed skill diagnoses well, and interventions derived from it actually improve outcomes. Preserve baseline conditions, genuinely inaccessible reserved evaluation answers, complete trial records, and critical regression gates. Allow no-change and inconclusive outcomes. Research/design authorization does not authorize installing the skill, rewriting a profile, or running production experiments.

See `references/narrative-to-agent-improvement.md` for the source-layering example, comparison safeguards, two-stage validation protocol, and research leads.

## Step 6: Package for the consumer

Choose the smallest durable package:

- **Knowledge base:** index plus product/market/competition/business/architecture/evidence/decision sections.
- **Local archive:** README, curated files/extracts, inventory with original paths and SHA-256, final manifest, optional ZIP.
- **Agent handoff:** authority order, exact revisions, verified/current versus historical state, risks, restricted content, next smallest action, and revalidation protocol.
- **Landing-page plan:** confidence-labeled synthesis, strategy, visual direction pending approval, content architecture, dependencies, release checks, and blockers.
- **Document:** render from the canonical source using the smallest deterministic path; validate file presence, page count, expected text, and visual output where stakes justify it.

Do not create an elaborate schema or implementation when the user asked only for a plan.

### Refreshing an existing project wiki

For “everything we know about this project,” inspect existing indexes, manifests, chapters, graphs, and relevant session history before building another corpus. Reuse a usable base: add a dated master entry and an inbound index link, preserving established link syntax. Do not force a new schema or graph export merely to deliver synthesis.

Compare inventoried SHA-256 hashes with current files and report unchanged, changed, missing, and unverifiable sources. Equality proves file identity, not truth or currency, and does not discover new files outside the manifest. Keep source freshness separate from synthesis date. Re-rendering stored graph data is not fresh semantic extraction; preserve its historical date unless extraction actually ran.

Keep documented identity, historically inspected implementation, proposals, and runtime-verified operation distinct. Do not combine budgets from different versions, agent rosters with running workers, or demos with commercial outcomes. Label simplified graph links separately from directed/multiple extraction relationships.

Leave a small rerunnable validator for local links, manifest comparison and graph endpoint integrity. Resolve each link relative to its containing file; flag paths outside the project as nonportable. Report validation scope explicitly: structural PASS can coexist with stale sources and unverified production. Review prose after the last edit for secrets; zero pattern matches is not a guarantee of absence.

See `references/existing-project-wiki-refresh.md` for the bounded refresh recipe and delivery checks.

### Evidence-backed specification handoffs

For documentation-only product briefs, preserve the user's requested language, directory boundary, no-Git/no-publication restrictions, and artifacts assigned to other agents. State that the MVP is defined, not implemented; leave specifications Draft until the named approver approves their version. Validation is not implementation authorization, and must not trigger product-test generation or deployment.

Distinguish documentary reuse evidence from runtime verification. A README describing sessions, audit, or CRM does not demonstrate tenant isolation or a working integration. Record candidate assets as documented, conceptual, or execution-verified; never copy client data or secrets to establish reuse. Mark roles, prices, thresholds and retention policies as proposals when not confirmed.

When a structural validator expects different language labels, inspect its actual parser and preserve the original document. If needed, run the unchanged validator on both the original and an ephemeral label-normalized copy; report both outcomes, the mapping, and the narrow scope of validation. Never fabricate endpoints or sections to raise a score. Independently check FR and NFR coverage, dangling acceptance references and semantic consistency. Do not silently patch shared tooling from a directory-scoped project task.

See `references/localized-specification-handoffs.md` for localized validation, approval gates and assisted-pilot measurement safeguards.

## Chat and multimedia operational reporting

Use this workflow for WhatsApp exports, field-team activity reports, existing productivity-table replicas, and dashboards derived from dated messages and attachments.

- Resolve the inclusive reporting window explicitly. Preserve message date, attachment date, and actual work date separately; a recently sent screenshot of old work is not current-period production.
- Parse multiline messages and attachment references into a traceable event ledger. Deduplicate work orders/events, not just messages; retain corrections and uncertain attribution for review.
- Inventory every attachment in scope by media type and review status. OCR is extraction, not visual verification: inspect originals for dates, identifiers, statuses, and ambiguous counts. Report unreviewed audio/video/documents rather than implying that image OCR covers all multimedia.
- Inspect the supplied table's real headers and category definitions before mapping codes. Preserve unknown categories, zones, targets, and denominators as N/D; never fabricate mappings to fill a template.
- Distinguish reported completions from independently verified closures. Activity counts alone do not establish efficiency or fair employee rankings without assignment, hours, complexity, and quality denominators.
- Generate spreadsheet, dashboard, and narrative from one canonical ledger. Leave a runnable reconciliation check and test dashboard filters against the same records. Preserve originals and keep private attachments local unless publication is explicitly authorized.
- Preserve order/folio identifiers as literal strings end to end, including leading zeros. Exact identifier matches take precedence over partial search matches; uncertain identifiers must not create evidence associations.
- When visual evidence is requested, include the images themselves in both deliverables, not only links: a portable HTML gallery and embedded Excel images, with an order-to-evidence view and an evidence atlas. Build from privacy-reviewed, flattened crops/redactions only; never hide sensitive original pixels with CSS or spreadsheet overlays.
- Favor a friendly summary-first dashboard with date/person filters, identifier search, empty/reset states, and a keyboard-accessible image viewer. Distinguish direct, contextual, and historical evidence visibly. Verify image decoding, associations, mobile layout, and Excel drawing anchors; floating spreadsheet images require a stable evidence sheet rather than an assumption that sorting preserves row associations.

See `references/chat-multimedia-productivity.md` for ledger fields, temporal inclusion rules, multimedia coverage, and cross-artifact checks.

## Evidence-backed executive dashboards

When turning reports or synthetic experiments into an executive presentation, preserve evidence boundaries in the interface itself, not only in a disclaimer:

- Separate product roles from simulated actors; requested sample size from executed sample size; terminal round/index from historical partials and approximate recovery.
- Label observed activity, historical technical evidence, unverified production readiness, and proposed operational/commercial metrics separately. Synthetic posts and traces do not establish a causal winner, accepted work, growth, or revenue.
- Use the user's requested visual direction and delivery scope. For a bounded static presentation, system fonts, CSS charts, and small local scripts can suffice; do not modify the original report or product, add packages, or deploy without authorization.
- Extract a minimal local snapshot directly from canonical structured data and leave a runnable equality check against the source. Define units, formulas, and selector-dependent denominators beside charts. Render external strings with textContent or escaping.
- Keep all sections visible in reading mode; presentation mode must have previous/next controls and a counter, while print exposes the whole narrative. Verify keyboard behavior and narrow layouts rather than inferring them from CSS.
- Distinguish data/structural tests, HTTP availability, and actual browser interaction/visual checks in the final report. If one automation dependency is absent, inspect available browser tools before stopping; HTTP 200 is not visual verification. Re-run checks after the final edit and never promise that another agent will finish unverified work.

See `references/executive-simulation-presentations.md` for the evidence mapping, minimal snapshot checks, and presentation verification recipe.

## Step 7: Deliver and verify

Uploads and sends are separate authorized actions. Before delivery, verify filename, size, recipient, subject, attachment, destination permissions, and privacy boundary. After sending, verify the sent record or platform receipt; after upload, read back the remote artifact. Do not retry ambiguous sends before checking for duplicates.

For public landing-page release, verify canonical URL, forms without real leads, noindex/analytics state, assets, accessibility, privacy, and rollback. Preview environments must not accept real leads or run production analytics.

## Step 8: Report only verified facts

Return:

1. Outcome and decision.
2. Sources and as-of time.
3. Claims/inferences and confidence.
4. Artifact paths or URLs.
5. Verification actually performed.
6. Privacy, access, durability, or delivery caveats.
7. Next minimum action or explicit stop condition.

Never imply research continues between turns unless a tracked background process or scheduled job exists.

## Reference files

The absorbed workflow banks under `references/absorbed/` preserve detailed recipes, templates, scripts, and provider-specific pitfalls:

- `context-transfer/` — commit-pinned agent/session handoffs.
- `document-delivery/` — PDF rendering and verified email/messaging attachment delivery.
- `evidence-first-landing-pages/` — evidence inventories and static-site release verification.
- `local-information-archivist/` — local/cloud collection, photo packages, Drive-safe staging, manifests, and redaction.
- `product-intelligence-research/` — product/market/business/architecture analysis and corpus schemas.
- `web-intelligence-research/` — sitemap-to-wiki capture and reproducible web corpora.
- `vendor-web-surface-hierarchy.md` — classify manuals, code, portals, training, forums, and marketing before assigning evidentiary weight; includes dynamic-site extraction fallback.
- `agent-profile-specialization.md` — turn a source bundle into an evidence-backed expert profile while keeping specialization, external integration, and production activation as separate authorization gates.
