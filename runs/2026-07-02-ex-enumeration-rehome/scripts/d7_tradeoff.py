#!/usr/bin/env python3 -u
"""
d7_tradeoff.py -- the DECISIVE refinement: the (H, margin, delta) tradeoff of the ring shell.

The d7 hunt showed the FTI-2 hypothesis CAN be entered (distinct far vertices both failing
exposedness) ONLY via a helper "ring" shell -- but in every such case H (= dist to conv W)
COLLAPSED toward 0 because the ring rows EXPAND conv W almost up to the v's, so delta/H^2
blew up (300..25000), the OPPOSITE of a refutation.  The genuine refutation channel would
be: a shell that BREAKS the exposer (margin < kappa) while KEEPING the v's far from conv W
(H >= target).  This module decides whether that channel exists by densely sweeping the ring
RADIUS and the poke g, recording the full joint (H, margin, delta, delta/H^2) curve, and
finding the MINIMUM delta/H^2 over all HYPOTHESIS-ENTERED (verified) points.

If min delta/H^2 over entered points has a positive floor comparable to (or above) the d3
band ~3.4 -> FTI-2 SUPPORTED.  If it dips toward 0 -> refutation candidate (STOP).

Crash-safe JSON; robust verification only.
"""
import json, os, itertools
import numpy as np
from d1_infra import neg_mass, dist1_to_conv, check_idempotent, exposed_margin
from d3_vertexfix import well_exposed_set_robust, is_row_vertex_robust
from d3_main import bary_to_P

OUTDIR = "out"; os.makedirs(OUTDIR, exist_ok=True)
C, c = 4.0, 0.25


def build(r, ma, g, w, nh, rad, rng, shell="ring"):
    pillar = ma - 1; a1, a2 = 0, 1 % ma
    bary = [np.eye(r)[a] for a in range(r)]
    anchors = list(range(ma))
    v1 = np.zeros(r); v1[pillar] = 1 + g; v1[a1] = -g
    v2 = np.zeros(r); v2[pillar] = 1 + g; v2[a2] = -g
    if r > ma: v1[ma % r] += w / 2; v1[pillar] -= w / 2
    if r > ma + 1: v2[(ma + 1) % r] -= w / 2; v2[pillar] += w / 2
    rows = bary + [v1, v2]; iv1, iv2 = r, r + 1
    mid = (v1 + v2) / 2
    for hh in range(nh):
        if shell == "ring":
            d = rng.normal(size=r); d = d - d.mean(); d = d / (np.abs(d).sum() + 1e-12)
            rows.append(mid + rad * d)
        elif shell == "between":
            t = (hh + 1) / (nh + 1); rows.append((1 - t) * v1 + t * v2)
        elif shell == "cap":
            # a single 'cap' row beyond the v-pair toward +pillar, distance rad
            base_pt = np.eye(r)[pillar]
            rows.append((1 - rad) * mid + rad * base_pt)
    return bary_to_P(rows, r), iv1, iv2, anchors


def verify(P, v1, v2):
    chk = check_idempotent(P, tol=1e-9); nm, delta = neg_mass(P)
    if not chk["ok"] or delta <= 1e-12:
        return None
    tau = float(np.sqrt(delta)); rho, kappa = C * tau, c * tau
    W, _ = well_exposed_set_robust(P, rho, kappa)
    d1, _ = dist1_to_conv(P, W, v1); d2, _ = dist1_to_conv(P, W, v2)
    H = min(d1, d2)
    ok1, m1, _ = exposed_margin(P, v1, rho, kappa)
    ok2, m2, _ = exposed_margin(P, v2, rho, kappa)
    vert1, _ = is_row_vertex_robust(P, v1); vert2, _ = is_row_vertex_robust(P, v2)
    distinct = np.abs(P[v1] - P[v2]).sum() > 1e-7
    entered = bool(distinct and vert1 and vert2 and (not ok1) and (not ok2) and H > 1e-9)
    return {"delta": float(delta), "tau": tau, "kappa": float(kappa), "nW": len(W),
            "H": float(H), "m1": (None if m1 is None else float(m1)),
            "m2": (None if m2 is None else float(m2)),
            "v1_fails": bool(not ok1), "v2_fails": bool(not ok2),
            "distinct": bool(distinct), "entered": entered,
            "delta_over_H2": float(delta / H ** 2) if H > 1e-9 else None}


def main():
    res = {"meta": {"normalization": "delta=max-row-neg (d3 units)", "C": C, "c": c},
           "curve": [], "entered_min": None, "refutation": None}
    OUT = os.path.join(OUTDIR, "d7_tradeoff.json")
    rs = [4, 5, 6]; mas = [3, 4]; gs = [0.05, 0.1, 0.2, 0.3]; ws = [0.0, 0.02, 0.05]
    nhs = [2, 4, 6]; rads = list(np.linspace(0.005, 0.6, 24)); shells = ["ring", "cap"]
    NREP = 6
    best_entered = None
    count = 0
    for (r, ma, g, w, nh, shell) in itertools.product(rs, mas, gs, ws, nhs, shells):
        if ma > r: continue
        for rad in rads:
            nrep = NREP if shell == "ring" else 1
            for rep in range(nrep):
                rng = np.random.default_rng(777 * count + rep)
                P, iv1, iv2, _ = build(r, ma, g, w, nh, rad, rng, shell=shell)
                v = verify(P, iv1, iv2)
                count += 1
                if v is None: continue
                if v["entered"]:
                    rec = {"r": r, "ma": ma, "g": g, "w": w, "nh": nh, "shell": shell,
                           "rad": float(rad), "delta": v["delta"], "H": v["H"],
                           "delta_over_H2": v["delta_over_H2"], "m1": v["m1"], "m2": v["m2"],
                           "kappa": v["kappa"], "nW": v["nW"]}
                    res["curve"].append(rec)
                    if best_entered is None or v["delta_over_H2"] < best_entered["delta_over_H2"]:
                        best_entered = rec
                        res["entered_min"] = best_entered
                        if v["delta_over_H2"] < 1.0:    # below d3 band -> candidate refutation
                            res["refutation"] = dict(rec, P=P.tolist())
                            with open(os.path.join(OUTDIR, "d7_refutation.json"), "w") as f:
                                json.dump(res["refutation"], f, indent=2, default=float)
                            print(f"  !!! CANDIDATE REFUTATION delta/H^2={v['delta_over_H2']:.4f}",
                                  flush=True)
        if count % 2000 < 100:
            with open(OUT, "w") as f:
                json.dump(res, f, indent=2, default=float)
            be = best_entered["delta_over_H2"] if best_entered else None
            print(f"  ...{count} configs, entered_min delta/H^2={be}", flush=True)
    res["summary"] = {"n_configs": count, "n_entered": len(res["curve"]),
                      "min_delta_over_H2_entered": (best_entered["delta_over_H2"]
                                                    if best_entered else None),
                      "verdict": ("REFUTATION" if res["refutation"] else
                                  ("SUPPORTED: entered-region floor delta/H^2 >= "
                                   + (f"{best_entered['delta_over_H2']:.2f}" if best_entered
                                      else "inf (empty)")))}
    with open(OUT, "w") as f:
        json.dump(res, f, indent=2, default=float)
    print(f"\n[d7-tradeoff] {count} configs, {len(res['curve'])} entered. "
          f"min delta/H^2 (entered) = "
          f"{res['summary']['min_delta_over_H2_entered']}", flush=True)
    print(f"  verdict: {res['summary']['verdict']}", flush=True)


if __name__ == "__main__":
    main()
