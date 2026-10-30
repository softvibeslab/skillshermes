# Miro API analysis notes

Use these notes when a Miro MCP toolset is available but a complete-board analysis requires pagination or geometry processing.

## Resolve share links

A `miro.com/welcomeonboard/...` invitation can redirect to:

```text
https://miro.com/app/board/<BOARD_ID>/?inviteKey=...
```

Use the resulting `<BOARD_ID>` for MCP/API calls. Resolving the URL is read-only; accepting invitations or changing membership is a separate action.

## Validate access

Minimum read validation:

1. List accessible boards.
2. Read the target board metadata.
3. Read a valid item page (`limit` may have a server-enforced minimum).
4. Confirm the current membership role.

Do not use `list_resources` as the sole health check. MCP resource discovery and Miro domain tools are separate capabilities.

## Pagination

Miro v2 item lists use cursor pagination. Follow `body.links.next` exactly until absent:

```python
items = []
url = f"https://api.miro.com/v2/boards/{quoted_board_id}/items?limit=50"
while url:
    body = get_json(url)
    items.extend(body.get("data", []))
    url = (body.get("links") or {}).get("next")
assert len(items) == body["total"]
```

If an MCP wrapper only exposes `offset`, compare returned IDs. Some wrappers may repeatedly fetch the first cursor page despite a changing offset. In that case, use the authenticated REST endpoint for read-only bulk extraction.

Connectors are separate:

```text
GET /v2/boards/{board_id}/connectors
```

Do not conclude there are no connectors from `/items` alone.

## Token handling

Hermes MCP server config may reference an environment variable rather than contain the literal credential, for example `${MIRO_ACCESS_TOKEN}`. For local scripts, read the resolved process environment instead of sending the placeholder.

Never print the token. Report only whether the variable exists, and keep extraction output free of headers or credentials.

## Useful normalized record

For each item retain:

```text
id, type, cleaned_text, parent_id, x, y, width, height,
created_at, modified_at, created_by, modified_by
```

Normalize HTML with standard-library parsing or conservative tag removal. Preserve paragraph boundaries when possible because long Miro text often encodes headings and tables inside HTML.

## Board-quality metrics

Calculate:

- total objects and counts by type;
- total connectors separately;
- titled versus untitled frames;
- objects with and without parent/frame;
- empty cards/stickies/placeholders;
- exact normalized-text duplicate groups;
- coordinate bounds and extreme outliers;
- dense spatial clusters;
- creators and creation-time concentration;
- cards with assignee and due date;
- long text blocks that should become summary + detail.

## Interpretation cautions

- A bulk-import timestamp across most objects indicates provenance, not necessarily current validity.
- A named project appearing in one cluster does not make every template elsewhere on the canvas project evidence.
- Numeric projections in example businesses must remain isolated from the active project's analysis.
- Unsupported item types can still contribute visual structure; count them and avoid destructive cleanup recommendations without rendered confirmation.
