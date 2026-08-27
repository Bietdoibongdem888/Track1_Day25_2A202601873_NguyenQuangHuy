# One-Pager traceability

Every numeric claim in the editable DOCX and final PDF maps to a workbook cell or a named P-015 evidence artifact. `EVAL` claims are local controlled-evaluation results, not customer results.

| One-Pager claim | Workbook tab | Workbook cell | Source assumption/evidence | Verification status |
|---|---|---|---|---|
| 2,400 completed packages/month | `1_Cost_Job` | `C8` | 3,000 attempts x 80% controlled grounded-package completion proxy | VERIFIED FORMULA; local-eval driver, not production |
| Cost/Job 7,648 VND | `1_Cost_Job` | `C61` | Total direct cost / completed packages | VERIFIED FORMULA |
| Price floor 22,945 VND | `2_Pricing` | `C9` | 3 x Cost/Job | VERIFIED FORMULA |
| Platform fee 30M VND/month | `2_Pricing` | `C6` | Hybrid pricing decision; workflow/integration/governance access | ASSUMPTION / DECISION |
| Usage price 32,000 VND/job | `2_Pricing` | `C7` | Proposed price decision | DECISION / NOT MARKET-VERIFIED |
| Variable / usage GM 76.1% | `2_Pricing` | `C11` | (Usage price - Cost/Job) / usage price | VERIFIED FORMULA |
| Blended GM 82.8% | `2_Pricing` | `C12` | (ARPU - monthly direct cost) / ARPU | VERIFIED FORMULA |
| Current package completion 80% | `2_Pricing` | `C14` | 4/5 grounded packages in `containment-eval.md` | LOCAL CONTROLLED EVAL; not customer containment |
| Autonomous completion 20% | N/A | N/A | `containment-eval.md`: 1/5 completed without required human intervention | VERIFIED LOCAL EVAL |
| Human-review cases 4/5 | N/A | N/A | `containment-eval.csv` | VERIFIED LOCAL EVAL |
| Failed grounding cases 1/5 | N/A | N/A | `containment-eval.csv`: missing/malformed ML score | VERIFIED LOCAL EVAL |
| Required containment 44.3% | `2_Pricing` | `C16` | Algebraic GM >=60% threshold | VERIFIED FORMULA |
| 40% adverse completion GM 56.1% | `2_Pricing` | `C19` | 2x adverse error scenario | VERIFIED FORMULA |
| Hybrid value metric | `3_Value_Metric` | `B12` | Attribution 2/5, Autonomy 1/5, matrix rule | VERIFIED DECISION |
| Attribution 2/5 and Autonomy 1/5 | `3_Value_Metric` | `B13:C14` | P-015 local evaluation and human-review architecture | VERIFIED CURRENT STATE |
| Sales-Led channel | `4_Channel_Fit` | `C6` | One-channel decision | VERIFIED DECISION |
| Monthly ARPU 106.8M VND | `4_Channel_Fit` | `C8` | Hybrid fee + 2,400 completed packages x usage price | VERIFIED FORMULA |
| ACV 1.282B VND / $49.3K reference | `4_Channel_Fit` | `C12`, `C25` | Monthly ARPU x 12; VND divided by 26,000 planning FX | VERIFIED FORMULA; USD is reference only |
| CAC budget 1,061M VND | `4_Channel_Fit` | `C11` | ARPU x GM x 12-month payback | VERIFIED FORMULA |
| Estimated CAC 350M VND | `4_Channel_Fit` | `C23` | AE cost, 12 opps/year, 25% win rate, onboarding allocation | VERIFIED FORMULA; planning assumptions |
| Affordability gap 711M VND | `4_Channel_Fit` | `C24` | CAC budget - estimated CAC | VERIFIED FORMULA |
| Affordability ratio 3.03x | `4_Channel_Fit` | `C26` | CAC budget / estimated CAC | VERIFIED FORMULA |
| Deals / AE 2.81/year and 0.013/day | `4_Channel_Fit` | `C14`, `C16` | Quota / ACV / 220 working days | VERIFIED FORMULA; planning assumptions |
| 15-minute labor anchor and 31,250 VND capture | `2_Pricing` | `C25:C29` | Labor rate 250,000 VND/hour, 50% capture | VERIFIED FORMULA; pilot validation required |
| Stripe Radar benchmark | `6_Benchmarks` | `A5:J5` | First-party pricing page checked 2026-08-27 | VERIFIED SOURCE |
| Fingerprint benchmark | `6_Benchmarks` | `A6:J6` | First-party pricing page checked 2026-08-27 | VERIFIED SOURCE |
| Eval Results status | N/A | N/A | `evidence/eval-evidence.md`, `containment-eval.*` and P-015 artifacts | VERIFIED LOCAL EVIDENCE / PARTIAL |
| Risk Checklist status | N/A | N/A | `evidence/risk-evidence.md` | VERIFIED STATUS / PARTIAL |
| Pilot Report status | N/A | N/A | `evidence/evidence-pack.md` | MISSING EVIDENCE; dated plan provided |
