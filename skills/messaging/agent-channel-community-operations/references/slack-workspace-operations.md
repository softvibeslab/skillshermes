---
name: slack-workspace-operations
description: Provision, organize, and verify Slack workspaces through the Slack API, app manifests, Socket Mode, channels, memberships, and bot access. Use when connecting an agent to Slack, creating or restructuring channels, assigning channel purposes, troubleshooting bot visibility, or validating an end-to-end Slack integration.
---

# Slack Workspace Operations

Operate Slack through durable APIs first; use the desktop UI only for OAuth/admin steps that Slack does not expose to the available token.

## Workflow

1. **Inspect before changing anything**
   - Identify the workspace, app, bot user, target channels, and desired topology.
   - Read the app manifest/scopes and determine whether the token is a bot or user token.
   - List existing channels before creating new ones; reuse or rename when that produces less clutter.

2. **Choose the smallest control path**
   - Prefer Slack Web API calls for channel creation, membership, topics, and test messages.
   - For public channel creation, ensure the acting token has the required management scope (normally `channels:manage`) before attempting `conversations.create`.
   - Use Socket Mode only for receiving events without a public HTTP endpoint; it does not grant channel-management privileges.
   - Use the GUI for app installation, OAuth approval, or workspace-policy dialogs only.
   - When the user supplies an exact permalink that the bot token cannot read, try API → authenticated desktop deep link → narrowly filtered local cache recovery. Never dump Slack LevelDB blocks: adjacent values can contain authenticated session material. See `references/slack-workspace-operations-slack-workspace-operations-slack-permalink-local-recovery.md`.

### MCP administration path

When Slack administration is requested through MCP:

- Inspect configured MCP servers first; a working Slack chat gateway does not imply an MCP admin server exists.
- Check the maintenance/deprecation status of any community Slack MCP package before installing it.
- If no trustworthy maintained server fits, prefer a narrow local MCP bridge exposing only the required operations: list/create channels, set topic/purpose, invite members, and post messages. Avoid a generic unrestricted Slack API passthrough.
- Keep the Slack token outside source code and chat output. Reauthorize after adding scopes; configuration changes alone do not upgrade the installed token.
- Make batch provisioning idempotent: normalize names, reuse existing channels, and retain a project-to-channel-ID result map.
- For the known-good capability gate, narrow FastMCP bridge shape, `${SLACK_BOT_TOKEN}` interpolation, and reauthorization/canary sequence, see `references/slack-workspace-operations-slack-mcp-channel-admin.md`.

### Capability gate and canary

Before promising or batch-creating channels, prove the complete path on **one** real channel (prefer the first requested channel over a disposable test channel):

1. List existing channels and confirm the proposed name is not already present.
2. Create one canary channel.
3. Verify the channel exists, the intended members/bot can access it, and one status message lands in it.
4. Only then repeat for the remaining channels.

If no token/tool can list and manage channels, stop before GUI batch work. Deliver the proposed topology and initial status drafts, state that creation is unverified, and name the single prerequisite needed (appropriate Slack scope/admin action or an available Slack window). Never imply channels were organized merely because names were drafted.

For GUI-only work, do not assume an unlabeled accessibility button is “Next” or “Create.” Use visible labels when available; otherwise operate one dialog at a time, recapture after every click, and abandon the batch if the window or verification path disappears.

3. **Provision in dependency order**
   - Update the manifest/scopes.
   - Reinstall or reauthorize the app when scopes change.
   - Create or reuse channels.
   - Invite the bot with `conversations.invite` or `/invite @bot`.
   - Set channel purpose/topic where useful.
   - Send a minimal test mention.

4. **Verify end to end**
   - Confirm the API call returned `ok: true` and retain channel IDs.
   - After any batch—especially when tool output is truncated or ambiguous—discard assumptions about what ran and reconcile from live Slack state: paginate `conversations.list`, compare against the exact requested-name set, then inspect each channel with `conversations.info`.
   - Confirm the bot is a member of every target channel; existence and `is_member` are separate checks.
   - Confirm topic/purpose independently rather than treating a successful create/join response as full provisioning.
   - Mention the bot in that channel and verify one response from the intended Hermes profile.
   - Check gateway logs for a received Slack event and a successful reply.
   - If multiple gateways share credentials, stop duplicates before testing; one Slack app/token pair should have one intended event consumer.

## Channel-organization defaults

Keep the initial topology small. A practical baseline is:

- `#anuncios`: decisions and company-wide updates
- `#operaciones`: delivery, blockers, and daily execution
- `#ventas`: pipeline and follow-up
- `#contenido-marketing`: campaigns and publishing
- `#workflows`: agents, automations, and process design
- `#informal`: social conversation

Reuse existing channels when their audience and history fit. Do not create speculative channels without an owner or recurring use.

When a filesystem or project catalog contains several folders for one real-world entity, create **one channel per client/product**, not one channel per folder. Consolidate analyses, proposals, media, redirects, alternate implementations, and archived outputs under the owning project channel. Explicitly exclude dependency repositories, tool libraries, output folders, and container directories unless they have an active owner and recurring workflow.

### Sidebar sections are not channels

Treat Slack custom sidebar sections (for example, `Landings`) separately from channel provisioning. They are user-specific UI organization and are not managed by the normal conversations Web API. API/MCP automation can create channels, set purpose/topic, invite members, and post status messages; the user normally creates the sidebar section once and moves channels into it. If requested, GUI automation may handle that personal UI step, but report it as GUI work rather than MCP/API provisioning. For a new empty section, complete Slack's two-step flow and choose **Omitir** on the conversation-picker step; verify the section heading appears before reporting success. See `references/slack-workspace-operations-slack-workspace-operations-custom-sidebar-sections.md` for the keyboard-safe GUI procedure.

## Safety

- Never print OAuth, bot, or app-level tokens in summaries or logs copied to chat.
- Store secrets in the designated environment/config file with restrictive permissions.
- Do not copy tokens to another host unless the user explicitly authorizes that destination.
- Scope additions require reauthorization; editing a manifest alone does not upgrade an installed token.

## GUI fallback pitfalls

Desktop automation is focus-sensitive. If another application becomes frontmost, stop rather than clicking against stale coordinates. Prefer adding the proper API scope over repeatedly automating channel-creation dialogs. If GUI work is unavoidable:

1. Operate one dialog at a time and recapture accessibility state after every transition.
2. Treat Slack channel creation as a two-step flow: enter the name, then explicitly verify visibility and press **Create**. Do not infer success from the first dialog closing.
3. Verify the resulting channel name, public/private state, and sidebar section before creating the next channel.
4. Prefer labeled accessibility elements. If a menu item cannot be pressed, recapture or reopen the menu; do not use blind menu-key typing because stale focus can send text as the logged-in user.
5. Before any typing, confirm the expected modal or input is visible. If the user is actively typing or a draft is present, stop UI automation rather than competing for focus.
6. Do not batch or queue GUI actions across changing screens. A delayed click or keystroke can land in the next dialog.

## New-channel messaging dependency

A newly created channel may not be resolvable by the bot or generic messaging target list until the bot is a member and channel discovery refreshes. Provision in this order:

1. Create and verify the channel.
2. Invite the intended bot/profile.
3. Refresh/list messaging targets and confirm the channel resolves.
4. Post the initial status through the API or messaging tool.
5. Verify the message in the channel.

Do not fall back to typing messages through the desktop UI while the user is active unless the user explicitly requests user-account posting.

## Project-channel context onboarding

When asked to connect Hermes to a project channel and give it project context:

1. Resolve the exact channel with the messaging target list before touching the Slack UI. Use the named target when available; retain the returned channel ID.
2. Match the channel slug to the real local workspace/repository. Inspect existing project notes, plans, prompts, Git state, tests, and live services before summarizing.
3. Create or update one concise context document inside the owning project. Include identity, purpose, MVP boundary, verified state, risks, next actions, sources of truth, and a rule requiring Hermes to recheck live state before future reports.
4. Post a shorter operational summary to the project channel: purpose, stage, verified progress, blockers, and three next actions.
5. Verify both artifacts independently: read back the context file and confirm the messaging tool returned success plus a message/channel ID.
6. Distinguish three separate facts in the report: message posted, bot membership confirmed, and Hermes response verified. Posting success alone does not prove the latter two.

Avoid committing context into a dirty mixed-purpose branch unless requested. Report the untracked file and recommend a clean project branch rather than mixing unrelated work.

## Project-channel context bootstrap

When one channel represents one project, do not stop after inviting the bot. Build a verified channel → repository map, inspect current repository evidence, post a compact purpose/status/blocker/next-step card, and verify delivery. Private channels must appear in a refreshed messaging-target list after invitation. Mark repository matches and historical test evidence explicitly when they are not confirmed live.

### Concurrent channel/session guard

A portfolio request may trigger several Hermes sessions at once. Prevent duplicate or contradictory onboarding:

1. Assign one owner per project channel; a channel worker updates only its channel, while one orchestrator owns the portfolio summary.
2. Before posting, inspect recent channel/session results for an existing status card. Correct or update it instead of broadcasting another independent version.
3. Freeze one canonical channel → project → repository map before parallel analysis. Label uncertain repository matches as candidates.
4. Treat a posted message, confirmed bot membership, and a verified Hermes reply as three separate outcomes.
5. If `stop`, `para`, or equivalent arrives, cancel pending side effects immediately. Resume only after a later explicit instruction, starting with fresh Slack discovery rather than stale UI references.

If conflicting repository mappings were already published, send one short correction with the canonical path and explicitly supersede the earlier context.

## References

- See `references/slack-workspace-operations-slack-workspace-operations-hermes-socket-mode.md` for the Hermes-specific Slack setup and troubleshooting checklist.
- See `references/slack-workspace-operations-slack-workspace-operations-project-channel-context-bootstrap.md` for the repeatable per-project onboarding, repository inspection, private-channel verification, and status-card workflow.
- See `references/slack-workspace-operations-slack-workspace-operations-project-channel-context.md` for the reusable context-file and Slack-status structure.
- See `references/slack-workspace-operations-slack-workspace-operations-concurrent-project-channel-onboarding.md` for multi-session ownership, stop semantics, deduplication, and canonical channel-to-repository mapping.
- See `references/slack-workspace-operations-slack-workspace-operations-slack-permalink-local-recovery.md` for the last-resort, security-bounded recovery of a user-supplied permalink from an authenticated Slack desktop cache.
