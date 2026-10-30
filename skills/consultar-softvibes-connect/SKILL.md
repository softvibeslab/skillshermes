---
name: consultar-softvibes-connect
description: "Consulta al perfil Softvibes Connect desde otro perfil: pide ayuda de catálogo, consulta integraciones, explica bloqueo Composio, revisa evidencia del dashboard, distingue autorización de activación o prepara diagnóstico sin acciones externas."
version: 1.0.0
created_by: agent
---
# Consultar Softvibes Connect

## Defaults
- Perfil destino: softvibes-connect, fijo; nunca profile use.
- Workspace: ~/.hermes/profiles/softvibes-connect/workspace.
- Timeout: 240 segundos (máximo 300); 3 turnos; cero herramientas.
- Idioma: español. Sin pregunta: explicar límites y bloqueos documentados.
- Evidencia: log local privado 0600 por invocación; no incluir secretos en pregunta.

## Step 1: Detectar entorno
Detectar Python 3 y Hermes con command -v; alternativa Python shutil.which y ~/.local/bin/hermes. Comprobar perfil/config, SOUL y skill operación. Si no existen, detener sin crear/copiar nada automáticamente. Si HERMES_HOME/HERMES_PROFILE o guardia de invocación indican softvibes-connect, responder directamente: no recursión. No usar APIs/mensajería como sustituto si no hay CLI.

## Step 2: Preparar contexto mínimo
El hijo no hereda conversación: aportar proyecto, objetivo, hechos con fuentes/fechas, pendientes y pregunta. No enviar tokens, .env, auth.json, CSRF, enlaces OAuth ni historial completo. Separar evidencia de hipótesis. Sin herramientas, el hijo no puede verificar hechos nuevos.

## Step 3: Ejecutar wrapper seguro
Ejecutar scripts/consultar.py con Python y enviar contexto por stdin; nunca interpolar contenido de usuario en shell. Ejemplo desde terminal con un script Python controlado:
```python
import subprocess
contexto = 'Proyecto: Connect. Evidencia: server.py App.state activation_enabled=False. Pregunta: ¿Qué puedo afirmar?'
r = subprocess.run(['python3', '/Users/USERNAME/.hermes/skills/consultar-softvibes-connect/scripts/consultar.py'], input=contexto, text=True, capture_output=True, timeout=270)
print(r.stdout)
print(r.stderr)
```
El wrapper usa argv, shell=False, entorno allowlist sin bots/MCP, cwd y TERMINAL_CWD del perfil, skill operación precargada, sin --yolo. No cambia perfil predeterminado. Si falla o expira no reintentar automáticamente; la salida real y metadatos quedan en workspace/evidence. Timeout termina el grupo de procesos. Sin terminal disponible, entregar limitación: no afirmar consulta realizada.

## Step 4: Interpretar resultado
Exit 0 más respuesta no vacía demuestra consulta real al modelo, no integración activada ni dashboard desplegado. Fallo de auth: informar y solicitar flujo oficial hermes --profile softvibes-connect auth; nunca mostrar credenciales. Exit 124 implica timeout y resultado incompleto. El CLI puede sembrar skills builtin aunque exista .no-bundled-skills: en esta instalación añadió 90; quedaron deshabilitadas con skills.disabled solo en el nuevo perfil. Comprobar tras actualizaciones, no modificar Hermes global para impedirlo. Los listados Rich truncan nombres: usar COLUMNS=240 para comprobar consultar-softvibes-connect; ausencia de coincidencia literal en salida estrecha no prueba ausencia de skill.

## Step 5: Entregar salida
1. Respuesta real del especialista.
2. Evidencia aportada frente a recomendaciones/hipótesis.
3. Bloqueos y comprobaciones no realizadas.
4. Ruta de registro y estado/exit code; un siguiente paso.

## Lectura desde cualquier perfil
Leer con read_file la ruta absoluta /Users/USERNAME/.hermes/skills/consultar-softvibes-connect/SKILL.md. No requiere instalar en otros perfiles ni modificarlos. Si se desea mostrar en catálogo de otro perfil, pedir autorización separada. No cargar ni ejecutar este wrapper desde el propio destino.

## Mantenimiento
Revalidar hermes chat --help antes de cambiar flags. Verificar skills con hermes --profile softvibes-connect skills list y hermes --profile default skills list; revisar PROFILE.md del proyecto. El método reutilizable es fresh sin clone, config modelo selectiva, auth únicamente del proveedor, workspace aislado y one-shot sin herramientas. No crea herramientas nuevas ni una capa de ejecución en el dashboard.
