# Skool CLI direct API fallback

Use this when MCP/CLI browser automation discovers the course but times out creating folders or lessons around `CourseMenuTop`.

## Why

`skool-cli` has lower-level API helpers in its published package. They can reuse the saved Skool auth state from `~/.skool-cli/auth-state.json` and call `api2.skool.com` directly for course tree mutations.

Do not record credentials. The auth state file is the only session source.

## Minimal recipe

```bash
pkg=$(mktemp -d)
cd "$pkg"
npm pack skool-cli --silent >/dev/null
tar -xf skool-cli-*.tgz
```

Create a one-off `.mjs` script in that temp dir:

```js
import { readFileSync } from 'node:fs';
import { SkoolApi } from './package/dist/core/skool-api.js';
import { markdownToHtml } from './package/dist/core/html-generator.js';

const api = new SkoolApi({});
api.getCookies = async () => api.loadCookiesFromFile();

const groupId = 'GROUP_ID';
const userId = 'USER_ID';
const rootId = 'COURSE_ID';
const base = '/absolute/path/to/markdown-lessons';

function html(file) {
  return markdownToHtml(readFileSync(`${base}/${file}`, 'utf8'));
}

const f = await api.createFolder({
  groupId,
  parentId: rootId,
  rootId,
  title: 'Módulo 2 — Produce tu Reel',
});
if (!f.success) throw new Error(f.message);

const page = await api.createPage({
  groupId,
  userId,
  parentId: f.folderId,
  rootId,
  title: 'Clase 2 — Crea tu avatar',
  content: html('clase-02.md'),
});
if (!page.success) throw new Error(page.message);
```

## Finding IDs

- `rootId`: course ID from `mcp_skool_skool_list_courses`.
- `folderId`: returned by `api.createFolder`, or from `mcp_skool_skool_list_lessons`.
- `userId`: decode the `auth_token` cookie payload in `~/.skool-cli/auth-state.json`; use only the `user_id`, never copy the token.
- `groupId`: fetch `GET /courses/<rootId>` with `SkoolApi.request` and read `course.group_id`, or inspect the course page metadata.

Inspection snippet:

```js
import { SkoolApi } from './package/dist/core/skool-api.js';
const api = new SkoolApi({});
api.getCookies = async () => api.loadCookiesFromFile();
const r = await api.request('GET', '/courses/COURSE_ID');
console.log(JSON.stringify(r.data.course, null, 2));
```

## Verification

After the upload, verify with MCP rather than trusting script output:

```text
mcp_skool_skool_list_lessons(group='GROUP_SLUG', course='Course Title')
mcp_skool_skool_get_lesson(group='GROUP_SLUG', id='PAGE_ID')
```

Expected success evidence:
- list shows the intended number of folders and lessons;
- one or more fetched lessons have the expected title, path, and non-empty HTML/body;
- no duplicate temporary pages remain.

## Notes from AgenticOS Avatar IA upload

A fast launch upload used this fallback to create:
- 3 folders,
- 7 lesson pages,
- 1 resources page,
- updates to existing placeholder pages.

The final verification reported 9 lessons across 3 folders. Course metadata rename attempts returned success but the visible course title remained unchanged, so verify course edits explicitly and avoid unnecessary renames.
