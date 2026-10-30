---
name: codebase-inspection
description: "Inspect codebases w/ pygount: LOC, languages, ratios."
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [LOC, Code Analysis, pygount, Codebase, Metrics, Repository]
    related_skills: [github-repo-management]
prerequisites:
  commands: [pygount]
---

# Codebase Inspection with pygount

Analyze repositories for lines of code, language breakdown, file counts, and code-vs-comment ratios using `pygount`.

## When to Use

- User asks for LOC (lines of code) count
- User wants a language breakdown of a repo
- User asks about codebase size or composition
- User wants code-vs-comment ratios
- General "how big is this repo" questions
- User asks to analyze a parent folder containing multiple sites, products, client projects, tools, or nested repositories

For mixed multi-project directories, follow `references/multi-project-workspace-audit.md`. It covers manifest-based discovery, independent nested Git status, maturity assessment, artifact/secrets hygiene, and the minimal root-catalog recommendation.

When the audit must become an Excel inventory, effort/value estimate, commercial-status review, or sales forecast, also follow `references/portfolio-commercial-inventory.md`. It defines workbook sheets, parent/child double-count protection, editable valuation formulas, sale-evidence rules, and scenario forecasting.

When a repository is only a wrapper, documentation shell, or release index for a shipped browser extension, follow `references/distributed-browser-extension-audit.md`. Inspect the release artifact and manifest, trace product-level rejection guards, compare them against README claims and bundled-library capabilities, and report authenticated-media compatibility conditionally.

## Prerequisites

```bash
pip install --break-system-packages pygount 2>/dev/null || pip install pygount
```

## 1. Basic Summary (Most Common)

Get a full language breakdown with file counts, code lines, and comment lines:

```bash
cd /path/to/repo
pygount --format=summary \
  --folders-to-skip=".git,node_modules,venv,.venv,__pycache__,.cache,dist,build,.next,.tox,.eggs,*.egg-info" \
  .
```

**IMPORTANT:** Always use `--folders-to-skip` to exclude dependency/build directories, otherwise pygount will crawl them and take a very long time or hang.

## 2. Common Folder Exclusions

Adjust based on the project type:

```bash
# Python projects
--folders-to-skip=".git,venv,.venv,__pycache__,.cache,dist,build,.tox,.eggs,.mypy_cache"

# JavaScript/TypeScript projects
--folders-to-skip=".git,node_modules,dist,build,.next,.cache,.turbo,coverage"

# General catch-all
--folders-to-skip=".git,node_modules,venv,.venv,__pycache__,.cache,dist,build,.next,.tox,vendor,third_party"
```

## 3. Filter by Specific Language

```bash
# Only count Python files
pygount --suffix=py --format=summary .

# Only count Python and YAML
pygount --suffix=py,yaml,yml --format=summary .
```

## 4. Detailed File-by-File Output

```bash
# Default format shows per-file breakdown
pygount --folders-to-skip=".git,node_modules,venv" .

# Sort by code lines (pipe through sort)
pygount --folders-to-skip=".git,node_modules,venv" . | sort -t$'\t' -k1 -nr | head -20
```

## 5. Output Formats

```bash
# Summary table (default recommendation)
pygount --format=summary .

# JSON output for programmatic use
pygount --format=json .

# Pipe-friendly: Language, file count, code, docs, empty, string
pygount --format=summary . 2>/dev/null
```

## 6. Interpreting Results

The summary table columns:
- **Language** — detected programming language
- **Files** — number of files of that language
- **Code** — lines of actual code (executable/declarative)
- **Comment** — lines that are comments or documentation
- **%** — percentage of total

Special pseudo-languages:
- `__empty__` — empty files
- `__binary__` — binary files (images, compiled, etc.)
- `__generated__` — auto-generated files (detected heuristically)
- `__duplicate__` — files with identical content
- `__unknown__` — unrecognized file types

## 7. Production Readiness Assessment\n\nBeyond basic LOC metrics, use code inspection to evaluate production readiness. For small browser + API repositories, follow `references/small-fullstack-production-audit.md`: read the code end to end, trace trust boundaries, verify README/runtime claims, run build and security checks, and prefer deleting unused dependencies before upgrading them.\n\n\n```bash\n# After getting basic stats, check for critical files\nls -la | grep -E \"\\.(env|yaml|yml|json|txt|md|Dockerfile|docker-compose)\"\n\n# Check backend structure\nfind backend/ -name \"*.py\" | head -5\n\n# Check frontend structure\nfind frontend/ -name \"*.js\" -o -name \"*.ts\" -o -name \"*.jsx\" -o -name \"*.tsx\" | head -5\n\n# Look for configuration and secrets\nfind . -name \"*.env*\" -o -name \"config*\" -o -name \"settings*\" | head -10\n\n# Check for testing infrastructure\nfind . -name \"test*\" -o -name \"spec*\" | head -5\n\n# Check CI/CD\nfind . -name \"*.github\" -o -name \"gitlab-ci*\" -o -name \"Jenkinsfile\" -o -name \"*.circleci\" | head -5\n```\n\nKey indicators of production readiness:\n- **Environment configuration**: Presence of .env.example or similar template\n- **Dependency management**: requirements.txt, package.json, Cargo.go, etc.\n- **Configuration separation**: Config files not committed to repo\n- **Documentation**: README with setup/deployment instructions\n- **Testing**: Test directories and files\n- **CI/CD**: Configuration for automated builds/tests/deployments\n- **API docs**: OpenAPI/Swagger files or similar\n- **Database**: Migration scripts or schema definitions\n\n## Pitfalls\n\n1. **Always exclude .git, node_modules, venv** — without `--folders-to-skip`, pygount will crawl everything and may take minutes or hang on large dependency trees.\n2. **Markdown shows 0 code lines** — pygount classifies all Markdown content as comments, not code. This is expected behavior.\n3. **JSON files show low code counts** — pygount may count JSON lines conservatively. For accurate JSON line counts, use `wc -l` directly.\n4. **Large monorepos** — for very large repos, consider using `--suffix` to target specific languages rather than scanning everything.\n5. **Missing production indicators** — A high LOC count doesn't mean production ready. Always check for env files, configs, secrets management, and deployment configurations.\n