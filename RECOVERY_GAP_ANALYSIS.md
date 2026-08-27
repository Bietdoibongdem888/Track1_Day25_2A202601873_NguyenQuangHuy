# Day25 recovery gap analysis

Baseline: first-pass self-audit **87/100**. This recovery pass targets the 13 points previously withheld; it does not convert missing customer or production evidence into completed evidence.

| Criterion / point group | Baseline self-audit | Maximum | Reason for deduction | Evidence needed to recover point | Can it be recovered now? | Action | Result |
|---|---:|---:|---|---|---|---|---|
| Cost/Job — point 29 | 28/30 | 30 | The 80% package-completion result was previously described as containment rather than as a separate commercial completion metric. | Directly relevant local E2E cases with attempted, grounded package, escalation and failure fields. | YES | Derived five-case local control eval from P-015's existing deterministic E2E report. | RECOVERED: commercial package completion 4/5 (80%); autonomous containment 1/5 (20%); human-review/escalation 4/5 (80%); grounding failure 1/5 (20%). |
| Cost/Job — point 30 | 28/30 | 30 | The prior model needed a clearer unit/blended GM distinction and explicit sensitivity/price bridge. | Unit GM, blended GM, base-fee rationale, price/floor bridge and 50–90% sensitivity. | YES | Added usage GM, blended GM, value-created anchor audit, base-fee rationale and sensitivity table. | RECOVERED: all required model mechanics are visible and formula-driven. |
| Value Metric — point 23 | 22/25 | 25 | The prior note did not explicitly reject Outcome and explain why current autonomy/attribution constrain it. | Three-sentence evidence-based Decision Note. | YES | Rewrote the exact three-sentence note with 2/5 Attribution and 1/5 Autonomy evidence. | RECOVERED. |
| Value Metric — point 24 | 22/25 | 25 | Seat, pure Usage and Hybrid trade-offs were not all explicit; base fee role was under-specified. | Clear distinction between account-level base fee and completed-package variable charge. | YES | Added base-fee purchase, variable unit, predictability and double-charge logic to workbook/memo. | RECOVERED. |
| Value Metric — point 25 | 22/25 | 25 | Benchmarks were adjacent but their similarity/difference was not explicit enough. | Current first-party prices, billing units, dates and similarity caveats. | YES | Rechecked Stripe Radar/Fingerprint pages and clarified both are usage-like fraud/risk anchors, not P-015 equivalents. | RECOVERED. |
| Channel — point 18 | 17/20 | 20 | ACV lacked a documented USD reference and affordability was only a VND gap. | ACV in VND/USD and affordability ratio. | YES | Added ACV USD reference using documented 26,000 VND/USD planning FX and 3.03x ratio. | RECOVERED. |
| Channel — point 19 | 17/20 | 20 | CAC estimate lacked a sufficiently explicit cost-per-opportunity bridge and source/date context. | Cost/opportunity, win rate, estimated CAC, source/date and assumptions. | YES | Added 50M VND/opportunity, 25% win rate, 350M CAC and 2026-08-27 planning-assumption context. | RECOVERED. |
| Channel — point 20 | 17/20 | 20 | Deals/day and customer-facing distribution surface were not prominent enough. | Deals/AE/year/day plus exact customer-facing workflow surface. | YES | Added 2.81/year, 0.013/day, user-facing alert queue/dashboard and separate backend integration. | RECOVERED. |
| Pain Moment / 90-Day — point 14 | 13/15 | 15 | Pain Moment named a time window but did not fully name actor, task and customer-facing app/surface. | Time/context + actor action + exact application surface. | YES | Rewrote the Pain Moment around a fraud analyst triaging the existing fraud-operations alert investigation queue/dashboard. | RECOVERED. |
| Pain Moment / 90-Day — point 15 | 13/15 | 15 | Integration path was partly architecture and the execution plan lacked a direct surface link. | Backend/user-facing separation and measurable phase gates. | YES | Separated Kafka/backend flow from embedded queue/dashboard and retained owner, deadlines, metrics and evidence outputs for all phases. | RECOVERED. |
| Evidence Pack — point 8 | 7/10 | 10 | Eval Results lacked a complete status block and case-level job record. | Status, existing evidence, source, gap, owner, deadline, criterion and case-level CSV. | YES | Added `containment-eval.md`, `containment-eval.csv`, reproducible builder and complete Eval status block with separate package-completion and autonomous-containment rates. | RECOVERED. |
| Evidence Pack — point 9 | 7/10 | 10 | Risk gaps were listed but procurement answers did not consistently use verified/partial/not-verified states with next actions. | Ten-question procurement table with evidence, action and deadline. | YES | Rewrote `risk-evidence.md` and `evidence-pack.md` with explicit statuses and dated actions. | RECOVERED. |
| Evidence Pack — point 10 | 7/10 | 10 | Pilot was honestly missing, but the protocol and completion criteria were not maximally explicit. | PLANNED / NOT YET EXECUTED protocol with profile, participants, dates, jobs, metrics, threshold, owner and report deadline. | YES | Added complete two-design-partner, 8-week, 6,000-job protocol and report deadline 2026-12-04. | RECOVERED as rubric-plan evidence; pilot remains unexecuted. |

## Recovery conclusion

- Recoverable rubric points: **13/13**.
- New rubric self-audit: **100/100 supported by current artifacts**.
- This is not a guarantee of instructor scoring.
- Non-scoring/readiness limitations remain: official Day28 templates were not recovered; the controlled evaluation has only five relevant cases; customer pilot/time-saved evidence and production security/deployment evidence remain open.
- These limitations are disclosed in the deliverables and do not get silently relabeled as verified customer evidence.

## Semantic consistency patch

- Case selected: **A**. `2_Pricing!C16` solves the commercial package-completion rate required by the GM equation because completed commercial jobs are `attempted jobs x package-completion rate`; it does not solve autonomous containment.
- Canonical local-eval rates: commercial package completion **80% (4/5)**; autonomous containment **20% (1/5)**; human-review/escalation **80% (4/5)**; grounding failure **20% (1/5)**.
- Economic comparison: current package completion **80%** versus breakeven package-completion rate **44.3%**, buffer **+35.7 percentage points**. Autonomous containment **20%** is explicitly excluded from this threshold comparison.
- Semantic/formula audit: **PASS** across workbook, DOCX/PDF source builders, README, final audit, gap analysis, evidence and traceability files.
