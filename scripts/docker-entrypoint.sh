#!/bin/bash
# Entrypoint for the reproducible-build image. Modes:
#   verify  (default) — build into a staging dir; check shape-equivalence
#                       against /repo/stl/ (tolerances tight enough that
#                       any drift is well below FDM print resolution).
#                       Also reports bit-identity as diagnostic info.
#   build             — build into /repo/stl/ (bind-mount /repo to write to host).
set -euo pipefail
cd /repo

STLS=(T1 T2 T3L T3R T4 T5 arc_T2 arc_T3L arc_T3R arc_T5)

run_builders() {
  local outdir="$1"
  STL_DIR="$outdir" python scripts/build_final_panels.py
  # build_arc_run also drops arc_run_plate.stl in CWD; keep it out of the outdir diff.
  (cd "$outdir" && STL_DIR="$outdir" python /repo/scripts/build_arc_run.py)
}

case "${1:-verify}" in
  build)
    run_builders /repo/stl
    echo "wrote stl/ under /repo (bind-mount the host repo to persist)."
    ;;
  verify)
    OUT=$(mktemp -d)
    run_builders "$OUT" >/dev/null
    STLS_STR="${STLS[*]}" OUT="$OUT" python <<'PY'
import os, sys, struct
import numpy as np, trimesh
STLS = os.environ['STLS_STR'].split()
OUT = os.environ['OUT']
BBOX_TOL_UM = 100.0     # 0.1 mm — coarser than any FDM nozzle
VOL_TOL_PCT = 1.0       # 1 % of the reference part's volume
fails = 0
byte_ok = 0
print(f"{'file':14s} {'bytes':6s} {'Δbbox':>9s} {'Δvol':>10s} {'result':6s}")
for name in STLS:
    a_path = f"{OUT}/{name}.stl"
    b_path = f"/repo/stl/{name}.stl"
    same_bytes = open(a_path,'rb').read() == open(b_path,'rb').read()
    if same_bytes: byte_ok += 1
    a = trimesh.load(a_path); b = trimesh.load(b_path)
    d_bbox_um = float(np.max(np.abs(a.bounds - b.bounds))) * 1000.0
    d_vol_mm3 = abs(a.volume - b.volume)
    d_vol_pct = 100.0 * d_vol_mm3 / max(abs(b.volume), 1e-9)
    ok = d_bbox_um <= BBOX_TOL_UM and d_vol_pct <= VOL_TOL_PCT
    print(f"{name+'.stl':14s} {'==' if same_bytes else '≠ ':6s} "
          f"{d_bbox_um:6.2f} µm {d_vol_mm3:7.3f} mm³ {'OK' if ok else 'FAIL':6s}")
    if not ok: fails += 1
print()
print(f"{byte_ok}/{len(STLS)} bit-identical, {len(STLS)-fails}/{len(STLS)} shape-equivalent "
      f"(Δbbox ≤ {BBOX_TOL_UM:.0f} µm, Δvol ≤ {VOL_TOL_PCT:.1f}%)")
sys.exit(1 if fails else 0)
PY
    ;;
  shell)
    exec /bin/bash
    ;;
  *)
    echo "Usage: verify | build | shell"
    exit 2
    ;;
esac
