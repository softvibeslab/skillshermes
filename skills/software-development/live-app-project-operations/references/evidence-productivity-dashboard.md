# Evidence-backed productivity reports: chat → Excel → static dashboard

## Scope and source truth

- Establish the exact inclusive date interval and its anchor before extracting “last N days”; a stale export's last date and today's date are different anchors. State which was used.
- Inspect the user's example workbook/report before designing the replacement. Reuse its meaningful columns and explain any unavailable metrics rather than inventing values.
- Keep chat timestamps, attachment association, and dates printed inside an image distinct. An old document shared during the period is historical evidence, not current productivity.
- Separate source messages, reconstructed activity rows, unique orders, and reported completions. These counts need not match. Repeated updates must not inflate the completion KPI.
- Preserve order IDs as strings through parsing, JSON, Excel, filters and joins. Leading-zero variants are different unless a source explicitly establishes equivalence. Search may be broad, but evidence joins must remain exact.
- Maintain a small evidence catalogue with source attachment/message, date basis, literal identifiers, supported claim, and limits. An identifier match alone establishes neither technician attribution nor completion. Contextual images stay unassigned when association cannot be verified.

## Anonymized derivatives

1. Keep original media and OCR in a private directory excluded from the publishing tree.
2. Render opaque redactions into new image pixels; do not depend on a removable HTML overlay or spreadsheet shape. Strip unnecessary metadata when re-encoding.
3. Review the full-size derivative visually, including edges, headers and handwritten text. Never trust a filename containing “anonymized” as proof.
4. Review the entire publication set for sensitive names, phones, credentials and operational identifiers. Image redaction alone does not sanitize HTML, JSON, workbook cells or downloads.
5. Keep the publish directory allowlisted: reviewed HTML, workbook, approved explanatory files and required assets only. Do not archive the parent analysis directory.

## Portable artifacts and UI

- For a small evidence set, embed processed images as data URLs in standalone HTML and `openpyxl.drawing.image.Image` objects in Excel. No backend or image hosting is required.
- Excel: include an introduction/index, dedicated evidence gallery, and an orders/evidence sheet with thumbnails only for verified literal joins. Maintain readable image dimensions and row heights.
- Conventional openpyxl images are floating drawing objects, not sortable cell values. Explain that sorting their sheets can misalign them; use a separate image-free sortable data sheet when needed.
- HTML: provide technician/date/order filters, visible active-result counts, reset, responsive tables, accessible image buttons and an integrated keyboard-dismissable viewer.
- el operador's preference: all details sections open on initial load, including matrix, criteria and references. Preserve this in templates and dynamic rendering, not only the final HTML. Users must still be able to close each section.

## Smallest useful checks

Leave a runnable check covering literal IDs (including a leading-zero pair), no historical/contextual evidence counted as completion, expected embedded media in HTML/XLSX, and no private-path dependencies. Validate joins rather than asserting only the image count.

Browser acceptance should exercise the actual event listeners: select a known technician, check the expected filtered count, reset to the full count, open/close an image, verify every initial details element is open, check mobile overflow and inspect console errors. Derive expected counts from the verified dataset, not hard-coded historical session totals.

## Publication acceptance

Follow `hostinger-static-dashboard-deployment.md` for provider mechanics. Create a separate `index.html` export rather than renaming the canonical local dashboard. Verify every local download link exists in staging; compare deployed artifact hashes over valid HTTPS and exercise interactions on the actual public URL.

If a new hostname resolves differently across resolvers, distinguish local resolver delay from server/TLS failure. Query current authoritative/public DNS before using `curl --resolve host:443:CURRENT_IP` as a diagnostic; preserve certificate validation and the requested hostname. Do not borrow a sibling site's IP or permanently pin a CDN address. A resolve override proves that endpoint, not universal DNS propagation; independently check the ordinary browser URL.

State sharing accurately: `noindex`, `nofollow`, `noarchive` and `robots.txt` do not authenticate visitors. A public dashboard may still expose technicians and order IDs even when customer images are redacted. If private access is required, protect the dashboard and all downloadable assets, not just the HTML entrypoint.

Final handoff: live URL, workbook link when useful, checks actually performed, and any remaining access/DNS limitation. Report chat-documented completions as reported, never independently certified merely because images were included.
