#!/usr/bin/env python3
from pathlib import Path
import re, sys
books = Path(__file__).resolve().parents[1] / '_books'
req = ['title:', 'book_title:', 'author:', 'slug:', 'seo:', 'cta:', 'summary:', 'actions:']
bad = False
for p in books.glob('*.md'):
    txt = p.read_text(encoding='utf-8')
    m = re.match(r"---\n(.*?)\n---", txt, re.S)
    fm = m.group(1) if m else ''
    miss = [r for r in req if r not in fm]
    print(('OK: ' if not miss else 'Missing: ') + str(p) + ((' ' + ','.join(miss)) if miss else ''))
    bad = bad or bool(miss)
sys.exit(1 if bad else 0)
