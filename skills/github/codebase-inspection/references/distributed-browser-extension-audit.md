# Auditing a distributed browser extension

Use this when a repository is mostly documentation, packaging, an Actor wrapper, or release metadata while the shipped extension contains the real implementation.

## Minimal workflow

1. Clone the repository and inspect its full tree and history.
2. Query the latest release metadata and enumerate assets.
3. Download one representative browser artifact, verify its published digest when available, and extract it in a temporary directory.
4. Treat the extracted `manifest.json` as the authority for:
   - Manifest version and service worker/content scripts
   - Host access and permissions
   - Scripts injected into every page/frame
   - External authentication, telemetry, and update endpoints
5. Trace the real execution path, not just README claims:
   - Detection/interception
   - Fetching and required session context
   - Parsing/transmuxing
   - Explicit rejection branches and error strings
6. Compare marketing claims with runtime guards. A bundled library mentioning AES, Widevine, FairPlay, or PlayReady does not prove the product supports encrypted downloads. Product-level checks such as rejecting `#EXT-X-KEY` override generic library capabilities.
7. Inspect the target SPA separately:
   - Locate its main bundle
   - Find the API method that returns the media field
   - Trace that field into the player and record its MIME type
   - Probe the endpoint without credentials only to establish the authentication boundary
8. State compatibility conditionally unless the exact media manifest was observed in an authorized session.

## Reporting contract

Separate these conclusions:

- **Architecture:** target appears to use HLS/M3U8.
- **Tool capability:** extension detects and downloads ordinary HLS.
- **Concrete verification:** whether the exact protected lesson was tested.
- **Encryption/DRM:** distinguish clear HLS, `EXT-X-KEY` encryption, SAMPLE-AES, and DRM/EME.
- **Privacy:** disclose broad host permissions, `webRequest`, scripting, tabs, downloads, and third-party activation.
- **Authorization:** do not extract or reuse tokens/cookies or explain bypasses; recommend testing only in a legitimate session and with download rights.

## Safe recommendation

For broad-permission extensions, recommend a separate browser profile and limiting site access to the target domain when the browser supports it. Never ask the user to send credentials, cookies, authorization headers, or signed media URLs; request only non-sensitive manifest metadata or visible error text.