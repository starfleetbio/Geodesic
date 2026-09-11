# Getting the dome plates into Bambu Studio (first-timer walkthrough)

Your files: 30 plate STLs (e.g. `T1_plate1.stl`), each already holding several panels laid **flat, outer-face-down**.
On the P1S you print **one color at a time**, so the color is the spool you load — not something you paint in software.

---

## 0. One-time setup (do once)

1. Download **Bambu Studio** from Bambu Lab's site and install it.
2. On first launch it asks for your printer — pick **Bambu Lab P1S**, **0.4 mm nozzle**.
3. Set the filament to **Bambu PLA Basic** (or "Generic PLA") in the filament dropdown, top-right.
4. Connect the printer over your network, or plan to export to the SD card. Either is fine.

---

## Then, per the Bambu workflow — do this one plate at a time

### 1 · Import 3D model
- Drag one plate file (start with **`T1_plate1.stl`**) onto the build plate, or **File → Import → Import STL**.
- It arrives as **one object containing ~12 panels**. Right-click it → **Split → To Objects** (sometimes "Split to Parts") so each panel is separate. This lets the slicer treat them individually and shows you nothing overlaps.
- **Do NOT** hit auto-orient / "Place on face" / auto-arrange — the panels are already correctly flat and outer-face-down, and those tools would re-tilt or shuffle them. (Only if you get an "outside the plate" warning, use **Auto-arrange**, which keeps them flat.)

### 2 · Edit & Colorize
- For single-color printing there's nothing to paint. Just set the top-right filament to the grey this plate uses, so the preview matches — optional, only for your own tracking.
- (Colorize/paint only matters if you later add an AMS for multi-color. Skip it now.)

### 3 · Verify → Slice & Print **test**  (⇄ Tune / Refine loop)
Set these in the left-hand settings, then slice:
- **Layer height** 0.2 mm (or 0.16 for a finer exterior).
- **Brim: ON**, outer, ~5 mm — the thin panels and arc walls need the extra grip.
- **Elephant's-foot compensation** ~0.15 mm (keeps the first layer from bulging over the magnet windows).
- **Supports: OFF** — flat parts need none. If the slicer wants supports, something is tilted; re-check step 1.
- Infill 10–15% (the parts are mostly solid rim anyway).

Click **Slice Plate**, check the preview (no supports, sane time/filament), then **print this one plate**.
When it's done, drop real 1/8″ magnets into a few sockets and confirm: the ball **snaps past the neck and stays**, and still **spins** in the socket. If it's too tight, too loose, or the first layer closed the windows → that's the **Refine parameters** loop: tweak the slicer setting, or tell me and I'll adjust the model's neck/window numbers and regenerate. Re-test until the fit feels right.

### 4 · Add Project Resource files
- Once the settings are dialed, keep them. Use the **plate tabs at the bottom** → **Add Plate**, and import the next STL onto its own plate — or just handle one color group at a time.
- "Project resources" = your models + tuned settings + arrangement, all held together in the project.

### 5 · Pack into a .3mf
- **File → Save Project As → `.3mf`**. That bundles the models, layout, and your slicer settings into one reopenable file.
- Practical tip for 30 plates: save **one .3mf per color** (e.g. `grey1_T1.3mf`), so reprinting a color is one click.

---

## Print order (load spool → print that color's plates)

| Spool | Plates | Files |
|---|---|---|
| grey1 (lightest) | 3 | T1_plate1–3 |
| grey2 | 3 | T2_plate1–3 |
| grey3 (mid) | 8 | T3L_plate1–4, T3R_plate1–4 |
| grey4 | 7 | T4_plate1–7 |
| grey5 (charcoal) | 3 | T5_plate1–3 |
| clear | 6 | arcT2T3_plate1–3, arcT5T3_plate1–3 |

Do **grey1 T1_plate1 as the test print first.** Everything else waits until the magnet fit checks out.
