# Containment / completion evaluation

Status: **LOCAL CONTROLLED EVAL — NOT PRODUCTION CUSTOMER EVIDENCE**

Generated: **2026-08-27**

## Commercial job definition

One P-015 job is commercially complete when the copilot produces a schema-valid, grounded investigation package with the required decision/evidence fields. Human review and final disposition remain customer-owned workflow steps; they are recorded separately and are not silently treated as autonomous completion.

This definition matches P-015's current copilot positioning and prevents the 4/5 intended human-review cases from being mislabeled as product failures. The autonomous-completion metric is reported separately.

## Results

| Metric | Result |
|---|---:|
| Attempted jobs | 5 |
| Completed grounded packages | 4 |
| Escalated / human review required | 4 |
| Failed grounding cases | 1 |
| Commercial completion / containment proxy | 4/5 = 80.0% |
| Completed autonomously without required human intervention | 1/5 = 20.0% |
| Retry events | 0 explicit events; retry telemetry is **NOT INSTRUMENTED** |
| Retry rate | **NOT MEASURED** |

## Case-level record

The complete machine-readable record is in [`containment-eval.csv`](containment-eval.csv). It includes case ID, input source, pipeline, report result, required fields, grounding, error, retry instrumentation, human intervention, commercial completion, autonomous completion and failure reason.

## Source and reproducibility

- Source report: `D:\AI20K\P-015\artifacts\agent\evaluation_report.md`.
- Source evaluator: `D:\AI20K\P-015\scripts\evaluate_agent.py`.
- Evaluation cases: E2E-A through E2E-E, the five cases used by the existing deterministic local evaluator.
- Pipeline boundary: supplied ML result -> Agent -> Retriever -> Reranker/fallback -> grounded report -> human-review recommendation.
- Evaluation date: 2026-08-27.

The separate P-015 `FraudAgentEval-v1` dataset has 30 chat/analytics queries, but it measures task success, facts, source selection and safety rather than completion of a fraud investigation package. It is therefore not included in this containment denominator.

## Interpretation and limitation

The 80% value is now reproducible for **grounded-package completion** in this five-case controlled evaluation, replacing the prior unexplained proxy. It is not production containment, and it does not prove analyst time saved. The 20% autonomous-completion result reinforces the decision to keep Hybrid pricing and human-owned escalation rather than claim outcome pricing.

Owner for the next evidence upgrade: Nguyen Quang Huy. Deadline: **2026-09-30** for a versioned 300-case job manifest with persisted disposition, observed retries and paired manual-vs-Copilot time measurement.
