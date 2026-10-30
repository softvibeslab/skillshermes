# Chrome multi-profile and multi-process disambiguation

Use this when a task must operate in the user's already-authenticated Chrome profile.

## 1. Detect ambiguity first

Call `computer_use(action="list_apps")`. If more than one `Google Chrome` process exists, treat `app="Google Chrome"` as ambiguous: input and capture may land on different processes or windows.

Do not type or submit until the post-action capture shows the expected page.

## 2. Resolve profile name to directory

Chrome stores the stable mapping in:

`~/Library/Application Support/Google/Chrome/Local State`

Read `profile.info_cache`. Each key is a directory such as `Default` or `Profile 3`; each value contains the human-visible profile `name` and often `user_name`.

Example probe:

```python
import json
from pathlib import Path

state = Path.home() / "Library/Application Support/Google/Chrome/Local State"
for directory, profile in json.loads(state.read_text())["profile"]["info_cache"].items():
    print(directory, profile.get("name"), profile.get("user_name"))
```

Launch using the resolved directory, not a guessed card position:

```sh
open -a "Google Chrome" --args --profile-directory="Profile 3" "https://example.com"
```

## 3. Verify the exact target

After launch, capture again and confirm all three:

1. Expected site/page title.
2. Expected Chrome profile identity where visible.
3. No permission, password, payment, or 2FA dialog.

If capture jumps to an unrelated normal/incognito window, stop and disambiguate with platform-native window enumeration. Do not keep retrying coordinates.

## Pitfalls

- A profile-picker card may be visible but partly covered by a fixed footer; coordinate clicks can hit the wrong layer.
- A successful click transport only proves the event was posted, not that the intended process handled it.
- `open --profile-directory` can be routed to an already-running Chrome singleton; verification is mandatory.
- Never kill or close a Chrome process until its windows are verified as disposable.
