---
name: hippo-spec
description: Continuation-first router that decides once whether software work needs persistent specification, then selects skip, light, full:new, continue, repair, or review-only and passes a fixed Hippo Spec Context to execution. Use when starting or resuming substantive work, repairing frozen behavior, or reviewing a fixed PR/diff. Do not use for status queries, simple reviews, or mechanical edits unless explicitly invoked.
---

# Hippo Spec

Act as a thin root router. Decide the lifecycle once, hand execution a fixed context, and stop routing. Do not restart a lifecycle merely because later work is cross-repository, security-sensitive, release-related, or has several validation layers.

## Authority

- In a project that uses OpenSpec, its main specs and selected change are the sole behavior authority. Issues may link work or ownership but must not duplicate the spec or task tree.
- Matt Pocock skills are optional engineering methods, not a specification, ticket, lifecycle, or completion authority.
- Artifact truth, implementation truth, and operational truth are distinct. A valid spec, passing code, and an active release/readback prove different states.

## Route once at the root

If a `Hippo Spec Context` is already present, accept it and execute its `current_slice`. Do not invoke Hippo Spec again, reconsider the lane, recreate planning artifacts, or expand `scope_lock`. Return a material scope conflict to the root task or user.

Otherwise inspect the request and existing project artifacts without writing, then choose exactly once in this order:

1. **review-only** — a final review of a fixed PR, commit range, diff, or `HEAD`; consume the existing spec and fixed code only.
2. **repair** — a defect or regression under already frozen behavior.
3. **continue** — an OpenSpec change with the same intent already exists. This is the default for its next slice, including release and cross-repository work.
4. **full:new** — only when both are true: the request introduces new, unrecorded persistent behavior, a public contract, permission, or ownership decision; and the work needs cross-session coordination.
5. **light** — a key product, behavior, permission, or ownership decision is still unresolved and short exploration can settle it; create no persistent change.
6. **skip** — clear, local, reversible work that fits one feedback loop. Status queries, simple reviews, and mechanical edits stay here and never escalate by risk vocabulary alone.

Cross-repository scope, security, release work, migrations, or multiple validations alone do not trigger `full:new`. When the same intent is already specified, keep `continue` and add those proofs to `acceptance_evidence`.

When explicitly invoked, report `Hippo Spec: <lane> — <short reason>`. When selected implicitly, keep `skip` silent; announce any other lane once.

## Emit the handoff context

After routing, provide one compact context and pass it unchanged to every executor:

```yaml
hippo_spec_context:
  lane: skip | light | full:new | continue | repair | review-only
  active_change: <exact change/spec id or none>
  scope_lock: <authorized files, systems, and explicit exclusions>
  current_slice: <single immediate objective>
  acceptance_evidence: <checks and readbacks required for this slice>
```

Child tasks and later executors inherit this context. They must not call Hippo Spec, select another lane, or enlarge scope. A new intent requires a separate root decision rather than recursive routing.

## Execute the lane

- **skip**: make the smallest change, run the single relevant feedback loop, and stop. Create no planning artifact.
- **light**: explore only the unresolved decision, report the result, and stop. Create no persistent change or implementation plan; any later implementation starts as a separate root request.
- **full:new**: use the project's installed OpenSpec workflow and schema. If OpenSpec is absent, ask before initialization; never invent a parallel authority. Read [references/full-lifecycle.md](references/full-lifecycle.md).
- **continue**: load the exact existing change and continue `current_slice`. Inherit `active_change`, `scope_lock`, and acceptance evidence; do not recreate proposal, design, specs, or the task tree. Read [references/full-lifecycle.md](references/full-lifecycle.md).
- **repair**: reproduce the frozen-behavior defect, build the smallest feedback loop, add a regression test at the correct seam, apply the minimum fix, and verify the original symptom. Do not start a new lifecycle for the bug.
- **review-only**: pin the fixed point, review once against the existing spec and repository rules, and do not create or modify planning artifacts.

Read only the relevant section of [references/engineering-discipline.md](references/engineering-discipline.md). Use [references/routing-examples.md](references/routing-examples.md) only when classification is ambiguous or this Skill is being validated.

## Optional engineering methods

In OpenSpec projects, do not default to Matt's `to-spec`, `to-tickets`, or full `implement` chain. Invoke `diagnosing-bugs`, `tdd`, `domain-modeling`, or `code-review` only for its matching stage and only when installed. There is no runtime dependency on Matt skills; use the compact fallback in `engineering-discipline.md` when absent.

Review findings block only when backed by a reproducible test failure, an explicitly cited missing specified behavior, or an explicitly cited repository-rule violation. Unsupported suggestions and subjective code smells are non-blocking. Run the final two-axis review once; after a fix, recheck only the cited evidence rather than repeating open-ended review until no suggestions remain.

## Completion boundary

Discover which truth layers the slice requires:

- **artifact truth**: the authoritative spec/change is present, current, and valid;
- **implementation truth**: the required behavior exists and its focused checks pass;
- **operational truth**: the intended release, process, external state, receipt, or fresh readback is active when applicable.

Call the root task complete only when every applicable layer has its stated evidence. A commit, PR, merge, checked task, or passing test does not substitute for release/readback evidence when operational truth is in scope.
