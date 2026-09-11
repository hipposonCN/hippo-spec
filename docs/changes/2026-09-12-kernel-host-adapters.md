# Kernel and host adapters

Status: active
Mode after record: `continue`

## Outcome

Hippo Spec loads as a short kernel. Host-specific delivery lives in adapters. The always-on host pointer does not ingest the method package.

## Changed behavior

- `SKILL.md` is the kernel: route, invariants, one-file read-next, handoff, close.
- Feature maps, verification discipline, multi-agent ownership, and CI closeout stay in existing references. This change does not rewrite those ideas.
- Delivery jobs are defined once in `references/generic-delivery.md`. Cursor and Codex bind the same jobs; a missing capability is disclosed.
- `skip` loads no method reference and no host adapter.

## Acceptance

- Package validation and local fixture tests pass.
- Kernel body stays short enough that `scripts/validate_package.py` accepts it.
- A README typo routes to `skip` without opening a delivery adapter.
- Cursor PR/browser work reads `cursor-delivery.md`, not `codex-delivery.md`.

## Exclusions

- No new local fixture for `always-on-weight`.
- No Claude Code or Pi adapter until those hosts run the same kernel cases.
- No Plugin marketplace packaging.
- No claim that this method plus a strong model is world-class without host transcripts.
