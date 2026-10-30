---
name: obsidian
description: Read, search, create, and edit notes in the Obsidian vault.
---

# Obsidian Vault

Use this skill for filesystem-first Obsidian vault work: reading notes, listing notes, searching note files, creating notes, appending content, and adding wikilinks.

## Vault path

Use a known or resolved vault path before calling file tools.

The documented vault-path convention is the `OBSIDIAN_VAULT_PATH` environment variable, for example from `~/.hermes/.env`. If it is unset, use `~/Documents/Obsidian Vault`.

File tools do not expand shell variables. Do not pass paths containing `$OBSIDIAN_VAULT_PATH` to `read_file`, `write_file`, `patch`, or `search_files`; resolve the vault path first and pass a concrete absolute path. Vault paths may contain spaces, which is another reason to prefer file tools over shell commands.

If the vault path is unknown, `terminal` is acceptable for resolving `OBSIDIAN_VAULT_PATH` or checking whether the fallback path exists. Once the path is known, switch back to file tools.

## Read a note

Use `read_file` with the resolved absolute path to the note. Prefer this over `cat` because it provides line numbers and pagination.

## List notes

Use `search_files` with `target: "files"` and the resolved vault path. Prefer this over `find` or `ls`.

- To list all markdown notes, use `pattern: "*.md"` under the vault path.
- To list a subfolder, search under that subfolder's absolute path.

## Search

Use `search_files` for both filename and content searches. Prefer this over `grep`, `find`, or `ls`.

- For filenames, use `search_files` with `target: "files"` and a filename `pattern`.
- For note contents, use `search_files` with `target: "content"`, the content regex as `pattern`, and `file_glob: "*.md"` when you want to restrict matches to markdown notes.

## Create a note

Use `write_file` with the resolved absolute path and the full markdown content. Prefer this over shell heredocs or `echo` because it avoids shell quoting issues and returns structured results.

## Organize notes by topic

For better knowledge organization, create notes in thematic folders rather than the root vault:

- Use descriptive folder names like `AI Tools/`, `Research/`, `Projects/`, etc.
- When creating a note, include the full path: `vault_path/Folder/Note Title.md`
- Create folders as needed by including them in the path

## Append to a note

Prefer a native file-tool workflow when it is not awkward:

- Read the target note with `read_file`.
- Use `patch` for an anchored append when there is stable context, such as adding a section after an existing heading or appending before a known trailing block.
- Use `write_file` when rewriting the whole note is clearer than constructing a fragile patch.

For an anchored append with `patch`, replace the anchor with the anchor plus the new content.

For a simple append with no stable context, `terminal` is acceptable if it is the clearest safe option.

## Targeted edits

Use `patch` for focused note changes when the current content gives you stable context. Prefer this over shell text rewriting.

## Wikilinks

Obsidian links notes with `[[Note Name]]` syntax. When creating notes, use these to link related content.

## Best practices for research notes

When documenting tools or research findings:

1. **Structure**: Use consistent headings for easy scanning
2. **Source attribution**: Always note where information came from (URL, date, source)
3. **Action items**: Clearly mark any follow-up steps needed
4. **Links**: Use both markdown links `[text](url)` and wikilinks `[[Related Note]]` appropriately
5. **Tags**: Use Obsidian tags `#topic` for cross-referencing when folder structure isn't sufficient
6. **AI Tool Discovery**: For AI tools discovered via social media (Instagram, Twitter/X, etc.), explicitly document:
   - Exact access method (e.g., "Comment 'CODING' on post to get link via DM")
   - Platform and creator handle
   - Date discovered
   - Any required engagement steps

Example structure for tool documentation:

```markdown
# Tool Name

**Source:** Platform description with URL and date (e.g., Instagram reel from @username [link](...))

## Description
Brief description of what the tool does

## Key Features
- Feature 1
- Feature 2

## Access Method
Specific steps to obtain access (e.g., "Comment 'CODING' on the Instagram post to receive the access link via direct message")

## Status
Current availability status (e.g., "⚠️ Investigation required - official website not publicly discoverable")

## Related
- [[Related Tool/Concept]]
- #tag-name
```

This approach ensures research is discoverable and-actionable in future sessions.