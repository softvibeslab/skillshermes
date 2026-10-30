# Project-channel onboarding and context handoff

Use when a team organizes work as one messaging channel per project and asks Hermes to identify the project, join the channel, understand it, and report status.

## Workflow

1. Read the current channel name and treat it as a locator hint, not guaranteed repo spelling.
2. Search likely workspace roots for exact and near-name matches.
3. Verify the selected project with its README/docs, Git remote, branch, dirty state, and recent history.
4. Identify related live systems from project docs (community, deployment, analytics, CRM, etc.) and query current state with the relevant tool/skill.
5. Check whether a dedicated Hermes profile already exists, its workspace/cwd, model, gateway state, and project context files.
6. Verify whether Hermes is already a channel participant before attempting an invitation. Do not assume the Slack app in a channel is backed by the dedicated profile; record the distinction when applicable.
7. Create or refresh a repo-level `PROJECT_CONTEXT.md` containing stable identity, purpose, local path, remote, external-system links, current stage, priorities, and a rule to re-query live metrics.
8. Add a short pointer near the top of the repo's existing instruction file (`AGENTS.md`, `CLAUDE.md`, or equivalent), using the documentation's language. The pointer must require reading `PROJECT_CONTEXT.md` before status/release claims and re-querying Git, checks, build/deployment services, and app stores. Do not duplicate the full context.
9. If the user explicitly authorized cross-profile context changes, update the dedicated profile's `SOUL.md` to point at `PROJECT_CONTEXT.md` and define the status-report format. Do not copy transient metrics into durable profile instructions.
10. Publish one concise context/status message in the exact project channel and verify the returned channel/message handle. A prior Hermes message is not enough evidence of current membership or dedicated-profile routing.
11. Read context edits back and run the smallest diff/syntax check available before claiming completion.
12. Keep project facts isolated to their matching channel/profile. Repeat the process per project rather than building one global context dump.

## Recommended channel post

- What the project is
- Current stage
- Repo/workspace and relevant live URL
- Verified advances and dated metrics
- Narrowest evidenced blocker
- Next action
- Instruction for Hermes to report: stage, advances, metrics, blockers, next action, suggested owner

## Reporting rules

- Repo state and live-service state are separate claims; verify both.
- Label metrics as a dated snapshot and re-query before future status reports.
- Correct stale setup docs when live profile/gateway state proves they are outdated.
- Preserve dirty work: do not commit, stash, or overwrite unrelated changes while onboarding context.
- Prefer a single project context file plus pointers over duplicating the same context across memory, channel posts, profile prompts, and several docs.
