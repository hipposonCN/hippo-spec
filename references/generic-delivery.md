# Host delivery jobs

Use when the authorized target needs a reviewable PR, CI readback, user-path verification, a persisted host entry, or a wait/handoff. Inspect the tools actually present in this session. Then read only the matching adapter:

- Cursor: [cursor-delivery.md](cursor-delivery.md)
- Codex: [codex-delivery.md](codex-delivery.md)
- Any other host, or a host missing a needed job: stay on this file and disclose the gap

This adapter does not create a scheduler, a second task store, or product rules. Carry [hippo_spec_context](../SKILL.md#hand-off). No worktree is isolated merely because another thread exists.

## Jobs

| Job | Required outcome | If the host has it | If it does not |
|---|---|---|---|
| `reviewable_pr` | Open or update a Draft PR on the current candidate after checking the workflow will not deploy | Use the live PR tool (`gh`, `glab`, or the host PR API) | Leave a local branch note and stop |
| `read_checks` | Read the exact head and required checks | Use the live CI/PR API | Report checks unknown |
| `user_path_verify` | Drive the affected user path | Use the host browser or the project's existing harness | Mark that layer blocked |
| `persist_entry` | Keep the short [host pointer](host-pointer.md) | User rule, `AGENTS.md`, or `CLAUDE.md` | Leave a session-only reminder |
| `handoff_or_wait` | Wait only if this host can wake the same owner | Use that wait API and record which wait mode actually worked | Explicit handoff; no new scheduler |

Bind to the current tool schema. Do not call a nonexistent API. Do not advertise automatic CI-to-agent continuation without observing it here.

## Shared delivery rules

Reuse the current task, branch, PR, and owner. Push the first coherent reviewable commit and open or update its Draft when PR delivery is authorized. The original owner handles ordinary CI failures. After two substantive fixes under the same hypothesis, return counterevidence. Do not weaken assertions.

Before merge, distinguish configured workflows, actual successful runs, and server-enforced checks. Merge and activation keep their own authorization. CI success grants neither.

Record which continuation mode worked: active-turn wait, configured scheduled follow-up, verified event wakeup, or manual re-entry.

## Select an execution resource

Use the least expensive existing host or runner that satisfies the task's platform and check requirements. A platform change needs either a concrete platform requirement or a bounded same-candidate comparison. Hold the exact candidate SHA, workflow and required-check set, fixtures, dependency versions, permissions, timeouts, and inputs constant; vary only the platform or resource, run each required check once on each compared resource within the authorized bound, and record startup/readiness, coverage, duration or cost signals, and failures. Keep a check-by-check coverage map and preserve every required check and assertion. A cheaper or faster resource does not justify dropping a check, weakening a test, or claiming savings from configuration alone. If the comparison cannot run, report the platform choice as unverified and retain the existing resource.

## Query existing CI before requesting a run

Treat a remote run as a state-changing, resource-consuming action and a query as a read-only observation. Query the exact candidate head, checks, run, jobs, and logs first. Request a run, rerun, or dispatch only when the existing task authorizes it, the exact head and required checks are known, and a missing or stale result or a recorded environment change makes the attempt necessary. Record whether each operation was a query or a run, its exact head/run identity, and its reason. Never trigger a run to poll status, substitute a different candidate, or repeat unchanged inputs. The final inventory must fail closed for a failed, cancelled, missing, or unexpectedly skipped required dependency; a zero-step or no-start job is not a successful check.

## Diagnose startup and infrastructure failures

If a remote job never starts, has no executable steps, or stops in queue/setup because of runner, service, billing, permission, or workflow infrastructure, classify it as an infrastructure/no-start result. Preserve the raw status, event, head, job and step state, annotations or logs, URL, and timestamps. It is neither a product-code failure nor a passing check; a required layer remains blocked until an actual run supplies its evidence. Inspect the workflow, exact ref/head, resource and account state before changing code. Do not edit product code, tests, assertions, or platform selection merely to turn an infrastructure result green, and do not blind-retry an unchanged no-start. Retry only after a concrete environment or workflow change is recorded and the bounded retry is authorized; otherwise return the blocker to the relevant owner. A job that starts and fails in its executable product steps follows the ordinary same-owner repair path.
