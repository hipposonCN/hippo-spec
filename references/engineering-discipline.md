# Optional engineering discipline

Read only the section that matches the current stage in the inherited `Hippo Spec Context`. These methods adapt complementary parts of Matt Pocock's engineering skills without making them a runtime dependency or a second specification, ticket, lifecycle, or completion authority.

If a named method skill is installed, it may help execute that stage. If it is absent, use the compact fallback below and continue.

## Light exploration

Use this only when the root selected `light`. Identify the single unresolved product, behavior, permission, or ownership decision that changes the outcome. Inspect enough evidence to recommend and settle that decision, report it, and stop. Do not create a persistent change, speculative task tree, implementation plan, or parallel specification; later implementation is a separate root request.

## Domain modeling

Use `domain-modeling` only when shared terminology, permission meaning, or ownership boundaries remain ambiguous in the current stage.

Fallback:

1. Compare the overloaded term with current code and the authoritative spec.
2. State the actor, responsibility, invariant, and boundary in plain language.
3. Record a resolved term in `CONTEXT.md` only when the project already uses it and the vocabulary will be reused.

Keep requirements and implementation details out of the glossary. Offer an ADR only when a decision is hard to reverse, surprising without its rationale, and the result of a real trade-off; it must not duplicate OpenSpec behavior.

## Implementation with TDD

Use `tdd` only while implementing an observable behavior slice. Documentation-only and mechanically verifiable changes do not require test-first ceremony.

Fallback:

1. Name the existing public seam that exposes the behavior.
2. Add one focused test that fails for the missing behavior.
3. Add the smallest implementation that makes it pass.
4. Run the narrow test and relevant static check.
5. Stop when the inherited `current_slice` and acceptance evidence pass.

Test public behavior rather than private structure. Do not create a new seam unless it removes a concrete testability or ownership constraint.

## Repairing frozen behavior

Use `diagnosing-bugs` only for the `repair` lane or a defect discovered inside an already selected implementation slice.

Fallback, in this order:

1. Reproduce the original symptom deterministically.
2. Reduce it to the smallest fast feedback loop.
3. Add a regression test at the correct public seam.
4. Apply the minimum repair without changing the frozen contract.
5. Rerun the regression test and verify the original symptom.

Test a small ranked set of falsifiable hypotheses one variable at a time. Remove temporary instrumentation. A bug under frozen behavior does not justify a new proposal, design, spec, or task tree.

## Review-only and final review

Use `code-review` only for a fixed PR, commit range, diff, or `HEAD`, or for the one final review required by an active change. Pin the reviewed point, consume the existing specification and repository rules, and keep the two axes separate:

- **Behavior axis**: the fixed implementation satisfies every cited requirement in scope.
- **Repository axis**: the fixed implementation follows explicit repository rules.

Run this review once. A finding blocks only when it contains at least one of:

1. a reproducible test failure with the command and observed failure;
2. a missing behavior with an explicit citation to the authoritative specification;
3. a violation with an explicit citation to a repository rule.

Unsupported suggestions, subjective code smells, style preferences not grounded in a rule, and speculative future risks are non-blocking. After a blocking finding is repaired, rerun only its cited test or evidence check; do not repeat open-ended review until a model produces no suggestions. Review-only work must not create or modify planning artifacts.

## Routing and completion boundaries

- In an OpenSpec project, do not default to Matt's `to-spec`, `to-tickets`, or full `implement` chain.
- Invoke `domain-modeling`, `tdd`, `diagnosing-bugs`, or `code-review` only for its matching stage and only when installed.
- Do not install a method skill, add a dependency, or stop execution merely because an optional method is absent.
- Do not reroute, change `active_change`, or expand `scope_lock`; return a material conflict to the root task or user.
- Keep artifact truth, implementation truth, and operational truth separate. A commit, passing test, review, or OpenSpec checkbox does not prove activation or fresh readback.

Method source: [Matt Pocock Skills](https://github.com/mattpocock/skills). The routing, authority, and completion boundaries are Hippo-specific adaptations.
