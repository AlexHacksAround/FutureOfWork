# Skybox AI Prompt Library — The Office of 2035

Prompts for generating the five 360° scenes in [Blockade Labs Skybox AI](https://skybox.blockadelabs.com/).
Each scene below has a recommended style preset, a main prompt, and a negative
prompt. Generate, review against the design principles, iterate, then integrate
(workflow at the bottom).

> **Length rule:** main prompts must stay under ~600 characters (Skybox AI's
> input limit); negative prompts are ordered most-critical-first so truncation
> loses the least important terms.

---

## Shared visual language

Every scene must speak the same dialect. Bake these into each generation and
check the result against them before accepting it:

- **Warm organic architecture, not a literal cave.** Curved earthen and clay
  surfaces, hand-plastered walls, warm wood, woven textiles, stone. Cave
  *qualities* — enclosure, curvature, warmth — rendered credible to executives.
- **Light:** daylight shafts from above, fire-toned indirect light, morning
  light. Warm palette only (ochre, umber, amber, sand, moss). Never blue, never
  neon, never sci-fi glow.
- **Technology is invisible.** Interactive surfaces read as painted clay,
  fabric, or paper. No visible screens, monitors, keyboards, projectors,
  cables, or gadgets anywhere.
- **Nobody home.** The rooms are empty of people — the visitor is the only
  person present. No humanoid figures of any kind, ever.
- **Camera:** standing eye height (~160 cm), roughly the center of the space,
  level horizon.

**Always exclude (append to every negative prompt, non-negotiable):**
people, humanoid figures, robots, avatars, faces, mannequins, statues of
people, screens, monitors, keyboards, televisions, projectors, holograms,
blue LED lighting, neon, sci-fi lighting, glass-and-steel corporate lobby,
office cubicles, text, writing, signage, logos, watermark.

---

## 1. The Approach

**Style preset:** Realistic — or Advanced (no preset) if the preset over-stylizes vegetation.

**Main prompt:**

> Outdoor guest commons before a low curved earthen office building, year
> 2035, from standing eye height on a winding path of warm flat stone through
> a lush garden: low round stone tables, planted alcoves with cushioned wooden
> benches, tall grasses, moss, mature trees. Ahead the rammed-earth facade
> curves gently, a wide doorway standing open with warm amber light glowing
> inside — no door hardware, no badge reader, no reception. Soft morning
> sunlight, long shadows, dew on leaves, open sky with light clouds.
> Photorealistic, warm, welcoming.

**Negative prompt:**

> people, humanoid figures, robots, avatars, faces, mannequins, statues of
> people, screens, monitors, keyboards, televisions, projectors, holograms,
> blue LED lighting, neon, sci-fi lighting, glass-and-steel corporate lobby,
> office cubicles, text, writing, signage, logos, watermark, cars, parking
> lot, skyscrapers, fences, security gates, turnstiles, cameras

---

## 2. The Hearth

**Style preset:** Interior Views — or Advanced (no preset) for tighter control.

**Main prompt:**

> Wide round arrival commons inside an earthen office building, year 2035,
> from standing eye height at the room's edge. At the center a low circular
> hearth: glowing embers in a shallow clay basin, no fence, no fountain.
> Curved hand-plastered clay walls, warm wood floor, wool rugs, low cushioned
> benches facing the fire. To one side an open kitchen alcove with a wooden
> counter, fresh bread, ceramic cups, a copper kettle. Daylight falls in soft
> shafts from a round skylight; the rest lit by firelight and hidden warm
> indirect light. Photorealistic, intimate, welcoming.

**Negative prompt:**

> people, humanoid figures, robots, avatars, faces, mannequins, statues of
> people, screens, monitors, keyboards, televisions, projectors, holograms,
> blue LED lighting, neon, sci-fi lighting, glass-and-steel corporate lobby,
> office cubicles, text, writing, signage, logos, watermark, reception desk,
> counter service, fireplace mantel, chandelier, smoke, cold lighting

---

## 3. The Painted Wall

**Style preset:** Interior Views — or Advanced (no preset).

**Main prompt:**

> Co-creation room in an earthen office building, year 2035, from standing
> eye height at the center. One long gently curved painted-clay wall covered
> in matte ochre and umber mineral-pigment sketch strokes — abstract diagrams,
> hand-drawn lines, faint older layers of drawing showing through beneath the
> newest marks, like cave paintings layered over centuries. No glow, no glass.
> A daylight shaft from a slot skylight rakes across the wall, revealing its
> texture. Warm wood floor, low wooden stools, small clay pots of pigment on
> a ledge. Photorealistic, contemplative, tactile.

**Negative prompt:**

> people, humanoid figures, robots, avatars, faces, mannequins, statues of
> people, screens, monitors, keyboards, televisions, projectors, holograms,
> blue LED lighting, neon, sci-fi lighting, glass-and-steel corporate lobby,
> office cubicles, text, writing, signage, logos, watermark, whiteboard,
> sticky notes, markers, glowing wall, digital display, readable letters,
> recognizable animals

---

## 4. The Den

**Style preset:** Interior Views — or Advanced (no preset). Keep it dark; reject any bright generation.

**Main prompt:**

> Tiny womb-like alcove for solo deep work in an earthen building, year 2035,
> from seated eye height inside the niche, barely wider than outstretched
> arms. A curved clay wall wraps behind a low bench draped in thick lambswool;
> a heavy felt curtain half-drawn across the low rounded entrance. On the
> bench a single matte sheet of e-paper, pale as a printed page, unlit. Dim
> and warm: one soft pool of candle-warm light from a hidden source above the
> bench, deep soft shadows elsewhere, wool and felt absorbing all sound.
> Photorealistic, enclosed, profoundly quiet.

**Negative prompt:**

> people, humanoid figures, robots, avatars, faces, mannequins, statues of
> people, screens, monitors, keyboards, televisions, projectors, holograms,
> blue LED lighting, neon, sci-fi lighting, glass-and-steel corporate lobby,
> office cubicles, text, writing, signage, logos, watermark, office pod,
> phone booth, desk, office chair, laptop, tablet, bright light, windows,
> spacious room

---

## 5. The Loom

**Style preset:** Interior Views — or Advanced (no preset). This is the centerpiece; iterate until the surface reads as a physical relief, not a screen.

**Main prompt:**

> Deepest room of an earthen office building, year 2035, from standing eye
> height beside a long waist-high workbench whose top is a living relief —
> ridges, valleys, and one distinct dent, sculpted from thousands of fine
> matte cells, as if data had been woven into terrain. Lit from within by
> faint warm amber gradients, like embers under cloth, never glowing like a
> screen. Curved clay walls hung with large woven Jacquard textiles, warp and
> weft. Warm wood floor, low fire-toned indirect light, one daylight shaft
> from above. Photorealistic, tactile, workshop-like.

**Negative prompt:**

> people, humanoid figures, robots, avatars, faces, mannequins, statues of
> people, screens, monitors, keyboards, televisions, projectors, holograms,
> blue LED lighting, neon, sci-fi lighting, glass-and-steel corporate lobby,
> office cubicles, text, writing, signage, logos, watermark, touchscreen
> table, glass table, charts, graphs, numbers, glowing grid, control room,
> conference room

---

## Workflow: from Skybox AI to the site

1. **Generate** the scene in Skybox AI with the prompt and negative prompt
   above, at the highest resolution your plan allows. Compare against the
   shared visual language; iterate the prompt until it passes (especially:
   no people, no screens, no blue light).
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
