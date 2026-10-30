---
name: contabo-cntb
description: Operates Contabo VPS/VDS resources through the official cntb CLI with profile-scoped credentials and token caches. Use when installing or configuring cntb, listing Contabo instances, managing authorized infrastructure, or activating Contabo access in a requested Hermes profile.
---

# Contabo CLI — cntb

## Local installation

- Source: /Users/USERNAME/Documents/SoftvibesLab/cntb
- Executable: /Users/USERNAME/.local/bin/cntb
- Upstream: https://github.com/contabo/cntb
- API credentials: https://my.contabo.com/api/details
- Installation uses the official Darwin ARM64 release, not a source build. Go/Docker are unnecessary for operation.
- On another machine discover OS/architecture and install the matching official release; verify its SHA-256 against the release checksums before execution.

## Scope and safety

1. Resolve the active Hermes home from HERMES_HOME; default is ~/.hermes. Never silently use another profile's credentials.
2. Store config and cache beneath $HERMES_HOME/integrations/contabo. Pass this directory as HOME to cntb only; do not change the agent's HOME.
3. Always pass --config explicitly: cntb also searches /etc/cntb otherwise. Set umask 077 and --debug warn. Remove inherited CNTB_* variables from the child environment if present so they cannot override credentials/endpoints.
4. Never run `cntb config view` on real credentials: it prints secrets. Never use debug/trace: upstream logs access tokens. Never read config or token cache into chat.
5. Start with read-only inventory. Verify exact resource IDs, names, account and current state before mutation. Resource creation can bill the account. Get explicit informed approval for purchases, deletion, reinstall, rollback, shutdown/restart, credential changes and network/security changes. Never infer authorization from installation alone.
6. This skill is procedural guidance, NOT an OS/API security boundary. Hermes profiles under the same OS user are not sandboxed. Use Contabo-side permissions and separate OS accounts/containers when actual isolation is needed.

## Configure credentials privately

Ask the user to run the bundled script in their own interactive terminal, not in tool logs. All four credential inputs are hidden; do not ask for secrets in chat or pass them in command-line arguments.

```sh
python3 /Users/USERNAME/.hermes/skills/contabo-cntb/scripts/setup.py --hermes-home /Users/USERNAME/.hermes
```

For a named profile, use its installed script and verified absolute Hermes home. The script writes JSON syntax accepted as YAML to `.cntb.yaml`, refuses to overwrite existing config, and uses private file/directory permissions. Credentials remain plaintext on disk; do not commit, sync or publish them. Authentication is NOT verified by saving the config.

## Read-only verification and inventory

Set H to the verified target home. Use an absolute binary path if PATH is missing in a gateway.

```sh
H="${HERMES_HOME:-$HOME/.hermes}"
C="$H/integrations/contabo"
# ponytail: native CLI plus scoped HOME isolates the token cache without a wrapper service.
(umask 077; HOME="$C" /Users/USERNAME/.local/bin/cntb --config "$C/.cntb.yaml" --debug warn get instances -o json)
```

Before executing, confirm config exists without printing contents; refuse if missing. Check inherited CNTB_* variable names, never values. For agent execution use subprocess with a copied environment excluding all CNTB_* keys, and override HOME just for that child. Never enable shell tracing.

- `cntb version` and `cntb get instances --help` are offline checks, not account validation.
- `cntb get instances -o json` is the authenticated smoke test; verify exit status and JSON. Do not expose full inventory unnecessarily.
- `cntb get images --help` / `cntb get --help` discover read operations.
- Use `--page` and `--size` to paginate; one page is not necessarily the whole inventory.
- For any mutation, inspect `cntb <verb> <resource> --help`; do not guess flags. Re-read resource state afterward.
- If authentication fails, do not repeatedly retry or reset passwords. Check credential presence/permissions, API access in the panel, and sanitized error status.
- Token cache is `$C/.cache/cntb/token`. Do not print it. Ensure private permissions. Never share a cache across profiles/concurrent accounts.

## Report VPS status

- Fetch fresh read-only inventory for a current-status request; do not reuse a previous `running` result as current evidence. Include query time and timezone.
- Report name, ID, provider status, plan, region/datacenter and allocated CPU/RAM/disk when returned. Preserve API units; allocated resources are not utilization metrics.
- `running` means powered on according to Contabo, not healthy applications, working SSH, Docker availability or free disk. Guest health requires separately authorized SSH/monitoring access.
- Capture stdout/stderr privately, check exit status, parse JSON, and display only selected fields. On failure, report sanitized error categories rather than raw output. Do not describe an empty/malformed response as success.
- See [Safe inventory and authentication troubleshooting](references/inventory-and-auth.md) for the verified subprocess pattern and credential recovery checks.

## Bootstrap de acceso SSH y dashboard protegido

- Separar autenticación Contabo, SSH y web. Resolver el acceso al huésped antes de prometer despliegue; un HTML, un registro DNS o HTTPS solos no constituyen un canal seguro de credenciales.
- Si el usuario entra por contraseña, preferir que la ingrese en su terminal y autorice una llave dedicada. No solicitarla en chat ni enviarla por correo; distinguirla del código temporal de acceso al dashboard.
- Descubrir DNS y acceso al proveedor antes de cambiar registros. No inferir control DNS por disponer de herramientas de hosting o de cloudflared.
- Verificar acceso no autenticado denegado, identidad permitida y origen protegido antes de entregar un enlace como operativo. Reportar cada capa pendiente sin confundir propuesta con implementación.
- Procedimiento: [Bootstrap seguro de observabilidad web](references/secure-dashboard-bootstrap.md).

## Límites de recursos dentro del VPS

Para limitar RAM de un perfil Hermes, usar systemd/cgroups del huésped, no la API Contabo. Confirmar nombre exacto y gestor del servicio (`systemctl` frente a `systemctl --user`), medir consumo y revisar reinicios antes de aplicar un techo. Si el techo está por debajo del consumo actual, advertir sobre OOM e interrupción y resolver la autorización antes del cambio. Verificar el cgroup y la salud del gateway, no solo que el comando termine correctamente. Procedimiento: [Límites de memoria por perfil](references/profile-resource-limits.md).

## Activate in another Hermes profile — only when requested

1. Load hermes-agent skill and list profiles to identify the exact existing target. Do not create a profile or modify unrelated configuration without a request.
2. Copy this complete skill directory (SKILL.md, references and scripts) to that profile's skills/contabo-cntb, refusing to overwrite a different existing skill. Use supported file tools with explicit cross-profile authorization. Do not copy credentials or tokens.
3. Ask whether the profile should use a distinct account. Default to independent credential setup with `--hermes-home` pointing at the target. Sharing credentials requires separate explicit consent.
4. Verify `hermes -p NAME skills list` discovers the skill. Reload skills or start a new session if needed; do not restart all gateways.
5. Verify the CLI on the profile's actual execution host. Local installation on this Mac does not install it on remote backends.
6. Run the read-only authenticated check only after credentials are configured, and report skill availability separately from successful API access.

## Maintenance checks

```sh
python3 /Users/USERNAME/.hermes/skills/contabo-cntb/scripts/setup.py --self-test
/Users/USERNAME/.local/bin/cntb version
git -C /Users/USERNAME/Documents/SoftvibesLab/cntb status --short
```

Updating the source checkout does not update the installed binary. Discover current official releases, verify checksum and architecture, then replace the binary only when an update is requested.
