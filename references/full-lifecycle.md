# Persistent specification routes

Use this reference only after the root selected `full:new` or `continue`. Do not route again here.

## Prefer continuation

Inspect existing OpenSpec changes and main specs before creating anything. Select `continue` whenever one change already owns the same intent, even if the current slice is cross-repository, security-sensitive, a migration, a release, or needs several validations.

For `continue`:

- bind `active_change` to the exact existing change;
- preserve its scope and normative behavior;
- set `current_slice` to the next incomplete, independently verifiable slice;
- carry forward the exact acceptance evidence already required, adding release/readback proof when the slice needs it;
- read the change through the project's installed OpenSpec status/instruction surface;
- do not regenerate proposal, design, specs, or the task tree.

If implementation exposes a genuinely different intent or an unrecorded public behavior decision, stop and return it to the root or user. Do not recursively call Hippo Spec or silently widen the current change.

## Create only when the gate is complete

Select `full:new` only when both conditions hold:

1. the request introduces new, unrecorded persistent behavior, a public contract, permission, or ownership decision; and
2. coordinating that decision and its implementation requires more than one session.

Risk, repository count, deployment, release, migration, or validation count does not satisfy condition 1 by itself.

When `full:new` is selected, use the project's installed OpenSpec workflow and schema to create the minimum coherent change. OpenSpec owns the behavior delta and tasks. GitHub issues may reference the change and assign work, but must not restate requirements or become a parallel task authority. If the project has no OpenSpec installation, request authorization before initializing it; do not substitute another specification system.

Once the change exists, emit a `Hippo Spec Context` with that exact `active_change`. Every later slice uses `continue` without another lifecycle assessment.

## Preserve the three truths

- **Artifact truth** proves the authoritative specification is present, current, and structurally valid.
- **Implementation truth** proves the scoped behavior exists and focused tests or checks pass.
- **Operational truth** proves the intended package, release, process, external state, receipt, or fresh readback is active when the specification requires it.

High-risk execution affects `acceptance_evidence`; it does not create a new lifecycle. Keep source, commit, PR, merge, release, activation, and readback as separate states when the project distinguishes them.

## Finish the active change

Mark a task complete only when its specified behavior and evidence exist. Run one final fixed-scope review when required, then verify only cited blockers after repairs. Sync or archive through the installed OpenSpec workflow only after all applicable truth layers pass. Follow-up work with a different intent returns to the root as a separate decision.
