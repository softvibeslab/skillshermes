# Tourism marketplace swipe MVP notes

Use these notes when converting a tourism marketplace idea into an Expo validation prototype.

## Product pattern
- Guest enters through a hotel/Airbnb/property-manager QR or code.
- Guest selects interests, then swipes local experiences.
- Right swipe/superlike creates intent; available experience creates a match.
- Match should lead to WhatsApp/chat or a booking request.
- Hotel/Airbnb gets referral attribution and commission.
- Provider gets qualified demand and can pay for boosts/premium visibility.

## Prototype screens that validate the loop
1. Welcome/landing with destination positioning.
2. Hotel/Airbnb code validation screen.
3. Interest selection chips.
4. Tinder-style experience card stack.
5. Match success screen.
6. Basic dashboard showing guests, swipes, matches, bookings, and QR code.

## Recommended early implementation
- Start with Expo blank TypeScript.
- Keep the first prototype in `App.tsx` if speed matters.
- Use mock experiences with real-looking content and images.
- Add README and implementation plan immediately.
- Verify with `npx tsc --noEmit` before claiming it runs.

## Next real backend model
Core tables:
- profiles
- partners
- partner_codes
- providers
- experiences
- swipes
- matches
- bookings
- commissions

## Validation-first rule
For Playa del Carmen/Riviera Maya marketplace ideas, do not overbuild payments/chat first. Use QR + WhatsApp + lead tracking to validate hotel recommendation behavior, guest swipe intent, and provider willingness to pay commission.
