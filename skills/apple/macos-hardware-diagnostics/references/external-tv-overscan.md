# External TV cropping / overscan

## Recognize and separate
- Desktop cut off at top, bottom, left, and right suggests TV overscan or a zoom picture mode, not automatically a defective Mac display.
- Distinguish cropped content from black borders (underscan), stretched aspect ratio, and merely large UI scaling.
- Keep an existing internal-panel failure as a separate incident; do not infer the same cause.

## Safe inspection and correction
1. Read `system_profiler SPDisplaysDataType`; identify the external display, primary/mirror state, resolution, and refresh rate. A rate reported for the TV is not evidence of the internal panel's rate.
2. Inspect System Settings > Displays with the external TV explicitly selected. Look for an Underscan control. If present, make one small reversible adjustment, record the original value, and read it back.
3. If no control appears in the inspected panel, say exactly that—not that macOS or the hardware can never support it. Do not cycle resolutions blindly: reducing resolution need not remove TV-side cropping.
4. Prefer native TV pixel mapping. On the active input, inspect Picture > Picture Size / Aspect Ratio / Screen / Display Area. Labels vary: Just Scan, Screen Fit, Fit to Screen, Full Pixel, Dot by Dot, 1:1. Disable Overscan / Sobreexploración or Zoom if those options exist. Do not assume plain 16:9 disables overscan.
5. Mac UI automation does not ordinarily control the TV's on-screen menus. If no authorized TV integration is available, ask for brand/model or a photo of the picture menu and give one targeted remote-control step. Do not invent a vendor-specific menu path.
6. Preserve the only readable external output: no blind unmirroring, cable disconnect, WindowServer restart, or reboot.

## Verification
- Read back any software setting actually changed.
- Ask the user to confirm the menu bar, Dock, and both horizontal edges are fully visible; a physical TV photo is stronger evidence than a screenshot because cropping can occur after the Mac generates the image.
- Mark the result as pending until physical visibility is confirmed. Finding a likely setting is not a repair.

## Inspection fallback
Use `computer_use` capture scoped to System Settings. If app matching fails, discover the localized name with `list_apps`. If labels or bounds are incomplete, query native accessibility through System Events and inspect the specific Displays content subtree. Re-resolve the window and controls from live output; do not reuse stale element indices or hardcoded nested paths across versions. An accessibility tree lacking a slider only supports 'not exposed in this inspected view.'
