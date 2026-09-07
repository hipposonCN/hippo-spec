---
name: hippo-spec
description: Deliver bounded software changes using current specs, short feedback loops, and evidence-based closeout. Use when implementing, repairing, resuming, or reviewing substantive project work; keep routine edits lightweight.
---

# Hippo Spec

Carry the user's requested outcome through implementation and applicable closeout. Keep the scope bounded, let evidence refine the approach, and use the least process that preserves correctness.

## Establish the working boundary

Infer the requested result, authorized scope, and completion evidence from the conversation and relevant project artifacts. Ask only for a missing decision that materially changes the outcome or authorization. Diagnosis, a verified patch, and an activated release are different deliverables.

Use one behavior and task authority: OpenSpec where the project uses it; otherwise the project's existing spec, documentation, or issue convention. Do not initialize a framework or create a second ledger merely to use this skill. A historical plan does not authorize work or override the user's current request. Code and runtime evidence describe what exists, not what the user intended.

Reuse a change only when it is still effective, not superseded, and its remaining work matches this request. Inspect the relevant authority and revision; do not audit the entire historical backlog on every task. Read [references/full-lifecycle.md](references/full-lifecycle.md) when selecting, updating, or closing a persistent record.

## Choose the smallest working mode

| Mode | Use it for | Action |
|---|---|---|
| `review-only` | Review of a fixed PR, commit range, or diff | Inspect the fixed work; do not implement or edit planning artifacts. |
| `repair` | A defect under an existing behavior contract | Reproduce, minimally repair, and verify the original symptom. |
| `continue` | Remaining authorized work in an effective change | Execute the next independently verifiable slice; update the same record. |
| `full:new` | An unrecorded durable behavior, public contract, permission, or ownership delta | Update a suitable record, or create the minimum change required by the project; then continue. |
| `light` | A question or material decision needs investigation | Investigate and answer; continue implementation only if already authorized. |
| `skip` | Clear local work with no behavior-contract delta | Make the change and run the relevant check; create no planning artifact. |

Behavior changes determine whether a spec needs updating, even within one session. Session count determines handoff needs. Cross-repository work, release, security, and multiple checks alone do not require a new change.

These modes describe work, not locked phases. Do not repeat planning on routine stage transitions or handoffs. Announce the initial mode briefly when explicitly invoked; keep routine implicit routing internal.

## Refine the approach without growing the assignment

- Distinguish required outcomes from design assumptions. Evidence may revise an assumption or task sequence in place; record the material reason without regenerating the whole proposal or task tree.
- Preserve authorized behavior, acceptance criteria, permissions, and explicit exclusions. Do not weaken a requirement to fit passing code. A material conflict returns to the root or user; continue independent authorized work meanwhile.
- Prefer one thin, observable slice through the necessary layers. Change an adjacent module only when required for that slice. Respect explicit file allowlists; otherwise a newly discovered relevant file is not itself a reason to restart planning.
- Keep unrelated improvements outside this change. Do not append speculative features or tickets. Continue the slices needed for the requested outcome, then stop; finishing one slice does not finish an explicitly requested larger deliverable.

Use short behavior-level feedback loops and proportional review. For hard diagnosis or domain-model changes, select the matching installed Matt Pocock method through [references/engineering-discipline.md](references/engineering-discipline.md). Use its fallback when absent; preserve this assignment's scope, authorization, and single behavior authority.

## Hand off the same assignment

Only when crossing an executor or session boundary, pass:

```yaml
hippo_spec_context:
  lane: skip | light | continue | repair | review-only
  active_change: <effective spec/change/task reference and revision, or none>
  scope_lock: <authorized systems, explicit exclusions and any file allowlist>
  current_slice: <immediate objective and its place in the requested outcome>
  acceptance_evidence: <required checks/readbacks and evidence already obtained>
```

`full:new` records the delta at the root, then becomes `continue`. Recipients inherit the assignment rather than replan it. Recheck the selected authority's validity on resumption; return material conflicts to the root. A mode transition never grants more scope or permission.

## Close the requested outcome

Verify only the applicable layers:

- **Artifact:** the relevant behavior record reflects the authorized change and remains valid.
- **Implementation:** the requested behavior and focused checks pass.
- **Operation:** the intended release, process, external receipt, or fresh readback is active when requested.

Update the selected task and synchronize/close its record as applicable, within authorization. A verified slice may finish while its parent change remains open. Distinguish completed, blocked, and superseded work; never mark unfinished work done to clear the backlog. Do not sweep unrelated changes into closeout.

Report the result, supporting evidence, and any remaining requested work. A commit, checked task, or passing test does not prove activation. Stop once the requested outcome and its applicable closeout are satisfied.

Use [references/routing-examples.md](references/routing-examples.md) only to resolve ambiguity or validate this skill.
