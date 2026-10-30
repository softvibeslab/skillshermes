# Local subject package: technical recipe

Use this when implementing the workflow from `local-information-archivist`.

## Query matrix

Build queries from four classes:

| Class | Examples | Why |
|---|---|---|
| Name | full name, accent variants, misspellings | primary discovery |
| Identity | handle, phone digits, email, domain | catches unnamed references |
| Projects | exhibition, product, client, event | finds topic-adjacent evidence |
| Claims | distinctive phrase or title | finds reused bios and proposals |

Run exact secondary identifiers after the broad name query. They often uncover files whose indexed content omitted the name.

## Relevance decision

Keep a candidate when at least one applies:

1. The subject is the document’s main entity.
2. The file records a meaningful event, project, contact, work, agreement, or conversation involving the subject.
3. It contains reusable research or deliverables made specifically for the subject.
4. It is an image, attachment, or contact explicitly referenced in a relevant conversation window.

Discard generic dictionary/license/dependency hits and incidental mentions with no subject value. For borderline files, preserve a source-path entry rather than copying the whole file.

## Extraction rules

- PDF: copy the original and create a UTF-8 text companion with page separators.
- Image-only PDF: copy first; OCR only if searchable text is useful.
- HTML: preserve as HTML; rename descriptively without changing internal links.
- Image: inspect visually and give it a descriptive filename.
- Chat: extract merged line windows around hits; do not copy the complete export by default.
- ZIP: enumerate or selectively read text members; extract only relevant attachments unless the archive is dedicated to the subject.
- JSON/session data: include only when the session is dedicated to the subject or extract its relevant records.

## Chat context algorithm

1. Find lines matching subject identifiers.
2. Capture a small window around each hit, normally 5 lines before and 6 after.
3. Merge overlapping windows.
4. Preserve source filename and original line ranges.
5. Redact unrelated sensitive values caught by context.
6. Scan the output again after redaction.

Large multiline messages can hold the core artifact; do not truncate them blindly.

## Secret scan

At minimum scan generated extracts for:

- bank labels and long account numbers;
- private keys, wallet addresses, API keys, tokens, and signatures;
- password-like strings;
- unrelated emails and phone numbers;
- payment URLs carrying embedded credentials or wallet data.

Allow subject contact details only inside the explicitly private contact area. Do not rely only on keyword labels: secret values may appear on adjacent lines without labels.

## Dossier structure

A useful short dossier contains:

1. Executive summary.
2. Identity and aliases.
3. Timeline/events.
4. Projects and commercial material.
5. Research and strategy.
6. Digital footprint and links.
7. Reliability caveats.
8. Inventory summary.

Keep claims attributed: “a local promotional document states…” is safer than presenting it as fact.

## Deterministic verification

```text
[ ] generated dossier PDF opens and has non-empty text/pages
[ ] all copied PDFs open
[ ] ZIP integrity test passes
[ ] final file count and total size recorded
[ ] inventory destinations exist
[ ] hashes refreshed after final redaction
[ ] no secret-pattern matches outside private contact area
[ ] no destination files rediscovered as sources
[ ] duplicates and unrelated bulk exports excluded
```

A self-referential manifest is unnecessary. Hash package contents, excluding the manifest itself and final ZIP; then create the ZIP last.
