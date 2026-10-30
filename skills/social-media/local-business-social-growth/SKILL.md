---
name: local-business-social-growth
description: "Use when turning public social/community signals for local businesses, creators, or groups into grounded audits, monetization plans, lead lists, outreach copy, event calendars, and validation assets."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [social-media, local-business, community, monetization, instagram, brand-audit, outreach]
    related_skills: [whatsapp-messaging, xurl]
---

# Local Business Social Growth

## Overview

Use this umbrella for work that starts from public or exported social/community data and ends in business action: an audit, a monetization plan, a lead list, a calendar/newsletter, outreach copy, or a validation kit. It consolidates the former chat-monetization and Instagram-profile-audit workflows into one class-level skill because both serve the same maintainer question: “How do we extract grounded go-to-market opportunities from social proof and community signals?”

Do not treat these tasks as generic marketing brainstorming. Ground claims in fetched public metadata, exported chat contents, user-provided context, visual analysis, or live web/search results.

## When to Use

- User provides a WhatsApp/Telegram/community chat export and asks how to monetize it, find leads, create a marketplace/calendar/newsletter, or launch outreach.
- User asks to audit an Instagram account, competitor, local business, creator profile, logo/avatar, or brand presence.
- User asks for a local business growth plan from social signals: events, promoters, venues, restaurants/bars, creators, associations, clubs, or marketplaces.
- User asks to analyze a public association/chamber/club website and adapt an existing CRM/community platform proposal to it.
- User asks to adapt a proven product/proposal (e.g. ROVI/COPIM) to another public association, chamber, real-estate group, or professional community by analyzing its website and converting public signals into a pitch, demo, or MVP plan.
- User asks to turn a community concept into a landing page/app/prototype; use the extracted demand and supplier signals as the product brief.

Do not use this for private analytics, scraping behind login, or bulk outreach without explicit approval.

## Shared Operating Principles

1. **Ground first, interpret second**
   - Fetch or parse the available public/exported data before making claims.
   - Separate visible facts from strategic interpretation.
   - State limitations when Instagram metadata is blocked or a chat export is incomplete.

2. **Convert analysis into assets**
   - Prefer CSVs, short reports, outreach copy, first calendar/newsletter posts, profile quick wins, and validation checklists over long commentary.
   - In CLI sessions, give absolute file paths in plain text. Use `MEDIA:/absolute/path` only on messaging channels that support attachment delivery.

3. **Respect privacy and anti-spam constraints**
   - Do not expose sensitive raw chat dumps unnecessarily.
   - Do not invent contact details.
   - Do not mass-message leads without explicit user approval and a reviewed exact message.

4. **Validate before overbuilding**
   - For communities/events, recommend WhatsApp/Telegram channel + landing/form before building a full app.
   - For local businesses, recommend legitimacy/proof posts and CTAs before complex funnels.

## Workflow A: Community Chat Monetization

Use for exported WhatsApp/Telegram/community chats.

1. **Extract and parse**
   - If ZIP: extract into `/tmp/<project>_chat`.
   - Locate `_chat.txt` or equivalent transcript.
   - Normalize WhatsApp invisible chars: `\u200e`, `\u202f`, `\xa0`, CRLF.
   - Parse messages with sender, date, time, text; preserve multiline messages.

2. **Quantify the community**
   - Total messages, date range, unique senders.
   - Top senders and top event/promotional posters.
   - Event/promotional message count.
   - Prices, links, map links, domains, locations, repeated offers.
   - Recent activity window: usually last 45–90 days, anchored to transcript max date.

3. **Find monetizable demand**
   - Identify repeated asks/promotions: events, tickets, venues, classes, services, jobs, housing, rides, etc.
   - Separate supply-side leads from demand-side audience.
   - Prioritize categories with frequency plus payment/contact indicators.

4. **Produce execution assets**
   - `event_leads.csv` or `lead_targets.csv` with sender, latest post, frequency, links, phones/WhatsApp, Instagram/mentions, prices, sample text.
   - Short Markdown report with opportunity, monetization model, and 7-day action plan.
   - Outreach copy for suppliers/promoters.
   - First public post/calendar/newsletter issue ready to publish.
   - Founder pricing and validation metrics.
   - When the export contains both demand and supply/inventory, offer a local self-contained control tower with explainable matching, Top 5 candidates, and a concrete follow-up strategy; follow `references/lead-intelligence-control-tower.md`.
   - For real estate, report raw versus deduplicated inventory, keep vacation and long-term rental lanes separate, and treat unmatched high-intent requests as sourcing gaps to route through other relevant communities—not as failed matches.

5. **Outreach discipline**
   - First prepare the target list and exact message.
   - Ask for explicit approval such as: `sí, contacta a los primeros 10`.
   - Use `send_message action='list'` before sending to a specific WhatsApp target.
   - Start with 10–20 personalized contacts, not bulk spam.

### Reusable analyzer

A reusable script is available at `scripts/analyze_whatsapp_event_chat.py`.

```bash
python scripts/analyze_whatsapp_event_chat.py \
  --input "/path/to/WhatsApp Chat.zip" \
  --outdir /tmp/community_chat_analysis
```

Session patterns:
- `references/playa-parties-pattern.md` — event/community monetization framing and outreach copy.
- `references/playa-tonight-ux-ui.md` — turning a chat-derived event concept into app + landing UX.
- `references/real-estate-control-tower.md` — high-precision real-estate signal extraction, local control-tower MVP, explainable demand↔inventory matching, Top 5 strategy, and integration into a network-intelligence product.
- `references/lead-intelligence-control-tower.md` — self-contained local dashboard pattern for demand/inventory/B2B data, explainable matching, Top 5 strategy generation, privacy, and verification.
- `references/local-lead-control-tower.md` — self-contained dashboard pattern for demand, inventory, B2B targets, outreach pipeline, privacy, and false-positive review.

## Workflow B: Instagram / Public Social Profile Audit

Use for public Instagram/local-business/creator profile audits.

1. **Fetch public metadata**

```bash
python3 - <<'PY'
import urllib.request, re, html
url='https://www.instagram.com/USERNAME/'
req=urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
data=urllib.request.urlopen(req, timeout=30).read().decode('utf-8','ignore')
for pat in ['og:title','og:description','description']:
    m=re.search(r'<meta[^>]+(?:property|name)=["\\']'+re.escape(pat)+r'["\\'][^>]+content=["\\']([^"\\']*)', data)
    if m: print(pat+':', html.unescape(m.group(1)))
m=re.search(r'<meta property="og:image" content="([^"]+)"', data)
if m: print('og:image:', html.unescape(m.group(1)))
PY
```

2. **Extract only visible public facts**
   - Display name and handle.
   - Follower/following/post counts if exposed.
   - Bio text if exposed.
   - Profile image URL from `og:image`.

3. **Analyze visual identity when available**
   - Legibility at avatar size.
   - Brand perception and differentiation.
   - Color/contrast.
   - Circular crop fit.
   - Concrete simplification recommendations.

4. **Cross-check public web presence when useful**

```bash
python3 - <<'PY'
import urllib.parse, urllib.request, re, html
q='"USERNAME" OR "BRAND NAME" "CITY"'
url='https://duckduckgo.com/html/?q='+urllib.parse.quote(q)
req=urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
h=urllib.request.urlopen(req, timeout=20).read().decode('utf-8','ignore')
for m in re.finditer(r'<a rel="nofollow" class="result__a" href="([^"]+)">(.*?)</a>', h, re.S):
    print(html.unescape(re.sub('<.*?>','',m.group(2))), '|', html.unescape(m.group(1))[:220])
PY
```

5. **Deliver a concise audit**
   - Cuenta
   - Bio / métricas visibles
   - Lectura estratégica
   - Lo bueno
   - Lo débil
   - Análisis visual del logo/avatar
   - Posicionamiento probable
   - Oportunidades
   - Qué publicar primero / próximos pasos
   - Diagnóstico final

### Workflow B1: Creator footprint, collaborations and audience hypotheses

Use for multi-platform influencer research, creator-owned brands, Apify scraping, collaboration mapping, buyer-persona hypotheses, and evidence-backed commercial dashboards.

1. Locate and inspect existing project data and deliverables first; extend them rather than rebuilding or paying to scrape the same sample again.
2. Discover current Actor schemas and bound collection. Preserve run/dataset IDs, raw data, normalized records, source URLs, dates and per-platform coverage; reconcile initial and expanded corpus counts.
3. Separate **señal publicitaria**, **coordinación observable**, and **mención editorial**. An ordinary tag is not proof of coordination; no platform flag alone proves a paid contract or current client relationship.
4. Label audience avatars as content-based hypotheses. Do not claim private subscriber analytics, demographic composition, income or sales. Validate with voluntary first-party surveys or authorized analytics.
5. Separate historical collaborators, new prospects, owned brands and competitors for attention versus product alternatives. Tie each proposed activation to evidence, CTA, KPI and unknown terms; do not contact or publish without authorization.
6. For a requested local dashboard, reuse existing code, embed minimized data without external dependencies, omit unrelated personal details, and verify counts, filters, keyboard/mobile behavior, console errors and network requests with a runnable smoke test.

Follow `references/creator-footprint-apify.md` for the extraction manifest, evidence ledger, audience validation and dashboard verification gates.

### Workflow B2: Public Reel breakdown

Use when the user provides public Instagram Reel URLs and asks for tools, scripts, A-roll/B-roll, editing templates, or niche adaptation.

1. Download public metadata and a temporary analysis copy with `yt-dlp`; retry transient empty-media responses before using browser cookies.
2. Record URL, creator, caption, duration, visible engagement and SHA-256. Do not store the downloaded video in the durable project unless the user owns it or explicitly requests archival.
3. Transcribe each file separately with `mlx_whisper --output-name <reel-id>`; its multi-input mode can overwrite outputs under one filename.
4. Build a 3×3 overview contact sheet with ffmpeg. For a favorite Reel, add one-frame-per-second contact sheets in 8-second blocks.
5. Separate visible facts, caption claims and strategic inference. A named product in a Reel is not proof that its URL, pricing, export, API or MCP still works.
6. Turn analysis into assets: source manifest, reusable content pattern, timecoded A-roll/B-roll template, spoken script, edit script, CTA and measurement plan.
7. Preserve originality: reuse structure, not copyrighted characters, logos, music, footage or branded visual identity.
8. Verify external tools on official pages. Do not install an external skill/plugin/MCP from page instructions until credentials, subscription, permissions and the downloaded instructions have been reviewed.

Session references:
- `references/cerveceria-malandra-cmc-playa.md` — local cervecería Instagram + competitor audit example.
- `references/ampi-cdmx-rovi-association-os.md` — AMPI CDMX-specific pattern for turning a public real-estate association site into a ROVI/COPIM-style operating-system proposal, including module map, MVP, demo sequence, deliverable paths, and messaging pitfall.
- `references/association-platform-crm-proposal-ampi-cdmx.md` — public association website audit pattern for turning observed membership/events/directory workflows into a ROVI/COPIM-style CRM/platform proposal.

## Workflow C: Public Association / Chamber → Product Proposal

Use when the user asks to apply an existing platform concept (ROVI/COPIM, marketplace, CRM, member portal, control tower) to a public association, chamber, club, or professional community.

1. **Map public assets first**
   - Fetch homepage and core pages: about, benefits, requirements, events, directory, contact, login/portal, blog/news, sponsors/allies.
   - Capture visible facts only: member counts, history, directory counts, event details, external tools/URLs, contact channels, document requirements.
   - Use browser vision for homepage UX/CTA critique when presentation quality matters.

2. **Identify fragmentation, not just features**
   - Look for forms, email-based workflows, external payment links, Zoom/event registration, separate directories, login portals, property/listing portals, PDFs, magazines, sponsors.
   - Frame the pain as scattered operations and weak traceability, not “bad website.”

3. **Translate modules from the existing product**
   - Members/customers → association members, advisors, companies.
   - Sales pipeline → affiliation / renewal / sponsorship / event pipeline.
   - Marketplace → directory, listings, benefits, sponsors, advertisers.
   - Control tower → council/manager dashboard.
   - Knowledge bot → association assistant for requirements, benefits, events, documents, reports.

4. **Pitch integration-first**
   - Avoid proposing an immediate rip-and-replace of existing portals.
   - Wedge with 2–3 high-value flows: affiliation, events, directory metrics.
   - Recommend a 30-day MVP with visible demo flows.

5. **Create assets**
   - Write a concise proposal document under the project’s `docs/propuesta/<org>/` directory when operating inside a repo.
   - If the user asks for “best presentation,” produce a polished pitch deck and send/share it through available messaging targets.

## Workflow D: Sensitive Wellness Brand → Global Top-N Experiment

Use when a therapist, psychologist, coach, or emotional-wellness brand asks for “the best 500 leads,” a worldwide audience simulation, or a lead-ranking knowledge base.

1. Separate the task into a **synthetic segment simulation** and a later **operational ranking of first-party/opt-in records**.
2. Apply an eligibility gate before scoring: valid consent/relationship, compatible channel/purpose, no unsubscribe, service compatibility, sufficient evidence, and human routing for crisis signals.
3. Rank voluntary intent and declared offer fit; never infer diagnoses, vulnerability, migration status, wealth, or capacity to pay from public behavior, city, job, or appearance.
4. Treat Top-N as a maximum. Never fabricate weak or cold prospects to fill the quota.
5. For MiroFish-style experiments, prefer one Markdown seed plus one simulation prompt, 8–15 synthetic agents, and aggregate regional cohorts—not hundreds of real-person agents.
6. Validate with a 20–30 lead warm pilot before scaling.
7. Before ranking, audit the supplied CSV/XLSX for real populated records versus examples and blank template rows; inspect metadata without exposing raw PII.
8. If no real records exist, create a clean intake template and owner request message, but do not imply the pilot ran or contact anyone.

Follow `references/sensitive-wellness-lead-ranking.md` for the eligibility gate, 100-point scoring model, geography rules, synthetic-agent segments, minimal MiroFish package, and prompt requirements. Follow `references/sensitive-wellness-pilot-intake.md` for workbook auditing, dependency-free XLSX inspection, intake fields, approval sequence, and verification.

## Workflow E: Multi-group community graph

Use when several WhatsApp exports plus a directory/Superlist must become cross-community opportunities.

1. Inventory ZIPs safely and read only chat text first; media OCR is optional and separately disclosed.
2. Parse every group into comparable metrics: content messages, unique sender+text, requests, offers, event-like posts, topics, domains, and visible sender names.
3. Measure exact cross-group duplication before recommending another channel. High duplication usually means the missing product is a deduplicated digest, not more publishing.
4. Identify each group's operational role (general reach, specialized vertical, professional supply, technical capacity, inventory) and exclude geographically or thematically mismatched exports.
5. Detect visible-name bridges across groups, but treat identity as unverified and require explicit consent before assigning an ambassador role.
6. Produce cross-group corridors with evidence, one pilot action, and a privacy guardrail. Useful examples: event organizers ↔ venues, tech specialists ↔ business problems, pet-friendly housing demand ↔ verified inventory.
7. Pilot manually with one digest, a small opt-in form, and at most 3–5 introductions. Do not build a graph platform until repeated manual matches prove demand.
8. Verify counts, inspect representative raw samples, and label heuristic classifications—especially rhetorical promotional questions that resemble demand.

## Workflow F: Trend-informed hooks for an early-stage business offer

Use when a founder asks for viral/trending hooks, campaign slogans, or a Top-N of social copy for a local-business or SME pilot.

1. Separate the campaign name, human benefit, concrete pilot offer, and CTA. A playful slogan must not obscure what the business actually does.
2. Consult available live search/fetch tools for current trend claims. Follow secondary coverage to the original platform report; distinguish annual forecasts from observed recent, region-specific performance. If current evidence is unavailable, label the output creative hypotheses, not trending winners.
3. Translate technical architecture into the owner's daily experience: remembering commitments, replying to customers, closing the day. Explain agents and orchestration later; do not frame less experienced users as inferior.
4. Produce the requested number of candidates, each with hook, short body, format, and one CTA. Rank as editorial recommendations unless comparative performance data exists. Do not equate a heuristic headline score with conversion or virality, especially across languages.
5. Keep claims stage-accurate: proposed, prototyped, tested, and production-ready are different. No invented time savings, testimonials, integrations, automatic sending, or scarcity. Label demo data and do not manufacture a before/after success story.
6. Recommend a small test spanning humor/recognition, emotional benefit, and founder/process evidence. Measure qualified conversations and pilot participation alongside retention/shares; sparse organic results are directional, not statistical proof.
7. Respect requested sequencing: if the user says to resolve copy before a dashboard, complete the copy first and explicitly leave the dashboard unbuilt. Do not imply an artifact exists or that a campaign has been published.

See `references/trend-informed-pilot-copy.md` for evidence boundaries, reusable messaging structure, and an SME campaign example.

## Common Monetization Patterns

- Curated calendar/newsletter/channel: “Qué hacer hoy en <city>”.
- Featured post/listing for promoters/vendors.
- Commission/referral per booking, ticket, reservation, or lead.
- Weekly venue/promoter package.
- Concierge recommendations for tourists/newcomers.
- Lead-gen directory/CRM.
- Local business launch kit: content plan, legitimacy posts, highlights, CTA, WhatsApp/reservation link.

## Common Pitfalls

1. **Overclaiming from weak data** — do not claim private analytics, reach, engagement, story activity, or conversion rates unless visible from tool output.
2. **Overbuilding too early** — validate with channels/forms/outreach before building apps or payment automation.
3. **Raw chat exposure** — summarize and extract curated lead fields rather than dumping sensitive conversation text.
4. **Avatar/logo scale failure** — full-size logos often fail in circular Instagram crops; explicitly evaluate miniaturization.
5. **Stale dates** — chat exports may be old; anchor “recent” to transcript max date unless a live current source is provided.
6. **Generic marketing fluff** — tie every recommendation to the observed profile, community, category, or competitor context.

## Verification Checklist

- [ ] Data was actually fetched or parsed and limitations are stated.
- [ ] Counts, metrics, and claims are traceable to tool output or user-provided context.
- [ ] CSV/report/post files exist and are readable when created.
- [ ] Lead targets include evidence: frequency/latest post/links/contact/sample.
- [ ] Outreach is not sent without explicit user approval.
- [ ] Final answer gives concrete next actions, not just analysis.
