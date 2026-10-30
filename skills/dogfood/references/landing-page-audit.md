# Landing-page audit checklist

Use this after the normal dogfood functional pass.

## 1. Establish the audience and job

Evaluate separately for each plausible audience (for example, hungry customer vs. restaurant owner). A polished page can still fail if it mixes incompatible jobs.

Record:
- Primary audience
- Single intended action
- Whether the CTA completes that action
- Information required before the user can act

If the audience is ambiguous, report both lenses and recommend one default rather than stalling.

## 2. Verify before judging

- Confirm HTTP success and page title/description.
- Check the browser console after load and interactions.
- Inspect the accessibility snapshot and the rendered page.
- Exercise search empty states, primary CTA, modals, language switchers, and feedback controls.
- Inspect source/DOM when clicks appear successful but state does not change; distinguish an automation miss from an application bug.

## 3. Conversion review

Check:
- Hero explains value rather than internal process.
- One dominant CTA exists above the fold.
- CTA leads to a meaningful next step; a selector that opens a dead-end modal is not conversion.
- Trust disclosures are concise and do not overwhelm the offer.
- Operational facts (price, availability, hours, contact, location) appear before research methodology for consumer flows.
- Controls earn their space. Search is usually unnecessary for only a few products.

## 4. Localization checks

Do not accept a translated product title as a working language switch. Verify:
- Navigation, hero, facts, buttons, empty states, modals, status messages, dates, and accessibility labels
- `html[lang]`
- Search terms/data in the selected language
- Image alt text and metadata where relevant

Prefer removing a partial language switch until the full experience is translated.

## 5. Modal and selection checks

Verify:
- `role="dialog"` and `aria-modal="true"`
- Initial focus, focus trap, Escape close, and focus restoration
- Background scroll lock
- No accidental duplicate selections
- Remove/edit action where selections persist
- A clear completion action

## 6. Feedback/NPS checks

A click should leave a persistent visual and accessible selection (`aria-pressed` or equivalent). For a demo, show the complete branch outcome; do not imply storage or review publishing when none occurs.

## 7. Responsive-testing pitfall

A headless-browser `--window-size` screenshot can be cropped to the requested width while layout uses a larger minimum inner viewport. Before reporting overflow:

1. Read `window.innerWidth`, `document.documentElement.clientWidth`, and `document.documentElement.scrollWidth`.
2. Confirm the CSS breakpoint actually fired.
3. Prefer device-metrics emulation through browser tooling/CDP.
4. Treat a screenshot as evidence only when viewport metrics match the intended device width.

Never report clipping from a cropped screenshot alone.

## 8. Report shape

Return:
1. Short verdict and scores by design, trust, conversion, and utility
2. What works
3. Critical conversion blockers
4. Verified functional/accessibility issues
5. Prioritized changes: now, after validation, later
6. Explicit simplifications to remove until content justifies them
