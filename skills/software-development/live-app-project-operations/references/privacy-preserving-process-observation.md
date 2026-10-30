# Privacy-preserving process and memory observation

Use when extending an existing operations dashboard with read-only Linux process telemetry. This is an observation feature, not a process-management console.

## Integration contract

1. Read the current server, UI, inventory collector, and README before editing. Preserve existing API keys/routes, authentication, polling and visual conventions. Inspect dirty state before changes when tools permit.
2. Honor local-only and parent-owned deployment boundaries: no SSH, uploads, remote probes, service restarts or privilege changes. Use synthetic /proc fixtures for local development on another OS.
3. Prefer a small stdlib module and one additive snapshot field. Reuse the existing slow-sampling cache (e.g. 30 seconds), not the browser refresh interval or one scan per HTTP request. Test the exact refresh boundary (`>= interval`). Include sample timestamp, availability and partial-read counts.
4. In the handoff, list exact changed files, the newly imported module required at deployment, runnable checks and evidence limits. A simulated DOM check is not browser QA; fixtures do not verify production /proc visibility.

## Minimal safe payload

- Per process: numeric PID, PPID, safe display name, group, RSS bytes, swap bytes or null, age seconds, recognized service, opaque cgroup identifier, profile and attribution evidence/kind.
- Groups such as Hermes, Chrome, Node and Others: process count, RSS sum, known swap sum and unknown-swap count. Classify only from recognized executable/name/script positions; arbitrary argument substrings are not classification evidence.
- Do not publish raw argv, environment, errors including file paths, or cgroup paths. Bound reads. Process `comm`/names can themselves contain sensitive text: use recognized display labels and a generic fallback rather than assuming truncation or HTML escaping provides privacy. Check legacy process views too when they could bypass the new sanitization boundary.
- Match profile/service labels against an established public inventory; lexical validity alone does not establish that a token is safe to publish. Never echo arbitrary unknown profile values. Do not silently scrape profile directories or relax service isolation to fill missing labels.
- A digest may provide an opaque equality label for cgroup paths, but is not authentication, proof of ownership, or strong anonymization against guesses. Do not retain raw paths in the response.

## Attribution and interpretation

Extract only HERMES_HOME or explicit --profile arguments for direct profile evidence. HERMES_HOME may identify a conventional default/named profile; custom or unrecognized roots remain unknown unless an authorized mapping exists. Multiple conflicting or unrecognized candidates are unresolved; do not quietly select one or replace conflict with ancestor attribution. Treat option terminators and malformed/missing flag values deliberately rather than scanning arbitrary text as flags.

An ancestor's direct evidence can support a separately marked inference. Walk PPIDs with a visited set, reject parents starting after children and stop at contradictory evidence. Never infer profile ownership from a similar process name or cgroup alone. An inherited environment variable is observed evidence, not proof of current workload or exclusive ownership.

Explain in the UI:
- RSS may double-count shared pages; its sum is not unique host memory or systemd MemoryCurrent.
- VmSwap excludes some shared-memory swap and missing values are not zero.
- Counts are processes, not agents, sessions or gateways.
- Old, idle-looking or duplicate-looking processes are not thereby safe to stop.

Provide only a human-review checklist: owner/evidence, repeated samples, active work/dependencies, pending data and recovery, explicit authorization outside the dashboard. No kill/restart controls or automatic safe-to-stop recommendations.

## /proc parsing and race handling

- `/proc/PID/stat`: locate the opening `(` and final `)` because comm can contain spaces and parentheses. In the remaining fields (starting with state), PPID is index 1, starttime 19, RSS pages 21.
- Convert RSS pages with SC_PAGE_SIZE; age uses `/proc/uptime - starttime/SC_CLK_TCK`.
- Parse only desired status keys, validate kB and multiply by 1024. A missing status file can fall back to stat RSS while swap remains null.
- Re-read stat after optional files and reject rows whose starttime or parent changed or which vanished. This narrows PID-reuse races; it does not make /proc a transactional snapshot.
- Accept cgroup v1/v2 lines with a bounded split on the first two colons; compare individual path components with known units without exposing the full path.
- Distinguish an unavailable /proc root from a genuinely empty observed list. Permission failures and process exits are expected; return sanitized partial state, not exception strings.

## Runnable verification pattern

One unittest file can use TemporaryDirectory for uptime and numeric PID directories, injecting page size and tick frequency. Include:
1. stat with spaces/parentheses; valid, missing and malformed status metrics.
2. both --profile forms, HERMES_HOME, unknown/custom roots and conflicts.
3. direct parent, multilevel descendants, cycles, newer parents, and no cgroup-only attribution.
4. group count/RSS/swap totals and unknown-swap accounting.
5. mocked PermissionError and disappearance between reads; mock access errors rather than chmod, which privileged runners can bypass.
6. credential sentinels in name, argv, environment, paths and exception messages; assert absence from the entire serialized payload.
7. cache reuse before the interval and refresh exactly at the interval; existing API fields remain.

Also compile Python, syntax-check inline JavaScript, check duplicate HTML IDs, and exercise unavailable/partial/escaped rendering in a small DOM stub if appropriate. Label that test accurately and leave actual browser/remote checks to the authorized deployment owner.

## Source-session anchor

Applied to the local VPS dashboard at `Documents/SoftvibesLab/vpsvibes-dashboard`: app.py and index.html were extended with memory_observer.py and a runnable test_memory_observer.py; README.md and profile-inventory.py were read without edits. Eight unittest cases plus Python compilation and synthetic JavaScript checks passed in that session. This is historical workflow evidence, not a claim about current files or production deployment.
