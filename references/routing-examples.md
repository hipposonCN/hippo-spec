# Routing acceptance examples

Use these examples to validate or disambiguate the root decision. They are examples of the routing contract, not another task ledger or behavior specification.

| # | Input | Expected result | Decisive rule |
|---|---|---|---|
| 1 | Correct wording in one documentation file with a Markdown check | `skip` | Clear, local, reversible, and one feedback loop; a mechanical edit does not escalate. |
| 2 | Implement the next vertical slice under an existing change with the same intent | `continue` | Inherit `active_change`, `scope_lock`, `current_slice`, and acceptance evidence; do not recreate artifacts. |
| 3 | Repair a production defect in an already frozen contract | `repair` | Reproduce, reduce to the smallest loop, add a regression test, apply the minimum fix, and verify the original symptom. |
| 4 | Execute a cross-repository release already covered by a frozen contract and active change | `continue`, not `full:new` | Repository and release risk add acceptance evidence but do not create new behavior intent. |
| 5 | Add a previously unrecorded public permission or persistence contract that needs cross-session coordination | `full:new` | Both creation gates are satisfied: a new durable authority decision and cross-session coordination. |
| 6 | Perform the final review of a pinned PR or fixed `HEAD` | `review-only` | Consume the existing spec and fixed code; do not write planning artifacts. |
| 7 | A fixed-scope review returns only unsupported suggestions or subjective code smells | Non-blocking; keep `review-only` and do not repeat the review | Only reproducible failure, cited missing specified behavior, or cited repository-rule violation blocks. |
| 8 | An executor receives an existing `Hippo Spec Context` | No route selection; execute the inherited `current_slice` | Only the root decides once. Executors do not call Hippo Spec or enlarge `scope_lock`. |

A simple conversational review or status query remains `skip`. `review-only` is reserved for consuming an existing specification and a deliberately fixed code point as a formal review boundary.
