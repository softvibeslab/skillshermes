# Buzz self-hosting and Codex ACP notes

Use this reference when evaluating or deploying Block's `block/buzz`.

## Distribution boundary

- Buzz has a desktop client (Tauri + React) and a separately self-hostable relay stack.
- A headless VPS should normally run the production relay bundle under `deploy/compose/`; the desktop app remains on the user's workstation and connects over WebSocket.
- Do not treat the root `docker-compose.yml` as production deployment. Upstream explicitly reserves it for local development.
- The production bundle requires Docker Compose v2.24.4+, Postgres, Redis, MinIO, stable secrets, migrations, and optionally Caddy/TLS.
- Before deployment, resolve two real prerequisites: non-interactive SSH key access and either a DNS name for TLS or explicit approval for a temporary IP-only, non-TLS test.
- Never request or type the VPS password. Have the user authorize an existing public key with `ssh-copy-id`, then verify access using `BatchMode=yes`.

## Minimum VPS workflow

1. Inspect upstream `README.md`, `deploy/compose/README.md`, `.env.example`, Compose files, image tags, and license.
2. Verify VPS architecture, OS, disk, memory, Docker/Compose versions, occupied ports, and existing deployment directory before modifying anything.
3. Clone into a dedicated path such as `/opt/buzz` only after confirming it is absent or safe to update.
4. Generate stable secrets once; never print them into chat or logs.
5. Validate with `./run.sh config` before starting.
6. Start privately first, probe `/_liveness`, inspect status/logs, then expose through DNS/TLS.
7. Report that the relay was deployed; do not imply that the GUI desktop application runs usefully on a headless VPS.

## Private npm-prefix Codex ACP failure

Buzz desktop can maintain its own npm prefix under its application-support directory. A system-global Codex installation does not repair this private dependency tree.

Typical symptom:

```text
Missing optional dependency @openai/codex-darwin-arm64
all agents failed to start
```

Diagnosis:

- Confirm host and Node architecture.
- Read the nested `@openai/codex/package.json` and verify its platform-specific optional dependency.
- Inspect the app-private npm logs for `ETIMEDOUT` and `reify failed optional dependency`.
- Check whether multiple ACP packages were installed concurrently into the same prefix; parallel global installs can leave one adapter partially installed.
- If every agent fails identically, recognize that they share one broken ACP executable rather than treating them as independent failures.

Repair the owning adapter in the same private prefix, with the desktop app closed, instead of following a generic global reinstall hint. Preserve the installed adapter version unless an upgrade is explicitly intended. Verify one agent before restoring full concurrency.
