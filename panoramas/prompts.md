# Skybox AI Prompt Library — The Office of 2035

Prompts for generating the five 360° scenes in [Blockade Labs Skybox AI](https://skybox.blockadelabs.com/).
Every scene is a retrofitted floor or ground level of a real, standing urban
office building — never a new earthen building in a landscape — and the scenes
show **work happening**: people collaborating, walls carrying diagrams and
product visuals. Each scene below has a recommended style preset, a main
prompt, and a negative prompt. Generate, review against the design principles,
iterate, then integrate (workflow at the bottom).

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
- **Work made visible.** Walls carry the work: hand-drawn diagrams, flow
  charts, data curves, product sketches — including a large 3D engineering
  drawing of a pump under development (Painted Wall) and a life-size live
  transmission to an industrial site (Loom). All wall content reads as drawn
  into or woven into the surface — matte, warm-toned — never a glowing blue
  rectangle. No freestanding monitors, laptops, or keyboards anywhere; the
  Den's single unlit e-paper sheet must read as a printed page.
- **People at work, rendered with care.** Small groups (2–4) of human
  colleagues: standing at walls with fingertips on the drawings, sitting
  together around the fire, gathered at the workbench. Natural proportions,
  everyday clothing, faces incidental — mostly seen from the side, from
  behind, or at conversational distance (this also avoids AI face artifacts).
  Never robots, avatars, mannequins, or synthetic figures. **The Den stays
  empty** — its occupant is the visitor.
- **Camera:** standing eye height (~160 cm) unless a scene says otherwise,
  roughly the center of the space, level horizon.

**Always exclude (append to every negative prompt, non-negotiable):**
robots, avatars, mannequins, statues of people, deformed faces, distorted
hands, extra fingers, holograms, blue LED lighting, neon, sci-fi lighting,
readable text, lettering, signage, logos, watermark — plus, per scene, the
display exclusions (screens, monitors, keyboards, televisions, projectors)
*except* where a scene's brief explicitly includes a display surface (the
Loom's live-transmission wall), and the sterile-office terms listed with each
negative prompt below.

---

## 1. The Approach

**Style preset:** Realistic — or Advanced (no preset) if the preset over-stylizes the street outside. Iteration note: with signage excluded, the tram stop may need a few re-rolls to read as a tram stop (shelter, platform edge, overhead wires) rather than ambiguous street furniture.

**Main prompt:**

> Renovated ground-floor lobby of a 1990s concrete-and-glass office building,
> year 2035, from standing eye height. Reception desk and turnstiles removed;
> pale bolt marks in the terrazzo floor where the desk stood. Concrete columns
> warmed with clay plaster and wood, low round guest tables, planted alcoves;
> two small groups of visitors in relaxed conversation at the tables, seen at
> a distance. The floor-to-ceiling glazing opens onto a city street with a
> tram stop and buildings across the road. Soft morning daylight, warm amber
> light inside. Photorealistic, welcoming.

**Negative prompt:**

> robots, avatars, mannequins, statues of people, deformed faces, distorted
> hands, extra fingers, screens, monitors, keyboards, televisions, projectors,
> holograms, blue LED lighting, neon, sci-fi lighting, cold sterile lobby,
> reception desk, turnstiles, security gates, office cubicles, readable text,
> lettering, signage, logos, watermark, badge readers, security cameras,
> revolving door, crowd

---

## 2. The Hearth

**Style preset:** Interior Views — or Advanced (no preset) for tighter control.

**Main prompt:**

> At the center of a wide renovated 1990s office floor, a shallow round clay
> basin of glowing embers, year 2035, from standing eye height; four
> colleagues sit together on low cushioned benches around the fire, coffee
> cups in hand, in easy conversation. High raw concrete ceiling softened with
> felt acoustic baffles, clay-plastered columns, tall windows with sheer wool
> curtains, city buildings outside. Warm wood floor, wool rugs; to one side a
> kitchen alcove with wooden counter, bread, ceramic cups, a copper kettle.
> Firelight and soft daylight. Photorealistic, intimate.

**Negative prompt:**

> fireplace, chimney, stove, flue, statue, sculpture, figurine, single person,
> person looking at camera, cottage, farmhouse, framed pictures, robots, avatars, mannequins, deformed faces, extra
> fingers, screens, monitors, keyboards, televisions, projectors, holograms,
> blue LED lighting, neon, sci-fi lighting, readable text, lettering, signage,
> logos, watermark, sterile corporate interior

---

## 3. The Painted Wall

**Style preset:** Interior Views — or Advanced (no preset).

**Main prompt:**

> A spacious co-creation room on a renovated 1990s office floor, year 2035,
> seen from its center, several meters back from a long flat hand-troweled
> clay wall covered in work: hand-drawn ochre and umber diagrams, flow
> charts, product sketches in matte mineral pigment, and one large 3D
> exploded-view engineering drawing of an industrial pump. A few people stand
> at the wall, seen from behind, fingertips on the drawings. Daylight from
> tall windows rakes across the wall; raw concrete ceiling, warm wood floor,
> low stools. Photorealistic, focused, tactile.

**Negative prompt:**

> close-up, cramped corridor, hallway, cave, melted shapes, skylight, blank wall, glowing wall, digital display,
> whiteboard, statue, sculpture, single person, person looking at camera,
> robots, avatars, mannequins, deformed faces, distorted hands, screens,
> monitors, keyboards, televisions, projectors, holograms, blue LED lighting,
> neon, sci-fi lighting, readable text, lettering, signage, logos, watermark

---

## 4. The Den

**Style preset:** Interior Views — or Advanced (no preset). Keep it dark; reject any bright generation. Iteration note: this tiny close-range volume is the hardest equirectangular brief — reject warped or impossible niche geometry and re-roll. The Den stays empty of people: its occupant is the visitor.

**Main prompt:**

> A tiny dark cocoon-like reading alcove, every wall upholstered in
> chocolate-brown wool felt, inside a renovated 1990s office building, year
> 2035, from seated eye height, barely wider than outstretched arms. Dark
> wool carpet; a low oak bench draped with a cream lambswool fleece; a heavy
> brown felt curtain half-open across the low doorway; on the bench a single
> white sheet of e-paper like a printed page, unlit. Night-time; one small
> warm reading light glowing above the bench; deep brown shadows, crisp
> textile detail. Photorealistic, snug, silent.

**Negative prompt:**

> white walls, gray floor, bright light, daylight, spacious room, large room,
> spa, gallery, hallway, blurry, out of focus, lettering, readable text,
> signage, logos, watermark, people, humanoid figures, faces, robots,
> avatars, mannequins, screens, monitors, keyboards, televisions, projectors,
> holograms, blue LED lighting, neon, sci-fi lighting, windows, office pod,
> desk, laptop

---

## 5. The Loom

**Style preset:** Interior Views — or Advanced (no preset). This is the centerpiece; iterate until the relief surface reads as physical, not rendered, and the live-transmission wall reads as warm documentary footage — a window to a real industrial site — never a blue screen.

**Main prompt:**

> A single long waist-high table dominates a former conference room on a
> renovated 1990s office floor, year 2035: its entire top is a sculpted
> relief landscape of ridges and valleys with one deep dent, carved pale
> wood glowing faint amber from within, like data woven into terrain. No
> other furniture. On the end wall, life-size warm live footage of an
> industrial hall with a large pump and one technician at work beside it.
> Woven Jacquard textiles on the side walls, raw concrete ceiling, warm wood
> floor, city buildings through tall windows. Photorealistic, workshop-like.

**Negative prompt:**

> people, humanoid figures, faces, person looking at camera, portrait,
> statue, office desks, office chairs, corridor, drawers, filing cabinet,
> conference table, empty room, renovation site, construction tools,
> countryside, forest, robots, avatars, mannequins, keyboards, laptops,
> holograms, blue LED lighting, neon, sci-fi lighting, readable text,
> lettering, signage, logos, watermark, touchscreen table

**Iteration notes:** (1) The live-transmission wall is the one sanctioned
display in the project — it must read warm and documentary (industrial hall,
the pump, one technician), never a glowing blue rectangle; re-roll if it
generates as a TV or monitor with bezels. (2) The site copy mentions the old
projector's mounting plate still marking the ceiling. If a small bare metal
plate happens to appear on the concrete ceiling, keep it — it is on-message.
Do not fight for it in the prompt.

---

## Workflow: from Skybox AI to the site

1. **Generate** the scene in Skybox AI with the prompt and negative prompt
   above, at the highest resolution your plan allows. Compare against the
   shared visual language; iterate the prompt until it passes (especially:
   people look natural and human, wall content reads as drawn or woven — not
   glowing, no blue light, and the space reads as a renovated floor of a real
   building — concrete structure visible, warm finishes).
   Generation can also run via `tools/make_skyboxes.py` (the automated path
   through the Skybox AI API).
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
