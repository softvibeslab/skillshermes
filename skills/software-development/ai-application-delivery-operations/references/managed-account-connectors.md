# Managed account connectors: research lessons

This reference preserves findings from a connector comparison, not a successful account-linking test. Revalidate provider support, pricing, and client commands before use.

## Provider comparison to revisit

- Composio: https://composio.dev/hermes — documented Hermes integration using `hermes mcp add` with OAuth, a dashboard, and managed account connections. Starting candidate for low-configuration personal agent use.
- Pipedream: https://mcp.pipedream.com — hosted MCP/account authorization; the research found Gmail and Facebook Pages support and a free own-use offering. Check current terms and customer-facing production conditions separately.
- Zapier MCP: research found a two-task charge per MCP call against the automation quota. Especially worth comparing when the user already has Zapier connections. Verify current pricing and desired actions.
- Nango: developer-oriented authorization/integration infrastructure with self-hosting options; evaluate when embedding integrations into a product, not automatically as the lowest-friction end-user choice.

## Important Composio distinctions observed

| Service | Research finding; recheck before setup |
|---|---|
| Gmail | Managed OAuth available |
| Facebook | Managed OAuth for Pages, not a promise of personal-profile access |
| Instagram | Professional Business/Creator accounts, not all personal accounts |
| Meta Ads | Own credentials required in the reviewed setup; not equivalent to managed one-click OAuth |
| WhatsApp | Business API support, not personal chat-account access |

The research surfaced different free allowances: a larger headline total and a smaller managed-OAuth allowance. The snapshot described 100K total calls versus 20K with managed OAuth. These figures are historical findings, not a current price guarantee. Inspect pricing footnotes and credentials requirements together before calling an offering free or plug-and-play.

## Minimal verification ladder

1. Read technical auth and action documentation for each requested app/account type.
2. Inspect installed client help without changing configuration. The observed `hermes mcp add --help` exposed `--url` and `--auth {oauth,header}`. That proved CLI support, not a successful connection.
3. Load the current Hermes skill/documentation before setup; use the provider's currently documented endpoint rather than constructing one.
4. Obtain authorization to configure. Let the user complete consent; do not ask for account passwords in chat or blindly approve excessive scopes.
5. Separate hub authorization from downstream app authorization. Discover tools, then run a narrow read-only query.
6. Report documented support, configured transport, authorized accounts, and successfully queried actions as separate states.
7. Gate sends, publishing, deletion, and ad spend independently of read access.

## Presentation pattern

Lead with the best fit and its dashboard/documentation link, then the account-type exceptions and cost boundary. Distinguish research from tested execution. Do not build a skill or dashboard merely because the request mentions one; a hosted connector may already cover the need. Preserve the user's requested low-friction experience while being explicit about the Meta products that require business accounts or developer credentials.
