# Compose with spec formats and craft skills

Use when a turn would load another process or craft skill next to Hippo Spec, or when choosing what to install beside it. Hippo Spec stays the protocol: route, authority, ownership, handoff, evidence, close. Other packages fill layers it does not own.

## Layers

| Layer | Owns | Source |
|---|---|---|
| Protocol | Mode, scope, owner, handoff, delivery target, evidence | Hippo Spec |
| Behavior record | Current requirements and the change delta | The project's existing convention, commonly the OpenSpec layout |
| Craft | How to do one step well | Optional craft skills |
| Enforcement | What actually blocks a bad change | Project CI, required checks, release manifests |
| Project | Repository boundaries and acceptance | Project `AGENTS.md` and project standard |

A lower layer never overrides a higher one's authority, and no layer creates a second task record.

## OpenSpec

Keep the document layout: `openspec/specs/` and `openspec/changes/`, maintained as described in [full-lifecycle.md](full-lifecycle.md).

- Do not run OpenSpec's propose/apply/archive commands or generated skills as the process driver beside Hippo Spec. Two drivers mean two routers.
- Keep the OpenSpec CLI as a validator where the project wants structural checks: `openspec validate --strict` in CI. Manual review is not that check.
- A project without OpenSpec keeps its own record convention. Do not install OpenSpec to satisfy this file.

## Craft skills

A craft skill is allowed when it does one step and returns its output to the current authority. A skill is excluded when it selects work, keeps its own ticket or spec store, defines its own handoff, or opens PRs on its own schedule.

Suggested use by situation, only when the skill is installed on this host:

| Situation in the current mode | Craft skill |
|---|---|
| `full:new` or `light`: requirements or a plan are still vague | `grill-me` or `grill-with-docs` (manual) |
| `continue` or `repair` with a testable seam | `tdd` |
| A UI or state model needs a throwaway check before committing | `prototype` |
| `light`: module interface or seam decision | `codebase-design`; `improve-codebase-architecture` (manual) |
| `light`: external facts or API behavior | `research` |
| `review-only` | `code-review`, reporting into the review, not a new record |
| Hard-to-localize defect | Bundled [diagnosing-bugs.md](diagnosing-bugs.md), not a second copy |
| Domain terms or responsibility boundaries | Bundled [domain-modeling.md](domain-modeling.md), not a second copy |

"Manual" skills declare `disable-model-invocation`; hosts that honor it will not auto-trigger them. When the table names one for the current turn, open its `SKILL.md` directly or ask the user, and say which.

Write craft output into the existing record: a decision into the change's design, a found requirement into the delta spec, test evidence into the task. A craft skill's own doc or ADR location is used only if the project already uses it.

## Matt Pocock Skills mapping

Checked against [mattpocock/skills](https://github.com/mattpocock/skills/tree/d81f3a183412e71a5b1e84ca21bc1a35eea03a60). Recheck on upgrade; names and triggers change.

| Keep as craft | Exclude beside Hippo Spec | Already bundled here |
|---|---|---|
| `tdd`, `prototype`, `research`, `codebase-design`, `improve-codebase-architecture`, `grill-me`, `grill-with-docs`, `code-review`, `wait-what`, `teach` | `to-spec`, `to-tickets`, `implement-spec`, `implement`, `pr`, `handoff`, `claude-handoff`, `triage`, `wayfinder`, `ask-matt`, `setup-matt-pocock-skills`, `wizard`, `loop-me` | `diagnosing-bugs`, `domain-modeling` |

Excluded skills are not wrong. They own routing, tickets, handoff, or PR flow, which Hippo Spec already owns. Installing both gives an agent two answers to the same question.
