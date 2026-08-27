# Eval Results evidence

Status: **PARTIAL — LOCAL CONTROLLED EVAL exists; production/customer autonomous containment is not measured.**

Existing evidence: P-015's deterministic E2E evaluator, agent/RAG/safety metrics, upstream LightGBM metrics, and the derived case-level record in [`containment-eval.csv`](containment-eval.csv).

Source: `D:\AI20K\P-015\scripts\evaluate_agent.py`, `D:\AI20K\P-015\artifacts\agent\evaluation_report.md`, `agent_metrics.json`, `retrieval_metrics.json`, `rag_metrics.json`, `safety_metrics.json`, and `artifacts\ml\lightgbm\metrics.json`. The source E2E run was generated on 2026-08-13; the derived Day25 record was generated on 2026-08-27.

Gap: no customer pilot, persisted customer final-disposition log, paired manual-vs-Copilot time measurement, or production retry telemetry.

Owner: Nguyen Quang Huy.

Deadline: 2026-09-30 for a versioned 300-case job manifest and baseline protocol.

Exact completion criterion: count eligible alert opportunities, schema-valid grounded investigation packages, human-review cases, grounding failures, persisted final dispositions and observed retries; report commercial package completion, autonomous containment, human-review/escalation rate, retry rate and p50/p95 latency separately.

## Job-level controlled evaluation

This is **LOCAL CONTROLLED EVAL — NOT PRODUCTION CUSTOMER EVIDENCE**. The commercial job is a schema-valid, grounded investigation package with required decision/evidence fields. Human review and final disposition remain customer-owned steps and are recorded separately; autonomous completion is not substituted for commercial package completion.

| Metric | Result | Interpretation |
|---|---:|---|
| Attempted jobs | 5 | E2E-A through E2E-E from the existing P-015 evaluator. |
| Commercial package completion rate | 4/5 = 80.0% | One completed commercial job is one completed grounded investigation package. |
| Human-review / escalation rate | 4/5 = 80.0% | Consistent with a human-gated copilot, not an autonomous outcome service. |
| Autonomous containment rate | 1/5 = 20.0% | Completed without required human intervention; reported separately from commercial package completion. |
| Grounding failure rate | 1/5 = 20.0% | E2E-D had a missing/malformed ML score and was routed to review. |
| Retry events | 0 explicit events | Retry instrumentation is not present in the source evaluator. |
| Retry rate | NOT MEASURED | The cost model retains an explicit 8% planning estimate until telemetry exists. |

The reproducible derivation and every case-level field are in [`containment-eval.md`](containment-eval.md) and [`containment-eval.csv`](containment-eval.csv). The 80% model input is therefore a **LOCAL CONTROLLED EVAL commercial package-completion rate**, not autonomous containment or an observed customer rate.

## Agent and RAG evidence

| Evaluation | Sample | Result | Interpretation |
|---|---:|---:|---|
| Agent structured output validity | 5 cases | 100% | All local reports validated against the structured schema. |
| Human-escalation expectation accuracy | 5 cases | 100% | Includes missing-score and prompt-injection cases. |
| Grounding rate | 5 cases | 80% | Four grounded packages; one missing-score case was ungrounded and routed to review. |
| Unsupported-claim rate | 5 cases | 0% | Local deterministic evaluation only. |
| Unsafe auto-action rate | 5 cases | 0% | Agent recommends; it does not approve/block/hold automatically. |
| ML score mutation rate | 5 cases | 0% | Upstream score was preserved. |
| Retrieval context relevance | 8 queries | 100% | Local labelled retrieval set. |
| RAG faithfulness | 8 queries | 100% | Local deterministic grounding evaluator. |
| Citation accuracy | 8 queries | 100% | Local synthetic policy corpus. |
| Agent p95 latency | 5 cases | 9.33 ms | Deterministic path; no remote LLM call. |

## Upstream ML evidence

| Split | Rows | Recall | ROC-AUC | Alert rate |
|---|---:|---:|---:|---:|
| Validation | 209,712 | 80.08% | 0.8420 | 29.26% |
| Integration | 104,853 | 84.84% | 0.8979 | 27.74% |

These are upstream fraud-ranking metrics, not investigation package completion. The separate P-015 `FraudAgentEval-v1` dataset has 30 chat/analytics queries, but it measures facts, task success, source selection and safety rather than completed fraud-investigation packages; it is not used in this denominator.
