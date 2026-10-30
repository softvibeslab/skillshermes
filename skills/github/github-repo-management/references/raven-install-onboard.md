# Raven GitHub install + onboard notes

Use when installing `EverMind-AI/Raven` from source on macOS/Linux.

## Install path

```bash
BASE="$HOME/Documents/GitHub"
mkdir -p "$BASE"
git clone https://github.com/EverMind-AI/Raven.git "$BASE/Raven"
cd "$BASE/Raven"
./install.sh
```

The local installer is source-aware: it installs `uv` if missing, checks Node >= 22, builds `ui-tui/dist/entry.js`, then installs Raven as a global uv tool at `~/.local/bin/raven`.

## Verify

```bash
raven --version
raven --help
raven doctor
```

If `raven doctor` says config is missing, run onboarding.

## Onboard headlessly

Inspect the CLI first, then use the non-interactive flags when credentials are known:

```bash
raven onboard \
  --non-interactive \
  --provider anthropic \
  --api-key "$ANTHROPIC_API_KEY" \
  --skip-sandbox \
  --skip-channel \
  --skip-memory \
  --yes \
  --reset
```

Provider examples:
- `anthropic` with `ANTHROPIC_API_KEY`
- `openrouter` with `OPENROUTER_API_KEY`

Avoid putting raw API keys directly in the command string; pass them via environment variables or let the interactive wizard prompt for paste. Raven may store provider config in `~/.raven/config.json`.

## Pitfall

A successful onboard can still warn if the provider probe fails. Example: Anthropic may return `Your credit balance is too low`. In that case `raven doctor` can still report config healthy, but `raven doctor --probe` and `raven agent ...` will fail until billing/provider access is fixed or the provider is changed.