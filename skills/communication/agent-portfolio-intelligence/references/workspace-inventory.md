---
name: portfolio-workspace-inventory
description: Inventory a mixed workspace of sites, apps, agents, research, and nested repositories into a decision-ready Excel catalog; use for “all my projects,” portfolio audits, latest-project reports, and category views such as landings, menus, or agents.
version: 1.0.0
metadata:
  hermes:
    tags: [portfolio, inventory, excel, workspace, projects, git, agents]
---

# Portfolio Workspace Inventory

Build a useful catalog of a mixed project warehouse without pretending every directory is a deployable project.

## Trigger

Use when the user asks to:
- inventory all projects in a parent workspace;
- produce an Excel/CSV catalog of landings, menus, apps, agents, or repositories;
- identify the most recently developed projects by category;
- assess maturity, duplication, Git coverage, documentation, tests, or deployment signals across many projects;
- convert a project portfolio into an indicative intangible-asset valuation, investor data room, cap table, or investment-route comparison.

For pure LOC/language analysis, also load `codebase-inspection`. This skill owns discovery, classification, workbook output, and recency reporting.

## Workflow

1. **Set explicit scope.** Default to the named workspace. Add external operational inventories (for example Hermes profiles) as separate sheets, never silently mix them into source-project totals.
2. **Discover project roots using evidence:** top-level initiatives, nested Git roots, technical manifests, and direct children of known product collections. Exclude dependencies, builds, caches, temporary browser profiles, generated output, and vendored code.
3. **Distinguish projects from support directories.** `assets`, `src`, `docs`, `tests`, `output`, `graphify-out`, and similar folders are not projects merely because they were recently modified. Include them only when they are independent Git/manifest roots or explicitly requested.
4. **Read shallow metadata only:** root README/context, package description, manifests, Git branch/remote/status, tests, CI, deploy config, file count, size, and latest owned-file modification. Never read secret values; report only `.env` presence.
5. **Classify with transparent categories.** Prefer categories grounded in path/product collection plus manifests: landing/site, digital menu, AI agent, mobile app, CRM/sales, proptech, content/video, tooling/infrastructure, research/content, or general initiative.
6. **Estimate maturity conservatively.** Use several signals (README, manifest, Git, tests, CI, deployment), label it “estimated,” and avoid equating modification time or LOC with readiness.
7. **Create a workbook** with at least: `Resumen`, `Proyectos`, `Repositorios Git`, `Hallazgos`; add domain sheets such as `Agentes Hermes` when relevant. Freeze headers, enable filters, set readable widths, and validate the XLSX as a ZIP container after writing.
8. **Answer recency follow-ups from leaf projects.** Sort by latest modification, but omit collection roots and support folders from the human-facing “latest developed” list. State that recency means filesystem modification unless Git commit dates were explicitly requested.
9. **Treat “remove/delete these projects” as workbook filtering by default when the active artifact is an inventory.** If the request could instead mean deleting local directories or remote repositories, ask which scope they mean before any destructive action. For workbook-only removal, filter all project/repository sheets consistently, refresh summary totals and filter ranges, append a methodology note describing the exclusion rule, and verify zero remaining matches without deleting source files.

## Minimum project columns

- Project name, category, level (principal/subproject), parent collection
- Purpose/description and detected stack
- Estimated maturity and latest modification date
- File count and size excluding dependencies/builds
- Git root, branch, clean/dirty state, remote
- README, tests, CI, deploy config, real `.env` presence
- Absolute path

## Recency report rules

- Separate categories instead of producing one mixed ranking.
- Prefer concrete leaf products over portfolio roots.
- For agents, distinguish source projects from configured/running agent profiles.
- If several entries share a date, do not invent an order; present them as same-day activity.
- A recent generated report does not make its parent product recently developed.

## Pitfalls

- Broad `package.json` searches commonly crawl `node_modules`; prune during traversal rather than filtering only after collection.
- Nested Git repositories need independent status checks. Do not inherit the parent repository’s branch/status.
- Duplicate names are a review signal, not permission to delete anything.
- `.env` inspection means presence only—never print keys or values.
- Do not install a spreadsheet dependency before checking for an already-installed writer such as `xlsxwriter`, pandas, LibreOffice, or Numbers automation.
- Keep the generated workbook out of project-root discovery on reruns.
- A domain/company filter is broader than matching one folder-name token. Build the exclusion vocabulary from project names, paths, remotes, and known product-family aliases; review matches before applying it so generic terms do not remove unrelated work.
- Do not silently rewrite or delete source projects when the user is working on an Excel inventory. Workbook filtering and filesystem/GitHub deletion are separate operations with very different risk.

## Verification

- Confirm the output file exists and is non-empty.
- Open it as a ZIP and run an archive integrity test.
- Confirm expected sheet names in `xl/workbook.xml`.
- Reconcile headline totals with the project table.
- After applying an exclusion filter, scan every affected sheet with the same normalized pattern and require zero remaining matches.
- Spot-check the newest three leaf projects in each requested category.

## References

- See `references/portfolio-workspace-inventory-portfolio-workspace-inventory-mixed-softvibes-workspace.md` for a condensed example of collection discovery, agent-profile separation, and recency filtering from a large mixed workspace.
- See `references/portfolio-workspace-inventory-portfolio-workspace-inventory-digital-portfolio-valuation-and-investor-readiness.md` when converting an inventory into an ownership-safe intangible-asset valuation, investor data room, cap table, and incorporation/private-equity/crowdfunding decision pack.
