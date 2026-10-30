# Expo Playwright E2E Reference

Session pattern: React Native/Expo SDK 54 app needed quick E2E coverage before native device automation was available. Solution was Playwright against Expo Web with mobile viewport.

## Known-good dependencies

```bash
npx expo install react-dom react-native-web @expo/metro-runtime
npm install -D @playwright/test
npx playwright install chromium
```

## Scripts

```json
{
  "web:e2e": "expo start --web --localhost --port 8081",
  "test:e2e": "playwright test"
}
```

## Minimal config

```ts
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './e2e',
  timeout: 30_000,
  expect: { timeout: 10_000 },
  use: {
    baseURL: 'http://127.0.0.1:8081',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
  },
  webServer: {
    command: 'npm run web:e2e',
    url: 'http://127.0.0.1:8081',
    reuseExistingServer: !process.env.CI,
    timeout: 120_000,
  },
  projects: [{ name: 'mobile-chrome', use: { ...devices['Pixel 7'] } }],
});
```

## Test authoring notes

- Add `testID` props to all key elements; target them with `page.getByTestId()`.
- For React Native Web, `testID` is a stable cross-platform hook and avoids brittle generated class names.
- If a text selector matches multiple elements, use exact text or add a `testID`.
- Run the first E2E before adding testIDs to verify RED; expected failure: element not found.

## Verification

```bash
npm run test:e2e -- --project=mobile-chrome
npx tsc --noEmit
```

## Cleanup

Add to `.gitignore`:

```gitignore
playwright-report/
test-results/
```
