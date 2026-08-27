# Day25 — AI Pricing · GTM · Evidence

## Project

- Student: Nguyen Quang Huy
- Student ID: 2A202601873
- Assignment: From working AI product to sellable product — pricing, GTM and evidence
- Selected AI product: P-015 AI Fraud Investigation Copilot

## Deliverables

- [Excel model](deliverables/NguyenQuangHuy_Day25_model.xlsx)
- [One-Pager PDF](deliverables/NguyenQuangHuy_Day25_onepager.pdf)
- [Editable one-page DOCX source](deliverables/NguyenQuangHuy_Day25_onepager.docx)

## Method

1. Budget + job definition
2. Value Metric
3. Cost/Job + pricing
4. GTM affordability
5. Pain Moment + 90-day plan
6. Evidence Pack

## Key Economics

- Cost/Job: 7,648 VND per completed grounded investigation package.
- Price: 30,000,000 VND/month platform fee + 32,000 VND per completed job.
- Gross Margin: 76.1% variable/usage GM; 82.8% blended GM.
- Current completion/containment: 80% LOCAL CONTROLLED EVAL PROXY (4/5 grounded packages); autonomous completion is 20%; neither is customer evidence.
- Breakeven containment: 44.3% for the variable usage economics at a 60% GM target.
- Critical sensitivity: a 2x adverse containment error to 40% lowers usage GM to 56.1%.

## GTM

- Chosen channel: Sales-Led only for the first 90 days.
- CAC budget: 1,061,327,040 VND/customer.
- Estimated CAC: 350,000,000 VND/customer.
- Affordability gap: 711,327,040 VND/customer favorable.
- Affordability ratio: 3.03x; ACV: 1,281,600,000 VND / $49.3K reference.
- Deals / AE: 2.81/year and 0.013/selling day.
- Pain Moment: 09:00–11:00 after an overnight alert burst, when a fraud analyst triages high-risk transactions in the existing fraud-operations alert queue/dashboard before manual disposition.

## Evidence

- Eval Results: PARTIAL local controlled evidence; 5 attempted, 4 grounded packages, 1 autonomous completion, 4 human-review cases and 1 grounding failure. Customer containment and time saved are missing.
- Risk Checklist: PARTIAL; grounding, fallback, injection defense, redaction and human review are evidenced, while production security and procurement controls remain open.
- Pilot: MISSING EVIDENCE; a dated 8-week, 2-design-partner plan for 6,000 jobs is supplied.

## Verification

- Automated formula and workbook audit: PASS.
- Numerical crosscheck against the editable one-pager: PASS.
- Excel visual QA: seven rendered tabs inspected; PASS.
- PDF visual QA: one-page Poppler render inspected; PASS.
- Manual rubric audit: PARTIAL; official Day28 templates and customer pilot evidence were not found.

## Known limitations / assumptions

- The official Day28 workbook and DOCX template were not found after the documented local search; transparent substitute layouts are used and disclosed.
- The 80% completion input is a reproducible 4/5 grounded-package local-eval proxy, not a customer completion rate; retry telemetry and paired time saved are not measured.
- API, infrastructure, labor and funnel inputs are labeled assumptions or verified public list prices in the workbook.
- Full Kafka/ML/production deployment, auth/RBAC, rate limiting, TLS, retention/deletion, durable audit export and vendor terms are not verified as production controls.

See [FINAL_AUDIT_REPORT.md](FINAL_AUDIT_REPORT.md) and the [evidence pack](evidence/evidence-pack.md) for the complete gate and deadlines.
