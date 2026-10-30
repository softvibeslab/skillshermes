---
name: local-information-archivist
description: Discover, verify, deduplicate, extract, and package all locally stored information about a person, project, client, or topic into a privacy-aware, Drive-ready archive. Use for requests like “search my whole computer,” “collect everything about X,” “organize it in a folder,” or “make a PDF dossier.”
version: 1.0.0
---

# Local Information Archivist

Build a complete, traceable local evidence package without dumping unrelated private data into it.

## Outcome

Create one subject folder that is:

- organized for a human to browse;
- searchable even when originals are PDFs;
- deduplicated;
- explicit about original source paths;
- safe to share at the intended privacy level;
- verified before reporting completion.

## Workflow

### 1. Define the subject and exclusions

List name variants, handles, URLs, phone identifiers, project names, common misspellings, and aliases. Exclude the destination folder from every search to prevent recursive rediscovery.

Use the user’s obvious scope immediately. If they say “my whole computer,” search the home directory, Spotlight-indexed content, and mounted volumes; do not stall for clarification.

### 2. Search in layers

Stop when additional layers only produce duplicates or generic false positives:

1. Spotlight metadata/content search (`mdfind`) for indexed documents, PDFs, images with OCR metadata, browser artifacts, and filenames.
2. Filename fallback across the requested roots and mounted volumes.
3. Content search across likely text/code formats, excluding `.git`, dependency trees, caches, and the destination.
4. Exact secondary identifiers such as a known URL, handle, phone number, or distinctive phrase.

Do not treat every lexical match as relevant. Generic first names inside software dictionaries, licenses, dependencies, and password-strength corpora are false positives unless surrounding context identifies the subject.

### 3. Inspect before copying

For each candidate:

- identify file type and size;
- extract text from text-based PDFs with PyMuPDF;
- inspect scanned/image-only PDFs visually or with OCR only when needed;
- inspect images with vision, using contact sheets for bounded batches;
- inspect archives selectively rather than expanding everything;
- capture a short relevance snippet for classification.

For named-person photo searches, establish identity from a labeled or user-confirmed reference image. Treat chat proximity, filenames, OCR, and automated face similarity only as candidate signals; manually verify every final inclusion. If a mass face scan is slow or unstable, narrow the candidate set by names, chats, timestamps, and source documents instead of brute-forcing the whole home directory.

A filename hit is not sufficient evidence of relevance.

### 4. Minimize privacy exposure

Prefer subject-only extracts over copying large conversations or archives containing unrelated people.

- For chat exports, save merged context windows around subject hits.
- Preserve attachments explicitly referenced in relevant windows.
- Put contact cards and personal identifiers in a clearly marked private folder.
- Sanitize unrelated credentials, bank data, wallet addresses, tokens, and passwords that fall inside context windows.
- Run a second secret-pattern scan against the generated extracts before packaging.

Never simplify away this boundary check.

### 5. Organize the package

Use the smallest useful structure:

```text
00_LEEME/
01_PDFs/
02_WEB_Y_RUTAS/
03_IMAGENES/
04_CHATS_EXTRAIDOS/
05_CONTACTO_PRIVADO/
06_DATOS_FUENTE/
07_TEXTO_EXTRAIDO/
```

Include:

- `LEEME.md`: contents, coverage, exclusions, privacy warning, and unverified claims;
- a concise dossier PDF when requested;
- `inventario.csv`: type, original path, destination, bytes, SHA-256;
- `MANIFIESTO_SHA256.csv`: hashes for packaged files;
- extracted PDF text for searchability;
- a ZIP only when it materially helps upload or transfer.

Do not add elaborate metadata schemas unless requested.

### 5.1 Route media-only requests to a compact package

When the request is specifically to collect a person's photos or other media, use the same discovery, privacy, provenance, and verification gates but avoid forcing the full dossier tree. Copy rather than move originals; preserve original formats and metadata; separate confirmed files from `REVISAR/`; deduplicate by hash; and produce a manifest with destination filename, source path, source type, match basis, confidence, and hash. Counts must be stated by confidence and accessible source rather than claiming “all.”

Before using Photos or messaging apps, follow the live-app and identity controls in `references/photo-collection.md`. A request to collect media never authorizes sending messages, changing chats, onboarding an app, or granting permissions.

### 5.2 Build a separate shareable staging layer

If the destination is Drive or another potentially shared location, do not upload the internal archive directly. Create a second staging folder containing the dossier, curated research, graph/report, selected non-private sources, a privacy/exclusions README, and a manifest generated from that final staging tree.

Exclude raw chats, VCFs, participant screenshots, agent-session dumps, private source paths, and stale manifests that enumerate excluded files. Relevant subject knowledge belongs in the curated dossier; unrelated PII does not.

After every removal or redaction, regenerate the manifest and ZIP, rerun secret/PII scans, and test archive integrity. For Drive API sync, verify the token has a write-capable Drive scope, confirm the target folder allows children, upsert by parent/name, and read back the result.

### 6. Separate evidence from claims

In the dossier, distinguish:

- directly observed local evidence;
- statements made in chats or promotional documents;
- AI-generated research or valuation estimates;
- independently verified facts.

Label unverified biographies, credentials, prices, awards, and relationship claims. A locally repeated claim is not automatically true.

### 6.5 Handle mixed local + cloud collection as a resumable job

When one archive combines local files with Google Drive or another authenticated cloud source:

1. Check cloud authentication before starting the expensive local scan.
2. If reauthorization is required, generate the exact consent URL immediately and continue the local collection into a stable staging folder while waiting for the callback.
3. Keep local and cloud manifests separate until both sources finish, then merge and deduplicate by SHA-256.
4. Make the collector resumable: reuse already-copied hashes and never restart a whole-computer scan merely because cloud authorization arrived later.
5. Do not create or announce the final ZIP until all requested sources are either collected or explicitly marked unavailable by the user.
6. If browser automation could reuse an existing signed-in session, treat it as a fallback that requires tool approval; never silently substitute it for API authorization.

### 7. Verify before completion

Leave one runnable check behind:

- open every generated PDF and confirm page count/text presence;
- test ZIP integrity;
- confirm destination file count and size;
- refresh inventory hashes after every edit;
- scan extracts for accidental secrets;
- ensure the destination was excluded from source discovery;
- confirm no unrelated bulk archive was copied merely because it contained one match.

Report the absolute folder path, optional ZIP path, file count, main contents, and privacy boundary in a concise completion message.

## Pitfalls

- Copying a 300 MB chat ZIP when two relevant messages and one VCF are sufficient.
- Trusting Spotlight alone; combine it with focused content and filename searches.
- Copying browser preferences or dependency dictionaries because they contain the same first name.
- Generating a dossier without preserving source paths and hashes.
- Hashing files before a final redaction, then forgetting to refresh the manifest and ZIP.
- Treating a raw agent-session export or original-path inventory as shareable because it contains no obvious password; these often expose account emails, phone numbers, local identities, and private paths.
- Reusing a read-only Workspace token for an upload flow; request explicit write scope with a dedicated token and verify destination capabilities.
- Publishing “last disciple,” valuations, credentials, or similar promotional claims as verified facts.

## Reference

See `references/local-subject-package.md` for a compact technical recipe, relevance scoring, redaction checks, and verification sequence.

See `references/photo-collection.md` for named-person photo discovery, read-only macOS WhatsApp handling, contact-sheet review, identity verification, and minimal Drive-ready packaging.

See `references/drive-safe-sync.md` for the internal-vs-shareable split, final PII gate, write-scoped Google Drive OAuth, idempotent folder sync, and graph/dossier verification.
