# Composition rules and one-source host install

Status: active
Mode after record: `continue`

## Outcome

Hippo Spec states which layer it owns beside OpenSpec and craft skills, and installs from one pinned source into every host a user names, with drift detection.

## Changed behavior

- `references/skill-composition.md`: protocol / record / craft / enforcement / project layers; OpenSpec kept as layout and CI validator, not as a second driver; craft skills suggested by mode and situation; Matt Pocock Skills split into keep, exclude and bundled.
- `references/hosts.md`: package directory, pointer entry and adapter status for Codex, Cursor, Claude Code, Kimi Code and Grok.
- `scripts/install_hosts.py`: dry run by default; `--apply` copies with `.hippo-spec-pin` and writes the pointer between markers; `--check` exits 1 on drift. Local edits in a host copy are kept aside, never overwritten. A hand-written Hippo Spec entry is reported, not duplicated.
- Personal choices (which hosts, roles, pinned version) live in a profile outside the repository. `profiles/example.json` is the only profile committed.

## Acceptance

- Package validation and all unit tests pass.
- Installer tests cover dry run, idempotent apply, drift, kept local edits, unmanaged entries and UI-only hosts.
- One real `--check` against an existing multi-host install, with its raw output kept in the PR.

## Exclusions

- No Claude Code, Kimi Code or Grok delivery adapter; they use generic delivery until they run the kernel cases.
- No download or install of third-party skills by the script.
- No automatic removal of hand-written entries in existing host files.
