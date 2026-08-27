# CFO red-team findings

1. **Denominator:** the official Cost/Job output at 1_Cost_Job!B66 divides direct cost by B11 completed autonomous jobs, not by the 3,000 attempts. The 20% autonomy rate is therefore an explicit economic driver.
2. **Containment semantics:** the local controlled eval reports 80.0% commercial package completion (4/5), 20.0% autonomous containment (1/5), 80.0% human review (4/5) and 20.0% grounding failure (1/5). These are not interchangeable.
3. **Retry:** B46 retains an 8% planning estimate until retry telemetry is instrumented; the local evaluator reports retry rate NOT MEASURED.
4. **HITL:** Variant A is explicit. Internal QA is included in vendor COGS; customer escalation and final disposition remain customer-owned.
5. **API math:** the official workbook separates cached input, fresh input and output. Current OpenAI GPT-5.6 Sol pricing is documented in evidence/pricing-sources.md; the local deterministic evaluator did not incur paid tokens.
6. **Infrastructure:** B41 allocates $0.005/attempt for retrieval, vector/embedding, storage, logging and runtime reserve. This is a planning assumption, not a production invoice.
7. **GM and failure threshold:** at $1.75/job, Cost/Job is $0.5422 and GM is 69.0%. Autonomous-containment breakeven is 15.5%; GM falls below 50% at about 12.4% containment. Current 20.0% clears the official usage case, but customer evidence is missing.
8. **GTM:** ARPU is $1,050/month, CAC budget $13,043.88, estimated CAC $12,000, official estimated/budget ratio 0.92x and inverse coverage 1.09x. The $3,000/opportunity input is founder-led planning only, not CRM evidence.
9. **Unverified deployment:** live Kafka/ML/full-stack deployment, production security controls, retention/deletion, vendor terms and procurement evidence remain partial or open. No production claim is made.
