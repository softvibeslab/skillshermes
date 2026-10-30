---
name: consultar-enfoque
description: "Llama al perfil Hermes enfoque desde otro perfil para ordenar ideas, simplificar una respuesta o definir un siguiente paso. Activar con 'consulta a enfoque' o 'pide ayuda a enfoque'."
version: 1.0.0
---
# Consultar Enfoque desde otro perfil

## Procedimiento
1. Prepara solo el contexto necesario: proyecto, objetivo, hechos comprobados y su evidencia, pendientes y pregunta. El perfil destino NO hereda esta conversación. No enviar secretos ni historiales completos.
2. Comprueba que existe el perfil con `hermes profile list`. Si ya eres enfoque, responde directamente; no recursión.
3. Usa el CLI nativo, sin cambiar el perfil predeterminado. Desde terminal ejecuta la siguiente forma mediante subprocess con argumentos separados (nunca interpolar el mensaje en shell):

```python
import subprocess
contexto = "Proyecto: ...\nAvance comprobado: ...\nPendiente: ...\nPregunta: ..."
r = subprocess.run(
    ["/Users/USERNAME/.local/bin/hermes", "--profile", "enfoque", "chat",
     "--quiet", "--toolsets", "", "--max-turns", "3",
     "-q", "Consulta de otro perfil. Solo asesora con el contexto dado; no uses herramientas ni cambies archivos. No asumas diagnóstico.\n" + contexto],
    cwd="/Users/USERNAME/.hermes/profiles/enfoque/workspace",
    capture_output=True, text=True, timeout=240,
)
print(r.stdout)
if r.returncode:
    raise RuntimeError(f"Consulta falló ({r.returncode}): {r.stderr[-2000:]}")
```

4. Devuelve la recomendación breve, indicando qué fue sugerido frente a comprobado. Si falla el proveedor, informa el fallo; no inventes que consultaste al perfil. No reintentes automáticamente si se desconoce si terminó.
5. Esta llamada es una consulta aislada: no cambia el perfil del llamador ni autoriza acciones externas. Una conversación interactiva aparte se abre con `hermes --profile enfoque`.

## Uso desde perfiles que no tengan esta skill instalada
Lee este archivo con read_file usando su ruta absoluta:
`/Users/USERNAME/.hermes/skills/consultar-enfoque/SKILL.md`.
No es necesario instalarla en todos los perfiles. Para mostrarla en su catálogo, copia esta carpeta a `$HERMES_HOME/skills/consultar-enfoque` solo cuando el usuario autorice el perfil destino; nunca sobrescribas una versión existente sin respaldo. Ejecuta `/reload-skills` después.

## Mantenimiento y comprobación
Ejecuta `/Users/USERNAME/.hermes/hermes-agent/venv/bin/python /Users/USERNAME/.hermes/skills/consultar-enfoque/scripts/verificar.py` para comprobar archivos, skills y configuración sin revelar credenciales.
En esta instalación la primera llamada necesitó autenticación Codex propia del perfil: no asumir que se hereda. Si caduca, usar el flujo oficial `hermes --profile enfoque auth` con el usuario, nunca mostrar tokens. El CLI puede añadir pools vacíos y skills bundled al primer arranque aunque exista `.no-bundled-skills`; eso no significa que se hayan copiado credenciales o sesiones. No modificar Hermes globalmente para evitar ese comportamiento como parte de una consulta.

## Verificación
Debe haber una respuesta real del perfil destino. El comando usa --profile enfoque, no profile use. No se envían credenciales ni se escribe en otros perfiles. La carpeta workspace evita cargar instrucciones accidentales del proyecto del llamador.
