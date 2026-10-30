# Slack custom sidebar sections via desktop UI

Use this only when the user asks for personal sidebar organization; sections are not channels and are not managed by the normal conversations API.

## Create an empty section

1. Confirm the intended Slack workspace is active.
2. Open the context menu on any existing labeled custom section (accessibility `AXShowMenu`/right-click is more reliable than an unlabeled sidebar `+`).
3. Choose **Administrar sección → Crear una nueva sección**.
4. Enter the exact section name and keep the requested/default sorting.
5. Activate **Crear y agregar canales**.
6. On **Agrega conversaciones** (step 2), choose **Omitir** when the user requested only an empty section; otherwise select only the requested conversations and continue.
7. Recapture Slack and verify the new section heading is visible in the sidebar before reporting success.

## Accessibility fallback

- Prefer labeled AX elements and visible menu labels.
- Slack menu submenus can be opened reliably with keyboard navigation after `AXShowMenu`; recapture before selecting.
- If window bounds are reported as `0x0` or raw clicks do not land, do not keep guessing coordinates. Move focus with Tab/Shift+Tab, confirm the visible focus ring is on the intended button, then press Return.
- Reacquire references after every modal/menu transition; never reuse stale AX indices.
