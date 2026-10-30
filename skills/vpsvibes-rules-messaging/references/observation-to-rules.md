# De observación a reglas: promoción segura

Patrón: ampliar un dashboard existente sin convertir el proceso web en un
administrador del host ni en lector de secretos de agentes.

## Circuito mínimo útil

1. Reutilizar inventario sanitizado y tarjetas existentes. Identificar entidades
   por IDs estables y alcance, no por etiquetas visibles.
2. Guardar reglas como borradores en SQLite durable, fuera de /run. Usar
   transacciones, claves foráneas y versión esperada en las actualizaciones.
3. Leer de nuevo después de crear/editar y mostrar estado real e historial.
4. Simular texto, audiencia y próximos disparos sin red ni ejecución privilegiada.
5. Archivar conserva auditoría. Cuando exista scheduler, debe cancelar pendientes
   y revalidar estado/versión justo antes de despachar.
6. Habilitar activación únicamente cuando exista un ejecutor verificado. No
   confundir guardar una preferencia con aplicarla al contexto de Hermes.

## Pruebas mínimas antes de publicar

- DB temporal: crear, consultar, editar, conflicto de versión, archivar y
  persistencia al reabrir; rechazo de valores, tipos y alcances inválidos.
- HTTP: rechazo anónimo y de escrituras cross-origin/sin CSRF; la autenticación
  básica no evita por sí sola CSRF. GET no debe producir efectos externos.
- Simulación: transporte bloqueado; ninguna prueba envía mensajes reales.
- UI: formulario → API → lectura posterior; errores visibles y controles
  deshabilitados para capacidades aún ausentes. Navegación por hash requiere
  esperar visibilidad, no solamente existencia del elemento.
- Regresión: métricas y navegación anteriores siguen funcionando; datos viejos
  no aparecen saludables. Probar escritorio/móvil y errores JavaScript.

## Frontera de privilegios

Mantener aislamiento del servicio web. El worker obtiene únicamente los secretos
necesarios del perfil emisor y vuelve a comprobar audiencia/allowlist. Los cambios
systemd usan un helper con catálogo de servicios permitido; nunca aceptar shell,
nombres de unidades arbitrarios o acceso general a /root desde formularios.

## Promoción y recuperación

Comparar fuentes vigentes antes de desplegar. Respaldar solo archivos afectados y
DB mediante backup API de SQLite; no copiar una DB activa como archivo ordinario.
Documentar qué versión está en local/staging/producción y cómo revertir sin perder
reglas. Validar configuración del proxy como su usuario efectivo y conservar
propiedad/permisos de fragmentos existentes. Reiniciar únicamente el servicio
modificado y recargar el proxy cuando corresponda.

Si el trabajo se interrumpe, dejar un handoff en el proyecto con rutas, cambios y
resultados verificables, incluyendo pruebas no ejecutadas. Una autorización
denegada no se resuelve reintentando por otra herramienta. No convertir el estado
incompleto de una sesión en una limitación permanente de la skill.
