# Multi-repo research workspace pattern

Use when the user gives several GitHub URLs and asks to clone, compare, or identify how they apply to a product direction.

## Pattern

1. Create a dedicated workspace instead of scattering clones:

```bash
BASE="$HOME/Documents/GitHub/<topic>-research"
mkdir -p "$BASE"
cd "$BASE"
```

2. Save the URLs to `repos.txt` for repeatability, then shallow-clone/update:

```bash
while read -r url; do
  [ -z "$url" ] && continue
  name="${url##*/}"
  if [ -d "$name/.git" ]; then
    git -C "$name" pull --ff-only || true
  else
    git clone --depth 1 "$url" "$name" || echo "FAILED $url" >> clone-failures.txt
  fi
done < repos.txt
```

3. Inspect before installing anything. Extract:
   - README summary
   - root files: `package.json`, `requirements.txt`, `pyproject.toml`, `Dockerfile`, `docker-compose.yml`
   - language/file counts
   - license
   - GitHub stars/forks/updated date via API when useful

4. Produce one durable report in the workspace, e.g. `ANALISIS.md`, grouping repos into:
   - usable as base
   - useful as reference/patterns
   - docs/market research only
   - avoid/caution due to license, cloud dependency, or overbuilt stack

5. Do not install every stack by default. Most repo-research tasks need comparison and architecture mapping, not 14 dependency trees.

## Pitfalls

- License matters: AGPL repos can be studied, but copying code into a product has obligations.
- A repo with a strong README may still be docs-only; check actual files.
- For product applicability, prefer the smallest working base and treat the rest as references.
- If the user asks for local-first AI, separate local-capable pieces from cloud/API-only wrappers.

## Verification

```bash
find "$BASE" -maxdepth 2 -type d -name .git | wc -l
[ -f "$BASE/ANALISIS.md" ] && wc -l "$BASE/ANALISIS.md"
```