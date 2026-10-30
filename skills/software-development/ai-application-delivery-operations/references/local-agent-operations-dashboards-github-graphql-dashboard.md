# GitHub connector for a local operations dashboard

Use `gh` as the credential boundary: verify `gh auth status`, then query read-only metadata without copying tokens into app configuration or browser responses.

## One-call repository snapshot

Prefer one GraphQL call over per-repository loops:

```bash
gh api graphql \
  -f query='query($owner:String!){repositoryOwner(login:$owner){repositories(first:100,orderBy:{field:PUSHED_AT,direction:DESC}){nodes{nameWithOwner url isPrivate pushedAt defaultBranchRef{name target{... on Commit{committedDate statusCheckRollup{state}}}} issues(states:OPEN){totalCount} pullRequests(states:OPEN){totalCount}}}}}' \
  -F owner=OWNER
```

Normalize each node to:

- `name`, `url`, `private`, `pushedAt`
- default `branch`
- latest `committedAt`
- `ci`: `SUCCESS`, `FAILURE`, or `NONE` when no status rollup exists
- open `issues` and open `prs` from `totalCount`

Do not use nested list lengths as totals; GraphQL connection lists may be truncated. Use `totalCount`.

## Runtime pattern

- Run `gh` with a fixed argv list via `subprocess.run`, never a browser-supplied shell string.
- Keep a separate 60-second GitHub cache; the main local-agent state can still refresh every 10 seconds.
- Return a graceful `{connected:false,error:...}` state when authentication or GraphQL fails.
- Keep the connector read-only by default. GitHub mutations need separate allowlisted endpoints and browser confirmation.
- Map flagship product names to explicit `owner/repo` identifiers server-side. Never guess repository names from display labels.

## UI pattern

Add a dedicated engineering view with:

1. repository count, open issues, open PRs, latest push;
2. cards for explicitly mapped flagship projects;
3. searchable recent-repository table with privacy, branch, last push, issue/PR counts, and CI state;
4. semantic CI colors: green `SUCCESS`, red `FAILURE`, muted `NONE`;
5. safe links using `target="_blank" rel="noreferrer"` and HTML escaping.

A progress bar is misleading for CI state. Show the literal state instead.

## Verification

- Confirm the API response contains the expected account and mapped repos.
- Check totals against `totalCount`, not visible list length.
- Filter for a known repository in the browser.
- Confirm private repository names render but no token, clone credential, secret, or workflow log is returned.
- Check browser console and visually inspect the dense table for clipping.
