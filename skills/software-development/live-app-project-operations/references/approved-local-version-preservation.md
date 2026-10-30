# Approved localhost version: preserve, verify, branch

## Trigger and scope

The user selects specific local routes and asks to keep their functionality and push a new branch. This is not permission to promote a newer experiment, merge, create a PR, or publish. If an earlier deployment was stopped, replace its stale plan with the new scope.

## Minimal sequence

1. Resolve the server document root, repository root, current branch, remote and dirty/untracked state. A nested app can belong to a parent monorepo; inspect the whole root before staging.
2. Read the app instructions and critical feature entrypoints. Trace UI, shared JS, canonical data, API and persistence separately.
3. Compare the approved HTTP responses to on-disk files and candidate Git blobs. For a static site, compare bytes for HTML, all relevant shared JS/CSS and canonical JSON. Use repository-root-relative paths with `git show`. For transformed/bundled applications, compare deployed build manifests/artifacts instead of claiming raw source equality.
4. Check the backend diff independently. HTTP page equality does not establish database preservation or complete feature parity.
5. Run existing backend checks on temporary storage, including migrations if available. Verify representative mobile/desktop routes and console/overflow state. A login fixture that submits credentials without checking the result is not an authenticated acceptance test.
6. If the approved implementation is already committed, no code or commit is needed. After checking branch-name availability and applicable push-triggered automation, use the sequence below. If new changes must be included, review explicit paths and isolate work rather than staging the monorepo wholesale.
7. Verify the remote hash and original working-tree state. Deliver branch URL, commit, actual checks and limitations. Do not claim live database backup from a source-only branch.

```sh
# Run from the discovered repository root; substitute verified values.
git branch <new-branch> <verified-commit>
git push -u origin <new-branch>
git rev-parse <new-branch>
git ls-remote --heads origin refs/heads/<new-branch>
git status --short
```

No checkout is needed. Do not use `git push origin HEAD` when the newly created branch is not checked out. Do not force an existing branch. A push may trigger configured deployment automation: inspect that boundary if the requested scope forbids publication.

## Responsive screenshot diagnostic

In one Chromium/Playwright run, a tall element screenshot changed observable mobile emulation: `pointer:coarse` changed from true to false and `maxTouchPoints` from 1 to 0. A subsequent parallax assertion failed because production code correctly reacted to the altered capabilities. This is a diagnostic pattern, not a universal browser limitation.

When an input-capability assertion fails after a screenshot, capture these values immediately before and after that screenshot:

```js
const capabilities = () => page.evaluate(() => ({
  coarse: matchMedia('(pointer:coarse)').matches,
  touch: navigator.maxTouchPoints,
  reduced: matchMedia('(prefers-reduced-motion: reduce)').matches
}));
console.log('before', await capabilities());
await page.screenshot({ path: screenshotPath, fullPage: false });
console.log('after', await capabilities());
```

Use viewport screenshots when they satisfy the evidence need; use a separate page/context for tall or full-page captures if they perturb the functional test. Re-run the original assertions. Do not weaken the mobile assertion or change production parallax logic to compensate for capture-induced state. Keep reduced-motion and coarse-pointer checks separate.

## Evidence labels

- Byte comparison: only listed served files match disk/commit.
- Backend suite: tested business invariants on disposable state.
- Route smoke: guest rendering/console/layout at listed widths.
- Authenticated E2E: actual login and subsequent persisted operations verified.
- Audit matrix: only the browser/profile combinations actually executed.
- Remote verification: named branch points to the expected commit.

A cancelled delegate audit supplies none of the missing evidence. Partial artifacts may exist and must be inspected before reuse; do not convert an interrupted run into a successful test claim.
