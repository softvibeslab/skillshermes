# Static multi-variant workspace + knowledge base + GitHub Wiki

Use when a public static site has accumulated several HTML variants, media exports, design research, and origin notes across multiple local folders, and the user wants one durable GitHub workspace without mixing product artifacts and knowledge.

## Minimal architecture

```text
repo/
├── README.md
├── workspace/
│   ├── index.html
│   ├── variants/<variant>/index.html
│   ├── deliverables/<type>/index.html
│   └── media/{final,production}/
├── knowledge-base/
│   ├── README.md
│   ├── overview/
│   ├── product/
│   ├── content-strategy/
│   ├── design/
│   ├── production/
│   ├── sources/
│   └── decisions/
├── archive/original-live-layout/
└── scripts/validate_workspace.py
```

- `workspace/` is for runnable/presentable artifacts.
- `knowledge-base/` is canonical, reviewable documentation and provenance.
- `archive/` preserves the exact live layout before restructuring.
- GitHub Wiki is a navigation and summary layer; it links to canonical repo documents rather than duplicating long text.

## Workflow

1. **Inventory before moving**
   - Search the current site directory, nearby knowledge/product folders, note vaults, and relevant session history.
   - Record source path, type, size/checksum, destination, and one state: `publish`, `sanitize`, `release-only`, or `exclude`.
   - Compare similarly named versions by checksum/content before treating them as distinct variants.

2. **Gate privacy and rights**
   - Scan HTML/Markdown/scripts for secrets, personal data, private URLs, client names, and embedded contact details.
   - Sanitize private transcripts and business context into summaries; do not publish raw messaging audio by default.
   - Summarize/adapt third-party methods with provenance; do not mirror full proprietary source documents without permission.
   - Do not invent a license. Leave `LICENSE` pending until the owner chooses one.

3. **Preserve the live site**
   - Copy the current deployed layout intact under `archive/original-live-layout/` and verify checksums.
   - Reorganizing GitHub must not silently change or redeploy the live Hostinger/static site. Treat deployment as a separate authorized task.

4. **Separate variants from deliverables**
   - A variant is an alternative runnable experience and gets its own folder with `index.html` and required assets.
   - Presentation, brochure, guide, infographics, and editorial dashboards are deliverables, not fake product variants.
   - Duplicate assets only when required to make a variant independently portable; otherwise share or archive them.
   - Add a root `workspace/index.html` launcher describing variant purpose and maturity.

5. **Handle media deliberately**
   - Track compact final media and only production sources needed for reproducibility.
   - Exclude caches, `.DS_Store`, compiled bytecode, contact sheets, and regenerable segment noise.
   - Put distributable ZIPs on a GitHub Release instead of duplicating them in Git history.

6. **Build the knowledge base**
   - Capture project origin, message/promise, operating model, roles, human-control rules, evidence/metrics, content strategy, visual evolution, production, source register, and architecture decisions.
   - Label facts, design decisions, hypotheses, illustrative metrics, and source confidence separately.
   - Keep public generic messaging free of client/project names unless disclosure is explicitly intended.

7. **Create the Wiki correctly**
   - Enable the repository Wiki and initialize `<owner>/<repo>.wiki.git`.
   - Add `Home.md`, `_Sidebar.md`, and concise topic pages.
   - Link Wiki pages to canonical `knowledge-base/` documents; avoid parallel long-form copies that drift.
   - Clone/read back the Wiki and verify public links.

8. **Leave one runnable check**
   - Use a stdlib script to verify each variant has `index.html`, relative resources exist, Markdown has no private local paths, forbidden generated files are absent, and no oversized files/common secret patterns are tracked.
   - Serve `workspace/` locally and inspect every variant, video, 3D asset, console, mobile layout, keyboard focus, and reduced-motion behavior.

9. **Publish with proof**
   - Push only after manifest/privacy review and validator success.
   - Verify local HEAD equals remote HEAD, README renders, Wiki loads, and release assets are downloadable.

## Common pitfalls

- Treating the Wiki as the source of truth; its separate Git repo drifts easily.
- Calling every HTML file a “version” when some are brochures or guides.
- Moving the current live layout before preserving/verifying it.
- Publishing raw WhatsApp audio, family/client context, or third-party methodology because it was locally available.
- Tracking ZIPs and all their expanded contents together.
- Sharing assets across variants that were requested to be independently portable.
