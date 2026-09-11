---
name: hippo-spec
description: Deliver bounded software changes using current specs, short feedback loops, and evidence-based closeout. Use when implementing, repairing, resuming, reviewing, or delegating substantive project work. Do not load this skill or its references for a clear local edit with no behavior-contract delta.
---

# Hippo Spec

Carry the requested outcome with the least process that preserves correctness. Use bundled references and the host's ordinary tools. Do not install another framework or second ledger.

## Route

1. Infer outcome, authorized scope, and delivery target (local / reviewable PR / merge / activation). Ask only for a decision that changes those. Diagnosis, a verified patch, and an activated release are different deliverables.
2. Use one existing project authority. Reuse a change only if it still owns this request. Read [full-lifecycle.md](references/full-lifecycle.md) only when selecting, updating, or closing a persistent record.
3. Read only the feature-map entries for this outcome. Classify each as valid, invalidated, or missing. A map is not permission to expand scope.
4. Pick the smallest mode. Then read at most one method reference and, if delivery needs host tools, at most one host adapter.

| Mode | When | Do |
|---|---|---|
| `skip` | Local work, no behavior-contract delta | Change and check. Load no method reference and no host adapter. |
| `review-only` | Fixed PR, commit, or diff | Inspect only. Do not edit implementation or planning records. |
| `repair` | Defect under an existing contract | Reproduce, minimal fix, verify the original symptom. |
| `continue` | Authorized remainder in an effective change | Next verifiable slice; same record. |
| `full:new` | Unrecorded durable behavior, public contract, permission, or ownership delta | Record the minimum delta, then `continue`. |
| `light` | A material decision needs investigation | Answer; implement only if already authorized. |

Modes describe work, not phases. Announcing a mode is not compliance. Score actions and artifacts.

## Invariants

1. One authority. Do not create a second ledger.
2. Least mode. Default `skip`.
3. Evidence over labels. A passing test, commit, or CI run is not activation.
4. A delivery target is not permission for merge or production.
5. Children may only narrow scope. Missing host capability is disclosed, not invented.

## Read next

Open a file only when this turn needs it:

- Checks, review, or a new verification procedure: [engineering-discipline.md](references/engineering-discipline.md)
- Next agent cannot run the user path, or the map/harness drifted: [project-verification.md](references/project-verification.md)
- Hard-to-localize defect: [diagnosing-bugs.md](references/diagnosing-bugs.md)
- Domain terms or responsibility boundaries: [domain-modeling.md](references/domain-modeling.md)
- Host PR, CI, browser, or wait/handoff: [generic-delivery.md](references/generic-delivery.md), then only the matching adapter
- Ambiguous routing: [routing-examples.md](references/routing-examples.md)
- Substantive change to this method: [method-evaluation.md](references/method-evaluation.md)

Preserve authorized behavior. Evidence may revise assumptions in place. A material conflict returns to the root or user. Update only affected feature-map entries in the same delivery. A new or changed verification procedure stays draft until one in-scope path has been run end to end.

## Hand off

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

Recipients inherit the assignment. Recheck authority on resumption. Independent reviewers stay read-only unless write ownership transfers. The coordinator splits work; start with at most three implementers; implementers do not redelegate. One Writer per worktree. Combined candidates need combined evidence.

## Close

Verify the layers that apply: artifact, implementation, operation. Report evidence and remaining work. Stop when the requested outcome is satisfied.
