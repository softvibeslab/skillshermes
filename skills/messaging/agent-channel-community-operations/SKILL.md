---
name: agent-channel-community-operations
description: Provision, secure, operate, and verify agent-facing communication channels and learning communities across Slack, Telegram, and Skool; covers identity, authorization, topology, content publishing, channel context, transport conflicts, and end-to-end validation.
version: 1.0.0
metadata:
  hermes:
    tags: [agents, messaging, communities, slack, telegram, skool, provisioning, verification]
---

# Agent Channel and Community Operations

Use when an agent or service must be connected to, organized within, or operated through a messaging workspace or learning community.

## Shared operating model

1. Resolve the exact workspace/community, bot/app identity, target channel/course/chat, and requested mutation.
2. Check session/token capability and inspect live state before writing.
3. Use the narrowest durable API or MCP path; reserve GUI automation for OAuth, admin, or platform-only UI steps.
4. Keep secrets outside source and conversation output; preserve allowlists and minimize scopes.
5. Apply changes in dependency order and in small idempotent batches.
6. Re-list/read back every mutation and prove a real end-to-end path, not merely authentication.
7. Report identity, access, object IDs, verified delivery/publication, and anything still requiring a human step.

## Platform modes

### Slack workspace and project-channel operations

Manage app scopes and reauthorization, channels, membership, topics/purposes, Socket Mode consumers, status messages, sidebar caveats, and channel-to-repository onboarding. Prove one canary channel before batching; channel existence, bot membership, posted message, and agent reply are separate facts.

### Telegram bot operations

Verify `getMe`, exactly one polling/webhook consumer, private-chat `/start`, numeric allowlist authorization, outbound delivery, then a real inbound agent reply. Treat exposed tokens as compromised and rotate them. For cloned Hermes profiles, scrub inherited messaging credentials before startup; never infer the human allowlist ID from the bot token or reuse a fixed ID from another profile. See `references/telegram-bot-operations-hermes-profile-allowlists.md`.

### Skool community and classroom operations

Check session, inspect courses/lessons/posts/events before mutation, publish folders and lessons in small slices, fetch created content to verify rendering, and keep Git-reviewed canonical content separate from observed remote snapshots. Distinguish inventory from adoption analytics.

## Support files

Detailed absorbed procedures are preserved in:

- `references/slack-workspace-operations.md`
- `references/telegram-bot-operations.md`
- `references/skool-community-operations.md`

Load the platform reference before acting; it contains exact failure interpretation, API/MCP fallbacks, publication verification, concurrent-session guards, and platform-specific limits.

## Safety boundaries

- Never print or persist passwords, bot tokens, OAuth tokens, or app-level tokens in notes or summaries.
- Scope additions require reauthorization; configuration alone does not upgrade an installed token.
- Do not claim operational success until the platform-specific real inbound/outbound or publish/read-back check succeeds.
- Stop on authorization dialogs, password prompts, conflicting consumers, stale GUI focus, or an explicit user stop signal.
