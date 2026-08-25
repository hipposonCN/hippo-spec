---
name: hippo-spec
description: Assess and orchestrate substantial software work by choosing no spec, lightweight exploration, or a full OpenSpec lifecycle, then adding domain modeling, vertical-slice TDD, diagnosis, and two-axis review only when useful. Use for multi-session initiatives, cross-module or cross-repo changes, migrations, new domain behavior, risky releases, or when the user asks whether a project needs a spec. Do not use for ordinary small fixes, simple answers, or status checks.
---

# Hippo Spec

Use the minimum process that makes the work safer and easier to finish. OpenSpec remains the durable behavior and change ledger; engineering methods improve how the change is discovered, implemented, and verified.

## Start with a read-only fit check

Inspect the request and readily available project evidence before creating planning files. Reuse an existing change when it has the same intent.

Choose one lane:

- **skip**: The outcome is clear, local, reversible, and realistically finishable in one focused session with one feedback loop.
- **light**: The work has meaningful uncertainty, touches several modules, or may outgrow one session, but does not yet justify durable change artifacts. Explore and settle the important branches without creating a change.
- **full**: Use when any hard trigger exists: work spans repositories, runtimes, or owners; changes persistent data or a public contract; includes migration, release, security, permissions, money, or irreversible external state; needs multiple sessions or independently accepted milestones; or requires several distinct proofs before it can truthfully be called complete. Also use full when two or more light signals remain after a brief inspection.

When explicitly invoked, report `Hippo Spec: skip|light|full — <short reason>`. When selected implicitly, say nothing for `skip`; for `light` or `full`, state the lane and reason before proceeding. Ask a question only when a missing decision materially changes the lane or solution.

## Keep each artifact authoritative

- Main OpenSpec specs describe agreed current behavior.
- One selected OpenSpec change describes the intended delta. Do not create a parallel spec in an issue, plan, or chat summary.
- `CONTEXT.md` is a glossary, not a behavior spec. Add terms only when a real ambiguity has been resolved.
- ADRs explain hard-to-reverse, surprising trade-offs. Do not use them as task lists.
- Tasks describe independently verifiable implementation slices.
- Tests, receipts, release identity, and fresh readback prove implementation or activation. OpenSpec validation and checked boxes alone do not.

If artifacts, source, and live behavior disagree, surface the divergence. Do not silently rewrite one to match another or claim a later completion state.

## Run the selected lane

### Skip

Make the smallest coherent change, run the narrow relevant check, and stop. Do not initialize OpenSpec or create planning documents.

### Light

Explore in conversation, or use the project's OpenSpec explore capability when already installed. Resolve only decisions that branch the outcome: user value, scope, key terms, constraints, and acceptance evidence. Promote to `full` if a hard trigger appears; otherwise proceed without durable artifacts.

### Full

Read [references/full-lifecycle.md](references/full-lifecycle.md). Use the project's installed OpenSpec workflow and schema rather than hand-inventing artifact shapes. If OpenSpec is absent, explain why full planning is warranted and ask before initializing or adding its project files.

During clarification, implementation, debugging, or review, read only the relevant part of [references/engineering-discipline.md](references/engineering-discipline.md).

## Preserve real completion gates

Discover the project's own completion chain before implementation. A typical chain may include source change, targeted tests, full validation, package or release creation, process activation, and fresh receipt/readback. Keep these states separate.

Mark an OpenSpec task complete only after its stated behavior and evidence exist. Verify the complete change against specs and project checks before syncing or archiving. Never bulk-archive merely because every checkbox is marked.
