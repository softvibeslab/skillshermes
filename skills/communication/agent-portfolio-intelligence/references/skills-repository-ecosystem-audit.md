# Skills + repository ecosystem audit

## Purpose
Turn an installed-tool inventory into integration decisions without mistaking presence for operation. Derived from a mixed Softvibes/ROVI workspace assessment; product names and counts are examples to rediscover, not current-state assertions.

## Discovery and normalization
1. Establish read-only scope, active profile, search roots, depth and exclusions. Report inaccessible or uncovered roots.
2. Detect both `.git` directories and `.git` files used by worktrees. Exclude dependency/generated trees from product counts, while retaining their classification if discovered.
3. Record path, sanitized remote, branch/worktree identity and source documents. Normalize equivalent SSH/HTTPS remotes; retain original local paths. A normalized origin is not a unique-product count.
4. Inventory the active skill catalog separately from SKILL.md files found inside repositories. Classify source-only skills as candidates, not installed capabilities.
5. Read README, manifests, project context and connection registries for shortlisted families. Distinguish executable contracts from aspirational documentation.

## Evidence matrix
Use one row per capability or project family:

| Field | Required content |
|---|---|
| Capability | User outcome, not tool branding |
| Components | Repositories and complementary skills |
| Evidence | File path and relevant section, or command and observed output |
| Observed level | Discovered / documented / configured / callable / end-to-end verified |
| Scope | What was read or tested, and what was not |
| Overlap | Existing component that already performs the role |
| Boundary | Source of truth, data ownership and approval requirements |
| Missing contract | Actual integration prerequisite, not speculative scaffolding |
| Pilot | Smallest useful input-to-output flow |
| Acceptance | Persistent result, observable evidence and human approval where needed |

Do not upgrade all capabilities because one command works. A successful squad listing proves discovery only; empty capability registration calls for further inspection, not a blanket claim that the ecosystem is broken. Registry status such as `active` is a declaration unless traffic or a test verifies the connection.

## Integration decisions
- Choose one authority for tasks, ownership and acceptance; specialize additional tools instead of making every dashboard an orchestrator.
- Trace input → persistence → responsible actor → next action → evidence. Mark proposed edges explicitly.
- Identify source-only skills that encode the project's own handoff/evidence contracts before recommending generic replacements. Installation remains a separate authorized action.
- Knowledge systems must have distinct roles: source ingestion, retrieval, relationship mapping, learning or reusable procedures. Avoid another ingestion store without a concrete unmet need.
- Commercial flows require consent and correct customer-data scope. Opportunity discovery is not permission for outbound contact.
- Use a bounded pilot rather than an ecosystem-wide migration. Include explicit defer/no-value recommendations.

## Artifact checks
- Use the same normalized inventory for prose and workbook totals.
- Separate discovered roots, normalized origins, catalog skills and deeply reviewed projects in the summary.
- If parallel reviewers are used, require exact source paths and independently read the evidence supporting consequential recommendations.
- Reopen the produced workbook; confirm sheet names, row counts and representative rows. Verify every delivered artifact exists before claiming it does.
- Sanitize credentials in URLs, configs and output before saving reports. Avoid copying unnecessary private data.
- Deliver a short decision summary, priorities, unverified limits and absolute artifact paths. State what was not changed.

## Frequent misreads
- Cloned repository ≠ installed service.
- Skill catalog entry ≠ compatible or exercised runtime.
- Shared Git origin ≠ disposable duplicate.
- Configured integration ≠ verified delivery.
- Static CTA ≠ backend event source.
- Documentation review ≠ production readiness audit.
