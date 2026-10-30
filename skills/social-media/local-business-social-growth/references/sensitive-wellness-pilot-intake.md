# Sensitive-wellness warm pilot intake

Use after a synthetic Top-N experiment when the next step is a real 20–30 record pilot.

## Audit the supplied workbook before claiming a pilot exists

1. Locate CSV/XLSX exports in the project directory.
2. Inspect sheet names, dimensions, headers, and populated-row counts without printing raw PII.
3. Distinguish real records from examples/placeholders. Labels such as `— EJEMPLO —`, numbered blank rows, summaries, and instruction sheets do not constitute a usable lead base.
4. Report the exact blocker: no real opt-in records, missing consent evidence, or incomplete channel/purpose fields.

When `openpyxl` is unavailable, XLSX is a ZIP of XML files. Use Python stdlib `zipfile` + `xml.etree.ElementTree` to inspect `xl/workbook.xml`, workbook relationships, and worksheet XML. Preserve cell references because blank cells may be omitted from the XML sequence.

## Minimum intake fields

Create a clean 20–30 row CSV with:

- anonymous lead ID;
- name or alias;
- source and last interaction date;
- authorized channel;
- consent status and evidence;
- self-declared objective;
- timing/readiness;
- language/timezone;
- modality and availability;
- missing data;
- do-not-contact and human-review flags;
- six scoring components, total, route, approved message, status, notes.

Do not request diagnoses, clinical notes, inferred vulnerability, private conversations, or public-post pain signals.

## Handoff sequence

1. Give the owner a short request message for the warm opt-in export.
2. Ask them to fill or export 20–30 records into the clean template.
3. Leave score/routing fields blank until eligibility is checked.
4. Rank locally and produce only the first five personalized messages for human approval.
5. Do not contact anyone merely because the user said “do it” if the base contains only examples or the exact messages/targets have not been reviewed.
6. After approval, run a small pilot and measure delivery, voluntary reply, application, appointment, attendance, confirmed sale, opt-out/block/report, and human handling time.

## Verification

- Confirm the intake file has the intended number of blank rows and stable IDs.
- Confirm the request message explicitly excludes scraping and cold outreach.
- Confirm the original workbook’s real populated-row count before saying the pilot is ready.
