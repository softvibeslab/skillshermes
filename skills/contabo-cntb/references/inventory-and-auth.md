# Safe inventory and authentication troubleshooting

## Verified CLI invocation pattern

Resolve the target Hermes home and absolute binary first. For Python subprocess execution:

- Integration directory: `<verified-hermes-home>/integrations/contabo`.
- Require `.cntb.yaml` to exist and reject a symlink; never display its contents.
- Copy the environment excluding keys beginning `CNTB_`; set `HOME` only in that child environment to the integration directory.
- In a short-lived launcher set umask `077` before spawning, so newly written OAuth cache files are private.
- Run `[binary, '--config', config_path, '--debug', 'warn', 'get', 'instances', '-o', 'json']` with `capture_output=True`, `text=True` and a bounded timeout.
- Check return code before parsing stdout as JSON. Inspect the actual response shape rather than assuming list versus object envelope. Handle invalid JSON or unexpected schema as a failed verification.
- Select only required instance fields: `instanceId`, `name`, `displayName`, `status`, `region`, `dataCenter`, `productName`, `cpuCores`, `ramMb`, `diskMb`.
- Include a timezone-aware local query timestamp. Use pagination when necessary; one returned page is not proof of total account inventory.

This avoids raw token-bearing diagnostics in tool output. `--config` alone does not isolate OAuth: cntb stores its token at `$HOME/.cache/cntb/token`. Existing permissions must also be checked: config/cache files 0600 and private integration/cache directories 0700. Umask only affects newly created files.

## Authentication recovery

A successful config write is not successful authentication. An `invalid_grant` / `Invalid user credentials` response warrants checking that the user entered the API User and API Password from the Contabo API details page, not assuming the ordinary control-panel login is interchangeable. Do not print raw stderr, token/cache contents or credentials when diagnosing.

The bundled setup script refuses overwrites. For an intentional credential correction, have the user privately back up or move the existing config without overwriting another backup, then rerun setup interactively with hidden input. Explain that backups also contain plaintext credentials and need restrictive permissions. Do not reset passwords or delete caches blindly. After correction, perform one fresh authenticated read-only query and report its outcome separately from installation and skill availability.

## Status interpretation

`running` confirms the provider reports the instance powered on. CPU cores, RAM and disk fields describe provisioned capacity, not current load, consumption or free storage. Application health, Docker status and logs require a separate guest-level check. Never imply API authentication grants SSH access.

## Evidence boundaries

Report separately: binary installation/version, skill discovery, credential file creation, authenticated API access, and guest health. A successful inventory query does not prove the setup script's self-test or skill checklist ran. If a validation command is denied, do not repeat it or obtain the same result through another route without renewed authorization.

When activating another profile, copy the complete skill package including references and scripts, not credentials or token cache; verify on that profile's actual execution host.
