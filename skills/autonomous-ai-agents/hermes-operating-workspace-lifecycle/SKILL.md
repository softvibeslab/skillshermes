---
name: hermes-operating-workspace-lifecycle
description: Use when creating, installing, packaging, specializing, launching, activating, or troubleshooting Hermes profiles and project operating workspaces, especially Telegram/gateway handoffs.
version: 1.2.0
author: Hermes Agent
license: MIT
created_by: agent
metadata:
  hermes:
    tags: [hermes, profiles, workspaces, gateway, telegram, packaging, specialization, launch]
    related_skills: [hermes-agent, hermes-agent-skill-authoring]
---

# Hermes Operating Workspace Lifecycle

## Overview

Use this umbrella skill for the full lifecycle of a Hermes operating workspace: project launch docs, dedicated profiles, specialized SOUL/skills, package import/export, gateway activation, Telegram/WhatsApp handoff, and live troubleshooting.

The class-level goal is to turn a user request into a safe, durable operating system rather than a one-off prompt or a half-configured bot.

## When to Use

Use this when the user asks to:

- create, clone, activate, switch, or troubleshoot a Hermes profile;
- install/import a profile package from ZIP/tarball;
- package/export a specialized Hermes profile for delivery;
- launch a project workspace with plan, dashboard, prompts, Kanban, tools map, and bot handoff;
- design a domain-specific or executive Hermes agent/profile;
- connect or debug Telegram/WhatsApp/Slack/Discord/webhook gateway behavior for a profile;
- upgrade the Hermes core while preserving profiles, sessions, gateways, secrets, and local source customizations.

Do not use for ordinary answers unrelated to Hermes profiles/workspaces. Load `hermes-agent` too when configuring Hermes Agent itself.

## Core Mental Model

A Hermes operating workspace has five layers:

1. **Workspace artifacts** — `PLAN.md`, `DASHBOARD.md`, prompts, tools/MCP map, scripts, dashboard, README.
2. **Profile identity** — `profile.yaml`, `SOUL.md`, memories, operating tone, project/domain context.
3. **Skill architecture** — one class-level umbrella skill plus companion skills only for distinct operating questions.
4. **Messaging/runtime config** — `.env`, `config.yaml`, gateway state, Telegram/WhatsApp allowlists, home channel.
5. **Package/install surface** — ZIP/tarball, install docs, templates, secret-clean placeholders, verification checklist.

## Workflow A — Project Ops Launch

Use this when the user is starting a new project and wants it operational, not just documented.

1. Create one project workspace under the user's project root.
   - For Softvibes/ROVI-adjacent work, prefer `/Users/USERNAME/Documents/SoftvibesLab/<ProjectName>` when appropriate.
   - Keep the first file set lean: `PLAN.md`, `DASHBOARD.md`, `PROMPTS.md`, `TOOLS_SKILLS_MCPS.md`, `TELEGRAM_SETUP.md`, `scripts/`.
2. Write the operating docs.
   - `PLAN.md`: strategy, audience, offer, milestones, risks, next actions.
   - `DASHBOARD.md`: current status, KPIs, sprint board summary, blockers, next 7 days.
   - `PROMPTS.md`: reusable prompts for content, research, execution, sales, community ops.
   - `TOOLS_SKILLS_MCPS.md`: available tools first; suggest new tooling only when it unlocks a current deliverable.
   - `TELEGRAM_SETUP.md`: token handoff, allowlist notes, gateway commands.
3. If a project-planning or snapshot dashboard is requested, ship a smallest-useful static app first. For live management of real Hermes profiles/configuration, follow the mutable fleet control-plane guidance below instead; a localStorage mockup does not satisfy live CRUD.
   - Single-file `dashboard/index.html`, no framework/backend by default for planning/snapshot dashboards.
   - Use `localStorage` plus JSON export/import before sync.
   - Include Kanban, owners, subtasks, notes/evidence, content calendar, team roles, rituals, KPIs, and AI/Hermes prompt/skill map.
4. Create a dedicated Hermes profile only when ongoing autonomous operation is needed.
5. Add Kanban only when it is a repeated execution handoff, not because every plan needs a board.
6. When research must become a future agent but profile activation is not yet approved, create one self-contained, source-hashed knowledge workspace inside the project's existing data/knowledge area; link it from parent indexes and report “workspace ready” separately from “profile active.” Follow `references/hermes-project-ops-launch--research-backed-agent-knowledge-workspace.md`.
7. If publishing to GitHub, add `.gitignore`/`README.md`, run a lightweight secret scan, then push and verify remote HEAD.

## Workflow B — Profile Creation, Activation, and Runtime Ops

1. List profiles before changing anything.
2. Choose creation mode deliberately.
   - Fresh profile for clean setup.
   - `--clone-from <source>` to inherit known-good configuration selectively.
   - `--clone-all` only when the user explicitly wants full copied state.
   - For a specialized profile that will be invoked by an orchestrator while sharing its Slack workroom, create fresh, copy only `config.yaml` and model `auth.json`, leave `.env` absent, and test with one-shot `chat -q`. Treat channel → profile routing as `documented` until a dedicated app or explicit router proves it. See `references/hermes-profile--shared-slack-coordination-channel.md`.
   - For a research-backed domain expert, create fresh with `--no-skills`, then selectively copy only required model/tool configuration. `--no-skills` is mutually exclusive with clone flags. Audit copied config for unrelated MCP registrations before the first chat, because an inherited OAuth MCP can open a browser or block the smoke test. Preserve the supplied corpus as per-source evidence, add one umbrella skill plus an evidence map, import only the first-use domain skills, and wire both into `SOUL.md`. Follow `references/hermes-profile--research-backed-domain-specialist.md`.
   - For an expert grounded in one source repository, clone and inspect the code first, pin the checkout path and commit in `SOUL.md`, create one profile-local skill with architecture/operations references, copy only provider auth when required, and prove grounding with a one-shot question that cites correct files and lines. Heavy runtime dependencies and model downloads are not prerequisites for code expertise. Follow `references/hermes-profile--repository-grounded-codebase-specialist.md`.
3. Only when switching the sticky default is requested, activate with `hermes profile use <name>` and verify the active profile changed. Creating a specialist alone does not authorize switching defaults; use `hermes -p <name> ...` or its wrapper for scoped verification.
4. Check the target profile gateway immediately.
5. If the user expects Telegram responses and the gateway is stopped, start it and verify logs.
6. Inspect Telegram wiring when behavior is wrong:
   - `TELEGRAM_BOT_TOKEN`
   - `TELEGRAM_ALLOWED_USERS`
   - `TELEGRAM_HOME_CHANNEL`
   - the config allowlist, normally `platforms.telegram.extra.allowed_users` (older profiles may use `platforms.telegram.allowed_users`)
   - gateway logs for connection, polling conflict, or `Unauthorized user`.
   Keep `.env` and `config.yaml` allowlists synchronized, restart the target gateway, and verify both parsed values plus the live PID. Follow `references/hermes-profile-operations--telegram-allowlist-troubleshooting.md`.
7. Sanitize cloned runtime state before gateway start.
   - Blank stale Discord/Slack tokens, set `WHATSAPP_ENABLED=false`, and disable every non-target platform.
   - Disable cloned webhook blocks or assign unique ports to avoid `8644` collisions.
   - Audit copied cron jobs; `--clone-all` copies schedules, so pause/remove source-profile jobs before the new gateway can fire them.
   - Treat cloned logs as historical data: verify only fresh lines after the target profile's current startup marker.
   - Follow `references/hermes-profile-operations--isolated-telegram-profile-hardening.md` for the full hardening and first-contact sequence.
8. Verify BotFather token with Telegram `getMe` using redacted output.
   - Load the token from the profile-local `.env`; never interpolate or print it in user-facing output.
   - Return only `ok`, bot ID, username, and Telegram's error description.
   - If verification is denied, blocked, or inconclusive, stop before gateway start. Report the profile as configured but not activated, and give one exact continuation action; never imply the bot is live.
   - If the user has not supplied the token in a secure channel, do not request it in chat. Finish the non-secret setup and generate a local `getpass` bootstrap script that validates `getMe` and `getWebhookInfo`, atomically writes the profile `.env` with mode `0600`, and only then starts the gateway. Follow `references/hermes-profile-operations--secure-local-telegram-token-handoff.md`.
9. For a fresh isolated Telegram profile, follow `references/hermes-profile-operations--fresh-isolated-telegram-bot.md`; it includes the required structured `home_channel` shape, model preflight, macOS launchd verification, and token-rotation handoff.
10. Before switching a profile to a requested model, separate model existence, artifact installation, account entitlement, and end-to-end Hermes success.
   - Verify the exact ID and current pricing in the provider's live catalog.
   - Run one minimal inference probe before changing the known-good default.
   - Treat a successful Ollama `:cloud` pull as manifest installation only; it does not prove free access.
   - Follow `references/hermes-model-runtime--availability-entitlement-preflight.md`.
11. Install third-party plugins into the target profile, not implicitly into `default`.
   - Run any required conversion/build step before installation.
   - Set `HERMES_HOME=~/.hermes/profiles/<profile>` explicitly.
   - Verify plugin files, `plugins.enabled`, the plugin validator, a fresh gateway restart, and one representative capability.
   - For lazy specialist routers, keep the catalog on disk and create permanent profiles only for roles needing independent state.
   - Follow `references/hermes-profile--profile-local-plugin-installation.md`.
12. For cross-host installation or knowledge synchronization, inventory profiles on both hosts and resolve the target mapping before writes. Inspect installer helpers: `--profile` may still modify the main config, and profile-local `HERMES_HOME` plus `--profile` may construct an unintended nested path. Separate SSH authentication probes from optional capability checks; a remote command's nonzero exit is not proof of failed authentication. Share only allowlisted project artifacts, not all Hermes runtime state; verify two-way edits, conflicts, offline catch-up, and secret exclusions before claiming synchronization. Follow `references/hermes-cross-host--installer-and-sync-preflight.md`.
13. For parallel work across a VPS and a local workstation, use GitHub Issues as the durable queue, host/state labels for routing, one branch per Issue, and PRs as verified delivery.
   - Keep exactly one owner for each long-polling Telegram bot; the other host can remain a CLI/worker without that gateway.
   - Prove one manual Issue-to-PR round trip before adding webhooks or polling automation.
   - Follow `references/hermes-profile--cross-host-github-worker-coordination.md`.

### Approval failures: evidence before attribution

- A tool response such as `User denied` establishes that execution was blocked, not necessarily that the person clicked Reject. Say “la aprobación no se completó” unless an explicit user rejection is established. If the user says they did not reject it, acknowledge the correction rather than repeating the tool's attribution.
- Distinguish explicit rejection, policy auto-denial, callback/input failure, and timeout using the installed approval implementation and fresh session-correlated logs. Historical matches illustrate possible causes; they do not diagnose the current session.
- Keep the approval boundary intact: do not disable security or retry the blocked action through another tool. User authorization and a functioning runtime approval channel are separate requirements.
- Treat restarting/resuming the CLI as a recovery attempt, not a proven fix. Verify supported commands first, preserve the pending scope, and confirm the approval flow works before claiming recovery. Do not make the user repeat the entire project brief.

Evidence limits and diagnostic checklist: `references/hermes-runtime--approval-attribution.md`.

### Adapting repository-native assistant kits

For repositories that ship Claude/Codex skills rather than a conventional application, separate repository installation, Hermes skill adaptation, profile specialization, optional UI runtime, and personal onboarding into independent verification gates. A clone plus a model setting is not an expert profile.

- Inspect skill bodies and their scripts/resources before copying. Preserve companion files, namespace collision-prone names, and translate upstream command/tool assumptions; changing frontmatter alone does not establish compatibility. Verify discovery and one representative skill-loaded chat before advertising slash commands.
- Verify the skill inventory again after the first real chat. Some Hermes builds seed bundled skills even for a profile created with `--no-skills`. For a user-authorized narrowly scoped profile, preserve those files and disable the extra names with the native profile-local `skills.disabled` YAML list; verify the registry shows only intended skills enabled. Do not alter global sync behavior to solve one profile's scope.
- Keep optional knowledge visualizers scoped to repository documents initially. Confirm the actual bind address, HTTP response, and source boundary separately; a localhost URL or a started process does not prove loopback-only exposure or application health.
- When extending an existing visualizer across named projects, reuse its configuration and history. Resolve project names to evidence-backed source roots before indexing, check real paths and symlinks, and keep other profiles' memories and conversations outside the source set unless separately authorized. Use bounded discovery within the approved scope before asking the user to locate folders; do not invent project variants as clarification choices. Verify representative nodes for every requested project, not just server health.
- Distinguish a repository-native skill from an installed Hermes skill. If registry lookup does not resolve it, inspect the documented repository skill path within the authorized workspace; do not install it merely to read it or claim it was loaded successfully. After compaction, label prior reads as historical until inspected again.
- Run read-only health checks separately from profile writes and Git-exclusion changes. A denied mixed command proves neither the read nor the write occurred. Stop after denial; do not retry through another tool or claim its planned artifacts exist.
- Onboarding examples are not verified user facts. Ask one question at a time, keep unknowns explicit, and distinguish documenting a connection from authorizing or activating it.

For multi-project knowledge visualizers, prefer an explicit strategic-document allowlist over recursive repository indexing. Keep project variants and third-party ownership clear, preserve the existing visual composition, and inspect selected documents for embedded secrets even when they are READMEs. Verify exclusions in graph/search data and node/raw-source responses, not just the visible search index. Report documentation coverage separately from operational status, and tested interactions separately from untested ones.

Curation manifest, privacy gates, AIS-OS build landmarks, and UI verification recipe: `references/project-knowledge-visualizer--curation-and-verification.md`.

Adaptation checklist and AIS-OS source landmarks: `references/hermes-profile--assistant-kit-adaptation.md`.

### Fleet migration between workstation and VPS

For multi-profile moves, produce a dependency-and-acceptance matrix before proposing a cutover order. Choose the smallest verified dependency surface as pilot, not merely the most related business project; missing MCP declarations do not prove independence. Read identities, skills, scripts, cron and external workspaces. Keep migration separate from a core upgrade, rebuild OS-specific environments, and measure destination headroom before promising fleet capacity.

A migration plan is not permission to stop gateways or transfer private state. For authorized execution, stage the destination with all autonomous consumers disabled, validate by CLI, drain source work, stop and verify source services and their automatic restart paths, synchronize final state, then activate exactly one destination gateway. Enable audited schedules last. Profiles sharing an OS user are not filesystem security boundaries. Host-bound workers require explicit identity, queue-label and capability adaptation, not just copied folders. Rollback must reconcile newly written state and external actions before reactivating the old host.

When staging under a dedicated Linux account, run configuration migration, provider authentication and CLI probes as that runtime user with the same resolved profile home the service will use. A successful root login does not authenticate the bot. Keep source operation intact while destination authentication is pending. On resumption, verify the live authorization process before presenting a device code: never reconstruct a redacted code from a summary or assert an expiry window without current provider output. Configuration inspection is not an inference test.

Detailed fleet matrix, cutover gates, destination-authentication checkpoints and rollback reconciliation: `references/hermes-profile--cross-host-migration.md`.

### Skill-context optimization pilots and IDE handoff

Before proposing a skill selector, trace the installed catalog builder, its prompt-assembly callers and existing skill tools. Distinguish metadata indexes from full skill bodies: changing SOUL instructions cannot remove tokens injected by the harness. Reuse category listing and on-demand loading; compare a simple lexical baseline before adding a decision model. Preserve current eligibility filters and stable-prefix caching, evaluate ambiguous/multi-skill cases, and measure total cost and latency including classifier calls—not just token reduction. Start in observation mode with uncertainty and broadening fallbacks; routing never grants permissions.

For plan-only requests, deliver one verified workspace plan and a bounded discovery-first IDE prompt. Verify the editor CLI before giving opening commands; do not modify the running core, profiles or gateways merely to deliver the plan. If the user accepts email or editor commands, either delivery path suffices; report only the one actually completed.

Source landmarks, evaluation gates and Cursor handoff recipe: `references/hermes-profile--skill-selection-pilot.md`.

## Workflow C — Safe Hermes Core Upgrade

Use this when Hermes must be updated without losing runtime state or local edits to the agent core.

1. Inventory the installed version, Git divergence, modified/untracked files, profiles, and live gateways without printing secrets.
2. Separate backups: use Hermes' supported backup for runtime state and a dedicated Git bridge for explicitly allowlisted source/test files. Private is the default recommendation, not permission to change visibility: honor an explicit request to keep the repository public. Before any public push, review every outgoing commit and reachable history for secrets/private material; if that cannot be established, keep the backup local and offer a sanitized snapshot.
   - Preflight backup traversal with `lstat`: preserve symlinks as links rather than following them, exclude special files, and keep the destination outside every source tree. Inventory size, external link targets, free space, and write permissions before starting. Stop if copied bytes exceed the inventoried scope.
   - Treat archive integrity and recoverability as separate gates: test extraction into an isolated directory and validate required state before activation. Detailed gates: `references/hermes-core--bounded-backup-and-recovery.md`.
3. Stop and verify every active gateway before copying mutable state or changing the active installation; record exactly which ones were running.
4. Build the candidate from a clean upstream revision in an isolated worktree, then reapply the reviewed customization branch there.
5. Run focused tests, the full supported suite, disposable config migration checks, and CLI/profile/gateway smoke tests before touching production.
   - Preserve manual approvals; distinguish interactive approval expiry from subagent policy auto-denial by tracing the actual caller. Do not enable auto-approval to make maintenance pass.
   - Probe skill synchronization under a temporary `HERMES_HOME`, including `.no-bundled-skills`. A candidate may seed essential skills despite that marker; report the actual delta and obtain consent before broadening intentionally scoped profiles.
   - Prefer `uv pip check --python <candidate-venv>/bin/python` when uv manages the candidate environment; do not install pip solely to check dependencies.
   - Report dependency consistency, focused tests, restore verification, and runtime smoke tests as separate gates. Passing a focused subset does not prove upgrade readiness.
   - Reproduction and evidence boundaries: `references/hermes-core--approval-and-skill-sync-preflight.md`.
6. Keep approval-sensitive operations isolated: run reversible checks and tests separately, prefer a new immutable remote branch over force-pushing, and request approval only for the single history-rewrite command when it is truly required.
7. Activate transactionally, restart only previously active gateways, and verify version, profiles, live processes, fresh logs, and customized behavior.
8. Keep rollback two-layered: old source revision plus runtime-state backup.
9. Define the pause path before quiescing: if approval is denied mid-maintenance, restore the recorded gateways or explicitly report that maintenance mode remains active and provide one exact continuation action.

Never update a dirty checkout in place, never assume `hermes update --backup` preserves source customizations, and never store secrets or `$HERMES_HOME` runtime data in the Git bridge. Follow `references/hermes-core--safe-upgrade-with-local-customizations.md`.

## Read-only Fleet Audit and Status Dashboard

When the user asks for status, optimization, or an update-readiness dashboard, audit first; this is not authorization to update, restart, repair permissions, change repository visibility, or edit any profile.

1. Resume from existing report files and inspect any existing Profile Hub before building another app. After interruption or compaction, verify artifacts and tests on disk before marking tasks complete or repeating prior success claims.
2. Keep collection read-only and write only to the report workspace. Export allowlisted metadata, never credentials, message bodies, raw logs, or arbitrary configuration objects.
3. Distinguish configured, process-running, last-recorded channel state, and end-to-end verified. A PID alone does not prove gateway identity; saved channel state is not a heartbeat. Show evidence timestamps and uncertainty. Stopped does not mean broken.
4. Deliver a small local static dashboard with searchable profiles, detail panels, sessions/usage, resources, security findings, and a staged update/rollback path. Explicitly label it a snapshot, not live monitoring; do not publish fleet metadata without separate approval.
5. Verify collection invariants, rendering, filtering, empty states, mobile layout, and absence of unintended external requests. Report only checks actually executed. Save incremental artifacts so provider interruptions do not erase progress.

Detailed collection semantics and verification gates: `references/hermes-fleet--read-only-status-dashboard.md`.

### Mutable fleet control planes

For live profile/session/channel/model/SOUL/MCP/skill/cron management, inspect the installed native dashboard extension contract and existing Profile Hub before adding another app. Track read, mutation, recovery, and end-to-end verification separately for each requested capability; inventory is not CRUD, a successful bundle is not plugin integration, and synthetic backend tests are not deployment proof. Enforce backend deny-by-default profile access, metadata-only responses, symlink-safe filesystem boundaries, revision-checked atomic mutations, backups, and redacted audit records. Verify concurrent writes with disposable profiles. Before remote publication, validate authentication, authorization, proxy/Host handling and HTTPS rather than simply relaxing localhost guards. Deploying the app does not authorize exporting all local profile state.

Security gates, concurrent lock-creation regression, and remote release checks: `references/hermes-fleet--mutable-control-plane.md`.

### Cross-host operational control towers

For a dashboard backed by a live workstation/VPS bridge, reuse the existing store and delegation mechanisms before adding an execution layer. Explicitly separate specialist catalog, task registration, dispatch, execution, and completion: a saved task is not a dispatched job, and available roles are not permanent running agents. Label automatic versus manually recorded delegation evidence by host/profile, show last-success and stale states, and report costs/tokens only when measured. Verify a representative delegation on each runtime, task persistence through the browser, bridge integrity, and current service state independently. Matching hashes prove only point-in-time equality; service installation does not prove startup recovery. Disclose workstation sleep/login/network dependencies and the host-local scope of loopback URLs.

Verification recipe and the Sales Academy handoff's evidence boundaries: `references/hermes-cross-host--control-tower-evidence.md`.

## Workflow D — Package Installation / Import

Use this when the user provides a ZIP/tarball profile package.

1. Inspect archive contents before writing.
2. Identify the intended profile slug and package shape.
3. Read `README.md`, `INSTALL.md`, `ops/install_to_hermes_profile.sh`, and nested tarballs before execution.
4. Summarize what will be installed and get consent before writing under `~/.hermes/profiles/` unless the user already approved installation.
5. Extract to a temporary workspace.
6. Prefer the package installer only if it is transparent and limited to profile copy/setup.
7. Verify:
   - profile directory exists;
   - expected files landed (`SOUL.md`, `config.yaml`, `skills/`, `memories/`, `workspace/`);
   - `hermes profile list` sees it;
   - `.env` exists and uses sane placeholders.
8. Close with the exact next step: token path, gateway state, start/status commands.

## Workflow E — Specialized Profile / Executive Agent Design

Use this when the user wants a domain-specific operator, executive chief-of-staff agent, or non-generic profile.

1. Define the leader/domain/scope and core operating question.
   - Resolve the analytical object before writing `SOUL.md`: “analyze a video” may mean interpreting its thesis, assumptions, worldview, evidence status, and human implications—not auditing editing, visuals, audio, or production.
   - Treat the input medium as transport, not automatically as the job. If the user cares about “lo que transmite”, make meaning/content analysis primary and production analysis explicitly opt-in.
2. Define main outputs: daily briefing, attention radar, executive minute, action plan, follow-up note, etc.
3. Define approved sources and guardrails. Separate evidence from hypothesis.
4. Create a class-level umbrella skill first.
5. Add companion skills only for distinct operating questions:
   - operational leakage vs leadership attention leakage;
   - diagnosis vs accountability;
   - prep vs follow-up packaging.
6. Wire skills into `SOUL.md` under an explicit specialists/internal modes section.
7. For multiniche digital-growth profiles, inventory the source and target profiles separately, keep one invariant evidence→diagnosis→execution→measurement method, and vary the funnel by business archetype. Draft outside the target profile until application is approved. Follow `references/hermes-profile--multiniche-digital-growth-agent.md`.
8. Restart the gateway after profile-local skills or `SOUL.md` changes.

### Model-capability specialists

When asked to make a profile expert in a model's “superpowers,” use live catalog and endpoint evidence, not identity prose alone. Keep model-specific snapshots in references under a class-level operational skill; wire it into SOUL. Separate advertised capability, runtime configuration, successful inference, and representative capability tests. Verify configuration keys are actually consumed (`agent.reasoning_effort` in the inspected CLI), media transport, endpoint-specific tool-choice restrictions, reference-file existence, and published retirement dates. Do not silently change the selected model or global default. Checklist: `references/hermes-profile--model-capability-specialist.md`.

### Naming pattern

Good names are class-level and describe the job to be done:
- `resort-leadership-intelligence`
- `flow-friction-finder-agent`
- `executive-meeting-prep`

Bad names encode one session, feature codename, or today's fix:
- `catalonia-agent-v3`
- `fix-leader-dashboard-today`
- `chris-idea-skill`

## Workflow F — Packaging / Export for Handoff

Use this when the user wants a reusable deliverable, knowledge transfer pack, or ZIP profile package.

Choose the smallest artifact that carries the requested state:

- **Knowledge-only handoff:** package one installable class-level skill with curated `references/`, an import prompt, manifest, stdlib validator, ZIP integrity test, and SHA-256 sidecar. Do not export a whole profile merely to move domain knowledge. Follow `references/hermes-knowledge-skill-transfer-pack.md`.
- **Runtime/profile handoff:** use the full profile structure below only when identity, memories, tools, gateway wiring, or runtime config must move.

Minimum full-profile package structure:

- `profiles/<profile-name>/profile.yaml`
- `profiles/<profile-name>/SOUL.md`
- `profiles/<profile-name>/config.yaml`
- `profiles/<profile-name>/.env.example`
- `profiles/<profile-name>/.env` with blanks/placeholders only
- `profiles/<profile-name>/skills/...`
- `profiles/<profile-name>/memories/MEMORY.md`
- `profiles/<profile-name>/memories/USER.md`
- `profiles/<profile-name>/workspace/README.md`
- `profiles/<profile-name>/SUGGESTED_CRON_JOBS.md`
- package-level `README.md`
- package-level `INSTALL.md`
- optional `install_profile.sh`

Never ship live secrets. Keep gateways stopped until real tokens and allowlists are configured.

## Telegram / WhatsApp Handoff Rules

### Telegram
Prepare placeholders for:
- `TELEGRAM_BOT_TOKEN`
- `TELEGRAM_ALLOWED_USERS`
- `TELEGRAM_HOME_CHANNEL`
- `TELEGRAM_HOME_CHANNEL_NAME`

If the intended chat/user is already known, prefill allowlist/home channel values, but leave bot token blank unless the user provided it in the current secure context.

### WhatsApp
Prepare placeholders for:
- `WHATSAPP_MODE=bot`
- `WHATSAPP_ENABLED=false`
- `WHATSAPP_ALLOWED_USERS`
- `WHATSAPP_HOME_CHANNEL`
- `WHATSAPP_HOME_CHANNEL_NAME`

Document later pairing with:

```bash
hermes --profile <profile> whatsapp
```

Do not auto-enable WhatsApp unless explicitly requested.

## Low-friction continuity and productivity customization

When evaluating productivity skills or configuring a workspace to reduce attention load:

- Separate response formatting, durable task state, and idea capture. A concise-output skill does not itself preserve progress between sessions; reuse `handoff` for checkpoint artifacts and `capture` for parked ideas rather than building another tracking system.
- For el operador, lead resumptions with proyecto / avance / un siguiente paso. Keep optional ideas out of the active task unless he switches scope.
- Resolve the latest live request before resuming a summarized task. Compaction notes and historical tool results are evidence, not new authorization. Label historical checks as historical; never turn a recalled test result into a claim of fresh verification.
- Inspect third-party skill instructions and executable hooks separately. Report cloned, reviewed, installed, and activated as distinct states; a repository-analysis request does not authorize plugin installation or changes to other profiles.
- Treat ADHD-oriented formatting as an optional communication aid, not a diagnosis or clinical efficacy claim. Do not infer health information from a repository title or productivity preference.

## Softvibes / ROVI Defaults

When the project is Softvibes/ROVI-style, default to:

- SER → HACER → TENER framing.
- Practical DWY/DFY ladder: free value → low ticket/community → bootcamp → high ticket → DFY.
- Natural Mexican Spanish, energetic and practical.
- Systems around lived user experience: attention load, rituals, social pressure, emotional friction, not just automation.

## Common Pitfalls

1. **Activating a profile but not starting its gateway.** Always check gateway status and logs.
2. **Assuming clone-all created a new Telegram bot.** Same token means same bot identity with a different Hermes profile/context.
3. **Shipping real secrets in a package.** Use placeholders and verify ZIP contents without echoing secret-bearing files.
4. **Creating one-session skills.** Put session/domain detail in `references/`; keep skill names class-level.
5. **Skipping package inspection.** Archives often contain nested profiles, install scripts, or malformed `.env` templates.
6. **Starting gateway too early.** Build and package first; start only after credentials/allowlists are ready.
7. **Not wiring skills into SOUL.** Skill files alone do not guarantee live specialist behavior.
8. **Ignoring inherited runtime state in cloned profiles.** Disable unused webhooks/platforms, audit copied cron jobs before startup, and read only fresh profile-specific log lines; `--clone-all` copies more than credentials.
9. **Expecting a new Telegram bot to initiate the first DM.** `getMe` and polling can succeed while `sendMessage` returns `Bad Request: chat not found`. Give the user the `t.me/<username>` link and ask them to press Start, then retest delivery.
10. **Using a scalar or JSON-looking string for Telegram config.** `platforms.telegram.home_channel` must be an object containing `platform`, string `chat_id`, and optional `name`; an integer/string scalar can crash gateway startup. Likewise, `extra.allowed_users` must be a YAML list. `hermes config set` may persist quoted JSON arguments as strings rather than structured YAML, so parse and verify both types before startup; patch `config.yaml` directly when needed.
11. **Treating service installation as runtime success.** Verify a current PID and fresh `Connected to Telegram` / `Gateway running` log lines. On macOS, `LastExitStatus` may refer to the process replaced during restart.
12. **Persisting or leaking a token shared in chat.** Configure only when requested, never echo it, set `.env` to `0600`, and tell the user to rotate it through BotFather because chat history is durable. Do not use diff-producing patch tools on secret-bearing `.env` files when adjacent lines may be included; edit internally and print only redacted verification fields. Quote `.env` values containing spaces (for example `TELEGRAM_HOME_CHANNEL_NAME="el operador GV - Content"`) so both dotenv loaders and shell-sourced verification commands parse the file safely; validate token shape/length without printing the value.
13. **Updating only one Telegram allowlist.** Keep `TELEGRAM_ALLOWED_USERS` and the config list (normally `platforms.telegram.extra.allowed_users`) synchronized, then restart and parse both to verify the same ID set.
14. **Calling a model free because it pulled successfully.** Provider catalog presence, an Ollama cloud manifest, account entitlement, and successful inference are separate checks. Do not switch Hermes until the inference probe passes.
15. **Treating a pasted SSH/Claude terminal as remotely controllable.** Test non-interactive SSH first and prefer an already-authorized key. If password auth is unavailable, explain that chat replies cannot select options in the user's separate TTY; do not ask for the root password. If a remote secret-write approval is denied, assume no write occurred, stop, close the SSH session, and wait for a fresh request instead of bypassing the denial.
16. **Treating Slack credential presence as a live connection.** `Slack ✓ configured` only proves expected variables exist. Verify fresh gateway logs or a redacted `auth.test`, then test both DM and an invited channel. For setup, channel pairing, browser-auth handoff, and transactional local-to-VPS cutover, follow `references/hermes-gateway--slack-socket-mode-setup.md`.
17. **Overstating desktop control during web setup.** If only headless browser automation is available and Google rejects it as unsafe, open the official page in the user's normal browser and pause for user authentication; never request or type passwords/2FA.
18. **Exporting an entire profile for a knowledge-only handoff.** This increases secret and configuration exposure for no benefit. Package an installable skill with curated references, manifest, validator, archive test, and checksum instead.
19. **Claiming an SCP handoff succeeded after local packaging.** Packaging and delivery are separate gates. If SSH auth fails, try known keys non-interactively, never handle the root password, and verify remote file size plus SHA-256 after a successful upload.
20. **Treating an open SSH port as a healthy SSH service.** A TCP connection to port 22 does not prove banner exchange, authentication, or command execution. Preflight with non-interactive SSH; a banner timeout is a destination `sshd`/load/network-path problem, not a credential failure.
21. **Assuming profile export includes everything needed on another host.** Inspect the archive. Provider auth and `.env` may be omitted, while stale runtime state may be present; external repositories and absolute source-host paths must be relocated explicitly. Follow `references/hermes-profile--cross-host-migration.md`.
22. **Automating cross-host dispatch before proving ownership and handoff.** First establish one Telegram gateway owner and complete one manual Issue → branch → PR cycle. A successful `gateway stop` message or stale service metadata is not shutdown proof; verify live process/service state before activating the other host. Follow `references/hermes-profile--cross-host-github-worker-coordination.md`.
23. **Treating a scoped specialist profile as a normal clone.** `--no-skills` cannot be combined with clone flags, and copying `config.yaml` can import unrelated MCP registrations that trigger OAuth during smoke tests. Create fresh, copy selectively, sanitize messaging/runtime state, remove unrelated MCPs, then verify one skill-loaded chat. Follow `references/hermes-profile--research-backed-domain-specialist.md`.
24. **Treating a Hermes runtime backup as a source-code backup.** Preserve customized core files separately in a reviewed, secret-free Git branch, honor the user's repository visibility choice, and port changes onto a clean upstream worktree. Never change public/private visibility against an explicit instruction; a public branch requires review of all outgoing history, not just the staged diff.
26. **Following symlinks during a state backup.** A link inside a profile can expand the copy into the user's home or another unrelated tree. Preflight with `lstat`, preserve links without dereferencing, and stop on unexpected growth. A partial copy is not a validated backup; remove only the exact generated artifact with authorization, never a resolved link target or prior backup.
25. **Bundling approval-sensitive Git rewrites with safe maintenance work.** Keep `push --force-with-lease` in its own approval boundary; a denial may block every command in the batch. Prefer a new immutable branch, assume denied commands made no change, and define gateway restoration or explicit maintenance-mode reporting before quiescing. Follow `references/hermes-core--safe-upgrade-with-local-customizations.md`.

## Verification Checklist

Before declaring success, verify the relevant items:

- [ ] Workspace/profile directory exists.
- [ ] Required docs/profile files are present.
- [ ] Profile appears in `hermes profile list` when applicable.
- [ ] `.env.example` uses placeholders and `.env` has no accidental borrowed secrets.
- [ ] Telegram token passed a redacted `getMe` check before gateway start; if not, status is explicitly “configured, not activated.”
- [ ] Telegram/WhatsApp allowlist and home channel are correct when runtime is expected.
- [ ] Cloned non-target platforms/webhooks are disabled and inherited cron jobs are audited before startup.
- [ ] A scoped specialist profile has no unrelated MCP registrations, and its one-shot smoke test completes without an auth prompt.
- [ ] Research-backed specialists have per-source evidence, a dated synthesis, refresh targets, an umbrella skill, and an evidence-map pointer wired into `SOUL.md`.
- [ ] Gateway status and fresh target-profile logs match the reported state.
- [ ] For core upgrades, the candidate was built from clean upstream in isolation, all customizations and tests passed, the Git bridge contains no runtime state/secrets, approval-sensitive rewrites were isolated from safe checks (or avoided with a new immutable branch), and only previously active gateways were restarted.
- [ ] For a new Telegram bot, the user pressed Start and outbound delivery was retested; otherwise report the exact pending manual step.
- [ ] Specialized skills are class-level and wired into `SOUL.md`.
- [ ] Package/ZIP exists and contains the expected tree.
- [ ] User-facing handoff states what is installed, where it lives, current status, and the one next action.

## Support Files

Use `references/` for concrete launch/package examples and provider quirks copied from prior sessions. Keep this SKILL.md focused on the class-level lifecycle.

- Isolated Telegram clone hardening, inherited cron audit, fresh-log verification, and first-contact handshake: `references/hermes-profile-operations--isolated-telegram-profile-hardening.md`.
- Secure local BotFather-token handoff using hidden input, `getMe`/`getWebhookInfo`, atomic `0600` `.env` writes, and meaning-vs-production specialization guidance: `references/hermes-profile-operations--secure-local-telegram-token-handoff.md`.
- Installing and validating a third-party plugin inside one target profile, including build/convert prerequisites and lazy specialist-router verification: `references/hermes-profile--profile-local-plugin-installation.md`.
- Slack Socket Mode setup, verification, and browser-auth handoff: `references/hermes-gateway--slack-socket-mode-setup.md`.
- Third-party Hermes messaging plugin review before installation, including relay trust, public-profile tool exposure, isolated tests, and production gates: `references/hermes-third-party-messaging-plugin-evaluation.md`.
- Packaging a small class-level skill ecosystem with architecture docs, a shared task schema, stdlib validation, private-by-default GitHub publication, remote-HEAD verification, and Slack announcement evidence: `references/hermes-multiagent-skill-ecosystem-repository.md`.
- Building a research-backed, source-hashed agent knowledge workspace inside an existing project while deliberately deferring Hermes profile activation: `references/hermes-project-ops-launch--research-backed-agent-knowledge-workspace.md`.
- Creating a specialized profile that is callable through an orchestrator while using a shared Slack coordination channel without duplicating gateway credentials: `references/hermes-profile--shared-slack-coordination-channel.md`.
- Building a knowledge-only Hermes handoff as a secret-clean installable skill pack with curated references, manifest, validator, ZIP test, checksum, and SCP verification: `references/hermes-knowledge-skill-transfer-pack.md`.
- Migrating a full Hermes profile between hosts with archive inspection, SSH/banner preflight, checksum verification, external-path relocation, destination re-authentication, and transactional gateway cutover: `references/hermes-profile--cross-host-migration.md`.
- Coordinating an always-on Hermes orchestrator and another host through GitHub Issues, worker/state labels, per-Issue branches, PR evidence, and single-owner Telegram cutover: `references/hermes-profile--cross-host-github-worker-coordination.md`.
- Creating a scoped, research-backed domain specialist with `--no-skills`, selective config reuse, MCP sanitization, auditable sources, an umbrella skill/evidence map, SOUL wiring, and a clean one-shot smoke test: `references/hermes-profile--research-backed-domain-specialist.md`.
- Creating a repository-grounded codebase specialist with a pinned checkout/commit, selective provider auth, one local skill plus architecture/operations references, and a source-citing one-shot verification: `references/hermes-profile--repository-grounded-codebase-specialist.md`.
- Updating Hermes safely when the core has local customizations, using separate runtime/code backups, a private Git bridge, clean upstream worktree, isolated verification, transactional activation, and two-layer rollback: `references/hermes-core--safe-upgrade-with-local-customizations.md`.
