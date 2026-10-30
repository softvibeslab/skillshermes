# Local lead-intelligence control tower

Use this pattern after parsing a community export into demand, inventory, and B2B target CSVs.

## Minimum useful artifact

Build a self-contained local HTML dashboard rather than a new application stack. Embed compact JSON generated from the CSVs so the file opens directly and keeps private exports on-device.

Recommended modules:

- Overview: demand, high-priority signals, inventory, active B2B targets, outreach queue.
- Demand: search plus category and score filters; detail drawer with source signal and suggested message.
- Inventory: search plus operation/property/location/price filters.
- Match engine: select one demand record and rank inventory.
- Targets B2B: activity, supply/demand counts, categories, contact evidence.
- Pipeline: pending, contacted, replied, demo/close; persist state in `localStorage`.

## Match heuristic

Start with an explainable weighted score:

- Same operation/category: 4 points.
- Same property type: 3 points.
- Overlapping normalized location token: 3 points when demand has a location.

Calculate percentage against only the available criteria. Display the reasons beside every result. This is intentionally a shortlist heuristic, not proof of compatibility.

Add filters for minimum match, operation, property type, free-text zone, price/currency text, and recency relative to the newest record in the export—not the machine clock.

## Strategy generator

From the filtered match results, create a Top 5 and a concrete execution sequence:

1. Verify the demand is current and confirm budget, timing, and non-negotiables.
2. Verify availability and commission with brokers represented in the Top 5.
3. Reduce to 2–3 verified finalists.
4. Send finalists with one clear closing question for a call or visit.
5. Record the response; follow up at 24 hours and once more at 72 hours.

Provide a copy button for the generated Top 5 and steps.

## Data-quality guardrails

- Chat classifiers often misread promotional phrases such as “Are you looking for…?” as demand. Keep a visible “verify validity and false positives” warning.
- Prefer high-precision demand patterns such as “busco”, “se busca”, “I am looking for”, or “looking for a client”; exclude listing language such as “for sale”, “prices from”, “schedule a visit”, and “move-in ready”.
- Do not claim exact budget compatibility until currencies, units, ranges, and formats have been normalized.
- Show at most the first 100–300 table rows while keeping filtering over the full local dataset.

## Verification

- Generator script should assert that the HTML exists, contains the expected title/module, and exceeds a sensible minimum size.
- Open through a local HTTP server.
- Check browser console for JavaScript errors.
- Exercise one match, one recency filter, and strategy generation; confirm five Top entries and five execution steps.
