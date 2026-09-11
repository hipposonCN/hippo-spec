# Continue delivery in Cursor

Use only in a Cursor session, after [generic-delivery.md](generic-delivery.md). Bind the same jobs to tools that exist here. Codex thread wait is not available.

## Bind the jobs

| Job | Cursor binding |
|---|---|
| `reviewable_pr` | `gh` or the GitHub plugin. Create or update a Draft PR on the current branch after checking the workflow will not deploy. |
| `read_checks` | `gh pr checks`, `gh run view`, or the GitHub plugin. Confirm the run belongs to the candidate head. |
| `user_path_verify` | The Cursor browser tools for a UI path; the project's existing CLI/API harness otherwise. A screenshot alone does not prove the path. |
| `persist_entry` | The existing Cursor user-rule or `~/.cursor/skills/hippo-spec` install. Keep only the [host pointer](host-pointer.md). |
| `handoff_or_wait` | Cursor does not prove that a finished turn will wake later. Finish available work and hand off the PR, exact head, evidence, and next owner. |

Inspect the live tool list before acting. If browser tools, `gh`, or a PR connector are missing, mark that job blocked. Do not invent a poller.

## Read PR feedback, repair, return

```bash
gh pr view "$delivery_pr" --repo "$delivery_repo" --json url,headRefOid,baseRefName,isDraft,mergeable,reviewDecision,statusCheckRollup
gh pr checks "$delivery_pr" --repo "$delivery_repo" --json name,state,link
gh run view "$delivery_run" --repo "$delivery_repo" --json headSha,event,status,conclusion,url,jobs
gh run view "$delivery_run" --repo "$delivery_repo" --log-failed
```

The original owner reads the raw failure, repairs within the allowlist, runs affected checks, and pushes the same branch when authorized. After two same-hypothesis fixes fail, return counterevidence.

## Acceptance of this adapter

For first use or a material change, capture one authorized isolated cycle: Draft PR or natural failure → owner repair → new head → real passing run or an explicit blocked check → browser or harness evidence for the affected path. If no suitable PR or browser exists, mark live adapter validation pending. Local fixture cases do not prove this adapter.
