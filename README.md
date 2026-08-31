# Magnetic Geodesic Dome — Scale Model

A 3D-printed, magnet-assembled scale model of a geodesic dome (Montreal Biosphère–inspired),
built as a proof-of-concept for an eventual full-size welded structure. The rest of this page is the
build spec; first, the short version of how it comes together.

## From a sphere to a dome you can hold

Geodesic domes turn a sphere into a lattice of triangles — the geometry behind landmarks like Montreal's
**Biosphère** and EPCOT's **Spaceship Earth**, and the starting point for this model.
(Background: [Geodesic polyhedron — Wikipedia](https://en.wikipedia.org/wiki/Geodesic_polyhedron).)

<p align="center">
  <img src="images/2%29%20Biosphere.png" width="47%" alt="Montreal Biosphère">
  <img src="images/3%29%20Spaceship_Earth%2C_EPCOT.jpg" width="47%" alt="Spaceship Earth, EPCOT">
</p>

<p align="center">
  <img src="images/2b%29%20Biosphere_side.jpg" width="40%" alt="Side view of the Montreal Biosphère geodesic frame">
  <br><em>A side view of the Montreal Biosphère — the geodesic frame up close.</em>
</p>

Start with an icosahedron and subdivide each of its 20 triangular faces into a finer grid — here **4V**
(four divisions per edge), giving 16 small triangles per face in just five distinct shapes.

<p align="center">
  <img src="images/4%29%204v_triangle.png" width="50%" alt="One face subdivided 4V into 16 triangles, shapes T1–T5">
</p>

Do that to all 20 faces and the whole sphere unfolds into this net:

<p align="center">
  <img src="images/5%29%20net20_labeled.png" width="100%" alt="Full icosahedron flat net — all 20 faces">
</p>

A full sphere isn't a dome, though — you cut it. Different fractions give different domes:

<p align="center">
  <img src="images/6%29%20truncations.png" width="68%" alt="Truncation options for the sphere">
</p>

This model takes the **5/8** cut — everything above a plane just below the equator. That leaves **200
panels**: the actual dome, unfolded and colored by shape:

<p align="center">
  <img src="images/7%29%20net58_labeled.png" width="100%" alt="5/8-truncation flat net — 200 panels">
</p>

Those 200 panels reduce to just **six printable parts** (T3 is chiral, so left and right):

<p align="center">
  <img src="images/8%29%20panels.png" width="85%" alt="The six panel shapes, inner face up with labels">
</p>

Give each shape its own grey — light at the vertices, dark at the centers — and the finished dome reads its
own structure, floating on a black base ring:

<p align="center">
  <img src="images/9%29%20shade_rim.png" width="100%" alt="Dome rendered in the production color ramp">
</p>

That base is **20 pieces in 4 shapes** (BL, BR, C, F) that mitre together into the rim — read them as several arcs or as one continuous ring, depending on how you group them:

<p align="center">
  <img src="images/10%29%20arcs_review.png" width="85%" alt="The four rim arc shapes in black">
</p>

Everything holds together with **magnets, not glue**. Each edge is *keyed* — its magnet pair sits at a
spacing unique to that chord — so only the correct panels can mate:

<p align="center">
  <img src="images/11%29%20keying_reference_1.png" width="70%" alt="Magnet keying reference">
</p>

And every magnet lives in the same little channel: a spherical seat that holds the ball flush at the surface,
a short throat that captures it, and a slide to load it from behind with a tamper:

<p align="center">
  <img src="images/12%29%20final_channel.png" width="70%" alt="Magnet channel cross-section">
</p>

---

# Spec sheet

*Rev. after first test print: tapered channel (prints open), show-face-flush orientation (no tilt),
thicker arc walls, bigger/deeper labels. See "First-print revisions" at the end.*

---

## Geometry

| | |
|---|---|
| Solid | Icosahedron |
| Subdivision | **4V (frequency 4)**, **Class I, Method 1** ("alternate") |
| Sphere diameter | **24 in (610 mm)** — radius R = 305 mm |
| Truncation | **5/8** (vertex-up, cut just below the equator at z ≈ −84 mm) |
| Dome height | ≈ 389 mm |
| Base diameter | ≈ 590 mm (a 20-sided zig-zag, amplitude only 7.7 mm) |

The base chord cycle repeats **C · B · F · B** (panels **T2 · T3 · T5 · T3**) five times around.

---

## Panels — 200 total, 6 printable shapes

| Shape | Chords | Edge lengths (mm) | Count |
|---|---|---|---|
| **T1** | A·A·C | 77.2 · 77.2 · 90.0 | 30 |
| **T2** | B·B·C | 89.8 · 89.8 · 90.0 | 35 |
| **T3-L** | B·D·E | 89.8 · 91.1 · 95.4 | 40 |
| **T3-R** | B·D·E | 89.8 · 91.1 · 95.4 | 40 |
| **T4** | E·E·F | 95.4 · 95.4 · 99.1 | 40 |
| **T5** | F·F·F | 99.1 · 99.1 · 99.1 | 15 |

Chord factors → mm (× R = 305): **A 77.2 · B 89.8 · C 90.0 · D 91.1 · E 95.4 · F 99.1**

Each panel: thin central **web 2.2 mm**, thicker **magnet rim 5.2 mm**, edges beveled along the
sphere's radial rays so they close into a sphere. Printed **outer-face-down** for a glossy exterior.

---

## Part labels (debossed on the inner face)

So panels can be sorted and oriented at assembly, each carries ID marks **debossed 0.6 mm into the
inner (pocket) face** — hidden on the finished dome, and facing up during printing so they engrave
cleanly with no supports. The outer show face is untouched.

- **Shape name** (T1 / T2 / T3L / T3R / T4 / T5) centered on the web, upright along the longest edge.
- **Chord letter** (A–F) centered on the rim band beside each edge, so the mating chord is obvious.
- **Arcs** carry their two seat chords: the T2·T3 arc reads **C** and **B**; the T5·T3 arc reads **F** and **B**.

---

## Rim — 20 arcs, 4 printable shapes  *(redesigned: arcs are now built as panels)*

The base ring was reworked so the arcs are **constructed and printed exactly like the triangular panels** —
flat, show-face-down, with the identical channel A loaded from the inner face. This replaced the old two-edge
arcs that printed standing up and whose magnets could not be inserted at all. Each old arc is split at its
middle vertex into two single-chord pieces, giving **20 arcs in 4 unique shapes, 5 each**:

- **C** — top chord C (seats a **T2**); two *tall* seams (symmetric)
- **F** — top chord F (seats a **T5**); two *short* seams (symmetric)
- **BL / BR** — top chord B (seats a **T3-L / T3-R**); one tall + one short seam (mirror pair)

Around the ring the chords run **B F B C** (×5). The seam heights — **tall ≈28 mm** at the C/B vertices,
**short ≈21 mm** at the F/B vertices — key the BL/BR mirror pair automatically: a tall seam only closes
against a tall seam, so a piece can't seat in its mirror's slot.

Construction (same helper as `build_panel`): a **radial frustum** (outer on the sphere at R, inner at
R−t_rim) so every edge is **beveled for free** at the panel dihedral; a **t_web pocket** on the inner face;
**channel A** cut on the top chord (to the panel above) and on both seams (to the neighbor arcs), **all loaded
from the inner face**. Wall thickness is the panel's **t_rim = 5.2 mm** (radial), pocket depth t_rim−t_web =
**3.0 mm** — byte-identical to a panel, so channel A sits at the same depth (Ø3.6 slide at 2.6 mm, 0.80 mm
wall over each magnet). The floor was dropped to **z = −105** so the short seams fit two magnets. Seam
magnets: **2 per seam** — the −105 floor makes even the short seams (~21 mm) tall enough for two (lower magnet
7 mm above the floor on every seam; tall pair 15.4 mm apart, short pair 7.7 mm apart).

Verified against the existing panels, all deltas **0.000 mm**: arc top-edge magnet windows coincide with the
owning panel's (C→T2, F→T5, BL/BR→T3-L/R); adjacent-arc seam windows coincide; and the arc∩panel and arc∩arc
*solids* abut with **zero interpenetration** (seam miters use the tangential bisector plane; a full-panel-plane
top cut was rejected — it sliced the wall into a wedge). Chord letters are debossed at the panel size (4.5/0.8).

---

## Magnets — 1/8 in (3.175 mm) N52 neodymium spheres

- **2 per edge**, free to rotate in their sockets to self-align polarity.
- Total ≈ **1,290 magnets** (≈1,200 in panel edges, 40 arc seats, 50 arc splices).
- Force is not the constraint — a single pair vastly exceeds the model's hoop tension; the sphere shape
  lets each ball find its own polarity.

### The one channel (identical for every magnet)

```
Ø1.4 window ← shallow spherical lead → OPEN barrel Ø3.6 → short chamfered throat Ø3.2 → slide Ø3.60 (to perimeter + 3.6 mm)
```

The channel axis is straight (one revolve, so no boolean-junction faces). One axis works because the kiss
direction (out the bevel) and the load direction (in from the pocket) are only ~5° apart on this
shallow-dihedral dome. **This is channel "A", locked by the coupon-2 magnet test** (see below); it replaced
a full Ø3.45 spherical cup that seated the ball beautifully but gripped it so hard it would not rotate.

- **Ø1.4 window (flush datum)** — the bevel truncates the seat to a Ø1.4 hole (1.4 < 3.175, so the ball can't
  escape the front). The ball floats forward to the window and, at assembly, the two mating **bevels close
  face-to-face** — *that* is what sets the flush kiss (front ~0.01 mm proud, so neighbor magnets touch). Because
  the kiss is set at the window/bevel, everything behind the window can be opened up for rotation **without
  changing how panels mate** — new parts kiss at the identical point as every part already printed.
- **Shallow spherical lead** — a short concentric spherical arc just behind the window cradles the ball
  forward (this is what gives retention its margin), *without* wrapping its whole front hemisphere the way the
  old full cup did. In the coupon test the two shallow-seat cases (A, B) both spun **and** retained; the cone
  seat (D) lost the ball out the throat because it had no forward cradle. So: shallow lead, not cone.
- **Open barrel Ø3.6** — behind the lead the ball's equator runs in a cylinder **0.21 mm wider per side** than
  the ball, so it **spins freely to self-align polarity**. This was the whole fix: opening the barrel (not
  touching the throat) is what freed rotation. Ø3.6 was chosen over Ø3.7/3.8 for the tighter retention margin
  and the thicker wall over the magnet (**0.80 mm** vs 0.70 mm at Ø3.8).
- **Throat = the retention knob (barrel/seat = A; throat is separate).** Coupon-2's letters A–F only varied
  barrel/seat at a *fixed* Ø3.2 throat, so "A" means **barrel Ø3.6 + shallow seat** and says nothing about the
  throat. Ø3.2 is only 0.025 mm under the 3.175 ball, so it captures **only** via the printer's ~0.1 mm shrink —
  which held on panels but **let the ball fall out of the arcs**. So the throat is being **tightened to
  Ø3.0–3.1** (nominally under the ball → captures by geometry, not luck) and confirmed on the arc test print;
  barrel/seat stay at A. Throat affects rotation not at all — purely capture.
- **Slide Ø3.60** — runs from the throat to the **perimeter** then **3.6 mm into the pocket** — just enough
  to drop the ball in and start a tamper rod straight.

*(Arc seat/splice magnets share the same window/kiss datum; the panel channel A geometry now applies to them
too, so panel and arc sockets are unified.)*

### How magnets are loaded (post-print, printer OFF)

Drop the ball into the slide from the pocket side, then push it with a small blunt rod (a **tamper**,
~2.5–3 mm) through the neck until it snaps into the socket flush at the window. The slide is the tamper's
guide. **Both panels and arcs load the same way — from the inner-face pocket, perpendicular to the edge** (the
arc redesign unified this; there is no separate "load up from the floor" case anymore).

### Keys (so wrong edges never mate)

Two magnets per edge at **t = 0.5 ± key**, symmetric about the midpoint, distinct per chord:

| A | B | C | D | E | F |
|---|---|---|---|---|---|
| ±0.14 | ±0.19 | ±0.24 | ±0.29 | ±0.34 | ±0.39 |

→ 21.6 mm apart on A edges, widening to 77.3 mm on F edges.

Splice keys: **3 magnets** stacked up the tall (T2·T3↔T5·T3) joints, **2** up the short
(T5·T3↔T2·T3) joints, ~7.7 mm apart, from 4 mm above the floor to 4 mm below the top.

---

## The coupons — how channel "A" was dialed in *(resolved)*

The fit that captures-and-holds while still letting the ball **spin** can't be predicted (the interference is
smaller than a 0.4 mm nozzle's ±0.1–0.15 mm repeatability), so it was measured on the machine with two
throwaway **coupons** — small test blocks, each a real T1 panel with the live channel repeated 6×,
printed show-face-down like a real panel.

- **Coupon 1 — throat sweep** (2.9 / 3.0 / 3.1 / 3.2 / 3.3 mm). Result: every throat captured and held, but
  **none let the ball rotate** — proving the throat was *not* what jammed rotation. The culprit was the full
  spherical cup gripping the ball's whole front hemisphere.
- **Coupon 2 — seat/barrel sweep** (throat fixed 3.2, window fixed 1.4; barrel Ø3.6/3.7/3.8 × shallow-seat vs
  cone vs the old full cup). Result: **A (barrel 3.6, shallow seat) and B (3.7, shallow) both spun and
  retained**; the cone (D) spun but **lost retention**; the old full cup (F) was too tight to rotate. **A won**
  — it rotates, has the best retention margin, and the thickest wall over the magnet. (Ø3.8 cases were void:
  the wide barrel reached the rim and the label deboss cut into the bore.)

**Outcome:** channel A is now the library default for every panel and arc. Nothing further to dial in unless a
future spool/nozzle prints retention marginal, in which case tighten the throat toward Ø3.1.

Shortcut if you don't want a separate coupon: **print your face test plate at neck 3.10 and use it as both
the coupon and your first real face.** If 3.10 is too tight or too loose once magnets arrive, it's a
one-line change and a reprint, with a real target to aim at.

Even with no magnets on hand yet, the first plate confirms everything that *doesn't* depend on them: flat
release, clean bevel dry-fit, readable labels, brim/first-layer behavior on the thin rim, and crisp slide
openings and windows.

---

## Colors (production)

The model is assembled **one color at a time** (single-extruder P1S), and color is made to carry the
shape information — so the finished dome reads as a graded pattern *and* the loose parts stay sortable by eye.

**Panels — a 5-step grey ramp, light at the vertices → dark at the centers.** Each of the five panel
shapes gets its own tone: lightest on **T1** (the little triangles clustered at the icosahedral vertices),
darkening step by step to **charcoal on T5** (the equilateral panels at each face center). This makes the
geodesic structure legible — the pentagonal vertex "stars" read light against dark face-centers — and
doubles as a bench sort key.

| Shape | Target tone (hex) | Bambu PLA Basic | Where it sits on the dome |
|---|---|---|---|
| **T1** | near-white `#F7F7FA` | **Jade White** `#FFFFFF` | vertex clusters |
| **T2** | light grey `#CCD1DB` | **Light Gray** `#D1D3D5` | just around the vertices |
| **T3-L / T3-R** | mid grey `#9EA3B0` (**shared**) | **Silver** `#A6A9AA` | the connective band |
| **T4** | dark grey `#737887` | **Gray** `#8E9089` (or Blue Grey `#5B6579`) | toward the face centers |
| **T5** | charcoal `#474C5C` | **Dark Gray** `#545454` | face centers |
| **Arcs (×10)** | — | **Black** `#000000` (its own "ground" tone) | base rim |

Bambu-color matches are nearest-hex from their official [PLA Basic hex table](https://store.bblcdn.com/s7/default/1084369ef84345bbaa5d704a492954e0/Bambu_PLA_Basic_Hex_Code.pdf);
T1/T2/T3/T5 are near-exact, T4 is a toss-up between **Gray** (better value separation) and **Blue Grey**
(truer to the cool tint). Confirm against a physical swatch before buying — printed PLA never matches an
on-screen hex.

The ramp is a **cool grey** (a faint blue in the neutral), stepping evenly white→charcoal. These are the
design-intent tones from the dome render (`shades2.py`); an earlier alternate ramp ran slightly lighter and
warmer (`shades.py`: `#F2F5FA · #D4D9E3 · #ADB5C2 · #858C9C · #596170`) if you prefer more contrast at the
dark end.

**T3-L and T3-R share one tone.** They're mirror images, so a single mid-grey covers both — the magnets'
keying (distinct per chord) enforces the chirality at assembly, so color doesn't have to. That keeps the
ramp to **five** filaments, not six.

**Arcs — Black (a sixth, "ground" color).** The 20 base rim arc pieces print in **Black** — a step below even the
T5 charcoal — so the base is its own element, not borrowed panel-grey. The five greys *code the five panel
shapes*; black reads as "not a panel, the ground the dome sits on." It gives a crisp value break wherever the
base meets the dome (even the darkest T5 panels stay distinct from the rim), recedes to pure shadow so the
grey dome floats above it, and completes the palette as an even six-step scale (White → Light Gray → Silver →
Gray → Dark Gray → Black). Black is also the cheapest, most consistent filament and hides ground scuffs best.
*Caveat:* pure black shows geometry (layer lines, blemishes catch light more than on grey), so the arcs want
clean first layers. (For a bright, deliberate plinth instead, **Jade White** arcs are a drop-in swap; to stay
at five spools, share the arcs onto **Dark Gray** with the T5 panels.)

The hex are **targets**, not exact filament colors — printed PLA won't land on a hex, so treat the Bambu
column as the nearest match and confirm on a swatch. (Prototyping is being done in the P1S sample **green** —
just a working color, not part of the scheme.)

### Filament quantities (full dome — 200 panels + 20 arc pieces)

Printed masses are calibrated from a real slice (the 117.06 g face plate → **0.906 g/cm³** effective, which
already includes walls + infill), so these are build numbers, not solid-volume guesses.

Per part, printed: **T1 ≈ 8.0 g · T2 ≈ 9.6 g · T3-L/R ≈ 10.0 g · T4 ≈ 10.9 g · T5 ≈ 11.3 g**; arc pieces
≈ **10–12 g** each (each old T2·T3 / T5·T3 arc is now split at its middle vertex into two halves).

Per color for the whole dome — net, and with a **+15 %** allowance for brim, purge, and the odd failed part:

| Color (Bambu) | Covers | Net | +15 % | 1 kg spools |
|---|---|---|---|---|
| **Jade White** | T1 ×30 | 240 g | 276 g | 1 |
| **Light Gray** | T2 ×35 | 336 g | 387 g | 1 |
| **Silver** | T3-L ×40 + T3-R ×40 | 800 g | 920 g | 1 |
| **Gray** (T4) | T4 ×40 | 436 g | 501 g | 1 |
| **Dark Gray** | T5 ×15 | 169 g | 195 g | 1 |
| **Black** | arc pieces ×20 | 215 g | 247 g | 1 |
| **Total** | 200 panels + 20 arc pieces | **2196 g** | **2525 g** | **6** |

Six colors, one 1 kg spool each — **~2.5 kg with margin**. The black is the lightest lift: the 20 arc pieces need
only ~215 g, so a single spool covers them several times over (and black is the cheapest, most available
stock). To collapse back to **five** spools instead, share the arcs onto **Dark Gray** with the T5 panels
(Dark Gray → ~442 g, still one spool).

---

## Production sequence (print & build)

**Build as face modules — this is what fits single-color printing.** The dome is ~**12½ identical face
triangles** plus the base ring. Every face is the same recipe, and every panel of a given color is
interchangeable, so printing (which yields piles of one color at a time) maps straight onto it: sequence
plates for printer efficiency, and assemble faces continuously from bins.

**One face module (16 panels):**

| Color | Panels per face |
|---|---|
| White (T1) | 3 |
| Light Gray (T2) | 3 |
| Silver (T3-L + T3-R) | 6 |
| Gray (T4) | 3 |
| Dark Gray (T5) | 1 |

*(Black arcs aren't part of a face — they're the separate base ring.)*

**Flow:**

1. **Base first.** Print the 20 Black arc pieces (~5 h) and assemble the mitred base ring — the foundation faces dock onto.
2. **Silver is the pacing color** — 6 of every 16 panels, 80 total. Keep Silver printing more or less
   continuously in the background; face completion is gated by how fast Silver arrives.
3. Print the four accent colors (White, Light Gray, Gray, Dark Gray) in **full single-color plates** around
   the Silver, changing filament only at plate boundaries (finish a color before switching to keep swaps low
   — ~19 color loads total across the run).
4. **Assemble a face** whenever the bins hold a full set (3 White · 3 Light Gray · 6 Silver · 3 Gray ·
   1 Dark Gray): drop and tamper its two magnets per edge, key-checked, then set the finished triangle aside.
5. **Dock faces bottom-up** onto the base ring, closing each horizontal course as a self-supporting
   compression hoop, up to the top cap.

This decouples printing from assembly: a failed panel is a non-event (pull the next same-color part from the
bin), and the printer never waits on the assembler or vice-versa.

*Alternative — progressive rings ("arcs up").* To watch a freestanding dome rise instead of building
modules, print bottom-up by course: the surface is **17 courses**, grouped into a base ring + ~6
color-interleaved phases (widest belt → equator → … → top cap), assembling each ring as its colors finish.
Same final result; it just couples print order to assembly order (more, smaller color batches) in exchange
for a taller dome after every phase.

**Scale:** ~**200 panels + 20 arc pieces**, ~**78 h** of printing across ~**28 plates** (≈90 h with reprints),
six PLA Basic spools (~2.5 kg). Silver and Gray are the long poles; the top third goes quickly.

---

## Print settings (Bambu P1S, 256 mm bed, 0.4 mm nozzle, one color at a time)

Standard:

- **Outer-face-down**, **supports OFF**, elephant's-foot compensation ~0.15 mm.
- Do **not** auto-orient / "place on face" — parts are pre-flattened show-face-down and just Auto-arrange.
- Full face (16 panels + 4 arc pieces) ≈ 3 plates.

For rounder holes and a crisper neck (the channels print as horizontal holes, whose tops tend to sag):

- **Layer height 0.16 mm** for panels (**0.12 mm** for the coupon) — thinner layers round the horizontal holes.
- **Calibrate flow rate / extrusion multiplier first** — over-extrusion is what closes small holes and tightens the neck.
- **Calibrate pressure advance** — keeps hole edges sharp instead of bulged.
- **Slow the outer wall / small-perimeter speed** (~50–100 mm/s) so the channel walls lay down cleanly.
- If slicing in **OrcaSlicer**, enable **X-Y hole compensation** to counter the typical hole under-sizing
  (Bambu Studio lacks a direct equivalent — lean on flow calibration there).
- The Ø1.4 window will likely print slightly under — that only *improves* retention, so it's fine.

**Bambu Studio process settings** (the exact toggles, plus what the first prints taught us):

- **Brim type: Auto** — *not* a forced "Outer brim." These are wide flat parts with a thick perimeter, so
  Auto adds none (huge bed-contact patch, no brim needed). A forced brim only mars the show-face edge and is
  annoying to peel. If a sharp triangle *tip* ever lifts, use **Mouse ears** (tiny corner discs), not a full brim.
- **Ironing → type: "Top surfaces."** Smooths the hidden inner face (the streaky top-skin we saw); optional, adds time.
- **Top surface pattern: Monotonic**, **Top shell layers: 4–5** — a fully-closed, uniform top skin.
- **Layer height 0.16 mm** for panels (**0.12 mm** for the coupon) — rounds the horizontal magnet holes.
- **Outer-wall / small-perimeter speed ~50–100 mm/s** — clean channel walls and crisp windows.
- **Calibrate flow rate + pressure advance first** — over-extrusion is what closes the small holes / tightens the neck.
- **Bed adhesion (anti-warp):** wash the plate with dish soap + warm water regularly, never touch the print area
  with bare fingers, and keep the **large flat panels toward the plate center** (the cooler edges are where big
  flats lift). Keep the door/lid closed. *(A T4 warped-and-rippled on plate 2 — it was a first-layer adhesion
  failure at a plate edge, not a lack of brim.)*
- **Orientation is baked in:** every part is pre-flattened **show-face-down** via the deterministic
  "largest-coplanar-facet → bed" method, **verified 0.000° tilt**. Do not re-orient — a residual tilt of only
  ~0.2° prints the first layer in visible steps (the T4/T5 files had this before the fix). Just Auto-arrange.
- **Save ONE process preset and slice every plate from it.** Plate-to-plate drift in settings is what let T4/T5
  come out tilted while the rest were flat; a single locked preset keeps all 200 panels identical.

Color scheme: see **Colors (production)** above — a 5-step Bambu grey ramp by shape (Jade White T1 → Dark
Gray T5, T3-L/R share Silver) plus **Black** for the base arcs. Six PLA Basic spools, ~2.5 kg total. Print
one color at a time.

---

## First-print revisions (what the test plate taught us)

The first full-face print worked, and revealed four things — all now fixed in the files:

1. **Stepped neck plugged shut.** The horizontal channel's abrupt slide→neck step sagged closed at the neck.
   → **Tapered channel** (Ø3.6 → Ø3.1 cone), which prints open. Bonus: it also removed a stubborn
   non-manifold edge on the symmetric T5.
2. **Show face printed with a tilted patch.** The old flatten aligned to the panel's average plane (PCA),
   tilting the show face ~0.3° so a corner floated ~0.2 mm off the bed and the first layer was skipped there
   (a crisp triangular texture change). → **Orient on the show face itself**, so it lies dead flat (corner
   spread now 0.000 mm).
3. **Arc seat sockets bled through to a slit** on the inner face (only ~0.8 mm of wall behind them).
   → **7 mm arc wall** (2.6 mm backing now). The *splice* openings on the arc inner face are intentional
   (that's how those end magnets load) and stay.
4. **Chord letters a little hard to read.** → **bigger (4.5 mm) and deeper (0.8 mm)**.

5. **Magnets seated but wouldn't rotate** (found with real magnets, coupon 2). The full Ø3.45 spherical cup
   cradled the ball's whole front hemisphere — great seating, but too much conforming contact to let it spin
   and self-align polarity. → **Channel A**: shallow spherical lead + **open barrel Ø3.6** + throat Ø3.2
   (see *The one channel* and *The coupons* above). Balls now rotate freely and still retain; kiss point
   unchanged, so it mates with every part already printed.

6. **Arcs were wrong in every way and got rebuilt as panels** (the big work since the last commit). The old
   arcs printed standing up; magnets would not insert, edges weren't beveled, and the channels didn't retain.
   → The rim is now **20 flat panel-family arcs in 4 shapes (C, F, BL, BR)** built from the same radial-frustum
   helper as the panels — beveled edges for free, channel A loaded from the inner face, wall = panel t_rim
   (5.2 mm), floor dropped to −105 for two magnets on the short seams. See **Rim** above. Interfaces to the
   existing panels and to neighbor arcs verified exact (0.000 mm). *Test print in progress: one BL/F/BR/C set
   against the existing T2/T5/T3-L/T3-R panels to confirm seating, arc-to-arc seams, retention, and height.*

### Open items
- **Throat for retention:** tightening from Ø3.2 to **Ø3.0–3.1** (Ø3.2 relied on print shrink and let go in
  the arcs); confirm on the arc test print, then lock one throat across panels **and** arcs.
- **Arc-to-panel top seam:** the arc top now abuts the panel with zero interpenetration and exact magnets; a
  small top-edge chamfer to close the shallow V-gap at that seam is optional and still to add.
- After the arc test passes: regenerate the full production kit (200 panels + 20 arcs) with the locked
  throat, and update the magnet count (the 20-arc rim changes the old 40-seat / 50-splice tally).
