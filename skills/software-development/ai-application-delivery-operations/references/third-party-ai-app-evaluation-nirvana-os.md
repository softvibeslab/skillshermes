# Nirvana-OS engine installation notes

Use these details when evaluating or installing `gutomec/nirvana-os-engine`; keep the general workflow in `third-party-ai-app-evaluation.md`.

## Safe install boundary

- Clone separately and install from the audited checkout when the request names the GitHub repository. Record both commit and `skills/VERSION`; upstream README badges, prose, and npm package versions may disagree.
- Runtime is Bun-only. Install Bun first, then use `bun install --frozen-lockfile` and `bun audit` before system integration.
- The source installer writes to `~/.nirvana`, `~/.local/bin`, runtime skill directories, shell PATH files, and runtime settings. It also creates empty `~/squads` and `~/businesses` libraries.
- For Hermes, prefer the bridge without per-tool hooks unless the user explicitly wants them:
  `bun scripts/install.ts --no-starter --with-hermes --no-hermes-hooks`
- The shared installer may still wire its standard audit hooks into other detected runtimes and may create Gemini/Antigravity settings files. Report these side effects.

## Verification chain

```bash
bun install --frozen-lockfile
bun audit
bun scripts/install.ts --dry --no-starter --with-hermes --no-hermes-hooks
bun scripts/install.ts --no-starter --with-hermes --no-hermes-hooks
nrv install --check
nrv validate
bun test skills
hermes config check
hermes skills list
```

A full source test run can fail before installation because tests resolve canonical modules through installed runtime skill paths. Re-run the full suite after installation; treat the post-install result as authoritative while still reporting the pre-install dependency on global paths as a test-isolation weakness.

## Known installer pitfall

In the observed 0.8.1 checkout, `--dry` still copied CLI dispatchers because `copyBinaries()` did not honor the dry flag. Therefore snapshot/check `~/.local/bin/nrv*` before previewing and verify actual filesystem state afterward. A dry-run claim is not proof of no writes.

## License and product boundary

The SUL v1.0 is source-available, not OSI open source. Internal business use is allowed; offering the engine itself as paid SaaS/PaaS/managed hosting requires a separate commercial license. Keep the engine as an internal orchestration layer unless legal review approves broader distribution or hosting.
