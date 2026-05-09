#!/usr/bin/env python3
"""
Refresh a small latest-plan block on the homepage.
"""

from __future__ import annotations

from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"
LATEST = ROOT / "_data" / "latest_action_plan.yml"

START = "<!-- AUTO-LATEST-PLAN:START -->"
END = "<!-- AUTO-LATEST-PLAN:END -->"


def main() -> None:
    if not INDEX.exists() or not LATEST.exists():
        return

    latest = yaml.safe_load(LATEST.read_text(encoding="utf-8")) or {}

    block = f"""{START}
<section class="section latest-plan-section">
  <div class="container latest-plan-card">
    <p class="eyebrow">Latest weekly action plan</p>
    <h2>{latest.get('book_title', 'This week’s book')}</h2>
    <p>{latest.get('one_line', 'A practical plan from one powerful book.')}</p>
    <a class="button secondary" href="{{{{ '{latest.get('url', '/books/')}' | relative_url }}}}">View action plan →</a>
  </div>
</section>
{END}"""

    text = INDEX.read_text(encoding="utf-8")

    if START in text and END in text:
        before = text.split(START)[0]
        after = text.split(END)[1]
        text = before + block + after
    else:
        insert_before = '<section class="section" id="how-it-works">'
        text = text.replace(insert_before, block + "\n\n" + insert_before)

    INDEX.write_text(text, encoding="utf-8")
    print("Homepage latest-plan block refreshed.")


if __name__ == "__main__":
    main()
