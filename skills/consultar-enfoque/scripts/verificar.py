"""Check the local Enfoque installation without displaying credentials."""
from pathlib import Path
import json
import stat
import yaml

root = Path.home() / '.hermes'
profile = root / 'profiles/enfoque'
config = yaml.safe_load((profile / 'config.yaml').read_text())
assert config['model']['provider'] == 'openai-codex'
assert config.get('platforms') == {}
assert config.get('mcp_servers') == {}
assert not (profile / '.env').exists(), 'Unexpected messaging/environment credentials'
assert (profile / 'workspace').is_dir()
assert not (profile / 'gateway.pid').exists(), 'Unexpected gateway'
auth_path = profile / 'auth.json'
auth = json.loads(auth_path.read_text())
assert set(auth.get('providers', {})) == {'openai-codex'}
# Hermes may initialize empty pools for auto-detected providers.
assert {k for k, v in auth.get('credential_pool', {}).items() if v} <= {'openai-codex'}
assert stat.S_IMODE(auth_path.stat().st_mode) == 0o600
for name in ('i-have-adhd', 'consultar-enfoque', 'punto-de-regreso', 'capture', 'handoff'):
    text = (profile / 'skills' / name / 'SKILL.md').read_text()
    assert text.startswith('---\n')
    _, front, body = text.split('---', 2)
    meta = yaml.safe_load(front)
    assert meta['name'] == name and meta['description'] and body.strip()
    if name in ('i-have-adhd', 'consultar-enfoque', 'punto-de-regreso'):
        assert text == (root / 'skills' / name / 'SKILL.md').read_text()
print('OK: perfil aislado, Codex privado, cinco skills y skills puente verificadas.')
