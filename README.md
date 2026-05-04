# Your Success is Closer Than You Think™

GitHub Pages-ready Jekyll site with a landing page and Markdown-first Book Action Library.

## What this is

- Landing page for the MailerLite newsletter
- `/books/` index
- One Markdown file per book in `_books/`
- YAML front matter for SEO, CTA tracking, and notes
- Source tracking via MailerLite hidden fields

## Python setup

Use a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Windows:

```bash
venv\Scripts\activate
```

## Add a new book

```bash
python3 scripts/new_book_action.py --title "Deep Work" --author "Cal Newport" --category "Focus and career leverage"
```

Then edit:

```text
_books/deep-work.md
```

## MailerLite tracking

Forms live in:

```text
_includes/email-capture.html
_includes/email-capture-inline.html
```

Keep this hidden field:

```html
<input type="hidden" name="fields[signup_source]" id="{{ capture_id }}Source" value="{{ source }}">
```

Use tracked links:

```text
https://lab.pierrehenry.dev?source=linkedin-fire-001
```

The JavaScript stores the `source` value in MailerLite as:

```text
signup_source
```

Fallback values include:

```text
homepage-hero
homepage-bottom
book slug
```

## GitHub Pages

`CNAME`:

```text
lab.pierrehenry.dev
```

Use GitHub Actions as the Pages source.

## Brand

```text
Font: Inter
Primary: #1F6F4A
Secondary: #C8A45D
Heading: #111827
Text: #4B5563
Border: #E5E7EB
Background: #FAF7F0
```

## Article capture

Each book article includes:

```text
Top capture block
Bottom capture block
Sticky sidebar CTA
```

## Author

[![Pierre-Henry Soria](https://avatars0.githubusercontent.com/u/1325411?s=200)](https://ph7.me "Pierre-Henry Soria, Software Developer")

Made with ❤️ by **[Pierre-Henry Soria](https://pierrehenry.be)**. A super passionate & enthusiastic AI Product Engineer. Also a true cheese 🧀, ristretto ☕️, and dark chocolate lover! 😋


[![@phenrysay](https://img.shields.io/badge/x-000000?style=for-the-badge&logo=x)](https://x.com/phenrysay) [![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/pH-7) [![BlueSky](https://img.shields.io/badge/BlueSky-00A8E8?style=for-the-badge&logo=bluesky&logoColor=white)](https://bsky.app/profile/pierrehenry.dev) [![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@pH7Programming)