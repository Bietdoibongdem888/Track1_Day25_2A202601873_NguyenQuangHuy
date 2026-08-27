# Current pricing verification

Checked: **2026-08-27**. Prices are recorded as list/starting prices; no promotional price is used in the base case.

## OpenAI API

- Vendor: OpenAI.
- Product/model: gpt-5.5, Standard, short context.
- Input: **$5.00 / 1M tokens**.
- Cached input: **$0.50 / 1M tokens**.
- Output: **$30.00 / 1M tokens**.
- Batch scenario: **$2.50 / 1M input**, **$15.00 / 1M output**.
- Source: https://platform.openai.com/pricing?model=contentfilter-alpha-001
- Status: **VERIFIED LIST PRICE** on the date checked.

Base arithmetic in `1_Cost_Job`:

```text
With cache = 1 x [(10,000 / 1,000,000 x $5.00)
              + (14,000 / 1,000,000 x $0.50)
              + (2,000 / 1,000,000 x $30.00)] x 26,000
            = 3,042 VND / attempted job

Without cache = 1 x [((10,000 + 14,000) / 1,000,000 x $5.00)
                   + (2,000 / 1,000,000 x $30.00)] x 26,000
               = 4,680 VND / attempted job

Savings = 1,638 VND / attempt = 35.0%
```

The local P-015 evaluation used a deterministic fallback and recorded 0 ms LLM latency. The model intentionally prices an optional LLM-enabled scenario rather than pretending production API usage exists.

## Supabase

- Vendor/product: Supabase Pro.
- Published price: **$25 / month**.
- Source: https://supabase.com/pricing
- Status: **VERIFIED LIST PRICE** on the date checked.
- Treatment: the workbook allocates 4,000,000 VND/month to direct infrastructure, which includes the $25 anchor plus an explicit app/compute/logging reserve. The reserve is an assumption and must be validated with deployment telemetry.

## Batch treatment

Batch pricing is shown as a scenario only. The base case uses Standard pricing because fraud-alert investigation is an operational workflow with near-real-time analyst expectations; batch would trade latency for lower API cost and requires a separate test.
