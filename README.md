# Your Success is Closer Than You Think™

GitHub Pages-ready Jekyll site with a landing page and Markdown-first Book Action Library.

## What this is

- Landing page for the MailerLite newsletter
- `/books/` library index
- one Markdown file per book in `_books/`
- YAML front matter for SEO, CTA tracking, raw notes and automation
- source tracking for MailerLite hidden fields

## Add a new book

```bash
python3 scripts/new_book_action.py --title "Deep Work" --author "Cal Newport" --category "Focus and career leverage"
```

Then edit `_books/deep-work.md`.

## MailerLite

Replace the placeholder form in `index.html` with your MailerLite embed. Keep this hidden field if possible:

```html
<input type="hidden" name="fields[source]" id="sourceField">
```

Use tracked links like:

```text
https://lab.pierrehenry.dev?source=linkedin-fire-001
```

## GitHub Pages

The `CNAME` file is already set to:

```text
lab.pierrehenry.dev
```

Use GitHub Actions as the Pages source.

## Brand colours

- Inter
- #1F6F4A
- #C8A45D
- #111827
- #4B5563
- #E5E7EB
- #FAF7F0


## Article email capture blocks

Each book article now includes newsletter capture blocks:

- one near the top of the article
- one at the bottom of the article
- one sticky sidebar CTA that jumps to the bottom capture form

The capture block lives in:

```text
_includes/email-capture.html
```

To connect MailerLite, replace the placeholder form inside the include with your MailerLite embedded form HTML.

Recommended hidden field:

```html
<input type="hidden" name="fields[source]" id="sourceField">
```

The JavaScript will fill that field from the URL parameter:

```text
?source=linkedin-fire-001
```

If no URL source exists, the book slug is used as the local fallback source.
