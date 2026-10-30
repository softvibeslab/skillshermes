# Cursor rules library install pattern

Use when the user asks to install a GitHub repo of Cursor `.mdc` rules globally/system-wide.

## Pattern

Cursor Project Rules are project-scoped: `.cursor/rules/*.mdc` inside each repo. A GitHub collection like `PatrickJS/awesome-cursorrules` should not be blindly copied into every project or loaded all at once.

Install as a central library plus a tiny helper that copies selected rules into the active project:

```bash
DEST="$HOME/.cursor/rules/awesome-cursorrules"
if [ -d "$DEST/.git" ]; then
  git -C "$DEST" pull --ff-only
else
  mkdir -p "$(dirname "$DEST")"
  git clone --depth 1 https://github.com/PatrickJS/awesome-cursorrules.git "$DEST"
fi
```

Helper shape:

```bash
~/.local/bin/cursor-rules list
~/.local/bin/cursor-rules search <text>
~/.local/bin/cursor-rules install <text-or-file> [project]
~/.local/bin/cursor-rules update
~/.local/bin/cursor-rules path
```

`install` should copy one matched `.mdc` into `$project/.cursor/rules/`; if multiple files match, print the matches and exit instead of guessing.

## Verification

```bash
command -v cursor-rules
cursor-rules path
cursor-rules list | wc -l
cursor-rules search nextjs | head
```

## Pitfall

Do not install hundreds of `.mdc` files into a project by default. Cursor rules are context; too many generic rules add noise. Keep the collection global and install only the stack-specific rules needed for the current project.
