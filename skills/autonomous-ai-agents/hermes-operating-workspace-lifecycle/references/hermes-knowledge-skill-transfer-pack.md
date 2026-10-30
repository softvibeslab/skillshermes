# Portable Hermes knowledge-skill transfer packs

Use this when the user wants to transfer domain/project knowledge to another Hermes without cloning a full profile.

## Choose the smaller artifact

Prefer a **skill pack** over `hermes profile export` when the target only needs knowledge, tone, operating rules, prompts, or workflows. A profile export is appropriate only when runtime configuration, memories, gateway wiring, or tool settings must move too.

## Minimal portable shape

```text
<pack>/
├── SKILL.md
├── README.md
├── IMPORT_PROMPT.md
├── manifest.json
├── references/
│   ├── knowledge/
│   ├── core/
│   ├── commercial/
│   └── website/
└── scripts/
    └── validate_pack.py
```

- `SKILL.md`: class-level trigger, identity, source priority, evidence rules, and known status.
- `references/`: curated source documents; exclude caches and duplicate builds.
- `IMPORT_PROMPT.md`: fallback instructions when the recipient cannot install skills.
- `manifest.json`: version, skill name, included paths, intentional exclusions, missing sources.
- `validate_pack.py`: stdlib-only required-file and possible-secret check.

## Build sequence

1. Search before writing; reuse the strongest existing agent/knowledge workspace.
2. Curate source material instead of copying the whole project.
3. Keep historical plans and projections, but mark them as non-verified status.
4. Exclude `.env`, tokens, credentials, sessions, gateway config, Graphify caches, deployment archives, images, and repository copies unless explicitly required.
5. Write one class-level `SKILL.md`; keep domain/session detail under `references/`.
6. Validate required files and scan for likely secrets.
7. Create the ZIP from inside the pack root so `SKILL.md` lands at the archive root.
8. Test the archive with `unzip -t`.
9. Generate a SHA-256 sidecar and report both absolute paths.

## Recipient install

```bash
mkdir -p ~/.hermes/skills/<skill-name>
unzip <pack>.zip -d ~/.hermes/skills/<skill-name>
```

Then start a new session and use:

```text
/reload-skills
/skill <skill-name>
```

or:

```bash
hermes -s <skill-name>
```

## Verification contract

Do not report transfer readiness until:

- validator exits zero;
- no required source is missing;
- secret scan is clean or every hit was manually resolved;
- `unzip -t` passes;
- the archive opens with `SKILL.md` at its root;
- SHA-256 was generated with a checksum tool.

## SCP handoff

When copying to another server:

1. Try the requested `scp` command.
2. If authentication fails, retry only with known local SSH keys using `BatchMode=yes` and `IdentitiesOnly=yes`; do not trigger repeated password prompts.
3. Never ask for, type, or handle the root password.
4. Report which keys were attempted and give the user the exact local `scp` command to run interactively.
5. After successful upload, verify remotely with `ssh ... 'stat ... && sha256sum ...'` before claiming delivery.

An authentication failure is transient server setup state; preserve the reusable pattern above, not a claim that SCP or the host is broken.
