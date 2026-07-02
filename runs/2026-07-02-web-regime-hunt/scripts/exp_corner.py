#!/usr/bin/env python3
"""Task 2/3: explore corner + dilution families. Track (delta, sigma~/tau, H/tau, hidden).
   Exact throughout.  Reports the binding constraint at each configuration."""
from fractions import Fraction as F
from pipeline import analyze, as_F, is_idempotent
from gen import build_from_R, build_from_R_general, mat_inv


def summary(P, label, verbose=False):
    res = analyze(P, label=label, verbose=verbose)
    if "ERROR" in res:
        return None
    d = res["delta"]
    if d == 0:
        return {"label": label, "delta": F(0)}
    H = res["H"]
    hidden = res["hidden"]
    # best hidden vertex by dist
    best = None
    for v in hidden:
        s = res["sigma_tilde"][v]
        dv = res["dists"][v]
        # exact predicates
        rec = {"v": v, "sigma": s, "distv": dv,
               "sigma_gt_tau": s * s > d, "dist_gt_tau": dv * dv > d,
               "sigma_over_tau2": (float(s) / float(d) ** 0.5),
               "dist_over_tau2": (float(dv) / float(d) ** 0.5)}
        if best is None or dv > best["distv"]:
            best = rec
    return {"label": label, "delta": d, "H": H, "nW": len(res["W"]),
            "W": res["W"], "hidden": hidden, "best": best,
            "H_over_tau": float(H) / float(d) ** 0.5,
            "H_over_delta": float(H) / float(d)}


print("################ FAMILY 1: transverse pair (k=2 pure corners), scan N ################")
# r1=e1, r2=e2 on 2 coords; hidden v = (1+N) r1 - N r2 ; need a 2nd hidden row to keep n=2k?
# Use direct construction: rank-1 P = I - u v^T style. Simpler: explicit 3x3 transverse.
# transverse pair: archetypes e1,e2; hidden rows reaching out.
# Build via R-first with k=2,n=4: archetypes on 4 coords.
for Nnum, Nden in [(1,10),(1,4),(1,3),(2,5),(1,2),(3,5)]:
    Nv = F(Nnum, Nden)
    # archetypes: r1 concentrated corner-1, r2 corner-2, each with tiny mass on hidden coords
    # to make R2 invertible. Use e-perturbation eps.
    eps = F(1, 100)
    r1 = [1 - eps, F(0), eps, F(0)]
    r2 = [F(0), 1 - eps, F(0), eps]
    R = [r1, r2]
    out = build_from_R(R)
    if out is None:
        print(f"  N={Nv}: R2 singular"); continue
    P, C = out
    s = summary(P, f"transverse eps=1/100 N={Nv}")
    if s: print(f"  N={Nv}: delta={s['delta']}={float(s['delta']):.4f} H/tau={s['H_over_tau']:.4f} "
                f"H/delta={s['H_over_delta']:.4f} nW={s['nW']} hidden={s['hidden']} "
                f"best={s['best']['sigma_over_tau2']:.3f}sig/tau {s['best']['dist_over_tau2']:.3f}dist/tau")


print("\n################ FAMILY 2: pure k-corner, hidden = signed combos (H=2delta check) ##")
for k in [2, 3, 4]:
    # n = 2k. archetypes near corners with eps mass on own hidden coord.
    eps = F(1, 1000)
    R = []
    for s in range(k):
        row = [F(0)] * (2 * k)
        row[s] = 1 - eps
        row[k + s] = eps
        R.append(row)
    out = build_from_R(R)
    if out is None:
        print(f"  k={k}: singular"); continue
    P, C = out
    sm = summary(P, f"pure-corner k={k}")
    if sm: print(f"  k={k}: delta={float(sm['delta']):.5f} H/tau={sm['H_over_tau']:.4f} "
                 f"H/delta={sm['H_over_delta']:.4f} nW={sm['nW']} hidden={sm['hidden']}")
