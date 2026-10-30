# Project operational wiki handoff

Use this when a user asks to analyze a live project, give Hermes durable context, create a wiki, and add it to the repository.

## Minimal durable artifact set

Prefer three artifacts, reusing existing files when present:

1. `PROJECT_CONTEXT.md` — short operational identity, source-of-truth paths, live-status rules, current blockers, and report format.
2. `docs/wiki/README.md` — durable product/domain/architecture/operations map that links to existing detailed docs instead of copying them.
3. Root `README.md` — one visible link to both.

Keep volatile status as a dated snapshot. Every report must distinguish:

- **Implemented:** present in current code.
- **Documented:** claimed by plans or historical reports.
- **Verified:** reproduced now through Git, tests, APIs, or live services.

## Safe publishing from a dirty or ahead checkout

If local `main` is dirty, ahead of the remote, or contains failing code, do not push it just to publish documentation.

1. Fetch remote refs and record local/remote divergence.
2. Create a clean docs branch/worktree from `origin/main`.
3. Copy only the wiki/context/README changes into that worktree.
4. Validate links **inside the clean worktree**. A link that works in the active checkout may point to a file that exists only in unpublished commits.
5. Run `git diff --check` before the first commit. Avoid Markdown two-space line breaks because they are reported as trailing whitespace; use separate blockquote lines or a blank line instead.
6. Commit and push the docs branch; open a docs-only PR that explicitly records any red tests as project status, not as PR regressions.
7. After a branch is published, prefer a normal follow-up commit for corrections. Rewriting published history with amend/force-push requires explicit authorization.
8. Verify the remote PR and only then remove the temporary worktree.

Do not merge automatically when doing so would make an active local `main` diverge from the remote. Leave the PR open unless merge/reconciliation is part of the request.

## Link check

Run from the intended worktree, not the richer local checkout:

```python
from pathlib import Path
import re

for name in ("README.md", "PROJECT_CONTEXT.md", "docs/wiki/README.md"):
    path = Path(name)
    missing = []
    for link in re.findall(r"\[[^]]+\]\(([^)]+)\)", path.read_text()):
        if "://" in link or link.startswith("#"):
            continue
        if not (path.parent / link).resolve().exists():
            missing.append(link)
    assert not missing, (name, missing)
```

## Wiki content checklist

- Product purpose and minimum outcome.
- Canonical repo/workspace/channel/environment links.
- Roles, permissions, and governance decisions.
- Architecture and primary flows.
- Data/domain map.
- Guardrails and trust boundaries.
- Current Git, tests, deployment, security, and live-service status.
- Knowledge coverage and editorial gaps.
- P0/P1/P2 backlog and pilot gates.
- Mandatory status-report format for Hermes.

## Channel handoff

Post one short channel update containing:

- wiki/context paths;
- remote PR URL;
- current semaforo;
- root blocker;
- next priority;
- instruction to revalidate live state before reporting.

Never paste credentials, tokens, personal data, or historical service claims as current truth.
