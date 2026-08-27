# CFO red-team findings

1. **Denominator:** corrected to completed grounded packages (`C8`), not attempts (`C6`). The incorrect attempted denominator understates Cost/Job by 20.0% in the base case.
2. **Retry:** 8% is an explicit estimate and produces 730,080 VND/month; it is not silently zero.
3. **HITL:** Variant A is explicit. Internal QA costs 3,000,000 VND/month; customer escalation labor is disclosed as 70,000,000 VND/month but excluded from our COGS because the customer owns escalation handling.
4. **API math:** fresh input, cached input and output are separated; cache savings are 1,638 VND/attempt or 35.0%. Batch prices are scenario-only.
5. **Infrastructure:** 4,000,000 VND/month is a conservative allocation with a Supabase Pro anchor and an explicit app/compute/logging reserve; not a measured production invoice.
6. **GM:** blended GM is 82.8%, below the 85% missing-cost trigger. Usage GM is 76.1%. The five-case controlled eval produces commercial package completion of 80%, autonomous containment of 20%, human-review/escalation of 80% and grounding failure of 20%; a 2x adverse package-completion error to 40% lowers usage GM to 56.1%, so the model does not celebrate an artificially tiny cost.
7. **Vendor/API data costs:** no paid external fraud-data API was found in the current P-015 evidence chain; this absence is not proof that a customer deployment will have none. The pilot must capture all paid APIs and data-access charges.
8. **Unverified deployment:** live Kafka/ML/full-stack deployment is not claimed; infrastructure and observability remain partially unverified. The controlled eval is reproducible but remains local and synthetic, not a customer pilot.
