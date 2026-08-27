# One-Pager traceability

Every numeric claim in the editable DOCX and final PDF maps to an official workbook cell or a named P-015 evidence artifact. The 80.0% package-completion result is not the 20.0% autonomous-containment result.

| One-Pager claim | Official workbook tab/cell | Source assumption/evidence | Verification status |
|---|---|---|---|
| Cost/Job $0.5422/job (~₫14,150) | 1_Cost_Job!B66; VND B69 | Completed autonomous-job cost; FX B68 | VERIFIED FORMULA |
| Price floor $1.6267/job | 2_Pricing!B7 | 3x Cost/Job | VERIFIED FORMULA |
| Proposed price $1.75/job | 2_Pricing!B19 | Planning decision; not a customer quote | DECISION / ASSUMPTION |
| GM 69.0% | 2_Pricing!B21 | (price - Cost/Job) / price | VERIFIED FORMULA |
| Breakeven autonomous containment 15.5% | 2_Pricing!B33 | Official usage-case breakeven; not package completion | VERIFIED FORMULA |
| Current autonomous containment 20.0% | 1_Cost_Job!B10 | 1/5 local controlled evaluation | VERIFIED LOCAL EVAL |
| Autonomous jobs/month 600 | 1_Cost_Job!B11 | 3,000 attempts x 20% autonomous containment | VERIFIED FORMULA / planning volume |
| Package-completion/non-autonomous jobs 2,400 | 1_Cost_Job!B12 | 3,000 attempts minus 600 autonomous jobs | VERIFIED FORMULA |
| Commercial package completion 80.0% | N/A | evidence/containment-eval.md: 4/5 grounded packages | LOCAL CONTROLLED EVAL; not autonomous containment or customer evidence |
| Human-review/escalation 80.0% | N/A | evidence/containment-eval.csv: 4/5 | VERIFIED LOCAL EVAL |
| Grounding failure 20.0% | N/A | evidence/containment-eval.csv: 1/5 | VERIFIED LOCAL EVAL |
| Attribution 2/10 | 3_Value_Metric!B10 | Scorecard | VERIFIED DECISION |
| Autonomy 1/10 | 3_Value_Metric!B18 | Scorecard | VERIFIED DECISION |
| Value metric Hybrid | 3_Value_Metric!B30 | Decision note and evidence boundary | VERIFIED DECISION |
| Benchmark rows | 3_Value_Metric!A26:D27 | Intercom Fin and Zendesk AI agents; checked 2026-08-27 | VERIFIED SOURCE |
| ARPU $1,050/month | 4_Channel_Fit!B5 | $1.75 x 600 completed autonomous jobs/month | VERIFIED FORMULA / pure-usage scenario |
| GM used in channel math 69.0% | 4_Channel_Fit!B6 | Cross-sheet reference to 2_Pricing!B21 | VERIFIED FORMULA |
| CAC budget $13,043.88/customer | 4_Channel_Fit!B9 | Official Channel Fit formula | VERIFIED FORMULA |
| ACV $12,600/year | 4_Channel_Fit!B10 | ARPU x 12 | VERIFIED FORMULA |
| Deals/AE/year 39.68 | 4_Channel_Fit!B15 | Quota / ACV | VERIFIED FORMULA / planning assumption |
| Deals/AE/day 0.180 | 4_Channel_Fit!B16 | Deals/year / 220 working days | VERIFIED FORMULA / planning assumption |
| Cost/opportunity $3,000 | 4_Channel_Fit!B20 | Founder-led planning input; not CRM measurement | ASSUMPTION |
| Win rate 25% | 4_Channel_Fit!B21 | Founder-led planning input | ASSUMPTION |
| Estimated CAC $12,000/customer | 4_Channel_Fit!B22 | Cost/opportunity / win rate | VERIFIED FORMULA / planning assumption |
| Estimated/budget 0.92x | 4_Channel_Fit!B23 | Estimated CAC / CAC budget | VERIFIED FORMULA |
| Budget coverage 1.09x | Derived B9 / B22 | Inverse of official B23 | DERIVED |
| 90-day plan | 5_90Day_Plan!B12:D18 | Channels, targets, activities, evidence, KPIs, owners | VERIFIED OFFICIAL TEMPLATE |
| Eval/Risk/Pilot status | 5_90Day_Plan!B23:D25 | Status, evidence/gap, owner/deadline | VERIFIED OFFICIAL TEMPLATE |
| Stranger-test limitation | 5_90Day_Plan!B32 | NOT YET TESTED; target <=3 questions | HONEST LIMITATION |

## Boundary note

A completed commercial package is a grounded investigation package with required evidence and decision fields. Human review and final disposition remain customer-owned. The official usage economics use autonomous jobs as the denominator, so package completion and autonomous containment are never silently substituted for one another.
