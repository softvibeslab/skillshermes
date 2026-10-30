# Softvibes Telegram package example

Session example of a Hermes profile package delivered as a ZIP.

## Observed layout

Top-level bundle contained both presentation assets and installable profile assets:
- `README.md`
- `agent/profile.json`
- `config/config.yaml`
- `ops/install_to_hermes_profile.sh`
- `softvibes-flow-hermes-profile.tar.gz`
- `SOUL.md`
- `skills/`
- `memories/`
- `knowledge_base/`
- `dashboard/`

## Intended profile

- Profile name: `softvibes-flow`
- Channel: Telegram
- Language: Spanish
- Tagline: "Deja que los agentes hagan la multitarea. Tu quedate en el flow."

## Safe install pattern used

1. Inspect archive contents.
2. Extract into a temp directory under `~/.hermes/tmp/`.
3. Read `README.md`, `agent/profile.json`, and `ops/install_to_hermes_profile.sh` before execution.
4. Verify target profile does not already exist.
5. Run the helper installer.
6. Verify with `hermes profile list`.
7. Inspect installed `.env` and report the remaining secret/config step.

## Important gotcha captured

The installed `.env` contained a malformed placeholder line:

```bash
TELEGRAM_BOT_TOKEN=*** Optional but recommended
```

Treat this as an example-template defect, not a usable token value. Always inspect `.env` after install and explicitly tell the user to replace malformed placeholders with the real BotFather token before starting the gateway.

## Good final handoff

Report:
- profile installed path
- gateway state (`stopped` until token is configured)
- exact `.env` file to edit
- exact launch command for the profile
