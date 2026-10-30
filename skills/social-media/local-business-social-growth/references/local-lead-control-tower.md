# Local Lead-Intelligence Control Tower

Use this pattern after parsing a community/chat export into demand, inventory, and B2B target CSVs.

## Minimum useful dashboard

Build a self-contained local HTML artifact before adding a backend. Embed the parsed data as JSON so it opens directly and does not expose community data to third parties.

Views:
- Executive summary: demand, high-priority leads, inventory, active B2B targets, outreach count.
- Demand: search plus category and score filters; detailed signal drawer; suggested message.
- Inventory: search by broker, zone, price, property type, or text.
- B2B targets: activity, supply/demand counts, categories, available contact.
- Outreach pipeline: pending, contacted, replied, demo/close.

Interaction:
- Persist pipeline state in `localStorage` for a no-backend pilot.
- Limit rendered tables to a practical first page (for example 300 rows) while keeping filtering across the complete in-memory dataset.
- Add responsive navigation and 44px mobile targets where practical.
- Keep lead details in a drawer rather than expanding every row.

## Data-quality guardrail

A high score does not prove a valid demand lead. Real-estate inventory often contains phrases such as “Are you looking for…”, which naive keyword rules misclassify as demand. Show a visible warning to validate freshness and false positives before outreach. For demos, use high-precision requests such as first-person “busco”, “se busca”, “I am looking for”, or “looking for a client”, and exclude listing language such as “for sale”, “prices from”, “schedule a visit”, and “move-in ready”.

## Privacy and outreach

- Keep raw exports and embedded data local unless the user explicitly requests publishing.
- Prefer anonymized samples for sales demos.
- Never send outreach merely because messages are prepared; require explicit approval of targets and exact copy.
- Start with 3–10 personalized contacts and measure replies before automation.

## Verification

1. Assert the generated HTML exists and contains the expected embedded counts.
2. Serve locally with `python3 -m http.server` for browser verification.
3. Check browser console for JavaScript errors.
4. Click at least one navigation view and verify pipeline rendering/state changes.
5. Visually inspect overflow, feed truncation, empty space, contrast, and mobile behavior.
