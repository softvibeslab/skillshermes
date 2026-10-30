# Self-hosted local dashboard installation

Use this for third-party dashboards that pair with a local agent/CLI through a database-backed bridge.

## Minimal workflow

1. Clone into the user's normal project workspace and record the exact commit.
2. Read the repository's onboarding, package manifests, lockfiles, env template, bridge docs, and project instructions before installing.
3. Verify prerequisites from live state: Node version, package manager, agent CLI path/version, database availability, and container runtime.
4. Install deterministically:
   - Root lockfile present: `npm ci`.
   - Nested bridge without its own lockfile: `npm install` in that directory; do not force `npm ci`.
   - Keep generated nested `node_modules/` and lockfiles out of the working tree with local `.git/info/exclude` when they are installation artifacts rather than requested source changes.
5. Create a local database only when no usable database exists. A named PostgreSQL Docker container on a non-default loopback port is sufficient. Use a named volume and a generated password; never print credentials.
6. Build `.env` from the documented required variables. Generate local session/internal secrets with `openssl`; leave optional integrations blank. Reuse an existing OAuth client only with user approval and after inspecting its client type and redirect URIs without exposing the secret.
7. Push the schema, then run the production build. Treat lint, build, dependency audit, runtime, and authentication as separate gates.
8. Start the website and bridge. The bridge may not load the parent `.env` automatically; source/export it explicitly before starting.
9. Verify all layers:
   - HTTP route returns 200.
   - Database accepts connections and has the expected schema.
   - Bridge process remains running.
   - Database contains the bridge's canonical connected event.
   - Browser reaches the login page.
10. Stop at any interactive account sign-in or consent screen and let the user authenticate. Never report authentication as verified merely because the provider login page opened.

## Post-install onboarding dashboard

When the user also asks how the system works, prefer a dedicated onboarding route inside the existing app over a separate demo or a rewrite of the main dashboard:

1. Reuse the app's existing UI kit, layout, theme, and navigation. Add one discoverable “Start here” entry; do not introduce a second component system.
2. Trace the real execution path first, then explain it in the UI as a short loop such as `Dashboard → database → bridge → local agent CLI → database → dashboard`.
3. Make the onboarding operational rather than purely static by reading the existing health/request APIs and showing the actual database and bridge state.
4. Let the first exercise submit one safe, non-side-effecting mission through the real dispatch endpoint. Do not make publishing, sending, deleting, or external writes the default onboarding action.
5. Explain the approval boundary explicitly: safe work may enter `queued`; side-effecting work must enter `awaiting_approval` and remain blocked until approved.
6. Keep the onboarding in its own route so learning content cannot destabilize the operational dashboard. On mobile, preserve the existing navigation limit by replacing a lower-priority shortcut instead of adding overflow.
7. Verify the new route independently with scoped lint, whitespace/diff checks, a production build, HTTP 200, browser console, and visual overflow/responsiveness inspection. Separate pre-existing repository lint or audit debt from regressions introduced by the onboarding.

## Security and release gate

- A successful local build does not clear dependency vulnerabilities or lint failures.
- Report upstream audit/lint findings separately from installation success.
- Do not deploy publicly while critical production dependency vulnerabilities remain unless the user explicitly accepts the risk after seeing it.
- Do not run `npm audit fix --force` on a third-party repo during installation; it can introduce breaking source changes. Upgrade deliberately in a separate change.

## Verification evidence

Keep claims narrow:

- `installed`: dependencies are present.
- `configured locally`: required env and local database are ready.
- `running`: website and bridge processes are live.
- `bridge connected`: canonical DB/event evidence exists.
- `login flow reached`: provider page opened.
- `authentication verified`: the user completed sign-in and the protected dashboard loaded.
- `deployable`: build, auth, audit, and release gates all pass.
