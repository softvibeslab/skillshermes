# Chat and multimedia to operational productivity reports

## Scope and acceptance

Use for private exported chats plus attachments and a user-supplied reporting template. Read-only discovery precedes generation. If asked only for a plan, deliver the source inventory, proposed window, extraction method, metrics, unknowns, and verification gates; do not implement deliverables without authorization.

For “last N days,” state the anchor and inclusive dates; distinguish calendar days from a rolling-hour window. Check the export's coverage and report gaps or a partial final day. Do not silently substitute the last available message date for today.

## Canonical ledger

Keep one row per operational event with:

- stable event ID and order ID, when available;
- raw technician label and normalized label, with unresolved identities separate;
- message timestamp, source line/message reference, raw excerpt;
- attachment filename and evidence reference;
- actual work date and its source, or unknown;
- raw work code, mapped category, mapping authority;
- reported status and evidence status as separate fields;
- inclusion flag, exclusion reason, duplicate/correction relationship;
- review state and unresolved discrepancies.

Do not merge people based only on similar names. Retain original spellings. A later status update for the same order is not automatically another completed job; define the counted event before aggregating. Preserve conflicting dates/statuses instead of silently overwriting them.

## Dates and media

Message timestamps select the communication window; actual work dates select production when supported. File modification times are not reliable work dates. If both communication activity and work completion are useful, expose separate metrics and explain their filters.

An image delivered in the current window may show an older completion date. Keep it in the media inventory but exclude it from current-period production, with a reason. Unknown work dates belong in an unresolved bucket unless the user explicitly accepts a message-date proxy; label that proxy.

Inventory all media types before processing. Detect available local extraction tools, favor local OCR for private images, and use visual inspection for critical/ambiguous dates, order numbers, and statuses. Transcribe audio or inspect video/document content when relevant and supported; otherwise record it as unreviewed. Do not upload private exports to an external OCR service without authorization.

Record coverage separately: files inventoried, OCR attempted/succeeded, originals visually reviewed, and unsupported/unreviewed files. OCR of all images is not full visual review of all attachments. Keep filename-to-message linkage so a reviewer can revisit the exact evidence.

## Template fidelity and metric limits

Inspect the actual workbook/document, not just its filename. Preserve headings and units; keep a small mapping table for raw codes to requested categories. Require documentary or user confirmation for ambiguous mappings. Missing category/zone/target is N/D, not zero.

Label sums as reported completions or reported liquidations when the chat is the only authority. Verification evidence can be a separate metric. Do not calculate efficiency, target attainment, or comparative performance without the required denominators. Explicitly flag that observed chat activity may omit real work.

## Generate and verify

Use the canonical ledger for all derivative outputs: spreadsheet detail and aggregates, dashboard dataset, executive summary. A minimal local HTML dashboard can suffice; reuse installed spreadsheet tooling rather than adding an application stack.

Leave one runnable check covering these invariants:

1. Included rows meet the declared date/status/counting rules.
2. Excluded historical records cannot enter current totals.
3. Duplicate messages cannot double-count the same operational event.
4. Per-person and per-day aggregates reconcile with the total.
5. Spreadsheet, dashboard payload, and summary agree with the ledger.
6. Missing values remain distinct from zero.

Then exercise dashboard date/person/status filters, reset, combined filters, and empty results in an actual browser. Check narrow layouts and evidence-link resolution from the intended delivery location. Distinguish structural checks from browser verification.

Preserve originals; put derivatives in a separate output folder. Avoid absolute private-source paths in a public artifact, and treat any shareable copy as a separate privacy-reviewed export.

## Portable visual evidence: implementation recipe

When the user asks for images in the report, a path or hyperlink is not an embedded image. Detect available image/spreadsheet libraries and browser verification tools first; use existing tooling rather than introducing a new application stack.

1. Preserve folios as strings during extraction, JSON serialization, Excel writes, and browser searches. For example, `00000000000` must not become `87572305`. Write Excel identifiers as text. Do not merge variants or assign evidence based on numeric equivalence or nearby chat messages alone.
2. Create a separate evidence manifest: evidence ID, private source reference, sanitized derivative filename, literal folios, work date, sent date, direct/context/historical classification, association rationale, and limitations. A contextual attachment is not proof of a technician's completion. Historical refers to time eligibility and may coexist with direct evidence of older work; keep those dimensions explicit.
3. Produce sanitized raster derivatives before packaging. Crop or paint opaque redaction blocks into the actual pixels, flatten, and re-encode without source metadata. Review resulting images visually; inspect surrounding captions, filenames, alt text, and HTML/Excel metadata for PII too. Keep originals outside the delivery artifacts. This is redaction of identified fields, not a guarantee of irreversible anonymity.
4. For a bounded gallery, embed sanitized images as MIME-correct Base64 data URIs in the HTML so it remains usable offline. For larger collections, measure size and agree on a portable asset bundle instead of silently degrading portability. In Excel, use installed tooling such as `openpyxl.drawing.image.Image` to add actual drawing objects with bounded dimensions and enough row/column space.
5. Provide an order/evidence sheet for verified associations and a stable evidence atlas with image, evidence ID, classification, date, and caveat. Reuse the same evidence ID if an image appears in both sheets. Unique images, drawing placements, and verified work orders are different counts. Floating Excel drawings may not follow sorted rows reliably: keep the atlas stable, link sortable detail to it, and disclose this limitation.
6. In the dashboard, show summary KPIs before detail; implement date/person filters, literal folio search, reset/empty states, and a gallery with an accessible modal. Exact folio equality takes precedence over substring matching; only use partial matching when no exact result exists. Support Escape, keyboard activation, focus return, labeled controls, and narrow screens without horizontal overflow. Ensure historical/context gallery items cannot inflate production KPIs.

### Verification additions

Extend the reconciliation check rather than introducing a separate testing framework:

- Assert leading-zero identifier round trips and correct exact-search precedence.
- Validate every evidence association against the manifest, including intentionally unassigned context images.
- Decode the HTML image payloads and compare them with approved sanitized derivatives; inspect the XLSX ZIP media/drawing relationships or reopen it to verify actual embedded objects.
- Calculate expected unique image count and expected placement count from the manifest; do not hardcode counts from a previous reporting period. One image repeated across sheets can legitimately mean more drawings than unique images.
- Test browser filters, folio searches, no-results/reset, viewer keyboard behavior, and mobile width. Confirm the file works without access to the original image folder. Review the workbook in a spreadsheet viewer when available; otherwise report structural verification without claiming visual verification of Excel.
- Re-run checks after the final edit and deliver the verified filenames. Evidence samples do not prove complete multimedia coverage or independently verify every reported completion.

## Delivery wording

Give exact artifact paths and the reporting window, followed by the primary measured result, its evidence level, coverage limits, and unresolved mappings. Never claim all multimedia was analyzed if only image OCR and a visual sample were completed. Do not publish or send the report merely because local generation was authorized.

## Motivating edge case

In the field-team reporting workflow behind this reference, a recently shared completion screenshot referred to work from an earlier month. Separating sent date from work date prevented inflated current-period totals. Other transferable safeguards were preserving the supplied template's categories as unresolved where code mappings lacked evidence and deriving Excel, dashboard, and narrative from a single ledger. These are methodology examples, not reusable team performance facts.
