# Establish or maintain a project verification entry

Use when a project's next agent cannot locate or execute the relevant user-path verification, or when the existing map/harness has changed. The behavioral proof requirements remain in [engineering-discipline.md](engineering-discipline.md#agent-operated-verification). This procedure makes those requirements reachable; it does not create another product specification.

## Reuse and locate

Read the selected task and relevant map entries, then inspect the existing launch command, tests, fixtures and evidence. Record only the affected paths as usable, invalidated by a relevant change, or missing. A different folder layout is not a gap. Prefer the project's existing verification Skill or test guide; do not generate a second map or move working files for consistency.

For each selected feature, the next agent needs:

| Field | Concrete project input |
| --- | --- |
| Reach | User entry point, permissions, prerequisites and relevant alternate routes |
| Identify | Checkout/build SHA, data binding, owned port/process and readiness check |
| Drive | Existing executable command or browser handles and isolated fixture |
| Assert | Observable success, specified rejection/replay/refresh behavior and unchanged state |
| Preserve | Raw results, receipt/readback, applicable screenshots, versions and evidence directory |
| Clean | Owned process/data handles; evidence outside the disposable state |

Resolve values from the repository. Do not hand over placeholders as a runnable guide. For multiple repositories, identify each required SHA and actual package/runtime input. Mark unavailable prerequisites explicitly instead of adding a fabricated adapter or bypassing a required writer.

## Close one concrete gap

Update the existing entry with missing commands or handles. Add a small helper only if available tools cannot execute the necessary operation reliably. A missing project-local Skill can be represented by the existing test guide referenced from AGENTS; a new Skill is useful only if discovery itself is the constraint. Choose the host-supported location, not a hard-coded Cursor directory.

Execute the resulting instructions on one affected feature, including the action, outcome, necessary negative path and cleanup. A passing API check cannot replace a required browser interaction. After a failed attempt, inspect health and instance identity before retrying; clean only that attempt's owned residue. Retain raw evidence outside the disposable fixture and confirm it survives teardown.

Return the exact version, entry/command, covered path, result, evidence and remaining prerequisite. One executed path proves only that path. If execution is blocked, the procedure remains draft for that path.

## Maintain without hiding regressions

Limit ordinary maintenance to the features changed by the delivery. Only an explicitly requested whole-map audit covers every feature. Start with the index and affected source paths, then exercise the affected real paths; reuse valid evidence elsewhere.

- **Documentation drift:** the accepted product behavior changed; correct the map and cite the authority.
- **Harness gap:** the supported behavior works but the verification route is broken; fix only the owned harness and re-drive it.
- **Product regression:** the app violates accepted behavior; return the defect to the product owner. Do not change the map to redefine the failure as success.

For a verification-only assignment, product implementation and formal data remain read-only. Report `clean` with reused/fresh coverage, `changed` with proven corrections, or `blocked` with the exact missing capability. A clean run needs no PR. Corrections go in the existing relevant PR when possible; no recurring audit is created by this method.
