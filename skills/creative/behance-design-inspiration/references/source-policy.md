# Behance Source Policy

## Current restriction

At the time this collection was created, `https://www.behance.net/robots.txt` explicitly disallowed multiple named AI bots from accessing `/`. Therefore this skill must not automate broad Behance scraping, pagination, project-asset downloads, or bulk visual extraction while that restriction remains.

Check the current file at runtime because policies can change.

## Permitted workflow under restriction

1. Use el operador's local catalog of canonical links and notes.
2. Generate URL-encoded Behance search links for el operador to open normally.
3. Use a general search-index MCP (for example Serper with `site:behance.net`) for discovery metadata and source links; label it `search-index metadata`, not a direct Behance observation.
4. Analyze screenshots, exports, or selected thumbnails that el operador deliberately shares or approves.
5. Store links, tags, evidence labels, and original analysis—not copied project assets.
6. Credit verified creators and source URLs.

## Prohibited behavior

- Bypassing login, CAPTCHA, rate limits, or bot controls.
- Pretending title-derived tags are visual observations.
- Downloading full project images into the skill repository.
- Recreating logos, illustrations, copy, exact palettes, or exact screen layouts.
- Treating appreciation/view counts or featured placement as proof of usability.

## If the policy changes

Use the minimum permitted access:

- one search page;
- no pagination by default;
- at most three selected project pages;
- polite rate limits;
- no asset redistribution;
- stop immediately on 403, 429, CAPTCHA, or access warnings.

## Attribution template

`Reference: [project title] by [verified creator], Behance, [canonical URL]. Adapted principle: [principle]. No project assets copied.`
