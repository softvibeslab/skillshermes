# Static landing release verification

Use this when publishing a prebuilt static landing to an existing file manager, upload API, object store, or web root.

## 1. Discover the real publication path

Before asking for new credentials, search existing project docs and local operational notes for:

- canonical domain and web root;
- dashboard or upload API;
- authentication method;
- expected root shape (`index.html` at root, not nested under the source folder);
- rollback location or previous artifact.

If SSH fails, do not conclude deployment is blocked until the project's native dashboard/API path has been checked.

Never print recovered passwords or tokens. Read them programmatically from their existing protected source and keep command output secret-free.

## 2. Inspect before replacing

List remote files first. Download the current public entry point to a timestamped local backup before overwriting it. Avoid deleting unrelated remote files unless replacement scope explicitly requires it.

For file-upload APIs, preserve each local path relative to the publish root and send bytes directly. A successful HTTP upload is only transport confirmation, not release verification.

## 3. Verify exact production bytes

For every published file:

1. Fetch its public URL.
2. Compare SHA-256 of public bytes with the local source.
3. Verify expected status and content type for HTML, CSS, JS, images, `robots.txt`, and `sitemap.xml`.

This catches partial uploads, stale assets, wrong nesting, and cache/proxy mismatches.

## 4. Run browser and functional QA on the public URL

Check:

- correct title and `lang`;
- no console or JavaScript errors;
- no horizontal overflow at mobile width;
- all hash anchors resolve;
- privacy route and assets load;
- navigation and tabs behave;
- content remains visible with JavaScript disabled or unsupported;
- mobile full-page screenshot has no clipping or missing sections.

For forms that open WhatsApp/email instead of posting to a backend:

- submit empty fields and assert accessible validation/status text;
- replace `window.open` with a local capture function in the browser test;
- submit valid values and assert the generated URL contains the correct destination and encoded fields;
- never open the external destination or send a real message during QA.

## 5. Accessibility/performance loop

Run Lighthouse (or equivalent) against production, not only localhost. Fix exact audit nodes, republish only changed files, and rerun until the target is met.

Common static-landing fixes:

- `aria-label` on a plain decorative `<span>` is invalid unless it has an appropriate semantic role; prefer visible text or add the correct role only when the state must be announced.
- Declared image `width`/`height` must match the source aspect ratio even when CSS constrains the rendered size.
- One brand accent rarely satisfies contrast on both light and dark surfaces. Use a darker token on light backgrounds and a brighter companion token on dark backgrounds rather than sacrificing brand identity globally.
- Keep content visible by default; JavaScript/intersection observers may add decorative motion, not structural visibility.

## 6. Release evidence

Do not say “published” until all are true:

- canonical public routes return 200;
- public bytes match local files;
- browser console is clean;
- responsive overflow/anchors pass;
- form success and failure paths pass without external side effects;
- accessibility/SEO scores are recorded;
- rollback artifact path is known.
