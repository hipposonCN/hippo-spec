# Full Hippo Spec lifecycle

Use this only for the `full` lane.

## 1. Locate the planning truth

Read the repository instructions, current specs, active changes, project validation commands, and release or runtime boundaries that affect the request. Use OpenSpec status and instruction output when available instead of guessing paths or required artifacts.

Before creating anything, compare the request with active changes:

- Reuse and update a change when the intent and acceptance target are the same.
- Start a new change when the intent differs, the old change can finish independently, or combining them would create unrelated acceptance paths.
- For a multi-month program, prefer several independently verifiable and archivable changes over one permanent mega-change. Keep an umbrella map only in an existing project planning surface when coordination actually needs one.

## 2. Reach agreement before implementation

Capture only information that changes implementation or acceptance:

- the user-visible problem and intended outcome;
- actors and ownership boundaries;
- current behavior and the intended delta;
- explicit non-goals;
- risky or hard-to-reverse decisions;
- the evidence required to call each milestone complete.

Use the repository's OpenSpec schema and generated instructions. In the usual spec-driven schema:

- proposal records why, scope, and impact;
- delta specs record normative behavior and scenarios;
- design records technical boundaries and consequential decisions;
- tasks are dependency-ordered vertical slices with observable acceptance.

Do not duplicate these artifacts in GitHub issues. Issues may link to the change and track ownership, but OpenSpec remains the behavior authority.

## 3. Implement in verified slices

Work one narrow end-to-end slice at a time. Prefer an existing public seam; create a new seam only when it removes a concrete testability or ownership constraint. Update artifacts when implementation reveals that an agreed assumption is wrong. Do not quietly narrow scope or mark deferred work complete.

Use the relevant method in `engineering-discipline.md`:

- domain modeling when terminology or ownership changes;
- vertical-slice TDD for observable behavior;
- the diagnosis loop for a hard defect;
- two-axis review before final acceptance.

## 4. Verify three different truths

Keep these checks distinct:

1. **Artifact truth**: OpenSpec artifacts are structurally valid and internally coherent.
2. **Implementation truth**: code and tests satisfy every requirement and scenario in scope.
3. **Operational truth**: the intended package, release, process, external state, or receipt is actually active and freshly readable when the project requires it.

Run the project's narrow checks during each slice and its full required gate at the end. OpenSpec validation does not replace tests or operational proof.

## 5. Close without sediment

Before archive:

- every checked task has evidence;
- implementation has been reviewed against both the change and repository standards;
- required runtime or external acceptance is complete;
- delta specs are reconciled with current specs using the installed OpenSpec workflow;
- remaining follow-up work has a separate intent and change.

Archive promptly once these conditions hold. If many completed changes have accumulated, audit them individually before using any bulk-archive capability.
