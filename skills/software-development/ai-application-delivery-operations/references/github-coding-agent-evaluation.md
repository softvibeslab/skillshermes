# GitHub coding-agent integration assessment

## Evidence and inspection checklist

- Record repository URL, exact reviewed commit, dirty-tree state and whether remote freshness was checked. Use immutable GitHub blob links with line anchors; do not attach current-main links to findings from an older clone.
- Read the action manifest, entrypoint, each reachable mode, permission/token setup, model invocation and output handling. Trace callers before interpreting a helper as universal protection.
- Map each trigger and actor type to allowed operations. Separate permission to trigger from permission to write, access secrets or merge.
- Inspect all outbound model calls, including classifiers and helpers, for provider routing, payload sensitivity and billing. Do not infer them from the main model setting.
- Establish whether approval checks identify bot accounts, commit authors, event actors or configured identities. Shared human credentials weaken agent attribution; universal human review requirements may be the simpler baseline.
- Treat issue bodies, comments and PR content as untrusted. Sanitization and prompt rules are not isolation. Never combine execution of untrusted checkout scripts with privileged credentials as a convenience.
- Preserve evidence levels: documented behavior, code-confirmed behavior, runtime-tested behavior and proposal. Conditional risks are not demonstrated exploits.

## Integration decision

Start with the gap: does an existing reviewer already provide the same signal? A useful split is orchestrator → implementation worker → PR/CI → independent reviewer → human merge decision. Avoid adding another orchestrator, fork, agent profile or dashboard merely to install a GitHub Action.

Pilot one repository manually with minimal permissions and explicitly bounded tools. Use historical PRs containing known problems plus a clean control. Record useful confirmed findings, duplicates, false positives, human review effort and actual billed cost. Timeout, turns and concurrency are operational limits, not hard spend guarantees. Gate wider deployment on evidence and preserve a disable/rollback path.

## Claude Code Action: revision-dependent leads

Source: https://github.com/anthropics/claude-code-action

The prior static assessment surfaced these inspection targets; they are leads to recheck, not permanent assertions about upstream:

- Mention-driven modes may edit and commit rather than only comment.
- `agent-approval-check` depends on configured identities; human-account automation needs special attention.
- `allowed_bots: '*'` broadens activation and should not be recommended without tracing its authorization interaction.
- An auxiliary comment-classification call may route directly to Anthropic even when the primary agent uses another provider.

Revalidate each against the requested revision before recommending configuration. Do not reproduce unverified line numbers or conclude that runtime behavior was tested from a static report alone.

## Deliverable contract

Provide a report outside the clean clone: purpose, actual execution flow, incremental ecosystem value, duplication, permissions/data/cost risks, smallest pilot, acceptance measures, source citations and limits of verification. Return the report's absolute path in CLI contexts. Cloned, analyzed, installed, activated and runtime-verified are separate completion states.
