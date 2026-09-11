# Engineering methods

Use only the section needed for the current work. All methods are bundled; no external skill, template, or second spec/ticket workflow is needed.

- **[Diagnosis](diagnosing-bugs.md):** read for hard-to-localize bugs, intermittent failures, or performance regressions. A routine fix with a known cause needs only the focused repair loop below.
- **[Domain modeling](domain-modeling.md):** read when defining or changing domain terms, entity relationships, or responsibility boundaries. Merely reading familiar terminology does not trigger modeling.

Pass the current outcome, scope, and authorization into the method. It cannot widen the assignment, turn read-only diagnosis into repair, or start a competing spec/task lifecycle. Use existing authorization for settled decisions; surface only material unresolved conflicts.

## Explore and model

Investigate the unresolved decision that changes the outcome. Prefer repository evidence before asking the user. Separate the required behavior from a tentative design; use a small disposable experiment when it resolves uncertainty cheaply.

Reuse the project's domain language. Keep glossary and decision rationale separate from behavior requirements. Continue already-authorized implementation once the decision is settled. A consultation-only request ends with the answer.

## Implement and repair

Each implementer works through one observable slice at a time; this does not require project-wide serial execution. Independent authorized slices may proceed concurrently under the ownership and dependency boundaries in the same Task. Prefer existing public interfaces and test seams. For behavior changes and regressions, demonstrate the missing or broken behavior before the fix, then add the minimum implementation and verify it. Test externally visible outcomes, not private structure or assertions that mirror the implementation.

Keep refactoring limited to a concrete constraint on the slice. Run focused checks during iteration and required integration/static checks at the appropriate boundary. Documentation and mechanical edits need their relevant checks, not artificial red tests. Do not rerun unchanged broad checks without a new failure, change, or unresolved concern.

## Review

Follow the verification requirements below when behavior or a verification procedure changes. For a documentation-only change, use applicable document/package checks; do not manufacture application tests.

Pin the reviewed diff and inspect both requested behavior and repository rules. Use independent review when the change or repository warrants it, not as a mandatory agent count.

A blocking finding needs an actionable defect with a concrete trigger and code/evidence trace, a failed check, or a cited requirement/rule violation. A runnable test is useful but not the only valid evidence of a defect. Subjective smells, speculative risks, and unsolicited redesigns are non-blocking.

After fixes, rerun affected checks and revisit affected findings. Broaden review only if the repair changes other relevant behavior or invalidates previous evidence. Do not repeat open-ended review until no model suggests improvements, and do not stop with a known substantive defect merely because one review has run.

## Agent-operated verification

The implementation owner must be able to understand the task, execute it, verify the relevant user behavior, and deliver inspectable evidence before parallelism is expanded. Start from the project's feature map, launch scripts, tests, and existing receipts. Classify them as reusable, invalidated by relevant changes, or missing; do not rebuild an existing harness or rerun unrelated historical acceptance.

### Select checks by the behavior at risk

| Change | Required verification when applicable |
| --- | --- |
| Bug or new behavior | Demonstrate the original symptom or missing behavior, implement the smallest change, and verify the desired result. Reuse a regression test or add one when it provides durable value; test observable behavior rather than copying implementation structure. If pre-fix reproduction is unavailable, preserve that limit instead of fabricating a red run. |
| UI interaction | Drive the real relevant screen with the available browser/app harness. Observe the action and resulting state, keyboard/viewport/reload behavior where affected. A screenshot alone or an API-only call does not prove the UI path. |
| CLI/API/library | Use the actual public command, endpoint, or exported interface. Check outputs, exit/status codes, relevant side effects, and specified error paths. |
| Durable writes or external boundaries | Use isolated synthetic state and the supported engine/package through the designated entry point. Verify persisted receipts and independent readback; check rejection, replay, lost-response and refresh invariants where relevant. Mocks prove only their declared boundary; do not bypass gates or substitute fabricated success receipts for a required real write. External delivery still requires authorization. |
| Performance | Capture comparable before/after measurements on the affected path with identified versions and inputs. Collect profiles or memory data only when needed to resolve the actual issue. |
| Integration or release | Validate the actual combined candidate and required package/activation/readback layers. Independent branch passes do not prove combined behavior; formal package requirements cannot be replaced with test-created attestations. |

Run type/static checks and affected tests during development, then the project's mandatory integration checks. Existing valid evidence may satisfy an unchanged layer when its code, inputs, interfaces, dependencies, and relevant environment remain compatible; retain its original identity. A required test that is skipped or not run without applicable reusable evidence is blocked, even if the process exits zero. Record setup failure separately from product failure. Never weaken an assertion or silently drop a requirement to make CI pass.

### Make verification executable by the next agent

Keep the procedure in the existing project verification Skill, harness documentation, or feature-map entry. Add a helper only for a concrete missing execution capability. Supply real commands/handles for that project, not an untested generic recipe:

1. **Prepare and identify:** checkout/build version, dependencies, test fixture, permitted data roots, available tools and authorization. Reuse the approved runtime; do not change interpreters or production configuration to make a test run.
2. **Launch and check health:** exact existing startup command and readiness probe; confirm the expected build, instance, port ownership and data binding. Short-lived commands need no background server. Check authentication only when required and within scope; never log credentials.
3. **Operate:** enter through the mapped user-facing path and perform the relevant actions with stable selectors or commands. Exercise specified failure conditions and verify what must remain unchanged. Do not use internal setters to manufacture the outcome the entry point should produce.
4. **Observe and preserve:** save commands, inputs/fixture identities, code versions, raw logs, exit/pass/fail/skip results, relevant screenshots/responses, receipts and before/after state. Distinguish observed effects from inferred ones, and mocks from real components. A dry-run label alone does not prove absence of effects.
5. **Clean up and hand over:** stop only instances created by this verification, identified by owned handles/PIDs; never broad-kill a process name. Remove only owned temporary state, including after failed attempts. Verify that evidence survives cleanup and give the next agent the reproducible command and evidence location.

Execute a new or materially changed procedure end to end once on at least one mapped feature before declaring the procedure delivered. One successful pilot validates only that feature/path, not the whole product. If it cannot run safely with current tools/access, identify the missing capability and mark it draft/blocked; do not shift routine log/screenshot transport onto the user or claim a text review is execution.

Independent review must inspect the fixed candidate and direct evidence rather than only the author's summary. When independent execution is required, reproduce the specified public path in an isolated environment; when only code review is possible, label that limitation.

### Validate method changes and domain conclusions separately

Package lint only establishes package integrity. For a substantive change to an execution/verification Skill, exercise a representative task using the changed method and inspect the resulting actions and raw artifacts. Keep task, fixture, code and environment fixed for before/after comparisons when claiming improved agent behavior; report outcomes, human intervention and failed attempts rather than treating token use, more agents or a reviewer opinion as proof. A reasoning-only scenario review is not an executed workflow.

In research or other judgment-heavy products, engineering correctness and domain quality are separate acceptance layers. Use the project's frozen cases and domain criteria for evidence support, temporal validity, counterevidence and reasoning where required. A valid schema, open page, or successful write does not establish the research conclusion. This does not authorize live research or introduce domain requirements into unrelated projects.

Method provenance is recorded in [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md). Source links are attribution, not runtime inputs or additional completion authorities.
