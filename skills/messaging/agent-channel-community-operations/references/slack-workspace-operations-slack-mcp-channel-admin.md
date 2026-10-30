# Slack MCP channel-administration bridge

Use this when a Slack chat MCP can read/post but cannot create or organize channels.

## Capability distinction

A valid bot token and a connected Slack MCP do not imply channel administration. Prove both gates separately:

1. Token gate: call `conversations.create` on the first requested channel (idempotently: list/reuse before create). `missing_scope` with `needed: channels:manage` means the app must add that bot scope and be reinstalled/re-authorized; editing config or a manifest alone does not upgrade the existing token.
2. Tool gate: inspect discovered MCP tools. Chat-only servers commonly expose list/history/post/reply/reaction but not create, topic, purpose, or invitations.

## Smallest durable bridge

Prefer a narrow local FastMCP stdio server over a generic Slack API passthrough. Expose only:

- `list_channels`
- `create_channel` (public only; normalize names; list/reuse first)
- `set_channel_details` (`conversations.setTopic` and `conversations.setPurpose`)
- `invite_users` (`conversations.invite`)

Read `SLACK_BOT_TOKEN` from the environment, never source code. In Hermes MCP config, pass it by placeholder so it remains in `.env`:

```yaml
mcp_servers:
  slack_admin:
    command: /absolute/path/to/hermes/venv/bin/python3
    args: [/absolute/path/to/slack_admin.py]
    env:
      SLACK_BOT_TOKEN: ${SLACK_BOT_TOKEN}
```

Hermes resolves `${VAR}` from its `.env` before launching the filtered MCP subprocess environment.

## Required sequence

1. Add `channels:manage` under Bot Token Scopes or the app manifest.
2. Reinstall/re-authorize the Slack app; retain the new bot token if Slack rotates it.
3. Restart/reload MCP discovery.
4. Test the admin MCP connection and confirm all four tools are discovered.
5. Canary on the first real requested channel, not a disposable channel:
   - list and reuse if present;
   - create if absent;
   - set topic/purpose;
   - verify membership and post one status message.
6. Only then run the remaining batch and retain a name-to-channel-ID map.

## Scope and post-batch verification

Do not infer an installed scope from the OAuth UI or from seeing a reinstall button. Make one authenticated Web API request and inspect Slack's `x-oauth-scopes` response header; require `channels:manage` there. A valid `auth.test` proves token/workspace identity, not administrative capability.

Treat every provisioning batch as an idempotent reconciliation:

1. Paginate `conversations.list`; do not rely on one page or on earlier script output.
2. Build the exact desired-name set and classify each channel as missing or existing.
3. Create only missing channels.
4. For every desired channel, call `conversations.info` and require `is_member: true`.
5. Join/invite where needed, set topic and purpose, then read them back.
6. Report success only when desired count equals verified count and the failure list is empty.

This reconciliation is also the recovery path when a previous script exited successfully but its output was truncated: inspect live Slack state instead of rerunning blindly or assuming nothing happened.

When inviting through the Slack desktop composer, `/invite @Bot` may open mention autocomplete. Press Return once to select the mention and again to send the command, then verify membership through `conversations.info`; visible text in the composer is not evidence that the command executed.

## Validation and safety

- Channel names: normalize to lowercase ASCII `[a-z0-9_-]`, 1–80 characters.
- Public channel IDs: validate `C[A-Z0-9]+`.
- Invitee IDs: validate user IDs (`U…` or `W…`), deduplicate before calling Slack.
- Treat sidebar sections separately: they are per-user UI organization, not normal channel API objects.
- If UI automation is denied or reaches password/2FA/admin approval, stop and give the user the exact remaining OAuth/reinstall steps; continue API verification only after authorization.
