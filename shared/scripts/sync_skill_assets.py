#!/usr/bin/env python3
"""Copy shared ESG references, templates, and examples into each skill directory."""

from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SHARED = ROOT / "shared"
SKILLS = [
    "esg",
    "esg-a-share-gap-check",
    "esg-hkex-gap-check",
    "esg-issb-climate",
    "esg-board-brief",
    "esg-investor-qa",
    "esg-data-request",
    "esg-rating-response",
    "esg-materiality",
]


def copy_tree_contents(source: Path, destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=True)
    for item in source.iterdir():
        target = destination / item.name
        if item.is_dir():
            # Safe scope: this script only regenerates controlled copies under repo skill folders.
            if target.exists():
                shutil.rmtree(target)
            shutil.copytree(item, target)
        else:
            shutil.copy2(item, target)


def main() -> int:
    for skill in SKILLS:
        skill_dir = ROOT / "skills" / skill
        copy_tree_contents(SHARED / "references", skill_dir / "references")
        copy_tree_contents(SHARED / "templates", skill_dir / "assets" / "templates")
        copy_tree_contents(SHARED / "examples", skill_dir / "examples")
    print("Synced shared references, templates, and examples into skill directories.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
