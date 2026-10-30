# ROVI CRM Bridge MCP pattern

Session-specific pattern for connecting a secure CRM bridge to Hermes via MCP.

## Bridge shape

- MongoDB CRM remains private; Hermes does not connect to Mongo directly.
- A local TypeScript bridge exposes:
  - GraphQL HTTP API for operational/manual queries.
  - MCP stdio server for Hermes tools.
- Safe defaults:
  - `READ_ONLY_MODE=true`
  - `ENABLE_WRITES=false`
  - `ALLOW_FULL_PII=false`
- PII sanitization is done in the bridge before data reaches Hermes. Mask emails/phones unless explicitly enabled.
- Write tools should exist but call a shared guard and fail closed unless both write flags are enabled.

## Project produced

Path:

```text
/Users/USERNAME/.hermes/profiles/rovi-broker/workspace/rovi-crm-agents/rovi-crm-bridge
```

MCP server:

```text
dist/mcp/server.js
```

Tools exposed:

- `rovi_crm_search_leads`
- `rovi_crm_get_lead`
- `rovi_crm_search_properties`
- `rovi_crm_get_property`
- `rovi_crm_list_followups`
- `rovi_crm_create_note`
- `rovi_crm_create_task`
- `rovi_crm_update_lead_stage`

## Hermes MCP CLI pitfall

Do **not** pass a whole shell command string to `--command` for stdio MCP servers. This fails because Hermes treats it as the executable path.

Wrong:

```bash
hermes --profile rovi-broker mcp add rovi-crm --command "node /abs/path/dist/mcp/server.js"
```

Right:

```bash
hermes --profile rovi-broker mcp add rovi-crm \
  --command node \
  --args /abs/path/dist/mcp/server.js
```

In non-interactive contexts, the add command prompts to enable tools. Pipe Enter to accept default all-tools selection:

```bash
printf '\n' | hermes --profile rovi-broker mcp add rovi-crm \
  --command node \
  --args /abs/path/dist/mcp/server.js
```

Verify:

```bash
hermes --profile rovi-broker mcp test rovi-crm
hermes --profile rovi-broker mcp list
```

A new Hermes session or gateway restart is still required for the agent to discover and use newly added MCP tools.

## Verification recipe used

1. Build/typecheck bridge:

```bash
npm run build
npm run typecheck
```

2. Start GraphQL bridge temporarily and query health with API key header.
3. Query one lead and verify:
   - A lead is returned.
   - Email/phone are masked under `ALLOW_FULL_PII=false`.
4. Run MCP server; for stdio, no output while running is normal.
5. `hermes --profile rovi-broker mcp test rovi-crm` should list discovered tools.

## Security notes

- Never print `.env` values or Mongo URI. Log only variable names or redacted summaries.
- If copying from an existing CRM `.env`, construct the new `MONGODB_URI` programmatically and print `[REDACTED]`.
- Keep `.env` out of git.
- Leave write flags disabled until user explicitly asks to enable writes and confirms the scope.
