# Static contract-review dashboard handoff

Use when an existing project needs a lightweight browser view for a service contract, NDA, or similar editable legal drafts.

## Minimal implementation

1. Inspect the real source documents and choose the intended version explicitly; projects often contain several similarly named drafts.
2. Extract headings/metadata first so the dashboard checklist reflects the actual clauses and unresolved placeholders.
3. Reuse the existing dashboard and its design system. Add one static route rather than a new app, backend, database, or dependency.
4. Preserve the editable originals under the dashboard's public assets and render a browser-readable copy. On macOS, the native conversion is enough:

```bash
textutil -convert html -output public/contracts/service-agreement.html source.docx
```

Keep the DOCX alongside the HTML so reviewers can download and edit it.
5. The route needs only:
   - document tabs;
   - draft/review status;
   - a short clause-specific checklist;
   - full-document iframe or open-in-new-tab link;
   - editable-file download;
   - a visible “do not sign until reviewed/completed” notice.
6. Run the existing typecheck/build, verify the route and every document asset return HTTP 200 locally, then inspect both tabs visually.
7. Query the production route separately. A successful static build proves only that the artifact exists locally; if production still returns 404, report “built, not published.”

## Review handoff

- Put a readable reviewer label/name in the UI, not a raw Slack mention token such as `<@U…>`.
- Make the actual Slack mention in the channel message so the platform resolves and notifies it.
- Ask for review of concrete areas: identities/signatures, scope and acceptance, fees/taxes/payment, support/warranty, confidentiality, personal data/security, IP, liability/termination, governing law, and annex placeholders.

## Pitfalls

- Do not claim a dashboard is live because the existing homepage responds 200; check the new route itself.
- Do not add fake interactive checkboxes or say reviewers can “register” decisions unless state is genuinely persisted.
- Converted legal documents can be dense. Always include “open in another tab” and the editable DOCX download.
- Keep legal language labeled as a draft and avoid presenting a product checklist as legal advice.
- In a dirty or concurrently changing repo, touch only the dashboard route/assets and report unrelated changes separately.