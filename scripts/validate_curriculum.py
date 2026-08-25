#!/usr/bin/env python3
"""Validate curriculum numbering and local Markdown links without dependencies."""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
DAY_PATTERN = re.compile(r"^## Day (\d+):", re.MULTILINE)
DAY_SECTION_PATTERN = re.compile(r"^## Day (\d+):(.*?)(?=^## Day |^### Phase checkpoint|\Z)", re.MULTILINE | re.DOTALL)
TRACKER_PATTERN = re.compile(r"^- \[[ xX]\] \[Day (\d+) ", re.MULTILINE)
LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
HEADING_PATTERN = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$", re.MULTILINE)
REQUIRED_FILES = (
    "README.md",
    "CURRICULUM.md",
    "CONTRIBUTING.md",
    "projects/capstone.md",
    "resources/README.md",
)


def validate_required_files() -> list[str]:
    return [f"missing required file: {path}" for path in REQUIRED_FILES if not (ROOT / path).is_file()]


def validate_days(markdown_files: list[Path]) -> list[str]:
    occurrences: list[tuple[int, Path]] = []
    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        occurrences.extend((int(day), path) for day in DAY_PATTERN.findall(text))

    counts = Counter(day for day, _ in occurrences)
    errors: list[str] = []
    expected = set(range(1, 61))
    actual = set(counts)

    if missing := sorted(expected - actual):
        errors.append(f"missing curriculum days: {missing}")
    if unexpected := sorted(actual - expected):
        errors.append(f"unexpected curriculum days: {unexpected}")
    if duplicates := sorted(day for day, count in counts.items() if count != 1):
        errors.append(f"days appearing more than once: {duplicates}")
    if len(occurrences) != 60:
        errors.append(f"expected 60 day headings, found {len(occurrences)}")

    return errors


def validate_daily_format(markdown_files: list[Path]) -> list[str]:
    errors: list[str] = []
    sections: list[tuple[int, str, Path]] = []
    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        sections.extend((int(day), section, path) for day, section in DAY_SECTION_PATTERN.findall(text))

    for day, section, path in sections:
        for label in ("**Goal:**", "**Task:**", "**Done when:**"):
            if label not in section:
                errors.append(f"{path.relative_to(ROOT)}: Day {day} is missing {label}")

    tracker = (ROOT / "CURRICULUM.md").read_text(encoding="utf-8")
    tracked_days = [int(day) for day in TRACKER_PATTERN.findall(tracker)]
    if tracked_days != list(range(1, 61)):
        errors.append("CURRICULUM.md must contain one tracker item for Days 1 through 60 in order")
    return errors


def local_link_target(raw_target: str, source: Path) -> tuple[Path, str] | None:
    target = raw_target.strip().strip("<>")
    if not target or target.startswith(("#", "http://", "https://", "mailto:")):
        if target.startswith("#"):
            return source, unquote(target[1:])
        return None

    path_part, _, fragment = target.partition("#")
    path_part = unquote(path_part)
    if not path_part:
        return None
    return (source.parent / path_part).resolve(), unquote(fragment)


def heading_anchors(path: Path) -> set[str]:
    anchors: set[str] = set()
    duplicates: Counter[str] = Counter()
    for heading in HEADING_PATTERN.findall(path.read_text(encoding="utf-8")):
        base = "".join(char for char in heading.lower() if char.isalnum() or char in "-_ ")
        base = base.replace(" ", "-")
        suffix = duplicates[base]
        anchors.add(base if suffix == 0 else f"{base}-{suffix}")
        duplicates[base] += 1
    return anchors


def validate_local_links(markdown_files: list[Path]) -> list[str]:
    errors: list[str] = []
    for source in markdown_files:
        text = source.read_text(encoding="utf-8")
        for raw_target in LINK_PATTERN.findall(text):
            resolved = local_link_target(raw_target, source)
            if resolved is None:
                continue
            target, fragment = resolved
            if ROOT not in target.parents and target != ROOT:
                errors.append(f"{source.relative_to(ROOT)}: link leaves repository: {raw_target}")
            elif not target.exists():
                errors.append(f"{source.relative_to(ROOT)}: missing link target: {raw_target}")
            elif fragment and target.is_file() and fragment not in heading_anchors(target):
                errors.append(f"{source.relative_to(ROOT)}: missing heading target: {raw_target}")
    return errors


def main() -> int:
    markdown_files = sorted(ROOT.rglob("*.md"))
    errors = validate_required_files()
    errors.extend(validate_days(markdown_files))
    errors.extend(validate_daily_format(markdown_files))
    errors.extend(validate_local_links(markdown_files))

    if errors:
        print("Curriculum validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Validated 60 formatted days, tracker items, and local links across {len(markdown_files)} Markdown files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
