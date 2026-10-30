# External-disk discovery: staged reports and evidence

Use for authorized read-only inventories of projects, sensitive-file candidates, and cryptocurrency artifacts across multiple volumes. Keep all outputs on the host and store paths and finding labels, not matched secrets.

## Avoid the archive bottleneck

A metadata inventory can finish while archive listing still has tens of thousands of items pending. A serial scan → content analysis → archive listing → renderer chain hides useful results until the slowest stage finishes.

1. Inventory accessible paths and record per-volume errors and completed-directory checkpoints.
2. Render an initial offline dashboard immediately after inventory; label it preliminary.
3. Inspect eligible content with explicit byte limits. List archive member names separately, with per-archive time/member limits and no extraction or execution.
4. Refresh the report at stage boundaries. Keep complete, partial, skipped, failed, and pending coverage distinguishable.
5. Run final dashboard checks only after the corresponding render succeeds. Do not present preliminary output as fully verified.

Expose metadata counts, inspected-content counts, archive progress, exclusions, and errors separately. Archive member-name discovery does not imply content inspection. A directory exclusion or bounded read means the analysis is not exhaustive, even when metadata traversal is complete.

## Crypto findings: evidence levels

- Filename or keyword: candidate only. Android Wallet SDKs, package examples, and generic `mnemonic` identifiers are common unrelated matches.
- Address reference: validate using the address format's rules. For legacy Bitcoin Base58Check, decode Base58 preserving leading zero bytes, check the expected payload/version, and compare the final four bytes with double-SHA256 of the payload. This does not validate Bech32 addresses or other networks.
- Wallet/signing container: classify by filename plus format signature where available. Java KeyStores and KeePass databases are credential artifacts, not automatically cryptocurrency wallets.
- Never infer balance, ownership, or recoverability from any of the above. Do not print seeds, private keys, credential values, or document excerpts in logs or tests.

When rules improve, recompute affected persisted findings before rendering. Keep rejected matches out of active totals, optionally under a labeled discarded section. If rereading fails, mark the finding unverified and record the error; do not silently confirm or discard it. Use public test vectors and synthetic invalid inputs for one runnable detector check, never private disk contents.

## Progress and delivery verification

For a status request, inspect both the tracked process and the current stage's latest log. Report the observed stage and counter, not an assumed overall percentage. A process can be running while the HTML does not yet exist; a generated HTML can exist without passing UI tests.

Use tracked background execution with completion notification for bounded scans. Verify report existence, generation success, per-volume counts, search/category/volume filters, absence of console errors and external network requests, and mobile overflow. State pending or unsupported coverage in the dashboard itself.
