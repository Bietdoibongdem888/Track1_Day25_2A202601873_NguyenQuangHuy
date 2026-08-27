# Current pricing verification

Checked: **2026-08-27**. These are current public list/planning references; no promotional price is used in the base case.

## OpenAI API

- Vendor/model: OpenAI GPT-5.6 Sol, Standard, short context.
- Standard input: **$4.00 / 1M tokens**.
- Cached input: **$0.40 / 1M tokens**.
- Cache writes: **$5.00 / 1M tokens**.
- Output: **$20.00 / 1M tokens**.
- Batch scenario: **$2.00 / 1M input**, **$0.20 / 1M cached input**, **$2.50 / 1M cache writes**, **$10.00 / 1M output**.
- Promotional pricing is shown by the vendor as available at least through 2026-11-21; it is not used in this base case.
- Source: https://developers.openai.com/api/docs/pricing
- Status: **VERIFIED FIRST-PARTY PRICE PAGE** on the date checked.

Official workbook arithmetic uses 6 turns/job, 3,000 cached tokens/turn, 1,000 fresh tokens/turn and 300 output tokens/turn:

- Cache-enabled LLM cost: **$0.081/job**.
- Non-cache comparison: **$0.132/job**.
- Cache savings: **38.6%**.

The local P-015 evaluation used a deterministic fallback and recorded no paid LLM tokens; the model intentionally prices an optional LLM-enabled scenario rather than pretending production API usage exists.

## FX planning reference

- USD/VND mid-market reference checked 2026-08-27: **1 USD = 26,095.90 VND**.
- Source: https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=VND
- Workbook input: 1_Cost_Job!B68 = 26095.90.
- Treatment: planning conversion only; customer contract currency is not claimed.

## Adjacent outcome/resolution benchmarks

- Intercom Fin: **$0.99 per resolution/outcome**, one outcome per conversation; default escalations/failures are not charged. Source: https://www.intercom.com/help/en/articles/8205718-fin-ai-agent-outcomes
- Zendesk AI agents: **as low as $1.50 per resolution**. Source: https://www.zendesk.com/service/ai/top-ai-agents/
- These are adjacent benchmarks, not identical to P-015's human-gated investigation package. They support a bounded usage anchor but do not prove a customer willingness-to-pay price.

## Infrastructure context

- Supabase Pro published reference: **$25/month**. Source: https://supabase.com/pricing
- The official workbook does not claim a production Supabase bill. Its input allocates **$0.005/attempt** for retrieval, embedding/vector DB, storage, logging and app/runtime reserve; this is a planning assumption pending deployment telemetry.

## Pricing decision

The official workbook selects **$1.75/job** for the pure usage case: above the 3x Cost/Job floor, within the labor/value guardrails and bounded by adjacent outcome/resolution references. Hybrid remains the commercial recommendation while P-015's current autonomy and attribution evidence are limited.
