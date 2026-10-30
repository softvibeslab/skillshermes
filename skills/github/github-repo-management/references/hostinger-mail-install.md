# Hostinger Mail SDK workspace

For requests to install hostinger/mail-api-{php,python,typescript}-sdk and hostinger/mail-api-cli:

1. Clone all four into a dedicated workspace without overwriting existing directories. Read manifests as well as README: Python/ PHP minimum versions in README may lag packaging requirements.
2. Python: `uv venv --python 3.12 .venv && uv pip install --python .venv/bin/python -e .`; verify `uv pip check --python .venv/bin/python`.
3. TypeScript: inspect package scripts; if no lockfile, `npm install --ignore-scripts && npm run build`; run `npm audit --omit=dev`. Use local dist/index.js for smoke check rather than global npm link.
4. PHP: PHP and Composer required; install via trusted package manager if missing. Run `composer install --no-interaction --no-scripts --no-plugins --prefer-dist`, then `composer audit`.
5. CLI: reuse installed `/opt/homebrew/bin/hostinger-mail` or `brew install hostinger/tap/hostinger-mail`; Go unnecessary when using binary distribution.
6. Auth: CLI accepts HOSTINGER_MAIL_API_TOKEN or ~/.hostinger-mail.yaml `api_token`. An existing MCP_HOSTINGER_MAIL_API_KEY may be reusable; validate via GET https://api.mail.hostinger.com/api/v1/me, never display value. Create config only if absent, with exclusive creation mode 0600. Do not overwrite existing credentials. JSON encoding is valid YAML and allows stdlib-only loading for SDK environment exports. Document that such loader expects JSON syntax.
7. SDK smoke checks: Python AccountApi.get_current_account_with_http_info returns response.status_code; use ApiClient as context manager (no public close method). TypeScript AccountApi.getCurrentAccount returns Axios response.status. PHP AccountApi.getCurrentAccount returns V1MeResource; no getCurrentAccountWithHttpInfo. Custom Guzzle client MUST set base_uri from config->getHost(), because generated request uses relative /api/v1/me. Use request timeouts and sanitized failures, not raw Axios/config exception dumps.
8. Verify CLI `account current --format json` via captured subprocess output; validate successful JSON without displaying account payload. Never send mail to verify installation.
9. Keep private configuration outside repos and generated local artifacts in .git/info/exclude. Verify git status. Leave runnable, secret-free SDK examples and concise local documentation.
