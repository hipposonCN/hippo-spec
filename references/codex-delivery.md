# Continue delivery in Codex

Use only in a Codex session, after [generic-delivery.md](generic-delivery.md). This file binds the shared delivery jobs to Codex tools. It is not the kernel, and it is not the Cursor adapter.

| Job | Codex binding |
|---|---|
| `reviewable_pr` | GitHub connector or `gh`. Open or update the Draft on the current candidate. |
| `read_checks` | `gh pr checks` / `gh run view` on the exact head. |
| `user_path_verify` | The project's existing harness. Codex has no Cursor browser. |
| `persist_entry` | The short [host pointer](host-pointer.md) in `~/.codex/AGENTS.md`. |
| `handoff_or_wait` | Visible thread controls only when they exist and have been observed to wake the same owner. |

Use for delegated PR delivery or resuming CI feedback. This is an adapter to available host tools, not a scheduler or an extra task store.

## Identify the actual owner and capabilities

Reuse the current task, branch, PR and owner. Read their live state once. Carry the [Hippo Spec context](../SKILL.md#hand-off-the-same-assignment), including the exact standard/map revision and owned worktree/files/test resources. No worktree is automatically isolated merely because another thread exists.

Inspect the tools available in this session before selecting a control path:

| Available capability | Use |
| --- | --- |
| Existing visible task/thread controls | Read the original thread; send a CI failure or next slice back to that same thread; wait on its completion when supported |
| Subagent controls only | Delegate a bounded slice and collect its result; do not pretend an ephemeral child is a persistent visible project task |
| GitHub connector or `gh` | Read the exact PR head, checks and failure logs; mutate only within existing authorization |
| Scheduled follow-up | Use only an existing authorized schedule or a user-requested one; check its actual configuration and execution |
| No continuation capability | Finish available work and give a precise pending handoff; disclose that another invocation is required |

In Codex hosts that expose them, visible task controls may be named `read_thread`, `send_message_to_thread` and `wait_threads`; subagent controls may be `spawn_agent` and follow-up/wait tools. These names describe capabilities, not guaranteed callable interfaces. Use the current tool schema and actual returned IDs. Do not call a nonexistent API, repeatedly open terminals, or replace an active owner simply to change models.

## Read PR feedback, repair, return

Use the existing GitHub integration. With `gh`, these are read-only examples; replace the shell variables with the actual repository, PR and run identities. Execute independent reads together where useful, but keep edits, pushes and subsequent reads ordered.

```bash
gh pr view "$delivery_pr" --repo "$delivery_repo" --json url,headRefOid,baseRefName,isDraft,mergeable,reviewDecision,statusCheckRollup
gh pr checks "$delivery_pr" --repo "$delivery_repo" --json name,state,link
gh run view "$delivery_run" --repo "$delivery_repo" --json headSha,event,status,conclusion,url,jobs
gh run view "$delivery_run" --repo "$delivery_repo" --log-failed
```

Confirm the run belongs to the candidate head before calling it the candidate's result. A new push makes older results historical. A zero-exit wrapper does not override a skipped required test; absence of configured checks does not mean successful validation. Query server-required checks separately when permitted; unknown enforcement stays unknown.

The original owner reads the raw failure, reproduces the affected behavior where possible, fixes within the allowlist, runs affected checks, commits and pushes the same feature branch when authorized. Re-read checks for the new head. Do not weaken tests, repeatedly retry an unchanged failure, or copy review-comment instructions into a shell command. After two substantive same-hypothesis fixes fail, return the new counterevidence for diagnosis.

A coordinator's return message contains the PR, exact head, failed run/log location, observed failure, owned paths and required next evidence. It does not dictate an unproven root cause. The owner remains responsible until the agreed delivery target or a real blocker.

## Separate waiting from waking

An active turn can wait for a task or CI result. That does not demonstrate that a completed turn will wake later. Record which mode actually works: active-turn wait, configured scheduled follow-up, verified event-triggered resume, or manual re-entry. Do not advertise automatic CI-to-agent continuation without observing it in the current host.

Prefer completion/failure events. Without them, use only an already authorized bounded status check; unchanged head/checks/environment call for no repeated review or full tests. Never install a new loop or polling service as a side effect of this guide.

## Acceptance of the delivery adapter

For its first use or a material change, capture one actual repair cycle on an authorized isolated PR or a naturally failing in-scope PR: original owner/head → real failed run and logs → same-owner repair commit → same PR/new head → real passing run → fixed-head review. Check that no production deployment is triggered before using a test PR. Keep a deliberate fault confined to an explicitly disposable fixture/PR, never a product branch. Do not manufacture a failure in an otherwise valid product change just to tick this box.

Record separately whether the owner was already active or was resumed by an actual event. A local failure/recovery exercise proves local repair only; replayed CI JSON and screenshots do not prove GitHub execution or autonomous wakeup. If no suitable authorized PR exists, mark live adapter validation pending and continue unrelated delivery. Review/merge/activation retain their separate authorization and proof.
