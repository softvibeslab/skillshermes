# Secure credential setup in existing dashboards

Use when adding a browser-based API-key setup flow to an already authenticated application. Extend its handler, provider, tests, and UI; do not introduce a second settings framework.

## Inspect before changing

- Read the entire relevant handler/provider implementation, tests, HTML, JavaScript, and styles; trace initialization, authentication, CSRF, state serialization, errors, and every provider caller.
- Check Git status before editing and preserve unrelated work. If Git metadata is absent, report that limitation rather than claiming a clean diff.
- Inspect the installed SDK's constructors, request signatures, timeout and retry controls, and existing documented read-only calls. Do not infer a current signature from memory.
- Respect code-only scope: SDK inspection and mocked validation do not authorize live API calls, deployment, public tunnels, profile edits, or credential entry in chat.

## Request and validation contract

1. Reuse server-side authentication and CSRF checks for the new POST route. Reject unauthorized requests before validation or persistence.
2. Bound request size and accept a JSON object containing only the expected key field. Reject non-string, empty, whitespace-containing, overlong, and unexpected-field inputs. Choose bounds from the provider contract; avoid inventing a prefix or minimum length without evidence.
3. Reject setup when already configured unless explicit replacement is an intended feature. Environment-provided credentials count as configured.
4. Validate a candidate through a separate provider instance with an explicit key argument. Use a small, read-only SDK operation with explicit timeout and bounded retries; do not mutate the active provider during validation.
5. Sanitize SDK/network failures. Exception strings, request headers, telemetry, debug logging, and HTTP bodies can contain credentials; do not serialize them into responses, activity feeds, or logs.

## Persistence and activation

- Define an explicit key-file setting with a project-local default. Environment credentials take precedence; load the file on startup only when the environment key is absent.
- Write a temporary file in the destination directory with mode 0600 from creation; flush and close it before atomic publication. Keep the directory private and clean up temporary files on failure.
- Atomic replacement and no-overwrite are different guarantees. A prior existence check followed by unconditional replacement is racy. For reject-existing semantics, use atomic no-clobber publication or appropriate synchronization and rechecking; an in-process lock alone does not protect multiple workers.
- Finish validation and durable persistence before swapping the active provider. Validation or write failure must preserve the previous file and provider.
- Public state contains only configured/validation status, never the key, its prefix, or a serialized provider object. Configured is not equivalent to validated in the current process.

## Browser and reverse-proxy behavior

- Use the existing CSS, a labeled password input, an accessible status message, and a disabled submit button while pending.
- Clear the input immediately after capturing the submitted value, including failure paths. Send the value only in the authenticated POST body; never in query strings, localStorage, rendered state, or console output.
- Use relative asset and fetch URLs for subpath mounts. Verify URL resolution against a trailing-slash base such as https://private.example/connect/. The bare /connect path may require a proxy redirect to /connect/.
- Relative URLs fix browser resolution; they do not prove the proxy strips the prefix correctly, supplies HTTPS, or enforces private ingress. Report those as separate verification layers.

## Small offline regression matrix

Use the existing test runner, provider mocks, synthetic sentinel keys, and temporary directories. Do not use real credentials.

- Unauthenticated and CSRF-invalid requests fail without calling the provider or changing files.
- Malformed JSON, incorrect shapes/types, invalid lengths/whitespace, and extra fields fail.
- Successful validation publishes mode-0600 storage and activates the candidate.
- Failed validation preserves a preexisting file and active provider. If HTTP replacement is rejected earlier, exercise the lower-level validation/persistence boundary too.
- Already configured and concurrent setup attempts cannot overwrite an existing key.
- A mocked SDK exception containing the sentinel key cannot leak it through HTTP errors or public state.
- Startup respects environment-over-file precedence.
- UI success/failure clears the field and sends CSRF; asset/fetch URLs resolve below the proxy prefix.

Run baseline tests, focused safety tests, the full existing suite, and JavaScript syntax checks. Distinguish executed checks from proposed or blocked checks. If a command is denied, do not route around that denial. Return exact changed paths and test outcomes; do not claim deployed HTTPS or live credential validation from mocked tests.

## Provider-specific example

For a Composio-backed dashboard, the requested contract used POST api/settings/composio, an api_key field capped at 512 characters, COMPOSIO_API_KEY environment precedence, and CONNECT_KEY_FILE defaulting to ROOT/state/composio.key. A toolkit-listing operation is a candidate read-only validation call, but inspect the installed SDK before choosing its exact invocation. Provider identifiers and paths are examples, not universal defaults.
