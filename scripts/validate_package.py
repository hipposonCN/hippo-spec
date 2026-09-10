#!/usr/bin/env python3
"""Check the portable method package without model calls or third-party packages."""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


def validate(root: Path) -> list[str]:
    errors: list[str] = []
    for relative in (
        "SKILL.md", "README.md", "LICENSE", "THIRD_PARTY_NOTICES.md",
        "agents/openai.yaml", "references/routing-examples.md",
    ):
        if not (root / relative).is_file():
            errors.append(f"Missing package file: {relative}")
    skill = root / "SKILL.md"
    if skill.is_file():
        text = skill.read_text(encoding="utf-8")
        header = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.S)
        if not header:
            errors.append("SKILL.md: missing frontmatter")
        else:
            for field in ("name", "description"):
                if not re.search(rf"^{field}:\s*\S.+$", header[1], re.M):
                    errors.append(f"SKILL.md: missing {field}")
    for path in sorted(root.rglob("*.md")):
        if ".git" in path.relative_to(root).parts:
            continue
        text = path.read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^\s)]+)\)", text):
            url = urlsplit(target.strip("<>"))
            if url.scheme or url.netloc or not url.path:
                continue
            resolved = (path.parent / unquote(url.path)).resolve()
            if not resolved.is_relative_to(root):
                errors.append(f"{path.relative_to(root)}: nonportable link {target}")
            elif not resolved.exists():
                errors.append(f"{path.relative_to(root)}: missing link target {target}")
    return errors


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    errors = validate(root)
    for error in errors:
        print(error, file=sys.stderr)
    if errors:
        raise SystemExit(1)
    print("Package entry points, required metadata, and local Markdown targets passed.")
