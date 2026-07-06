# Skybox AI Prompt Library — The Office of 2035

Prompts for generating the five 360° scenes in [Blockade Labs Skybox AI](https://skybox.blockadelabs.com/).
Every scene is a retrofitted floor or ground level of a real, standing urban
office building — never a new earthen building in a landscape. Each scene below
has a recommended style preset, a main prompt, and a negative prompt. Generate,
review against the design principles, iterate, then integrate (workflow at the
bottom).

> **Length rule:** main prompts must stay under ~600 characters (Skybox AI's
> input limit); negative prompts are ordered most-critical-first so truncation
> loses the least important terms.

---

## Shared visual language

Every scene must speak the same dialect. Bake these into each generation and
check the result against them before accepting it:

- **Retrofit realism, not greenfield fantasy.** Every scene is inside (or at
  the street level of) a real existing urban office building — a 1990s/2000s
  concrete-and-glass block. The concrete structure stays visible: columns,
  floor plates, ceiling beams — but *softened*. The warm materials (clay
  plaster, wood, felt, wool, textiles) are **finishes applied to existing
  structure**, the way real retrofits work. The image must answer: "how does
  this fit into a building a company already leases?"
- **Warm organic materiality as finish.** Hand-troweled clay plaster over
  concrete, wood cladding and floors, felt acoustic baffles, woven textiles.
  Cave *qualities* — enclosure, curvature, warmth — where surfaces were
  reworked, credible to executives.
- **Light:** daylight from the building's real windows. Where windows appear,
  the outside is the city: other buildings, a street, tram infrastructure.
  Interior light is warm (ochre, umber, amber, sand). Never blue, never neon,
  never sci-fi glow.
- **Technology is invisible.** Interactive surfaces read as painted clay,
  fabric, or paper. No visible screens, monitors, keyboards, projectors,
  cables, or gadgets anywhere — the Den's single unlit e-paper sheet is the
  only exception, and it must read as a printed page.
- **Nobody home.** The rooms are empty of people — the visitor is the only
  person present. No humanoid figures of any kind, ever.
- **Camera:** standing eye height (~160 cm) unless a scene says otherwise,
  roughly the center of the space, level horizon.

**Always exclude (append to every negative prompt, non-negotiable):**
people, humanoid figures, robots, avatars, faces, mannequins, statues of
people, screens, monitors, keyboards, televisions, projectors, holograms,
blue LED lighting, neon, sci-fi lighting, text, writing, signage, logos,
watermark — plus, per scene, the sterile-office terms listed with each
negative prompt below (the Approach *is* a former corporate lobby, so it
excludes lobby furniture, not the lobby itself).

---

## 1. The Approach

**Style preset:** Realistic — or Advanced (no preset) if the preset over-stylizes the street outside. Iteration note: with signage excluded, the tram stop may need a few re-rolls to read as a tram stop (shelter, platform edge, overhead wires) rather than ambiguous street furniture.

**Main prompt:**

> Renovated ground-floor lobby of a 1990s concrete-and-glass office building, year 2035, from standing eye height. Reception desk and turnstiles removed; a pale rectangle of bolt marks in the terrazzo floor where the desk stood. Concrete columns warmed with clay plaster and wood cladding, low round wood guest tables with cushions, planted alcoves. The original floor-to-ceiling glazing opens onto a city street with a tram stop, tram wires overhead, buildings across the road. Soft morning daylight through the glass, warm amber light inside. Photorealistic, welcoming.

**Negative prompt:**

> people, humanoid figures, robots, avatars, faces, mannequins, statues of
> people, screens, monitors, keyboards, televisions, projectors, holograms,
> blue LED lighting, neon, sci-fi lighting, cold sterile lobby, reception
> desk, turnstiles, security gates, office cubicles, text, writing, signage,
> logos, watermark, badge readers, security cameras, revolving door

---

## 2. The Hearth

**Style preset:** Interior Views — or Advanced (no preset) for tighter control.

**Main prompt:**

> Renovated open upper floor of a 1990s concrete office building, year 2035, from standing eye height. Raw concrete ceiling softened with clay plaster and felt acoustic baffles. At the center a sealed ember hearth: glowing embers in a shallow clay basin, no fence, no fountain. Clay-plastered walls, warm wood floor, wool rugs, low cushioned benches facing the fire. To one side a kitchen alcove with wooden counter, fresh bread, ceramic cups, a copper kettle. Tall windows with sheer wool curtains show the city outside. Firelight and soft daylight. Photorealistic, intimate.

**Negative prompt:**

> people, humanoid figures, robots, avatars, faces, mannequins, statues of
> people, screens, monitors, keyboards, televisions, projectors, holograms,
> blue LED lighting, neon, sci-fi lighting, sterile corporate interior,
> office cubicles, text, writing, signage, logos, watermark, reception desk,
> counter service, fireplace mantel, chandelier, smoke, cold lighting

---

## 3. The Painted Wall

**Style preset:** Interior Views — or Advanced (no preset).

**Main prompt:**

> Co-creation room on a renovated floor of a 1990s concrete office building, year 2035, from standing eye height. One long clay-plastered wall running where glass meeting boxes once stood, covered in matte ochre and umber mineral-pigment sketch strokes, hand-drawn lines, faint older layers showing through beneath the newest marks. No glow, no glass. Daylight from the building's own tall windows rakes across the wall, revealing hand-troweled texture; a concrete column at each end. Warm wood floor, low wooden stools, clay pots of pigment on a ledge. Photorealistic, tactile.

**Negative prompt:**

> people, humanoid figures, robots, avatars, faces, mannequins, statues of
> people, screens, monitors, keyboards, televisions, projectors, holograms,
> blue LED lighting, neon, sci-fi lighting, sterile corporate interior,
> office cubicles, text, writing, signage, logos, watermark, whiteboard,
> sticky notes, markers, glowing wall, digital display, readable letters,
> glass partitions, recognizable animals

---

## 4. The Den

**Style preset:** Interior Views — or Advanced (no preset). Keep it dark; reject any bright generation. Iteration note: this tiny close-range volume is the hardest equirectangular brief — reject warped or impossible niche geometry and re-roll.

**Main prompt:**

> Tiny felt-and-wood alcove fitted between two raw concrete columns on a renovated 1990s office floor, year 2035, from seated eye height inside the niche, barely wider than outstretched arms. A curved felt-lined wall wraps behind a low wooden bench draped in thick lambswool; a heavy felt curtain half-drawn across the low opening; concrete column faces visible at the niche edges. On the bench a single matte sheet of e-paper, pale as a printed page, unlit. One pool of candle-warm light from a hidden source above, deep soft shadows. Photorealistic, enclosed, profoundly quiet.

**Negative prompt:**

> people, humanoid figures, robots, avatars, faces, mannequins, statues of
> people, screens, monitors, keyboards, televisions, projectors, holograms,
> blue LED lighting, neon, sci-fi lighting, sterile corporate interior,
> office cubicles, text, writing, signage, logos, watermark, office pod,
> phone booth, desk, office chair, laptop, tablet, bright light, windows,
> spacious room

---

## 5. The Loom

**Style preset:** Interior Views — or Advanced (no preset). This is the centerpiece; iterate until the surface reads as a physical relief, not a screen.

**Main prompt:**

> Former main conference room of a 1990s concrete office building, renovated, year 2035, from standing eye height beside a long waist-high workbench whose top is a living relief: ridges, valleys, and one distinct dent, sculpted from thousands of matte cells, as if data had been woven into terrain. Lit faintly from within by warm amber gradients, like embers under cloth, never glowing like a screen. Clay-plastered walls hung with large woven Jacquard textiles. Raw concrete ceiling, warm wood floor, a tall curtained window, low fire-toned light. Photorealistic, workshop-like.

**Negative prompt:**

> people, humanoid figures, robots, avatars, faces, mannequins, statues of
> people, screens, monitors, keyboards, televisions, projectors, holograms,
> blue LED lighting, neon, sci-fi lighting, sterile corporate interior,
> office cubicles, text, writing, signage, logos, watermark, conference
> table, projection screen, touchscreen table, glass table, charts, graphs,
> numbers, glowing grid, control room

**Iteration note:** the site copy mentions the old projector's mounting plate
still marking the ceiling. If a small bare metal plate happens to appear on
the concrete ceiling, keep it — it is on-message. Do not fight for it in the
prompt (asking for it tends to summon a whole projector, which the negative
prompt rightly forbids).

---

## Workflow: from Skybox AI to the site

1. **Generate** the scene in Skybox AI with the prompt and negative prompt
   above, at the highest resolution your plan allows. Compare against the
   shared visual language; iterate the prompt until it passes (especially:
   no people, no screens, no blue light, and the space reads as a renovated
   floor of a real building — concrete structure visible, warm finishes).
   Generation can also run via `tools/make_skyboxes.py` (the automated path
   through the Skybox AI API; script arrives with the next task).
2. **Download** the equirectangular JPG (not the cube map, not the video).
3. **Replace** the placeholder: save the file as `site/panos/<id>.jpg`
   (`approach`, `hearth`, `painted-wall`, `den`, `loom`) — same filename,
   the site picks it up unchanged. Target ≤ 2.5 MB; if larger, resave with
   Pillow at `quality=82`.
4. **Regenerate the blur-up preview** without touching the real panoramas:

       python3 tools/make_placeholders.py --previews-only

5. **Re-aim the hotspots:** open the scene in the browser
   (`python3 -m http.server 8080 --directory site`) and adjust that scene's
   hotspot `pitch`/`yaw` values in `site/content.json` so each ember sits on
   the object its card describes.
6. **Re-validate the content:** `python3 -m json.tool site/content.json`
   (syntax) plus the completeness check from plan Task 4 Step 3, which must
   still print `content OK, 19 hotspots`.
7. **Commit** per scene: `feat: real panorama for <id>`.
