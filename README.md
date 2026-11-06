# NVivo for HDR researchers (2026)

Two NVivo training sessions for HDR students, Graduate Research School, University of Sydney.
Monday 9 November 2026. Organised by Francesco Bailo with the Graduate Research School (Yulia Ulyannikova); delivered by Takwa Tissaoui, Alicia Wang and Raka Pamungkas.

| Deck | Time | Focus |
|---|---|---|
| [session-1.qmd](session-1.qmd) | 10:00–11:30 | From data to codes |
| [session-2.qmd](session-2.qmd) | 12:30–14:00 | From codes to analysis |

Both decks follow Mortelmans, D. (2025). *Doing Qualitative Data Analysis with NVivo*. Springer.
Open access: <https://doi.org/10.1007/978-3-031-66014-6>.

## Mapping to the book

Mortelmans (2025) chapters (checked against the full book, `978-3-031-66014-6.pdf`):

| Block | Session | Chapter |
|---|---|---|
| What NVivo can (not) do; code-and-retrieve | 1 | Ch. 2 Guided Tour in QDA, Ch. 3 Quick Tour of NVivo |
| Install, licence, user profile, updates, Win vs Mac | 1 | Ch. 4 Getting Started 1: Installing and Configuring |
| Workspace and jargon | 1 | Ch. 5 Getting Started 2: The Workspace and Jargon |
| Project file, backups, folders, importing, transcription | 1 | Ch. 6 Setting Up Your Project: Primary Data Management |
| Memos vs annotations | 1 | Ch. 7 Working with Memos |
| Coding: deductive/inductive, methods, stripes, hierarchies, aggregate, in vivo | 1 | Ch. 8 Thematic Coding |
| Merge, split, uncode | 2 | Ch. 8 Thematic Coding |
| Cases and classifications | 2 | Ch. 9 Coding with Classifications |
| The eight queries, matrix and crosstab, coding comparison | 2 | Ch. 12 Querying (Coded) Data |
| Explore and comparison diagrams, framework matrix; maps | 2 | Ch. 10 Exploring Coded Data; Ch. 13 Visualising Data with Maps |
| Semi-automatic and AI autocoding | 2 | Ch. 19 NVivo and AI |
| Teams | 2 | Ch. 20 Using NVivo in Team Projects |
| Reports, extracts, REFI-QDA | 2 | Ch. 14 Reporting and Exporting Data |

Not covered (pointed to on the final slide): Ch. 11 secondary data management, 15 focus groups,
16 multimedia, 17 social media, 18 mixed methods, 21 literature reviews.

Practice data: **#SydneyRent**, 86 synthetic social media posts by 19 users with attributes, used in both sessions. Built by `data/build_corpus.py`; share `data/nvivo-practice-data.zip` (see `data/README.md`).

## Rendering

```r
install.packages("countdown")
```

```sh
quarto render session-1.qmd
quarto render session-2.qmd
```

The theme in `assets/` is copied from the GOVT6139 slides.

## Emails

`emails/`: drafts sent to participants (e.g. the pre-install email).

NVivo project files (`.nvp`, `.nvpx`) are git-ignored.
