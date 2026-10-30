# Small Full-Stack Repository Production Audit

Use this when a repository is small enough to read end to end. LOC alone is not an analysis; trace the browser → API → external service flow and verify the claims in the README.

## Fast workflow

1. Clone the exact default-branch revision and record the SHA, commit count, authors, tags, and last code push. Do not confuse GitHub's `updated_at` with source activity.
2. Inventory every source file, manifest, lockfile, CI file, test, environment template, container file, and deployment artifact.
3. Read all source when practical. Map entry points, endpoints, state ownership, persistence, external calls, and trust boundaries.
4. Compare direct imports with declared dependencies. Flag direct imports that are only available transitively and dependencies never referenced by application code.
5. Run the smallest safe checks available: syntax compile, lint, production build, dependency audit, and a language-appropriate static security scanner.
6. Test README setup claims against current supported runtimes. If installation fails on a newer runtime, retry with the project's likely supported LTS version or a non-mutating compatibility check; report the compatibility boundary, not merely the local failure.
7. Rank findings by production impact, then recommend deletion before upgrades or new abstractions.

## High-value checks

### Browser/UI

- Treat `v-html`, `innerHTML`, Markdown renderers, syntax highlighters, and model-generated text as trust boundaries. Verify sanitization with a harmless HTML payload; do not assume the Markdown library sanitizes.
- Check whether generated diff HTML escapes original and model-produced code before interpolation.
- Look for stale-response races in debounced autocomplete: request cancellation, sequence IDs, or response-version checks.
- Detect hardcoded API origins, absent loading/error states, whole-file replacement, and inaccessible controls.
- Compare editor libraries configured in the build with the editor actually imported by the UI. Unused editor plugins can dominate bundle size.

### API/backend

- Global mutable chat/code histories are single-user demo state. In a server they cause cross-user leakage, reset collisions, worker inconsistency, and races.
- Synchronous HTTP clients inside `async def` block the event loop. Either make the endpoint synchronous or use a shared async client.
- For outbound HTTP, check TLS verification, explicit timeouts, bounded retries, response validation, and error propagation.
- Binding to all interfaces without authentication/rate limits is a deployment risk, especially when endpoints consume GPU inference.
- Bare `except:` around input offsets hides malformed requests; validate ranges at the request boundary.

### Dependencies and builds

- Prefer removing unused vulnerable dependencies over upgrading them.
- Separate the web/API service dependencies from an independently operated inference server; do not force every API install to pull the GPU runtime.
- Lock or constrain versions and keep README runtime requirements consistent with package metadata.
- A build that passes only with an engine override is evidence of a runtime-support boundary, not a clean pass.
- Report bundle warnings when unused plugins generate large workers or assets.

## Minimum evidence in the report

- Exact SHA and real source activity
- Source-file and line counts
- Architecture/data-flow summary
- Build/lint/syntax results
- Dependency-audit totals and static-security findings
- Tests/CI/deployment/configuration gaps
- Prioritized: security → correctness → simplification → reliability
- Clear verdict: demo, internal tool, or production-ready
