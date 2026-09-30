# Host entries and install targets

Use when installing, checking, or updating Hippo Spec on a host. This file lists where each host reads the [host pointer](host-pointer.md) and the package. It does not grant capabilities; delivery jobs stay in [generic-delivery.md](generic-delivery.md).

## One source, many hosts

Keep one pinned checkout of this repository outside every host's skill directory, so no host discovers it twice. Install from it into each host with `scripts/install_hosts.py`; the script copies by default and writes `.hippo-spec-pin` with the source commit. A profile file outside the public repository says which hosts to install. See `profiles/example.json`.

`--check` reports drift: a host copy whose pin or files differ from the source. Fix drift by reinstalling from the source, never by editing a host copy.

## Hosts

Defaults below are the hosts' documented or observed user-level locations. Override them in the profile when a host moves them.

| Host | Package directory | Entry for the pointer | Entry type | Delivery adapter |
|---|---|---|---|---|
| Codex | `~/.codex/skills/hippo-spec` | `~/.codex/AGENTS.md` | file | [codex-delivery.md](codex-delivery.md) |
| Cursor | `~/.cursor/skills/hippo-spec` | User Rules in Cursor settings | UI | [cursor-delivery.md](cursor-delivery.md) |
| Claude Code | `~/.claude/skills/hippo-spec` | `~/.claude/CLAUDE.md` | file | none; generic only |
| Kimi Code | `~/.kimi-code/skills/hippo-spec` | `~/.kimi-code/AGENTS.md` | file | none; generic only |
| Grok | none | Custom instructions in the Grok app | UI | none; generic only |

For a file entry the script writes the pointer between `hippo-spec:pointer` markers and leaves the rest of the file alone. If the file already mentions Hippo Spec outside the markers, it reports that instead of writing a second pointer. For a UI entry it prints the pointer to paste.

A host without a package directory reads the method by path: its pointer names the pinned checkout. The project `AGENTS.md` remains its only automatic entry.

## Capability status

A host without its own adapter uses [generic-delivery.md](generic-delivery.md) and discloses each job it cannot bind. Until a host has run the kernel cases in [method-evaluation.md](method-evaluation.md) with a kept transcript, assign it `review-only` or `light` work, or implementation that another owner verifies. Record which cases a host has passed in the profile, not here.
