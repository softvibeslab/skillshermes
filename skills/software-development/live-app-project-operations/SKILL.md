---
name: live-app-project-operations
description: "Use when operating a specific deployed application/project: locating repos and docs, verifying environments, checking live APIs, handling demo credentials, inspecting seeded data, and turning operational state into concise user-facing answers."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [project-operations, live-api, environments, demo-credentials, FastAPI, CRM, revenue]
    related_skills: [github-repo-management, systematic-debugging]
---

# Live App Project Operations

## Overview

Use this umbrella when the user asks about a live app or project instance rather than general code structure: environment URLs, demo credentials, health, live API data, seeded tenants/users, deployment quirks, or a sales/demo path. Keep project-specific facts in labeled subsections and references so the skill remains class-level while still preserving operational knowledge.

This absorbs the former narrow `rovi-crm-operations` skill as the first project subsection.

## When to Use

- User asks for current URLs, preview/dev/prod status, health checks, or demo credentials for a known project.
- User asks to inspect live CRM/business data through API endpoints.
- User asks for association/member/customer/tenant lists from a deployed app.
- User asks how to demo, sell, monetize, or prepare a revenue sprint for an existing live app.
- User asks about a project with known local repo path and deployment docs.
- User asks to launch a multi-stage AI job (graph build, simulation, report generation) in a locally running application.
- User asks for a local, live operations dashboard over CLI-driven systems, agent profiles, sessions, cron jobs, or Kanban state.
- User asks Hermes to identify a project from its messaging-channel name, add project context, verify status, and establish a repeatable channel report.
- User asks for a lightweight project dashboard to consult and review contracts, NDAs, or other editable operational documents.
- User asks to publish a prebuilt static dashboard or document portal to an existing Hostinger website and verify the live routes/artifacts.
- User asks to add or publish terms, privacy, acceptable-use, or another legal page on an existing static site.
- User asks to consolidate multiple static-site variants, media, design research, and origin knowledge into a GitHub workspace plus Wiki while keeping the live deployment intact.

For channel-based project onboarding, follow `references/project-channel-context-handoff.md`. For static legal-document review dashboards, follow `references/static-contract-review-dashboard.md`. For Hostinger static publishing, follow `references/hostinger-static-dashboard-deployment.md`. For adding legal routes to an existing static site, follow `references/static-legal-page-publishing.md`. For multi-variant static workspaces with a separate knowledge base and GitHub Wiki, follow `references/static-multivariant-workspace-knowledge-wiki.md`. For installing a self-hosted local dashboard plus database-backed agent bridge, follow `references/self-hosted-local-dashboard-installation.md`.

Do not answer from memory when live state matters. Re-query docs and APIs first. For read-only local dashboards, use the minimal and safe pattern in `references/local-read-only-operations-dashboard.md`.

## Preserve an approved local version without publishing

When el operador selects exact localhost routes as the version to keep, treat those routes—not the newest alternate design—as the acceptance target. A later “stop” cancels the previous merge/deployment scope; a subsequent branch-only request does not renew it. Update the task plan accordingly.

- Resolve the serving checkout and Git root (which may be a parent monorepo), record dirty state, and compare served HTML, shared scripts and canonical data with disk and candidate commit. Static equality proves only the compared files; do not infer backend or database equality from it.
- If the approved files and required backend already belong to a verified commit, create and push a named branch from that commit without checkout, staging, or an unnecessary new commit. Preserve unrelated dirty work. If they differ, review and commit only the requested scope, using an isolated worktree when needed.
- Validate existing business behavior with disposable databases and focused browser checks. Distinguish backend tests, guest-route smoke checks, authenticated browser journeys, and full multi-engine audits; one does not prove the others. Never exercise rewards or migrations against production data for a backup request.
- Verify the remote branch hash, then report its URL, evidence scope, and whether merge/deployment occurred. A source branch is not a backup of live member data.

See `references/approved-local-version-preservation.md` for the branch-only recipe and a screenshot/emulation diagnostic from responsive testing.

## Read-only process and memory observation

When adding process telemetry to an existing dashboard, preserve its API and sampling architecture and keep collection strictly read-only. Read the server, UI, inventory collector and README first. Respect explicit local-files-only / parent-owned deployment scope: do not SSH, deploy, restart services or change permissions to improve coverage. Keep the requested UI language and return exact changed paths and runnable test output.

Treat process names, arguments, environments and cgroup paths as potentially sensitive. Publish only safe display labels and inventory-recognized profile/service names; do not echo arbitrary values or raw read errors. Attribute profiles only from HERMES_HOME or explicit --profile evidence, retain unknown/conflicting states, and label ancestry as inferred rather than proven. Never infer agent counts or safe-to-stop status from process counts, age, apparent idleness or duplication. Explain RSS sharing/double-counting and unknown swap, and provide a review checklist without mutation controls.

Use synthetic /proc fixtures for parsers, permissions/exits, ancestry, secret non-emission and sampling-cache boundaries. Distinguish these checks and simulated JavaScript rendering from Linux runtime or browser verification. See `references/privacy-preserving-process-observation.md` for the stdlib payload, parsing offsets, PID-race checks and regression recipe.

## Existing-dashboard onboarding and setup flows

Use this umbrella also when adding onboarding or a setup home page inside an existing authenticated dashboard. Read the router, navigation, theme/locale conventions, API/query consumers, clipboard/URL helpers, and test setup before editing. Preserve auth/backend boundaries and unrelated dirty work; reuse established helpers instead of adding parallel infrastructure.

Keep manual browser-local checklist progress separate from verified server state. Selecting a step, visiting a destination, or copying example code does not prove configuration succeeded. Label manual progress and browser/account scope explicitly, validate stored booleans, handle storage failure, and reset only the owned checklist. Show only API-grounded counts with loading/error states; registered credentials do not establish validity or quota. Example snippets should use placeholders, never retrieve secrets unnecessarily, and provide accessible success/failure feedback.

Honor explicit parent-owned install/build boundaries: run only authorized focused checks using available dependencies, and return exact changed paths plus remaining concerns. Do not equate unit/typecheck success with responsive visual or deployed-browser verification. Keep requested page language and styles scoped, and check both mobile navigation and desktop header fit when adding home.

See `references/existing-dashboard-onboarding.md` for the React integration sequence, truthful gateway copy, safe persistence/snippets, and React Query/Vitest asynchronous rendering test pattern.

## Offline recovery and immutable staging

For interrupted jobs and accepted recovery policies, use `references/offline-recovery-sqlite-policy.md`. This is an explicit exception to this skill's live-health/API defaults: when the user restricts scope to OFFLINE, do not probe endpoints, start services/jobs, call models, or install dependencies. Respect the requested timebox and keep changes to the smallest policy script, tests, and report; do not expand into frontend work or a continuation runner.

- Read existing preparation reports/scripts/tests and actual database schema plus consumers before choosing a repair. Preserve original and sealed-preparation manifests; write only an independent new copy.
- Preserve committed actions. Mark an accepted incomplete round `partial` in a new append-only recovery event, never as a fabricated successful round end. Record last fully completed round, next round, target, no-replay decision, and approximate clock/downtime assumptions separately.
- Inspect every foreign key, including empty child tables. Physical `integrity_check` success is not referential integrity; missing parents and incompatible parent keys may mask other orphan rows.
- Compare complete table row multisets, rowids where applicable, and sequence state, not merely counts. Do not manufacture parent records or delete historical rows to obtain a green check.
- Separate staging verification from readiness: a verified immutable staging package may honestly contain recorded blockers, but readiness must fail closed on FK violations or an untested continuation runner. Do not weaken a failed readiness assertion and describe the result as a full recovery success.
- Tests must block network and model execution, reject overwrite/tampering/duplicate events, validate accepted boundaries and actual key enforcement on disposable copies, and reverify protected hashes. Final delivery: concise status, exact blockers, absolute artifact paths, and runnable verification commands with expected failure exits.

### Executable continuation after recovery approval

When the user explicitly advances from policy staging to implementing an actual continuation runner, do not preserve a stale staging-only scope or deliver another blocker-only staging package. Separate implementation/offline testing from permission to launch: if the parent owns launch, deliver the exact runnable command and do not call paid models yourself. Respect explicit clone-only, original-configuration, timebox, and no-frontend/no-dependency constraints.

- Reuse the original runner's model factory, profiles, scheduling, actions and environment loading; hydrate existing identities without reset/signup/seeding.
- Approved quarantine is a narrow exception to historical-row preservation: export full rows durably first, delete only the explicitly authorized operational-copy rows transactionally, and prove every other row unchanged plus FK/integrity clean.
- Keep sealed evidence separate from the operational verification contract. Persist accepted partial/no-replay boundaries and approximate history/clock assumptions in new artifacts, never rewritten historical logs.
- Require an exclusive process lock and durable pending checkpoints before dispatch. Fail closed on ambiguous results; single-use continuation must reject automatic restarts after a run has begun.
- Framework errors may be returned rather than raised. Detect those and worker failures; cancel and await owned sibling tasks before closing DBs to prevent late writes. Async timeouts do not preempt synchronous blocking code.
- Verify with network-blocked mocks over disposable DBs and actual hydration where possible. Report exactly what was tested, what remains unverified remotely, and the new checkpoint/action-log paths.

See `references/conservative-continuation-runner.md` for implementation order, minimal regression checks, OASIS concurrency/trace pitfalls, and the historical MiroFish recovery parameters.

## Reuse-first pilot kickoff

Also use this umbrella when turning an existing product portfolio into a new MVP and repository with initial SPECS. Keep discovery bounded to the proposed user journey, not an exhaustive inventory of every project.

- Recover prior decisions first. If session search is empty, inspect known project documents; an empty search does not prove the idea or assets do not exist.
- Classify reuse evidence explicitly: repository discovered, relevant source inspected, locally tested, or integration verified. Repository descriptions, directory listings, and README promises identify candidates, not working integrations.
- If a README endpoint is missing or contains only a placeholder, inspect the root listing and relevant entrypoints/manifests rather than concluding the project has no usable implementation. Check the API request succeeds before decoding its content; a successful final pipeline command can hide a failed upstream request.
- Separate deliverables: repository + draft specifications, interactive prototype, operational concierge pilot, and integrated application. Never silently replace a requested working MVP with documentation or call a manual pilot a built app.
- A spec-approval gate blocks implementation, not authorized drafting or repository setup. Prepare the actual spec and its acceptance criteria for review; never mark it approved on the user's behalf. Clearly identify any requested implementation still pending approval.
- Reuse only reviewed source/assets, not whole workspaces or credential-bearing archives. Keep secrets, customer exports, and unrelated profile backups out of the new repository.
- Distinguish a project repository from a GitHub Projects board. Do not expand permissions just to obtain a board; when a board is optional, use an authorized repository backlog and report that distinction.
- An explicit tool denial stops the affected workflow, including equivalent requests through another surface. A later skills-review request authorizes skill maintenance only, not resumption of repository creation.

See `references/reuse-first-pilot-kickoff.md` for the minimum artifact set and verification gates.

## Class-Level Workflow

1. **Locate the project**
   - Identify local repo path and remote.
   - When the user only remembers an approximate name or shares a screenshot, extract visible clues first: browser title, localhost route/port, repository tab, app branding, IDs, and terminal text. Search exact and near-name variants; do not assume the user's spelling is the repository name.
   - If normal project-name search misses, use browser history for the visible localhost URL/title, then shell history for clone/start commands. Use the recovered remote/name to search likely workspace roots, and compare duplicate clones by remote, dirty state, and modification time before declaring which copy is active.
   - Read project instructions (`AGENTS.md`, `CLAUDE.md`, deployment docs) before running commands.
   - Check `git status --short` before editing; avoid mixing unrelated local changes.

2. **Verify environments before reporting**
   - Health endpoint(s).
   - Frontend/backend direct URLs.
   - HTTPS/certificate caveats.
   - Demo credential login status.

3. **For multi-stage jobs, verify every stage**
   - Distinguish app health from job state: service running, input accepted, intermediate artifact built, job prepared, job actually running, and job completed are separate claims.
   - Preserve returned project/task/job IDs and poll the documented status endpoint to a terminal state.
   - Add a quality gate before expensive downstream stages; HTTP 200 with generic or empty AI-generated structure can still be a degraded result.
   - Verify final execution through advancing rounds/events/actions, not only a `ready` flag.
   - After a service restart, treat persisted `running` flags as unverified: compare update timestamps and confirm the recorded worker PID belongs to the expected process, then check for advancing progress. Service recovery does not prove worker recovery.
   - When given a report URL, resolve its report → simulation association and compare report completion time with the latest run start time. A completed report can belong to an earlier run of the same simulation ID; never present it as the latest run's final result.
   - Keep service startup separate from simulation execution: permission to start the application does not authorize restarting a paid simulation or regenerating its report.

4. **Use live API checks for live data and capability claims**
   - Authenticate through the documented login endpoint.
   - Reuse a session/token rather than guessing from static docs.
   - Query the smallest endpoint set needed for the user’s request.
   - Include only requested fields unless the user asks for export/detail.
   - Before telling a user how to perform an action from a public dashboard, verify the rendered control, frontend API call, backend route, and persistence path. Label the operation as UI-supported, API-only, static configuration, or absent.
   - Keep “agent” and “skill” distinct: a skill specializes an existing runtime; a new agent needs independent identity/runtime, tools, memory, and lifecycle. See `references/authenticated-local-agent-dashboard-publication.md`.

5. **Report concisely**
   - Prefer bullets over tables for chat/Telegram-style delivery.
   - Include URLs, credential status, roles/scopes, counts, and requested records.
   - Label anything stale or reference-derived as a starting point, not current truth.

### Capability catalogues and DNS-gated VPS publication

- Separate catalogue selection, skill installation, process activation, and verified integration. A persisted “selected pilot” is not an activated application; when activation was requested, selection-only staging is partial delivery, not task completion.
- Separate the DNS provider from the application host. Verify authoritative A/AAAA records, the actual SSH destination, occupied ports, and existing proxy vhosts before changing infrastructure. Recover documented SSH identity/username from project docs or session context before asking the user to repeat them; never recover passwords from history.
- When DNS/TLS setup is pending, continue safe authorized staging: bind the backend to loopback, run as an isolated unprivileged service, and fail closed on public app routes. Do not expose plaintext Basic Auth as a temporary workaround.
- An existing HTTPS host with a private subpath can be proposed as an alternative publication target, but do not silently substitute it for the requested domain. Confirm the changed target when it changes the approved scope, then verify that the exact subpath, APIs, and assets inherit the intended authentication boundary. Until verified, label its URL as proposed, not live or secure.
- A clarification timeout is not user consent. In particular, a tool's generic “use best judgement and proceed” fallback cannot renew a denied deployment or verification action. Keep that action paused until the user explicitly authorizes the scope; report the pending decision once without repeatedly prompting or attempting equivalent commands.
- Gate publication on valid TLS, unauthenticated rejection across UI/API/assets, authenticated success, CSRF/Origin rejection, and actual browser persistence. Unit tests plus backend health do not establish browser or public readiness.
- If a delegated implementation times out, inspect its artifacts before retrying. Partial files may exist; read and test them independently instead of assuming success or starting a duplicate implementation.
- Treat an explicit tool result such as `BLOCKED: User denied this command` as withheld authorization, not an SSH/filesystem permission error or a transient deployment failure. Stop the denied deployment or verification workflow; do not split, rephrase, or route the same action through another tool. A subsequent request to review documentation or update skills does not renew deployment consent. In the handoff, distinguish authorization denied, execution failed, and executed but unverified; describe the command as blocked rather than asserting an independently verified remote state.
- When the user explicitly renews a denied deployment request (for example, “continúa”), distinguish renewed conversational authorization from the execution tool's approval gate. Recheck read-only prerequisites if state may have changed, then submit the authorized operation through the normal gate. A new denial stops that workflow again; do not bypass it. Report the gate's actual result without assuming the user saw a particular approval dialog or claiming that the chat authorization was invalid. Do not promise that a specific UI approval mechanism exists unless it was observed.
- A denied compound command does not prove its staging, upload, installation, or service steps ran. Keep earlier successful read-only findings separate from the blocked operation, and never promote prepared command text to migration evidence. For a later authorized resume, inspect actual local and remote state before rerunning non-idempotent creation or copying SQLite over an existing database. Preserve the source database and encryption key; use SQLite's backup API rather than a live file copy, and validate the snapshot before migration.
- If verification is denied, stop that workflow rather than retrying through another tool or command. Report exactly which checks were denied; a blocked shell probe is not a browser test. Preserve previously observed evidence with its provenance, but after context loss treat earlier completion summaries as reported history, not independently verified current state. Keep remaining activation/integration requirements visible even when publication succeeded.

### Caddy TLS recovery without premature publication

When DNS is correct but HTTPS fails during the handshake, inspect both Caddy's imported site files and its active configuration before blaming DNS or certificates. A running listener on 443 does not establish that the requested hostname is configured. Inspect only relevant host blocks and sanitized service metadata; avoid dumping full proxy configs, which can contain password hashes, authorization headers, and unrelated private routes.

If the hostname is absent and deployment is authorized, add a dedicated site fragment under an already-imported directory, validate the complete configuration, then reload rather than restart Caddy. Preserve unrelated sites. Until application authentication is ready, the new HTTPS vhost may return a deliberate maintenance 503 for every path, with no backend exposure. If validation/reload fails, remove or restore only the owned fragment so invalid staging does not remain for a future reload.

Verify TLS with normal certificate verification (never `curl -k`), and separately record the HTTP status. A valid HTTPS maintenance response proves TLS recovery, not dashboard publication or authentication readiness. Avoid `curl --retry` for an expected maintenance 503: it retries the intentional response; use a single request or a bounded certificate-issuance check. Do not treat curl's exit code alone as HTTP success.

After TLS recovery, continue the authorized integration when feasible rather than repeatedly ending with the same remaining-work list. If a real decision or blocker prevents deployment, name it precisely. Keep remote VPS profiles distinct from Mac profiles: a VPS frontend cannot read the Mac's Hermes home without an explicitly designed private connection; never imply that domain publication supplies that connection.

See `references/caddy-tls-before-app-publication.md` for the bounded diagnostic and safe-staging sequence. See `references/dns-gated-capability-dashboard.md` for staging, finish, verification, and rollback checklists.

### Pilot acceptance and state-integrity reviews

For multi-role pilots, trace each critical UI action through request serialization, the registered route, authenticated identity, SQL predicate, and all persistence side effects. Passing tests that write directly to the database do not establish browser/API compatibility; homepage HTTP 200 does not establish acceptance readiness.

Use a disposable database, synthetic identities, and mocked outbound effects. Include two users sharing one task definition, one identity with multiple profiles, and repeated completion/approval requests. Assert per-submission isolation, profile scoping, first-transition-only rewards, consistent counters, and durable feedback/timestamps/audit records. Verify batch and individual callers against the same invariants. Keep review-only work off the real database and distinguish proposed corrections from applied fixes.

When implementing pilot corrections, protect eligibility checks and all reward/counter/audit effects in one transaction shared by individual and batch callers. Test concurrent replay, rollback/retry, and submit-versus-review races on disposable databases. Published submission IDs must survive migration and maintenance; implicit SQLite rowids are not a durable API contract. Verify actual frontend serialization separately from backend tests, without claiming a VM harness is a browser run. See the implementation checklist in `references/multi-role-pilot-contract-audit.md`.

Report the evidence level precisely: code inspection, synthetic API reproduction, browser run, or deployed end-to-end execution. An overridden authentication dependency does not prove an authentication bypass. For PR-only delivery, verify the requested base branch and remote head commit; an empty checks list means no CI checks reported, not CI passed. Do not merge or deploy without authorization.

See `references/multi-role-pilot-contract-audit.md` for reproduction recipes and historical BeGlobal-derived contract pitfalls.

### Project-channel onboarding

When the user asks to add Hermes to a project channel and give it context:

1. Resolve the project from the user's message and the actual messaging origin first. A foreground Slack/browser window may be stale or showing another channel; never use it as stronger evidence than the current chat target. Likewise, an identical prompt or completed handoff found through session search is historical evidence, not proof of the current channel's scope. If the project is still ambiguous, inspect named messaging targets and map the origin `chat_id → channel name` before posting or editing any repo.
2. Treat the channel name as a locator hint, not necessarily the repo name; search near-name variants and inspect remotes/docs.
3. Verify the real project state from git plus the live product/API before summarizing.
4. Reuse an existing dedicated Hermes profile when present; inspect its workspace and project instructions before creating anything new.
5. Put stable identity, paths, purpose, source-of-truth links, status-report format, and priorities in a repo-level `PROJECT_CONTEXT.md`. Mark live metrics as a dated snapshot and tell Hermes to re-query them.
6. Before writing scope or MVP, cross-check the dedicated profile's `SOUL.md` and durable user memory; preserve explicit platform/product exclusions and remove stale contradictory claims.
7. Update the existing repo/profile instructions to point at that file. Put the rule near the top, in the project's documentation language: read `PROJECT_CONTEXT.md` first, then re-query Git, checks, deployment/build services, and stores before any status or release claim. Remove stale operational claims discovered during verification. Re-read both files after concurrent agent activity before patching so you do not overwrite newer work.
8. Confirm whether Hermes is already a channel member before inviting it. A visible historical Hermes message proves only that the app posted there once; it does not prove current membership or profile routing. Prefer the messaging tool over desktop Slack: list targets first, address the exact named channel, and treat a successful send's returned `chat_id` and `message_id` as canonical. Write the canonical ID back to `PROJECT_CONTEXT.md`.
9. Distinguish “the Slack app is in this channel” from “a dedicated Hermes profile owns this channel.” Do not claim profile routing unless its gateway/platform configuration is verified; otherwise say only what was actually verified.
10. Verify context edits by reading them back and running the smallest available diff/syntax check before reporting completion.
11. Report the current project only unless the user explicitly asks for a batch across every project channel.

Use `references/project-channel-context-handoff.md` for a reusable context file, Slack concurrency pitfalls, and channel-message shape.

### Evidence-backed productivity dashboards and exports

When publishing operational reports reconstructed from chat and multimedia, preserve the distinction between reported activity and independently verified completion. Keep identifiers as literal strings (including leading zeros), and never attribute an image to a technician or status merely because it mentions an order. Separate contextual and historical evidence from KPI inputs.

For el operador's evidence-report dashboards, show all collapsible sections expanded by default, including technician-by-day matrices and methodology; retain individual collapse controls. Apply this preference in both the source template and generated output so regeneration preserves it. Embed requested images in the actual Excel workbook and standalone HTML, not just as links; put clearly linked evidence beside matching records and provide a separate gallery.

Publish only an explicit allowlist of reviewed, anonymized derivatives. Keep originals and OCR private, inspect image pixels rather than trusting filenames, and note that technician names and operational identifiers may remain sensitive. `noindex` and `robots.txt` discourage indexing, not access: explicitly distinguish public publication from authenticated sharing. Validate real production filters, reset behavior, image viewer, expanded defaults, console errors, and downloadable artifact parity before reporting success.

See `references/evidence-productivity-dashboard.md` for reconstruction boundaries, image/Excel handling, and a minimal publication acceptance checklist.

### Static document-review dashboards

When the user asks for a dashboard to consult a contract, NDA, or similar project document:

1. Identify the canonical draft from the actual files; do not silently pick among similarly named versions.
2. Reuse the existing project dashboard and native document conversion before adding dependencies or services. A static route with readable HTML plus the original editable download usually holds.
3. Base the review checklist on headings and unresolved placeholders extracted from the documents, and label the content as a draft rather than legal advice.
4. Keep reviewer identity human-readable inside the UI. Put platform mention syntax in the Slack/channel handoff, where it can resolve and notify.
5. Verify typecheck/build, the route, every document asset, and both document views locally.
6. Check the exact production route separately. Report **built locally, not published** when the project homepage is healthy but the new route is still 404.
7. Do not imply review state is recorded unless controls genuinely persist it.

Use `references/static-contract-review-dashboard.md` for the minimal route shape, native DOCX conversion, verification sequence, and review-message checklist.

When the user also requests a repository wiki and the active checkout is dirty, ahead, or red, publish documentation from a clean worktree based on `origin/main`; validate links in that worktree so local-only files do not become broken remote links. After publishing, use a normal follow-up commit for corrections—do not amend/force-push without explicit authorization. See `references/project-operational-wiki-handoff.md`.

6. **Revenue-first mode**
   - If the user asks to monetize, sell, create money, or prioritize revenue work, shift from technical inspection to a revenue sprint.
   - Prioritize actions that help sell, collect payment, deliver a pilot, or retain customers.
   - Do not overbuild before validating demand.
   - Keep operational and commercial state separate: `live`, deployed, public URL, or client-branded code does not prove a sale. Mark a project sold only from explicit contract, accepted proposal, invoice/payment, or CRM `closed/won` evidence; otherwise report `sale unconfirmed`.
   - When forecasting without historical close rates, present conservative/base/aggressive scenarios with visible unit, ticket, recurring-revenue, 90-day, and 12-month assumptions. Label them as models, not commitments.

## Project-specific configuration

Private operational examples were excluded from this public edition. Obtain endpoints and credentials from the authorized local configuration. Never infer demo access or privileges from this package.

## Common Pitfalls

1. **Using stale credentials** — documented demo users can drift; always recheck login before giving demo instructions.
2. **Answering from docs only** — live API checks are required for environment health and current tenant/member data.
3. **HTTPS certificate traps** — try documented HTTP endpoints when HTTPS certificate names mismatch.
4. **Over-reporting data** — for member lists, concise fields are usually name, email, company, and status.
5. **Ignoring local dirty state** — check git status before editing repo artifacts or committing.
6. **Mining ambient credentials** — never recover passwords or tokens from shell history, logs, browser profiles, or unrelated files to complete a deployment. Use the documented/configured deploy surface or obtain explicit authorization; if blocked, report `ready locally, not published`.
7. **Claiming deployment too early** — writing files locally or identifying the server is not publication. Verify the exact public route before saying it is live.
8. **Revenue requests becoming engineering tasks** — first ask whether each task helps sell, collect payment, deliver the pilot, or retain the customer.

## Verification Checklist

- [ ] Project docs/instructions were checked when a repo is available.
- [ ] Relevant health/login/API endpoints were queried live when current state matters.
- [ ] Multi-stage jobs were followed to the exact claimed stage with IDs, terminal status, and a quality check on generated artifacts.
- [ ] “Running” was verified from live progress/actions rather than inferred from preparation or HTTP success.
- [ ] Credential status is reported as verified or stale/reference-derived.
- [ ] Output includes requested URLs, roles/scopes, counts, or records.
- [ ] Any file edits/created artifacts are verified with paths and git status.
