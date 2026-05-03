---
layout: default
title: "Book Action Library"
description: "Book-based action guides for engineers working towards FIRE."
seo:
  meta_title: "Book Action Library | Book-Based Actions for Engineers Working Towards FIRE"
  meta_description: "Browse practical book-action guides that turn money, productivity, career and investing books into daily actions for engineers working towards FIRE."
permalink: /books/
---
<section class="page"><div class="container"><p class="eyebrow">Book Action Library</p><h1>Books turned into actions for engineers working towards FIRE.</h1><p class="lead">Each guide gives useful ideas, practical actions, and the next step from one book. No long summaries. No theory collection.</p></div></section><section class="section"><div class="container"><div class="grid">{% assign sorted_books = site.books | sort: 'date' | reverse %}{% for book in sorted_books %}<a class="tile" href="{{ book.url | relative_url }}"><p class="eyebrow">{{ book.category }}</p><h2>{{ book.book_title }}</h2><p>{{ book.summary.one_line }}</p><div class="pills"><span>{{ book.author }}</span><span>{{ book.actions.size }} actions</span></div></a>{% endfor %}</div></div></section>
