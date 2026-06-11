#!/usr/bin/env python3
"""Audit translation coverage and protected-item preservation."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


CHINESE_RE = re.compile(r"[\u4e00-\u9fff]")


def load_units(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, list):
        return data
    if isinstance(data, dict) and isinstance(data.get("units"), list):
        return data["units"]
    raise ValueError("translation units must be a list or an object with a 'units' list")


def status_from_counts(failures: int, warnings: int) -> str:
    if failures:
        return "fail"
    if warnings:
        return "warning"
    return "pass"


def audit(units: list[dict[str, Any]], english_text: str, review_text: str = "") -> tuple[str, list[str], list[str]]:
    combined_text = english_text + "\n" + review_text
    failures: list[str] = []
    warnings: list[str] = []

    translatable = [unit for unit in units if unit.get("translate", True)]
    for unit in translatable:
        unit_id = str(unit.get("unit_id", "")).strip()
        if unit_id and unit_id not in combined_text:
            failures.append(f"Missing translated/reviewed unit ID: {unit_id}")

    protected_source_units = [unit for unit in units if not unit.get("translate", True)]
    for unit in protected_source_units:
        unit_id = str(unit.get("unit_id", "")).strip()
        unit_type = str(unit.get("unit_type", "")).strip()
        if unit_id and unit_id in english_text and unit_type == "reference":
            warnings.append(f"Reference unit appears in English draft; confirm it was preserved, not translated: {unit_id}")

    for unit in units:
        unit_id = str(unit.get("unit_id", "")).strip()
        for item in unit.get("protected_items", []) or []:
            item_text = str(item).strip()
            if item_text and item_text not in combined_text:
                warnings.append(f"Protected item not found in outputs: {unit_id} -> {item_text}")

    chinese_hits = CHINESE_RE.findall(english_text)
    if chinese_hits:
        sample = "".join(chinese_hits[:20])
        warnings.append(f"Chinese characters remain in English draft sample: {sample}")

    if re.search(r"\n{4,}", english_text):
        warnings.append("English draft contains unusually large blank gaps.")

    return status_from_counts(len(failures), len(warnings)), failures, warnings


def render_report(status: str, failures: list[str], warnings: list[str]) -> str:
    lines = [
        "# Coverage Audit",
        "",
        f"Status: `{status}`",
        "",
        "## Failures",
        "",
    ]
    lines.extend([f"- {item}" for item in failures] or ["- None"])
    lines.extend(["", "## Warnings", ""])
    lines.extend([f"- {item}" for item in warnings] or ["- None"])
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("translation_units", type=Path)
    parser.add_argument("english_draft", type=Path)
    parser.add_argument("--review-notes", type=Path)
    parser.add_argument("--out", type=Path, default=Path("coverage_audit.md"))
    args = parser.parse_args()

    units = load_units(args.translation_units)
    english_text = args.english_draft.read_text(encoding="utf-8")
    review_text = args.review_notes.read_text(encoding="utf-8") if args.review_notes else ""
    status, failures, warnings = audit(units, english_text, review_text)
    args.out.write_text(render_report(status, failures, warnings), encoding="utf-8")
    print(f"Coverage audit status: {status}")
    return 1 if status == "fail" else 0


if __name__ == "__main__":
    raise SystemExit(main())
