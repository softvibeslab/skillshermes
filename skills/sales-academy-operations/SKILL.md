---
name: sales-academy-operations
description: Operar, verificar y recuperar el squad Sales Academy y su torre privada Mac–VPS. Usar para retomar salesacademy, revisar el dashboard 8790, diagnosticar sincronización, instalar el plugin de forma acotada, comprobar delegaciones o registrar evidencia. También cuando el usuario pregunta por agentes inactivos, resultados faltantes o tareas que no arrancan desde la torre.
---

# Sales Academy: operación privada Mac–VPS

## Defaults y alcance

| Parámetro | Default |
|---|---|
| Acción | Diagnóstico de solo lectura; no reinstalar |
| Perfil objetivo | `salesacademy` |
| Repositorio | `src/sales-academy-squad` bajo el home real de la cuenta |
| Origen | `git@github.com:softvibeslab/sales-academy-squad.git` |
| Workspace | `sales-academy-shared` bajo el home real |
| Dashboard | `http://127.0.0.1:8790`, solo Mac local |
| Destino SSH | Descubrir del bridge/config local; no inventar host ni usuario |
| Escrituras en perfiles | Solo con autorización explícita para ese perfil |

Cargar `hermes-agent` antes de configurar Hermes. Esta skill no autoriza cambios por sí sola. Guardar una skill no autoriza instalarla en otros perfiles ni en el VPS.

## Step 1: Detectar entorno y fuentes

Comprobar `uname -s`, `command -v hermes`, `command -v python3`, `command -v ssh`, y `hermes profile list` según herramientas disponibles. Obtener el home real con Python `pwd.getpwuid(os.getuid()).pw_dir`: el HOME de una terminal Hermes puede estar aislado. Usar rutas absolutas resueltas, nunca asumir que `~` apunta al usuario del sistema.

- Con acceso al repositorio: leer `control/OPERATIONS.md`, `AGENTS.md` y los scripts implicados antes de actuar.
- Sin repositorio: localizarlo con búsqueda de archivos. Clonar solo cuando se solicite instalación; si existe no sobreescribirlo ni hacer pull sobre cambios locales.
- Sin SSH o autenticación válida: diagnosticar localmente y declarar VPS no verificado. No debilitar host-key checking ni imprimir secretos.

Rutas documentadas originales, sujetas a comprobación: Mac `/Users/USERNAME/src/sales-academy-squad`; VPS `/root/src/sales-academy-squad`.

Salida: entorno, rutas reales, alcance autorizado y fuentes disponibles.

## Step 2: Inspeccionar y respaldar antes de instalar

Revisar cambios con `git status --short`. Leer `scripts/install-vps.sh` y `scripts/enable-hermes-plugin.py` antes de usarlos.

**Pitfall importante:** `install-vps.sh --profile NAME` NO limita la instalación a ese perfil: copia el plugin al HERMES_HOME base, modifica su config y además habilita el perfil. También elimina el destino del plugin y puede eliminar el squad previo. No ejecutar ese comando a ciegas.

Para una instalación autorizada exclusivamente en un perfil existente, verificar primero su directorio y config, respaldar plugin/config/SOUL, y considerar la interfaz existente:

```sh
bash "$REPO/scripts/install-vps.sh" --skip-nrv --hermes-home "$PROFILE_HOME"
```

`REPO` y `PROFILE_HOME` deben contener rutas absolutas verificadas; no pasar también `--profile`, que agregaría una ruta anidada. Si se solicita Nirvana, inspeccionar instalación y destino por separado antes de omitir `--skip-nrv`.

Preferir reutilizar una instalación saludable a reinstalar. No actualizar Hermes global por una incompatibilidad del plugin. No copiar un Hermes home completo siguiendo symlinks. Reiniciar solo el proceso del perfil autorizado, descubriendo su servicio real.

## Step 3: Verificar el puente y la torre

Leer `control/bridge.py` y `control/install_mac_services.py` antes de cambiar configuración o servicios; no inventar flags. No ejecutar `attach_profile.py` sin inspección: tiene perfil fijo y usa Path.home().

En Mac, inspeccionar los servicios existentes:

```sh
launchctl print gui/$(id -u)/com.softvibes.salesacademy-dashboard
launchctl print gui/$(id -u)/com.softvibes.salesacademy-sync
```

Verificar HTTP con `curl -fsS http://127.0.0.1:8790/` o navegador. Si no hay servicio, usar logs/config del repositorio para diagnosticar antes de reinstalar.

Con sincronización autorizada y configuración revisada:

```sh
python3 "$REPO/control/bridge.py" sync
```

Compartir únicamente `docs/`, `decisions/`, `tasks/`, `results/`, `events/`. Nunca sesiones, memorias globales, credenciales ni configuración Hermes. Comprobar frescura y hashes locales/remotos de archivos concretos; una respuesta HTTP no demuestra sincronización.

Límites documentados: archivos planos UTF-8 .md/.txt/.json/.csv, 512 KiB por archivo, 8 MiB y 2000 archivos por inventario. Un archivo inválido bloquea el tick. Detector de secretos heurístico: revisar manualmente. Verificar límites actuales en código si cambian.

No hay borrado remoto. Conflictos con igual nombre conservan versiones con sufijo SHA-256; resolver con un nuevo documento versionado, no borrar evidencia ni modificar eventos UUID. Estado stale/offline no significa pérdida de datos. Sincronización periódica requiere Mac despierto y conectado; LaunchAgents arrancan al iniciar sesión.

## Step 4: Delegar y registrar evidencia real

Detectar las herramientas disponibles en el runtime objetivo:

- Con lifecycle compatible y `sales_academy_delegate`: delegar mediante plugin y comprobar eventos correlacionados de inicio/final/error.
- Sin lifecycle compatible: `sales_academy_load` seguido de `delegate_task` nativo en el turno llamante; registrar evidencia explícitamente. Este es el fallback documentado del Mac, no una garantía eterna sobre versiones futuras.

Ejemplo después de verificar el entregable:

```sh
python3 "$REPO/control/bridge.py" record --node mac --agent agents-orchestrator --status completed --task 'Revisión de documento X' --result 'Evidencia en results/documento-x-v1.md'
```

En VPS usar `--node vps`. Verificar los flags actuales mediante código/ayuda si difieren. No marcar completed por una mera afirmación del subagente: leer el archivo/URL resultante.

La bandeja del dashboard registra tareas manualmente; NO dispara ejecución. Exigir autorización de la tarea y un único responsable Mac/VPS; referenciar su UUID al resolverla. El roster de especialistas no representa procesos permanentes. Éxito de ejecución no equivale a certificación de negocio. No inventar costos/tokens ni reconstruir telemetría histórica inexistente.

## Step 5: Validar y entregar

Si se cambió código/plugin, ejecutar el chequeo existente en cada equipo modificado:

```sh
python3 -m unittest discover -s "$REPO/control" -v
```

Usar el intérprete compatible con el proyecto si python3 del sistema difiere del runtime Hermes. No guardar conteos de pruebas como expectativas permanentes. Verificar por separado: tests, servicio HTTP, sincronización/hash y delegación. Si solo hay acceso local, declarar que la parte remota queda pendiente.

Mantener servidor en loopback, controles Host/Origin/CSRF y transporte SSH verificado. No exponer a internet, duplicar el bot Telegram del VPS en Mac ni actualizar otros perfiles como efecto colateral.

Responder en español con:
1. **Estado:** verificado, parcial o bloqueado, por componente.
2. **Evidencia:** URL/rutas, comandos ejecutados y resultado actual.
3. **Límites/siguiente paso:** solo lo pendiente; distinguir registro manual de ejecución.
