# Prototype Brand Sanitization

Use when a generated or static prototype borrowed a real brand and must become distributable as a neutral demo.

## Scope the whole package

Search more than active HTML/CSS/JS:

- filenames, folder names, documentation, design specs, alt/ARIA text, localStorage keys, fixture data, comments, titles, and metadata;
- generated reference screens, screenshots, image assets, exported ZIPs, and stale source snapshots;
- colors, typography lockups, mascots, icon silhouettes, merchant names, account/card examples, and remote asset URLs that can preserve recognizable identity without naming it.

Inspect archive contents before deleting them. A clean active tree is insufficient if the deliverable still ships branded historical copies.

## Minimal neutralization

1. Prefer a generic product label over inventing another commercial brand or isotipo.
2. Replace distinctive brand colors with a neutral accessible palette while preserving contrast and hierarchy.
3. Remove non-functional brand-specific controls instead of renaming them.
4. Replace branded/remote visual assets with simple local neutral placeholders.
5. Use conspicuously synthetic identifiers and generic merchants; keep a visible demo/no-real-data warning.
6. Rewrite documentation and design tokens so the package does not reintroduce the old identity later.
7. Preserve the existing architecture unless the user separately requests a production redesign.

## Verification

- Search the full remaining tree for names, known numbers, color values, CSS class names, asset filenames, and old storage-key prefixes.
- Validate all local `src`/`href` references after deletion.
- Run syntax checks, then exercise the primary SPA flow and any independent dashboard.
- Check console output, broken-image states, layout gaps left by removed logos, and camera/permission fallbacks.
- Report deleted archives/reference directories explicitly because sanitization is a packaging change, not only a UI edit.

Neutral branding does not make client-side credentials, biometric storage, PAN/CVV handling, or frontend-only authorization production-safe.