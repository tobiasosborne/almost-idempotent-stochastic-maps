#!/usr/bin/env python3 -u
"""
d3_main.py -- THE envelope experiment.  Mines env(H) := min max-row-neg over EXACT
idempotents with some row at honest dist_1(.,conv W) >= H, fits the exponent, runs
controls and the adversarial-R check.

KEY EMPIRICAL STRUCTURE established in the smoke tests (see d3-envelope-report.md):
 * In the canonical family R=[I_r|0], rows are barycentric coords in the (r-1)-simplex;
   neg(row)=ell^1 mass of negative coords; ell^1 row-distance = ell^1 bary-distance.
 * A far cluster of DISTINCT vertices is ALWAYS well-exposed at (rho,kappa)=(C tau,c tau)
   -> joins W -> distance collapses.  The ONLY way to be hidden is to be a NON-VERTEX
   (the cheapest: a coincident cluster, or an interior point of a far cluster whose
   supporting vertices are themselves non-exposed).
 * With realized rows pinned, max-neg is determined and R is irrelevant (verified:
   adversarial R never lowers the cost).  So the adversarial lever lives entirely in the
   choice of the cheapest hidden realized geometry -> the bary-coord LP envelope_lp.

We therefore sweep the bary LP, but parametrize by the *honest verified distance* H_true
(not the LP's anchor-face separator), and fit log(env) vs log(H_true).

FAMILIES:
  F1 "coincident-poke": a cluster of m coincident rows poking beyond a pillar by g
     (bary (-g,0,1+g,...)).  Non-vertex (coincident) -> stays out of W.  We sweep g.
  F2 "interior-of-far": a genuine far simplex of distinct vertices PLUS an interior
     centroid row; the centroid is the hidden non-vertex.  Tests whether a NON-coincident
     hidden config also costs ~ linear (the vertices are exposed & join W, so the
     centroid's distance to conv W is set by how far the centroid sits beyond the
     exposed-vertex hull; we measure neg vs that distance).
CONTROLS:
  C1 isolated far row (should expose -> verified_hidden False).
  C2 inside circuit (interior point inside conv W -> dist 0, neg 0).
Outputs out/d3_main.json crash-safe.
"""
import sys, os, json, time
import numpy as np

from d1_infra import (neg_mass, well_exposed_set, dist1_to_conv, exposed_margin,
                      is_row_vertex, check_idempotent)
from d3_envelope import alternating_min, verify, lp_optimize_R

OUT = "out/d3_main.json"
RES = {"meta": {"created": time.strftime("%Y-%m-%d %H:%M:%S"), "C": 4.0, "c": 0.25},
       "F1": [], "F2": [], "controls": [], "fits": {}, "Ccc_sweep": []}


def save():
    with open(OUT, "w") as f:
        json.dump(RES, f, indent=2, default=float)


def bary_to_P(bary_rows, r):
    """Given r archetype rows e_0..e_{r-1} and extra rows as bary coords (each len r),
       build the EXACT n x n idempotent P = Lam R0 with R0=[I_r|0].
       bary_rows includes the r archetype rows (=identity rows) followed by hidden rows.
       n = len(bary_rows). P[i,:] = (Lam[i,:], 0,...,0) padded to n cols."""
    Lam = np.asarray(bary_rows, float)        # n x r
    n = Lam.shape[0]
    R0 = np.zeros((r, n)); R0[:, :r] = np.eye(r)
    return Lam @ R0


# ---------------------------------------------------------------------------
# F1: coincident poke cluster.  r archetypes, anchors A, pillar p.  m coincident
# hidden rows at bary lam = e_p + g*(e_p - mean(A))*scale... we use the explicit
# poke (-g on one anchor, 1+g on pillar) which has neg=g and pokes beyond the pillar.
# ---------------------------------------------------------------------------
def build_F1(r, anchor_a, pillar, g, m=3):
    """rows: e_0..e_{r-1}, then m coincident rows = e_pillar pushed by g beyond,
       with -g on anchor_a, 1+g on pillar.  neg = g."""
    rows = [np.eye(r)[a] for a in range(r)]
    lam = np.zeros(r); lam[pillar] = 1 + g; lam[anchor_a] = -g
    for _ in range(m):
        rows.append(lam.copy())
    P = bary_to_P(rows, r)
    return P, list(range(r, r + m))


def run_F1(r=5, anchor_a=0, pillar=2, m=3, gs=None, C=4.0, c=0.25):
    if gs is None:
        gs = np.concatenate([np.linspace(0.01, 0.2, 12), np.linspace(0.25, 2.0, 14)])
    print(f"[F1] r={r} anchor={anchor_a} pillar={pillar} m={m} coincident-poke", flush=True)
    for g in gs:
        P, hid = build_F1(r, anchor_a, pillar, float(g), m=m)
        v = verify(P, hid, C=C, c=c, H_target=None)
        rec = {"g": float(g), "r": r, "m": m,
               "max_neg": v["max_neg"], "delta": v.get("delta"),
               "tau": v.get("tau"), "nW": v.get("nW"), "W": v.get("W"),
               "dist": v.get("max_hidden_dist"),
               "verified": v.get("verified_hidden"),
               "hidden_in_W": v.get("hidden_in_W")}
        RES["F1"].append(rec);
        print(f"  g={g:.3f}: neg={v['max_neg']:.4f} dist={v.get('max_hidden_dist')} "
              f"verif={v.get('verified_hidden')} |W|={v.get('nW')}", flush=True)
    save()


# ---------------------------------------------------------------------------
# F2: interior-of-far.  A far simplex of distinct vertices (these EXPOSE & join W)
# plus an interior centroid pushed a bit beyond, measuring neg vs its dist to conv W.
# We push the centroid 'further out' than the convex hull of the far vertices by t,
# making it a non-vertex just outside conv(far vertices) -> hidden by amount ~ t.
# ---------------------------------------------------------------------------
def build_F2(r, anchors, pillar, base_g, t, kfar=3):
    """far vertices: kfar distinct rows poking beyond pillar by base_g, spread in
       tangent dirs (distinct, will be exposed).  hidden row = their centroid pushed
       OUT by extra t beyond pillar (so just outside conv(far verts))."""
    rows = [np.eye(r)[a] for a in range(r)]
    far = []
    for j in range(kfar):
        lam = np.zeros(r); lam[pillar] = 1 + base_g; lam[anchors[0]] = -base_g
        # spread in tangent: shift mass between pillar and a different anchor
        if len(anchors) > 1:
            sh = 0.1 * (j - (kfar - 1) / 2)
            lam[anchors[1 % len(anchors)]] += sh; lam[pillar] -= sh
        far.append(lam); rows.append(lam)
    cen = np.mean(far, axis=0)
    # push centroid further beyond pillar by t
    hid_lam = cen.copy(); hid_lam[pillar] += t; hid_lam[anchors[0]] -= t
    rows.append(hid_lam)
    n0 = r
    far_idx = list(range(n0, n0 + kfar))
    hid_idx = [n0 + kfar]
    P = bary_to_P(rows, r)
    return P, far_idx, hid_idx


def run_F2(r=6, anchors=(0, 1), pillar=2, kfar=3, base_g=0.3, ts=None, C=4.0, c=0.25):
    if ts is None:
        ts = np.concatenate([np.linspace(0.0, 0.2, 10), np.linspace(0.3, 1.5, 10)])
    print(f"[F2] r={r} anchors={anchors} pillar={pillar} kfar={kfar} base_g={base_g}", flush=True)
    for t in ts:
        P, far_idx, hid = build_F2(r, list(anchors), pillar, base_g, float(t), kfar=kfar)
        v = verify(P, hid, C=C, c=c, H_target=None)
        rec = {"t": float(t), "base_g": base_g, "r": r, "kfar": kfar,
               "max_neg": v["max_neg"], "delta": v.get("delta"), "tau": v.get("tau"),
               "nW": v.get("nW"), "W": v.get("W"), "dist": v.get("max_hidden_dist"),
               "verified": v.get("verified_hidden"), "hidden_in_W": v.get("hidden_in_W"),
               "far_idx": far_idx, "far_in_W": [i for i in far_idx if i in (v.get("W") or [])]}
        RES["F2"].append(rec)
        print(f"  t={t:.3f}: neg={v['max_neg']:.4f} dist={v.get('max_hidden_dist')} "
              f"verif={v.get('verified_hidden')} |W|={v.get('nW')} "
              f"far_in_W={rec['far_in_W']}", flush=True)
    save()


def run_controls(C=4.0, c=0.25):
    print("[controls]", flush=True)
    # C1 isolated far row
    for g in [0.3, 0.6, 1.0]:
        r = 4
        rows = [np.eye(r)[a] for a in range(r)]
        lam = np.zeros(r); lam[2] = 1 + g; lam[0] = -g
        rows.append(lam)
        P = bary_to_P(rows, r); hid = [r]
        v = verify(P, hid, C=C, c=c)
        RES["controls"].append({"ctrl": "isolated_far", "g": g, "dist": v.get("max_hidden_dist"),
                                "verified": v.get("verified_hidden"), "in_W": v.get("hidden_in_W")})
        print(f"  C1 isolated g={g}: dist={v.get('max_hidden_dist')} "
              f"verified_hidden={v.get('verified_hidden')} (expect False)", flush=True)
    # C2 inside circuit: a point INSIDE the simplex (all positive) -> neg 0, dist 0
    r = 4
    rows = [np.eye(r)[a] for a in range(r)]
    rows.append(np.ones(r) / r)   # centroid, interior
    P = bary_to_P(rows, r); hid = [r]
    nm, delta = neg_mass(P)
    RES["controls"].append({"ctrl": "inside_centroid", "delta": float(delta),
                            "note": "interior point, neg=0"})
    print(f"  C2 inside centroid: delta={delta} (expect 0; neg-free interior)", flush=True)
    save()


def fit_exponent(pairs, label):
    """pairs: list of (dist, max_neg) verified. Fit log neg = p log dist + b."""
    arr = np.array([(d, m) for (d, m) in pairs if d is not None and d > 1e-9 and m > 1e-12])
    if len(arr) < 2:
        RES["fits"][label] = {"p": None, "n": len(arr)}
        return
    x = np.log(arr[:, 0]); y = np.log(arr[:, 1])
    A = np.vstack([x, np.ones_like(x)]).T
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    p, b = coef
    yhat = A @ coef
    ss_res = float(((y - yhat) ** 2).sum()); ss_tot = float(((y - y.mean()) ** 2).sum())
    r2 = 1 - ss_res / ss_tot if ss_tot > 1e-15 else 1.0
    # also robust slope between consecutive points (local exponent)
    local = []
    s = arr[np.argsort(arr[:, 0])]
    for i in range(1, len(s)):
        if s[i, 0] > s[i - 1, 0] and s[i, 1] > 0 and s[i - 1, 1] > 0:
            local.append((np.log(s[i, 1]) - np.log(s[i - 1, 1])) /
                         (np.log(s[i, 0]) - np.log(s[i - 1, 0])))
    RES["fits"][label] = {"p": float(p), "b": float(b), "r2": float(r2),
                          "n": int(len(arr)),
                          "local_p_min": float(min(local)) if local else None,
                          "local_p_max": float(max(local)) if local else None,
                          "local_p_med": float(np.median(local)) if local else None}
    print(f"[fit {label}] p={p:.3f} r2={r2:.4f} n={len(arr)} "
          f"local_p in [{min(local):.2f},{max(local):.2f}]" if local else
          f"[fit {label}] p={p:.3f}", flush=True)


if __name__ == "__main__":
    print("=" * 70, flush=True)
    print("d3_main: envelope env(H) + exponent fit + controls", flush=True)
    print("=" * 70, flush=True)
    run_controls()
    # F1 at several (r, anchor, pillar, m)
    for (r, a, p, m) in [(5, 0, 2, 3), (5, 0, 2, 1), (6, 0, 3, 4), (4, 0, 2, 2)]:
        run_F1(r=r, anchor_a=a, pillar=p, m=m)
    # F2
    for (r, anc, p, kf, bg) in [(6, (0, 1), 2, 3, 0.3), (6, (0, 1), 2, 4, 0.5),
                                (7, (0, 1, 2), 3, 3, 0.3)]:
        run_F2(r=r, anchors=anc, pillar=p, kfar=kf, base_g=bg)
    # fits (verified points only)
    f1pairs = [(x["dist"], x["max_neg"]) for x in RES["F1"] if x.get("verified")]
    f2pairs = [(x["dist"], x["max_neg"]) for x in RES["F2"] if x.get("verified")]
    fit_exponent(f1pairs, "F1_coincident_poke")
    fit_exponent(f2pairs, "F2_interior_of_far")
    fit_exponent(f1pairs + f2pairs, "ALL")
    save()
    print("\nDONE. saved", OUT, flush=True)
