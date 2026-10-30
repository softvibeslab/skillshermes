# Secure CRM Bridge pattern (MongoDB → GraphQL/MCP → Hermes)

Use this when the user wants Hermes to access CRM/database data without giving the agent direct database access.

## Architecture

```text
MongoDB CRM
  ↓
project-specific bridge service
  ├─ GraphQL API for human/dev queries
  └─ MCP stdio server for Hermes tools
       ↓
Hermes profile / gateway bot
```

## Safety defaults

- Do **not** give Hermes direct MongoDB access.
- Keep the MCP server as the permission boundary.
- Read-only first:
  - `READ_ONLY_MODE=true`
  - `ENABLE_WRITES=false`
  - `ALLOW_FULL_PII=false`
- Mask PII by default: phone/email/WhatsApp fields should be redacted unless an explicit env flag permits full PII.
- Write tools should exist but hard-fail unless both write flags are enabled.
- Never store real Mongo URI/API keys in source; create `.env.example` only.

## Useful implementation shape

- TypeScript Node project with:
  - `src/index.ts` GraphQL API, usually `graphql-yoga`.
  - `src/mcp/server.ts` stdio MCP server using `@modelcontextprotocol/sdk`.
  - `src/db.ts` shared Mongo connection.
  - `src/security/pii.ts` masking helpers.
  - `src/crm/repository.ts` query/write boundary.
- Scripts:
  - `npm run build` → `tsc -p tsconfig.json`
  - `npm run dev` → GraphQL dev server
  - `npm run mcp` → TS MCP server via `tsx`
  - `npm run mcp:dist` → compiled MCP server

## MCP connection pitfall

Hermes stdio MCP subprocesses may start from a different working directory. The bridge should load `.env` relative to the project/module path, or support an explicit env pointer like `ROVI_CRM_BRIDGE_ENV=/absolute/path/.env`. Do not rely only on `dotenv.config()` from current working directory.

Example robust config loader:

```ts
import dotenv from 'dotenv';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const moduleDir = path.dirname(fileURLToPath(import.meta.url));
const projectEnvPath = path.resolve(moduleDir, '..', '.env');
dotenv.config({ path: process.env.ROVI_CRM_BRIDGE_ENV || projectEnvPath });
dotenv.config();
```

## Validation checklist

1. `npm install`
2. `npm run build`
3. `npm run typecheck` if available
4. Start GraphQL with safe dummy/local env and POST a health query.
5. Start MCP with safe dummy/local env and verify the process stays alive waiting on stdio.
6. Only then add to Hermes:

```bash
hermes --profile <profile> mcp add <name> --command "node /absolute/path/to/project/dist/mcp/server.js"
hermes --profile <profile> mcp test <name>
hermes --profile <profile> mcp configure <name>
```

Restart the target Hermes profile/gateway after adding MCP servers so tools are rediscovered.
