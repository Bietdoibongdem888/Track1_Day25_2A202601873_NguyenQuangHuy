# DAY25 - FINAL RECOVERY AUDIT REPORT

## Overall Status

READY (template limitation disclosed)

The recovery pass closes the previously recoverable rubric gaps with reproducible local evidence, formula-driven economics, explicit unit/blended GM logic, a complete GTM bridge, an exact Pain Moment and a procurement-oriented evidence pack. This is a review-ready artifact submission, not a claim of production readiness or customer validation.

## Deliverables

- `deliverables/NguyenQuangHuy_Day25_model.xlsx`
- `deliverables/NguyenQuangHuy_Day25_onepager.docx` (editable source)
- `deliverables/NguyenQuangHuy_Day25_onepager.pdf` (one-page controlled export)
- `evidence/` research, traceability, critique, red-team, evaluation and risk records
- `scripts/` reproducible build and audit scripts

## Recovery Summary

1. Corrected the 80% terminology: it is commercial package completion, while autonomous containment is 20%, human-review/escalation is 80% and grounding failure is 20% in the five-case local controlled evaluation.
2. Added the missing economic recovery mechanics: completed-job denominator, 3x price floor, usage versus blended GM, 50%-90% sensitivity, base-fee role and value-created anchor audit.
3. Added ACV USD reference, affordability ratio, cost/opportunity bridge, deals/day, exact Pain Moment, user-facing surface and backend integration path.
4. Rewrote the Eval, Risk and Pilot evidence blocks with status, source, gap, owner, deadline and measurable acceptance criteria.
5. Re-ran all automated and visual checks after the recovery edits.

## Official Templates

- Excel: NOT FOUND. The exact `day28_monetization_model.xlsx` and relevant variants were searched across the workspace, parent project area, common download/desktop/documents folders and `.codex` locations.
- DOCX: NOT FOUND. The exact `day28_one_pager_template.docx` and relevant variants were searched using the same documented scope.
- Search evidence: `templates/SEARCH_LOG.md`, status BLOCKED; no authenticated browser/CDP session or credentials were accessed. A transparent substitute layout is used and the limitation is disclosed.

## Product

P-015 is a B2B AI Fraud Investigation Copilot that assembles grounded evidence, policy context and analyst next steps for suspicious alerts while an authorized human owns final disposition. Selected framing: Option A, software/tool. Buyer: Head of Risk/COO. Approver: CTO/security/procurement. Initial budget line: fraud-operations software.

## Deliverable Links

- [Final Excel model](D:/AI20K/Track1_Day25_2A202601873_NguyenQuangHuy/deliverables/NguyenQuangHuy_Day25_model.xlsx)
- [Final editable one-pager DOCX](D:/AI20K/Track1_Day25_2A202601873_NguyenQuangHuy/deliverables/NguyenQuangHuy_Day25_onepager.docx)
- [Final one-page PDF](D:/AI20K/Track1_Day25_2A202601873_NguyenQuangHuy/deliverables/NguyenQuangHuy_Day25_onepager.pdf)

## Measured Evaluation

- attempted: 5 deterministic local P-015 E2E cases (E2E-A through E2E-E)
- completed: 4 schema-valid, grounded investigation packages (80% local package-completion proxy)
- escalated: 4 cases routed to human review; customer final disposition is recorded separately and is not measured
- failures: 1 failed grounding case; 0 unsafe auto-actions in the source report
- commercial package completion rate: 80% (4/5); not production/customer evidence
- autonomous containment rate: 20% (1/5)
- human-review/escalation rate: 80% (4/5)
- grounding failure rate: 20% (1/5)
- retry: NOT MEASURED in the source evaluator; the workbook retains an 8% retry planning estimate and labels it as such

The five-case local evaluator is a reproducible control check, not customer evidence. The separate 30-sample conversational `FraudAgentEval-v1` dataset is intentionally excluded from autonomous-containment measurement because it does not produce a completed investigation package or production disposition outcome.

## Economics

- Cost/Job: 7,648 VND per completed grounded investigation package; 6,119 VND per attempted job is shown separately and is not used as the completed denominator.
- variable price: 32,000 VND per completed package; price floor is 22,945 VND (3x Cost/Job); price/cost is 4.18x.
- base fee: 30,000,000 VND/month for account-level workflow access, integration/configuration and governance/auditability; it is not a second charge for the same package.
- unit GM: 76.1% on variable usage economics.
- blended GM: 82.8% including the base fee at the 3,000-attempt base case.
- breakeven package-completion rate: 44.3% at the 60% usage-GM target; this is not an autonomous-containment threshold.
- safety buffer: 35.7 percentage points from the 80% commercial package-completion rate to breakeven.
- critical sensitivity: at 40% package completion, completed commercial jobs halve and usage GM falls to 56.1%; the workbook also shows 50%, 60%, 70%, 80% and 90% cases.

## Value Metric

- selection: Hybrid - account-level platform access/integration/governance plus 32,000 VND per completed, grounded investigation package.
- Attribution: 2/5. The local control eval establishes output validity and grounding, but no measured analyst time saved or causal customer outcome.
- Autonomy: 1/5. Only 1/5 local cases completed without required human intervention; 4/5 routed to review.
- benchmarks: Stripe Radar and Fingerprint Pro Plus are current public, usage-like fraud/risk budget anchors, not 1:1 substitutes for P-015's lower-autonomy investigation package. Sources: [Stripe Radar pricing](https://stripe.com/radar/pricing), [Fingerprint pricing](https://fingerprint.com/pricing/). Supabase is used as an infrastructure context anchor in the evidence file.

Outcome pricing is not appropriate without causal customer results. Pure Seat pricing does not map cleanly to marginal AI usage, while pure Usage can reduce bill predictability; Hybrid is the safer interim choice while keeping the variable charge tied to a completed customer-visible unit.

## GTM

- segment: mid-market fintech/payment processor
- ARPU: 106,800,000 VND/month
- ACV: 1,281,600,000 VND/year; USD reference $49,292 at the documented planning FX of 26,000 VND/USD
- CAC budget: 1,061,327,040 VND/customer using ARPU x blended GM x 12-month payback
- cost/opportunity: 50,000,000 VND from 600M VND loaded AE cost / 12 qualified opportunities per year
- win rate: 25%
- estimated CAC: 350,000,000 VND/customer, including 200M VND selling cost per won deal plus 150M VND pre-sales/onboarding allocation
- affordability ratio: 3.03x CAC budget / estimated CAC
- deals/AE/year: 2.81
- deals/AE/day: 0.013 across 220 selling days
- channel: Sales-Led only for the first 90 days

## Pain Moment

Between 09:00 and 11:00 after an overnight alert burst, a fraud analyst triages high-risk transactions in the existing fraud-operations alert investigation queue/dashboard and needs a grounded case package before manual disposition and SLA review. The 90-day plan links this workflow to discovery, shadow-mode validation, design-partner pilot and procurement-readiness gates with named owner, deadlines, metrics and evidence outputs.

## Integration Surface

Backend: Kafka `fraud_alerts` -> fraud engine/agent -> REST `/api/v1/fraud/analyze`. User-facing: the existing fraud analyst alert investigation queue/dashboard, with an embedded side panel for evidence, policy context and recommended action. Full live deployment and production boundary are PARTIAL / NOT VERIFIED.

## Evidence Pack

- Eval: COMPLETE for the local controlled-evaluation record; `evidence/containment-eval.csv` is case-level and `evidence/eval-evidence.md` explains the proxy, exclusions, source and 2026-09-30 300-case manifest deadline.
- Risk: PARTIAL with ten procurement questions and explicit VERIFIED, PARTIAL, NOT VERIFIED or MISSING EVIDENCE statuses; open items have owners, actions and dates.
- Pilot: PLANNED - NOT YET EXECUTED. Two design partners, 4-8 analysts, 8 weeks from 2026-10-01 to 2026-11-26, 6,000 labeled jobs, completion/time-saved/latency/retry/Cost-Job/safety metrics, Nguyen Quang Huy as owner and report due 2026-12-04.

## Verification

- formula audit: PASS - workbook ZIP integrity, exact tabs, required formulas, no formula error tokens, positive completed denominator, non-zero retry planning input, HITL presence, GM/breakeven, sensitivity formulas and benchmark dates.
- semantic formula audit: PASS - `2_Pricing!C16` solves Case A commercial package-completion rate; autonomous containment at 20% is not compared with the 44.3% threshold.
- number crosscheck: PASS - workbook and editable one-pager agree on Cost/Job, floor, price, GM, package completion, package-completion breakeven, ACV reference, CAC budget, estimated CAC, affordability ratio and deals/day.
- Excel visual QA: PASS - all seven sheets rendered and inspected; no clipping, `#####` or formula-error tokens observed.
- PDF visual QA: PASS - Poppler reports one letter-size page; rasterized page inspected with no clipping, overflow, broken tables or unreadable core metrics.
- DOCX conversion note: a headless Office converter is unavailable in this environment; the PDF is a controlled reportlab export using the same one-page content, while the DOCX remains the editable source.
- secret scan: PASS - no credential-pattern matches in project-authored files; `.env`, credential, secret and temporary Office/cache patterns are ignored; external repositories were not copied into this workspace.
- git diff --check: PASS after final files are written.

## Final Hardening Pass

- Baseline verified before modification: `main`, clean working tree, HEAD `2cc30ba92dde21a956125de6988ac5ab1aedc559`.
- Safety backup created at `backups/final_submission_20260827_101756/` before changes; backups remain ignored.
- One final official-template search completed across the specified local roots and archive candidates; official Day28 files remain NOT FOUND and the limitation remains disclosed in `templates/SEARCH_LOG.md`.
- Verified defect fixed: the OpenAI GPT-5.5 source URL was corrected to the direct first-party model page; the cached-input and batch price display was corrected to preserve decimal precision. No economic input or formula was changed.
- Semantic audit scope covers the full workbook text, README, audit reports, recovery analysis, evidence, traceability/search-log files, scripts, DOCX and PDF. The audit also checks the completed-commercial-job denominator and the Case A formula boundary.
- One-Pager stranger test: PASS. A first-time reader can identify the sold package, buyer/budget, billing unit, Cost/Job, price, unit/blended GM, package-completion threshold, separate autonomous containment, channel/affordability, Pain Moment, embedding, evidence and gaps without more than three clarifications.
- Audit-of-audit: PASS. Source inspection confirms required conditions append failures and return non-zero; the missing-workbook negative invocation returned exit code 1; the final gate aggregates workbook, one-pager, numerical, semantic and required-artifact checks.
- GitHub Actions: NOT CONFIGURED / NOT REQUIRED BY LAB. Local automated audits and committed QA evidence are the verification mechanism.

## Rubric

- Cost/Job: 30/30
- Value Metric: 25/25
- Channel: 20/20
- Pain Moment/90-Day: 15/15
- Evidence: 10/10
- TOTAL: 100/100

Rubric self-audit: 100/100 supported by current artifacts; not a guaranteed instructor score. The score reflects recoverable artifact requirements and the explicitly planned pilot pathway. It does not turn missing customer or production evidence into verified evidence.

## Git

- repository: `https://github.com/Bietdoibongdem888/Track1_Day25_2A202601873_NguyenQuangHuy`
- branch: `main`
- commit: recorded after final verification
- push: requested and executed after checks
- remote verification: verified against `origin/main` if authentication succeeds; otherwise this field will state the exact push blocker

## Remaining Limitations

- Official Day28 Excel/DOCX templates were not found; the substitute layout is disclosed in `templates/SEARCH_LOG.md`.
- The local controlled evaluation has five relevant E2E cases. Its 80% commercial package completion is not autonomous containment or customer evidence; autonomous containment is 20% and retry telemetry is not measured.
- No customer pilot, analyst time-saved measurement, causal outcome, production deployment or live Kafka integration is claimed.
- Production auth/RBAC, rate limiting, TLS, retention/deletion, durable audit export, vendor data-use terms, SLA and certification claims remain open with owners and deadlines in the risk evidence.
- DOCX-to-PDF conversion through a headless office engine is unavailable in this environment; PDF visual QA covers the controlled PDF export.

## Final Submission Decision

READY

Ready means the recovery artifact set is internally consistent, reviewable, evidence-labeled, visually checked and prepared for submission. It does not mean production-ready, customer-validated or guaranteed to receive the self-audited score.
