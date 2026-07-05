# The Office of 2035 — The Listening Cave

A consulting thought-leadership project in three parts:

- **`site/`** — an interactive 360° website where visitors explore the office
  of 2035 (guided tour or free roam, EN/DE). Pure static site, no build step.
- **`docs/essay/`** — the manifesto-style vision essay.
- **`panoramas/prompts.md`** — the Skybox AI prompt library used to generate
  the 360° scenes.

## Run locally

    python3 -m http.server 8080 --directory site

Open http://localhost:8080

## Regenerate placeholder panoramas

    pip install pillow
    python3 tools/make_placeholders.py

## Deploy

Pushing to `main` deploys `site/` to GitHub Pages via
`.github/workflows/deploy.yml` (enable Pages → Source: GitHub Actions in repo
settings, one time).

Design: `docs/plans/2026-07-05-office-of-the-future-design.md`
