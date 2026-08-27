# Day25 — AI Pricing · GTM · Evidence

## Project

- Student: Nguyen Quang Huy
- Student ID: 2A202601873
- Assignment: From working AI product to sellable product — pricing, GTM and evidence
- Selected AI product: P-015 AI Fraud Investigation Copilot

## Official-template deliverables

- [Excel model](deliverables/NguyenQuangHuy_Day25_model.xlsx)
- [One-Pager PDF](deliverables/NguyenQuangHuy_Day25_onepager.pdf)
- [Editable one-page DOCX source](deliverables/NguyenQuangHuy_Day25_onepager.docx)

The workbook and DOCX were migrated from the official Lab-linked Drive sources recorded in templates/SEARCH_LOG.md. The supplied workbook's seven-tab layout and formulas were preserved; six objectively broken unquoted cross-sheet references were repaired and documented in qa/official_formula_preservation_report.md.

## Method

1. Budget + completed-job definition
2. Value Metric
3. Cost/Job + pricing
4. GTM affordability
5. Pain Moment + 90-day plan
6. Evidence Pack

## Canonical economics

- Cost/Job: **$0.5422 per completed autonomous job** (~₫14,150 at 26,095.90 VND/USD).
- Price floor: **$1.6267/job** (3x Cost/Job).
- Proposed pure-usage case: **$1.75/job**.
- Gross Margin: **69.0%** at the current 20% autonomous containment case.
- Breakeven autonomous containment: **15.5%** for the official usage case; GM falls below 50% at about **12.4%** containment.
- Current autonomous containment: **20.0% (1/5)**.
- Commercial package completion: **80.0% (4/5)**, with human review/escalation **80.0% (4/5)** and grounding failure **20.0% (1/5)**. These are distinct local-evaluation metrics; none is customer evidence.
- Hybrid is the commercial recommendation, while the official workbook's pricing tab models the pure $/completed-autonomous-job usage leg.

## GTM

- Chosen channel: **Sales-Led only** for the first 90 days.
- Segment: mid-market fintech/payment processor.
- ARPU: **$1,050/month**; ACV: **$12,600/year**.
- CAC budget: **$13,043.88/customer**.
- Estimated CAC: **$12,000/customer**.
- Official estimated/budget ratio: **0.92x**; inverse budget coverage: **1.09x**.
- Deals/AE/day: **0.180** under the founder-led planning case.
- The **$3,000/opportunity** input is explicitly a planning assumption, not CRM evidence.

## Evidence

- Eval Results: **PARTIAL** local controlled evidence; five cases support 80% package completion and 20% autonomous containment.
- Risk Checklist: **PARTIAL**; grounding/fallback/redaction are evidenced, while auth/RBAC, retention/deletion, TLS, vendor terms and live deployment remain open.
- Pilot: **PLANNED / NOT EXECUTED / MISSING EVIDENCE**; the 90-day plan specifies two design partners, 6,000 labeled jobs, paired baseline measurement, owners, gates and a 2026-12-04 report deadline.
- Stranger test: **NOT YET TESTED**; target is no more than three clarification questions.

## Verification

- Official workbook structural/formula/style audit: PASS.
- One-pager DOCX official-topology audit: PASS.
- Numerical and semantic crosschecks: PASS.
- Excel visual QA: all seven official tabs rendered and inspected; PASS.
- PDF visual QA: one letter-size page rendered with Poppler and inspected; PASS.
- DOCX-to-PDF note: LibreOffice was unavailable and Word COM export did not complete in this environment; the PDF is a controlled ReportLab export of the same official-template content and the DOCX remains editable.
- Secret scan and git diff --check: PASS after final verification.

## Known limitations

- No customer pilot, analyst time-saved measurement, causal customer outcome or production deployment is claimed.
- Retry telemetry is not instrumented; the workbook's 8% retry value is a planning estimate.
- The official supplied workbook contained six unquoted cross-sheet formulas that failed in the compatible evaluator; only those six references were repaired.
- Production auth/RBAC, rate limiting, TLS, retention/deletion, durable audit export, vendor data-use terms and SLA evidence remain open with named owners and deadlines.

See FINAL_AUDIT_REPORT.md and the evidence pack at evidence/evidence-pack.md for the complete gate and deadlines.
