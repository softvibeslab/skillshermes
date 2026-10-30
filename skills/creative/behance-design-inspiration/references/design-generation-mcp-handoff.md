# Design-Generation MCP Handoff

Use this after Behance research has produced an original visual direction and the user wants screens, not only analysis.

## Detection

Check whether a design-generation MCP is already registered and authenticated. Stitch is one example; keep the workflow provider-neutral because tool names and schemas vary.

Route in this order:

1. Registered and authenticated design MCP: generate through it.
2. Registered but unauthenticated: give the user the shortest local credential setup step; continue producing the screen map and prompts while blocked.
3. No design MCP: deliver wireframes, design tokens, or implementation directly with available tools.

Never request, repeat, persist, or test an API key pasted into chat. Treat it as exposed, ask the user to rotate it, and reference secrets from local environment variables in MCP configuration.

## Prompt Package

Translate the synthesis into a compact provider-ready package:

- product, audience, platform, and primary job;
- screen name and success state;
- hierarchy and navigation model;
- required components and states;
- color and type roles;
- signature element and deliberate restraint;
- accessibility constraints;
- explicit exclusions that prevent cloning Behance sources.

Do not include creator assets, copied layouts, or vague style requests such as “make it Behance-like.”

## Lazy Generation Sequence

1. Generate the hardest or most representative screen first.
2. Request at most two materially different variants.
3. Review hierarchy, task clarity, interaction states, responsive behavior, accessibility, and originality.
4. Select one direction before generating the remaining screen family.
5. Preserve the winning prompt package and source URLs; do not preserve downloaded Behance assets.

This avoids spending generation cycles on a direction the user has not approved.

## Output

Return:

1. MCP/provider used and authentication state.
2. Screen generated and why it was chosen first.
3. Variant differences.
4. Review verdict and recommended winner.
5. Remaining screen map.
6. Fallback artifact delivered if generation was blocked.
