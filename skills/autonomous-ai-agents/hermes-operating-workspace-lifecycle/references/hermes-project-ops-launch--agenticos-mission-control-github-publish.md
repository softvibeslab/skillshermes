# AgenticOS Mission Control — GitHub publish handoff

Use when a Softvibes/AgenticOS project workspace needs to be promoted from local operating folder to a GitHub repository.

## Minimal publish pattern

1. Work from the project workspace, not the Hermes profile folder.
   - Example: `/Users/USERNAME/Documents/SoftvibesLab/AgenticOS-Skool`.

2. Add repo hygiene before staging.
   - Create `.gitignore` for `.env`, `*.env`, `.DS_Store`, logs, local venvs, `node_modules`, temp/backups.
   - Add a short `README.md` with: purpose, how to open dashboard, key files, team, and secret note.

3. Secret scan before commit.
   - Scan text files for obvious token markers: `TOKEN`, `SECRET`, `PASSWORD`, `API_KEY`, `TELEGRAM_BOT_TOKEN`, `sk-`, `ghp_`, `github_pat_`.
   - Ignore binary assets; inspect any hits manually. Placeholder strings in docs/scripts are OK, real token values are not.

4. Initialize/push.

```bash
cd /path/to/workspace
[ -d .git ] || git init -b main
git remote remove origin 2>/dev/null || true
git remote add origin https://github.com/org/repo.git
git add .
git commit -m "feat: launch <project> mission control"
git push -u origin main
```

5. Verify.

```bash
git status --short
git rev-parse --short HEAD
git ls-remote origin refs/heads/main
```

## Notes

- Do not include Hermes profile `.env` or tokens in the repo.
- For a static dashboard, GitHub Pages is a later optional step, not required for first publish.
- If `gh` is unavailable, plain `git push` over HTTPS can still work if credentials are already configured.
