# Behance Discovery Integration Options

Research snapshot: 2026-08-29. Re-check live status before installing or calling any integration.

## Recommended ladder

1. **Configured design-inspiration MCP (Serper-backed)** — preferred automated discovery. It searches Google's index with `site:behance.net`, returns image/source URLs, and avoids running a Behance crawler from Hermes.
2. **Existing Apify MCP** — use `maximedupre/behance-dribbble-scraper` only when current source policy permits direct automated access. Keep `platform=behance`, `targetType=discover`, `maxItems=10`, no pagination by default.
3. **Canonical Behance search URL** — always available: `https://www.behance.net/search/projects/{URL_ENCODED_QUERY}`. Ask el operador for screenshots/exports of selected results for verified visual analysis.
4. **Curated catalog** — rank the 28 preserved Agentic OS links even when live discovery is unavailable.

Do not install or use a downloader merely to build inspiration. Search metadata plus selected screenshots is enough; bulk project-image downloads add copyright, storage, and source-policy risk without improving the design brief.

## Option assessment

| Option | What it provides | Requirements | Verdict |
|---|---|---|---|
| YonasValentin/design-inspiration-mcp-server | `design_search_images`, `design_search_references`, `design_search_styles`; searches Behance, Dribbble, Awwwards, Mobbin, and Pinterest through Serper; optional live-site token extraction | Node, local clone/build, `SERPER_API_KEY`; `dembrandt` only for token extraction | **Preferred MCP discovery**. Multi-source, visual URLs, structured output, MIT. Do not extract tokens from Behance project pages; use token extraction on ordinary live websites only when permitted. |
| Arnonfr/behance-mcp-server | Direct Puppeteer scraping for projects, profiles, images, jobs, and details; seven tools; no API key | Node 18+, clone/build, Chromium/Puppeteer | **Do not enable by default.** Direct crawler conflicts with the current AI-bot restriction; tiny/new repository (created 2026-03-30, one star at review). Keep only as a future option if Behance policy changes and a code/security review passes. |
| maxmedupre/behance-dribbble-scraper (Apify) | Discovery, direct projects/shots, profiles, tags, metrics, image URLs; maxItems and field/tool filters | Existing Apify MCP/auth; paid per item ($0.0045 free-tier event price observed) | **Best operational scraper fallback**, but direct use remains gated by current Behance policy. Small adoption at review (14 total, 5 monthly users). Prefer 10 results, not its default 25. |
| jupri/behance-scraper (Apify) | Broad all-in-one extraction: projects, images/assets, profiles, freelancers, services, jobs, comments | Apify; $25/month rental with 3-day trial observed | **Skip for this use case.** Too broad, expensive, zero monthly users at review, and encourages asset harvesting we do not need. |
| promisefemi/behance-downloader | Go CLI/web app that downloads full Behance projects; live Fly app returned HTTP 200 | Go or hosted form | **Skip.** Downloader, not discovery/search; no repository license detected; last push observed 2024-01-18; project assets should not enter the inspiration library. |
| Polyneue/behance-api | Node wrapper for legacy Behance API endpoints: projects, users, teams, collections, fields | Historical Behance API key/API availability | **Do not implement.** Last push observed 2020-11-21 and docs target Behance's old developer API. Useful only as endpoint history. |
| Direct Behance URL | Native search page with exact query in path | Browser and URL encoding | **Reliable fallback and current default** while no Serper key is configured. |

## Current source-policy fact

At review time, `https://www.behance.net/robots.txt` listed `GPTBot`, `ClaudeBot`, `Claude-Web`, `anthropic-ai`, and other named AI bots with `Disallow: /`. It also disallowed selected filtered search routes for general crawlers. Therefore:

- do not directly crawl Behance from this agent;
- do not use the Arnon MCP or downloader under the current policy;
- do not ask Apify to bypass CAPTCHA, bot controls, login, or rate limits;
- indirect search-index results may be used as metadata, but visual claims still require an image supplied or deliberately selected for analysis;
- stop on 403, 429, CAPTCHA, or access warnings.

## Hermes setup for the preferred MCP

Only after el operador provides/configures a Serper key:

```bash
git clone https://github.com/YonasValentin/design-inspiration-mcp-server.git ~/.hermes/mcp/design-inspiration-mcp-server
cd ~/.hermes/mcp/design-inspiration-mcp-server
npm install
npm run build
hermes mcp add design-inspiration \
  --command node \
  --args ~/.hermes/mcp/design-inspiration-mcp-server/dist/index.js
```

Put `SERPER_API_KEY` in `~/.hermes/.env` or the MCP server's explicit `env` config; never paste it into SKILL.md. Then run:

```bash
hermes mcp test design-inspiration
```

Restart Hermes or use `/reload-mcp`, then verify that `mcp_design_inspiration_design_search_images` (or the discovered equivalent) appears. Do not install `dembrandt` unless website token extraction is actually requested.

## Saved source links

- https://github.com/promisefemi/behance-downloader/
- https://behance-downloader.fly.dev/
- https://apify.com/maximedupre/behance-dribbble-scraper/api/cli
- https://apify.com/jupri/behance-scraper/api/mcp
- https://glama.ai/mcp/servers/Arnonfr/behance-mcp-server
- https://glama.ai/mcp/servers/Arnonfr/behance-mcp-server/tools/search_behance_projects
- https://glama.ai/mcp/servers/Arnonfr/behance-mcp-server/tools/search_behance_profiles
- https://glama.ai/mcp/servers/Arnonfr/behance-mcp-server/tools/get_behance_project_details
- https://glama.ai/mcp/servers/Arnonfr/behance-mcp-server/tools/get_behance_jobs
- https://glama.ai/mcp/servers/Arnonfr/behance-mcp-server/tools/get_behance_job_details
- https://glama.ai/mcp/servers/YonasValentin/design-inspiration-mcp-server
- https://glama.ai/mcp/tools?query=Behance
- https://github.com/Polyneue/behance-api/blob/main/docs/API.md
