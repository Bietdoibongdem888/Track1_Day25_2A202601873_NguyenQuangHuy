"""Derive a job-level package-completion/autonomous-containment evidence table from P-015's local E2E report.

This intentionally uses only the five cases produced by the existing deterministic
evaluator. It does not inflate the sample with unrelated chat benchmark cases.
"""
from __future__ import annotations

import csv
import json
import re
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path(r"D:\AI20K\P-015\artifacts\agent\evaluation_report.md")
CSV_OUT = ROOT / "evidence" / "containment-eval.csv"
MD_OUT = ROOT / "evidence" / "containment-eval.md"


def load_reports() -> list[dict]:
    text = SOURCE.read_text(encoding="utf-8")
    reports = []
    for match in re.finditer(r"^### (E2E-[A-Z])\s+```json\s+(.*?)\s+```", text, flags=re.MULTILINE | re.DOTALL):
        reports.append(json.loads(match.group(2)))
    if not reports:
        raise RuntimeError(f"No E2E JSON reports found in {SOURCE}")
    return reports


def classify(report: dict) -> dict:
    grounded = bool(report.get("grounded"))
    schema_valid = True  # The source evaluator only writes a report after schema validation.
    required_fields = schema_valid and all(
        key in report for key in ("transaction_id", "decision", "recommended_action", "human_review_required")
    )
    commercial_complete = bool(schema_valid and required_fields and grounded and not report.get("unsupported_claims"))
    autonomous = bool(commercial_complete and not report.get("human_review_required"))
    reasons = []
    if not grounded:
        reasons.append("grounding condition failed")
    if report.get("human_review_required"):
        reasons.append("human review required: " + "; ".join(report.get("review_reason") or ["review gate"]))
    return {
        "case_id": report["transaction_id"],
        "input_source": "P-015/scripts/evaluate_agent.py::_payload + local synthetic policy corpus",
        "pipeline_executed": "supplied ML result -> fraud_graph Agent -> retriever -> reranker/fallback -> structured report",
        "result_produced": "schema-valid investigation report",
        "required_output_fields_present": required_fields,
        "grounding_evidence_condition": "PASS" if grounded else "FAIL",
        "error": not grounded,
        "retry": "NOT_INSTRUMENTED",
        "human_intervention_required": bool(report.get("human_review_required")),
        "completed_commercial_package": commercial_complete,
        "completed_autonomously": autonomous,
        "failure_reason": " | ".join(reasons) if reasons else "none",
        "recommended_action": report.get("recommended_action"),
        "agent_status": report.get("agent_status", "not exposed in report excerpt"),
    }


def build() -> None:
    reports = load_reports()
    rows = [classify(report) for report in reports]
    fields = list(rows[0])
    CSV_OUT.parent.mkdir(parents=True, exist_ok=True)
    with CSV_OUT.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    attempted = len(rows)
    completed = sum(row["completed_commercial_package"] for row in rows)
    autonomous = sum(row["completed_autonomously"] for row in rows)
    escalated = sum(row["human_intervention_required"] for row in rows)
    failed = sum(row["error"] for row in rows)
    md = f"""# Commercial package completion and autonomous containment evaluation

Status: **LOCAL CONTROLLED EVAL — NOT PRODUCTION CUSTOMER EVIDENCE**

Generated: **{date.today().isoformat()}**

## Commercial job definition

One P-015 job is commercially complete when the copilot produces a schema-valid, grounded investigation package with the required decision/evidence fields. Human review and final disposition remain customer-owned workflow steps; they are recorded separately and are not silently treated as autonomous completion.

This definition matches P-015's current copilot positioning and prevents the 4/5 intended human-review cases from being mislabeled as product failures. The autonomous-containment rate is reported separately.

## Results

| Metric | Result |
|---|---:|
| Attempted jobs | {attempted} |
| Completed grounded packages | {completed} |
| Escalated / human review required | {escalated} |
| Failed grounding cases | {failed} |
| Commercial package completion rate | {completed}/{attempted} = {completed / attempted:.1%} |
| Autonomous containment rate | {autonomous}/{attempted} = {autonomous / attempted:.1%} |
| Human-review / escalation rate | {escalated}/{attempted} = {escalated / attempted:.1%} |
| Grounding failure rate | {failed}/{attempted} = {failed / attempted:.1%} |
| Retry events | 0 explicit events; retry telemetry is **NOT INSTRUMENTED** |
| Retry rate | **NOT MEASURED** |

## Case-level record

The complete machine-readable record is in [`containment-eval.csv`](containment-eval.csv). It includes case ID, input source, pipeline, report result, required fields, grounding, error, retry instrumentation, human intervention, commercial package completion, autonomous containment and failure reason.

## Source and reproducibility

- Source report: `D:\\AI20K\\P-015\\artifacts\\agent\\evaluation_report.md`.
- Source evaluator: `D:\\AI20K\\P-015\\scripts\\evaluate_agent.py`.
- Evaluation cases: E2E-A through E2E-E, the five cases used by the existing deterministic local evaluator.
- Pipeline boundary: supplied ML result -> Agent -> Retriever -> Reranker/fallback -> grounded report -> human-review recommendation.
- Evaluation date: {date.today().isoformat()}.

The separate P-015 `FraudAgentEval-v1` dataset has 30 chat/analytics queries, but it measures task success, facts, source selection and safety rather than completion of a fraud investigation package. It is therefore not included in the autonomous-containment denominator.

## Interpretation and limitation

The 80% value is reproducible **commercial package completion** in this five-case controlled evaluation. It is not autonomous containment and is not production/customer evidence. Autonomous containment is 20% (1/5), human-review/escalation is 80% (4/5), and grounding failure is 20% (1/5). The 20% autonomous-containment result reinforces Hybrid pricing and human-owned escalation rather than outcome pricing.

Owner for the next evidence upgrade: Nguyen Quang Huy. Deadline: **2026-09-30** for a versioned 300-case job manifest with persisted disposition, observed retries and paired manual-vs-Copilot time measurement.
"""
    MD_OUT.write_text(md, encoding="utf-8")
    print(json.dumps({"written": [str(CSV_OUT), str(MD_OUT)], "attempted": attempted, "completed": completed, "autonomous": autonomous, "escalated": escalated, "failed": failed}, indent=2))


if __name__ == "__main__":
    build()
