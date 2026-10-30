# Onboarding inside an existing React dashboard

## Integration sequence

1. Read project instructions, dirty state, app/router shell, nav rendering branches, locale conventions, relevant API consumers, URL/clipboard helpers, and test configuration before implementing.
2. Keep the existing auth boundary, router basename, theme provider, backend, and query cache intact. Replace only the approved root redirect; retain other redirects. Add home to both desktop and mobile navigation, using an existing translation key or a narrow explicit-label extension. Make home active only at the root. Check header width after adding another item.
3. Keep the requested page language consistent, including errors, accessibility labels, copy feedback, and persistence notices. Scope palette and selectors to the page; a deliberately light panel must not change global dark-mode tokens.
4. Treat step selection, manual completion, and verified server state as different concepts. Selecting a step or copying a snippet must not auto-complete setup. Use buttons with pressed state for selection and real links for navigation; avoid partial ARIA tabs without keyboard behavior.

## Truthful data and local progress

- Reuse the existing query key/API helper. A registered-key count is not a healthy-key count or available quota. Distinguish pending, failure, successful zero, and stale cached results; never default a failed request to a reassuring zero.
- Store only checklist booleans under a versioned namespaced key. Parse JSON defensively, accept literal `true` only, normalize length, and catch unavailable storage.
- Label progress manual, local, and unverified. Browser-wide localStorage is not account-scoped: state that limitation or use an existing non-secret account identifier if account scoping is required. On write failure, explain that current state survives only while mounted.
- Reset only this checklist; never clear unrelated storage. A reset is not a backend rollback.

## Snippets and safety copy

Reuse deployment-aware URL helpers and existing clipboard fallbacks. Do not fetch or insert actual credentials merely to show an example. Keep key and model placeholders conspicuous, explain both substitutions, provide async success/failure feedback via a status region, and retain manual selection on failure. Copying does not send a request.

For gateway products, ground copy in source/docs: gateway versus model; provider credentials versus gateway credentials; upstream quotas and charges; encrypted credentials at rest versus upstream prompt/context processing. Do not imply SQLite is wholly encrypted when only credential fields are encrypted.

## Focused verification under parent-owned build constraints

If the parent owns installation/build, do not run either. Use existing local binaries for a focused test and no-emit typecheck when authorized. Do not install dependencies just to add a small test.

A plain Vitest setup may need per-file `// @vitest-environment jsdom`, a MemoryRouter, a fresh QueryClient with retries disabled, and mocked API/clipboard/base-URL helpers. Test persisted malformed state, real destination links, step selection, toggle/reset, placeholder copying and failure, and absence of secret inputs. Add pending/error/storage-failure cases when feasible.

React Query notifications may arrive after the first render act. Poll the expected DOM state while flushing React work, rather than assuming a resolved mock has rendered immediately:

```tsx
await vi.waitFor(async () => {
  await act(async () => {})
  expect(container.textContent).toContain('0 claves de proveedor registradas')
})
```

Keep render/click/unmount inside `act`; clear storage/mocks and dispose test roots/query clients. Do not hide warnings or loosen assertions to accommodate asynchronous rendering. Prefer existing Testing Library helpers if already present.

Typecheck and unit tests do not establish visual/browser readiness. Report exact files and commands, and explicitly identify outstanding viewport/header, keyboard, theme, and deployed-route checks.

## Historical reference: FreeLLMAPI

The September 2026 implementation used `client/src/App.tsx`, `InicioPage.tsx`, `inicio.css`, and `InicioPage.test.tsx`; `['keys']` with `/api/keys`; existing `apiBaseUrl()` and `copyText()` helpers; and routes `/keys`, `/models/chat`, `/playground`, `/agents`. Three focused tests, a no-emit typecheck, and diff whitespace check passed. Browser visual QA remained outstanding. Reinspect these paths and contracts before future changes; these are historical examples, not guaranteed current state.
