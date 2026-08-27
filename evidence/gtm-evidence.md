# GTM and affordability evidence

## Positioning options

### Option A - Software/tool framing

P-015 is a fraud investigation copilot that helps fraud analysts turn alerts into grounded, auditable investigation packages.

- Buyer: Head of Risk / COO.
- Approver: CTO, security and procurement.
- Budget owner: Software / fraud operations tooling.

### Option B - Work-replacement framing

P-015 handles the manual evidence-assembly work currently performed by fraud analysts, while the analyst retains the final case disposition.

- Buyer: Head of Risk / COO.
- Approver: CTO, security and procurement.
- Budget owner: Operations / headcount productivity.

## Selected option

**Option A - Software/tool framing.** Current evidence shows an assistive copilot with human decision ownership, not a vendor-managed outcome service. Software budget is the more honest initial line because the customer continues to own escalations and final dispositions; the model therefore uses HITL Variant A.

## Segment and primary channel

**Segment: mid-market fintech / payment processor.** The proposed ACV is about $49.3K using the model's explicit 26,000 VND/USD planning FX, while integration, security review and procurement make a self-serve motion unlikely.

**Sales-Led only** for the first 90 days. The first motion is a focused founder-led design-partner/pilot motion inside Sales-Led, not a second primary channel.

## Base affordability math

- Monthly ARPU: 106,800,000 VND = 30,000,000 VND platform fee + 2,400 completed grounded packages x 32,000 VND.
- Blended gross margin: 82.8%; variable/usage gross margin: 76.1%.
- Conservative payback: 12 months, below the mid-market 18-month ceiling.
- CAC budget: 106,800,000 x 82.8% x 12 = **1,061,327,040 VND/customer**.
- ACV: **1,281,600,000 VND/customer/year**, or **$49,292/year reference** at 26,000 VND/USD. This is not a quoted USD contract price.
- Annual AE quota assumption: 3,600,000,000 VND -> **2.81 deals/AE/year**.
- Realistic selling days: 220 -> **0.0128 deals/AE/selling day**, displayed as 0.013 in the workbook.
- AE fully loaded cost: 600,000,000 VND/year; 12 qualified opportunities/year -> **50,000,000 VND/opportunity**.
- Win-rate assumption: **25%** -> estimated selling CAC = 50,000,000 / 25% = 200,000,000 VND per won deal.
- Pre-sales/onboarding allocation: 150,000,000 VND/customer.
- Estimated CAC: **350,000,000 VND/customer**.
- Affordability headroom: **711,327,040 VND/customer** favorable.
- Affordability ratio: **1,061,327,040 / 350,000,000 = 3.03x**.

The 600M AE cost, 12 qualified opportunities, 25% win rate, 150M onboarding allocation, 220 selling days and 3.6B quota are internal Day25 planning assumptions as of 2026-08-27, not observed CRM or external benchmark facts. They must be replaced with CRM funnel evidence after the design-partner phase. Sales-Led survives the red-team because the model is integration-heavy, ACV is material, expected annual deals per AE are low, and CAC headroom is 3.03x; the conclusion remains planning-only.

## Pain Moment and integration surface

Between **09:00 and 11:00 after an overnight alert burst**, a **fraud analyst** triages high-risk transactions in the **existing fraud-operations alert investigation queue/dashboard** and needs a grounded case package before manual disposition. The customer-facing embedding is the existing analyst alert investigation queue/dashboard side panel. Backend integration is **Kafka `fraud_alerts` -> fraud engine/agent -> REST `/api/v1/fraud/analyze`**. P-015 documents this intended boundary locally, but full live integration is **PARTIAL / NOT VERIFIED**.
