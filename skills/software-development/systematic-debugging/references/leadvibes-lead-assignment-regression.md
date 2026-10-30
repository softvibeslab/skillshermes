# LeadVibes lead assignment regression debugging note

## Context

During LeadVibes leads-module work, new UI support for `assigned_broker_id` initially made existing assignments appear lost. The data was not necessarily deleted; the regression was in data flow and UI wiring.

## Root cause pattern

When adding assignment/responsible UI to an existing page, verify both persisted IDs and hydrated display objects:

- List endpoint `/leads` may return `assigned_broker_id` without `assigned_broker`; detail endpoint may hydrate `assigned_broker` separately.
- UI cards/tables/modals may rely on a local broker roster; if `brokers` is not passed through every render path, labels fall back to `Sin asignar` or `Usuario no encontrado`.
- Legacy workspaces may not have membership records yet; `/brokers` built only from memberships can return `[]` even when old users exist in `users`.
- Backend update code that filters out `None` values can prevent clearing an assignment intentionally; use `model_dump(exclude_unset=True)` and preserve explicit `assigned_broker_id: null` only when sent.

## Fix checklist

1. Inspect `git diff` and search for assignment references across backend + frontend.
2. Ensure backend lead update distinguishes omitted fields from explicit null:
   ```python
   raw_update_data = lead_data.model_dump(exclude_unset=True)
   update_data = {k: v for k, v in raw_update_data.items() if v is not None}
   if "assigned_broker_id" in raw_update_data:
       update_data["assigned_broker_id"] = raw_update_data["assigned_broker_id"]
   ```
3. Enrich list responses when UI needs display labels:
   - collect `assigned_broker_id` from returned leads
   - fetch matching users
   - attach `assigned_broker` to each serialized lead
4. Thread broker roster through every frontend path:
   - Kanban column -> lead card
   - drag overlay
   - table view
   - detail modal
   - new lead modal
5. Add legacy fallback to roster builders when membership tables are empty, using tenant users with broker-like roles.
6. Validate minimally when build tooling is broken:
   - Python: `python3 -m py_compile backend/server.py backend/models.py`
   - JS/JSX syntax: parse target file with `@babel/parser`

## User-facing note

If the user says “se perdió la asignación”, treat it as a data-preservation regression until proven otherwise. Avoid saying it is merely visual until checking persistence and response shape.