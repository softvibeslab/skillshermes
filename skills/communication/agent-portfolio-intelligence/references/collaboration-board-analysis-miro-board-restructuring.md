# Miro board restructuring runbook

Use this when the user explicitly asks to rewrite, clean, or realign an existing Miro board—not merely analyze it.

## Safe sequence

1. Read the project's canonical sources before touching the board. Prefer durable briefs, wikis, manifests, and verified runtime evidence over old board text.
2. Inventory the board completely: items, connectors, groups, mind maps, tables, frames, and unsupported object types.
3. Copy the board before destructive cleanup. Verify the copy by reading its metadata and confirming the original item total.
4. Design the replacement as a small decision system: current decision, proposition, user/research, MVP flow, roles, architecture, roadmap/gates, blockers, metrics, and later vision.
5. Build the replacement plan offline and assert frame titles/counts before writing.
6. Clear connectors and ordinary items first; delete container-owned objects through their container endpoints:
   - delete groups with `deleteItems=true`;
   - delete a mind-map root through the mind-map endpoint so descendants cascade;
   - delete frames last so children do not become difficult to reconcile.
7. Create frames, then their summaries and cards. Keep all operational content parented to a frame.
8. Rename and describe the board with the canonical source and backup board ID.
9. Re-fetch the complete board and verify counts, frame titles, parent relationships, connectors, and unexpected legacy remnants.

## Miro REST details

### Parent-relative coordinates

When `parent: {"id": frame_id}` is supplied on a text or sticky-note create request, `position.x/y` are coordinates relative to the frame's top-left, not canvas coordinates. A safe layout for a 3300×2900 frame is:

```text
summary:  x=1650, y=300
cards:    (850,800), (2450,800),
          (850,1500), (2450,1500),
          (850,2200), (2450,2200)
```

Check each child's half-width/half-height against the frame bounds; otherwise Miro returns `new position is outside of parent boundaries`.

### Sticky-note geometry

Sticky notes have a fixed aspect ratio. Send only `geometry.width` or only `geometry.height`, never both. For example:

```json
{"geometry": {"width": 1250}}
```

### Color values

Prefer values accepted by Miro's current sticky-note schema: `gray`, `light_yellow`, `yellow`, `orange`, `light_green`, `green`, `dark_green`, `cyan`, `light_pink`, `pink`, `violet`, `red`, `light_blue`, `blue`, `dark_blue`, `black`. Do not assume wrapper aliases are accepted by raw REST calls.

### Legacy containers

Generic `DELETE /items/{id}` is not reliable for all imported objects:

- mind-map descendants can return “part of mind map”; delete the root through the mind-map endpoint;
- grouped shapes can return `operationNotSupported`; delete their group with `deleteItems=true`;
- imported tables may expose a read endpoint but no supported delete or move operation through REST. Preserve them in the verified backup and report any remnants honestly; use authenticated UI deletion only when the user approves and UI control is available.

Do not encode these as permanent tool failures: they are object-type and endpoint constraints that may change.

## Verification contract

A successful rebuild should establish:

- backup total equals original pre-cleanup total;
- replacement frame count and titles match the plan;
- every new summary/card has a parent frame;
- no accidental orphan from a failed partial run;
- connector total matches the intended design;
- any residual legacy objects are counted by type and disclosed;
- board name, description, source references, and backup ID are readable through metadata.

If a write fails mid-frame, delete that newly created frame before retrying so its children cascade and the rebuild stays idempotent.
