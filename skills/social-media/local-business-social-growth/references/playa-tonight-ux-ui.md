# Playa Tonight UX/UI Pattern

Session pattern for turning a monetized community-calendar concept into app + landing design artifacts.

## Strategic framing

For local event/community chat monetization, position the product as a **curated discovery layer**, not another noisy group:

- User promise: “Sal hoy sin revisar 8 grupos.” / “Find the right plan tonight.”
- Supplier promise: “Convert attention into attendance.”
- MVP channel: WhatsApp/Telegram + landing + self-serve event submission before building a full app.

## UX/UI trends applied

Use these as design requirements, not decorative copy:

1. **AI discovery by intent**
   - Search prompt examples: “¿Salsa, rooftop o algo tranquilo?” / “Recomiéndame algo para ir solo”.
   - Keep recommendations explainable with visible tags and filters.

2. **Curation over infinite feeds**
   - Emphasize Top 5 / today / this week.
   - Avoid raw feed dumps from group exports.

3. **Mobile thumb-first**
   - Bottom navigation belongs inside the app mockup/prototype, not as a page-level fixed nav on desktop.
   - 44px+ tap targets, sticky reserve CTA on event detail.

4. **Trust before conversion**
   - Show date/time, location, price, organizer/promoter, vibe labels, “good for going alone/groups/beginners”.

5. **Map/list hybrid**
   - Local events need both curated list and map affordance.

6. **Promoter self-serve**
   - Form fields: event name, date/time, place/Google Maps, price, link/WhatsApp, short vibe description.
   - Copy: “Publica en 60 segundos.”

## Visual direction

Blend:

- Airbnb-like marketplace trust: warm surfaces, rounded cards, strong CTA, clear pricing/location.
- Spotify-like discovery energy: compact mobile feed, chips, dark premium surfaces, content-as-color.
- Local/tropical palette: coral action, teal trust/local, lime energy/nightlife, night premium, sand background.

Suggested tokens:

- Coral/action: `#ff385c`
- Teal/trust: `#007c78`
- Lime/night energy: `#d9ff63`
- Night/premium: `#11191f`
- Sand/background: `#fff8ee`

## Deliverables to create

When user asks for “app + landing” after chat monetization analysis, generate one high-fidelity HTML artifact with:

- Trends section translating UX/UI trends into product decisions.
- App mockups: home discovery, event detail, promoter submission.
- Landing preview: user CTA + promoter CTA + venue segment.
- System section: palette, components, positioning.
- Final CTA: publish landing / create app prototype.

## Verification pitfall

If the page contains mobile bottom navigation, ensure `.phone-screen` or mockup container is `position: relative`; otherwise `.tabs { position:absolute }` may escape and appear as a floating desktop nav across the page. Verify with browser screenshot/vision and console check.