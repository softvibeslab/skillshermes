# Cache versus runtime data

A directory named `Caches` or `.cache` is not sufficient evidence that everything inside is disposable. Measure exact children, identify their owner, and separate downloaded runtime dependencies from ordinary caches. Paths below are examples to verify on the live installation, not a deletion allowlist.

## Common mixed stores

| Location or class | Candidate for scoped cleanup | Preserve or review separately |
|---|---|---|
| `~/.npm` | `_cacache`, after package activity stops | `_npx` may contain running MCP servers or CLI runtimes |
| `~/.cache/uv` | Native cache cleanup after installation/build activity stops | Project virtual environments and Python installations |
| Playwright/Puppeteer caches | Only browser versions confirmed unused | Browser executables needed by automation; removal can break agents until reinstalled |
| Hugging Face / Codex runtime caches | Individually verified unused downloads | Model weights and runtime binaries, even when under `.cache` |
| Chrome/Brave | Selected HTTP cache with owning browser closed, or browser cache-only controls | Cookies, passwords, history, extension data, local storage and automation profiles such as `.chrome-cdp` |
| Cursor Application Support | Verified `Cache`, `CachedData`, `CachedExtensionVSIXs` after closing app | `snapshots`, `User`, `WebStorage`, recovery state and conversations |
| Claude Application Support | Verified `Cache` and `Code Cache` after closing app | `vm_bundles`, VM disks, local agent sessions and extensions |
| Electron updater / `ShipIt` folders | Staged downloads after confirming owner and no update in progress | Do not infer owner from an opaque bundle ID alone |
| Telegram cache | In-app cache controls with user-selected scope | Local-only content or content whose remote copy may no longer exist |

## First-wave approval boundary

1. List exact candidate paths and measured allocated sizes, not whole parent folders.
2. State required app closures and any re-download or first-launch cost.
3. Exclude browser runtimes, models, databases, snapshots, session stores and backups by default.
4. Obtain approval for that named set before cleanup. Cache deletion is reconstructible only while the source remains available; it is not inherently reversible.
5. Measure free space afterward and smoke-test affected apps or agents. APFS accounting and files held open can reduce immediate recovery.

Use the smallest sufficient first wave. Larger optional stores remain separate decisions even if removing them would reclaim more space.

## Execution pitfalls

- `npm cache clean --force` can partially succeed before failing with `EACCES` on root-owned cache entries. Re-measure `_cacache` and report the remainder. Do not automatically follow npm's suggestion to recursively `sudo chown` the whole `.npm` tree: `_npx` may host live MCP processes, and ownership repair is a separate scope.
- A general approval to close apps for cache cleanup is not a reason to interrupt active coding agents or browser automation. If those are detected, preserve their owning applications and caches, clean the idle subset, and report the skipped space.
- Record free space immediately before deletion, separately from the initial audit and any graceful app closures. Report measured net change rather than summing deleted directory sizes; hardlinks, clones, concurrent writes and swap changes affect the result.
