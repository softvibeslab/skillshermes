# Static legal-page publishing

Use this for adding terms, privacy notices, acceptable-use pages, or similar legal routes to an existing static site.

## Minimal workflow

1. Read the existing legal page, footer, stylesheet, sitemap, and deployment notes before writing. Reuse the current legal layout and identity/contact facts instead of inventing a new template or legal entity.
2. Describe only the site's current behavior. For example, if a form prepares a WhatsApp message locally, do not claim server-side collection, accounts, payments, analytics, subscriptions, or contractual guarantees that do not exist.
3. Keep the page plain-language and scoped:
   - operator/contact;
   - site purpose and acceptance;
   - free diagnostic or informational-content boundaries;
   - separate project agreements for scope, price, delivery, licenses, and support;
   - AI limitations and human review for sensitive actions;
   - user responsibilities and acceptable use;
   - intellectual property;
   - third-party services;
   - availability, liability, privacy, governing law, updates, and contact.
4. Add the route to the main footer and sitemap. Cross-link related legal pages so no page is orphaned.
5. Validate local links and semantic HTML. A legal page normally needs no new JavaScript or dependency.
6. Discover the real production path before deployment: resolve DNS, inspect the active reverse proxy/service, and identify the served directory or documented upload mechanism. A healthy homepage does not prove a new route is published.
7. Use a configured deployment surface or credentials explicitly supplied/approved for this operation. Never recover or print secrets from shell history, logs, browser state, or unrelated files. If authorization is unavailable or an execution guard blocks the remote write, stop and report `ready locally, not published`.
8. Back up only files that will be overwritten, deploy the minimum file set, preserve expected owner/mode, then verify the exact public URL, title, links, and HTTP status. Do not claim publication before this check succeeds.

## Reporting states

Use one exact state:

- `Drafted locally` — content exists but local checks are incomplete.
- `Ready locally, not published` — local checks passed; deployment lacked an approved path or authorization.
- `Published and verified` — the exact public route and updated navigation return the expected content.

## Legal boundary

Do not present generated text as attorney-reviewed. If the operator's legal name, address, tax identity, jurisdiction, refund terms, subscription rules, or payment flow affect enforceability and are unknown, keep the page honest and flag those fields for legal review rather than guessing.
