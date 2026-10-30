# Cross-host control towers: evidence and capability boundaries

## Context and evidence limit

The Sales Academy handoff described a Mac/VPS knowledge bridge and a local dashboard showing specialists, tasks, events, results, errors, documents, and bridge state. It explicitly separated observation/registration from execution and distinguished plugin-captured delegations from native delegations with explicit evidence.

The retained conversation contains that handoff, not the underlying implementation or test output. Treat its paths, test counts, service status, and sync claims as historical assertions requiring re-verification. Do not use this reference as proof that a deployment is currently healthy.

## 1. Inventory the actual runtime

- Discover each host's profile, delegation mechanism, existing data store, service manager, and dashboard before adding components.
- Read the installed plugin/API and trace its event-writing path. Native delegation and plugin delegation may have different telemetry coverage; detect rather than assume either one lacks support.
- Reuse the existing bridge and event store when possible. A new dashboard does not justify a second scheduler or task engine.

## 2. Make capabilities explicit

| Surface | What it proves | What it does not prove |
|---|---|---|
| Specialist catalog | Roles available for selection | Persistent worker processes or active work |
| Task form | A task record was saved | A worker accepted or executed it |
| Recorded event/result | Evidence reached the store | Complete capture of every delegation |
| Bridge heartbeat | A recent transport cycle succeeded | Conflict safety or future availability |
| Matching hashes | Compared files match at that instant | Two-way sync, offline recovery, or secret exclusion |

Label task registration, dispatch, execution, and completion separately. Do not present a registration-only dashboard as an execution console. Add dispatch only when requested and backed by a tested authorized runner.

## 3. Preserve evidence provenance

Use the existing schema where available. Events should be attributable to a host, profile, task/run, timestamp, and evidence source. Distinguish automatic plugin capture, native runtime capture, and manually recorded evidence in the UI.

Show last-success timestamps and stale/offline states. Missing telemetry means unknown, not idle or successful. Only show token/cost metrics when a real source supplies them; otherwise mark them unavailable.

## 4. Verify separate gates

1. Run focused checks independently on each host; report results per host rather than projecting one result onto both.
2. Exercise one representative delegation through each active mechanism and read back its result/event.
3. Submit a harmless task through the dashboard and verify persisted data, not only a success toast.
4. Verify bridge payloads and hashes, then separately test two-way edits, conflicts, reconnect catch-up, and exclusions using the sync-preflight reference.
5. Verify the local HTTP endpoint and browser rendering, including empty/error/stale states.
6. Inspect service configuration and current process/log evidence. Installed autostart is not proof that reboot/login recovery was tested.

A workstation bridge depends on that workstation being awake, connected, and—when implemented as a user-session service—logged in. Report this availability boundary instead of implying always-on operation. A loopback URL is accessible on its host; it is not a public or automatically cross-device URL.

## 5. Handoff

Return the dashboard URL with host scope, profile invocation, observed capabilities, and the most important limitation. Separate freshly verified results from historical handoff claims. Do not mark todos complete after compaction without rechecking the underlying artifacts.

Related: `references/hermes-cross-host--installer-and-sync-preflight.md` for safe installation and bridge gates; `references/hermes-fleet--read-only-status-dashboard.md` for fleet snapshots.
