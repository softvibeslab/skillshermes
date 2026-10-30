# Límites de memoria por perfil Hermes en un VPS Linux

## Alcance

La API de Contabo no limita procesos individuales dentro del huésped. Usar SSH autorizado y systemd/cgroups existentes; no instalar otro supervisor. Un nombre de perfil no constituye un límite de recursos: todas sus ejecuciones deben estar dentro del servicio o slice correspondiente para compartir un techo.

## Descubrimiento antes de cambiar

1. Resolver el nombre exacto del perfil y su servicio. Si el nombre pedido solo se parece al encontrado, confirmar antes de modificarlo.
2. Revisar tanto `systemctl` como `systemctl --user` del usuario dueño del agente. Un gateway puede ser un servicio de usuario incluso cuando ese usuario es root. `systemctl` sin `--user` puede mostrar not-found mientras el gateway está activo en el gestor de usuario.
3. Verificar cgroup v2 con `stat -fc %T /sys/fs/cgroup` y consultar, en el gestor correcto:

```sh
systemctl --user show "$UNIT" \
  -p MainPID -p ControlGroup -p FragmentPath \
  -p MemoryCurrent -p MemoryPeak -p MemoryHigh -p MemoryMax \
  -p MemorySwapMax -p Restart -p NRestarts
```

4. Confirmar identidad mediante ExecStart y HERMES_HOME sin imprimir entornos completos ni secretos. Inspeccionar PID, padre y pertenencia real al cgroup, no solo nombres de procesos. Buscar ejecuciones adicionales del mismo perfil fuera del servicio.
5. Comparar consumo actual/pico con el techo solicitado; convertir bytes mediante una herramienta y distinguir MB decimales de MiB. `200M` en systemd no equivale a 200 millones de bytes.

## Semántica y riesgo

- MemoryHigh aplica presión de recuperación y puede ralentizar; no es un techo duro.
- MemoryMax es un techo para memoria contabilizada del cgroup, no una suma exacta de RSS. Si no se puede recuperar memoria, puede activar OOM y terminar procesos.
- MemorySwapMax controla swap por separado. No afirmar que MemoryMax por sí solo limita RAM más swap.
- Hijos que permanezcan en el cgroup cuentan; navegadores compartidos, contenedores, modelos externos, servicios remotos y otras sesiones fuera del grupo no quedan cubiertos automáticamente.
- Si el límite pedido está claramente por debajo del consumo actual, explicar interrupción y posible ciclo de OOM/reinicio antes de aplicarlo. Revisar Restart y límites de arranque. No cambiar la política de reinicio ni reducir funcionalidades de forma incidental.

## Aplicación y verificación tras autorización

- Guardar los valores y overrides previos. Usar propiedades nativas del servicio y cambios limitados a la unidad confirmada; nunca reiniciar toda la flota.
- No aplicar un techo peligroso como supuesto ensayo inocuo: una actualización en caliente también puede terminar procesos inmediatamente.
- Verificar tanto propiedades efectivas como archivos del cgroup (`memory.max`, `memory.high`, `memory.swap.max`, `memory.current`, `memory.events`).
- Observar estado, contador de reinicios y eventos OOM durante actividad representativa; probar respuesta del gateway. Un set-property exitoso no demuestra que el agente pueda trabajar bajo el límite.
- Si falla, informar y usar el rollback acordado. No aumentar silenciosamente un techo explícito ni declarar operativo un gateway que reinicia en bucle.
- Distinguir estado final: límite solicitado, configurado, efectivo y operación comprobada. Si faltó confirmación, reportar que no se modificó nada.
