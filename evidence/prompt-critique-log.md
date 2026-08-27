# AI critique and red-team log

The student owns the final decisions. Each critique was applied as a structured pre-submission review on 2026-08-27; suggestions were accepted, rejected or partially accepted rather than pasted into the final deliverables.

| Critique mode | Suggestion | Decision | Reason | Artifact changed |
|---|---|---|---|---|
| Cost/Job Stress Test | Retry must be non-zero; HITL and completed-job denominator must be explicit; cache delta and attempted-vs-completed error must be visible. | ACCEPT | These are material economic drivers and required by the rubric. | `1_Cost_Job`, `evidence/eval-evidence.md` |
| Cost/Job Stress Test | Put all escalations into vendor COGS to look conservative. | PARTIAL | Variant A is the truthful software model: customer owns escalations; the workbook discloses the customer-borne labor separately while internal QA stays in COGS. | `1_Cost_Job`, `evidence/gtm-evidence.md` |
| Value Metric Challenger | Do not select Outcome without causal customer evidence and end-to-end autonomy. | ACCEPT | Current evidence is assistive and human-gated. | `3_Value_Metric`, `2_Pricing` |
| Value Metric Challenger | Seat is the safest metric because P-015 is a tool. | REJECT | Usage aligns a portion of revenue with job volume/cost; Hybrid preserves a platform fee for access/integration. | `3_Value_Metric`, `evidence/value-metric-benchmarks.md` |
| Channel Reality Check | Choose one channel; integration/procurement cycles make PLG unlikely for this workflow. | ACCEPT | Sales-Led is the only primary 90-day channel; founder-led pilots are a tactic within it, not a second channel. | `4_Channel_Fit`, `5_90Day_Plan` |
| Procurement Objection Simulator | Add explicit FAIL/MISSING EVIDENCE states for auth, retention, encryption, vendor training use, export and incident response. | ACCEPT | P-015 docs show these gaps; hiding them would be misleading. | `evidence/risk-evidence.md`, `evidence/evidence-pack.md` |
| One-Pager Defensibility Check | Every numeric claim must point to a workbook cell or evidence file, and estimates must be labeled. | ACCEPT | Prevents conflicts between memo and model. | `evidence/onepager-traceability.md`, one-pager |

## Recovery pass decisions

| Finding | Decision | Reason | Change made |
|---|---|---|---|
| The old 80% value was only described as an estimate. | ACCEPT | P-015 has five directly relevant deterministic E2E reports; derive a reproducible package-completion record without using unrelated chat queries. | Added `containment-eval.md`, `containment-eval.csv` and `build_containment_eval.py`; model now labels 80% as a local controlled-eval proxy and reports 20% autonomous completion separately. |
| The 30-case FraudAgentEval dataset could increase the denominator. | REJECT | It evaluates chat/analytics task success and safety, not completed investigation packages; using it as containment would be semantically invalid. | Kept it as contextual evidence only. |
| Hybrid needs separate unit and blended economics. | ACCEPT | The base fee and per-package charge have different economic roles and must not be conflated. | Workbook, DOCX and PDF now show variable GM and blended GM; base fee rationale is workflow/integration/governance access, not outcome billing. |
| Sales-Led affordability needed a ratio and USD ACV. | ACCEPT | A positive VND gap alone is incomplete. | Added ACV USD reference, affordability ratio, explicit cost/opportunity, win-rate and deals/day traceability. |
| Pain Moment was too architectural. | ACCEPT | The user-facing surface must connect the actor's task to the existing workflow. | Rewrote the Pain Moment with time, actor, task and alert-queue/dashboard surface; separated backend integration from customer-facing embedding. |
| A missing pilot should be hidden to avoid a deduction. | REJECT | No customer or participant evidence may be fabricated. | Added complete status blocks, a dated protocol, owners, criteria and procurement deadlines; retained `MISSING EVIDENCE`. |
