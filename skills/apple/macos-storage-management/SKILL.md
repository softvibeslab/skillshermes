---
name: macos-storage-management
description: Audit macOS disk usage and design safe, evidence-based cleanup plans without deleting important data. Use for low-disk-space incidents, APFS accounting confusion, oversized app containers, developer caches, local AI models, Docker/VM storage, and requests to reclaim space safely.
version: 1.0.0
platforms: [macos]
metadata:
  hermes:
    tags: [macos, storage, apfs, cleanup, disk-space]
    category: apple
---

# macOS Storage Management

Audit first, distinguish physical allocation from logical size, and classify every candidate by reversibility before deleting anything. The goal is durable free space without damaging application databases, source code, credentials, virtual machines, or synced files.

## 1. Establish the real pressure

Collect the filesystem and APFS baseline before inspecting folders:

```sh
sw_vers
df -h
diskutil info /
tmutil listlocalsnapshots /
diskutil apfs listSnapshots /
```

Report container capacity and free space from `diskutil`, plus the Data volume's usage from `df`. APFS system and Data volumes share one container; do not add their reported sizes.

Check virtual memory separately:

```sh
sysctl vm.swapusage
uptime
```

Large swap is temporary pressure, not user data. Recommend closing heavy applications or rebooting; never delete `/System/Volumes/VM` manually. Treat swap recovery as temporary rather than durable savings.

## 2. Measure without lying about APFS

Use allocated-size measurements for cleanup estimates and apparent size only to diagnose sparse files:

```sh
du -x -k -d 1 "$HOME" 2>/dev/null | sort -nr
du -h /path/to/file
du -Ah /path/to/file
ls -lskh /path/to/file
```

Important accounting caveats:

- Sparse VM/container images can appear hundreds of GB logically while using far less physical storage.
- APFS clones, hard links, snapshots, and File Provider data can make directory totals non-additive or larger than disk capacity.
- Deleting one cloned duplicate may reclaim less than its displayed size.
- Never promise an exact recovered amount before rechecking `df` after cleanup.

## 3. Drill into the largest classes

Inspect the largest home folders, then only their largest children. Common classes:

- `~/Library/Group Containers` and `~/Library/Containers`
- `~/Library/Caches`, `~/Library/Application Support`, `~/Library/CloudStorage`
- `~/Downloads`, `~/Desktop`, `~/Documents`
- Docker/Colima/Parallels data
- package caches: npm, pip, Homebrew, Gradle, uv, pnpm
- local-model stores: Ollama, LM Studio, ComfyUI, Hugging Face
- generated development directories: `node_modules`, `target`, `build`, `.next`, `.venv`, `DerivedData`

Do not scan deeply everywhere by default. Start broad, then drill into the few dominant branches. `du -d 1` limits displayed depth, not traversal work: avoid concurrently scanning a parent and its children. For long scans, use a tracked background job with completion notification, then drill down after it finishes. Capture permission errors separately or count them; unreadable folders are unknown, not empty, and the report must disclose partial coverage without requesting broader permissions automatically.

## 4. Classify candidates before cleanup

### Safe or reconstructible

Examples: application caches, package-manager caches, downloaded installers, verified duplicate downloads, compiler targets, build output, dependency directories with valid lockfiles.

A cache-named parent is not a deletion allowlist: it can hold browser executables, model weights, or live CLI/MCP runtimes. Classify exact children and exclude runtime dependencies from the first wave. See `references/cache-versus-runtime-data.md` for npm, uv, Playwright/Puppeteer, browser, Cursor, Claude, and updater boundaries.

Prefer native cleanup commands (`brew cleanup`, `pip cache purge`, `npm cache clean --force`, `cargo clean`) when they only remove cache or generated output. Before cleaning a development project, record `git status`, confirm no build/package process is active, and identify its lockfile or rebuild command. Do not run framework tasks such as Gradle `clean` blindly: configuration can resolve dependencies, install SDK/NDK components, or fail before removing output. When a directory is unambiguously generated and ignored, removing that directory directly is safer and smaller than invoking a mutating build. Close the owning application first.

### App-managed or review-required

Examples: WhatsApp/Telegram media, Docker images and volumes, Android emulators, cloud-provider storage, virtual machines, browser profiles, local AI models.

Use the owning app's storage manager or CLI. Never delete an app container, chat database, Docker volume, `.pvm`, or cloud-storage folder merely because it is large.

### Preserve by default

Source repositories, `.git`, credentials, Hermes profiles/memory, browser profile databases, app `Application Support`, photo libraries, backups, and macOS update snapshots.

### Failed or runaway backups

A failed backup is not automatically safe to delete: identify its exact destination from the execution log, confirm its writers stopped, and obtain approval for that directory alone. Preserve source data, historical backups, and staged installations. Inspect symlinks before retrying; a profile's `home` link may expand the copy into the whole user home. Process substring matches require interpretation (`rsync` also matches macOS ColorSync services). Verify deletion and measure free space afterward; do not promise recovery equal to `du` size. See `references/failed-backup-recovery.md` for the scoped cleanup and safe retry procedure.

## 5. Verify duplicates correctly

Matching filenames and sizes are only candidates. Verify content before recommending deletion:

```sh
cmp -s /path/a /path/b && echo IDENTICAL
```

Keep the copy used by the application. Downloads are usually safer to remove than installed model paths. If two applications reference separate model roots, consolidate only after confirming or updating both configurations.

## 6. Handle dominant storage safely

- **Chat media:** delete through the app's storage manager so conversations and databases remain consistent. For large cloud-first backups before deletion, follow `references/chat-media-cloud-backup.md` (chunked TARs, resumable upload, remote checksum gate, and resumable manifest).
- **Docker:** inspect the current context first, then run `docker system df -v` if its daemon is already available. In a read-only audit, do not start a stopped daemon without approval: containers with restart policies may start too. Report allocated disk size and mark reclaimable contents unknown until runtime inspection is authorized. Remove only confirmed-unused images/build cache; do not include volumes without explicit approval.
- **Colima:** treat its VM disk as a separate runtime; remove the environment only when confirmed unused.
- **Parallels:** use the product's reclaim/compact function; never remove the `.pvm` directly.
- **Cloud/File Provider paths:** verify remote copies and use “Remove Download”, disconnect, or the provider's cache control.
- **Local AI models:** list models through each runtime and protect models referenced by active agents or projects.
- **Developer artifacts:** report project path and rebuild command; generated does not mean currently disposable.

## Read-only external-disk discovery dashboards

For an explicitly requested whole-disk project/credential/wallet inventory:

- Confirm mounted data volumes and read-only status. Keep reports on the host, not the source disk; do not mount recovery/EFI partitions or attempt deleted-file recovery without a separate request.
- Inventory all accessible paths without following symlinks. Separate complete metadata traversal from bounded content inspection, archive-name listing, and unsupported/encrypted formats. Record errors as unknown coverage, not empty folders.
- For million-entry SQLite inventories, enable WAL and a busy timeout before scanning. Concurrent progress queries in rollback-journal mode can block writer commits and abort the scan. Persist completed-directory checkpoints together with the associated entries; test interrupted-directory resumption before relying on it.
- Detect secrets locally and store labels and paths only, never matched values, seed phrases, document excerpts, or private key bodies. Protect the output directory and use a self-contained offline HTML dashboard with no external assets or network requests.
- List archive members without extracting or executing them. Bound runtime/member count, retain already received names on timeout, and label partial listings. Listings do not constitute content inspection; nested archives and ciphertext remain unknown.
- Distinguish personal wallet candidates from Android/Google Wallet SDK resources, library examples, public certificates, and debug keystores. Never infer balances or recoverability from a filename. Preserve production signing keystores and credential databases, without opening or rotating them automatically.
- Verify both volume coverage and dashboard search/category/volume filters, mobile overflow, console errors, and absence of network requests. State full inventory counts separately from inspected-content counts.
- Publish a clearly labeled preliminary dashboard after metadata traversal; do not make the first useful report wait behind tens of thousands of archive listings. Refresh it at stage boundaries and mark pending work and coverage explicitly.
- Validate cryptocurrency candidates with format-specific checks rather than regex alone. A valid address is only an address reference, not proof of wallet ownership, private keys, recoverability, or funds. Revalidate persisted findings when detection rules change so obsolete matches do not survive into the report.
- For progress questions, check the tracked process and the latest stage log. Distinguish running, completed, generated, and verified; a queued renderer is not an existing dashboard. Use completion notifications for bounded background scans and avoid inferring an ETA from file counts alone.

See `references/external-disk-discovery.md` for staged delivery, safe crypto classification, and report verification.

## 7. Report in action order

Return:

1. Capacity, actual free space, and severity.
2. Largest physical consumers, with sparse/logical caveats.
3. A conservative first wave: reversible and low-risk.
4. App-managed high-impact options requiring user selection.
5. Explicit “do not touch” paths.
6. Temporary savings versus durable savings.
7. A range, not a guaranteed total, followed by a `df` verification step.

Do not delete during an audit unless the user explicitly authorizes a named cleanup phase. A useful phase boundary is: caches and verified duplicates first; app databases, models, containers, emulators, and VMs only after review.

## Verification

After any cleanup:

```sh
df -h /
diskutil info /
```

Open affected applications and verify projects, chats, containers, model runtimes, and synced files still work. If space did not increase as predicted, investigate APFS clones, sparse files, snapshots, or delayed File Provider reclamation rather than deleting more blindly.

## Reference

See `references/apfs-storage-audit.md` for a compact read-only probe set, interpretation rules, and cleanup safety matrix.

## Pitfalls

- Adding APFS volume sizes as though they were separate disks.
- Reporting apparent size as reclaimable physical space.
- Counting swap as durable cleanup.
- Deleting app containers instead of using in-app storage controls.
- Running Docker prune with volumes included by default.
- Deleting all local models without checking active agent dependencies.
- Treating every `build`, `.venv`, or `node_modules` folder as disposable without a rebuild path.
- Summing overlapping directory totals into a false savings promise.
