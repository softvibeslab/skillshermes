# Profile-local plugin installation and lazy specialist routers

Use this when a specialized Hermes profile needs a third-party plugin without changing `default` or every other profile.

## Safe installation sequence

1. Create and harden the target profile first. Do not start its gateway while cloned platform credentials, webhooks, or cron jobs are still active.
2. Validate the plugin source and generated artifacts using the repository's own checker when available.
3. If the project separates source conversion from installation, run conversion first. A missing generated integration directory is a build-state issue, not a reason to copy files manually.
4. Point installation explicitly at the target profile:

```bash
./scripts/convert.sh --tool hermes
HERMES_HOME="$HOME/.hermes/profiles/<profile>" \
  ./scripts/install.sh --tool hermes --no-interactive
```

5. Verify all three layers before restart:
   - plugin files exist under `$HERMES_HOME/plugins/<plugin>/`;
   - `config.yaml` lists the plugin under `plugins.enabled`;
   - plugin-specific validation passes.
6. Restart only the target profile gateway and inspect fresh startup lines.
7. Confirm the gateway reports only intended platforms. A healthy Telegram connection does not excuse an inherited webhook or duplicate platform failure.
8. Test one representative plugin capability. For a lazy specialist router, search/inspect one agent before trusting delegation.

## Lazy router pattern

Prefer one router plugin plus on-disk specialist data over hundreds of permanent Hermes profiles. The router should expose stable operations such as search, inspect, prompt composition/load, and delegation. Create a dedicated profile only when a role needs independent memory, credentials, channel, workspace, or recurring processes.

## Verification evidence

Report:

- target profile and plugin path;
- generated specialist count or catalog version;
- plugin enabled state;
- validator result;
- fresh gateway PID/connection state;
- one pending manual handshake, such as Telegram `/start`, separately from runtime activation.

Never claim first-contact delivery succeeded when Telegram returns `Bad Request: chat not found`; provide the bot link, ask the user to press Start, then retest.
