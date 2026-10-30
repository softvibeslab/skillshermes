---
name: skool-community-operations
description: "Operate Skool communities from Hermes: login/session checks, list communities/courses, create or edit courses, folders, lessons, posts, events, members, analytics, and verify published classroom content using the Skool MCP/CLI."
version: 1.0.0
---

# Skool Community Operations

Use this when the user wants to manage a Skool community: upload course content, create folders/lessons, publish posts, update About text, inspect members/analytics, or troubleshoot Skool MCP/CLI automation.

## Default flow

1. Confirm target community only if ambiguous.
   - Prefer the known group slug when the conversation or memory provides it.
   - For AgenticOS/Emprende Inteligente, use `emprendedores-con-ia-6640`.

2. Check session before mutating.
   - `mcp_skool_skool_check_session` or `mcp_skool_skool_list_communities`.
   - If not logged in, ask for credentials only when needed, use `mcp_skool_skool_login`, and never repeat or persist the password.

3. Inspect before writing.
   - List courses with `mcp_skool_skool_list_courses`.
   - List lessons for the target course with `mcp_skool_skool_list_lessons`.
   - List categories/posts before publishing community posts.

4. Upload content in small launch slices.
   - Prefer one complete course/module path over dumping everything.
   - Create folders first, then lessons.
   - For Markdown lesson bodies, use the MCP `markdown_content` field or CLI `--file` path.

5. Verify every mutation.
   - Re-list lessons after folder/lesson creation.
   - Fetch at least one created lesson with `mcp_skool_skool_get_lesson` to confirm content rendered.
   - Verify course metadata after edits; do not trust a success message alone.

## Git-reviewed content synchronization

When the user wants to analyze all live Skool content, document it in a repository, approve it through a PR, and synchronize later:

1. Keep Skool read-only during capture and reconciliation.
2. Save a dated snapshot under `docs/skool/`; clearly distinguish observed remote content from approved canonical content.
3. Reconcile every remote item against the repo and assign stable approval IDs.
4. Apply only explicitly approved decisions to canonical files.
5. Open the PR as draft; merge before proposing remote writes.
6. Re-query Skool after merge, show the exact write set, obtain separate authorization, then mutate in small verified batches.
7. Preserve privacy: commit aggregate member metrics, not member profiles or credentials.

Use `references/skool-community-operations-version-controlled-content-audit.md` for the complete directory layout, approval matrix, incomplete-inventory recovery order, validation checks, and optional interactive dashboard pattern.

## Useful commands/tools

MCP tools:
- `mcp_skool_skool_list_communities`
- `mcp_skool_skool_list_courses`
- `mcp_skool_skool_list_lessons`
- `mcp_skool_skool_create_folder`
- `mcp_skool_skool_create_lesson`
- `mcp_skool_skool_edit_lesson`
- `mcp_skool_skool_get_lesson`
- `mcp_skool_skool_create_post`
- `mcp_skool_skool_edit_about`
- `mcp_skool_skool_create_event`
- `mcp_skool_skool_list_events`

CLI equivalents:
```bash
npx -y -p skool-cli skool whoami
npx -y -p skool-cli skool list-courses -g GROUP_SLUG
npx -y -p skool-cli skool list-lessons -g GROUP_SLUG --course 'Course Name'
npx -y -p skool-cli skool create-folder -g GROUP_SLUG --course 'Course Name' -t 'Module Name'
npx -y -p skool-cli skool create-lesson -g GROUP_SLUG --course 'Course Name' -m 'Module Name' -t 'Lesson Title' -f lesson.md
```

## Direct API fallback for classroom uploads

If Skool browser automation times out around `CourseMenuTop` while creating folders/lessons, use the package internals and saved session cookies rather than repeating the same failing browser action.

Pattern:
1. Pack `skool-cli` into a temp directory.
2. Import `SkoolApi` and `markdownToHtml` from the unpacked package.
3. Override `api.getCookies = async () => api.loadCookiesFromFile()` so requests use `~/.skool-cli/auth-state.json`.
4. Use known IDs:
   - `groupId` from course API/page metadata.
   - `userId` from the `auth_token` cookie payload.
   - `rootId` from the course ID.
   - folder IDs from list/get output or create results.
5. Call:
   - `api.createFolder({ groupId, parentId: rootId, rootId, title })`
   - `api.createPage({ groupId, userId, parentId: folderId, rootId, title, content: markdownToHtml(md) })`
   - `api.updatePage(pageId, { title, content: markdownToHtml(md) })`

See `references/skool-community-operations-skool-community-operations-skool-cli-direct-api-fallback.md` for a working session recipe.

## NotebookLM course exports

When converting a live Skool course into a NotebookLM source:

- Resolve and export only the exact requested course; do not mix in other courses from the community inventory.
- Fetch every visible lesson by ID and preserve the published module order.
- Produce two files: a source-only course wiki and a separate prompt pack for podcast, video, infographic, and final source audit.
- Do not place production instructions inside the uploaded wiki; NotebookLM may treat them as course facts.
- Surface duplicate lesson bodies, count mismatches, missing attachments, stale prices, and unsupported tool claims instead of silently filling gaps.
- Never invent the contents of a lesson whose title and body disagree.

Use `references/skool-community-operations-notebooklm-course-export.md` for the complete extraction, packaging, prompt, and verification pattern.

## Status and analytics reporting

- Query analytics, members, courses, and posts independently; a healthy session or large course count does not prove community activation.
- Deduplicate posts by stable ID before reporting counts because list responses can repeat the same post.
- Separate inventory metrics (courses/lessons) from adoption metrics (visitors, signups, members, contributions, likes, comments, MRR).
- Diagnose the narrowest evidenced bottleneck. If content inventory is broad but engagement is near zero, prioritize one entry course, onboarding, rituals, and member actions instead of creating another course.
- Treat every metric as a dated snapshot and re-query before future status reports.

## Pitfalls

- Do not save Skool passwords in memory, skills, notes, or final replies.
- Skool About page description rejects bodies over 1000 chars even if the source plan says a longer text is "ready to paste". On failure, shorten and retry rather than abandoning the Settings update.
- For launch events, pick a concrete near-term default if the user says "create an event" without details: one 60-minute office hour within the next week, using `America/Mexico_City` when operating this user's LATAM community, then verify with `list_events`.
- Avoid renaming an existing course unless the user explicitly wants it; a stable visible title is more important than a clever optimized title.
- Course edit success messages can be misleading. Always re-read course metadata after `edit-course` or direct `updateCourse`.
- Some Markdown tables may render as paragraphs if the CLI converter is simple. That is acceptable for a fast launch; convert critical tables to bullets only if the user cares about polish.
- If one folder/lesson creation partly succeeds, list lessons before retrying to avoid duplicates.

## Launch bias

For community launches, ship the smallest complete path:
- one lead-magnet course,
- 3-7 lessons,
- one resources lesson,
- one welcome post,
- one course announcement post.

Skip pricing, payment, and video URLs until the user confirms those details.
