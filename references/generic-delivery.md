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
