# Magnetic Geodesic Dome — Scale Model Spec Sheet

A 3D-printed, magnet-assembled scale model of a geodesic dome (Montreal Biosphère–inspired),
built as a proof-of-concept for an eventual full-size welded structure.

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

Color scheme (single color at a time):

- **5 greys** = 5 panel shapes (T1 lightest at the vertex clusters → T5 charcoal at the face centers;
  T3-L/R share a tone, magnets enforce chirality).
- **Clear / translucent** reserved for the rim arcs, so the base recedes.

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
