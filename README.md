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

That base is **ten curved arcs** that mitre together into the rim:

<p align="center">
  <img src="images/10%29%20arcs_review.png" width="85%" alt="The two rim arc shapes in black">
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

## Rim — 10 arcs, 2 printable shapes

The 5/8 base is too wide to split in fifths (347 mm > 256 mm bed), so it's **10 arcs** (≈186 mm each):

- **5 × "T2·T3 arc"** — top seats on chords **C + B**
- **5 × "T5·T3 arc"** — top seats on chords **F + B**

Each arc is a wall standing on a flat foot, with **mitred joint faces** so neighbors close flush. The wall is
**7 mm thick** (thicker than the 5.2 mm panel rim): the panel-to-arc joint angle made a 5.2 mm wall too slim
behind the seat sockets, so they broke through the inner face — the extra material is added on the inner side,
seats stay at the outer bevel so panel mating is unchanged. Every arc has one **3-magnet (tall)** end and one
**2-magnet (short)** end; tall meets tall, short meets short. (Arc seats load vertically and print as clean
holes, so they keep a stepped Ø3.1 throat rather than the taper.)

---

## Magnets — 1/8 in (3.175 mm) N52 neodymium spheres

- **2 per edge**, free to rotate in their sockets to self-align polarity.
- Total ≈ **1,290 magnets** (≈1,200 in panel edges, 40 arc seats, 50 arc splices).
- Force is not the constraint — a single pair vastly exceeds the model's hoop tension; the sphere shape
  lets each ball find its own polarity.

### The one channel (identical for every magnet)

```
Ø1.4 window ← spherical seat → Ø3.45 cylinder → short chamfered throat Ø3.1 → slide Ø3.60 (to perimeter + 3.6 mm)
```

The channel axis is straight (one revolve, so no boolean-junction faces). One axis works because the kiss
direction (out the bevel) and the load direction (in from the pocket) are only ~5° apart on this
shallow-dihedral dome.

- **Spherical seat + Ø1.4 window** — the front of the socket is a **sphere** (Ø3.45) sunk 1.577 mm behind the
  bevel, which the bevel truncates to the Ø1.4 window. Only a sphere seats the ball **concentric and flush**
  (front 0.01 mm proud) so neighbor magnets actually touch. *(A cone was tried and rejected: it seats the ball
  ~0.26 mm recessed → a ~0.5 mm gap between magnets.)*
- **Cylinder socket Ø3.45** — behind the sphere seat, a short cylinder gives the ball room to spin (set
  polarity) and is forgiving of exactly where it settles.
- **Short chamfered throat Ø3.1** — a brief V (chamfer down to Ø3.1, chamfer back up to the slide). The
  chamfers print open (no ledge — the old *stepped* Ø3.10 neck bridged shut on the first print), and because
  the pinch is short (**~0.1 mm of interference, vs the old 0.8 mm neck**) the ball pushes through easily with
  a tamper. Ø3.1 is a hair under the 3.175 ball → **light mechanical capture in ANY orientation** (panels
  horizontal, arc seats vertical), so gravity can't drop a rim magnet. **Final throat TBD by magnet fit test.**
- **Slide Ø3.60** — runs from the throat to the **perimeter** then **3.6 mm into the pocket** — just enough
  to drop the ball in and start a tamper rod straight.

*(Arc seat/splice magnets still use the older sphere-socket retention — they print vertically as clean holes,
so it's fine there; panel and arc sockets can be unified later once the fit is proven.)*

### How magnets are loaded (post-print, printer OFF)

Drop the ball into the slide from the pocket side, then push it with a small blunt rod (a **tamper**,
~2.5–3 mm) through the neck until it snaps into the socket flush at the window. The slide is the tamper's
guide. Panel edges load **perpendicular to the edge** from the pocket; arc seats load **up from the floor**;
arc splices load from the **inner face**.

### Keys (so wrong edges never mate)

Two magnets per edge at **t = 0.5 ± key**, symmetric about the midpoint, distinct per chord:

| A | B | C | D | E | F |
|---|---|---|---|---|---|
| ±0.14 | ±0.19 | ±0.24 | ±0.29 | ±0.34 | ±0.39 |

→ 21.6 mm apart on A edges, widening to 77.3 mm on F edges.

Splice keys: **3 magnets** stacked up the tall (T2·T3↔T5·T3) joints, **2** up the short
(T5·T3↔T2·T3) joints, ~7.7 mm apart, from 4 mm above the floor to 4 mm below the top.

---

## The coupon — dial in the neck before committing

The neck (Ø3.10) grips a Ø3.175 ball with only **0.075 mm of interference — smaller than a 0.4 mm
nozzle's dimensional repeatability (±0.1–0.15 mm).** So the *exact* neck that captures-and-holds while
still letting the ball spin can't be predicted; it must be measured on your machine.

A **coupon** is a small throwaway test print — not a whole panel. The useful one here is a **neck sweep**:
one small block with the real socket-neck-slide-window channel repeated ~5 times at
**neck = 2.9 / 3.0 / 3.1 / 3.2 / 3.3 mm**, printed in the same **horizontal channel orientation** as a
panel (outer-face-down). Drop a magnet in each; whichever neck snaps the ball past and holds it while it
still spins is your number. Then rebuild every panel/arc with that neck.

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

**Arcs — Black (a sixth, "ground" color).** The 10 base rim arcs print in **Black** — a step below even the
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

### Filament quantities (full dome — 200 panels + 10 arcs)

Printed masses are calibrated from a real slice (the 117.06 g face plate → **0.906 g/cm³** effective, which
already includes walls + infill), so these are build numbers, not solid-volume guesses.

Per part, printed: **T1 ≈ 8.0 g · T2 ≈ 9.6 g · T3-L/R ≈ 10.0 g · T4 ≈ 10.9 g · T5 ≈ 11.3 g**; arcs ≈ **23 g**
(T2·T3) and **20 g** (T5·T3).

Per color for the whole dome — net, and with a **+15 %** allowance for brim, purge, and the odd failed part:

| Color (Bambu) | Covers | Net | +15 % | 1 kg spools |
|---|---|---|---|---|
| **Jade White** | T1 ×30 | 240 g | 276 g | 1 |
| **Light Gray** | T2 ×35 | 336 g | 387 g | 1 |
| **Silver** | T3-L ×40 + T3-R ×40 | 800 g | 920 g | 1 |
| **Gray** (T4) | T4 ×40 | 436 g | 501 g | 1 |
| **Dark Gray** | T5 ×15 | 169 g | 195 g | 1 |
| **Black** | arcs ×10 | 215 g | 247 g | 1 |
| **Total** | 200 panels + 10 arcs | **2196 g** | **2525 g** | **6** |

Six colors, one 1 kg spool each — **~2.5 kg with margin**. The black is the lightest lift: the 10 arcs need
only ~215 g, so a single spool covers them several times over (and black is the cheapest, most available
stock). To collapse back to **five** spools instead, share the arcs onto **Dark Gray** with the T5 panels
(Dark Gray → ~442 g, still one spool).

---

## Print settings (Bambu P1S, 256 mm bed, 0.4 mm nozzle, one color at a time)

Standard:

- **Outer-face-down**, brim ON (~5 mm), **supports OFF**, elephant's-foot compensation ~0.15 mm.
- Do **not** auto-orient / "place on face" — parts are already flat and correctly oriented; just Auto-arrange.
- Full face (16 panels + 2 arcs) ≈ 3 plates.

For rounder holes and a crisper neck (the channels print as horizontal holes, whose tops tend to sag):

- **Layer height 0.16 mm** for panels (**0.12 mm** for the coupon) — thinner layers round the horizontal holes.
- **Calibrate flow rate / extrusion multiplier first** — over-extrusion is what closes small holes and tightens the neck.
- **Calibrate pressure advance** — keeps hole edges sharp instead of bulged.
- **Slow the outer wall / small-perimeter speed** (~50–100 mm/s) so the channel walls lay down cleanly.
- If slicing in **OrcaSlicer**, enable **X-Y hole compensation** to counter the typical hole under-sizing
  (Bambu Studio lacks a direct equivalent — lean on flow calibration there).
- The Ø1.4 window will likely print slightly under — that only *improves* retention, so it's fine.

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

Still open, to finalize with real magnets: the exact **throat diameter** (3.1 is the safe capture default;
loosen toward 3.2 only if it's too tight to seat), and confirming the window/throat print cleanly enough that
magnets seat and hold without hand-clearing.
