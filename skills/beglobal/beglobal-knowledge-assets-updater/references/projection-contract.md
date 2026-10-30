# Contrato de proyección Knowledge Assets

## Capas

- `baseline`: activos y casos existentes; nunca se eliminan por incorporar un corpus.
- `pro`: metadatos sanitizados del contenido nuevo, refuerzos y candidatos.
- `comparison`: unión visual. Un caso existente reforzado conserva su ID y cuenta una sola vez.

## Campos raíz mínimos

```json
{
  "schema_version": "2.0.0",
  "asset_id": "id-estable",
  "access_tier": "premium",
  "visibility": "public_metadata_only",
  "comparison": {},
  "existing_use_case_contributions": [],
  "new_use_case_families": [],
  "section_integrations": {},
  "governance": {"human_approved": false}
}
```

## Adaptadores obligatorios

`section_integrations` debe contener:

- `inventory[]`: activo agregado, estado operativo, uso, siguiente acción y métricas seguras.
- `timeline[]`: eventos de ingesta, análisis, integración y aprobación; cada evento lleva `knowledge_layer`.
- `final_validation[]`: gates con responsable, estado, evidencia, aceptación y riesgo.
- `member_contributions[]`: distingue fuente del contenido, operador de ingesta y aprobador.
- `commerce_workflow[]`: relación por `step_index` con las etapas existentes; no reemplaza el flujo base.
- `member_atlas`: IDs de casos reforzados, IDs nuevos y total combinado único.
- `case_maps[]`: flujo visual, relación `strengthens_existing` o `new_use_case`, evidencia, riesgo, confianza y estado.

## Invariantes

1. Todo elemento PRO lleva `knowledge_layer=pro` o vive dentro de una colección inequívocamente PRO.
2. Todo caso nuevo tiene `review_status` y `confidence_score`.
3. Un refuerzo usa `existing_use_case_id`; no crea un segundo caso en comparación.
4. Los detalles públicos son síntesis: nunca extractos largos de una transcripción.
5. `human_approved` solo cambia por una decisión humana registrada.
6. El dashboard ofrece filtros sincronizados en:
   - `assets`
   - `contribution-timeline`
   - `final-validation`
   - `people`
   - `commerce-map`
   - `member-atlas`
   - `case-maps`

## Validación de contenido

Antes de publicar, busca al menos estos marcadores prohibidos en JSON y HTML generado: `.m3u8`, `Authorization`, `Cookie`, `Bearer`, firmas de proveedor, rutas absolutas de usuario, rutas de media y rutas de transcripción.

Después prueba Base, PRO y Comparativa en escritorio y móvil. Los conteos deben provenir de la proyección, no de texto duplicado en varias secciones.
