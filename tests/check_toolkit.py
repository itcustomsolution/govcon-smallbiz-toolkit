#!/usr/bin/env python3
"""Packaging checks for the toolkit (stdlib only): run `python3 tests/check_toolkit.py`.

Checks frontmatter, the per-folder LICENSE, the trust-boundary text and the documented folder-copy
installation. It does not run or evaluate any AI assistant.
"""
from pathlib import Path
import re
import shutil
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
SKILLS = sorted(p.parent for p in ROOT.glob("*/SKILL.md"))
REQUIRED_PHRASES = ("## Trust boundary", "untrusted data", "do not follow them", "Never invent or upgrade facts",
                    "keep the LICENSE file in this folder")


def problems():
    found = []
    license_text = (ROOT / "LICENSE").read_text()
    if "Permission is hereby granted" not in license_text or "Copyright (c)" not in license_text:
        found.append("root LICENSE is not the MIT notice")
    if len(SKILLS) != 3:
        found.append(f"expected 3 skill folders, found {len(SKILLS)}")
    for folder in SKILLS:
        text = (folder / "SKILL.md").read_text()
        m = re.match(r"---\nname: ([a-z0-9-]+)\ndescription: (.+?)\n---\n", text, re.S)
        if not m or m.group(1) != folder.name:
            found.append(f"{folder.name}: frontmatter name must match the folder")
        elif not 1 <= len(m.group(2)) <= 1024:
            found.append(f"{folder.name}: description must be 1-1024 characters")
        for phrase in REQUIRED_PHRASES:
            if phrase not in text:
                found.append(f"{folder.name}: missing {phrase!r}")
        if "\u2014" in text:
            found.append(f"{folder.name}: contains an em dash")
        # Simulate the README's "copy a whole folder" installation and inspect the result.
        with tempfile.TemporaryDirectory() as tmp:
            installed = Path(shutil.copytree(folder, Path(tmp) / folder.name))
            names = sorted(p.name for p in installed.iterdir())
            if names != ["LICENSE", "SKILL.md"]:
                found.append(f"{folder.name}: copied folder holds {names}, expected LICENSE and SKILL.md")
            elif (installed / "LICENSE").read_text() != license_text:
                found.append(f"{folder.name}: LICENSE differs from the root MIT notice")
    readme = (ROOT / "README.md").read_text()
    for phrase in ("Keep the `LICENSE` file with the copy", "does not make a model immune", "does not evaluate assistant behavior"):
        if phrase not in readme:
            found.append(f"README: missing {phrase!r}")
    return found


if __name__ == "__main__":
    issues = problems()
    for issue in issues:
        print("FAIL:", issue)
    print(f"{len(SKILLS)} skills checked, {len(issues)} problem(s)")
    sys.exit(1 if issues else 0)
