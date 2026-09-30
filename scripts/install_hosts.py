#!/usr/bin/env python3
"""Install one pinned Hippo Spec checkout into each host named by a profile.

Default is a dry run. --apply writes; --check reports drift and exits 1 on any.
"""

import argparse
import filecmp
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import time

PIN = ".hippo-spec-pin"
START = "<!-- hippo-spec:pointer:start -->"
END = "<!-- hippo-spec:pointer:end -->"
IGNORE = shutil.ignore_patterns(".git", "__pycache__", PIN)

HOSTS = {
    "codex": {"package_dir": "~/.codex/skills/hippo-spec", "entry": "~/.codex/AGENTS.md"},
    "cursor": {"package_dir": "~/.cursor/skills/hippo-spec", "entry": "ui:Cursor Settings > Rules > User Rules"},
    "claude-code": {"package_dir": "~/.claude/skills/hippo-spec", "entry": "~/.claude/CLAUDE.md"},
    "kimi-code": {"package_dir": "~/.kimi-code/skills/hippo-spec", "entry": "~/.kimi-code/AGENTS.md"},
    "grok": {"package_dir": None, "entry": "ui:Grok > Settings > Custom instructions"},
}


def expand(value, home: Path) -> Path:
    return home / value[2:] if value.startswith("~/") else Path(value)


def pointer_text(source: Path) -> str:
    text = (source / "references/host-pointer.md").read_text(encoding="utf-8")
    match = re.search(r"```text\n(.*?)\n```", text, re.S)
    if not match:
        raise SystemExit("references/host-pointer.md: pointer block not found")
    return match[1]


def source_commit(source: Path, allow_dirty: bool) -> str:
    def git(*args):
        return subprocess.run(["git", "-C", str(source), *args], capture_output=True, text=True, check=True).stdout.strip()
    if git("status", "--porcelain") and not allow_dirty:
        raise SystemExit(f"{source}: uncommitted changes; commit them or pass --allow-dirty")
    return git("rev-parse", "HEAD")


def differs(a: Path, b: Path) -> bool:
    cmp = filecmp.dircmp(a, b, ignore=[".git", "__pycache__", PIN])
    if cmp.left_only or cmp.right_only or cmp.funny_files:
        return True
    _, mismatch, errors = filecmp.cmpfiles(a, b, cmp.common_files, shallow=False)
    return bool(mismatch or errors) or any(differs(a / d, b / d) for d in cmp.common_dirs)


def package_state(source: Path, target: Path, commit: str) -> str:
    if target.is_symlink():
        return "ok" if target.resolve() == source.resolve() else "foreign-symlink"
    if not target.exists():
        return "missing"
    if differs(source, target):
        return "files-differ"
    pin = target / PIN
    return "ok" if pin.is_file() and pin.read_text().strip() == commit else "pin-differs"


def entry_block(pointer: str) -> str:
    return f"{START}\n{pointer}\n{END}"


def entry_state(entry: Path, pointer: str) -> str:
    if not entry.exists():
        return "missing"
    text = entry.read_text(encoding="utf-8")
    if START in text:
        return "ok" if entry_block(pointer) in text else "pointer-differs"
    return "unmanaged-mention" if re.search(r"hippo.?spec", text, re.I) else "missing"


def install_package(source: Path, target: Path, commit: str, state: str, mode: str) -> str:
    if state == "foreign-symlink":
        return f"skip: {target} links elsewhere; remove it by hand if intended"
    note = ""
    if state == "files-differ":
        backup = target.with_name(f"{target.name}.local-edits-{time.strftime('%Y%m%dT%H%M%S')}")
        target.rename(backup)
        note = f" (local edits kept at {backup})"
    elif target.is_symlink() or target.exists():
        shutil.rmtree(target) if not target.is_symlink() else target.unlink()
    target.parent.mkdir(parents=True, exist_ok=True)
    if mode == "symlink":
        target.symlink_to(source.resolve(), target_is_directory=True)
    else:
        shutil.copytree(source, target, ignore=IGNORE)
        (target / PIN).write_text(commit + "\n")
    return f"installed {mode} at {target}{note}"


def write_entry(entry: Path, pointer: str, state: str) -> str:
    if state == "unmanaged-mention":
        return f"skip: {entry} already mentions Hippo Spec outside markers; merge by hand"
    text = entry.read_text(encoding="utf-8") if entry.exists() else ""
    block = entry_block(pointer)
    if START in text:
        text = re.sub(re.escape(START) + ".*?" + re.escape(END), lambda _: block, text, flags=re.S)
    else:
        text = (text.rstrip() + "\n\n" if text.strip() else "") + block + "\n"
    entry.parent.mkdir(parents=True, exist_ok=True)
    entry.write_text(text, encoding="utf-8")
    return f"pointer written to {entry}"


def run(profile_path: Path, home: Path, apply: bool, check: bool, allow_dirty: bool) -> int:
    profile = json.loads(profile_path.read_text(encoding="utf-8"))
    source = expand(profile["source"], home)
    commit = source_commit(source, allow_dirty)
    pointer = pointer_text(source)
    drift = 0
    print(f"source {source} @ {commit[:12]}")
    for name, cfg in profile.get("hosts", {}).items():
        if not cfg.get("enabled", True):
            continue
        if name not in HOSTS and not {"package_dir", "entry"} <= cfg.keys():
            print(f"[{name}] unknown host; give package_dir and entry in the profile")
            drift += 1
            continue
        spec = {**HOSTS.get(name, {}), **cfg}
        mode = spec.get("mode", "copy")
        if spec.get("package_dir"):
            target = expand(spec["package_dir"], home)
            state = package_state(source, target, commit)
            drift += state != "ok"
            action = install_package(source, target, commit, state, mode) if apply and state != "ok" else state
            print(f"[{name}] package {target}: {action}")
        host_pointer = pointer if spec.get("package_dir") else f"{pointer}\n\nHippo Spec package: {source}/SKILL.md"
        entry = spec.get("entry")
        if entry and entry.startswith("ui:"):
            print(f"[{name}] entry is {entry[3:]}; paste this pointer by hand:\n{host_pointer}\n")
        elif entry:
            path = expand(entry, home)
            state = entry_state(path, host_pointer)
            drift += state != "ok"
            action = write_entry(path, host_pointer, state) if apply and state != "ok" else state
            print(f"[{name}] entry {path}: {action}")
    if check:
        return 1 if drift else 0
    if not apply and drift:
        print("dry run; pass --apply to install")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile", type=Path, default=Path.home() / ".agents/hippo-spec.profile.json")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--apply", action="store_true")
    group.add_argument("--check", action="store_true")
    parser.add_argument("--allow-dirty", action="store_true")
    args = parser.parse_args()
    sys.exit(run(args.profile, Path.home(), args.apply, args.check, args.allow_dirty))
