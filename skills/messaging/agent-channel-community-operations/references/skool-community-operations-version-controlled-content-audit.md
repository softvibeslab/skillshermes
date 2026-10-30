# Version-controlled Skool content audit

Use this pattern when a Skool community has live content that must be captured, reviewed in Git, approved by humans, and only then synchronized.

## Safe sequence

1. Treat Skool as read-only during discovery.
2. Capture a dated snapshot of community metadata, analytics, courses, folders, lessons, posts, categories, and events.
3. Keep inventory metrics separate from adoption metrics.
4. Deduplicate posts by stable ID.
5. Store only aggregate member data; exclude emails, bios, photos, cookies, tokens, and other unnecessary PII.
6. Save remote content under a dated `docs/skool/snapshot-YYYY-MM-DD/` tree. Label it as evidence, not approved canonical content.
7. Build `RECONCILIATION.md` mapping each remote item to its repo counterpart with one of: `equal`, `skool_only`, `repo_only`, `different`, `unmapped`.
8. Build `APPROVAL_MATRIX.md` with stable IDs, proposed action, owner, state, and review comment. Suggested states: `pending`, `approved`, `edit_required`, `rejected`.
9. Apply only approved decisions to canonical repo files.
10. Open a draft PR; convert it to ready only after explicit approvals and validation.
11. Merge approved repo changes first.
12. Re-query Skool, present the exact remote write set, and require separate authorization before mutating Skool.
13. Apply remote writes in small batches and re-read every changed object.

## Recommended snapshot layout

```text
docs/skool/
├── README.md
├── snapshot-YYYY-MM-DD/
│   ├── community.md
│   ├── analytics.json
│   ├── courses.json
│   ├── posts.json
│   ├── events.json
│   ├── manifest.json
│   └── courses/<course-slug>/
│       ├── course.md
│       └── lessons/<lesson-slug>.md
├── RECONCILIATION.md
└── APPROVAL_MATRIX.md
```

The manifest should retain stable remote IDs, source URLs, privacy/access level, capture time, path, and approval state. Lesson Markdown may use minimal frontmatter with these fields.

## Incomplete lesson inventories

`list_lessons` can report a non-zero lesson count while returning an empty `items` array. Treat count and returned items as separate facts.

Recovery order:

1. Retry by exact course title.
2. Fetch known lesson IDs or URLs with `get_lesson`.
3. Use the saved-session CLI/direct API fallback in read-only mode to recover folder/page IDs.
4. Mark unresolved entries as `capture_failed`; never infer titles, IDs, or content.
5. Reconcile the reported count against files actually captured and explain every gap.

## Minimal validation

- Parse every JSON file with the standard library.
- Confirm course and lesson totals, or document unresolved gaps.
- Scan the staged diff for credentials, cookies, tokens, member PII, and accidental secrets.
- Run `git diff --check`.
- Confirm no Skool write tool was called during the audit.
- Keep pre-existing local changes in a separate commit so the audit diff stays reviewable.

## Dashboard companion

For stakeholder review, a dependency-free HTML dashboard can mirror the plan with collapsible phases, localStorage checkboxes, progress, search, filters, and JSON export. It is a visualization of the plan, not the source of truth; the Markdown plan and Git diff remain canonical.
