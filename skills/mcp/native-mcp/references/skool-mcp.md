# Skool MCP via `skool-cli`

Use this when adding Skool.com automation as a Hermes MCP server.

## Known-good config

```yaml
mcp_servers:
  skool:
    command: npx
    args:
      - -y
      - -p
      - skool-cli
      - skool-mcp-server
    timeout: 120
    connect_timeout: 60
```

Verify:

```bash
hermes mcp test skool
```

Expected result: connection succeeds and discovers 37 tools including `skool_login`, `skool_list_courses`, `skool_create_post`, `skool_get_members`, `skool_get_analytics`, and chat/notification tools.

## Why `-p` matters

`skool-cli` exposes multiple npm binaries (`skool` and `skool-mcp-server`). Plain:

```bash
npx -y skool-cli skool-mcp-server
```

can fail with `npm error could not determine executable to run`. Use:

```bash
npx -y -p skool-cli skool-mcp-server
```

For Hermes MCP, that becomes `args: ["-y", "-p", "skool-cli", "skool-mcp-server"]`.

## Browser prerequisite

Skool uses Playwright/browser automation. Install Chromium for the package before first real use:

```bash
npx -y -p skool-cli playwright install chromium
```

## Auth

Login is separate from MCP installation. Either call the MCP `skool_login` tool from Hermes or run:

```bash
npx -y -p skool-cli skool login --email "$SKOOL_EMAIL" --password "$SKOOL_PASSWORD"
```

Do not store Skool credentials in the MCP config unless the user explicitly wants env-based automation.
