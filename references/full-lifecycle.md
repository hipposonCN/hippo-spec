# Keep one current behavior record

Use this reference when selecting, updating, or closing a persistent record. Do not restart planning for a stage transition.

## Select the effective authority

Inspect the relevant current spec, candidate change, and available supersession or completion evidence. A matching title, newer timestamp, or unchecked box alone does not establish authority. If sources conflict materially, expose the conflict rather than silently pick the convenient one.

Continue a change only when it still owns the requested behavior and has authorized work remaining. An archived or superseded change can explain history but must not reactivate its old task tree. Honor the user's explicit new decision by updating the affected requirement; preserve unrelated contracts and permissions.

## Record only the behavior delta

Use the existing documentation/spec/task convention with ordinary file reads and edits. If none exists and durable behavior needs recording, use one concise Markdown record in the project's normal documentation location. Do not install a framework, add a schema, or publish to an external tracker merely to use this skill.

Capture the outcome, changed behavior, necessary acceptance scenarios, and exclusions. Reuse existing requirements by reference. Add design rationale only for a consequential choice; do not generate exhaustive user stories or speculative future tasks.

Refine design assumptions and task order as evidence arrives. Replace obsolete planning text in place, retaining a short reason or supersession link where needed. An implementation difficulty is not permission to remove a requirement or narrow acceptance. A newly discovered need outside the assignment is a separate decision, not an automatic addition.

## Maintain existing OpenSpec records without its CLI

Treat OpenSpec as a document layout, not a runtime dependency. Read the relevant local configuration/schema when present; custom layouts retain their own requirements. For the common spec-driven layout:

1. Read the affected current `openspec/specs/<capability>/spec.md` and selected `openspec/changes/<change>/` records: proposal, tasks, design if relevant, and delta specs. Current requirements plus the authorized delta define the assignment. Preserve unrelated records.
2. Edit only the needed Markdown. Keep existing `### Requirement:` and `#### Scenario:` structure; delta sections use `ADDED`, `MODIFIED`, `REMOVED`, or `RENAMED Requirements`. A modified requirement includes its complete intended text and scenarios. Do not create missing artifact types unless the local convention or this change needs them.
3. After verification, synchronize the accepted delta into the current spec. Add missing requirements; replace the uniquely matched modified requirement; apply explicit removals and renames only. Preserve unrelated requirements and scenarios, and omit delta operation headings from the current spec. If already synchronized, do not duplicate it. A missing/ambiguous match or conflicting overlapping delta needs resolution before synchronization; never guess from archive order.
4. Review the resulting spec against the accepted behavior and evidence. Check changed requirement names, scenarios, references, and task truth. Archive only the selected completed folder using the project's existing archive naming, without overwriting an archive; if no convention exists, use `openspec/changes/archive/YYYY-MM-DD-<change>/`.

Run repository-required checks when applicable. Direct document review does not replace or claim equivalence to `openspec validate --strict`. If an existing build/CI requires that CLI and it is unavailable, report the unmet check and keep its completion claim open; do not install it silently, bypass the gate, or rewrite build policy. Removing that project dependency requires a scoped migration preserving the checks that matter. New projects need no OpenSpec configuration or CLI gate.

## Close precisely

- Mark only behavior backed by the required evidence complete. Keep source, merge, activation, and delivery states distinct when they matter to the request.
- Synchronize accepted behavior into the current spec using the existing document convention. Reconcile overlapping deltas by explicit decisions and implementation evidence, not archive order alone.
- Archive a completed change when its applicable evidence and synchronization are complete. A superseded change needs a replacement reference and disposition of remaining work; do not claim the old work was implemented.
- Close only the selected change or slice. A larger parent can remain open; unrelated historical cleanup is a separate assignment.

If closeout requires unavailable authority or an unapproved external action, report exactly what is complete and what remains. Preserve the evidence so the next executor can continue without reconstructing the task.
