# Macs Fan Control on macOS

## Installation and launch

```sh
brew install --cask macs-fan-control
open -a 'Macs Fan Control'
```

The app bundle is normally `/Applications/Macs Fan Control.app`.

## Built-in preset keys

Preferences use `com.crystalidea.macsfancontrol`:

- `Predefined:0` — Automatic
- `Predefined:1` — Full blast

Read the preset:

```sh
defaults read com.crystalidea.macsfancontrol ActivePreset
```

If GUI automation is unavailable and the user explicitly requested Full blast, stop the app, write the preset, and relaunch:

```sh
pkill -x 'Macs Fan Control'
defaults write com.crystalidea.macsfancontrol ActivePreset -string 'Predefined:1'
open -a 'Macs Fan Control'
```

Return to system control with `Predefined:0` using the same sequence.

## Privileged helper and verification

Expected artifacts after user-authorized setup:

- `/Library/PrivilegedHelperTools/com.crystalidea.macsfancontrol.smcwrite`
- `/Library/LaunchDaemons/com.crystalidea.macsfancontrol.smcwrite.plist`
- `system/com.crystalidea.macsfancontrol.smcwrite`

```sh
defaults read com.crystalidea.macsfancontrol ActivePreset
pgrep -fl 'Macs Fan Control'
launchctl print system/com.crystalidea.macsfancontrol.smcwrite
```

A running app, Full blast preset, and helper show that the override is configured and capable of writing fan controls. They do not measure RPM; use a readable sensor or the app UI for that claim.

## Interpretation

- `pmset -g therm` reports thermal/performance warning history.
- `system_profiler SPPowerDataType` may expose battery temperature and power modes.
- Apple silicon may not expose useful legacy fan RPM/CPU temperature keys through `ioreg -c AppleSMC`.
- `powermetrics --samplers smc` generally requires administrator authorization.
- High Power Mode can increase heat and is not equivalent to Full blast fans.