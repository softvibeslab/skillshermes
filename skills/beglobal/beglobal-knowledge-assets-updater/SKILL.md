---
name: beglobal-knowledge-assets-updater
description: Integra contenido nuevo ya procesado en Be Global Knowledge Assets y propaga su proyección sanitizada al inventario, línea de tiempo, validación, aportes, Commerce OS, Atlas y mapas con filtros Base/PRO/Comparativa. Usar después de una ingesta o actualización de corpus; no descarga ni transcribe contenido.
---

# Be Global Knowledge Assets Updater

Actualiza el dashboard sin reemplazar la base anterior ni publicar detalle premium. La salida debe permitir tres lecturas consistentes: `baseline`, `pro` y `comparison`.

## Antes de editar

1. Confirma que el contenido ya tiene paquete de ingesta, análisis y estado de revisión. Si falta, usa `$beglobal-lesson-ingestor` o `$beglobal-ingestion-guide`; esta skill no descarga ni transcribe.
2. Lee [references/projection-contract.md](references/projection-contract.md).
3. Identifica el generador de la proyección pública y el dashboard que la consume. No copies transcripciones ni contenido premium al HTML.

## Flujo

1. Regenera el agregado privado y una proyección pública sanitizada. Cuando el paquete contiene notas `graphify/lesson.md`, materializa primero el corpus aislado:

```bash
python3 .agents/skills/beglobal-knowledge-assets-updater/scripts/prepare_course_graphify_corpus.py \
  --course-root beglobal/dataset/premium/courses/COURSE_ID
```

   Ejecuta Graphify sobre `graphify/corpus`, nunca sobre la carpeta que contiene media o transcripciones.
2. Conserva los casos anteriores; los refuerzos PRO deben enlazarlos por ID y los casos nuevos deben tener IDs estables.
3. Completa los siete adaptadores de `section_integrations`: inventario, timeline, validación, aportes, Commerce OS, Atlas y mapas.
4. Mantén `human_approved=false` hasta que exista una aprobación humana explícita. Etiqueta inferencias y candidatos como pendientes de Corporate.
5. Sincroniza el fallback embebido:

```bash
python3 .agents/skills/beglobal-knowledge-assets-updater/scripts/sync_projection_fallback.py \
  --projection beglobal/piloto/beglobal-pro-knowledge-assets.json \
  --dashboard beglobal/piloto/dashboard.html
```

6. Ejecuta la validación determinista:

```bash
python3 .agents/skills/beglobal-knowledge-assets-updater/scripts/validate_dashboard_update.py \
  --projection beglobal/piloto/beglobal-pro-knowledge-assets.json \
  --dashboard beglobal/piloto/dashboard.html
```

7. Valida JavaScript, DOM, filtros y responsive en un servidor local. Deriva los conteos desde la proyección:

```bash
python3 .agents/skills/beglobal-knowledge-assets-updater/scripts/validate_dashboard_runtime.py \
  --projection beglobal/piloto/beglobal-pro-knowledge-assets.json \
  --dashboard beglobal/piloto/dashboard.html
```

   - Base: conserva todos los casos anteriores y oculta candidatos nuevos.
   - PRO: muestra todos los refuerzos y candidatos de los corpus incorporados.
   - Comparativa: casos Base + candidatos nuevos únicos; los refuerzos no cuentan dos veces.
8. Si el usuario pidió publicar, crea respaldo remoto, sube primero la proyección y después el HTML, purga caché y compara checksums. No despliegues por inferencia.

## Límites

- Nunca publiques `.m3u8`, URLs firmadas, cookies, bearer tokens, cabeceras de autorización, rutas locales, media ni transcripciones.
- No atribuyas la autoría del curso al operador de ingesta. Separa `fuente`, `orquestación` y `aprobación`.
- El avance técnico no implica permiso de ejecución, asesoría legal/fiscal/financiera ni autorización para gasto publicitario.
- Conserva un respaldo verificable antes de reemplazar un archivo remoto.

## Entrega

Reporta: activo incorporado, cobertura, casos reforzados, casos nuevos, total único, estado Corporate, resultado de privacidad, resultado de filtros y si hubo o no despliegue.
