# Product selection

## Selected product

**P-015 - AI Fraud Investigation Copilot**, a B2B investigation layer that turns a fraud alert and its upstream ML result into a grounded investigation report for a human fraud analyst.

## Product definition

P-015 helps a bank, fintech, wallet, or payment processor assemble evidence, policy references, risk signals, and analyst next steps for a suspicious transaction case while leaving the final disposition with an authorized human.

## Buyer and user

- Target buyer: Head of Risk, COO, or fraud-operations leader.
- Budget owner: fraud operations / risk software budget.
- Approver: CTO/security/procurement for integration and data controls.
- Target user: Fraud Analyst / Human Reviewer.

## Evidence repositories used

- `D:\AI20K\P-015\artifacts\agent\agent_metrics.json`
- `D:\AI20K\P-015\artifacts\agent\retrieval_metrics.json`
- `D:\AI20K\P-015\artifacts\agent\rag_metrics.json`
- `D:\AI20K\P-015\artifacts\agent\safety_metrics.json`
- `D:\AI20K\P-015\artifacts\agent\evaluation_report.md`
- `D:\AI20K\P-015\artifacts\ml\lightgbm\metrics.json`
- `D:\AI20K\P-015\docs\business_product_direction.md`
- `D:\AI20K\P-015\docs\ai_fraud_agent.md`
- `D:\AI20K\P-015\docs\security.md`
- `D:\AI20K\P-015\docs\deployment_guide.md`
- `D:\AI20K\Track1_Day23_2A202601873_NGUYENQUANGHUY\metrics-pack.md`
- `D:\AI20K\Track1_Day24_2A202601873_NguyenQuangHuy\README.md`

## Why selected

P-015 has the strongest measurable evidence chain in the student's prior work: a versioned ML artifact with validation/integration metrics, an executable local agent/RAG evaluation artifact, explicit human-review behavior, safety controls, a concrete analyst workflow, and a Day24 finance baseline. It is therefore more defensible for a cost-per-completed-investigation model than a hypothetical new product.

## Missing evidence

- No valid customer pilot, persisted customer disposition log or observed time-saved baseline was found.
- A reproducible five-case LOCAL CONTROLLED EVAL now supports an 80% grounded-package completion proxy and 20% autonomous completion; production customer containment remains unmeasured. See `evidence/containment-eval.md`.
- No verified live Kafka -> ML -> Agent deployment or production telemetry.
- Auth/RBAC, rate limiting, TLS, retention/deletion, vendor-processing terms, and a complete procurement package are not evidenced as implemented.
- Official Day28 workbook and one-pager template were not found locally; see `templates/SEARCH_LOG.md`.
