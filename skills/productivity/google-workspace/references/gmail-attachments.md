# Gmail attachments via the API

Use this when `google_api.py gmail send` does not expose an attachment flag. Build a MIME message with the Python standard library and send it through Gmail API.

```python
from base64 import urlsafe_b64encode
from email.message import EmailMessage
from pathlib import Path

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

attachment = Path("/absolute/path/report.zip")
message = EmailMessage()
message["To"] = "recipient@example.com"
message["Subject"] = "Report"
message.set_content("Attached.")
message.add_attachment(
    attachment.read_bytes(),
    maintype="application",
    subtype="zip",
    filename=attachment.name,
)

creds = Credentials.from_authorized_user_file(
    Path.home() / ".hermes/google_token.json"
)
service = build("gmail", "v1", credentials=creds)
result = service.users().messages().send(
    userId="me",
    body={"raw": urlsafe_b64encode(message.as_bytes()).decode()},
).execute()
print(result["id"])
```

Choose the correct MIME type for non-ZIP files. Never print token contents.

## Verification

A successful send response proves Gmail accepted the message, but verify recipient, subject, and attachment name with `messages.get(format="full")`. Attachment filenames may be nested inside multipart sections, so recurse through `payload.parts`; `format="metadata"` can omit that structure.

```python
def filenames(part):
    found = [part["filename"]] if part.get("filename") else []
    for child in part.get("parts", []):
        found.extend(filenames(child))
    return found

sent = service.users().messages().get(
    userId="me", id=result["id"], format="full"
).execute()
headers = {h["name"]: h["value"] for h in sent["payload"]["headers"]}
assert headers["To"] == "recipient@example.com"
assert attachment.name in filenames(sent["payload"])
```

If OAuth has expired, run `setup.py --auth-url`, have the user return the complete localhost redirect URL, exchange it with `setup.py --auth-code '<URL>'`, then run `setup.py --check` before sending.