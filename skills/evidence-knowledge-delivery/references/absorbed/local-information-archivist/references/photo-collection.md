# Local photo collection for a named person

Use this recipe when the user asks to find all local photos of a person and prepare a clean upload folder.

## Discovery order

1. Establish identity with the strongest available reference image: an explicitly named contact/profile photo, a user-confirmed portrait, or a clearly labeled source page.
2. Check the macOS Photos library before assuming it contains originals. Inspect the library database and originals count read-only; an initialized but empty library is not evidence that no photos exist elsewhere.
3. Search filenames, Spotlight metadata/OCR, archived webpages/PDFs, screenshots, and project media folders for name variants.
4. With explicit user authorization, inspect local messaging stores read-only. Never send, edit, mark read, or mutate chat state during collection.
5. Review media near textual mentions in addition to media in the direct chat; a relevant photo may live in another conversation.

## WhatsApp on macOS

The desktop app may store chat metadata under:

`~/Library/Group Containers/group.net.whatsapp.WhatsApp.shared/ChatStorage.sqlite`

and contacts under `ContactsV2.sqlite`. Query copied databases or open them read-only. Stored attachment paths may begin with `Media/...` while physical files live under `Message/Media/...`; resolve both forms and verify file existence rather than trusting the database path literally.

The contact profile image is useful as an identity reference, but treat it as personal data and include it only when it matches the user's sharing intent.

## Confidence labels and live-app safety

Use `confirmed-face` for a visual match to a user-confirmed reference, `explicit-context` when adjacent text explicitly identifies the person, `name-ocr` for a screenshot containing the name without confirmed depiction, and `manual-review` for plausible but unverified matches. Put the last two in `REVISAR/` unless the user chooses otherwise.

Before driving Photos, WhatsApp, or another personal app, capture its current state. Never click or type in a live conversation while the user may be active; prefer read-only filesystem/export paths. Unlabeled controls and contact-header coordinates are unsafe targets. Collection does not authorize sending messages, onboarding an app, changing chats, or granting permissions. If private-data access is denied, stop that source rather than retrying by another route.

## Classification

Create contact sheets for fast visual review. Include only:

- photos where the person is clearly visible;
- promotional images directly about the person when useful to the request;
- cropped screenshots only when the crop removes irrelevant UI without changing meaning.

Exclude stickers, artwork, objects, receipts, travel screenshots, unrelated people, and ambiguous faces. A lexical mention near an image is a candidate signal, not proof.

Automated face matching is optional triage, never the sole inclusion test. If a full-library scan is slow or unstable, stop it and use bounded candidate sets from names, chats, timestamps, and source documents. Manually verify every final image against the reference.

## Packaging

For a small photo-only result, do not force the full archive directory tree. One clearly named folder with ordered filenames and a short `LEEME.txt` is enough. Record source category and exclusions without exposing contact identifiers or unrelated conversation text.

Verify every image can be decoded, then report the absolute folder path, image count, and what was excluded. Upload remotely only when the user requested it and the destination/session is known.