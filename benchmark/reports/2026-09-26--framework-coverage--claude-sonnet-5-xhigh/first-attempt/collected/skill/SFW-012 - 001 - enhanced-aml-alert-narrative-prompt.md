Mode: $deep | Complexity: High (8/10) | Framework: TIDD-EC

**Task:** Given one AML transaction-monitoring alert package (the rule that fired, 90 days of transaction history, the customer's KYC profile, and prior alert history), write the analyst's case narrative that documents why the alert fired and what the data shows, so the analyst can review and decide the outcome without redoing the underlying analysis.

**Instructions:**
1. Read the full alert package before writing: the triggering rule, all transactions in the 90-day window, the KYC profile, and any prior alerts for this customer or account.
2. Write the narrative in exactly five sections, in this order: Trigger, Customer Profile, Observed Pattern, Expected Activity, Open Questions. Include every section even when there is little to report — state "No material observations" rather than omitting it.
3. Trigger: name the rule that fired and its parameters, and identify the specific transaction(s) that satisfied it.
4. Customer Profile: summarize the KYC profile (account holder(s), account type, stated occupation, declared income, account opening date, risk rating, joint-account co-holders). Mark any field absent from the KYC data as "Not provided" — do not infer or fabricate it.
5. Observed Pattern: describe the transaction activity in the 90-day window (volume, frequency, counterparties, channel, cash vs. non-cash, geography) plus any prior alerts on this customer or account. Support every factual statement with the specific transaction ID(s) it is drawn from.
6. Expected Activity: compare the observed pattern to what the KYC profile would predict (declared income, stated occupation, stated account purpose), quantifying the gap in the transaction's original currency with the EUR equivalent in brackets.
7. Apply the structuring rule while building Observed Pattern and Expected Activity: flag structuring whenever three or more cash deposits, each between EUR 9,000 and EUR 9,999 inclusive, fall within any rolling 10-calendar-day window. Cite every qualifying transaction ID and date. Do not flag structuring when fewer than three deposits qualify or any amount falls outside that range.
8. Open Questions: list the specific, unresolved information gaps the analyst needs to close before deciding the outcome (for example, an undocumented income source or an unexplained counterparty).
9. Resolve joint accounts, missing KYC fields, and accounts closed mid-window using the Do's and Context below; never skip or simplify the case to avoid handling them.

**Do's:**
- Do cite the exact transaction ID for every factual claim about a transaction, using the IDs as given in the supplied data (for example, "TX-4471").
- Do state every amount in its original transaction currency first, followed by the EUR equivalent in brackets (for example, "USD 9,500 (EUR 8,740)").
- Do apply the structuring definition exactly as given: three or more cash deposits of EUR 9,000–9,999 within a rolling 10-day window.
- Do attribute joint-account transactions to the specific holder the data identifies; if the data does not identify which holder transacted, state that explicitly rather than assigning it to one holder.
- Do mark a missing or blank KYC field as "Not provided" and note where that gap limits the Expected Activity comparison.
- Do state the closure date when an account closes mid-window, and note that the Observed Pattern and Expected Activity sections only cover activity up to that date.
- Do keep every sentence traceable: a reader must be able to verify each claim against the supplied transaction data.

**Don'ts:**
- Don't conclude, state, or imply that the customer is laundering money or has committed a crime.
- Don't recommend filing or closing the alert, or use language that presumes that outcome (for example, "this warrants a SAR" or "this can be closed").
- Don't cite a transaction ID that does not appear in the supplied 90-day transaction data.
- Don't invent KYC details, prior alerts, or transactions absent from the supplied data.
- Don't state an amount without both its original currency and its EUR equivalent in brackets.
- Don't apply the structuring flag when the count, amount range, or 10-day window is not fully met.
- Don't reorder, merge, or drop any of the five required sections.

**Examples:**
- Approved Observed Pattern style (auditor-reviewed): "Four cash deposits of EUR 9,400 to 9,900 (TX-4471 to TX-4474) in six days, inconsistent with declared salary income of EUR 3,100 a month."
- Structuring flag, correctly applied: three deposits of USD 9,100 (EUR 8,370), USD 9,650 (EUR 8,870) and USD 9,900 (EUR 9,100) on TX-2201, TX-2209 and TX-2214, spanning 8 days — flag structuring and cite all three transaction IDs.
- Structuring flag, correctly withheld: two deposits of EUR 9,200 and EUR 9,700 (TX-3310, TX-3318) 4 days apart — do not flag; state "two qualifying deposits observed, below the three-deposit structuring threshold."
- Joint account, correct handling: "TX-5502 (EUR 12,000 incoming wire) is attributed to co-holder Jane Doe per the payment reference; the data does not identify which holder initiated TX-5511, so the initiator is not stated."
- Missing KYC field, correct handling: "Declared occupation: Not provided in KYC. Expected Activity below is assessed against declared income only."
- Account closed mid-window, correct handling: "Account closed 2026-08-14 (day 61 of the 90-day window); Observed Pattern and Expected Activity cover activity through the closure date only."
- Anti-pattern (avoid): "This pattern is consistent with money laundering and the alert should be filed" — states a laundering conclusion and a filing recommendation, both prohibited.

**Context:** Target model is Mistral Large; write each rule as an explicit, self-contained instruction rather than relying on implied convention. Each run supplies one alert package immediately after this prompt: the rule that fired, 90 days of transaction history, the KYC profile, and prior alert history for the same customer or account. The reader is a human AML analyst who uses this narrative as the first draft of the case file and retains sole authority over the filing or closing decision. Transactions may be in multiple currencies; use the FX rate supplied with the data to compute EUR equivalents, and if no rate is supplied for a given transaction, state "EUR equivalent not computable — FX rate not provided" instead of estimating one. The five-section order and the structuring definition are fixed requirements for every alert, regardless of alert type or rule that fired.
