#!/usr/bin/env python3
"""
Generate the next weekly Book Action Plan.

Required GitHub secret:
OPENAI_API_KEY

Optional environment variables:
OPENAI_MODEL=gpt-4o-mini
SITE_URL=https://lab.pierrehenry.dev
"""

from __future__ import annotations

import json
import os
import re
import sys
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Dict, List

import yaml
from openai import OpenAI

ROOT = Path(__file__).resolve().parents[1]
BOOKS_DIR = ROOT / "_books"
DATA_DIR = ROOT / "_data"
BACKLOG = ROOT / "data" / "books_backlog.yml"
REPORTS = ROOT / "reports"
MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
SITE_URL = os.getenv("SITE_URL", "https://lab.pierrehenry.dev").rstrip("/")

BOOKS_DIR.mkdir(exist_ok=True)
DATA_DIR.mkdir(exist_ok=True)
REPORTS.mkdir(exist_ok=True)


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def read_backlog() -> List[Dict[str, Any]]:
    if not BACKLOG.exists():
        raise FileNotFoundError(f"Missing backlog: {BACKLOG}")
    data = yaml.safe_load(BACKLOG.read_text(encoding="utf-8")) or []
    if not isinstance(data, list):
        raise ValueError("data/books_backlog.yml must be a list.")
    return data


def pick_next_book() -> Dict[str, Any] | None:
    existing = {p.stem for p in BOOKS_DIR.glob("*.md")}
    for item in read_backlog():
        if not item.get("enabled", True):
            continue
        slug = slugify(item["title"])
        if slug not in existing:
            item["slug"] = slug
            return item
    return None


def build_prompt(book: Dict[str, Any]) -> str:
    return f"""
Create a weekly Book Action Plan page for this Jekyll site.

Book:
- title: {book['title']}
- author: {book['author']}
- category: {book.get('category', 'Book action plan')}
- angle: {book.get('angle', '')}

Audience:
Software engineers and tech professionals working towards FIRE who read useful books but often apply too little because they lack time, consistency and a simple weekly implementation system.

Brand:
Your Success is Closer Than You Think™
Tagline:
Read less. Apply more.
Product format:
Weekly Action Plan Letter

Output requirements:
Return strict JSON only with these keys:
- title
- meta_description
- one_line
- problem
- promise
- intro_markdown
- key_ideas: array of 3 strings
- actions: array of 3 objects with title, time_required, why, action
- weekly_plan: array of 5 objects with day, focus, action
- closing_markdown

Rules:
- Do not invent direct quotes.
- Do not make financial advice claims.
- Do not promise guaranteed FIRE or returns.
- Make actions concrete and doable in 5 to 20 minutes.
- Avoid generic summary language.
- Focus on implementation.
- Target finance, wealth, self-improvement, habits, focus and early retirement.
- Make the page feel specific to software engineers, not a generic audience.
- Write in clear British English.
"""


def generate_plan(book: Dict[str, Any]) -> Dict[str, Any]:
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError("OPENAI_API_KEY is missing.")

    client = OpenAI()
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a careful editor and product marketer. "
                    "Create concise, practical, ethical weekly action plans from books. "
                    "No hype. No financial advice. No fake quotes."
                ),
            },
            {"role": "user", "content": build_prompt(book)},
        ],
        response_format={"type": "json_object"},
        temperature=0.45,
    )

    content = response.choices[0].message.content
    if not content:
        raise RuntimeError("OpenAI returned empty content.")
    return json.loads(content)


def yaml_string(value: str) -> str:
    escaped = str(value).replace('"', '\\"')
    return f'"{escaped}"'


def render_markdown(book: Dict[str, Any], plan: Dict[str, Any]) -> str:
    slug = book["slug"]
    canonical = f"{SITE_URL}/books/{slug}/"
    today = date.today().isoformat()

    action_yaml_parts = []
    for action in plan["actions"]:
        action_yaml_parts.append(
            "  - title: " + yaml_string(action["title"]) + "\n"
            "    time_required: " + yaml_string(action["time_required"]) + "\n"
            "    why: " + yaml_string(action["why"]) + "\n"
            "    action: " + yaml_string(action["action"])
        )
    action_yaml = "\n".join(action_yaml_parts)

    key_ideas = "\n".join([f"- {idea}" for idea in plan["key_ideas"]])
    weekly_plan = "\n".join(
        [
            f"- **{item['day']}**: {item['focus']} — {item['action']}"
            for item in plan["weekly_plan"]
        ]
    )

    front_matter = f"""---
layout: book
title: {yaml_string(plan["title"])}
book_title: {yaml_string(book["title"])}
author: {yaml_string(book["author"])}
slug: {yaml_string(slug)}
date: {today}
status: "published"
audience: "Software engineers working towards FIRE"
category: {yaml_string(book.get("category", "Book action plan"))}
tags: [FIRE, engineers, weekly action plan]
session:
  youtube_url: ""
  spotify_url: ""
  duration: "15-20 min"
seo:
  meta_title: {yaml_string(plan["title"])}
  meta_description: {yaml_string(plan["meta_description"])}
  canonical_url: {yaml_string(canonical)}
cta:
  label: "Get the weekly action plan"
  url: "{SITE_URL}?source=book-{slug}"
summary:
  one_line: {yaml_string(plan["one_line"])}
  problem: {yaml_string(plan["problem"])}
  promise: {yaml_string(plan["promise"])}
actions:
{action_yaml}
---
"""

    body = f"""
{plan["intro_markdown"]}

## Key ideas to apply this week

{key_ideas}

## Weekly action plan

{weekly_plan}

{plan["closing_markdown"]}
"""
    return front_matter + body


def update_latest(book: Dict[str, Any], plan: Dict[str, Any]) -> None:
    latest = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "book_title": book["title"],
        "author": book["author"],
        "slug": book["slug"],
        "title": plan["title"],
        "one_line": plan["one_line"],
        "url": f"/books/{book['slug']}/",
    }
    (DATA_DIR / "latest_action_plan.yml").write_text(yaml.safe_dump(latest, sort_keys=False), encoding="utf-8")


def write_report(book: Dict[str, Any], plan: Dict[str, Any]) -> None:
    report = f"""# Weekly Book Action Plan Generated

Generated: {datetime.now(timezone.utc).isoformat()}

## Book

{book['title']} by {book['author']}

## Page

`_books/{book['slug']}.md`

## Summary

{plan['one_line']}

## Manual review checklist

- [ ] The page does not give financial advice.
- [ ] No direct quotes were invented.
- [ ] Actions are practical and specific.
- [ ] CTA points to the Weekly Action Plan Letter.
- [ ] The page renders correctly locally.
"""
    (REPORTS / f"generated-{book['slug']}.md").write_text(report, encoding="utf-8")


def main() -> None:
    book = pick_next_book()
    if not book:
        print("No new enabled books to generate.")
        return

    plan = generate_plan(book)
    output = BOOKS_DIR / f"{book['slug']}.md"
    output.write_text(render_markdown(book, plan), encoding="utf-8")
    update_latest(book, plan)
    write_report(book, plan)

    print(f"Generated {output}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
