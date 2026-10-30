# Local process monitoring and safe controls

Use when a CPU/background-process investigation becomes a request for a local dashboard. Keep observation, process control, service management, and AI advice separate capabilities.

## Discover and reuse

Inspect an existing dashboard before building another. Discover macOS version, Python runtime, available native commands, and any local inference endpoint/models. A stdlib HTTP server plus static HTML/CSS/JS can suffice; do not install a monitoring dependency solely to read native command output. Python version compatibility must be checked rather than assumed.

## Metric semantics

- Use native `ps` for process inventory and `top`, `vm_stat`, `sysctl`, and filesystem statistics as available for aggregate measurements. Parse the actual output format on the host.
- Process CPU percentages can exceed 100% because multiple cores are used; do not equate their sum to a normalized system utilization percentage.
- A single `top` snapshot is a snapshot, not proof of sustained load. Validate sampling intervals and compare repeated samples with Activity Monitor before claiming precision.
- Distinguish resident memory, compressed memory, swap allocation, swap activity, and available disk space. Swap allocated alone does not prove current thrashing; do not sum RSS as unique physical memory.
- Parse `vm_stat` page size rather than assuming 4096 bytes. Show units, sample time, and stale/error state; collection failures must not appear as zero utilization.
- Start with a modest polling interval (for example five seconds), prevent overlapping collectors, bound subprocess execution, and measure the monitor's own overhead.

## Profile and agent attribution

A useful extension from the MacPulse work was a profile/agent pulse with process drill-down, rather than another flat process table. Reuse the existing collector and dashboard; do not introduce a separate monitoring service just for grouping.

- Keep configured-profile inventory separate from observed running groups. A profile existing on disk does not mean its agent is running; an unobserved profile is not proven stopped if collection failed.
- Attribute processes only using inspected runtime evidence. Record the attribution source internally; do not guess from a generic Python process name. Parent-child relationships can support attribution, but do not assign a shared service wholesale to one profile without evidence.
- Retain “Sin atribuir” for insufficient evidence. Prefer uncertainty over an attractive but incorrect breakdown.
- Assign each process to at most one group within a snapshot. Sum CPU using the collector's stated semantics and show resident RAM as approximate RSS, not unique physical memory. Keep PID and process-start identity together across refreshes.
- Expand each group into its contributing processes: PID, observed state, process age, and cumulative CPU time. CPU time is not elapsed age or instantaneous CPU utilization.
- Bound pulse history and label sampling/staleness. A missing sample must not silently become a zero-load measurement.
- Support name/PID search, state/type filters, and ascending/descending sorting by CPU, RAM, name, or process count. Make clear whether search retains the matching group or filters its child rows, so visible totals remain interpretable.
- Publish only the minimum identifying fields. Do not expose raw environments, credentials, or full command lines in the browser/API to explain an attribution.
- Tokens, costs, and GPU metrics require independent instrumentation. CPU/RAM readings cannot supply them.

Verification: leave a runnable check for grouped totals without duplicate PIDs, ambiguous attribution, empty/error samples, and PID reuse. Verify actual UI search/filter/sort behavior and process drill-down against a live sample. Report configured-profile and observed-group counts as distinct observations, not fixed expectations. Restart only the monitoring server when necessary; do not restart the monitored agents to refresh the dashboard.

## Safe local control boundary

Bind only to loopback. Validate Host and Origin and require a per-session CSRF token for state-changing POST requests. Reject invalid bodies, unknown actions, and arbitrary commands. Loopback alone does not protect a control API from malicious web pages.

Expose a small allowlist of signals: pause (SIGSTOP), resume (SIGCONT), graceful termination (SIGTERM). No default SIGKILL. Explain that SIGTERM does not guarantee saved work and SIGSTOP can hold locks or interrupt ongoing activity.

Before each signal, independently re-read ownership, executable, and process identity (including start time where available). Reject changed identity: the same PID and executable can belong to a different process after PID reuse. A check followed by signaling still has a race; do not claim atomic safety from a path comparison.

Default to read-only. Allow controls only for explicitly eligible user-owned applications; `/Applications/` is a scope filter, not proof that termination is safe. Protect system processes, Finder, the dashboard server, the active agent/runtime, terminals, and browsers hosting the control UI. Enforce protection on the backend, not just disabled buttons. Never offer browser pause and then rely on a warning to preserve access to Resume.

Keep process and service semantics distinct: resuming a paused process is not restarting a terminated application. A launchd-managed process may immediately respawn. List services read-only unless explicit service management is requested; service controls require domain/label discovery, separate authorization, and a restoration route.

## Resource-aware local AI

Make inference opt-in and advisory. Discover installed models rather than installing or hardcoding one; prefer an appropriate small available model. Send only the necessary process names and aggregate metrics, not environment variables, full command arguments, or full paths. Treat process names as untrusted data, not prompt instructions.

Bound inference time and concurrency, expose loading/errors, and warn that local inference itself uses RAM and CPU. Rules-based observations should remain available without AI. Never execute model suggestions automatically or promise optimization without affecting activities.

## Verification gates

1. Verify live metrics, freshness, parsing failures, and absence of overlapping sampling.
2. Test protected targets, wrong owner, unknown action, stale identity, invalid Origin/Host, and missing token without signaling real user applications.
3. Test pause/resume/termination only on an explicitly disposable fixture; record whether control was mocked or exercised live.
4. Check the UI remains usable and reflects backend denials and errors.
5. Run an actual bounded inference before calling AI verified; an available endpoint or button proves integration only.
6. Deliver the local URL, absolute project path, startup/lifetime instructions, and separate verified features from untested ones. Do not install auto-start unless requested.

## Reference implementation context

MacPulse was implemented as a local stdlib Python server and static HTML/CSS/JS, with safety tests and an on-demand Ollama adapter. Its service inventory was read-only. UI and metric verification did not by itself verify inference. Reuse this separation of capability and verification; do not preserve transient ports, PIDs, tokens, model inventories, or resource readings as defaults.
