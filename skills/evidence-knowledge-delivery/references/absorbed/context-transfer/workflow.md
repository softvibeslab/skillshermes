---
name: context-transfer
description: Create and audit durable context-transfer packages between agents or sessions, especially when the source of truth is a Git repository, branch, PR, or exact commit. Use for handoffs, onboarding prompts, commit-pinned knowledge packages, and read-only reconstruction of project state.
version: 1.0.0
---

# Context Transfer

Transfer enough context for another agent to act correctly without copying whole repositories, leaking private runtime state, or confusing documentation with live product state.

## Principles

1. Reference durable artifacts by path, URL, branch, PR, and exact commit instead of duplicating them.
2. Separate the documentation snapshot from the implementation snapshot, current default branch, and live services.
3. Preserve dirty working trees; use an isolated worktree for exact-commit analysis.
4. Label every claim as implemented, documented, verified, proposed, inferred, blocked, or historical pending revalidation.
5. Treat graphs, summaries, plans, and transcripts as discovery aids unless a traceable human decision grants authority.
6. Never transfer secrets, credentials, personal identifiers, runtime databases, sessions, memory, logs, caches, attachments, or uncertain-license content.

## Workflow

1. Identify the receiving agent's next task and required depth.
2. Locate canonical artifacts and repository instructions.
3. Record repository, remote, default branch, documentation branch, PR, exact commits, and verification time.
4. If auditing GitHub state, follow [commit-pinned transfer verification](references/git-commit-pinned-context-transfer.md).
5. Read package documents in a fixed order: index, state, project context, architecture, operating model, sources, decisions, risks, glossary, handoff prompt, manifest.
6. Open original linked sources; do not trust summaries alone.
7. Validate package shape, links, manifest paths, commit scope, and authority labels.
8. Distinguish checks run now from historical test/build/service evidence.
9. Produce one self-contained prompt that points back to durable artifacts for detail.
10. End with the minimum next action, revalidation protocol, and an explicit stop condition if the receiving agent must wait for user direction.

## Output contract

Include:

- goal and product model;
- repository identity and commit relationships;
- verification timestamp and checks actually run;
- reading order and source precedence;
- architecture, roles, workflow, state, decisions, risks, and open questions;
- restricted content policy;
- next minimum action;
- instructions to fetch and revalidate before reporting mutable state.

Do not claim a PR is merged, a branch is current, a suite is green, or a service runs unless that exact fact was freshly verified.

## Verification

A handoff is complete only when another agent can answer:

- What artifact is authoritative?
- What exact product commit is described?
- What was checked now versus inherited historically?
- What is unsafe or unauthorized to copy?
- What is the next smallest action?

## References

- [Git commit-pinned context transfer](references/git-commit-pinned-context-transfer.md)
