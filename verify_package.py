"""Verify the exported skill files without executing any skill code."""
from pathlib import Path
import hashlib
import json


def verify(root):
    manifest = json.loads((root / 'manifest.json').read_text())
    expected = manifest['files']
    actual = {p.relative_to(root).as_posix() for p in (root / 'skills').rglob('*') if p.is_file()}
    if actual != set(expected):
        raise ValueError('Missing or unexpected skill files')
    for relative, digest in expected.items():
        path = root / relative
        if not path.resolve().is_relative_to(root.resolve()) or path.is_symlink():
            raise ValueError('Unsafe path: ' + relative)
        if hashlib.sha256(path.read_bytes()).hexdigest() != digest:
            raise ValueError('Checksum mismatch: ' + relative)
    skills = list((root / 'skills').rglob('SKILL.md'))
    if len(skills) != manifest['skill_manifests']:
        raise ValueError('Skill count mismatch')
    print(f'OK: {len(skills)} SKILL.md; {len(expected)} files verified')


if __name__ == '__main__':
    verify(Path(__file__).resolve().parent)
