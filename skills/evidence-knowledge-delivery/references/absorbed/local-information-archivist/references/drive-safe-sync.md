# Privacy-safe Drive synchronization

Use this after the local archive and derived dossier/knowledge graph are complete.

## Two-layer delivery

Keep two distinct outputs:

1. **Internal archive:** originals, private chats, VCF/contact cards, screenshots, full provenance, and sensitive source paths.
2. **Shareable staging folder:** dossier, curated research, graph/report, selected non-private source material, and a fresh manifest.

Do not upload the internal archive merely because the user says “everything” when the destination may be shared. Preserve all subject knowledge by integrating relevant facts into the curated dossier while omitting raw PII.

Common exclusions from the shareable layer:

- chats and contact cards;
- videollamada/WhatsApp screenshots and participant photos;
- raw agent-session JSON containing account email, prompts, local paths, or tool schemas;
- inventories containing phone numbers or private original paths;
- old manifests that enumerate excluded private filenames.

Add `README_PRIMERO.md` listing deliberate exclusions and where the non-sensitive conclusions were preserved.

## Final privacy gate

After staging is assembled:

1. Scan text-like files for email addresses, international phone patterns, WhatsApp JIDs, CLABE/SWIFT/account terms, wallet addresses, API keys, secrets, and passwords.
2. Inspect hits; dates and words such as “Secretaría” are common false positives.
3. Remove or redact the source file, not just the ZIP copy.
4. Regenerate `MANIFIESTO_SHA256.csv` after every change.
5. Rebuild the ZIP and run an archive integrity test.

The manifest must describe the final shareable package, not the pre-redaction package.

## Google Drive authorization

Read access is insufficient for synchronization. The OAuth token must include a write-capable Drive scope such as:

- `https://www.googleapis.com/auth/drive.file` for files the app creates/opens; or
- `https://www.googleapis.com/auth/drive` when the user explicitly authorizes synchronization into an existing arbitrary folder.

Use a dedicated token for broad Drive write access rather than silently widening an unrelated Workspace token. Store it outside the project directory.

Before writing:

- fetch destination metadata;
- verify it is a Drive folder;
- verify `capabilities.canAddChildren`;
- create one named root folder under the user-provided destination;
- upsert children by `(parent, name)` so retries are idempotent;
- return the created root folder ID/link and uploaded file count;
- read back or list uploaded items to verify completion.

If interactive OAuth redirects to `http://localhost:1`, that failure is expected in a headless flow: ask for the complete redirected URL and exchange it using the stored PKCE verifier/state.

## Graph and dossier packaging

When the archive also produces a knowledge graph:

- point graph provenance to a file that actually exists in the shareable staging tree;
- mark extracted, inferred, and ambiguous edges separately;
- retain the interactive HTML, graph JSON, and graph report;
- verify node, edge, and community counts before upload.

For the dossier, ship at least Markdown plus one human-friendly format (PDF or DOCX), and verify the PDF opens with a non-zero page count.
