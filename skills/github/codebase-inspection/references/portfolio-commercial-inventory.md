# Portfolio inventory, valuation, and sales forecast

Use this extension when a multi-project workspace audit must become an Excel inventory or commercial planning artifact.

## Inventory workbook

Create one workbook with these sheets when relevant:

- `Resumen`: scope, counts by category/maturity, totals.
- `Proyectos`: one row per initiative or independently deployable subproject.
- `Repositorios Git`: independent roots only.
- `Agentes Hermes`: profile inventory without exposing secrets.
- `Hallazgos`: concise gaps and recommended actions.
- `Nombres duplicados`: same project name in multiple paths.
- `Parametros`: editable hourly rate and estimation notes.
- `Pronóstico ventas`: scenario-based commercial forecast.

Exclude dependencies, builds, caches, generated output, and temporary browser data from file/size metrics.

## Avoid double-counting

A portfolio root, collection, monorepo, or parent directory can coexist with deployable children in the inventory, but must not be counted again in valuation totals.

Add an `Incluir en total` field:

- `No` when another inventoried project is a descendant of that path.
- `Sí` for leaf/deployable projects.

Show estimated hours/value for every row if useful, but compute portfolio totals with `SUMIF` over `Incluir en total = Sí`.

## Hours and valuation

Never label inferred hours as recorded effort. Use `Horas hombre estimadas` and document the model. A minimal reproducible model may combine:

1. Base effort by maturity.
2. A capped file-volume factor.
3. A stack-complexity multiplier.
4. An editable hourly rate in `Parametros`.

Project value should reference the rate cell with formulas so changing one parameter recalculates the workbook.

## Commercial-state rule

Do not infer a sale from any of these:

- Deployed or `live` status.
- A public URL.
- A client/person name in the folder.
- A completed landing or CMS.

A project is sold only with explicit evidence such as a signed agreement, accepted proposal, payment, invoice, or a CRM state equivalent to `closed/won`. If evidence is absent, use `Venta no confirmada` rather than `No vendido`.

Useful commercial columns:

- Estado comercial
- Cliente
- Precio acordado
- Cobrado
- Fecha de cierre
- Evidencia / fuente
- Próxima acción

## Forecasting

When historical close-rate data is missing, create a model, not a prediction presented as fact. Use three scenarios:

- Conservador
- Base
- Agresivo

For each, state units sold, ticket assumptions, recurring revenue, 90-day revenue, and 12-month revenue. Keep assumptions visible in the workbook. Prefer a revenue-first model based on products that can already be demonstrated; do not turn the forecast into another engineering roadmap.

## Verification

After writing the workbook:

1. Validate it as a ZIP/XLSX container.
2. Confirm sheet names.
3. Confirm formulas exist.
4. Recalculate key totals independently.
5. Report the path, assumptions, and headline totals concisely.
