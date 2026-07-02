#!/usr/bin/env python3 -u
"""
d7_ringedge.py -- the REFUTATION test: can the ring-shell hidden regime drive delta/H^2
BELOW the d3 envelope floor (~3.49 in max-neg units)?  If yes at any radius -> refutation
candidate.  We finely scan the ring radius near the exposedness EDGE (margin ~ kappa, where
H is maximal for given delta), for a few (delta, frame) cells, and track the global min
delta/H^2 over HYPOTHESIS-ENTERED verified points.  Crash-safe; flushed.
"""
import json, os
import numpy as np
from d7_exponent import build_ring, measure

OUTDIR = "out"; os.makedirs(OUTDIR, exist_ok=True)


def main():
    res = {"meta": {"normalization": "delta=max-row-neg (d3 units)", "d3_floor": 3.49},
           "scan": [], "global_min": None}
    OUT = os.path.join(OUTDIR, "d7_ringedge.json")
    gmin = 1e18; grec = None; count = 0
    cells = [(0.08, 5, 3), (0.08, 6, 4), (0.16, 6, 4), (0.32, 6, 4), (0.04, 6, 4)]
    rads = np.linspace(0.002, 0.7, 100)
    for (g, r, ma) in cells:
        cellmin = 1e18; cellrec = None
        for rad in rads:
            for rep in range(3):
                rng = np.random.default_rng(int(1e7 * g) + int(1e5 * rad) + rep + 1000 * r + ma)
                P, iv1, iv2 = build_ring(r, ma, g, 0.0, 4, rad, rng)
                m = measure(P, iv1, iv2)
                count += 1
                if m is None or not m["entered"]:
                    continue
                if m["delta_over_H2"] < cellmin:
                    cellmin = m["delta_over_H2"]
                    cellrec = {"g": g, "r": r, "ma": ma, "rad": float(rad),
                               "delta": m["delta"], "H": m["H"],
                               "delta_over_H2": m["delta_over_H2"],
                               "m1": float(m["m1"]), "m2": float(m["m2"]),
                               "kappa": float(m["kappa"])}
        if cellrec:
            res["scan"].append(cellrec)
            if cellmin < gmin:
                gmin = cellmin; grec = cellrec
            print(f"  cell g={g} r={r} ma={ma}: min delta/H^2={cellmin:.3f} "
                  f"(H={cellrec['H']:.4f} rad={cellrec['rad']:.3f})", flush=True)
        else:
            print(f"  cell g={g} r={r} ma={ma}: NO entered config", flush=True)
        with open(OUT, "w") as f:
            json.dump(res, f, indent=2, default=float)
    res["global_min"] = grec
    res["verdict"] = ("REFUTATION (delta/H^2 < d3 floor 3.49)" if gmin < 3.49 else
                      f"SUPPORTED: ring-regime floor delta/H^2 >= {gmin:.1f} (>> d3 floor 3.49)")
    with open(OUT, "w") as f:
        json.dump(res, f, indent=2, default=float)
    print(f"\n[d7-ringedge] {count} configs. GLOBAL min delta/H^2 = {gmin:.3f}", flush=True)
    print(f"  {res['verdict']}", flush=True)


if __name__ == "__main__":
    main()
