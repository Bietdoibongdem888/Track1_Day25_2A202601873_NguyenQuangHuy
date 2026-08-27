# Day25 Final Submission Manifest

Student: Nguyen Quang Huy  
Student ID: 2A202601873  
Assignment: Day25 - AI Pricing, GTM and Evidence  
Product: P-015 AI Fraud Investigation Copilot

Repository: https://github.com/Bietdoibongdem888/Track1_Day25_2A202601873_NguyenQuangHuy

## Submit to LMS

1. `NguyenQuangHuy_Day25_model.xlsx`
2. `NguyenQuangHuy_Day25_onepager.pdf`

Supporting source: `NguyenQuangHuy_Day25_onepager.docx`

## Canonical metrics

- Commercial package completion rate: 80% (4/5).
- Autonomous containment rate: 20% (1/5).
- Human-review/escalation rate: 80% (4/5).
- Grounding failure rate: 20% (1/5).
- Cost/Job: 7,648 VND per completed commercial job.
- Usage price: 32,000 VND per completed grounded investigation package.
- Base fee: 30,000,000 VND/month.
- Breakeven package-completion rate: 44.3%; package-completion buffer: +35.7 percentage points.
- Unit GM: 76.1%; blended GM: 82.8%.
- Attribution: 2/5; Autonomy: 1/5; value metric: Hybrid.

## Formula and commercial definition

Case A is confirmed. `2_Pricing!C16` solves for the minimum commercial package-completion rate required by the usage-GM equation. It compares 80% commercial package completion with the 44.3% breakeven package-completion rate. The 20% autonomous containment result is not compared with that threshold.

One completed commercial job is one completed grounded investigation package with the required evidence and decision fields. The 32,000 VND variable charge is tied to that package boundary. Human review and customer final disposition remain separate workflow steps and are not represented as autonomous AI completion. Outcome pricing is not claimed.

## Evidence status

- Five-case result: small local controlled evidence, not customer evidence.
- Pilot: planned, not executed; no customer or participant is fabricated.
- Risk/procurement: partial, with open production controls and dated owners/actions.
- Official Day28 templates: not found after the documented local search; substitute layout disclosed in `templates/SEARCH_LOG.md`.
- GitHub Actions: NOT CONFIGURED / NOT REQUIRED BY LAB. Local automated audits and visual inspection are the verification mechanism.

## GTM

- Channel: Sales-Led only for the first 90 days.
- ARPU: 106,800,000 VND/month; ACV: 1,281,600,000 VND/year; USD reference: $49.3K at 26,000 VND/USD.
- CAC budget: 1,061,327,040 VND/customer; estimated CAC: 350,000,000 VND/customer; affordability ratio: 3.03x.

## Verification record

- Workbook formula audit: PASS.
- Numerical crosscheck: PASS.
- Semantic consistency audit: PASS.
- All seven Excel sheets rendered and inspected: PASS.
- One-page PDF rendered and visually inspected: PASS.
- DOCX structure audit and PDF page-count audit: PASS.
- Secret scan: PASS.
- `git diff --check`: PASS.
- Audit scripts reject the missing-workbook negative case: PASS.

Final commit SHA: PENDING FINAL GIT COMMIT  
Final remote HEAD: PENDING PUSH VERIFICATION

## Submission decision

READY WITH DISCLOSED LIMITATIONS. Suitable for LMS artifact submission; not a claim of production readiness, customer validation, autonomous containment, outcome pricing or a guaranteed instructor score.
