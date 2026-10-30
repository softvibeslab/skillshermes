# Wappy mobile release and audit operations

## Locator

- Active working copy: `/Users/USERNAME/Documents/SoftvibesLab/wappyvibes`
- Older duplicate: `/Users/USERNAME/Documents/GitHub/wappyvibes`
- Remote: `https://github.com/softvibeslab/wappyvibes.git`
- Stack: Flutter/FlutterFlow, Firebase, Stripe, Fastlane, Android Play Console.
- Android package: `com.softvibeslab.wappy`.

Always compare duplicate clones by branch, remote, dirty state, recent commits, and artifact timestamps. The SoftvibesLab copy has been the active release workspace.

## Release status workflow

1. Read the newest reports under `docs/`, especially production-release, store-release-validation, Google-login, and upload-kit folders.
2. Verify current source version from `pubspec.yaml` and current Git state.
3. Run the smallest live Play API probes with Fastlane:
   ```bash
   fastlane run google_play_track_version_codes package_name:com.softvibeslab.wappy track:internal json_key:fastlane/play-service-account.json
   fastlane run google_play_track_version_codes package_name:com.softvibeslab.wappy track:production json_key:fastlane/play-service-account.json
   ```
4. Verify artifact checksum and signature; do not infer store state from a local AAB.
5. Check privacy/account-deletion URLs live.
6. Run `flutter test` before reporting readiness.
7. Distinguish clearly:
   - technically valid artifact,
   - active Internal Testing release,
   - production promotion eligibility,
   - actual public production release.

A `FAILED_PRECONDITION` while promoting an already accepted internal bundle usually means Play Console prerequisites are incomplete rather than a signing/build failure. Inspect Publishing overview, App content declarations, countries/regions, testing requirements, and stale draft releases. Browser access may require interactive Google sign-in; the Play Developer API can still verify track version codes.

## APK handoff

For direct Android installation, build only ARM64 unless broader ABI coverage is requested:

```bash
flutter build apk --release --target-platform android-arm64 --split-per-abi
```

Then copy to a user-friendly path and verify:

```bash
shasum -a 256 <apk>
apksigner verify --verbose --print-certs <apk>
```

Report version, architecture, size, signer, checksum, and absolute path. Remind the user that Play Console uses the AAB, while the APK is for direct installation/testing.

## Comprehensive QA/manual pattern

Reuse the existing matrices under `docs/full-e2e-audit-2026-07-03/matrices/` rather than creating a second disconnected test catalog. Reconcile them against the current 52-route inventory and current build. Use one structured case source to generate the test matrix, evidence-linked dashboard, client/host manual, PDF/DOCX, infographic metrics, and release recommendation.

Capture user-visible screenshots during happy-path tests so each image serves as both QA evidence and manual material. Keep debug/failure captures separate. Execute each module in happy-path, negative/security, and regression rounds.
