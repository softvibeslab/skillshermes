# Local Hermes Profile Hub

Use when a privileged dashboard must display and manage the Hermes profiles stored on the same machine.

## Minimal runtime pattern

1. Keep the dashboard bound to `127.0.0.1`; it can create, rename, back up, and delete real profiles.
2. Point the backend at the authoritative Hermes root:

```bash
export AGENTIC_OS_HERMES_HOME="$HOME/.hermes"
export AGENTIC_OS_HERMES_PROFILE="agentic-os"
export AGENTIC_OS_HERMES_BACKUP_DIR="$HOME/.hermes/backups/agentic-os-profiles"
```

3. Store the dashboard admin token in a mode-600 file instead of source code or shell history:

```bash
TOKEN_FILE="$HOME/.hermes/agentic-os-admin-token"
[ -s "$TOKEN_FILE" ] || openssl rand -hex 24 > "$TOKEN_FILE"
chmod 600 "$TOKEN_FILE"
export AGENTIC_OS_ADMIN_TOKEN="$(<"$TOKEN_FILE")"
```

4. Start the existing app locally, then open its Profiles route. Copy the token without printing it:

```bash
pbcopy < ~/.hermes/agentic-os-admin-token
```

## Verification

- Count profile directories from the configured Hermes root and include `default` exactly once.
- Authenticated `GET /api/hermes/profiles` returns that same count.
- The dashboard Profiles route renders an admin-token gate.
- The profiles endpoint returns `401` without the token.
- The UI exposes a real create action backed by `hermes profile create`, not a static card or mock.
- Keep protected-profile decisions authoritative in the backend.

## Deployment boundary

A dashboard running on a VPS sees the VPS Hermes home, not profiles on a user's Mac. Do not claim a public dashboard is connected to local profiles merely because both use Hermes. The smallest safe solution is to run Profile Hub on the machine that owns `~/.hermes` and optionally publish that localhost service through an authenticated tunnel. Copying profile directories to the VPS creates a separate snapshot, not a live connection.

A stopped profile gateway does not prevent one-shot CLI calls such as `hermes -p <profile> chat -q ...`; gateway status and CLI availability are separate checks.
