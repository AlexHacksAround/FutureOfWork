# Skybox AI Prompt Library — The Office of 2035

Prompts for generating the five 360° scenes in [Blockade Labs Skybox AI](https://skybox.blockadelabs.com/).
Every scene is a retrofitted floor or ground level of a real, standing urban
office building. Two key technologies carry the vision and must read clearly:
the **interactive wall** (painted-wall scene) and the **haptic data table**
(loom scene). Rooms are bright, modern, matter-of-fact workplaces — warm, but
never a temple. Generate, review against the design principles, iterate, then
integrate (workflow at the bottom).

> **Length rule:** main prompts must stay under ~600 characters (Skybox AI's
> input limit); negative prompts are ordered most-critical-first so truncation
> loses the least important terms.
>
> **Edit-and-regenerate loop:** edit this file (locally or on GitHub), then run
> `python3 tools/make_skyboxes.py --only <scene-id>` — it parses the prompts
> from this file and replaces `site/panos/<id>.jpg`.

---

## Shared visual language

- **Retrofit realism.** Inside (or at street level of) a real 1990s/2000s
  concrete-and-glass urban office building. Concrete structure visible but
  renovated; city, street, tram outside the real windows.
- **Modern natural materials, no temple.** Wood, stone, glass, matte light
  plaster, plants, paper, daylight, warm neutral tones. NO clay walls, no
  wool, no felt cocoons, no candle-lit ritual atmosphere. Bright rooms.
- **Nobody present.** Generated people read awkward — scenes are momentarily
  empty; the work shows through artifacts: walls covered in drawings and
  charts, a table mid-analysis, chairs pushed back as if people just stepped
  out.
- **The two displays are matte and warm.** The interactive wall and the data
  table may visibly display content (diagrams, charts, contours) but always
  paper-like, daylight-readable, warm-toned — never a glowing blue screen,
  never bezels, never a mounted TV.
- **Camera:** standing eye height (~160 cm), roughly the center, level
  horizon.

**Always exclude (append to every negative prompt, non-negotiable):**
people, humanoid figures, faces, robots, avatars, mannequins, statues,
televisions, monitors with bezels, keyboards, laptops, projectors, holograms,
blue LED lighting, neon, sci-fi lighting, readable text, lettering, signage,
logos, watermark, candles, meditation room, spa, yoga studio.

---

## 1. The Approach

**Style preset:** Realistic — or Advanced (no preset). NOTE: the current live
panorama (roll 3) is approved and kept; this prompt is for future regeneration
only.

**Main prompt:**

> Renovated ground-floor lobby of a 1990s concrete-and-glass office building,
> year 2035, from standing eye height. Reception desk and turnstiles removed;
> pale bolt marks in the terrazzo floor where the desk stood. Concrete columns
> and a warm wood-slat ceiling, low round guest tables of light wood, stone
> benches with planted beds, a coffee bar alcove. The original floor-to-ceiling
> glazing opens onto a city street with a tram stop and buildings across the
> road. Bright, soft morning daylight. Photorealistic, welcoming, modern.

**Negative prompt:**

> people, humanoid figures, faces, robots, avatars, mannequins, statues,
> reception desk, turnstiles, security gates, badge readers, security cameras,
> revolving door, cold sterile lobby, televisions, monitors with bezels,
> keyboards, laptops, projectors, holograms, blue LED lighting, neon, sci-fi
> lighting, readable text, lettering, signage, logos, watermark

---

## 2. The Hearth (Interaction room)

**Style preset:** Interior Views — or Advanced (no preset). The room where
groups meet so that everyone can see each other; data on the walls around
them.

**Main prompt:**

> Bright renovated open floor of a 1990s concrete office building, year 2035,
> from standing eye height. A wide arc of wooden benches and chairs with warm
> neutral upholstery curves around a low round table so that everyone faces
> each other; around the seating, matte wall surfaces carry warm ochre
> hand-drawn charts, timelines and diagrams, paper-like, daylight-readable.
> Renovated concrete ceiling, light wood floor, plants, tall windows with city
> buildings outside. Fresh coffee on the table, chairs slightly pushed back.
> Bright daylight, warm tones. Photorealistic, modern, inviting.

**Negative prompt:**

> people, humanoid figures, faces, robots, avatars, mannequins, statues,
> fireplace, fire pit, candles, meditation room, spa, yoga studio, cushion
> circle, televisions, monitors with bezels, keyboards, laptops, projectors,
> holograms, blue LED lighting, neon, sci-fi lighting, readable text,
> lettering, signage, logos, watermark, cubicles, conference table

---

## 3. The Painted Wall (the interactive wall)

**Style preset:** Interior Views — or Advanced (no preset). Key technology #1:
the wall itself must dominate — matte, paper-like, covered in work.

**Main prompt:**

> A bright co-creation room on a renovated 1990s office floor, year 2035, seen
> from its center. One long flat matte wall, warm paper-white, is covered
> edge to edge in work: hand-drawn ochre and umber diagrams, flow charts,
> data curves, product sketches, and one large exploded-view engineering
> drawing of an industrial pump, all in warm line work like ink on paper,
> daylight-readable, no glow. Light wood floor, a few wooden stools, plants
> in the corner. Daylight from tall windows with the city outside rakes
> across the wall. Photorealistic, focused, modern.

**Negative prompt:**

> people, humanoid figures, faces, robots, avatars, mannequins, statues,
> glowing wall, blue glow, whiteboard, sticky notes, projector screen, framed
> pictures, televisions, monitors with bezels, keyboards, laptops, projectors,
> holograms, blue LED lighting, neon, sci-fi lighting, readable text,
> lettering, signage, logos, watermark, cave, rock, sand dune

---

## 4. The Den (Focus room)

**Style preset:** Interior Views — or Advanced (no preset). WELL-LIT — this is
the brightest small room on the floor, not a dark cocoon.

**Main prompt:**

> A small, bright, quiet focus room on a renovated 1990s office floor, year
> 2035, from seated eye height. Warm wood-panelled walls, one comfortable
> armchair with a light fabric throw, a small side table with a single matte
> white sheet of e-paper like a printed page. One matte wall panel carries a
> single hand-drawn document outline in warm gray line work, paper-like, no
> glow. A tall window with sheer curtain, soft north daylight, a plant, light
> wood floor. Calm, ordered, bright. Photorealistic, serene, modern.

**Negative prompt:**

> dark room, dim light, cocoon, felt, wool, cave, candles, meditation room,
> spa, yoga studio, people, humanoid figures, faces, robots, avatars,
> mannequins, statues, televisions, monitors with bezels, keyboards, laptops,
> projectors, holograms, blue LED lighting, neon, sci-fi lighting, readable
> text, lettering, signage, logos, watermark, desk, office chair

---

## 5. The Loom (the haptic data table)

**Style preset:** Interior Views — or Advanced (no preset). Key technology #2:
a waist-high interactive table whose surface is a physical data relief. The
one sanctioned display surface besides the walls — matte and warm, never a
blue screen.

**Main prompt:**

> Standing directly at the edge of a large waist-high data table that fills
> the foreground, in a bright former conference room of a renovated 1990s
> office building, year 2035. The tabletop stretches away from the camera:
> a matte dark-bronze surface sculpted as a physical topographic relief of
> gentle ridges and valleys, like a precise landscape model of wood and
> metal, one small distinct bump, soft warm amber contour lines glowing
> between the ridges, no glare. Light wood floor, renovated concrete
> ceiling, tall windows with city buildings, bright daylight.
> Photorealistic, precise, modern.

**Negative prompt:**

> people, humanoid figures, faces, robots, avatars, mannequins, statues,
> touchscreen with icons, glowing blue table, billiard balls, pool table,
> conference table with chairs around it, televisions, monitors with bezels,
> keyboards, laptops, projectors, holograms, blue LED lighting, neon, sci-fi
> lighting, readable text, lettering, signage, logos, watermark, fabric
> landscape, textile dunes, art installation

---

## Workflow: from Skybox AI to the site

1. **Generate** the scene with the prompt and negative prompt above
   (`python3 tools/make_skyboxes.py --only <id>` or the web UI). Compare
   against the shared visual language; iterate until it passes (bright,
   modern, no people, the two technologies matte and warm, city outside).
2. **Download** the equirectangular JPG (not the cube map, not the video) —
   the script does this automatically.
3. **Replace** the placeholder: `site/panos/<id>.jpg` (`approach`, `hearth`,
   `painted-wall`, `den`, `loom`) — same filename. Target ≤ 2.5 MB; if
   larger, resave with Pillow at `quality=82`.
4. **Regenerate the blur-up preview:**

       python3 tools/make_placeholders.py --previews-only

5. **Re-aim the hotspots:** adjust that scene's hotspot `pitch`/`yaw` in
   `site/content.json` so each ember sits on the object its card describes.
6. **Re-validate:** `python3 -m json.tool site/content.json` plus the
   completeness check (must print `content OK, 19 hotspots`).
7. **Commit** per scene: `feat: real panorama for <id>`.
