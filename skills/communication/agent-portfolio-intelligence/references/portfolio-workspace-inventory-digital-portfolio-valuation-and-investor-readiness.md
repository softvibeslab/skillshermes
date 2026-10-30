# Digital portfolio valuation and investor readiness

Use this extension when a project inventory must support company valuation, incorporation, a private equity round, or regulated crowdfunding.

## 1. Start from an ownership-safe asset perimeter

Do not value every discovered folder. Build three sets:

1. **Owned candidate assets** — company/founder-owned repositories or local work with evidence to be completed.
2. **Dependencies and references** — forks, third-party repositories, open-source packages, API subscriptions, base models, examples, and research copies. Record them, but do not capitalize them as owned IP.
3. **Excluded duplicates** — worktrees, backups, `-old`, `-golden`, CI copies, portfolio roots, and collections whose children are inventoried separately.

Give each included asset one canonical repository/path and an `Incluir en total` decision with a reason. A large repository count is not itself enterprise value.

## 2. Use several valuation methods, not one magic number

### Adjusted replacement cost

Useful as an early-stage floor before reliable revenue exists:

`replacement_cost = estimated_hours × blended_rate × complexity_factor`

`adjusted_value = replacement_cost × ownership_factor × maturity_obsolescence_factor`

Label hours as estimated, expose every assumption, and set excluded/duplicate assets to zero. Do not infer value directly from LOC, file count, or historical modification time.

### Income approach

Use only with evidence:

- verified MRR/ARR and invoices/bank receipts;
- gross margin and provider/cloud costs;
- growth, churn, customer concentration, CAC/LTV;
- contracted backlog and renewal terms;
- defensible forecast and discount rate.

Until those exist, mark DCF or revenue-multiple valuation as `Pendiente`; do not apply SaaS multiples to unfinished projects.

### Relief-from-royalty / market approach

Use for registered brands or licensable technology only when exclusivity, attributable revenue, useful life, comparable royalty/multiple, and transferability can be supported.

## 3. Separate owned assets from recurring expenses

Inventory these categories independently:

- software and documentation;
- registered marks, domains, channels, and names;
- datasets, prompts, knowledge bases, and trade secrets;
- proprietary model weights, adapters, evaluations, and fine-tunes;
- hardware and transferable prepaid infrastructure;
- customer contracts, recurring revenue, and backlog;
- debt, tax, contractual, privacy, and litigation liabilities.

Model/API subscriptions are normally operating expenses, not owned assets. Capitalize only a demonstrably transferable right, prepaid credit, proprietary derivative, or contractually controlled artifact. A fine-tune needs evidence for the base-model license, training data rights, weights, benchmark, and transferability.

## 4. Chain-of-title gate

An asset cannot be investor-ready until evidence answers:

- Who authored it?
- Was the author an employee, contractor, founder, or third party?
- Is there a written assignment or license?
- Does the repository include incompatible OSS or copied code?
- Are datasets lawful, consented, and transferable?
- Are domains/accounts registered to the company?
- Are marks/software registered where useful?
- Are confidentiality controls sufficient for trade-secret treatment?

Keep automatic inventory values explicitly preliminary until legal review and an independent appraisal confirm title and assumptions.

## 5. Three capital routes are different transactions

### Contribution in kind at incorporation

This transfers selected software/IP into the company in exchange for founder capital/shares. It is not outside investment. Require an appraisal, written assignments, corporate approval, accounting and tax treatment, and a schedule of contributed assets.

### Private equity round

Model pre-money, new cash, post-money, dilution, fully diluted cap table, runway, milestones, and investor rights. A simple check is:

`investor_ownership = new_cash / (pre_money + new_cash)`

If a provisional asset floor causes excessive dilution, do not hide it; improve evidence, narrow/phase the raise, or wait for traction. Do not present a private round as a public securities offer.

### Regulated crowdfunding

Distinguish debt, equity, and revenue-share/royalty structures. In Mexico, public-facing digital intermediation should be reviewed under the Fintech framework and conducted through an authorized crowdfunding institution when applicable. Do not collect public investment directly from a landing page, chat, or social channel. Verify platform authorization, limits, fees, disclosure duties, investor rights, auditability of revenue, and termination/cap terms.

## 6. Investor-ready workbook shape

Add these sheets to the core inventory:

- `Resumen ejecutivo` — preliminary floor, confirmed other assets, liabilities, and missing valuation methods.
- `Activos software` — canonical assets, inclusion reason, ownership, assumptions, replacement cost, adjusted value, and evidence required.
- `Otros activos y PI` — editable low/base/high values with title and transferability evidence.
- `Métodos de valuación` — asset, income, royalty, and market approaches with data gaps.
- `Parámetros` — editable rates, factors, raise amount, and pre-money assumptions.
- `3 vías de inversión` — contribution in kind, private shares, regulated crowdfunding.
- `Cap table` — current and fully diluted ownership.
- `Plan 90 días` — title cleanup, incorporation, financial data room, investor materials, outreach.
- `Data room` — corporate, IP, code/licenses, AI/model, privacy, finance, commercial, team, and security evidence.
- `Riesgos` and `Fuentes legales`.

All formulas and hypotheses must remain editable. Never call the model a formal appraisal or promise investor returns.

## 7. Recommended sequence

1. Select 5–10 core assets and 1–3 investable products; archive the rest from the pitch, not necessarily from disk.
2. Establish canonical repositories and remove secrets.
3. Resolve assignments, OSS/model/data licensing, marks, domains, and privacy.
4. Obtain an independent appraisal and incorporate the company.
5. Reconcile revenue, costs, debt, and contracts into a data room.
6. Build 36-month projections from evidence.
7. Cross-check asset, income, royalty, and market methods.
8. Choose raise size from runway and milestones, then choose the legal instrument.

## Verification

- Excluded-domain filter returns zero matches in every valuation sheet.
- Third-party and duplicate rows contribute zero to totals.
- Headline totals reconcile to included asset rows.
- Every non-zero intangible has an evidence field and transferability status.
- Subscription/model costs are not silently capitalized.
- Dilution independently recomputes from pre-money and new cash.
- Legal sources are official and dated; counsel reviews final instruments.
- Workbook language says `indicative`, `estimated`, or `preliminary`, never `real value` or `formal appraisal` without a signed valuation report.
