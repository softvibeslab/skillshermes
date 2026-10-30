# Local macOS monitoring and process-control dashboards

Design guidance, not a previously tested application. No dashboard implementation was completed in the originating session.

## Measure without becoming the workload

- Inspect existing project helpers and available dependencies first. A small Python stdlib HTTP server plus native macOS commands is an option, not a permanent ban on psutil.
- Collect snapshots on a bounded cadence and cache them across clients. Do not spawn a fresh expensive system scan for every browser request. Refresh service discovery less often than process metrics.
- Use native global CPU measurements rather than adding process CPU percentages. Label process CPU accounting and sample interval.
- Distinguish physical RAM, compressed memory, swap occupancy, and current memory pressure. Sum RSS only as an explicitly approximate grouping metric.
- Read process identity and executable names without full command arguments or environment variables, which may contain credentials.
- Mark missing metrics unavailable; never substitute zeros. Bound chart history and show snapshot age and collection errors.

## Controls need stronger boundaries than read-only metrics

- Bind to loopback, validate Host and Origin, reject cross-origin writes, require a random CSRF token in a custom header, and cap request bodies. Localhost alone is not protection against browser-origin attacks.
- Allow only recognized, user-owned process targets. Protect critical system processes, the dashboard and its ancestors, terminal sessions, agents, and active infrastructure by default. Unknown targets remain read-only. User-added protections cannot remove baseline safeguards.
- Re-read UID, executable and start time immediately before signaling. Reject stale or reused PIDs. This narrows but does not eliminate the read-to-signal race; never promise absolute race freedom.
- Explain semantics before confirmation: SIGSTOP pauses but does not release RAM; SIGCONT resumes; SIGTERM requests exit and may lose unsaved work. Avoid force-kill as the default. A process action is not necessarily an application-wide action.
- Separate requested action from observed outcome. Verify stopped/resumed/exited state with bounded checks; report pending or uncertain results honestly.
- A launchd-managed process can respawn. Discover service identity rather than inventing labels. Restrict service mutations to verified user LaunchAgents and exact plist paths; do not act on system domains or disable services persistently by default. Reject symlinks and label/path mismatches.
- Never execute arbitrary shell text received from the browser. Render dynamic UI text safely rather than interpolating it into HTML.

## Advisory AI is separate from control

- Offer deterministic recommendations immediately and label them rules, not AI.
- Invoke a local model only on explicit request. Inference itself consumes CPU and memory; discover available models before selecting a small one and use bounded context/output and timeouts.
- Send sanitized aggregate metrics and application names, not command lines, paths, secrets or raw logs. Let the user identify activities that must stay uninterrupted.
- Model output remains advisory. It cannot invoke signals, launchctl, shell commands, or automatic optimization actions. Report model failures instead of inventing an analysis.

## Verification and delivery

- Test protection rules, stale identities, request validation, parsing and denied actions with stdlib tests or the project's existing test tools.
- Test actual signaling only on disposable child processes created for testing, not the user's running workload. Keep test allowances out of production authorization.
- Verify collector overhead, live API responses, and UI behavior before claiming delivery.
- Distinguish built, tested, started and reachable. If execution authorization prevents work, report the exact uncompleted stage; do not claim files or a running server exist.
- Do not promise optimization with zero disruption. State what is protected, what remains uncertain and which actions require confirmation.
