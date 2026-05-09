#!/usr/bin/env python3
"""
Quality checks for generated weekly action plan pages.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BOOKS = ROOT / "_books"

FORBIDDEN = [
    "guaranteed return",
    "guaranteed returns",
    "guaranteed fire",
    "risk-free",
    "get rich quick",
    "investment advice",
    "financial advice",
    "newsletter",
]


def main() -> None:
    errors: list[str] = []

    for path in BOOKS.glob("*.md"):
        text = path.read_text(encoding="utf-8", errors="ignore")
        lower = text.lower()

        if "action plan" not in lower:
            errors.append(f"{path}: missing action plan positioning.")

        for term in FORBIDDEN:
            if term in lower:
                errors.append(f"{path}: contains forbidden wording: {term}")

        if "actions:" not in text:
            errors.append(f"{path}: missing actions front matter.")

        if len(re.findall(r"time_required:", text)) < 3:
            errors.append(f"{path}: expected at least 3 actions.")

    if errors:
        print("Quality check failed:")
        for error in errors:
            print(f"- {error}")
        sys.exit(1)

    print("Quality check passed.")


if __name__ == "__main__":
    main()
