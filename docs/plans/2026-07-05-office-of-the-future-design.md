# The Office of 2035 — Design Document

**Date:** 2026-07-05
**Status:** Validated with partner
**Working title:** "The Listening Cave — The Office of 2035" (name still open)

## Purpose

A consulting thought-leadership deliverable in two connected parts, aimed at company
leadership, showcasing workplace/organization design expertise. Goal: start
conversations, build credibility. No sales pitch inside the deliverable.

1. **Vision essay** — manifesto-style, 8–12 pages, English first, German later.
2. **Interactive 360° website** — visitors explore the office of 2035 through
   AI-generated panoramas. Hosted on GitHub Pages.

## Thesis

We are going back to cave painting — except the cave walls are interactive and the
cave listens. The most advanced office will look the *least* technological:
technology disappears into the walls; the space becomes warm, primal, human.
Work becomes embodied again — information is ingested with all senses, including
adaptive haptics (feel the dent in a dataset). The office stops being a container
for desks and becomes a temple of interaction, creation, empathy, and deep focus.

**Time horizon:** ~2035 — one office-lease cycle away.

## Design principles

- **Retrofit realism (added 2026-07-06, supersedes greenfield imagery).** 2035 is
  nine years away: the buildings in use then are the buildings standing now. Every
  scene is a retrofitted floor or ground level of a today-standard office building
  in an urban area — concrete structure, existing floor plates and columns, large
  windows onto a street, a tram stop nearby. The warm materials (clay plaster,
  wood, felt, textiles) are *finishes applied to existing structure* — which is
  real retrofit practice — never a new earthen building in a landscape. The
  consulting question the imagery must pose: how do these technologies and spatial
  ideas retrofit into the buildings companies already lease? Temple-like calm,
  right next to a tram station.
- **Warm organic materiality, not literal caves.** Clay-plastered surfaces,
  wood, daylight, fire-toned indirect light. Cave *qualities* — enclosure,
  warmth, curvature where walls were reworked — credible to executives.
- **No visible screens or gadgets.** Interactive surfaces read as painted/organic.
- **Ambient intelligence, never embodied. No uncanny valley.** No humanoid avatars,
  robots, faces, or synthetic colleagues anywhere — in the imagery, the essay, or
  the site copy. The *room* responds (light, surfaces, sound); it never pretends
  to be a person.
- **The haptic data surface is the centerpiece — and it is a tool, not a show.**
  A surface that displays data and physically adapts to touch at the same time:
  see the trend line and feel the anomaly as a dent, then push back — probe,
  filter, reshape with your hands. Working with data is framed as a craft
  (active), never a presentation (passive). Anchored to real research
  trajectories (MIT inFORM/Materiable shape displays, Ultraleap mid-air
  ultrasound haptics, electrostatic surface haptics) so it reads as foresight,
  not fantasy.

## The five spaces (shared skeleton of essay and site)

Narrative arc: arrive outside → be welcomed → deeper into the office as the work
gets deeper. Emphasis throughout on feeling welcome. May depart entirely from
classic office aesthetics.

1. **The Approach** — a repurposed ground-floor lobby: the former corporate
   entrance hall with reception desk and turnstiles removed, warmed into a
   street-level guest commons; the tram stop visible through the glazing;
   guest collaboration before anyone goes "inside".
2. **The Hearth** — warm arrival commons around a fire-like center; empathy and
   encounter.
3. **The Painted Wall** — co-creation room; a large interactive organic wall where
   a team sketches and the room listens and draws with them.
4. **The Den** — small enclosed alcove for concentrated solo work; soft, dark,
   womb-like.
5. **The Loom** — the room where you *work* data like a material, not merely
   sense it. The adaptive display-and-touch surface is its workbench: weave,
   probe, and reshape data; feel the anomaly as a dent under your fingers.
   Named for the loom as the ancestor of computing (Jacquard) — the first
   machine to hold data was a tactile craft tool. The deepest chapter and
   richest scene.

## Deliverable 1: the essay

Structure:

- **Opening: Lascaux, seventeen thousand years ago.** The first shared workspace was a cave wall.
  We're going back — this time the wall listens.
- **The wrong future.** Demolition of the glass-and-hologram office cliché
  (including anthropomorphic AI); why "more screens" is the past.
- **Five chapters, one per space.** Each opens with a second-person scene
  ("You arrive and…"), then unpacks: what work happens here, what technology
  enables it invisibly, what it replaces. Each chapter ends with a link/QR into
  the matching 360° scene.
- **What this means for leaders.** Three questions every executive should ask
  about their real estate, their tools, and their rituals. Conversation-starter
  close, no pitch.

Tone: keynote-like, concrete, sensory. Claims anchored to real technology
trajectories (spatial audio, e-textile and surface haptics, shape displays,
ambient LLMs).

## Deliverable 2: the website

### Experience

- **Landing:** one dark, quiet screen — title, one thesis sentence, one *Enter*
  button.
- **Guided tour (default):** scenes in narrative order. Each opens with a slow
  auto-pan and a 2–3 sentence narration card, then frees the visitor to look
  around; a subtle *Continue* advances.
- **Free roam:** minimal map/menu to jump between scenes.
- **Hotspots:** 3–5 glowing points per scene; each opens a short card with the
  idea behind what you're seeing. The Loom's central hotspot explains the
  adaptive haptic surface and the loom-to-computing lineage.
- **Language toggle** EN/DE (DE content in phase 2).
- Desktop drag, mobile gyroscope, presentable on a big screen in client meetings.

### Architecture

- Plain HTML/CSS/JS + **Pannellum** (MIT, ~21 KB) for 360° viewing, scene linking,
  hotspots. No framework, no build step.
- All copy (narrations, hotspot texts, both languages) in one `content.json` —
  editable without touching code.
- Panoramas: equirectangular from Blockade Labs Skybox AI, ~6–8K wide, served as
  WebP (~1–2 MB each) with low-res blur-up preload.
- **Hosting: GitHub Pages** (free, HTTPS, custom domain possible later).

### Repo layout

```
docs/          essay + design docs
site/          the website (deployed via GitHub Pages)
panoramas/     prompts.md — Skybox prompt library, so scenes are regenerable
```

## Image pipeline

For each scene: a detailed Skybox AI prompt encoding the shared visual language
(see design principles; explicitly exclude humans-as-robots/avatars, visible
screens, sci-fi blue lighting). Partner generates in Skybox AI (free tier first);
review together; iterate prompts; integrate. Placeholder panoramas stand in so the
site is fully functional before final images exist.

## Build order

1. Design doc committed, repo initialized ✅
2. Site skeleton with placeholder panoramas — tour, hotspots, toggle functional
3. Prompt library → partner generates scenes in Skybox AI → integrate
4. Essay (EN)
5. Polish, DE translation, GitHub Pages deploy
