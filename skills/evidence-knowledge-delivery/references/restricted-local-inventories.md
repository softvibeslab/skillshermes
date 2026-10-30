# Restricted local inventories for identity graphs

Use for local-only personal/work portfolios with an explicit allowlist, denylist, and evidence requirement. No network, service authentication checks, or external identity enrichment unless separately authorized.

## Scope before content

- Model authorization as roots plus content classes: an allowed repository does not authorize every file underneath it. First-level README/client evidence is not permission to inspect lead CSVs or people directories.
- Discover filenames first. Prune denied directories before descent; never open denied files to classify them. Do not follow symlinks or search indexes spanning unauthorized roots.
- Apply deny patterns to path components as specified by the user. Record omitted paths without contents; distinguish denied from merely uninspected.
- Maintain an in-memory ledger of each content read and its purpose; include it in the authorized report if needed. No auxiliary files when only the report is writable. Exclude the report itself from evidence discovery to prevent recursive self-citation.
- Operational skill reads are not subject evidence, but remain reads for a whole-session scope test. Disclose exceptions; do not silently redefine zero out-of-scope files as zero evidence files.
- When XLSX is explicitly mentioned but binaries are broadly forbidden, declare the ambiguity and leave it uninspected pending permission. Do not silently mark the inventory complete or generalize this into a permanent XLSX prohibition.

## Minimize before exposing

- Sanitize extracted snippets before returning tool output. Never first print raw matches and redact only the final report.
- Mask the requested portion of email local parts; omit third-party personal identifiers and records rather than merely masking a bulk people list.
- If allowed Markdown contains apparent credentials, omit the entire value and emit only `SECRETO_EN_DOC:<path>` plus a safe description.
- MCP inventories expose server names and explicitly declared tool names, not env values, command arguments, or credential-bearing URLs. Config presence does not prove a connection works; absent tool declarations are `NO ENCONTRADO`, not a reason to execute the server.
- Restrict agent documents to frontmatter/titles when requested. Never expand to full agent prompts just because they are Markdown.

## Evidence and synthesis

For each claim retain path, line range where available, minimal sanitized excerpt, and confidence. Existence of a path proves presence, not ownership, authorship, deployment, or active use. Names supplied by the operator or persistent memory are search candidates, not disk evidence.

Keep identity merges proposed only. Preserve both source excerpts for contradictions; distinguish incompatible assertions from plausible historical changes or different contexts. Use `NO ENCONTRADO` for missing evidence and state search coverage.

Separate a readable synthesis from complete path inventories within the same authorized report. Avoid megabytes of repeated metadata or full source text; group repeated findings without dropping paths the user explicitly requested. Count files separately from projects with a README.

## Acceptance checks after the final edit

1. Confirm required report sections and note-count limits.
2. Check cited paths and line ranges, then verify the cited text actually supports each material claim. Valid line numbers alone are not semantic validation.
3. Compare project counts with distinct parent project folders, not README file counts.
4. Scan the final output for unmasked emails, credential-bearing URLs, private-key headers and common token patterns. Emit counts/locations, never matched secret values.
5. Reconcile the read ledger with scope; report evidence and operational exceptions separately. If there is no complete ledger, report the scope claim as unverified instead of PASS.
6. Confirm no denied file was opened. A recorded `.env` path is not evidence of reading its values.
7. Deliver the exact report path, verified coverage, and caveats. Say 'zero detected matches' rather than claiming proof of zero secrets.
