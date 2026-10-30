# APFS Storage Audit Reference

Use this as a read-only probe and interpretation checklist. Adapt depth and timeouts to the machine; deep `du` scans can take minutes.

## Baseline

```sh
sw_vers
system_profiler SPHardwareDataType -detailLevel mini
df -h
diskutil info /
tmutil listlocalsnapshots /
diskutil apfs listSnapshots /
sysctl vm.swapusage
uptime
```

Interpretation:

- APFS system and Data volumes share a container.
- The Data volume near 95–100% indicates urgent pressure even if `/` looks less full.
- OS update snapshots are not ordinary cleanup targets.
- Swap may disappear after restart and return under the same workload.

## Progressive size scan

```sh
du -x -k -d 1 "$HOME" 2>/dev/null | sort -nr
du -x -k -d 1 "$HOME/Library" 2>/dev/null | sort -nr
du -x -k -d 1 "$HOME/Library/Containers" 2>/dev/null | sort -nr
du -x -k -d 1 "$HOME/Library/Group Containers" 2>/dev/null | sort -nr
du -x -k -d 1 "$HOME/Library/Caches" 2>/dev/null | sort -nr
du -x -k -d 1 "$HOME/Library/Application Support" 2>/dev/null | sort -nr
```

Stop drilling when a branch is small enough not to matter. Keep output bounded to the largest entries.

## Sparse-file check

For Docker, Colima, emulator, or VM disk images:

```sh
ls -lskh /path/to/image
du -h /path/to/image
du -Ah /path/to/image
```

- `du -h`: allocated blocks.
- `du -Ah`: apparent/logical size.
- A huge apparent value with modest allocated value is normal for a sparse image.

## Duplicate confirmation

```sh
cmp -s /path/to/candidate-a /path/to/candidate-b && echo IDENTICAL
```

Confirm which copy the application references. Prefer removing redundant Downloads copies. APFS clones can make the displayed duplicate size larger than the actual recovered space.

## Runtime inventories

```sh
ollama list
lms ls
docker system df -v
```

Some commands start their owning service. Check service state before invoking a command that may auto-start it in a read-only audit. Do not stop an application the user already had running. Docker inspection requires its daemon: check `docker context show` first, and if the daemon is stopped, request approval before starting it because restart-policy containers may launch. Until then, distinguish known allocated disk size from unknown reclaimable contents.

## Developer-artifact preflight

Before removing a large `build`, `target`, cache, dependency tree, or virtual environment:

```sh
git -C /path/to/repo status --short
pgrep -fl 'gradle|flutter|cargo|node|npm|pnpm|yarn'
git -C /path/to/repo check-ignore -q build && echo GENERATED_OR_IGNORED
```

Confirm a lockfile or documented rebuild command exists. Prefer a package manager's cache-only purge, but avoid framework `clean` tasks when they must configure the project first: Gradle and similar tools may download toolchains or SDK components merely to reach the cleanup task. For clearly ignored generated directories, direct removal is the lower-side-effect operation. Re-run `git status` afterward to prove tracked source was untouched.

## Cleanup safety matrix

| Class | Default action | Risk |
|---|---|---|
| Swap | Restart/close heavy apps | Temporary savings only |
| Package caches | Native cleanup command | Re-download later |
| App caches | Close app, clear selected cache | Slower first launch |
| Downloaded installers | Remove after app installed | Low |
| Verified duplicate downloads | Remove download copy | APFS may reclaim less |
| Build/target directories | Verify generated/ignored status and rebuild path; remove approved exact output directories when framework clean would configure/download dependencies | Rebuild required; confirm no active build |
| `node_modules` / virtualenv | Remove only with lockfile/rebuild command | Reinstall required |
| Chat media | In-app manage-storage UI | User content selection |
| Docker images/build cache | Inspect, prune selected unused data | Re-pull/rebuild |
| Docker volumes | Preserve unless explicitly approved | Data loss |
| Local models | Remove through runtime after dependency check | Re-download, agent breakage |
| Android emulators | Remove unused AVD in Device Manager | Emulator state loss |
| Cloud/File Provider data | Remove Download/disconnect after remote verification | Sync/data-loss risk |
| Parallels VM | Compact in Parallels | Never delete `.pvm` casually |
| App containers/databases | Preserve/use owning app | High data-loss risk |
| Source and `.git` | Preserve | High project-loss risk |

## Savings math

Separate findings into:

- **Temporary:** swap and purgeable runtime state.
- **Durable/reconstructible:** caches, installers, verified duplicates, generated outputs.
- **Optional/high-impact:** chat media, models, VMs, container runtimes, emulators.

Do not add overlapping parent and child directories. Present upper bounds as estimates and verify the actual result with:

```sh
df -h /
diskutil info /
```
