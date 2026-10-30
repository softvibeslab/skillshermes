# Multi-project workspace audit

Use this when a directory is a portfolio/workspace containing many projects rather than one repository.

## Scope

Inventory only owned/source material by default. Exclude `.git`, `node_modules`, `dist`, `build`, `.next`, `.astro`, `venv`, `.venv`, `__pycache__`, and `coverage` from content and LOC scans.

## Workflow

1. List top-level directories and classify them as product/client project, analysis/content, reusable tooling, media/output, archive, or experiment.
2. Find technical manifests (`package.json`, `pyproject.toml`, `requirements*.txt`, `Cargo.toml`, `go.mod`, `composer.json`) to identify runnable projects. Do not assume every top-level folder is an application.
3. Detect nested Git repositories independently. For each, record branch, remote, and porcelain status without modifying the tree.
4. Read the root README plus README/manifests for the active projects. Extract purpose, stack, run/deploy path, maturity, and obvious next action.
5. Check trust-boundary hygiene: real `.env` files versus examples, committed build/dependency directories, archives, duplicated trees, and large binaries. Report presence, not secret values.
6. Run code metrics only after exclusions. Treat LOC as composition evidence, not readiness evidence.
7. Assess readiness using docs, dependency metadata, tests, CI, deployment config, real-vs-demo data, Git cleanliness, and whether a canonical version is identified.
8. Make no edits during an analysis-only request. Explicitly report that the workspace was left unchanged.

## Report shape

- One-line diagnosis: monorepo, portfolio workspace, or mixed asset warehouse.
- Scale: top-level folders, runnable projects, nested repos, code/binary/duplicate signals.
- Table or short list per important project: purpose, stack, Git state, maturity.
- Cross-cutting risks: duplication, mixed artifacts, missing canonical source, uncommitted work, secrets hygiene, test/CI gaps.
- Ordered recommendations that minimize churn. Prefer a generated root catalog/manifest before a broad folder migration.

## Pitfalls

- Do not call the root a deployable site merely because it contains websites.
- Do not aggregate nested Git repositories into one status.
- Do not claim “no CI/tests” from one shallow search; say “none detected in the inspected scope.”
- Do not recommend reorganizing first. A small catalog (`projects.yaml`/`projects.json`) usually creates visibility with less risk; move folders only when ownership/deployment boundaries are clear.
- Never print credentials while checking `.env` files.