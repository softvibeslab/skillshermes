# Hostinger static dashboard deployment

Use this when a project already has a Hostinger static website and the user asks to publish a prebuilt dashboard or document portal.

## Safe deployment sequence

1. Re-read project instructions and check `git status --short`; do not mix or overwrite concurrent unrelated edits.
2. Inspect the live domain before packaging. A Hostinger parked-domain page with HTTP 200 means DNS resolves, not that the domain is attached to a website; confirm hosting assignment separately.
3. Build and validate the static export (`npm run check && npm run build`, or the project's equivalent).
4. Decide the public entry point explicitly. If the requested page is not already `index.html`, stage a deployment copy and rename/copy it to `index.html` there; do not rewrite the canonical source or overwrite an unrelated tracked homepage merely to package a deploy.
5. Validate every local `href`/`src` in the staged directory, then serve it locally and probe `/`, linked feature pages, and at least one asset. Exercise one browser navigation branch before packaging.
6. Verify the expected route and downloadable artifacts exist inside the export directory.
7. Query Hostinger for the exact domain before deploying. Confirm `is_enabled`, account username, and `root_directory`; do not infer them from an old deployment record.
   - If the MCP requests renewed authorization, complete the browser OAuth flow before any deploy call. Keep the verified build/archive intact, tell the user exactly which authorization is pending, and resume by re-querying the domain after approval. Do not claim publication while OAuth is pending.
8. Zip the **contents** of the export directory, not its parent directory. Name it `directoryname_YYYYMMDD_HHMMSS.zip` and assert that `index.html` and all required linked files are archive-root entries.
9. Call Hostinger MCP `hosting_deployStaticWebsite` with:
   - `domain`: exact production domain
   - `archivePath`: archive path
   - `removeArchive: true`
   - Treat the ZIP as consumable when `removeArchive` is true. Preserve the staging directory; recreate an archive afterward only if the user needs a retained handoff artifact.
10. Purge server/CDN cache using `hosting_clearWebsiteCacheV1` with the verified username and domain.
11. Poll production until **every staged file** returns HTTP 200, not only the root and one feature route. Use `scripts/verify-static-deployment.py <staging-dir> <base-url>` for the manifest and text-file parity check.
12. Compare SHA-256 for critical HTML/CSS/JS. Shared hosting may optimize binary images, so a binary hash mismatch is a visual-QA signal rather than automatic deployment failure unless byte identity was explicitly required.
13. Open the live routes in a browser, exercise the important interactions, and inspect the console. HTTP 200 and matching HTML do not prove JavaScript/Three.js initialization succeeded.
14. If runtime QA finds a source bug, patch both the canonical source and the staged deployment copy, rebuild/repackage, redeploy, purge cache again, and repeat the full manifest + browser-console checks.
15. Update the repo's deployment metadata only after live verification; never include credentials in it.

## Browser-permission fallback

When the only available deploy surface is an already-authenticated hPanel browser session:

- Ask for desktop-control approval once and explain that existing session state will be reused; never request or type the password.
- If approval is denied, a second attempt is reasonable only after the user explicitly says permission is enabled. Do not bypass denial with AppleScript, shell-driven UI automation, browser-profile extraction, or credential mining.
- Preserve the verified staging directory and ZIP in a user-accessible location, stop temporary local servers, and provide the shortest manual hPanel path: attach domain to hosting → open `public_html` → upload archive → extract archive contents at root → clear cache.
- Report `ready locally, not published` until the exact production URL and linked routes are verified.

## Next.js static-export clean-route pitfall

With `output: "export"`, a route such as `/contratos` may emit `out/contratos.html`. If public assets also create `out/contratos/`, Hostinger can resolve `/contratos` as a directory and return 403 even though `contratos.html` exists.

Fix the root cause in `next.config.ts`:

```ts
const nextConfig: NextConfig = {
  output: "export",
  trailingSlash: true,
};
```

Rebuild and verify `out/contratos/index.html` exists, then redeploy. Do not work around it by telling users to visit `/contratos.html`.

## Verification details

- Verify both `/route/` and every embedded/download artifact, not just `/`.
- A successful deployment request means accepted, not necessarily live; poll the public URLs.
- A DOCX may be served with a generic MIME type by shared hosting. If HTTP 200 and browser download works, do not add server configuration unless inline MIME behavior is explicitly required.
- Keep API tokens out of commands, logs, chat, deployment metadata, and skill references. Read them from the configured MCP environment/credential store.
