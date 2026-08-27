# Risk checklist and procurement evidence

Status: **PARTIAL**.

Existing evidence: P-015 implementation notes and tests cover some safeguards; prototype and production gaps are separated below. Reviewed 2026-08-27.

| Procurement question | Status | Evidence / gap | Owner + next action | Deadline |
|---|---|---|---|---|
| Can AI output be wrong? | PARTIAL | Grounding/unsupported-claim checks and deterministic fallback exist; no independent customer acceptance baseline. | Nguyen Quang Huy: run independent sample review and corrections log. | 2026-09-30 |
| What happens on uncertain cases? | VERIFIED | Missing-score, malformed-input and prompt-injection cases route to review/fallback. | Add as pilot acceptance test. | Before pilot |
| Is human review required? | VERIFIED CURRENT STATE | P-015 docs and E2E evaluation keep human ownership of final disposition. | Instrument persisted disposition. | 2026-09-30 |
| Where is customer data stored? | NOT VERIFIED | Local persistence/deployment docs do not establish a customer-approved production region. | Produce data-flow and deployment decision. | Before pilot |
| Is customer data used to train a model? | MISSING EVIDENCE | No signed vendor data-processing or training-use position for customer deployment. | Obtain vendor terms and customer approval. | Before pilot |
| How are PII and secrets handled? | PARTIAL | Python observability redaction and tests exist; Java/other paths and production retention are not fully evidenced. | Complete all-path redaction and secret-handling test. | 2026-10-15 |
| What happens when model/API is unavailable? | PARTIAL | Deterministic fallback and fail-open observability concepts are documented; full ML/Kafka recovery is not verified. | Run outage/recovery rehearsal. | 2026-10-31 |
| How are actions and logs audited? | PARTIAL | Review persistence and audit concepts exist; durable export and replay are not verified. | Implement/export audit trail and test replay. | 2026-10-31 |
| How can data be deleted or exported? | MISSING EVIDENCE | No approved customer retention/deletion schedule, deletion test or durable export was found. | Define and test retention/deletion/export. | Before pilot / 2026-10-31 |
| What controls are not production-verified? | NOT VERIFIED | Auth/RBAC, rate limiting, TLS, live Kafka/ML deployment, vendor terms, incident runbook and SLA remain open. | Close each with artifact, test or signed policy. | 2026-11-15 |

Source files: `D:\AI20K\P-015\docs\security.md`, `deployment_guide.md`, `ai_fraud_agent.md`, observability/redaction code and tests. Unit tests are not treated as proof of production security.

No SOC 2, ISO 27001, DPA, enterprise SLA, production encryption guarantee or formal retention promise is claimed in the Day25 artifacts.
