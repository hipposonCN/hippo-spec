# Diagnose through a repeatable symptom

Use for hard-to-localize bugs, intermittent failures, and performance regressions. Read the relevant project context and decisions. Keep the root assignment's authorization: read-only diagnosis must not edit project files, install tools, add instrumentation, or trigger mutating operations. Use safe existing observations and report any reproduction limit. Redact secrets from commands, output, and captured artifacts.

## Establish the feedback loop

Before choosing a cause or fix, build a short repeatable check that fails on the user's actual symptom. Reading code to find a runnable seam is useful; code inspection alone is not reproduction evidence.

Prefer an existing test seam, a request against a permitted local service, a CLI fixture, a browser assertion, or replay of an available trace. If needed and within scope, use a disposable harness, seeded property checks, or a comparison of known states. Reuse available tools rather than install a new diagnostic stack.

Run the check and retain the command, inputs, and observed failure. Assert the wrong value, error, missing result, or measured latency; "did not crash" is insufficient when the reported bug is incorrect behavior. Make setup cheap, isolate unrelated state, and control time, randomness, and external responses where possible.

For intermittent failures, repeat under controlled conditions and record attempts, failures, and conditions before and after the fix. Increase the reproduction rate safely in an isolated environment; a lucky green run does not establish a repair. For performance, measure the same workload and baseline before changing code; use a profiler or query plan when it distinguishes causes.

If automation is impossible, describe a precise human-assisted trigger and expected/actual signal without depending on a script template. If no safe reproduction is available, report what was tried and which access or artifact is missing. Label code-traced explanations as unconfirmed; do not present a guessed fix as verified. Continue independent authorized work.

## Minimize and discriminate

Reduce inputs and steps one at a time while retaining the exact failure. Stop when further reduction would lose the real triggering pattern or cease to help distinguish causes.

Rank the plausible causes and state a falsifiable prediction for each: changing or observing which variable would distinguish it? Do not invent extra hypotheses to fill a quota. Share the leading predictions briefly when useful; existing authorization does not require a new approval checkpoint.

Probe one variable at a time using debugger inspection, a targeted measurement, or narrowly tagged temporary logs when edits are authorized. Each probe should distinguish predictions. Avoid broad log dumps. Use bisection when a known good/bad boundary makes it cheaper than further speculation.

## Repair and verify when authorized

Turn the reduced scenario into a regression test at a seam that exercises the real bug pattern, including multiple callers or layers when needed. Run it red before the fix, apply the minimum repair, then run it green and rerun the original scenario. A shallow test that cannot fail on the reported pattern is not regression coverage.

If no suitable permanent test seam exists, retain the reproducible verification evidence and state the coverage gap; do not launch an architecture rewrite to manufacture a test. Remove temporary instrumentation and disposable artifacts created for this diagnosis. Record the demonstrated cause, fix, and remaining limitations in the existing result or change record.

Adapted from Matt Pocock's diagnosis method; attribution and license are in [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md).
