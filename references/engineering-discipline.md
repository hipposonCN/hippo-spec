# Engineering discipline

Read only the section needed for the current stage. These methods adapt the complementary parts of Matt Pocock's engineering skills while leaving OpenSpec as the specification authority.

## Clarification

Ask only questions whose answers change scope, architecture, ownership, or acceptance. Prefer one decision at a time and lead with the current recommendation. Stop once the material branches are resolved; do not turn a clear request into an interview ritual.

## Domain modeling

Sharpen overloaded terms against code and current specs. Record a resolved term in `CONTEXT.md` only when the shared vocabulary will be reused. Keep implementation details and requirements out of the glossary.

Offer an ADR only when the decision is simultaneously hard to reverse, surprising without its rationale, and the result of a real trade-off.

## Vertical-slice TDD

Name the public seam that exposes the behavior. For each slice:

1. Add one test that fails on the missing behavior.
2. Add the smallest implementation that makes it pass.
3. Run the narrow test and relevant static checks.
4. Continue with the next independently observable behavior.

Test through public behavior rather than private structure. Skip test-first ceremony for documentation-only or mechanically verifiable changes, but still run an appropriate check.

## Hard-bug diagnosis

Before forming a confident root-cause theory, create a fast, deterministic loop that can reproduce the user's exact symptom. Minimize the case, then test a small ranked set of falsifiable hypotheses one variable at a time. Turn the minimal reproduction into a regression test at the correct seam before fixing when such a seam exists. Remove temporary instrumentation and rerun the original loop after the fix.

## Two-axis review

Review the final diff against two separate questions:

- **Spec**: Is every requested requirement present and correct, with no silent scope reduction or unrequested behavior?
- **Standards**: Does the change follow repository rules and avoid needless duplication, speculative abstraction, shallow pass-through modules, and scattered ownership?

Keep the findings separate so a clean implementation cannot hide a wrong product result, and correct behavior cannot hide a maintainability regression. Use subagents only when explicitly authorized and when independent review materially improves confidence.

## Routing boundaries

- Do not use a second generic `to-spec` or `to-tickets` flow once OpenSpec owns the change.
- Do not treat a commit, passing tests, or an OpenSpec checkbox as live completion when activation or receipts remain.
- In governed research systems, route domain research through the project-owned research and admission path; do not substitute a generic background Markdown research task.

Method sources: [Matt Pocock Skills](https://github.com/mattpocock/skills), especially its domain-modeling, TDD, diagnosing-bugs, and code-review skills. The lifecycle and completion rules here are Hippo-specific adaptations.
