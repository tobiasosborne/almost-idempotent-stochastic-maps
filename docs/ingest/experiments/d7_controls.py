#!/usr/bin/env python3 -u
"""
d7_controls.py -- the mandatory scientific controls for the d7 FTI-2 decider.

(i)  WITHOUT the failed-exposedness requirement, delta/H^2 can be ~0: a transient circuit
     of distinct vertices sits inside conv W (dist 0) so "height" without the non-exposed
     gate is meaningless; and an interior point can be far in a coordinate sense while
     dist(.,conv W)=0.  We verify the pipeline FINDS dist=0 (no spurious hidden rows).
(ii) In the CANONICAL frame, a poke vertex at coordinate-excursion g has neg = g and, when
     it is genuinely hidden (forced non-vertex via coincidence), dist = (something) with the
     LINEAR relation delta >= H/2 appearing -- we recover the d3/d5 linear floor delta ~ H/2.
(iii) The d3 thin-diamond floor delta/H^2 ~ 3.4-3.85 should be re-found: the coincident
     poke cluster (a NON-vertex hidden config) gives delta/dist^2 in that band.

These calibrate that the d7 verification gate reproduces KNOWN structure before we trust its
verdict on the open hypothesis.
"""
import json, os
import numpy as np
from d1_infra import neg_mass, dist1_to_conv, check_idempotent
from d3_vertexfix import well_exposed_set_robust, verify_robust
from d3_main import bary_to_P

OUTDIR = "out"; os.makedirs(OUTDIR, exist_ok=True)
C, c = 4.0, 0.25


def control_i_transient():
    """Distinct far vertices (no non-exposed gate): they expose -> dist 0.  Confirms the
       pipeline does NOT fabricate hidden rows.  delta/H^2 'effectively 0/undefined'."""
    r = 5
    out = []
    for g in [0.05, 0.1, 0.2]:
        rows = [np.eye(r)[a] for a in range(r)]
        v1 = np.zeros(r); v1[2] = 1 + g; v1[0] = -g
        v2 = np.zeros(r); v2[2] = 1 + g; v2[1] = -g
        rows += [v1, v2]
        P = bary_to_P(rows, r)
        v = verify_robust(P, [r, r + 1])
        out.append({"g": g, "delta": v["delta"], "dist": v["max_hidden_dist"],
                    "hidden": v["verified_hidden"], "nW": v["nW"]})
    return out


def control_ii_canonical_linear():
    """Coincident poke cluster (the only canonical hidden config): a NON-vertex far point.
       Measure delta vs dist; check the LINEAR floor delta ~ H/2 and the quadratic
       delta/H^2 ~ 3.4-3.85 band (d3)."""
    r = 5
    out = []
    for g in np.linspace(0.02, 0.4, 12):
        rows = [np.eye(r)[a] for a in range(r)]
        lam = np.zeros(r); lam[2] = 1 + g; lam[0] = -g
        for _ in range(3):           # coincident cluster -> non-vertex -> hidden
            rows.append(lam.copy())
        P = bary_to_P(rows, r)
        v = verify_robust(P, [r, r + 1, r + 2])
        H = v["max_hidden_dist"]
        rec = {"g": float(g), "delta": v["delta"], "dist": float(H),
               "hidden": v["verified_hidden"], "nW": v["nW"]}
        rec["delta_over_H"] = float(v["delta"] / H) if H > 1e-9 else None
        rec["delta_over_H2"] = float(v["delta"] / H ** 2) if H > 1e-9 else None
        out.append(rec)
    return out


def control_iii_d3_band():
    """Reproduce the d3 floor: from the saved d3 robust envelope (dist/tau bound), the
       worst-case delta/H^2 = 1/(max dist/tau)^2.  This is the floor FTI-2 must beat to
       be refuted.  We recompute it from out/d3_clean_scaling.json (robust W)."""
    try:
        d3 = json.load(open(os.path.join(OUTDIR, "d3_clean_scaling.json")))
    except Exception:
        return None
    env = d3["envelope"]; rows = []
    for tau, H in env:
        delta = tau ** 2
        rows.append({"tau": float(tau), "H": float(H), "delta": float(delta),
                     "delta_over_H2": float(delta / H ** 2) if H > 1e-9 else None})
    maxr = d3["global_max_ratio"]
    return {"per_bin": rows, "global_max_dist_over_tau": float(maxr),
            "floor_delta_over_H2": float(1.0 / maxr ** 2),
            "p99_dist_over_tau": float(d3["p99"]),
            "typical_delta_over_H2": float(1.0 / d3["p99"] ** 2)}


def main():
    res = {"control_i_transient": control_i_transient(),
           "control_ii_canonical": control_ii_canonical_linear(),
           "control_iii_d3_band": control_iii_d3_band()}
    # summaries
    ci = res["control_i_transient"]
    res["control_i_summary"] = {
        "all_dist_zero": all(abs(x["dist"]) < 1e-6 for x in ci),
        "none_hidden": all(not x["hidden"] for x in ci)}
    cii = [x for x in res["control_ii_canonical"] if x["hidden"]]
    if cii:
        dH = [x["delta_over_H"] for x in cii if x["delta_over_H"]]
        dH2 = [x["delta_over_H2"] for x in cii if x["delta_over_H2"]]
        res["control_ii_summary"] = {
            "n_hidden": len(cii),
            "delta_over_H_range": [float(min(dH)), float(max(dH))] if dH else None,
            "delta_over_H2_range": [float(min(dH2)), float(max(dH2))] if dH2 else None}
    with open(os.path.join(OUTDIR, "d7_controls.json"), "w") as f:
        json.dump(res, f, indent=2, default=float)
    print("[control i] distinct far vertices (no non-exposed gate):", flush=True)
    for x in ci:
        print(f"   g={x['g']}: delta={x['delta']:.4f} dist={x['dist']:.4f} "
              f"hidden={x['hidden']} (expect dist=0, hidden=False)", flush=True)
    print(f"   summary: all_dist_zero={res['control_i_summary']['all_dist_zero']} "
          f"none_hidden={res['control_i_summary']['none_hidden']}", flush=True)
    print("[control ii] coincident poke cluster (canonical hidden non-vertex):", flush=True)
    for x in res["control_ii_canonical"]:
        print(f"   g={x['g']:.3f}: delta={x['delta']:.4f} dist={x['dist']:.4f} "
              f"d/H={x['delta_over_H']} d/H^2={x['delta_over_H2']} hidden={x['hidden']}",
              flush=True)
    if "control_ii_summary" in res:
        print(f"   summary: delta/H in {res['control_ii_summary']['delta_over_H_range']}, "
              f"delta/H^2 in {res['control_ii_summary']['delta_over_H2_range']}", flush=True)


if __name__ == "__main__":
    main()
