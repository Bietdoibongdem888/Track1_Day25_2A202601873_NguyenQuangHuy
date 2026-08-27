# GTM and affordability evidence

## Positioning

P-015 is a fraud investigation copilot that helps fraud analysts turn alerts into grounded, auditable investigation packages.

- Buyer: Head of Risk / COO.
- Approver: CTO, security and procurement.
- Budget owner: software / fraud operations tooling.
- Commercial recommendation: Hybrid — platform/governance access plus measured usage.
- Official workbook economics: pure usage at $1.75 per completed autonomous job; this is a planning case, not a customer quote.

## Segment and primary channel

**Segment: mid-market fintech / payment processor.**

**Sales-Led only** for the first 90 days. The initial motion is founder-led design-partner and paid-pilot selling within one primary channel; PLG and Partner-Led are not selected.

## Official channel math

All values below are copied from the official 4_Channel_Fit tab:

- ARPU: **$1,050/month** from 600 completed autonomous jobs/month at $1.75/job.
- ACV: **$12,600/year**.
- CAC budget: **$13,043.88/customer**.
- Estimated CAC: **$12,000/customer**.
- Official estimated/budget ratio: **0.92x**.
- Derived budget coverage: **1.09x** = 13,043.88 / 12,000.
- Deals/AE/year: **39.68**.
- Deals/AE/day: **0.180** across 220 working days.
- Planning cost/opportunity: **$3,000**.
- Win rate: **25%**.
- The $3,000 opportunity input is a founder-led first-90-day planning assumption, not CRM measurement. It must be replaced after pilot funnel data.

The chosen channel remains a planning conclusion: integration, security review, customer-owned disposition and a material first-year ACV support a founder-led Sales-Led motion. No conversion or win-rate claim is presented as observed customer evidence.

## Pain Moment and integration surface

Between **09:00 and 11:00 after an overnight alert burst**, a **fraud analyst** triages high-risk transactions in the **existing fraud-operations alert investigation queue/dashboard** and needs a grounded case package before manual disposition. The customer-facing embedding is the queue/dashboard side panel. Intended backend path: Kafka fraud_alerts -> fraud engine/agent -> REST /api/v1/fraud/analyze. Full live integration is **PARTIAL / NOT VERIFIED**.

## Evidence needed next

The 90-day plan requires 8 fraud-operations interviews, 2 design partners, a 300-case baseline, then 2 paid pilots / 6,000 labeled jobs with paired manual-vs-Copilot time measurement, autonomous containment separated from package completion, and procurement/security closure before expansion.
