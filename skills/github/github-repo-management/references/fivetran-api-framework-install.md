# Fivetran api_framework install notes

Session-derived notes for installing `https://github.com/fivetran/api_framework` locally.

## Observed shape

- Repo is a reference/example framework, not a packaged Python library.
- Root README lists only base dependencies: `requests`, `json` (stdlib), `colorama`.
- No root `pyproject.toml`, `setup.py`, or root `requirements.txt` was present during install.
- Many runnable files are examples under `examples/` and may require Fivetran credentials and resource IDs.

## Known-good local setup on macOS

```bash
mkdir -p ~/Documents/GitHub
git clone https://github.com/fivetran/api_framework.git ~/Documents/GitHub/api_framework
cd ~/Documents/GitHub/api_framework
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install requests colorama 'urllib3<2'
python -m pip check
```

`urllib3<2` avoids macOS system Python warnings like:

```text
NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with LibreSSL 2.8.3
```

## Useful local files

Create `requirements-local.txt`:

```text
requests
colorama
urllib3<2
```

Create `config.example.json`:

```json
{
  "fivetran": {
    "api_key": "TU_API_KEY",
    "api_secret": "TU_API_SECRET"
  }
}
```

Then users can copy to untracked `config.json` and fill real credentials.

## Pitfalls

- Several scripts use `r = '/config.json'`, which points to filesystem root. For repo-local usage, change it to `r = 'config.json'` before running.
- Do not run example scripts until placeholders like `connector_id`, `group_id`, etc. are filled and the user confirms side effects.
- During one compile check, these upstream files had syntax issues:
  - `examples/api_interact_cert_mgmt.py`: incomplete assignment around `limit =      #example 1-1000`
  - `examples/api_interact_sftp_pattern.py`: smart quote in `r = ‘=config.json'`

## Verification snippet

```bash
. .venv/bin/activate
python - <<'PY'
import requests, colorama, urllib3
print('OK requests', requests.__version__)
print('OK colorama', colorama.__version__)
print('OK urllib3', urllib3.__version__)
PY
python -m pip check
```
