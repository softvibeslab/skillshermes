# Raven install and onboarding notes

Use when the user asks to install or configure `https://github.com/EverMind-AI/Raven`.

## Install from a local clone

```bash
BASE="$HOME/Documents/GitHub"
mkdir -p "$BASE"
git clone https://github.com/EverMind-AI/Raven.git "$BASE/Raven"
cd "$BASE/Raven"
./install.sh
```

The local installer detects the source checkout, builds the TUI bundle with `npm ci && npm run build` under `ui-tui/`, then installs Raven as a `uv` tool. Expected binary:

```bash
~/.local/bin/raven
```

Verify:

```bash
raven --version
raven --help
raven doctor
```

Fresh install can be healthy structurally but unconfigured until `~/.raven/config.json` exists.

## Non-interactive onboarding with an API-key provider

Use this when the user supplies a key and does not need channel/sandbox/memory setup yet:

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

Then:

```bash
raven doctor
raven doctor --probe
```

If `doctor` is healthy but `doctor --probe` or onboarding's test message fails with billing/credits, the config is valid; the provider account needs credits or a different provider.

## Codex OAuth provider

Raven supports OpenAI Codex via OAuth, not API key.

```bash
raven provider login openai-codex
```

Then set the default model in `~/.raven/config.json`:

```bash
python3 - <<'PY'
import json
from pathlib import Path
p = Path.home() / ".raven/config.json"
data = json.loads(p.read_text())
data["agents"]["defaults"]["model"] = "openai-codex/gpt-5-codex"
data["agents"]["defaults"]["provider"] = "auto"
p.write_text(json.dumps(data, indent=2) + "\n")
PY
```

Verify:

```bash
raven doctor
raven doctor --probe
```

Pitfall: CLI command uses hyphenated provider names (`openai-codex`, `github-copilot`), while config/registry internals use underscores or camelCase (`openai_codex`, `openaiCodex`).
