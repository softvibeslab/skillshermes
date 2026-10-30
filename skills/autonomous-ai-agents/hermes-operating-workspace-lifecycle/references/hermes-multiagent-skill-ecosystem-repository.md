# Multiagent Skill Ecosystem Repository

Use this pattern when the user wants a reusable repository that packages several related Hermes skills plus the operating architecture around them.

## Repository shape

```text
README.md
.gitignore
docs/
  ARCHITECTURE.md
  OPERATING_MODEL.md
schemas/
  task-envelope.schema.json
scripts/
  validate.py
skills/
  <class-level-skill>/SKILL.md
```

Keep the skill set small:

1. One class-level orchestration umbrella.
2. Companion skills only for genuinely distinct operating questions.
3. Session/project details in `references/`, not narrow skill names.
4. Shared transport contracts under `schemas/` rather than duplicated prose.

## Architecture boundary

- Slack: human conversation, approvals, summaries.
- GitHub Issues/PRs: durable tasks, decisions, and reviewable changes.
- Repositories/docs: canonical project context.
- HMAC webhooks: machine-to-machine transport.
- Orchestrator: routing and portfolio view.
- Specialist: execution through its existing workflow.

Use a stable task envelope with `task_id`, project, objective, owner, status, acceptance criteria, inputs, constraints, evidence, return target, and next action. Require idempotency for repeated `task_id` values.

## Creation workflow

1. Search local and remote destinations before creating the repository.
2. Confirm GitHub authentication without exposing credentials.
3. Author architecture and operating-model docs before writing companion skills.
4. Make every skill name class-level and every description begin with a useful trigger such as `Use when ...`.
5. Add one stdlib validation script that checks:
   - frontmatter boundaries;
   - skill directory/name match;
   - required description;
   - non-empty body;
   - JSON schema syntax and core required fields.
6. Run a lightweight secret scan over tracked content.
7. Commit locally, create the remote, push, and verify local HEAD equals remote `main` HEAD.
8. If visibility was not specified and the material contains internal operating architecture, use a private repository as the safe default and report that choice.
9. When asked to announce it in a named Slack channel, resolve the target first, send the repository link plus a compact contents summary, and retain the returned channel/message ID as delivery evidence.

## Minimum verification

- Validator passes.
- Working tree is clean.
- Secret scan finds no credentials or private keys.
- Remote repository URL and visibility are confirmed.
- Remote `main` matches local HEAD.
- Slack announcement returns success and a message ID when requested.

## Pitfalls

- Copying every existing Hermes skill into the new repository instead of packaging only the new ecosystem-specific skills.
- Creating one skill per session artifact instead of one umbrella plus references.
- Treating Slack as the durable state store or bot-to-bot transport.
- Reporting “published” after a push without checking remote HEAD.
- Making internal architecture public merely because visibility was omitted.
