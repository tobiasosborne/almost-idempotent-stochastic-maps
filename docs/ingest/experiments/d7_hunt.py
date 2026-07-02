#!/usr/bin/env python3 -u
"""
d7_hunt.py -- the DECISIVE FTI-2 hunt: actively drive v1,v2 INTO the non-exposed region.

The d7_drive sweep + every prior hunt finds the same wall: distinct far row-vertices are
ALWAYS (4tau, tau/4)-well-exposed, so they JOIN W and dist(v_j, conv W) collapses to 0 --
the FTI-2 hypothesis is never entered.  To DECIDE FTI-2 we must rule out that this is mere
search failure.  We therefore hunt DIRECTLY for the hypothesis region by minimizing the
exposedness MARGIN of the far vertices over exact (Lambda,R) completions, with helper rows
forming a candidate "shadow shell".  If the minimal achievable margin over all far distinct
configs stays >= kappa, the hypothesis is (numerically) EMPTY -> FTI-2 vacuously true; if it
dips below kappa at small delta, we have a candidate refutation and read off delta/H^2.

STRATEGY (random + structured multistart, robust verification):
  * Build exact idempotents with two distinct far vertices v1,v2 (poke targets) and a ring
    of helper rows placed to SHADOW them (each helper near the v's / between them and C), so
    that no affine h in [0,1] with h(v)=0 can lift all far rows above kappa.  We try MANY
    helper placements (the shell is where a refutation hides) -- coincident-with-v shells,
    ring shells, between-shells -- and for each compute the ROBUST exposedness margin and
    robust W.  We also let the canonical bary geometry vary (g, w, mu, helper radius).
  * For every config we record (delta, H=dist to conv W, margins, whether the hypothesis is
    entered).  The OUTPUT is the joint distribution: does (margin < kappa AND dist >= H) ever
    occur for DISTINCT VERTICES, and at what delta/H^2?

This is breadth in the helper-shell DOF (the blind spot) but depth on the one decisive
question.  Crash-safe JSON.
"""
import sys, os, json, time, itertools
import numpy as np

from d1_infra import check_idempotent, neg_mass, dist1_to_conv, exposed_margin
from d3_vertexfix import well_exposed_set_robust, is_row_vertex_robust
from d3_main import bary_to_P

OUTDIR = "out"; os.makedirs(OUTDIR, exist_ok=True)
C, c = 4.0, 0.25


def verify(P, v1, v2, anchors, H_target=None):
    P = np.asarray(P, float); n = P.shape[0]
    chk = check_idempotent(P, tol=1e-9)
    nm, delta = neg_mass(P)
    out = {"idem_ok": bool(chk["ok"]), "delta": float(delta)}
    if not chk["ok"] or delta <= 1e-12:
        out["pass"] = False; out["reason"] = "bad_or_zero"; return out
    tau = float(np.sqrt(delta)); rho, kappa = C * tau, c * tau
    W, _ = well_exposed_set_robust(P, rho, kappa)
    d1, _ = dist1_to_conv(P, W, v1); d2, _ = dist1_to_conv(P, W, v2)
    H = min(d1, d2)
    ok1, m1, _ = exposed_margin(P, v1, rho, kappa)
    ok2, m2, _ = exposed_margin(P, v2, rho, kappa)
    vert1, _ = is_row_vertex_robust(P, v1); vert2, _ = is_row_vertex_robust(P, v2)
    distinct = np.abs(P[v1] - P[v2]).sum() > 1e-7
    out.update({"tau": tau, "kappa": kappa, "nW": len(W), "W": list(map(int, W)),
                "dist_v1": float(d1), "dist_v2": float(d2), "H": float(H),
                "m1": (None if m1 is None else float(m1)),
                "m2": (None if m2 is None else float(m2)),
                "v1_fails": bool(not ok1), "v2_fails": bool(not ok2),
                "v1_vertex": bool(vert1), "v2_vertex": bool(vert2),
                "distinct": bool(distinct)})
    entered = bool(distinct and vert1 and vert2 and (not ok1) and (not ok2) and H > 1e-9)
    out["hypothesis_entered"] = entered
    out["delta_over_H2"] = float(delta / H ** 2) if H > 1e-9 else None
    out["pass"] = bool(entered and (H_target is None or H >= H_target - 1e-9))
    return out


def build_shell(r, ma, g, w, nh, shell_kind, shell_rad, rng):
    """Canonical-frame idempotent (R=[I_r|0]) with anchors e_0..e_{ma-1}, two distinct
       poke vertices v1,v2 beyond pillar (anchor ma-1), and nh helper rows forming a
       'shadow shell' around the v's.  Returns (P, v1_idx, v2_idx, anchor_idx)."""
    pillar = ma - 1
    a1, a2 = 0, 1 % ma
    bary = [np.eye(r)[a] for a in range(r)]    # r archetype rows
    anchors = list(range(r))[:ma]               # anchors are archetypes 0..ma-1 (in W)
    # v1, v2 poke beyond pillar via distinct anchors + thin transverse on axes ma, ma+1
    v1 = np.zeros(r); v1[pillar] = 1 + g; v1[a1] = -g
    v2 = np.zeros(r); v2[pillar] = 1 + g; v2[a2] = -g
    if r > ma:
        v1[ma % r] += w / 2; v1[pillar] -= w / 2
    if r > ma + 1:
        v2[(ma + 1) % r] -= w / 2; v2[pillar] += w / 2
    else:
        v2[a2] -= 1e-3; v2[pillar] += 1e-3
    rows = bary + [v1, v2]
    iv1, iv2 = r, r + 1
    # helper shell
    mid = (v1 + v2) / 2
    for hh in range(nh):
        if shell_kind == "coincident_v":
            h = v1.copy() if hh % 2 == 0 else v2.copy()
        elif shell_kind == "between":
            t = (hh + 1) / (nh + 1)
            h = (1 - t) * v1 + t * v2
        elif shell_kind == "ring":
            # near mid, pushed out radially by shell_rad along a random frame dir
            d = rng.normal(size=r); d = d - d.mean()
            d = d / (np.abs(d).sum() + 1e-12)
            h = mid + shell_rad * d
        elif shell_kind == "shadow":
            # explicitly: a row that is a near-combo making v1,v2 non-exposed: sit just
            # outside the v-pair on the C side so it 'caps' the exposer
            t = rng.uniform(0.3, 0.7)
            base_pt = np.eye(r)[pillar]
            h = (1 - shell_rad) * (t * v1 + (1 - t) * v2) + shell_rad * base_pt
        else:
            h = mid.copy()
        rows.append(h)
    P = bary_to_P(rows, r)
    return P, iv1, iv2, anchors


def main():
    t0 = time.time()
    OUT = os.path.join(OUTDIR, "d7_hunt.json")
    res = {"meta": {"created": time.strftime("%Y-%m-%d %H:%M:%S"), "C": C, "c": c,
                    "normalization": "delta=max-row-neg (d3 units)"},
           "entered": [], "near_misses": [], "min_margin_over_kappa": None,
           "refutation": None, "summary": {}}
    rs = [4, 5, 6]
    mas = [3, 4]
    gs = [0.05, 0.1, 0.2, 0.35]
    ws = [0.0, 0.01, 0.05]
    nhs = [0, 2, 4]
    shells = ["coincident_v", "between", "ring", "shadow", "none"]
    rads = [0.02, 0.1, 0.3]
    N_RING = 8        # random restarts for ring/shadow shells
    best_ratio_over_kappa = np.inf     # min over all far distinct vertices of margin/kappa
    best_ratio_rec = None
    count = 0
    combos = list(itertools.product(rs, mas, gs, ws, nhs, shells))
    print(f"[d7-hunt] {len(combos)} base combos x rads x rings. Deciding if hypothesis "
          f"is realizable for DISTINCT far vertices.", flush=True)
    for (r, ma, g, w, nh, shell) in combos:
        if ma > r:
            continue
        rad_list = rads if shell in ("ring", "shadow") else [0.0]
        nrestart = N_RING if shell in ("ring", "shadow") else 1
        if nh == 0 and shell != "none":
            continue
        if nh > 0 and shell == "none":
            continue
        for rad in rad_list:
            for rep in range(nrestart):
                rng = np.random.default_rng(10000 * count + rep)
                P, iv1, iv2, anchors = build_shell(r, ma, g, w, nh, shell, rad, rng)
                v = verify(P, iv1, iv2, anchors)
                count += 1
                if not v.get("idem_ok"):
                    continue
                # track the closest approach to the hypothesis for DISTINCT vertices:
                # margin/kappa over far vertices (we want to know if it ever < 1)
                if v.get("distinct") and v.get("v1_vertex") and v.get("v2_vertex") \
                        and v.get("kappa", 0) > 0 and v.get("H", 0) > 1e-9:
                    for mside in (v["m1"], v["m2"]):
                        if mside is not None:
                            rk = mside / v["kappa"]
                            if rk < best_ratio_over_kappa:
                                best_ratio_over_kappa = rk
                                best_ratio_rec = {"r": r, "ma": ma, "g": g, "w": w,
                                                  "nh": nh, "shell": shell, "rad": rad,
                                                  "margin": mside, "kappa": v["kappa"],
                                                  "margin_over_kappa": float(rk),
                                                  "delta": v["delta"], "H": v["H"],
                                                  "delta_over_H2": v["delta_over_H2"]}
                if v.get("hypothesis_entered"):
                    print(f"  !!! HYPOTHESIS ENTERED r={r} ma={ma} g={g} shell={shell} "
                          f"rad={rad}: delta/H^2={v['delta_over_H2']:.4f}", flush=True)
                    rec = dict(v); rec.update({"r": r, "ma": ma, "g": g, "w": w, "nh": nh,
                                               "shell": shell, "rad": rad, "P": P.tolist()})
                    res["entered"].append({k: rec[k] for k in rec if k != "P"})
                    if v["delta_over_H2"] is not None and v["delta_over_H2"] < 0.5:
                        res["refutation"] = rec
                        with open(os.path.join(OUTDIR, "d7_refutation.json"), "w") as f:
                            json.dump(rec, f, indent=2, default=float)
                # near miss: a far distinct vertex with small exposedness margin
                elif v.get("distinct") and v.get("H", 0) > 1e-9 and v.get("m1") is not None:
                    mm = min(x for x in (v["m1"], v["m2"]) if x is not None)
                    if mm < 2 * v.get("kappa", 0):
                        res["near_misses"].append(
                            {"r": r, "ma": ma, "g": g, "shell": shell, "rad": rad,
                             "min_margin": float(mm), "kappa": v["kappa"],
                             "H": v["H"], "delta": v["delta"]})
        if count % 200 < 20:
            res["min_margin_over_kappa"] = (None if best_ratio_rec is None
                                            else best_ratio_rec)
            with open(OUT, "w") as f:
                json.dump(res, f, indent=2, default=float)
    res["min_margin_over_kappa"] = best_ratio_rec
    res["summary"] = {
        "n_configs": count,
        "n_hypothesis_entered": len(res["entered"]),
        "min_margin_over_kappa": (None if best_ratio_rec is None
                                  else best_ratio_rec["margin_over_kappa"]),
        "verdict": ("REFUTATION" if res["refutation"] else
                    ("HYPOTHESIS_REALIZABLE" if res["entered"] else
                     "HYPOTHESIS_EMPTY (FTI-2 vacuously holds for distinct vertices)")),
        "elapsed_s": time.time() - t0,
    }
    with open(OUT, "w") as f:
        json.dump(res, f, indent=2, default=float)
    print(f"\n[d7-hunt] {count} configs. entered={len(res['entered'])} "
          f"min(margin/kappa)={best_ratio_over_kappa:.3f} "
          f"verdict={res['summary']['verdict']} ({res['summary']['elapsed_s']:.1f}s)",
          flush=True)
    if best_ratio_rec:
        print(f"  closest approach: margin/kappa={best_ratio_rec['margin_over_kappa']:.3f} "
              f"at {best_ratio_rec['shell']} shell, delta/H^2={best_ratio_rec['delta_over_H2']}",
              flush=True)


if __name__ == "__main__":
    main()
