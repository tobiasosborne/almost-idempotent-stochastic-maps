#!/usr/bin/env python3 -u
"""
d7_exponent.py -- the REGIME / EXPONENT check at the FTI-2 floor (methodology step 5).

The decided floor is delta/H^2 ~ 3.49 (max-neg units), attained on the d3 exposedness-
boundary envelope where dist/tau ~ 0.54 (H ~ tau).  Question: along REALIZABLE families,
does delta scale as H^2 (the conjecture's binding form) or H (the d5 linear claim)?

We CONTROL the geometry instead of random sampling (which under-finds the envelope at small
tau -> a spurious p~1 fit, see d3 report).  We build the WORST hidden config explicitly: a
ring-shadowed far pair tuned so the v's sit AT the (Cτ,cτ) exposedness boundary (margin ~
kappa), then sweep delta DOWN by 4x and record the MAX achievable H at each delta.  We fit
log H vs log delta on the controlled family.

OUTCOME we expect (if FTI-2 holds with the d3 floor): H_max ~ sqrt(delta)*0.54, i.e.
delta ~ 3.4 H^2 (p=2 as the binding inequality); delta/H -> 0 as delta -> 0 (so the linear
delta~H/2 does NOT bind except at H~tau~O(1)).
"""
import json, os
import numpy as np
from d1_infra import neg_mass, dist1_to_conv, check_idempotent, exposed_margin
from d3_vertexfix import well_exposed_set_robust, is_row_vertex_robust
from d3_main import bary_to_P

OUTDIR = "out"; os.makedirs(OUTDIR, exist_ok=True)
C, c = 4.0, 0.25


def build_ring(r, ma, g, w, nh, rad, rng):
    pillar = ma - 1; a1, a2 = 0, 1 % ma
    bary = [np.eye(r)[a] for a in range(r)]
    v1 = np.zeros(r); v1[pillar] = 1 + g; v1[a1] = -g
    v2 = np.zeros(r); v2[pillar] = 1 + g; v2[a2] = -g
    if r > ma: v1[ma % r] += w / 2; v1[pillar] -= w / 2
    if r > ma + 1: v2[(ma + 1) % r] -= w / 2; v2[pillar] += w / 2
    rows = bary + [v1, v2]; iv1, iv2 = r, r + 1
    mid = (v1 + v2) / 2
    for hh in range(nh):
        d = rng.normal(size=r); d = d - d.mean(); d = d / (np.abs(d).sum() + 1e-12)
        rows.append(mid + rad * d)
    return bary_to_P(rows, r), iv1, iv2


def measure(P, iv1, iv2):
    chk = check_idempotent(P, tol=1e-9); nm, delta = neg_mass(P)
    if not chk["ok"] or delta <= 1e-12:
        return None
    tau = float(np.sqrt(delta)); rho, kappa = C * tau, c * tau
    W, _ = well_exposed_set_robust(P, rho, kappa)
    d1, _ = dist1_to_conv(P, W, iv1); d2, _ = dist1_to_conv(P, W, iv2)
    H = min(d1, d2)
    ok1, m1, _ = exposed_margin(P, iv1, rho, kappa)
    ok2, m2, _ = exposed_margin(P, iv2, rho, kappa)
    v1v, _ = is_row_vertex_robust(P, iv1); v2v, _ = is_row_vertex_robust(P, iv2)
    distinct = np.abs(P[iv1] - P[iv2]).sum() > 1e-7
    entered = bool(distinct and v1v and v2v and (not ok1) and (not ok2) and H > 1e-9)
    return {"delta": float(delta), "tau": tau, "H": float(H), "entered": entered,
            "m1": m1, "m2": m2, "kappa": kappa,
            "delta_over_H2": float(delta / H ** 2) if H > 1e-9 else None,
            "delta_over_H": float(delta / H) if H > 1e-9 else None}


def main():
    res = {"meta": {"normalization": "delta=max-row-neg (d3 units)"}, "controlled": []}
    # For each target delta (=g, since canonical poke neg=g), find the MAX H over a ring
    # radius sweep that keeps the hypothesis ENTERED, at fixed r,ma. This traces the
    # achievable envelope as we shrink delta 4x.
    r, ma, w, nh = 6, 4, 0.0, 4
    gs = [0.32, 0.16, 0.08, 0.04, 0.02, 0.01]    # delta down by 2x each (>4x total)
    rads = np.linspace(0.002, 0.5, 120)
    for g in gs:
        bestH = -1.0; bestrec = None
        for rad in rads:
            for rep in range(4):
                rng = np.random.default_rng(int(1e6 * g) + int(1e4 * rad) + rep)
                P, iv1, iv2 = build_ring(r, ma, g, w, nh, rad, rng)
                m = measure(P, iv1, iv2)
                if m is None or not m["entered"]:
                    continue
                if m["H"] > bestH:
                    bestH = m["H"]; bestrec = dict(m, g=g, rad=float(rad))
        if bestrec:
            res["controlled"].append(bestrec)
            print(f"  delta~{g:.3f}: max H (entered) = {bestH:.5f}  delta/H^2="
                  f"{bestrec['delta_over_H2']:.3f}  delta/H={bestrec['delta_over_H']:.4f}",
                  flush=True)
        else:
            print(f"  delta~{g:.3f}: NO entered config found", flush=True)
    # fit H ~ delta^q  (q=1/2 => delta~H^2)
    arr = res["controlled"]
    if len(arr) >= 3:
        dl = np.log([a["delta"] for a in arr]); hl = np.log([a["H"] for a in arr])
        q = np.polyfit(dl, hl, 1)[0]
        res["fit"] = {"H_vs_delta_exponent_q": float(q),
                      "implied_delta_vs_H_exponent_p": float(1.0 / q) if q != 0 else None,
                      "delta_over_H2_values": [a["delta_over_H2"] for a in arr],
                      "delta_over_H_values": [a["delta_over_H"] for a in arr]}
        print(f"\n  FIT: H ~ delta^{q:.3f}  => delta ~ H^{1/q:.3f}", flush=True)
        print(f"  delta/H^2 across the family: "
              f"{[round(a['delta_over_H2'],2) for a in arr]}", flush=True)
        print(f"  delta/H across the family (->0 confirms H^2 not H): "
              f"{[round(a['delta_over_H'],4) for a in arr]}", flush=True)
    with open(os.path.join(OUTDIR, "d7_exponent.json"), "w") as f:
        json.dump(res, f, indent=2, default=float)


if __name__ == "__main__":
    main()
