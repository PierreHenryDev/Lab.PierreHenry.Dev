# Your Success is Closer Than You Think™

GitHub Pages-ready Jekyll site with a landing page and Markdown-first Book Action Library.

## What this is

- Landing page for the MailerLite newsletter
- `/books/` index
- One Markdown file per book in `_books/`
- YAML front matter for SEO, CTA tracking, and notes
- Source tracking via MailerLite hidden fields

## Python setup (one-time)

From Python 3.11 onwards, many macOS and Linux systems restrict global `pip install` in system-managed environments ([PEP 668](https://peps.python.org/pep-0668/)). Use a **virtual environment** to install dependencies in an isolated project sandbox.

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

> **Windows:** `venv\Scripts\activate`
> Activate the environment each time you open a new terminal.

## Add a new book

```bash
python3 scripts/new_book_action.py --title "Deep Work" --author "Cal Newport" --category "Focus and career leverage"
```

Then edit `_books/deep-work.md`.

## MailerLite

Replace the placeholder form in `index.html` with your embed. Keep this hidden field:

```html
<input type="hidden" name="fields[source]" id="sourceField">
```

Use tracked links:

```text
https://lab.pierrehenry.dev?source=linkedin-fire-001
```

## GitHub Pages

`CNAME` is set to:

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

## Article email capture

Each article includes:

- Top capture block  
- Bottom capture block  
- Sticky sidebar CTA  

Located in:

```text
_includes/email-capture.html
```

Replace the form with your MailerLite embed.

Hidden field:

```html
<input type="hidden" name="fields[source]" id="sourceField">
```

The script fills it from:

```text
?source=linkedin-fire-001
```

Fallback: book slug.

## Author

[![Pierre-Henry Soria](https://avatars0.githubusercontent.com/u/1325411?s=200)](https://ph7.me "Pierre-Henry Soria, Software Developer")

Made with ❤️ by **[Pierre-Henry Soria](https://pierrehenry.be)**

[![@phenrysay](https://img.shields.io/badge/x-000000?style=for-the-badge&logo=x)](https://x.com/phenrysay)
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/pH-7)
[![BlueSky](https://img.shields.io/badge/BlueSky-00A8E8?style=for-the-badge&logo=bluesky&logoColor=white)](https://bsky.app/profile/pierrehenry.dev)
[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@pH7Programming)
