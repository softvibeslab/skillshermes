# Research-backed domain specialist profile

Use when a user wants a dedicated Hermes expert whose operating context comes from a supplied source corpus.

## Known-good sequence

1. Create a fresh scoped profile with `--no-skills`; do not combine it with `--clone` or `--clone-all` because those modes are mutually exclusive.
2. If the specialist needs the default model/tool setup, copy only the required config/auth material. Do not copy messaging tokens, home channels, cron state, sessions, or unrelated gateway identity.
3. Audit inherited `config.yaml` before the first chat. A copied config can carry unrelated MCP server registrations; remote OAuth MCPs may open a browser or block a smoke test. Remove or disable all MCP servers unrelated to the specialist.
4. Keep the profile gateway stopped unless a separate messaging identity was explicitly requested.
5. Build an auditable research workspace inside the profile:
   - `research/<topic>/plan.md`
   - `sources.csv`
   - one `sources/NN_slug.md` per supplied source, with URL, timestamp/commit, authority, summary, limits, risks, and exact quotes
   - `findings/` for cross-source theses and contradictions
   - dated decision report
   - `refresh_targets.md`
6. Create one class-level umbrella skill for the domain. Put only operating rules and routing logic in `SKILL.md`; add `references/evidence-map.md` pointing to the research corpus.
7. Import only the upstream skills needed for the domain's first real tasks. Do not install a whole catalog merely because it exists.
8. Wire the umbrella skill and canonical report into `SOUL.md`, including evidence labels, security defaults, and rules for refreshing current claims.
9. Verify:
   - profile appears in `hermes profile list/show`;
   - expected skills appear in `hermes -p <profile> skills list`;
   - no messaging variables were accidentally copied;
   - unrelated MCP servers are absent;
   - `hermes -p <profile> doctor` passes the required model checks;
   - one quiet, one-shot chat loads the umbrella skill and returns the expected domain decision without auth prompts.

## Pitfalls

- `--no-skills` plus clone flags fails by design. Create fresh, then selectively copy.
- Copying `config.yaml` is not neutral: MCP registrations and platform/runtime settings may come with it.
- Writing a skill into another profile can trigger the cross-profile safety guard. The user must have explicitly requested that target profile; use the profile-aware operation or explicit cross-profile override, then verify the file and skill registry.
- A deep-research report alone does not specialize behavior. The umbrella skill and `SOUL.md` must route future tasks back to the evidence.
- “MCP-compatible” is not an end-to-end integration test. Defer installation of credentialed/beta components until the required service and authorization exist.
