#!/usr/bin/env python3
"""One-shot advisory call; no shell, no caller credentials, bounded process group."""
import argparse
import datetime
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import uuid

PROFILE = 'softvibes-connect'
ROOT = Path.home() / '.hermes'
TARGET = ROOT / 'profiles' / PROFILE
WORKSPACE = TARGET / 'workspace'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--timeout', type=int, default=240)
    args = parser.parse_args()
    if not 1 <= args.timeout <= 300:
        parser.error('timeout debe estar entre 1 y 300 segundos')
    current = os.environ.get('HERMES_HOME', '')
    if (os.environ.get('SOFTVIBES_CONNECT_CALL') or
            os.environ.get('HERMES_PROFILE') == PROFILE or
            (current and Path(current).expanduser().resolve() == TARGET.resolve())):
        parser.error('No recursión: responder directamente desde el perfil destino')
    executable = shutil.which('hermes')
    fallback = Path.home() / '.local/bin/hermes'
    if not executable and fallback.is_file() and os.access(fallback, os.X_OK):
        executable = str(fallback)
    if not executable:
        parser.error('Hermes CLI no disponible; no se realizó consulta')
    for path in (TARGET/'config.yaml', TARGET/'SOUL.md',
                 TARGET/'skills/softvibes-connect-operations/SKILL.md'):
        if not path.is_file():
            parser.error(f'Falta requisito local: {path}')
    if not WORKSPACE.is_dir():
        parser.error('Falta workspace aislado')
    text = sys.stdin.read(16001).strip()
    if len(text) > 16000:
        parser.error('Contexto demasiado largo; máximo 16000 caracteres')
    text = text or 'Explica límites documentados del catálogo, autorización, verificación y activación.'
    # Do not pass caller HERMES_HOME, bot/API secrets, model overrides, MCP or hooks.
    env = {key: os.environ[key] for key in ('HOME', 'PATH', 'LANG', 'LC_ALL', 'TMPDIR', 'SSL_CERT_FILE') if key in os.environ}
    env.update({'HERMES_HOME': str(ROOT), 'TERMINAL_CWD': str(WORKSPACE),
                'SOFTVIBES_CONNECT_CALL': '1', 'PYTHONUNBUFFERED': '1',
                'HERMES_REDACT_SECRETS': 'true'})
    prompt = ('Consulta aislada de otro perfil. Solo asesora con la skill precargada y contexto dado; '
              'no uses herramientas, no cambies archivos, no delegues. Distingue evidencia aportada '
              'de hipótesis; no afirmes inspección runtime ni activación. Responde en español.\n' + text)
    argv = [executable, '--profile', PROFILE, 'chat', '--quiet', '--toolsets', '',
            '--skills', 'softvibes-connect-operations', '--max-turns', '3', '-q', prompt]
    os.umask(0o077)
    evidence = WORKSPACE/'evidence'
    evidence.mkdir(mode=0o700, exist_ok=True)
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '-' + uuid.uuid4().hex[:8]
    log = evidence / ('consult-' + stamp + '.json')
    start = datetime.datetime.now(datetime.timezone.utc).isoformat()
    proc = subprocess.Popen(argv, cwd=WORKSPACE, env=env, stdin=subprocess.DEVNULL,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            text=True, start_new_session=True)
    timed_out = False
    try:
        stdout, stderr = proc.communicate(timeout=args.timeout)
    except subprocess.TimeoutExpired:
        timed_out = True
        os.killpg(proc.pid, signal.SIGTERM)
        try:
            stdout, stderr = proc.communicate(timeout=5)
        except subprocess.TimeoutExpired:
            os.killpg(proc.pid, signal.SIGKILL)
            stdout, stderr = proc.communicate()
    code = 124 if timed_out else proc.returncode
    record = {'started_at':start, 'finished_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
              'profile':PROFILE, 'cwd':str(WORKSPACE), 'toolsets':[], 'max_turns':3,
              'skill':'softvibes-connect-operations', 'exit_code':code, 'timeout':timed_out,
              'stdout':stdout, 'stderr':stderr}
    with log.open('x') as handle:
        json.dump(record, handle, ensure_ascii=False, indent=2)
    log.chmod(0o600)
    print(stdout, end='')
    print(f'\nRegistro local privado: {log}; exit={code}', file=sys.stderr)
    if code:
        print('Consulta incompleta/fallida. Revisar registro local sin exponer secretos; no reintento automático.', file=sys.stderr)
    return code if code else (0 if stdout.strip() else 2)


if __name__ == '__main__':
    sys.exit(main())
