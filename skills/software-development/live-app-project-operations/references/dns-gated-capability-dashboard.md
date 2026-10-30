# DNS-gated capability dashboards on an existing VPS

## Trigger
A user wants to evaluate multiple repositories through a central dashboard, integrate them with agent/IDE runtimes, and publish via a domain whose DNS may be managed separately from the VPS.

## Discover before deploying
1. Deduplicate repository URLs; record exact commits and whether each entry is a new clone or an existing checkout. Do not update an operational checkout merely to populate a catalogue.
2. Read existing registry, project instructions and integration docs; reuse identities rather than inventing a parallel registry.
3. Identify configured SSH access from documented context. Use BatchMode and host verification for read-only probes; do not mine ambient credentials.
4. Probe actual remote resources, occupied ports, proxy vhosts and service management. Local Docker availability says nothing about remote Docker.
5. Query authoritative DNS including A and AAAA. A hosting-account listing is not a DNS-zone listing. Recheck available DNS tooling each time; do not encode a historical lack of access as a permanent limitation.

## Honest capability model
Keep separate fields for source availability, static audit, sandbox installation, runtime tests and integration evidence. Synthetic examples are neither functional tests nor A/B results.

A one-pilot selection screen can be useful staging, but label its button “Seleccionar piloto,” explain that it only stores a preference, and retain the requested execution controls as unfinished scope. A remote dashboard does not control a Mac's Hermes/Cursor runtime without an explicit authenticated bridge. Never infer activation from a selected state or an HTTP 200.

## Minimal protected staging
- Backend bound only to 127.0.0.1 on a verified free port.
- Dedicated unprivileged systemd user; code read-only under a distinct application directory and writable SQLite state outside the web root.
- Restart policy, restrictive umask, NoNewPrivileges, PrivateTmp, ProtectSystem/ProtectHome, narrow ReadWritePaths and appropriate resource caps.
- Exact static route allowlist; never derive filesystem paths or shell commands from browser input.
- For selection: allowlisted IDs, parameterized SQL, singleton state, bounded JSON bodies, exact Host/Origin checks and CSRF token. CSRF is not authentication.
- While TLS/auth is pending, the new HTTP vhost serves only the ACME challenge directory and returns 503 for application paths. No public backend port and no credentials over HTTP.
- Test nginx config before reload. Roll back only the newly introduced enabled vhost on failure; preserve other configurations and classify existing warnings separately.

## Finish publication
1. Create only the authorized DNS record; preserve unrelated records and resolve conflicting A/AAAA routes deliberately.
2. Verify propagation to the intended host, then issue the certificate through an ACME webroot supported by the existing server/account.
3. Add HTTPS plus an authentication boundary for all app routes, APIs, assets and health. Keep credential hashes outside web roots; deliver new credentials through a protected channel/file, not logs or source code.
4. Proxy to loopback while preserving the validated Host. Redirect plaintext app requests to HTTPS; retain the challenge route.
5. Validate config, reload and verify the public URL with normal certificate validation.

## Evidence checklist
- Unit checks: invalid ID/body, origin/token rejection, path allowlist, singleton replacement and persistence after restart.
- Remote checks: service active, correct loopback listener, health response and expected catalogue contents.
- Before publication: public app route closed; no accidental alternate public route to backend.
- After publication: trusted HTTPS, unauthenticated 401/403 for UI/API/assets, authenticated 200, malicious Origin rejected, and browser selection surviving reload.
- Review actual UI rendering and console errors; do not describe Node syntax checks or HTTP probes as browser tests.
- Record current paths, service/vhost names, verification results and blockers in the project's deployment document, not durable memory.

## Interrupted verification and handoff

Keep a small evidence ledger in the project deployment document: check, method, observed result, and pending reason. Separate certificate/auth HTTP probes, redirect checks, remote service/timer checks, and real browser rendering/persistence tests.

If a combined shell command is denied, none of its checks produced fresh evidence. Do not relabel that denial as a failed or pending browser run, and do not route around it with equivalent tools. Report earlier checks only if their results are available; if only an earlier assistant summary survives compaction, label those claims as previously reported and not reverified. Resume blocked checks only after renewed authorization.

A deployment handoff should state the URL, verified access boundary, safe credential-file location (not its contents), exact pending checks, and whether controls merely select a pilot or genuinely activate services. A published catalogue is not completion of a requested repository-to-Hermes/Cursor integration.

## Delegation recovery
A timeout can leave complete or partial files. Inspect the output directory, read the implementation and run checks yourself before redelegating. Do not trust absent/self-reported summaries or overwrite existing artifacts. Publication must still be verified independently.

## Rollback and report
Stop/disable only the new service, remove only its enabled vhost, test config and reload. Preserve state unless deletion is explicitly authorized. Report built, staged, publicly reachable, authenticated, and actually integrated as distinct milestones; identify the exact external prerequisite without claiming the full task complete.
