# Engineering methods

Use only the section needed for the current work. All methods are bundled; no external skill, template, or second spec/ticket workflow is needed.

- **[Diagnosis](diagnosing-bugs.md):** read for hard-to-localize bugs, intermittent failures, or performance regressions. A routine fix with a known cause needs only the focused repair loop below.
- **[Domain modeling](domain-modeling.md):** read when defining or changing domain terms, entity relationships, or responsibility boundaries. Merely reading familiar terminology does not trigger modeling.

Pass the current outcome, scope, and authorization into the method. It cannot widen the assignment, turn read-only diagnosis into repair, or start a competing spec/task lifecycle. Use existing authorization for settled decisions; surface only material unresolved conflicts.

## Explore and model

Investigate the unresolved decision that changes the outcome. Prefer repository evidence before asking the user. Separate the required behavior from a tentative design; use a small disposable experiment when it resolves uncertainty cheaply.

Reuse the project's domain language. Keep glossary and decision rationale separate from behavior requirements. Continue already-authorized implementation once the decision is settled. A consultation-only request ends with the answer.

## Implement and repair

Work through one observable slice at a time. Prefer existing public interfaces and test seams. For behavior changes and regressions, demonstrate the missing or broken behavior before the fix, then add the minimum implementation and verify it. Test externally visible outcomes, not private structure or assertions that mirror the implementation.

Keep refactoring limited to a concrete constraint on the slice. Run focused checks during iteration and required integration/static checks at the appropriate boundary. Documentation and mechanical edits need their relevant checks, not artificial red tests. Do not rerun unchanged broad checks without a new failure, change, or unresolved concern.

## Review

Pin the reviewed diff and inspect both requested behavior and repository rules. Use independent review when the change or repository warrants it, not as a mandatory agent count.

A blocking finding needs an actionable defect with a concrete trigger and code/evidence trace, a failed check, or a cited requirement/rule violation. A runnable test is useful but not the only valid evidence of a defect. Subjective smells, speculative risks, and unsolicited redesigns are non-blocking.

After fixes, rerun affected checks and revisit affected findings. Broaden review only if the repair changes other relevant behavior or invalidates previous evidence. Do not repeat open-ended review until no model suggests improvements, and do not stop with a known substantive defect merely because one review has run.

Method provenance is recorded in [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md). Source links are attribution, not runtime inputs or additional completion authorities.
