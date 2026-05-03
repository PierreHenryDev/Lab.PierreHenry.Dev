#!/usr/bin/env python3
import argparse,re
from datetime import date
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
BOOKS=ROOT/'_books'
def slugify(v): return re.sub(r'[^a-z0-9]+','-',v.lower()).strip('-')
parser=argparse.ArgumentParser()
parser.add_argument('--title', required=True)
parser.add_argument('--author', required=True)
parser.add_argument('--category', default='Book actions')
a=parser.parse_args()
slug=slugify(a.title)
out=BOOKS/f'{slug}.md'
if out.exists(): raise SystemExit(f'File exists: {out}')
content = f"""---
layout: book
title: "{a.title} for Engineers Working Towards FIRE"
book_title: "{a.title}"
author: "{a.author}"
slug: "{slug}"
date: {date.today().isoformat()}
status: "draft"
audience: "Engineers working towards FIRE"
category: "{a.category}"
tags: [FIRE, engineers, book actions]
session:
  youtube_url: ""
  spotify_url: ""
  duration: "15-20 min"
seo:
  meta_title: "{a.title} for Engineers Working Towards FIRE"
  meta_description: "Three practical ideas and actions from {a.title} for engineers working towards FIRE."
  canonical_url: "https://lab.pierrehenry.dev/books/{slug}/"
cta:
  label: "Get one daily book-based action"
  url: "https://lab.pierrehenry.dev?source=book-{slug}"
summary:
  one_line: "Write one clear sentence about why this book matters."
  problem: "Write the specific problem this book helps solve."
  promise: "This guide turns the book into practical actions."
actions:
  - title: "Action title"
    time_required: "5 minutes"
    why: "Why this matters."
    action: "What to do."
---

## Why this book matters

Write here.

## 3 useful ideas

### 1. Idea one

**Action:** Action to apply.
"""
out.write_text(content, encoding='utf-8')
print(out)
