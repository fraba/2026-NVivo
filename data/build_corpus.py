"""Build the NVivo practice dataset from corpus.json.

Outputs (in data/nvivo-practice-data/, zipped to data/nvivo-practice-data.zip):
  posts/<handle>.docx  one file per user = one case; Heading 1 = user, Heading 2 = post date
                       (the heading styles allow autocoding by paragraph style, Mortelmans Ch. 19)
  users.xlsx           classification sheet: column 1 = case name (matches file name), then attributes
  all_posts.xlsx       one row per post with user attributes (dataset import, Ch. 18)
  README.txt           instructions for participants

Needs python-docx and openpyxl:
  python3 -m venv /tmp/nvivoenv && /tmp/nvivoenv/bin/pip install python-docx openpyxl
  /tmp/nvivoenv/bin/python data/build_corpus.py
"""

import json
import shutil
from datetime import date
from pathlib import Path

from docx import Document
from openpyxl import Workbook
from openpyxl.styles import Font

HERE = Path(__file__).resolve().parent
OUT = HERE / "nvivo-practice-data"
ATTRS = [("gender", "Gender"), ("age_group", "Age group"), ("tenure", "Tenure"), ("location", "Location")]


def nice_date(iso):
    return date.fromisoformat(iso).strftime("%-d %B %Y")


def write_posts(corpus):
    (OUT / "posts").mkdir(parents=True)
    for u in corpus["users"]:
        doc = Document()
        doc.add_heading(f"@{u['handle']}", level=1)
        doc.add_paragraph(f"Bio: {u['bio']}")
        for i, p in enumerate(u["posts"], 1):
            doc.add_heading(f"Post {i}, {nice_date(p['date'])}", level=2)
            doc.add_paragraph(p["text"])
        doc.save(OUT / "posts" / f"{u['handle']}.docx")


def write_sheet(path, header, rows):
    wb = Workbook()
    ws = wb.active
    ws.append(header)
    for c in ws[1]:
        c.font = Font(bold=True)
    for r in rows:
        ws.append(r)
    for col in ws.columns:
        width = max(len(str(c.value)) for c in col)
        ws.column_dimensions[col[0].column_letter].width = min(width + 2, 80)
    wb.save(path)


def write_readme(corpus):
    n_posts = sum(len(u["posts"]) for u in corpus["users"])
    text = f"""{corpus['title']}

{corpus['note']}

Contents
--------
posts/       {len(corpus['users'])} Word files, one per user ({n_posts} posts, March-May 2026).
             Each file = one case. Posts are separated by 'Heading 2' lines.
users.xlsx   Classification sheet: one row per user (case) with Gender, Age group,
             Tenure and Location. The first column matches the file names.
all_posts.xlsx  All posts in one table (one row per post), for exploring outside NVivo.

Session 1: Import > Files > select everything in posts/ (tick "Create a case for
each imported file" if you want to save a step for Session 2).
Session 2: Import > Classification Sheets > users.xlsx (case classification).
"""
    (OUT / "README.txt").write_text(text)


def main():
    corpus = json.loads((HERE / "corpus.json").read_text())
    if OUT.exists():
        shutil.rmtree(OUT)
    write_posts(corpus)
    users = corpus["users"]
    write_sheet(OUT / "users.xlsx", ["Name"] + [h for _, h in ATTRS],
                [[u["handle"]] + [u[k] for k, _ in ATTRS] for u in users])
    write_sheet(OUT / "all_posts.xlsx", ["Handle", "Post", "Date", "Text"] + [h for _, h in ATTRS],
                [[u["handle"], i, p["date"], p["text"]] + [u[k] for k, _ in ATTRS]
                 for u in users for i, p in enumerate(u["posts"], 1)])
    write_readme(corpus)
    shutil.make_archive(str(OUT), "zip", OUT.parent, OUT.name)
    print(f"Wrote {OUT} and {OUT}.zip")


if __name__ == "__main__":
    main()
