# Atticus: native desktop assistant installation checks

Source: https://github.com/SaarthurR/atticus-mac.git . Findings below came from source inspection during an installation; recheck the current checkout before reuse. This is a verification recipe, not a claim that onboarding or voice operation passed.

## Inspect before running

Read README.md, install.sh, build.sh, and preference definitions in Atticus.swift and atticus.py. The inspected build compiled Swift for macOS 26, staged the app before replacement, copied Python/resources, signed the bundle, and installed/started a launch-at-login job. Account for those persistent side effects, not just compiler dependencies.

Expected project locations at inspection:
- Source: ~/.atticus
- Bundle: ~/Applications/Atticus.app
- Launch job: com.atticus.app
- Runtime stderr: ~/.config/atticus/app.err

Do not assume these paths when an existing installation differs. Preserve dirty checkouts and existing configuration.

## Independent verification gates

```bash
"$HOME/Applications/Atticus.app/Contents/MacOS/Atticus" --selftest
codesign --verify --deep --strict "$HOME/Applications/Atticus.app"
launchctl list com.atticus.app
claude auth status
```

These establish native checks, bundle integrity, loaded job, and provider authentication separately. None proves voice input, permission grants, screen access, or a successful model round trip. Avoid copying account identifiers from auth output into reports.

From the source checkout, isolate Python tests from personal state:

```bash
SCRATCH=$(mktemp -d /tmp/atticus-check.XXXXXX)
ATTICUS_DIR="$SCRATCH" ATTICUS_POSTHOG_KEY='' \
  python3 -m unittest discover -s tests > "$SCRATCH/tests.log" 2>&1
RESULT=$?
printf 'LOG=%s/tests.log\nRESULT=%s\n' "$SCRATCH" "$RESULT"
exit "$RESULT"
```

Use a tracked background process with completion notification for long runs, retain its handle, and read the final summary. Run `python3 atticus.py --selftest` separately with its own temporary ATTICUS_DIR and empty ATTICUS_POSTHOG_KEY. Its result is independent of unittest discovery.

If a resolver assertion such as `app_named('the trading view application') == 'TradingView'` fails, inspect `app_named`, all callers, aliases, and installed-app discovery. Do not infer the cause or patch the assertion without that trace. A native pass does not cancel a Python failure.

## Privacy and onboarding

The inspected preference defaults included `safe: true`, `stats: true`, and `improve: false`. The backend checks `stats` for telemetry; an empty ATTICUS_POSTHOG_KEY disables capture only for processes receiving that environment. Test overrides do not change installed-app privacy preferences. Settings reside under the application's runtime DIR; discover its actual value rather than conflating the source checkout with runtime state.

Let the user approve microphone, speech recognition, accessibility, and screen recording access. Check which functions actually require each permission. A welcome screen is pending setup, not functional verification.

README-documented shortcuts at inspection: hold Control+Option+Space to speak a request; fn for dictation. Verify configured shortcuts before advising the user. Start with a harmless request after permission approval; separately test Spanish recognition rather than inferring it from a Spanish dictation-cleanup fixture.

## Ecosystem framing

Recommend dictation into the user's existing Hermes/project-agent input first. Atticus is a desktop interaction surface, not an automatic bridge to every agent's memory, Telegram identity, Slack connector, VPS access, or repository context. Label window-management, screen-reading, and meeting examples as documented/proposed until exercised. Local speech recognition does not mean model-bound text or screenshots stay local. Review recipients before sends and obtain participant consent before meeting capture.
