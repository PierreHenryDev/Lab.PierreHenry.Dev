# Your Success is Closer Than You Think™

GitHub Pages-ready Jekyll site with a landing page and Markdown-first Book Action Library.

## What this is

- Landing page for the MailerLite newsletter
- `/books/` library index
- one Markdown file per book in `_books/`
- YAML front matter for SEO, CTA tracking, raw notes and automation
- source tracking for MailerLite hidden fields

## Python setup (one-time)

From Python 3.11 onwards, many macOS and Linux systems restrict global `pip install` in system-managed environments ([PEP 668](https://peps.python.org/pep-0668/)). Use a **virtual environment** to install dependencies in an isolated project sandbox.

```bash
python3 -m venv venv
source venv/bin/activate
```

> **Windows:** use `venv\Scripts\activate`

Install dependencies if needed:

```bash
pip install -r requirements.txt
```

> Activate the environment each time you open a new terminal before running scripts.

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

## Author

[![Pierre-Henry Soria](https://avatars0.githubusercontent.com/u/1325411?s=200)](https://ph7.me "Pierre-Henry Soria, Software Developer")

Made with ❤️ by **[Pierre-Henry Soria](https://pierrehenry.be)**. A super passionate & enthusiastic problem-solver engineer. Also a true cheese 🧀, ristretto ☕️, and dark chocolate lover! 😋

[![@phenrysay](https://img.shields.io/badge/x-000000?style=for-the-badge&logo=x)](https://x.com/phenrysay "Follow Me on X") [![pH-7](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/pH-7 "My GitHub") [![BlueSky](https://img.shields.io/badge/BlueSky-00A8E8?style=for-the-badge&logo=bluesky&logoColor=white)](https://bsky.app/profile/pierrehenry.dev "Follow Me on BlueSky") [![YouTube Video](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@pH7Programming "My Channel, NextGen Dev: AI & Code")
