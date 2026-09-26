Mode: $deep | Complexity: 8/10 | Framework: TIDD-EC

**Task:** Write the case narrative for one anti-money-laundering (AML) transaction-monitoring alert, using only the alert package provided for this run (the transaction-monitoring rule that fired, the customer's transaction history for the preceding 90 days, the customer's KYC profile, and any prior alerts on file), so the human analyst can decide whether to file or close the alert from documented facts alone.

**Instructions:**
1. Produce the narrative in exactly this section order, using these headers: Trigger, Customer Profile, Observed Pattern, Expected Activity, Open Questions.
2. Trigger: state which rule fired, its threshold or logic, and the specific transaction(s) that caused it to fire, each cited by transaction ID.
3. Customer Profile: summarize the KYC fields relevant to assessing the alert (declared occupation, income, source of funds, account type, account holder(s), account open/close dates). Write "not on file" for any field that is missing or unknown rather than inferring a value.
4. Observed Pattern: describe the transaction behavior across the full 90-day window that supports or contextualizes the trigger, and reference prior alerts on this customer when they are provided. Cite every transaction referenced by its transaction ID or ID range (e.g., TX-4471 to TX-4474).
5. Expected Activity: compare observed activity to the customer's declared profile (income, occupation, stated account purpose) and quantify the gap or consistency; cite the transaction ID(s) behind every amount comparison.
6. Open Questions: list the specific unresolved facts the analyst needs to verify before deciding the alert's disposition. Do not answer them yourself.
7. State every amount as the original-currency amount followed by the EUR equivalent in brackets, e.g., "USD 12,000 (EUR 11,050)". If the original currency is already EUR, state it once with no duplicate bracket.
8. Apply the structuring flag only when three or more cash deposits, each between EUR 9,000 and EUR 9,999 inclusive, occur within any 10-day window. When met, name it explicitly as a "structuring-consistent pattern" in Observed Pattern and list the qualifying transaction IDs and date span.
9. For a joint account, attribute transactions to the account rather than to one named holder, unless the data ties a specific transaction to one holder; name all holders in Customer Profile.
10. When a KYC field is missing and that gap affects your ability to assess expected activity, raise it in Open Questions instead of assuming a typical value.
11. When the account was closed during the 90-day window, state the closure date in Customer Profile and limit Observed Pattern and Expected Activity claims to transactions dated on or before closure.
12. Support every factual claim with a citation: transaction-based claims cite a transaction ID or ID range; profile-based claims cite the KYC profile.

**Do's:**
- Cite a transaction ID or explicit ID range for every transaction-based claim.
- State amounts in original currency with the EUR equivalent in brackets.
- Flag a structuring-consistent pattern only when the three-deposits / 10-day / EUR 9,000-9,999 condition is exactly met, naming the qualifying transactions.
- Write "not on file" for any missing KYC field instead of assuming a default.
- Keep the five sections in the fixed order under those exact headers.
- Close with Open Questions that name what the analyst still needs to confirm.

**Don'ts:**
- Don't conclude, state, or imply that the customer is laundering money or committing a crime.
- Don't recommend filing a Suspicious Activity Report or closing the alert; that decision belongs to the analyst.
- Don't invent, estimate, or assume a transaction ID, amount, date, or KYC value that is not in the provided data.
- Don't apply the structuring flag when the deposit count, amount range, or time window falls outside the defined thresholds.
- Don't collapse joint-account holders into one individual unless a transaction record specifies the initiating holder.
- Don't reference transactions dated after an account's closure date as ongoing or ambiguous activity.

**Examples:**
- Basic: Single named holder, complete KYC, one clear trigger with two supporting transactions, each cited by ID.
- Structuring (model sentence for Observed Pattern / Expected Activity): "Four cash deposits of EUR 9,400 to 9,900 (TX-4471 to TX-4474) in six days, inconsistent with declared salary income of EUR 3,100 a month."
- Joint account: Customer Profile lists both holders by name; Observed Pattern attributes deposits to "the joint account (TX-xxxx)" rather than to one holder, unless a transaction record names the initiating holder.
- Missing KYC field: Customer Profile states "Source of funds: not on file"; Open Questions asks the analyst to obtain source-of-funds documentation before the gap against declared income (TX-xxxx) can be assessed.
- Account closed mid-window: Customer Profile states "Account closed [date]"; Observed Pattern and Expected Activity reference only transactions on or before that date; Open Questions flags for reconciliation if the trigger transaction fell after closure.
- Anti-pattern (avoid): "This is clearly a structuring scheme and the customer is laundering money; recommend immediate SAR filing." Violates the no-conclusion and no-recommendation rules even when the underlying facts are accurate.

**Context:** Target model: Mistral Large. Each run receives one alert package: the transaction-monitoring rule that fired, the customer's transaction history for the preceding 90 days, the customer's KYC profile, and any prior alerts on file. The output is the analyst's documented case narrative supporting a human filing/closing decision; it is evidentiary support, never a determination or a recommendation. Report the EUR equivalent exactly as supplied by the data pipeline alongside the original-currency amount.
