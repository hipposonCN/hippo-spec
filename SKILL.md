---
name: hippo-spec
description: Deliver bounded software changes using current specs, short feedback loops, and evidence-based closeout. Use when implementing, repairing, resuming, or reviewing substantive project work; keep routine edits lightweight.
---

# Hippo Spec

Carry the user's requested outcome through implementation and applicable closeout. Keep the scope bounded, let evidence refine the approach, and use the least process that preserves correctness.

This skill is self-contained. Use its bundled references and the host's normal repository tools; no OpenSpec CLI, Matt Pocock skills, external templates, or network setup is required by this workflow.

## Establish the working boundary

Infer the requested result, authorized scope, and completion evidence from the conversation and relevant project artifacts. Ask only for a missing decision that materially changes the outcome or authorization. Diagnosis, a verified patch, and an activated release are different deliverables.

Use one behavior and task authority in the project's existing spec, documentation, or issue convention. Existing OpenSpec Markdown remains usable as project records without installing its framework. Do not initialize another framework or create a second ledger. A historical plan does not authorize work or override the user's current request. Code and runtime evidence describe what exists, not what the user intended.

Reuse a change only when it is still effective, not superseded, and its remaining work matches this request. Inspect the relevant authority and revision; do not audit the entire historical backlog on every task. Read [references/full-lifecycle.md](references/full-lifecycle.md) when selecting, updating, or closing a persistent record.

Read only the feature-map entries relevant to the user outcome. Separate implemented behavior with valid evidence, evidence invalidated by relevant changes, and actual missing behavior. Use that comparison to select the next independently verifiable slice; a map is not permission to expand the backlog. If the project has no map, use its existing tests and documentation and record only the mapping needed for this task.

Establish the authorized delivery target in the existing task before implementation: local change, reviewable PR with required validation, merge, or activated release with runtime proof. Infer it from the user's request and existing authorization; ask only for a material ambiguity. A target does not authorize its side effects. Keep scope, owner, baseline, relevant feature-map entries, and acceptance conditions together; do not create a parallel task format.

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

Use short behavior-level feedback loops and proportional review through [references/engineering-discipline.md](references/engineering-discipline.md). For hard diagnosis or domain-model changes, it routes to bundled methods. Read only the needed reference and use it directly, without an external skill lookup or installation. These methods inherit this assignment's scope, authorization, and single behavior authority.

For behavior changes, select the applicable checks using that reference's [verification requirements](references/engineering-discipline.md#agent-operated-verification). The owner executes the available user-path verification and captures raw evidence without making the user relay routine screenshots or logs. Reuse existing verification entry points; a newly written or materially changed verification procedure is only a draft until its own instructions have been run end to end on at least one in-scope feature, including cleanup and surviving evidence. Missing access or tools blocks the affected claim; builds, mocks, and another agent's opinion do not replace the required observation.

When the next agent cannot find or operate that entry, or the map/harness has drifted, use [project verification maintenance](references/project-verification.md). Reuse the project's existing location and repair only the affected mapping or harness; do not change documented expectations to hide a product regression.

## Hand off the same assignment

Only when crossing an executor or session boundary, pass:

```yaml
hippo_spec_context:
  lane: skip | light | continue | repair | review-only
  active_change: <effective spec/change/task reference and revision, or none>
  scope_lock: <authorized systems, explicit exclusions and any file allowlist>
  current_slice: <immediate objective and its place in the requested outcome>
  acceptance_evidence: <required checks/readbacks and evidence already obtained>
  standard_and_map: <actual paths and revisions/content hashes; relevant entries only>
  ownership: <owner and return destination; checkout/base SHA; owned files and isolated test resources>
  delivery_target: <authorized terminal outcome; existing branch/PR or not applicable>
  return_evidence: <candidate SHA, changed paths, raw results, evidence locations, blockers and next owner>
```

`full:new` records the delta at the root, then becomes `continue`. Recipients inherit the assignment rather than replan it. Recheck the selected authority's validity on resumption; return material conflicts to the root. A mode transition never grants more scope or permission.

Supply this context explicitly when delegating, including to further descendants; do not assume the host copies conversation or global instructions. Resolve the referenced inputs before dependent writes; report missing inputs rather than inventing them. A child may narrow permissions, never widen them. Use one Writer per worktree/branch, assign shared interfaces and integration files to one owner, and isolate writable fixtures/ports. Independent reviewers remain read-only unless write ownership is explicitly transferred. Delegate only when an independently completable slice materially benefits from it; otherwise execute locally.

For controlled parallel work, record the implementers, worktrees/baselines, owned files and writable test resources, shared-file owner, dependencies, and delivery endpoints in the existing Task before dispatch. Begin with at most three implementers; only the coordinator splits the work, and implementers do not redelegate. Each owns one independently verifiable slice through implementation, applicable verification, and ordinary repair. This limits each assignment, not the whole project to serial execution. Coordinate on delivery, failure, shared-boundary changes, or real blockers; accept the actual combined candidate using still-valid evidence plus checks of affected integration boundaries.

## Own delivery through feedback

For an authorized PR delivery, push the first coherent reviewable commit and create or update its Draft PR after checking that the workflow does not cause unauthorized deployment. Do not wait for all project work or final independent review to open the Draft. Reuse the same task and PR through implementation, affected tests, CI repair, and delivery. Update only affected feature-map entries with implementation, test, PR, and evidence references in that delivery.

The original owner handles ordinary CI failures autonomously within scope. After two substantive fixes under the same failing hypothesis, reassess the hypothesis, inputs, and environment and return the counterevidence to the coordinator if unresolved. Preserve raw failures; do not weaken assertions or skip required checks to get green. Reuse valid unchanged evidence and recheck affected boundaries after a fix. Integrated or release acceptance must cover the actual combined candidate and required package/runtime layers.

Use available task-completion and CI feedback mechanisms. On delivery, failure, or a decision, send the coordinator the PR, exact head, run/result, evidence, blocker, and next owner. Do not assume a CI event can wake an agent: when unsupported, disclose that limit and use an existing bounded status check or explicit handoff. Do not create a scheduler or recurring automation without authorization; unchanged state calls for no repeated audit or reminder.

For Codex thread/PR continuation, use the [host adapter](references/codex-delivery.md) only when needed. Bind to tools actually available in that session and distinguish an active wait from a proven later wakeup.

Before merge, verify the reviewed candidate against the intended merge content and required checks. Distinguish configured workflows, actual successful runs, and server-enforced checks. Merge, deployment, and external delivery retain their own authorization boundaries; CI success alone grants none of them.

## Close the requested outcome

Verify only the applicable layers:

- **Artifact:** the relevant behavior record reflects the authorized change and remains valid.
- **Implementation:** the requested behavior and focused checks pass.
- **Operation:** the intended release, process, external receipt, or fresh readback is active when requested.

Update the selected task and synchronize/close its record as applicable, within authorization. A verified slice may finish while its parent change remains open. Distinguish completed, blocked, and superseded work; never mark unfinished work done to clear the backlog. Do not sweep unrelated changes into closeout.

Report the result, supporting evidence, and any remaining requested work. A commit, checked task, or passing test does not prove activation. Stop once the requested outcome and its applicable closeout are satisfied.

Use [references/routing-examples.md](references/routing-examples.md) only to resolve ambiguity or validate this skill.

For substantive method changes, use [fixed behavioral cases](references/method-evaluation.md) and inspect executed actions and artifacts. The fixture helper does not run agents or prove their behavior by itself.
