---
layout: default
title: "Book Action Library"
description: "Weekly action plans from powerful books for software engineers working towards FIRE."
seo:
  meta_title: "Book Action Library | Weekly Action Plans From Powerful Books"
  meta_description: "Browse practical action plans from books on finance, wealth, self-improvement, habits, focus and early retirement."
permalink: /books/
---

<section class="page">
  <div class="container">
    <p class="eyebrow">Book Action Library</p>
    <h1>Powerful books turned into weekly action plans.</h1>
    <p class="lead">
      Built for software engineers who want better money decisions, stronger habits, clearer focus and progress towards FIRE.
      No long summaries. No theory collection. Just practical plans you can apply.
    </p>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="three-grid">
      {% assign sorted_books = site.books | sort: 'date' | reverse %}
      {% for book in sorted_books %}
        <a class="book-tile" href="{{ book.url | relative_url }}">
          <p class="tile-kicker">{{ book.category }}</p>
          <h2>{{ book.book_title }}</h2>
          <p>{{ book.summary.one_line }}</p>

          <div class="tile-meta">
            <span>{{ book.author }}</span>
            <span>{{ book.actions.size }} actions</span>
          </div>

          <span class="read-more">View action plan →</span>
        </a>
      {% endfor %}
    </div>
  </div>
</section>
