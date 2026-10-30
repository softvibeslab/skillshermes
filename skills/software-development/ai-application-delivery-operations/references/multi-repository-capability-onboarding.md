# Multi-repository capability onboarding

## Intake and authorization

For a list of repositories intended for an agent ecosystem:

1. Normalize GitHub owner/repo URLs and deduplicate; retain all unique requested items in the inventory, even those deferred from a pilot.
2. Retrieve prior context and inspect current project registries, clones, dashboards, and adapters. Registry entries are leads, not proof of running services.
3. Record requested deliverables separately: assessment, plan, clone, implementation, installation, execution, integration, deployment. Do not infer a plan-only restriction merely from the phrase “give me a plan.” Report unfinished deliverables explicitly.
4. Use repository metadata and README for triage, then inspect actual manifests, configuration, license, entry points, and relevant code before implementation. A truncated README is not sufficient to certify compatibility.
5. Preserve existing remotes, branch state, and uncommitted work. Compare before pulling or updating an existing clone.

## Capability matrix

For each unique repository record:

- Canonical repository and inspected revision.
- Capability type: procedural skill, application, API/MCP tool, model gateway, or hybrid.
- User outcome and concrete project pilot.
- Existing overlapping capability: reuse, adapt, compare, or decline duplication.
- Runtime, external service dependencies, license obligations, data sensitivity, and cost model.
- Integration surface and target agent/editor/project scope.
- Acceptance test and rollback that preserves user data.
- Evidence maturity: documentation reviewed, source inspected, smoke-tested, integrated, or production-verified.

A job-search framework for candidates is not automatically an employer marketplace backend. A notebook application is not automatically a replacement for an existing knowledge pipeline. Test the actual workflow and domain fit, not just whether the UI opens.

## Dashboard contract

Reuse a suitable existing operations surface before introducing a new one. Verify its bridge against the installed CLI/API instead of copying commands from historical docs.

Keep independent dimensions for checkout/version, installation, process health, connection status, skill destination, and last test result. Actions depend on type:

| Type | Action | Required verification |
|---|---|---|
| Service | Start/stop/open | Health probe and ownership of the managed process |
| Skill | Install/remove in selected scope | Discovery and representative use in a fresh session |
| API/MCP | Connect/disconnect | Real query from the intended client |
| Gateway | Select route/test fallback | Successful request and controlled fallback test |
| Security runner | Execute scoped test | Explicit authorized target, isolation, evidence and cleanup |

Use fixed allowlisted command adapters, not browser-provided shell strings. Do not kill unrelated processes sharing a port. Never return secrets in dashboard logs or settings. A green toggle without verified execution is not activation.

## Hermes and Cursor adaptation

- Check current documentation and live configuration formats for each client; do not assume identical skill directories or MCP schemas.
- Review Claude-specific tools, subagent names, hooks, shell assumptions, and installation scripts before adapting a repository.
- Share portable procedure content where practical, but keep client-specific adapters and discovery checks explicit.
- Install into the selected project or profile, not every agent globally. Respect profile isolation.
- Compare proposed skills against existing ones first; improve an umbrella or add a reference when functionality overlaps.
- Maintain an optional direct model route while evaluating a gateway; avoid making an unproven proxy a global dependency.

## Pilot and promotion gates

Start with synthetic/redacted fixtures and one bounded workflow per capability. Text skills can use before/after samples; document tools must support source-grounded answers; SEO tools need an authorized test site and a real query; model gateways need request/fallback checks. Active security tools require specifically authorized targets and isolation; owning a repo is not blanket permission to scan connected production systems.

For every pilot, verify useful output, privacy boundaries, expected cost, failure behavior, and rollback before broader installation. Stop/disconnect should leave documents and user data intact.

## Reproducible clone and skill pilot pattern

1. Inventory existing checkouts by canonical remote before creating new paths. Never automatically `pull --ff-only` merely because the folder exists: preserving the evaluated revision is part of reproducibility. Record dirty state without cleaning it.
2. For a source-only intake, use a shallow clone with hooks disabled and an empty template directory, e.g. `git -c core.hooksPath=/dev/null clone --depth 1 --template= URL DEST`. Do not initialize submodules or run installers. If using `GIT_LFS_SKIP_SMUDGE=1`, explicitly label large-file assets as not downloaded; the checkout is not yet a complete runtime. Clone flags are not a sandbox for later execution.
3. Record canonical URL, absolute checkout path, commit, and separate availability/installation/runtime states. For reused repositories, “not installed during this run” is accurate; “not installed” requires inspecting prior state.
4. Audit the exact skill directory and manually read its full instructions and referenced files. A scanner PASS is scoped to those files, not the entire repository, dependencies, or behavior. Note semantic risks too: invented numerical examples, unjustified time estimates, unsupported clinical generalizations, and persistent style conflicts.
5. Copy only the reviewed `SKILL.md`, required references/evaluation files, and license into isolated destinations. Do not deploy hooks, extensions, or unrelated installers. Record source, destination, commit and SHA-256; refuse to overwrite a differing destination. Include licenses in the managed-file inventory when defining rollback.
6. For a Hermes discovery-only check, an explicitly scoped invocation such as `HERMES_HOME=/absolute/lab/hermes-home hermes skills list --source local` can inspect a sandbox without changing the shell's global home. Verify behavior against the current CLI. Do not copy operational credentials or messaging configuration. A standalone home may still need provider setup before an actual conversation can run.
7. For Cursor, use an isolated project workspace and the currently supported project-skill location. Files existing under `.cursor/skills/` do not prove the running editor discovered or invoked them. Verify separately in a fresh editor session.
8. Leave a small read-only check that verifies unique inventory entries, recorded commits, deployed hashes, source/copy equality, and evidence files. This is an integrity test, not an application smoke test.

## Evidence and cost labels for text pilots

| Evidence | What it proves | What it does not prove |
|---|---|---|
| Static audit PASS | No configured scanner findings in the scanned files | Complete security or safe runtime behavior |
| Matching hashes | Deployed content matches the reviewed source | Client discovery or invocation |
| CLI skill listing | That CLI discovers the skill in that home | A model loaded and followed it |
| Manual input/output examples | The evaluator can illustrate the criteria | Independent baseline, model A/B, or client integration |
| Fresh client session with saved output | Observed behavior in that client/configuration | Superiority over existing skills or broad reliability |

For a genuine comparative pilot, fix synthetic inputs and a rubric first, run baseline and skill-enabled conditions independently, retain raw outputs and model/client configuration, and obtain human review for voice or usability. Compare factual preservation, uncertainty, CTA/price/date preservation, full explanations, safety boundaries, and disabling persistent modes. Never write both sides yourself and label it a measured A/B improvement.

“No application-provider calls” is narrower than “zero cost”: delegation and agent inference can still consume tokens. Do not claim no paid calls or a zero-cost session without usage evidence. For a small illustration, direct execution may be more efficient than spawning a separate agent with a large context.

## Delivery checklist

- All unique requested repositories are accounted for, including deferred ones.
- Planned, cloned, installed, tested, and connected are not conflated.
- Existing work and credentials are preserved.
- UI state matches observed backend evidence.
- Agent and editor connections are tested independently.
- Current setup blockers are reported in the project artifact, not fossilized into reusable skill rules.
- The final response lists actual artifacts and remaining scope, without claiming a plan is a built dashboard.
