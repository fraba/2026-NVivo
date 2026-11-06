# Practice data: #SydneyRent (synthetic)

86 short social media posts by 19 fictional users on housing and renting in NSW
(March–May 2026). Used in **both** sessions. **All synthetic**, written for the workshop.

- `corpus.json`: the source (users, attributes, posts). Edit this.
- `build_corpus.py`: builds `nvivo-practice-data/` and `nvivo-practice-data.zip`:
  - `posts/<handle>.docx`: one file per user = one case (Heading 1 = user, Heading 2 = post),
    so autocoding by paragraph style works (Ch. 19)
  - `users.xlsx`: classification sheet (Name = file name; Gender, Age group, Tenure, Location)
  - `all_posts.xlsx`: one row per post
  - `README.txt`: instructions for participants

```sh
python3 -m venv /tmp/nvivoenv && /tmp/nvivoenv/bin/pip install python-docx openpyxl
/tmp/nvivoenv/bin/python data/build_corpus.py
```

Design: themes deliberately vary by attribute so matrix queries show something:
- rent rises, competition and insecurity (renters)
- costs and feeling blamed (landlords)
- the intergenerational divide, both sides (65+ owners vs young renters, with a 65+ renter as a counter-case)
- city to regions spillover (Regional NSW)
- blame on investors, government, planning/NIMBYs, immigration (contested, civil), agents
- family help (bank of mum and dad, living at home)
- community and belonging
- @-replies link users (e.g. retired_ray and priya_in_parra, investor_ian and nursenat_westie, hugh_property_tips and housing_now_kate)

Research question used in the slides: *How do people in NSW make sense of the housing
crisis: what do they experience, and whom do they blame?*

For practice after the workshop, NVivo's built-in **Multi-method** sample project is the one
used throughout Mortelmans (2025).

Never commit real participant data or NVivo project files (`.nvp`, `.nvpx`).
