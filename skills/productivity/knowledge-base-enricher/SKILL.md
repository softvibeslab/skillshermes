---
name: knowledge-base-enricher
description: "Analyze links/images, generate abstracts, and store in Notion and Obsidian knowledge bases."
version: 1.0.0
author: community
license: MIT
metadata:
  hermes:
    tags: [knowledge-base, notion, obsidian, analysis, abstract]
    homepage: https://hermes-agent.nousresearch.com
prerequisites:
  env_vars: [NOTION_API_KEY, OBSIDIAN_VAULT_PATH]
  optional_env_vars: [NOTION_KB_DATABASE_ID]
---

# Knowledge Base Enricher

This skill helps you analyze web pages, images, or text content, generate meaningful abstracts/summaries, and store them in both Notion and Obsidian for unified knowledge management.

## When to Use

Use when you want to:
- Save valuable online content (articles, research, tutorials) to your personal knowledge base
- Analyze images/screenshots and extract key information
- Create searchable, interconnected notes across Notion and Obsidian
- Automatically tag and organize content for easy retrieval

## Setup

### 1. Notion Configuration
1. Check if `NOTION_API_KEY` is available in:
   - Environment variables
   - Hermes memory (look for "Notion API key" in your memory)
2. If not found, create an integration at https://notion.so/my-integrations
3. Copy the API key (starts with `ntn_` or `secret_`)
4. Store it in `~/.hermes/.env`:
   ```
   NOTION_API_KEY=ntn_your_key_here
   ```
5. **Important:** Share target pages/databases with your integration in Notion
6. (Optional) Create a dedicated database for knowledge entries and set:
   ```
   NOTION_KB_DATABASE_ID=your_database_id_here
   ```
   If not set, the skill will search for or create a "Knowledge Base" database.

### 2. Obsidian Configuration
1. Check if `OBSIDIAN_VAULT_PATH` is available in:
   - Environment variables
   - Hermes memory (look for "Obsidian vault path" in your memory)
2. If not found, set your vault path in `~/.hermes/.env`:
   ```
   OBSIDIAN_VAULT_PATH=/path/to/your/vault
   ```
   Defaults to `~/Documents/Obsidian Vault` if not set.
3. Ensure the vault exists and is accessible.

### 3. Dependencies
No additional Python packages required beyond what Hermes provides.

## Workflow

The skill follows this process:
1. **Input Handling** - Accepts URL, image path, or text
2. **Content Analysis** - Uses appropriate tools to extract information:
   - URLs: Browser tools to fetch and parse web content
   - Images: Vision analysis to describe and extract text
   - Text: Direct processing
3. **Abstract Generation** - Creates a concise summary using LLM reasoning
4. **Metadata Extraction** - Identifies title, key topics, suggested tags
5. **Dual Storage** - Saves to both Notion and Obsidian with consistent formatting

## Commands & Usage

This skill is designed to be used through natural language interaction. Simply share:
- A URL: "Analyze this article: https://example.com/article"
- An image: [attach image] "What's in this diagram?"
- Text content: "Summarize and save this: [paste text]"

The skill will:
1. Process the input
2. Generate an abstract with key insights
3. Ask for confirmation/tags (if needed)
4. Save to:
   - Notion: As a page in your knowledge database
   - Obsidian: As a markdown note in your vault

## Notion Storage Format

Creates pages with these properties:
- **Name** (title): Extracted or generated title
- **Abstract** (rich_text): Generated summary
- **Source** (url): Original URL or "Image Analysis"/"Text Input"
- **Date** (date): When processed
- **Tags** (multi_select): Suggested or user-provided tags
- **Content Type** (select): URL/Image/Text
- **In Obsidian** (checkbox): Whether also saved to Obsidian

## Obsidian Storage Format

Creates markdown notes with:
```markdown
---
title: "Extracted or Generated Title"
source: "https://example.com or Image Analysis"
date: 2026-05-09
tags: [tag1, tag2, tag3]
content_type: url
in_notion: true
---

# Abstract

[Generated abstract/summary]

## Source
[Original URL or description]

## Key Insights
- [Bullet points of key takeaways]
```
Notes are stored in the vault root or a configured `knowledge-base` folder.

## Customization

You can influence the output by:
- Specifying preferred tags: "Tag this as #AI #research"
- Requesting specific formats: "Give me a bullet-point summary"
- Choosing storage location: "Only save to Obsidian for now"

## Error Handling

- **Invalid URLs**: Will notify and suggest checking the link
- **Access Denied**: For paywalled/content-restricted sites, will attempt what's possible
- **Vision Limits**: Very large images may be resized automatically
- **Quota Issues**: Will warn if Notion API limits are approached
- **Missing Credentials**: Clear instructions for setup (check memory first!)

## Example Interactions

```
User: Analyze this: https://arxiv.org/abs/2605.00123
Skill: [Processes paper, generates abstract]
Skill: Got it! Title: "Novel Approach to X". Abstract: [summary]. Tags: #AI #research #paper
Skill: Saving to Notion and Obsidian... Done!
```

```
User: [shares screenshot of architecture diagram] Explain this
Skill: [Analyzes image]
Skill: This appears to be a microservices architecture showing...
Skill: Saving analysis to knowledge base...
```

## Best Practices

1. **Batch Similar Content**: Process related links together for better tagging
2. **Review Tags**: The skill suggests tags but you can refine them
3. **Use Consistently**: Regular use builds a rich interconnected knowledge base
4. **Leverage Both Systems**: Use Notion for database/views, Obsidian for networked thinking
5. **Backup**: Regularly backup both your Notion workspace and Obsidian vault

---

## Notes

- The skill makes best-effort attempts to extract meaningful content
- For academic papers, it prioritizes abstract/methodology/conclusion
- For news/articles, it focuses on key events and implications
- For images, it describes visual elements and attempts OCR if text is present
- All stored content includes source attribution for traceability
- Tags are suggested based on content analysis but user input overrides