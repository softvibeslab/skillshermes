---
name: react-native-expo-development
description: "Build, test, debug, and ship React Native applications with Expo: greenfield MVPs, state/data issues, role-gated UI, Expo Web E2E with Playwright, and EAS Android builds."
version: 1.0.0
author: Hermes Agent
created_by: agent
metadata:
  hermes:
    tags: [react-native, expo, mobile, debugging, playwright, eas]
---

# React Native Expo Development

Use this class-level skill for React Native applications built with Expo, from a greenfield validation prototype through debugging, end-to-end testing, and EAS distribution. Keep product-specific fixes and one-off reproduction recipes in `references/` rather than expanding the main workflow around one codebase.

## 1. Inspect before changing

1. Read repository instructions and `package.json`.
2. Use the Expo SDK and package versions declared by the project; prefer `npx expo install` for Expo-managed dependencies.
3. Identify navigation, state ownership, backend client, authentication/roles, and build profiles.
4. Reproduce the smallest failing journey before editing.
5. Verify with the project's scripts plus `npx tsc --noEmit`; do not treat a silent background dev server as proof the app works.

## 2. Greenfield MVP kickoff

```bash
npx create-expo-app@latest <app-name> --template blank-typescript --yes
```

For product validation, implement the smallest clickable loop first: onboarding, core action, success state, and a basic operator/partner view. A single `App.tsx` is acceptable temporarily when speed matters, but record the extraction plan. Add a short README and a dated implementation plan, then compile-check before committing.

Prefer manual or deep-link handoffs over premature infrastructure when they test the same hypothesis—for example, WhatsApp links before custom chat and payments in an early marketplace.

## 3. Systematic UI and state debugging

When UI is missing or stale, inspect in this order:

1. **Render gates:** role checks, feature flags, route registration, loading states, and null user/session values.
2. **State ownership:** confirm the mutation updates the state consumed by the visible component and triggers a re-render.
3. **Navigation lifecycle:** determine whether read/refresh effects run only on one route while equivalent entry points bypass them.
4. **Backend mutation:** inspect returned errors and row counts; with Supabase, verify RLS policies and query predicates.
5. **Derived counters:** badges often combine unread messages and notification rows, so update every authoritative source or centralize the counter.
6. **Temporary bypasses:** if a role/flag is forced open for diagnosis, label the change and revert it after testing.

Use logs to inspect identity, role, route params, room/request IDs, and mutation results. Never infer successful persistence only from navigation or local optimistic state.

## 4. Expo Web E2E with Playwright

When native automation is not already configured, Expo Web plus Playwright is the fastest journey-level test path.

```bash
npx expo install react-dom react-native-web @expo/metro-runtime
npm install -D @playwright/test
npx playwright install chromium
```

Add stable `testID` props to key views, buttons, inputs, and text, then target them with `page.getByTestId(...)`. Configure Playwright's `webServer` to start Expo Web on localhost and use a mobile device profile. Run the first test before adding missing hooks when practical so the expected failure is observed.

Verify both:

```bash
npm run test:e2e -- --project=mobile-chrome
npx tsc --noEmit
```

Ignore `playwright-report/` and `test-results/`. See `references/expo-playwright-e2e.md` for a ready-to-copy configuration.

## 5. EAS Android builds

1. Authenticate with `eas login` and confirm the project is linked.
2. Define an explicit `eas.json` profile; use `"android": { "buildType": "apk" }` for internal APK distribution.
3. Check SDK/native-module compatibility, assets, environment variables, app version, and Android version code.
4. Build and inspect status/logs:

```bash
eas build --platform android --profile preview
eas build:list
eas build:view <build-id>
```

Do not broadly clear caches or rewrite lockfiles before reading the concrete build error. See `references/expo-eas-build.md` for commands and pitfalls.

## 6. Verification and reporting

Before declaring success:

- run TypeScript and repository lint/test scripts;
- exercise the original journey, not just the edited component;
- verify backend state when the fix mutates remote data;
- run E2E for the core flow when available;
- inspect `git status --short` and report any uncommitted artifacts;
- distinguish compile verification from device/simulator verification.

## References

- `references/expo-playwright-e2e.md` — Expo Web + Playwright setup and selectors.
- `references/expo-eas-build.md` — EAS Android build commands and pitfalls.
- `references/tourism-swipe-mvp.md` — validation-first tourism marketplace prototype pattern.
- `references/elmec-v2-ui-chat-notification-debugging.md` — codebase-specific role, chat-tab, FAB, and unread-badge fixes.
