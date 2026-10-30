# Repository-grounded codebase specialist

Use this recipe when the user wants a dedicated Hermes profile that becomes an expert in one source repository, but does not yet need the repository's heavyweight runtime installed.

## Minimal construction

1. List existing profiles and verify the remote/default branch before writing.
2. Clone the requested repository into the user's established project workspace; preserve the checkout unchanged.
3. Read the README, package metadata, dependency manifests, entrypoints, core modules, examples, and tests. Trace the primary execution flow and record contradictions between docs and code.
4. Create a fresh scoped profile:

```bash
hermes profile create <slug> --no-skills --description "..."
```

`--no-skills` is mutually exclusive with `--clone` and `--clone-all`. Do not fall back to cloning the whole default profile.

5. Configure only the required runtime values:

```bash
hermes -p <slug> config set model.default <model>
hermes -p <slug> config set model.provider <provider>
hermes -p <slug> config set terminal.cwd /absolute/repo/path
```

If the selected provider uses profile-local OAuth state, selectively copy only `auth.json` with mode `0600`. Leave `.env` absent unless a required non-messaging credential is actually needed; never copy Telegram/Slack/WhatsApp tokens for a CLI-only specialist.

6. Write a concise `SOUL.md` that names the canonical checkout and pinned commit, requires source inspection before API claims, separates code/README/upstream/inference, and requires file/line citations.
7. Add exactly one profile-local expert skill. Keep durable architecture and operational detail in `references/architecture.md` and `references/operations.md`, not in an oversized SOUL.
8. Record verified compatibility gaps and dependency omissions found in the source. Do not install large parsers, models, GPU stacks, or external services merely to make the profile knowledgeable.

## Verification

Run all of these before saying the profile is ready:

```bash
hermes profile show <slug>
hermes -p <slug> skills list
python3 -m compileall -q <package-dir>
git -C /absolute/repo/path status --short
git -C /absolute/repo/path rev-parse HEAD
<profile-alias> chat -Q -q "Inspect the local code and explain one core flow plus one verified inconsistency. Cite files and lines; modify nothing."
```

The one-shot answer must use the repository, cite correct locations, and avoid inventing runtime results. Compilation verifies syntax only; it does not prove optional integrations or models work.

## Pitfalls

- Installing a large dependency tree before a real execution task exists.
- Treating README marketing as implementation truth.
- Copying the default `.env` and accidentally cloning messaging identities.
- Claiming expertise because files exist without running a source-grounded one-shot question.
- Letting `compileall` artifacts dirty the checkout; confirm `git status --short` is empty or only expected changes remain.
- Updating the checkout without also updating the pinned commit and architecture references.
