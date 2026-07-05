# The Office of 2035 — Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.
> When building or styling the website (Tasks 4–6), also load the `frontend-design` skill first.

**Goal:** Build the interactive 360° "Office of 2035" website (guided tour + free roam, EN/DE, GitHub Pages), the Skybox AI prompt library, and the manifesto essay, per `docs/plans/2026-07-05-office-of-the-future-design.md`.

**Architecture:** Pure static site — no framework, no build step. Pannellum (vendored) renders equirectangular panoramas; all copy lives in `site/content.json`; `site/app.js` drives landing → guided tour → free roam. Placeholder panoramas are generated locally with Pillow so the whole experience works before any AI images exist. Deployment is a GitHub Actions workflow that publishes `site/` to GitHub Pages.

**Tech Stack:** HTML/CSS/vanilla JS, Pannellum 2.5.6, Python 3 + Pillow (placeholder generator only), GitHub Pages via `actions/deploy-pages`.

**Testing approach:** This project has no unit-testable logic worth a JS test harness (YAGNI). Every task instead has explicit verification steps: JSON validity checks, image dimension checks, HTTP smoke tests against `python3 -m http.server`, and browser console checks. Do not skip them.

---

### Task 1: Repo scaffolding

**Files:**
- Create: `README.md`
- Create: `.gitignore`
- Create: `site/`, `panoramas/`, `tools/`, `docs/essay/` directories

**Step 1: Create `.gitignore`**

```gitignore
__pycache__/
*.pyc
.DS_Store
```

**Step 2: Create `README.md`**

```markdown
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
```

**Step 3: Verify and commit**

Run: `ls site panoramas tools docs/essay` → directories exist (git won't track empty dirs; that's fine, files arrive in later tasks).

```bash
git add README.md .gitignore
git commit -m "chore: scaffold repo structure"
```

---

### Task 2: Vendor Pannellum

**Files:**
- Create: `site/vendor/pannellum.js`
- Create: `site/vendor/pannellum.css`

**Step 1: Download Pannellum 2.5.6**

```bash
curl -fsSL -o site/vendor/pannellum.js https://cdn.jsdelivr.net/npm/pannellum@2.5.6/build/pannellum.js
curl -fsSL -o site/vendor/pannellum.css https://cdn.jsdelivr.net/npm/pannellum@2.5.6/build/pannellum.css
```

**Step 2: Verify integrity**

Run: `grep -c "pannellum" site/vendor/pannellum.js && wc -c site/vendor/pannellum.js site/vendor/pannellum.css`
Expected: count > 0; pannellum.js ≈ 55–60 KB (56,249 B verified byte-identical to the official release), pannellum.css ≈ 9–10 KB. If the CDN fails, fall back to `https://github.com/mpetroff/pannellum/releases/download/2.5.6/pannellum-2.5.6.zip` (files are in `build/` inside the zip).

**Step 3: Commit**

```bash
git add site/vendor
git commit -m "chore: vendor Pannellum 2.5.6"
```

---

### Task 3: Placeholder panorama generator

**Files:**
- Create: `tools/make_placeholders.py`
- Create (generated): `site/panos/{approach,hearth,painted-wall,den,loom}.jpg` and `site/panos/{...}-preview.jpg`

**Step 1: Write the generator**

Each placeholder is a 4096×2048 equirectangular JPEG: vertical warm gradient (unique hue per scene), a horizon line, and the scene name repeated 4× around the horizon so it is readable at any yaw. Also emit a 512×256 preview for Pannellum's blur-up `preview` option.

```python
#!/usr/bin/env python3
"""Generate placeholder equirectangular panoramas for the five scenes."""
from PIL import Image, ImageDraw, ImageFont

W, H = 4096, 2048
SCENES = {
    "approach":     ((46, 58, 38),  (168, 154, 118)),  # mossy green -> sand
    "hearth":       ((38, 22, 12),  (196, 120, 60)),   # dark wood -> fire amber
    "painted-wall": ((52, 34, 24),  (178, 140, 96)),   # clay -> ochre
    "den":          ((22, 18, 16),  (92, 70, 56)),     # near-dark -> soft umber
    "loom":         ((30, 26, 34),  (140, 110, 130)),  # dusk -> woven mauve
}

def font(size):
    for path in ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",):
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            pass
    return ImageFont.load_default()

for name, (top, bottom) in SCENES.items():
    img = Image.new("RGB", (W, H))
    px = img.load()
    for y in range(H):
        t = y / (H - 1)
        row = tuple(int(a + (b - a) * t) for a, b in zip(top, bottom))
        for x in range(W):
            px[x, y] = row
    d = ImageDraw.Draw(img)
    d.line([(0, H // 2), (W, H // 2)], fill=(200, 190, 180), width=2)
    label = name.replace("-", " ").upper() + " · PLACEHOLDER"
    f = font(56)  # longest label ~981px, fits the 1024px quarter spacing
    tw = d.textlength(label, font=f)
    for i in range(4):  # readable at any viewing direction
        d.text(((W * i / 4 + W / 8) - tw / 2, H // 2 - 140), label,
               font=f, fill=(255, 245, 230))
    img.save(f"site/panos/{name}.jpg", quality=80)
    img.resize((512, 256)).save(f"site/panos/{name}-preview.jpg", quality=60)
    print(f"site/panos/{name}.jpg")
```

**Step 2: Run it**

```bash
mkdir -p site/panos
pip install pillow 2>/dev/null || pip3 install pillow
python3 tools/make_placeholders.py
```

Expected: five filenames printed, no traceback.

**Step 3: Verify dimensions and count**

Run: `python3 -c "from PIL import Image; import glob; [print(p, Image.open(p).size) for p in sorted(glob.glob('site/panos/*.jpg'))]"`
Expected: 10 files; main panos `(4096, 2048)`, previews `(512, 256)`.

**Step 4: Commit**

```bash
git add tools/make_placeholders.py site/panos
git commit -m "feat: placeholder panorama generator + generated scenes"
```

---

### Task 4: Content model (`content.json`)

**Files:**
- Create: `site/content.json`

**Step 1: Write the content file**

Schema: `meta` (title, thesis line per lang), `ui` (all button/label strings per lang), `scenes[]` in tour order. Each scene: `id`, `pano`, `preview`, `name.{en,de}`, `narration.{en,de}` (2–3 sentences), `hotspots[]` with `pitch`, `yaw`, `title.{en,de}`, `body.{en,de}` (2–4 sentences). DE strings: real German, not placeholders — translate while writing (the language toggle must demo convincingly; a native-polish pass happens in Task 8).

Content requirements (write full copy during execution; honor the design principles — ambient intelligence, no humanoid AI, no screens, warmth):

- **approach** — 3 hotspots: outdoor guest commons / the building that welcomes (door recognizes rhythm of arrival, not faces on screens) / why work starts outside.
- **hearth** — 4 hotspots: the fire-center; acoustic architecture (the room hears mood, softens noise); no reception desk — hosts, not gatekeepers; food & ritual.
- **painted-wall** — 4 hotspots: the wall that draws with you (sketch, speak, it listens and renders); versioned like cave layers (every stratum of an idea preserved); materials — clay & mineral pigment display tech; group rituals for divergence/convergence.
- **den** — 3 hotspots: the womb-like enclosure; information without screens (audio, light temperature, one sheet of e-paper at most); the right to be unreachable as architecture.
- **loom** — 5 hotspots (richest scene): the adaptive surface itself — displays data AND reshapes under your fingers, the anomaly is a dent you feel before you see; working data as a craft (probe, filter, reshape by hand); the Jacquard lineage — the first machine to hold data was a loom, computing began as tactile craft; multi-sensory ingestion (sound, texture, temperature as data channels); why hands beat dashboards (proprioception, memory, group work around a table not a projector).

Hotspot pitch/yaw for placeholders: distribute around the horizon (pitch −5…10, yaws spread ~70° apart, first hotspot at yaw 0 facing the initial view). Refine after real panoramas arrive (Task 9).

**Step 2: Validate JSON**

Run: `python3 -m json.tool site/content.json > /dev/null && echo OK`
Expected: `OK`

**Step 3: Verify completeness**

Run: `python3 -c "
import json; c = json.load(open('site/content.json'))
assert [s['id'] for s in c['scenes']] == ['approach','hearth','painted-wall','den','loom']
for s in c['scenes']:
    assert s['narration']['en'] and s['narration']['de'], s['id']
    assert len(s['hotspots']) >= 3, s['id']
    for h in s['hotspots']:
        assert h['title']['en'] and h['body']['en'] and h['title']['de'] and h['body']['de']
print('content OK,', sum(len(s['hotspots']) for s in c['scenes']), 'hotspots')
"`
Expected: `content OK, 19 hotspots`

**Step 4: Commit**

```bash
git add site/content.json
git commit -m "feat: scene content model with EN/DE copy"
```

---

### Task 5: Page shell (`index.html` + `styles.css`)

**Files:**
- Create: `site/index.html`
- Create: `site/styles.css`

Load the `frontend-design` skill before this task.

**Step 1: Write `index.html`**

Structure (all text injected from `content.json` by `app.js`; elements carry `data-ui` keys):

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>The Office of 2035 — The Listening Cave</title>
  <link rel="stylesheet" href="vendor/pannellum.css">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- Landing -->
  <section id="landing">
    <h1 data-ui="title"></h1>
    <p class="thesis" data-ui="thesis"></p>
    <button id="enter" data-ui="enter"></button>
    <button id="lang-toggle" class="lang"></button>
  </section>

  <!-- Experience -->
  <section id="experience" hidden>
    <div id="viewer"></div>
    <div id="narration" class="card" hidden>
      <h2 id="narration-name"></h2>
      <p id="narration-text"></p>
      <button id="narration-ok" data-ui="lookAround"></button>
    </div>
    <div id="hotspot-card" class="card" hidden>
      <h3 id="hotspot-title"></h3>
      <p id="hotspot-body"></p>
      <button id="hotspot-close" data-ui="close"></button>
    </div>
    <nav id="hud">
      <button id="menu-toggle" data-ui="scenes"></button>
      <span id="scene-label"></span>
      <button id="next-scene" data-ui="continue"></button>
      <button id="lang-toggle-hud" class="lang"></button>
    </nav>
    <div id="menu" hidden><ul id="menu-list"></ul></div>
  </section>

  <script src="vendor/pannellum.js"></script>
  <script src="app.js"></script>
</body>
</html>
```

**Step 2: Write `styles.css`**

Visual language (from design doc): dark, quiet, warm. Background `#14100c`; text warm off-white `#f3ead9`; accent fire-amber `#d98e4a`. Serif display for headings (`Georgia, 'Times New Roman', serif` — no webfonts, keeps it self-contained), system sans for UI. Landing: full-viewport, centered column, generous whitespace, `Enter` as a quiet outlined button. Cards: bottom-centered on desktop (max-width 34rem), full-width bottom sheet on mobile; soft 0.35s fade/rise transition. HUD: single slim bar, semi-transparent, bottom of screen; never overlaps Pannellum's own controls. Custom hotspot style: a slow-pulsing warm ember dot (CSS class `hotspot-ember`, ~18px, radial gradient, `animation: pulse 3s infinite`). Respect `prefers-reduced-motion` (disable pulse/auto-fade). Focus-visible outlines on all interactive elements.

**Step 3: Verify shell serves**

```bash
python3 -m http.server 8080 --directory site &
sleep 1
curl -fsS http://localhost:8080/ | grep -c 'id="viewer"'
curl -fsS -o /dev/null -w "%{http_code}\n" http://localhost:8080/styles.css
```

Expected: `1` and `200`. Leave the server running for Task 6.

**Step 4: Commit**

```bash
git add site/index.html site/styles.css
git commit -m "feat: page shell and warm-dark visual system"
```

---

### Task 6: Experience logic (`app.js`)

**Files:**
- Create: `site/app.js`

**Step 1: Write `app.js`**

Single IIFE, no dependencies beyond the global `pannellum`. Responsibilities:

1. `fetch('content.json')` → build state `{ lang: 'en', mode: 'tour', index: 0, content }`. Default lang from `navigator.language.startsWith('de') ? 'de' : 'en'`.
2. **Pannellum init:** one viewer via `pannellum.viewer('viewer', { default: {...}, scenes: {...} })` built from content. Per scene: `type: 'equirectangular'`, `panorama`, `preview`, `autoLoad: true`, `autoRotate: -2` (slow pan; Pannellum stops it on user drag), `hfov: 100`, `compass: false`, and `hotSpots` with `cssClass: 'hotspot-ember'`, `clickHandlerFunc` opening the hotspot card for `(sceneId, hotspotIndex)`.
3. **Landing:** populate title/thesis/buttons; `Enter` hides `#landing`, shows `#experience`, calls `showScene(0)`.
4. `showScene(i)`: `viewer.loadScene(scenes[i].id)`; show narration card (name + narration in current lang); `Continue` button label switches to "Finish" (`ui.finish`) on the last scene; update `#scene-label` ("2 / 5 · The Hearth"); rebuild is not needed — cards read from state.
5. **Narration card:** `Look around` dismisses it. `Continue` in HUD advances `showScene(i+1)`; on last scene it opens the menu with a closing line (`ui.outro`) instead.
6. **Hotspot card:** exclusive with narration card (opening one hides the other); `Close` hides it.
7. **Menu (free roam):** list of scene names in current lang; click → `showScene(i)` and `mode='roam'` (roam mode never auto-shows narration again once a scene was visited; keep a `visited` Set).
8. **Language toggle:** flips `state.lang`, re-applies every `data-ui` string, narration card, hotspot card (if open), menu list, scene label, and both toggle buttons' labels (`EN`/`DE` shows the *other* language as the label). Hotspot tooltips: pass `createTooltipFunc` that renders from state so language flips affect them on next open (documented limitation: Pannellum tooltip text is set at creation; use tooltip-less ember dots and rely on the card, so nothing stale is shown).
9. **Keyboard:** `→`/`Space` = continue, `Esc` closes cards/menu, `m` toggles menu.
10. **Audio layer (added):** a `#sound-toggle` button in the HUD (add to `index.html`; label from `ui.soundOn`/`ui.soundOff` — add both keys to `content.json` EN/DE). Scenes may declare optional `audio: { narration: {en, de}, ambience: "audio/<id>-ambience.mp3" }` paths in `content.json`. On scene enter, if sound is on: play the narration clip for the current language (one shared `<audio>` element, `preload="none"`); start/crossfade the ambience loop (second `<audio>`, `loop`, volume 0.25). Missing files or missing `audio` keys must degrade silently (catch play() rejections, `onerror` → ignore). Sound defaults ON (the Enter click is the required user gesture); toggling off pauses both elements immediately. Language switch mid-scene: stop narration, don't replay automatically.

**Step 2: Smoke-test over HTTP**

With the Task 5 server still running:

```bash
curl -fsS -o /dev/null -w "%{http_code}\n" http://localhost:8080/app.js
curl -fsS -o /dev/null -w "%{http_code}\n" http://localhost:8080/panos/hearth.jpg
node --check site/app.js && echo SYNTAX-OK   # if node absent: python3 -c "import subprocess" && skip
```

Expected: `200`, `200`, `SYNTAX-OK`.

**Step 3: Browser verification (manual or scripted)**

Open http://localhost:8080 in a real browser. Checklist — every item must pass:

- [ ] Landing shows title + thesis, Enter works
- [ ] Scene 1 loads, slow auto-pan, drag stops it
- [ ] Narration card appears per scene; Continue advances through all 5; Finish behavior on scene 5
- [ ] Ember hotspots visible; click opens card; Esc/Close dismisses
- [ ] Menu jumps to any scene; revisited scenes skip narration
- [ ] DE toggle flips every visible string (landing, cards, HUD, menu)
- [ ] No console errors
- [ ] Narrow window (~375px): cards become bottom sheets, HUD usable

If a headless browser is available (`npx playwright --version` works), automate: load page, click Enter, assert `.pnlm-container` exists and console is clean. Otherwise report the manual checklist to the partner.

**Step 4: Commit**

```bash
git add site/app.js
git commit -m "feat: guided tour, free roam, hotspots, EN/DE toggle"
```

---

### Task 6b: Voiceover pipeline (ElevenLabs)

**Files:**
- Create: `tools/make_voiceovers.py`
- Create (when key available): `site/audio/<scene>-<lang>.mp3` (10 clips), optionally `landing-<lang>.mp3`, `outro-<lang>.mp3`

**Step 1: Write `tools/make_voiceovers.py`**

Reads narrations (and meta.thesis, ui.outro) from `site/content.json`; calls the ElevenLabs TTS API (`eleven_multilingual_v2`, one warm narrator voice for both languages, voice ID configurable at top of script); writes MP3s to `site/audio/`. Requires `ELEVENLABS_API_KEY` env var — if absent, print clear instructions and exit 0 (pipeline is "prepared", not failing). Use `requests` (or stdlib `urllib`) — no SDK dependency. `--only <scene-id>` flag for regenerating a single clip. Print each written file + size.

**Step 2: Update `site/content.json`** — add `audio.narration.{en,de}` paths to all five scenes (paths may not exist yet; app.js degrades silently) and `ui.soundOn`/`ui.soundOff` strings.

**Step 3: Verify** — without a key: script exits 0 with instructions. With a key: 10 MP3s in `site/audio/`, each < 1 MB, spot-listen one per language.

**Step 4: Commit** — `feat: ElevenLabs voiceover pipeline` (+ generated clips if key was available).

**Licensing note:** ElevenLabs free tier is non-commercial; partner needs Starter tier or above for this client-facing deliverable.

**Ambience (optional, non-blocking):** CC0 loops (fire crackle for hearth, outdoor birdsong for approach, soft room tone elsewhere) may be added later as `site/audio/<id>-ambience.mp3` + `audio.ambience` keys; player support ships in Task 6.

---

### Task 7: Skybox AI prompt library

**Files:**
- Create: `panoramas/prompts.md`

**Step 1: Write the prompt library**

For each of the five scenes: a title, the Skybox AI style preset recommendation (e.g. "Interior Views" / "Advanced (no preset)"), a main prompt (~80–120 words, concrete nouns, lighting, materials, camera position), and a negative prompt. Shared visual language block at the top, referenced by all scenes:

- Curved earthen/clay surfaces, warm wood, woven textiles, daylight shafts, fire-toned indirect light, morning light
- **Always exclude:** people, humanoid figures, robots, avatars, faces, visible screens/monitors/keyboards, holograms, blue LED / neon / sci-fi lighting, glass-and-steel corporate lobby aesthetics, text/logos
- Camera at standing eye height, center of room

Also include a short workflow section: generate at highest available resolution → download equirectangular JPG → drop into `site/panos/<id>.jpg` (same filename), regenerate preview via `python3 tools/make_placeholders.py` — **amend the script first** so it derives previews from existing files rather than overwriting real panoramas (add `--previews-only` flag in this task: if `--previews-only`, load each existing `site/panos/<id>.jpg` and only write `-preview.jpg`).

**Step 2: Amend `tools/make_placeholders.py` with `--previews-only`**

```python
import sys
PREVIEWS_ONLY = "--previews-only" in sys.argv
# in the loop:
#   if PREVIEWS_ONLY: img = Image.open(f"site/panos/{name}.jpg")
#   else: (existing generation code)
```

**Step 3: Verify**

Run: `python3 tools/make_placeholders.py --previews-only && python3 -c "from PIL import Image; print(Image.open('site/panos/loom-preview.jpg').size)"`
Expected: `(512, 256)`, main panos untouched (`git status` shows only previews if anything).

**Step 4: Commit**

```bash
git add panoramas/prompts.md tools/make_placeholders.py site/panos
git commit -m "feat: Skybox AI prompt library + previews-only regeneration"
```

---

### Task 8: The essay (EN, then DE)

**Files:**
- Create: `docs/essay/the-listening-cave-en.md`
- Create: `docs/essay/the-listening-cave-de.md` (after EN is approved)

**Step 1: Write the English essay**

Structure and budgets (total ~4,500–6,000 words ≈ 8–12 pages):

1. **Lascaux, 17,000 BC** (~400 w) — the first shared workspace; the wall as memory, teaching, ritual. Pivot: we are going back, but this time the wall listens.
2. **The wrong future** (~500 w) — glass towers, hologram receptionists, humanoid assistants, dashboard walls: why "more screens" extrapolates the past instead of imagining the future; the uncanny valley as a design dead end; the real trajectory of technology is disappearance (cite: calm computing, ubiquitous computing lineage).
3. **The Approach** (~500 w) · 4. **The Hearth** (~600 w) · 5. **The Painted Wall** (~700 w) · 6. **The Den** (~500 w) · 7. **The Loom** (~900 w, the centerpiece) — each chapter: opens with a second-person scene ("You arrive and…"), unpacks what work happens here / what invisible technology enables it / what it replaces; ends with a link to the matching 360° scene. The Loom chapter carries the haptic-data argument and Jacquard lineage in full.
4. **What this means for leaders** (~600 w) — 2035 is one office-lease cycle away; three questions (real estate, tools, rituals); conversation-starter close, no pitch.

Anchor claims to real trajectories: Weiser's calm computing, MIT inFORM/Materiable, Ultraleap mid-air haptics, electrostatic surface haptics, spatial audio, ambient LLMs. No vendor names in the vision chapters — research lineages only.

**Step 2: Verify against design principles**

Run: `grep -inE "robot|avatar|humanoid|hologram|assistant" docs/essay/the-listening-cave-en.md`
Expected: matches only inside "The wrong future" chapter (where they are being rejected). Read the essay once top-to-bottom checking: every chapter ends with a scene link; no vendor names in chapters 3–7; second-person scene openers present.

**Step 3: Commit; DE translation after partner approves EN**

```bash
git add docs/essay/the-listening-cave-en.md
git commit -m "feat: vision essay (EN)"
```

DE translation is a separate commit after review: `feat: vision essay (DE)`.

**Also in the DE polish pass (carried from Task 4 review, content.json):** confirm with partner the generic feminine forms ("einer Kollegin", "eine Moderatorin"); consider "die Ihre Hände durchwandern können" for the loom narration ("abschreiten"); conscious sign-off on the two borderline personifications ("wie ein guter Lehrling", den's "Eine Stimme liest…" → safer: "Der Raum liest…").

---

### Task 9: Real panoramas integration (partner-gated)

**Blocked on:** partner generating scenes in Skybox AI using `panoramas/prompts.md`.

**Steps per delivered scene:** save as `site/panos/<id>.jpg` (target ≤ 2.5 MB; if larger: `python3 -c` Pillow resave at `quality=82`, or convert to WebP and update `content.json` paths) → `python3 tools/make_placeholders.py --previews-only` → open the scene in the browser and adjust that scene's hotspot `pitch`/`yaw` in `content.json` so embers sit on the objects they describe → re-run Task 4 Step 3 validation → commit per scene: `feat: real panorama for <id>`.

---

### Task 10: GitHub Pages deployment

**Files:**
- Create: `.github/workflows/deploy.yml`

**Step 1: Write the workflow**

```yaml
name: Deploy site to GitHub Pages
on:
  push:
    branches: [main]
  workflow_dispatch:
permissions:
  contents: read
  pages: write
  id-token: write
concurrency:
  group: pages
  cancel-in-progress: true
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - uses: actions/checkout@v4
      - uses: actions/configure-pages@v5
      - uses: actions/upload-pages-artifact@v3
        with:
          path: site
      - id: deployment
        uses: actions/deploy-pages@v4
```

**Step 2: Verify YAML**

Run: `python3 -c "import yaml,sys; yaml.safe_load(open('.github/workflows/deploy.yml')); print('YAML OK')"`
(If PyYAML missing: `pip install pyyaml`.)
Expected: `YAML OK`

**Step 3: Commit**

```bash
git add .github/workflows/deploy.yml
git commit -m "ci: deploy site/ to GitHub Pages"
```

**Step 4: Repo/Pages state (updated 2026-07-05)**

Repo exists: `https://github.com/AlexHacksAround/FutureOfWork` (remote `origin`, pushed). Partner already enabled Pages with custom domain **futureofwork.byatw.com** (cert approved), but `build_type` is `legacy` (branch `main`, path `/`) — wrong for our `site/` layout. In this task, after committing the workflow: switch to workflow deployment and enforce HTTPS via `gh api -X PUT repos/AlexHacksAround/FutureOfWork/pages -f build_type=workflow -F https_enforced=true`, then push and verify the Actions run deploys and `https://futureofwork.byatw.com/` serves the site. All site URLs are relative, which works at a domain root too.
Task order note: Task 10 is pulled forward to run right after Task 6, so every subsequent push is visible live.

---

### Task 11: Final verification

- Re-run every verification step from Tasks 4–7 and the full Task 6 Step 3 browser checklist.
- `du -sh site/` — total payload sane (placeholders: ~a few MB; real panos: < 15 MB).
- Load the deployed GitHub Pages URL on a phone: gyroscope look-around works (needs HTTPS — Pages provides it), cards usable.
- Partner walkthrough → collect copy edits → final commit.
