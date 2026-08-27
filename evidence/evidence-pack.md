# Evidence Pack

## 1. Eval Results

Status: **PARTIAL**.

Existing evidence: a reproducible five-case local control evaluation with 4/5 grounded commercial packages (80% completion proxy), 1/5 autonomous completions (20%), 4/5 human-review cases and one grounding failure; plus agent/RAG/safety and upstream ML reports.

Source: [`eval-evidence.md`](eval-evidence.md), [`containment-eval.csv`](containment-eval.csv), and P-015 `artifacts/agent/*`, `artifacts/ml/lightgbm/metrics.json`, generated from the local P-015 evaluator on 2026-08-13 and derived on 2026-08-27.

Gap: no customer-level containment, persisted customer final-disposition log, paired manual-vs-Copilot time measurement or production retry telemetry.

Owner: Nguyen Quang Huy.

Deadline: 2026-09-30.

Exact completion criterion: produce a versioned 300-case manifest with eligible alerts, grounded package completion, autonomous completion, human-review/escalation status, persisted final disposition, retry events, p50/p95 latency and paired time-on-task measurements.

## 2. Risk Checklist

Status: **PARTIAL**.

Existing evidence: grounding checks, deterministic fallback, prompt-injection defense, ML-score preservation, PII/log redaction tests, human-review routing and fail-open observability concepts.

Source: [`risk-evidence.md`](risk-evidence.md), P-015 `docs/security.md`, `docs/deployment_guide.md`, `src/observability/*`, and tests.

Gap: authentication/RBAC, rate limiting, TLS, approved retention/deletion, durable audit export, vendor data-use terms, production incident runbook and full live deployment are not verified.

Owner: Nguyen Quang Huy.

Deadline: staged: before external pilot for auth/RBAC, retention/deletion and vendor terms; 2026-10-15 for production logging/redaction evidence; 2026-10-31 for audit export/recovery; 2026-11-15 for incident rehearsal.

Exact completion criterion: each procurement question has a verified implementation artifact, test or signed policy; no prototype HTTP/PLAINTEXT control is presented as production security.

## 3. Pilot Report

Status: **PLANNED — NOT YET EXECUTED / MISSING EVIDENCE**.

Existing evidence: no completed customer or participant pilot; only a concrete protocol is supplied.

Source: this plan and `5_90Day_Plan` in the workbook.

Gap: customer access, participant consent, job manifest, paired manual baseline and measured outcome/time data.

Owner: Nguyen Quang Huy for measurement design and report; customer fraud team owns final dispositions.

Start date: 2026-10-01. End date: 2026-11-26. Report deadline: 2026-12-04.

Exact completion criterion: two design partners with 4–8 analysts total, at least 6,000 labeled eligible investigations, completion/containment, correction/escalation rate, p50/p95 investigation time, retry rate, direct Cost/Job, safety outcomes and a user acceptance question answered. Success requires >=85% measured package completion, >=70% blended GM after telemetry, no unsafe auto-action, and a paired time-saved measurement without claiming it in advance.

## Procurement objection table

| Question | Status | Evidence | Next action | Deadline |
|---|---|---|---|---|
| Can AI output be wrong? | PARTIAL | Grounding and unsupported-claim checks exist; customer acceptance baseline is absent. | Run independent sample review and record corrections. | 2026-09-30 |
| What happens on uncertain cases? | VERIFIED | Missing/malformed score and injection cases route to review/fallback. | Add this behavior to pilot acceptance test. | Before pilot |
| Is human review required? | VERIFIED CURRENT STATE | E2E cases and P-015 docs keep human ownership of final disposition. | Instrument persisted disposition. | 2026-09-30 |
| Where is customer data stored? | NOT VERIFIED | Local persistence/deployment docs do not establish a customer-approved production region. | Produce deployment/data-flow decision. | Before pilot |
| Is customer data used for model training? | MISSING EVIDENCE | No signed vendor data-processing/training-use position for customer deployment. | Obtain vendor terms and customer approval. | Before pilot |
| How are PII/secrets handled? | PARTIAL | Redaction tests and log hooks exist; production retention and all paths are not verified. | Complete redaction/secret scan and retention test. | 2026-10-15 |
| What happens when model/API is unavailable? | PARTIAL | Deterministic fallback and fail-open observability concepts exist; full recovery is not verified. | Run outage rehearsal with evidence. | 2026-10-31 |
| How are actions/logs audited? | PARTIAL | Review persistence and audit concepts exist; durable export is not verified. | Implement/export audit trail and test replay. | 2026-10-31 |
| How can data be deleted/exported? | MISSING EVIDENCE | No approved deletion schedule, deletion test or customer export was found. | Define and test retention/deletion/export. | Before pilot / 2026-10-31 |
| What controls are not production-verified? | NOT VERIFIED | Live Kafka/ML, auth/RBAC, rate limiting, TLS, incident runbook and vendor terms remain open. | Close each item with artifact, test or signed policy. | 2026-11-15 |

No SOC 2, ISO 27001, DPA, enterprise SLA, production encryption guarantee or formal retention promise is claimed.
