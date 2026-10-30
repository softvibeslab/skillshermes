#!/usr/bin/env bash
set -euo pipefail

: "${PUBLIC_URL:?Set PUBLIC_URL, e.g. https://example.ngrok.app}"
: "${TUNNEL_USER:?Set TUNNEL_USER}"
: "${TUNNEL_PASSWORD:?Set TUNNEL_PASSWORD}"
: "${ADMIN_TOKEN:?Set ADMIN_TOKEN}"

DASHBOARD_PATH="${DASHBOARD_PATH:-/}"
PROTECTED_PATH="${PROTECTED_PATH:-/api/admin/status}"
ADMIN_HEADER="${ADMIN_HEADER:-X-Admin-Token}"

status() {
  curl --silent --show-error --output /dev/null --write-out '%{http_code}' \
    --max-time 15 "$@"
}

printf 'outer_auth_missing=%s\n' "$(status "${PUBLIC_URL}${DASHBOARD_PATH}")"
printf 'dashboard_authenticated=%s\n' "$(status --user "${TUNNEL_USER}:${TUNNEL_PASSWORD}" "${PUBLIC_URL}${DASHBOARD_PATH}")"
printf 'app_auth_missing=%s\n' "$(status --user "${TUNNEL_USER}:${TUNNEL_PASSWORD}" "${PUBLIC_URL}${PROTECTED_PATH}")"
printf 'fully_authenticated=%s\n' "$(status --user "${TUNNEL_USER}:${TUNNEL_PASSWORD}" --header "${ADMIN_HEADER}: ${ADMIN_TOKEN}" "${PUBLIC_URL}${PROTECTED_PATH}")"
