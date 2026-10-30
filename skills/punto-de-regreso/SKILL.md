---
name: punto-de-regreso
description: "Guarda o recupera un punto de regreso verificable al cambiar de sesión o perfil. Activar con 'ubícame', 'guarda dónde vamos' o 'deja un punto de regreso'."
version: 1.0.0
---
# Punto de regreso entre perfiles

## Ubicar
1. Lee el punto de regreso que el usuario indique o el archivo PUNTO_DE_REGRESO.md en la raíz del proyecto conocido. Respeta un documento de estado existente antes de crear otro.
2. Si falta contexto, usa session_search antes de pedirlo de nuevo. Las sesiones son del perfil activo: no asumas historial compartido. Si no hay un proyecto inequívoco, pregunta cuál.
3. Devuelve Proyecto / Avance comprobado / Siguiente paso. Un documento antiguo es evidencia histórica, no estado vivo: verifica Git, PR o artefactos cuando sea relevante; sin verificación di 'último estado registrado'.

## Guardar
Cuando el usuario pida guardar o transferir contexto:
1. Lee primero el archivo existente y conserva pendientes ajenos. Usa fecha/hora de herramienta, no inventada.
2. Actualiza el archivo de estado de proyecto que ya exista; si no existe, crea PUNTO_DE_REGRESO.md en la raíz confirmada del proyecto. No escribir dentro de perfiles ajenos para compartir estado.
3. Incluye: proyecto y ruta, fecha, perfil de origen conocido, objetivo, hechos con evidencia/rutas/URLs, pendientes/bloqueos, decisiones abiertas y UNA siguiente acción. No copies secretos ni conversaciones completas; referencia los artefactos. Usa handoff para un relevo técnico extenso y enlázalo.
4. Lee el archivo escrito para verificar y entrega su ruta absoluta. El otro perfil debe leer esa ruta; no recibe el contexto mágicamente.

## Ideas sin desviar el trabajo
Usa capture para organizar ideas. Si el usuario pide guardarlas, usa el buzón existente del proyecto o IDEAS.md en su raíz, preservando lo anterior. No ejecutar las ideas por mencionarlas.

## Invocación desde otro perfil
Lee `/Users/USERNAME/.hermes/skills/punto-de-regreso/SKILL.md` con read_file y luego el punto de regreso compartido. Para instalar en otro catálogo se requiere autorización del perfil destino y no sobrescribir archivos existentes sin respaldo.

## Verificación
Estado comprobado separado de reportado/propuesto. Nada de progreso temporal en memoria durable personal. Ruta existente y contenido leído después de guardar. Nunca prometer acceso al historial de otro perfil.
