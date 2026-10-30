# Real-estate community signals → control tower

Use this pattern when an exported WhatsApp real-estate group must become an operational lead product rather than a static report.

## Data products

Normalize the export into four curated datasets:

- demand signals: sender, date, operation, property type, location, score, phone, price text, source message;
- inventory signals: broker, date, operation, property type, location, price text, source message;
- B2B targets: sender, activity, offer/demand counts, contact evidence;
- outreach pipeline: target, message, status, notes.

Do not expose the raw chat when a curated signal is enough. Keep outreach manual until the user explicitly approves sending.

## High-precision classification

Real-estate promotions often contain phrases such as “are you looking for...” and are easy to misclassify as demand. A demand shortlist should require first-person/client request language such as:

- `busco`, `buscamos`, `se busca`, `cliente busca`;
- `I am looking for`, `looking for a client`.

Exclude listing language such as:

- `for sale`, `move-in ready`, `prices from`, `schedule a visit`;
- `sold fully furnished`, `HOA`, `property tax`, `oportunidad de reventa`;
- rhetorical inventory hooks such as `are you or a client looking for...` when the same message contains price, amenities, availability, or a visit CTA.

Deduplicate exact or normalized repeated inventory before matching. Report both raw publication count and distinct inventory count; a high repetition rate is itself a coordination signal. Deduplicate aggregator demand by stable request ID when present, and repeated broker requests by normalized sender + text.

Anchor recency to the transcript’s latest date. Always visually review a small recent sample before presenting counts or a demo.

## Control-tower MVP

A self-contained HTML artifact is enough for validation. Embed normalized JSON so it works locally without a backend. Useful modules:

1. overview KPIs and category/location distributions;
2. searchable demand and inventory tables;
3. B2B target ranking;
4. editable outreach pipeline persisted in `localStorage`;
5. demand ↔ inventory match module;
6. Top 5 and an actionable follow-up strategy.

Keep the source generator beside the HTML so new exports can rebuild it deterministically.

## Match heuristic

Start explainable and conservative:

- same operation: 4 points;
- same property type: 3 points;
- overlapping normalized location: 3 points.

Show reasons next to every score. Add inventory filters for operation, property type, zone, price text, age, and minimum match. Treat free-text price comparison as provisional until currencies and ranges are normalized.

A generated strategy should:

1. verify the demand is still active;
2. confirm budget, dates, and non-negotiables;
3. verify availability and commission with brokers behind the Top 5;
4. reduce to 2–3 verified finalists;
5. contact the lead with a clear closing question;
6. schedule 24h and 72h follow-up.

## Integration into a network-intelligence product

Do not iframe the standalone dashboard into a real product. Promote its domain model into the host API:

- sender → Contact;
- source group → Group;
- demand/inventory row → Signal;
- ranked pair → Opportunity.

Then combine property compatibility with relational confidence: shared groups, direct/second-degree paths, broker influence, and recent activity. Preserve human approval before messaging.

Minimal entities: `Contact`, `Group`, `Signal(kind=demand|inventory)`, and `Opportunity(demandSignalId, inventorySignalId, score, reasons, status, strategy)`.

## Verification

- Generated files exist and counts match source datasets.
- Search and filters update result counts.
- Selecting a demand returns ranked inventory.
- Top 5 contains exactly five items when enough results exist.
- Strategy contains runnable steps.
- Pipeline state survives refresh.
- Browser console has no JavaScript errors.
