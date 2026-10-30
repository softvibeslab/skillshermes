# Safely exposing a local agent dashboard

Use this pattern when a local dashboard can invoke AI CLIs, read/write project files, or expose memory and has no application authentication.

## Minimal implementation

1. Inspect the real backend before publishing. Treat chat, skill execution, settings, backups, session replay, webhooks, and file editors as privileged endpoints.
2. Keep the app bound to `127.0.0.1`; do not change it to `0.0.0.0` merely to obtain a public URL.
3. Reuse an authenticated tunnel already installed. For a temporary review URL, ngrok Basic Auth is enough:

```bash
ngrok http 8080 --basic-auth 'user:strong-random-password' --log stdout --log-format json
```

4. Read the assigned URL from `http://127.0.0.1:4040/api/tunnels` rather than scraping terminal formatting.
5. Verify both sides of the boundary:
   - request without credentials returns `401`;
   - authenticated root returns `200` and expected app content;
   - authenticated health/status endpoint returns the expected live state.
6. Label the URL temporary: it depends on the local app, tunnel process, network, and host staying awake.

Basic Auth protects access but does not make an unsafe backend production-ready. A durable deployment still needs identity/authorization, rate and concurrency limits, secret isolation, agent sandboxing, and transactional state where concurrent writes matter.

## Integrating a dedicated Hermes profile

A repository's `agents/hermes/SOUL.md` may be documentation only. Trace the actual runtime call. If the backend invokes `hermes chat`, the repository files do not specialize that process.

Minimal integration:

1. Create a dedicated profile cloned from a working profile.
2. Set `terminal.cwd` to the repository so repo-level `AGENTS.md` is injected.
3. Replace the profile `SOUL.md` with project-specific operating rules.
4. Keep its gateway stopped unless a dedicated channel and clean messaging credentials are intentionally configured.
5. Change the real subprocess call to `hermes -p <profile> chat -q <message>`; an environment variable may override the profile when portability matters.
6. Verify twice: run the profile directly, then call the dashboard's chat endpoint and require an exact sentinel response.

## macOS resolved-path pitfall

On macOS, temporary paths may enter the program as `/var/...` but resolve to `/private/var/...`. If path validation resolves the candidate, derive relative paths from the resolved base too:

```python
resolved = (base / user_path).resolve()
relative = resolved.relative_to(base.resolve())
```

Mixing `resolved.relative_to(base)` can raise even after containment validation succeeds. Keep traversal tests plus one valid-file test running inside a temporary directory.

## Capability truth before user guidance

Do not equate navigation labels, repository folders, or marketing copy with supported dashboard workflows. When the user asks how to create or manage something from the public URL:

1. Inspect the rendered UI and list the actual controls available.
2. Search the frontend API client for the requested operation.
3. Inspect the backend route and its validation/storage path.
4. Classify the capability explicitly:
   - **UI-supported** — a visible workflow calls a real endpoint;
   - **API-only** — the endpoint exists but the dashboard has no control for it;
   - **static adapter/config** — the named “agents” are hardcoded runtime integrations, not dynamically creatable entities;
   - **absent** — implementation is required.
5. Distinguish an **agent** (identity, runtime/model, tools, memory, lifecycle) from a **skill** (reusable instructions executed by an existing agent). Do not present a generated skill template as a new autonomous agent.
6. If an API-only workaround is safe, give a same-origin `fetch(...)` example so the authenticated browser session can call it without exposing tunnel credentials. State exactly what files/state it creates and any hardcoded defaults.

Prefer the existing runtime plus a skill when that satisfies the specialization. Add dynamic-agent CRUD only when independent identity, memory, tools, model selection, or lifecycle is genuinely required.

## Verification checklist

- Local health responds.
- Full test suite passes after integration.
- Dedicated profile command returns the expected sentinel.
- Dashboard chat reaches that profile, not the default profile.
- Unauthenticated public request is `401`.
- Authenticated public root and health are `200`.
- App and tunnel processes are confirmed running.
- Final handoff includes local path, profile command, URL, credentials, online/offline agents, and temporary-versus-production caveat.
