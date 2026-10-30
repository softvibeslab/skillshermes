---
name: vpsvibes-rules-messaging
description: >
  Planear y operar reglas de VPSVibes por perfil, agente, grupo o usuario.
  Usar para crear reglas, editar límites, pausar alertas, programar mensajes,
  consultar reglas heredadas, configurar preferencias rápido/a fondo, avisar
  de memoria alta o repetir el aviso de Pepito. También para activar esta
  capacidad en otro perfil o explicar por qué no llegó una notificación.
---

# VPSVibes: reglas y mensajes

## Estado y límites

Esta skill guía descubrimiento, planificación y operación segura. No instala
un motor de reglas ni convierte instrucciones en automatizaciones persistentes.
El dashboard partió de observación; puede haber implementación local de CRUD
sin UI terminada ni despliegue. Verificar por separado código local, pruebas
actuales y capacidades del servicio destino; nunca inventar rutas ni confundir
staging con producción.

## Valores predeterminados

| Parámetro | Valor si falta |
|---|---|
| Acción | Consultar o preparar borrador, sin efectos externos |
| Instancia | La nombrada por el usuario; confirmar si no se puede resolver |
| Perfil | Activo solo para consulta; otra instalación requiere nombre explícito |
| Alcance | Perfil indicado; no ampliar a todos |
| Canal | El explícito o el verificado del perfil; sin coincidencia única, detener envío |
| Destinatarios | Ninguno hasta resolver audiencia autorizada |
| Programación | Ninguna; no convertir fecha ambigua en envío |
| Zona | La configurada y verificada del destinatario/regla; si falta, solicitar antes de activar |
| Regla nueva | Borrador |
| Prueba | Simulación sin red |
| Cooldown de alerta | Proponer 6 horas, editable antes de activar |
| Persistencia de umbral | Proponer 60 segundos, con métrica fresca |
| Reintento ambiguo | Deshabilitado; revisión manual |
| Instalación en perfiles | Solo los nombrados y autorizados |

## Step 1: Detectar entorno y capacidades

Cargar hermes-agent al tocar perfiles, cron o configuración. Recuperar contexto
con session_search antes de pedir rutas conocidas. Detectar herramientas con
`command -v hermes`, `command -v ssh` y `command -v python3`; comprobar ayuda
instalada antes de invocar comandos de escritura. Nunca imprimir secretos.

Identificar host, HERMES_HOME activo y perfil; Mac y VPS no son el mismo entorno.
Consultar código/docs del dashboard y salud/autenticación sin saltarse 401.

Decisión:
1. API administrativa real y acceso configurado: usar API y sus contratos.
2. Sin API, pero CLI Hermes/SSH autorizado: lectura y operación explícita de
   alcance limitado mediante comandos documentados; registrar que no fue CRUD.
3. Sin acceso: entregar borrador y bloqueo preciso. No buscar credenciales en
   logs, historial o archivos de otros proyectos.

Salida: matriz de capacidades verificadas y autoridad disponible.

## Step 2: Resolver entidades y audiencia

Usar inventario sanitizado del dashboard; si no existe, listar perfiles mediante
CLI autorizada. Para usuarios/chats, usar directorio verificado o una extracción
mínima de metadatos permitidos; nunca volcar conversaciones completas.

Identidad: instancia + perfil emisor + plataforma + chat + hilo, con user_id
separado. No fusionar personas por nombre. Diferenciar grupo administrativo de
chat de Telegram; una sesión DM no prueba membresía en ningún grupo.

Intersecar destinatarios seleccionados con autorización vigente y chat conocido.
Revalidar antes de cada envío. No enviar por defecto a todos los registrados.
Salida: alcance explícito, lista o cantidad de destinatarios y exclusiones.

## Step 3: Construir regla y simular

Tipos: alerta de métrica, política de recursos, mensaje programado o preferencia.
Validar condición tipada, umbral/unidad, duración, recuperación, vigencia, canal,
texto, horario silencioso, cooldown y zona IANA. No aceptar shell/eval/plantillas
que ejecuten código.

Preferencias: usuario en perfil > grupo > perfil > global explícito. Conflictos
entre grupos requieren prioridad definida; seguridad/denegación siempre gana.
Una regla de usuario no modifica límites del cgroup compartido. No atribuir RAM
exclusiva a usuarios desde métricas de procesos compartidos.

Simular por API si existe; si no, preparar especificación con datos observados.
Mostrar audiencia, próximos disparos, conflictos y cambio deseado/efectivo.
MemoryHigh implica presión/reclamación; MemoryMax puede provocar OOM. Swap es
independiente. Un mensaje de “rápido/a fondo” no aplica ninguna preferencia hasta
que exista integración comprobada en el contexto del agente.
Salida: borrador revisable; no afirmar ejecución.

## Step 4: Ejecutar solo el alcance autorizado

Una solicitud de plan no autoriza desplegar, enviar ni aplicar límites.
Para activar, confirmar texto, audiencia, zona y efecto técnico si no están
inequívocamente autorizados. Usar API existente; alternativamente operación CLI
específica verificada. No editar a mano almacenes cron activos.

Reutilizar scheduler instalado si cubre el contrato; de lo contrario proponer
worker restringido + timer. Un solo propietario por job. Mensajes fijos no
necesitan LLM. Cron debe tener instrucciones autocontenidas y destino explícito.

Mantener separación entre web, tokens de bots y helper de límites. No remover
ProtectHome para facilitar acceso; no aceptar nombres de servicio arbitrarios.
Respaldar solo archivos afectados y verificar límites leídos después del cambio.

Programar con UTC + zona IANA, persistencia y deduplicación por ocurrencia y
destinatario. Si la plataforma no garantiza idempotencia, timeout tras envío
queda resultado_desconocido, no se reenvía ciegamente. Respetar retry_after y
revocaciones; nunca tratar un 403 como éxito.
Salida: IDs de regla/job/operación o bloqueo, sin secretos.

## Entrega incremental y recuperación tras interrupciones

Al convertir un dashboard de observación en uno con escrituras, entregar primero
un circuito completo de borradores: tarjeta/formulario → API validada → SQLite →
lectura posterior → historial → simulación sin efectos. Un backend parcial no
constituye un CRUD utilizable ni una automatización activa. Etiquetar en la UI
las funciones no implementadas; no ofrecer «Activar» o «Enviar» si falta el worker
o la verificación de audiencia.

Antes de habilitar escrituras, comprobar autenticación y protección CSRF: la
autenticación básica del navegador no basta por sí sola. Validar origen y token
CSRF, tipos de contenido, tamaños de cuerpo y esquemas; usar versiones para
rechazar ediciones concurrentes en vez de perder cambios silenciosamente.

Tras compresión o reanudación, verificar archivos y pruebas reales antes de
continuar: distinguir fuente remota vigente, copia de inspección, implementación
local, staging y producción. No desplegar una copia histórica sobre cambios más
recientes. Registrar archivos modificados, pruebas ejecutadas/no ejecutadas y
bloqueo en el README o documento de handoff del proyecto, no como estado durable
en esta skill. Si una ejecución fue denegada, no cambiar de herramienta para
eludirla ni afirmar que las pruebas pasaron; solicitar autorización para ese
paso y mantener separados los avances comprobados de los pendientes.

Ver `references/observation-to-rules.md` para los criterios de promoción y las
pruebas mínimas del circuito de borradores.

## Step 5: Verificar y registrar

Leer de nuevo la regla y próxima ejecución; probar pausa/cancelación sin tocar
jobs ajenos. Para envío real autorizado, verificar aceptación y message_id;
no confundir aceptado con leído. Para recursos, verificar propiedades efectivas.

Pruebas con DB temporal, reloj falso y transporte bloqueado: aislamiento entre
perfiles, reglas conflictivas, datos stale, repetición, reinicio, concurrencia,
DST y errores ambiguos. No enviar pruebas masivas. Si no hay implementación,
validar el plan y declarar pendientes las pruebas de runtime.

## Entrega local de administración draft-only

Cuando el usuario pide LOCAL STAGING y prohíbe deploy/SSH, trabajar únicamente
sobre fuentes locales y fixtures sintéticos. No consultar inventario vivo ni
usar credenciales de producción para completar una prueba. Leer el flujo
existente antes de insertar API/UI y preservar monitorización y `/health`.

- Separar persistir de ejecutar: CRUD de borradores, archivo, duplicación y
  preview no crean cron, transportes, alertas activas, preferencias efectivas ni
  cambios de recursos. El directorio administrativo no autoriza envíos.
- Validar campos y tipos estrictos (incluida versión entera, no bool), perfiles,
  identidad explícita y membresías. Horarios: ISO con offset compatible con zona
  IANA; detectar horas inexistentes/ambiguas de DST, sin corrección silenciosa.
- Persistir con transacciones, versión optimista y auditoría. Dos actualizaciones
  concurrentes de la misma versión deben producir un ganador y un conflicto;
  no basta probar actualizaciones secuenciales.
- API administrativa fail-closed: identidad de proxy configurada, Host/Origin
  permitidos, CSRF, JSON acotado y rutas/métodos restringidos. Documentar que el
  proxy debe sobrescribir cabeceras de identidad aportadas por clientes. No
  ampliar acceso del servicio a secretos ni quitar ProtectHome.
- UI nativa en español, tarjetas y editor con vistas por alcance. Editor bloqueado
  hasta verificar capacidad administrativa; usar textContent/DOM seguro para
  texto de usuario. Mostrar siempre que preview es simulación, no ejecución.
- Verificar separadamente backend, assets y comportamiento de navegador. Una
  prueba que busca marcadores HTML no demuestra CRUD/preview usable. Usar DB
  temporal, HTTP loopback y fake proxy; comprobar que preview no altera estado
  ni invoca transportes. Si HTML se carga al importar el servidor, reiniciar el
  proceso de prueba para verificar los cambios.
- Tras agregar pruebas, el resultado anterior ya no cubre la suite actual.
  Informar por separado pruebas pasadas, nuevas no ejecutadas y UI pendiente.
  Una denegación de ejecución no es un fallo del test: detener ese intento sin
  reescribirlo ni buscar otra vía para lograr el mismo resultado.

Contrato y evidencia de la primera entrega parcial:
`references/local-draft-staging.md`. Revalidar archivos antes de continuar;
la referencia no certifica el estado actual ni una entrega completa.

## Step 6: Activar la skill en otro perfil

Listar perfiles del host correcto y comprobar destino. Solo con autorización
explícita copiar esta skill y sus referencias al perfil nombrado, sin clonar
.env, tokens, sesiones ni memoria. Usar mecanismo de skills soportado por la
versión instalada o copia acotada y comprobar con `hermes -p NOMBRE skills list`.
No sobrescribir una versión personalizada sin comparar. Verificar listado y
carga; instalar la skill no garantiza acceso al dashboard ni autoriza envíos.

## Step 7: Entregar resultado

1. Estado: propuesta / guardada / activa / verificada / bloqueada.
2. Alcance: host, perfil, entidad, canal, audiencia y horario con zona.
3. Evidencia: IDs, resultado de lectura posterior y pruebas ejecutadas.
4. Pendientes: diferencias entre guardar, activar, enviar y aplicar preferencias.
5. Ubicación: plan o archivos locales, sin rutas inventadas ni credenciales.

## References

- `references/vpsvibes-context.md`: localizador y restricciones de integración.
