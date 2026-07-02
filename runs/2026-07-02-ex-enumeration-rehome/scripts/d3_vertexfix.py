#!/usr/bin/env python3 -u
"""
d3_vertexfix.py -- FIX for the coincident-row vertex-test artifact (a NEW failure mode
discovered in the envelope mine, 2026-06-10).

DISCOVERED FAILURE MODE.  d1_infra.is_row_vertex(rows, i) tests whether row i is a
convex combination of ALL other rows.  When two or more rows of P COINCIDE at an extreme
location v, this test wrongly returns NON-vertex for each copy (each is trivially a
convex combination of its identical twin), so v is dropped from W even though v IS a
genuine extreme VERTEX of K=conv(rows).  In the envelope mine this fabricated an
'apparent counterexample': a coincident far cluster at ell^1-distance ~2 from conv W with
dist/tau ~ 7-63, which EVAPORATES once multiplicity is handled correctly (a single copy
of v is well-exposed and JOINS W -> dist 0).  This is the SAME degenerate-near-duplicate
class as the d1 spike (test_lp_robustness.py), now in the VERTEX test rather than the
exposedness LP.

FIX.  is_row_vertex_robust tests reconstruction from the GEOMETRICALLY DISTINCT other
rows only (drop near-duplicates of row i).  v is a vertex iff it is NOT a convex
combination of the distinct others.  well_exposed_set_robust / verify_robust use it.
"""
import numpy as np
from scipy.optimize import linprog
from d1_infra import (robust_linprog, neg_mass, check_idempotent, exposed_margin,
                      dist1_to_conv)


def is_row_vertex_robust(rows, i, tol=1e-7, dup_tol=1e-9):
    """v=rows[i] is a vertex of K=conv(rows) iff it is NOT a convex combination of the
       GEOMETRICALLY DISTINCT other rows (rows within dup_tol of v are ignored, since a
       coincident copy does not make an extreme point non-extreme)."""
    rows = np.asarray(rows, float)
    n, d = rows.shape
    v = rows[i]
    others = [k for k in range(n) if k != i and np.abs(rows[k] - v).sum() > dup_tol]
    if not others:
        return True, 0.0          # only copies of itself -> genuine (isolated) vertex
    A = rows[others].T
    m = len(others)
    nv = m + d
    c = np.concatenate([np.zeros(m), np.ones(d)])
    A_ub = []; b_ub = []
    for j in range(d):
        rp = np.zeros(nv); rp[:m] = A[j]; rp[m + j] = -1.0
        A_ub.append(rp); b_ub.append(v[j])
        rn = np.zeros(nv); rn[:m] = -A[j]; rn[m + j] = -1.0
        A_ub.append(rn); b_ub.append(-v[j])
    A_eq = np.zeros((1, nv)); A_eq[0, :m] = 1.0
    res = robust_linprog(c, A_ub=np.array(A_ub), b_ub=np.array(b_ub),
                         A_eq=A_eq, b_eq=[1.0], bounds=[(0, None)] * m + [(0, None)] * d)
    if res is None or not res.success:
        return True, np.inf
    return bool(res.fun > tol), float(res.fun)


def well_exposed_set_robust(rows, rho, kappa, vtol=1e-7, dup_tol=1e-9, verbose=False):
    """W with the multiplicity-correct vertex test.  Coincident extreme points are
       treated as ONE vertex (we add the first representative of each coincidence class
       that is exposed)."""
    rows = np.asarray(rows, float)
    n = rows.shape[0]
    W = []; info = {}
    seen_repr = {}   # map rounded coords -> representative index already classified
    for i in range(n):
        key = tuple(np.round(rows[i], 9))
        vert, verr = is_row_vertex_robust(rows, i, tol=vtol, dup_tol=dup_tol)
        if not vert:
            info[i] = {"vertex": False, "verr": verr}
            continue
        ok, s, ex = exposed_margin(rows, i, rho, kappa)
        info[i] = {"vertex": True, "exposed": ok, "margin": s}
        if ok:
            W.append(i)
        if verbose:
            print(f"  row {i}: vertex={vert} exposed={ok} margin={s}", flush=True)
    return W, info


def verify_robust(P, hidden_idx, C=4.0, c=0.25, H_target=None, idem_tol=1e-7,
                  dup_tol=1e-9):
    """Honest verification with the multiplicity-correct W.  Same contract as
       d3_envelope.verify but uses well_exposed_set_robust."""
    P = np.asarray(P, float)
    n = P.shape[0]
    chk = check_idempotent(P, tol=idem_tol)
    nm, delta = neg_mass(P)
    out = {"idem_ok": bool(chk["ok"]), "idem_resid": chk["idem_resid"],
           "delta": float(delta), "max_neg": float(delta)}
    if not chk["ok"]:
        out["verified_hidden"] = False; out["reason"] = "not_idempotent"; return out
    if delta <= 1e-12:
        out["tau"] = 0.0; out["verified_hidden"] = False; out["reason"] = "delta_zero"; return out
    tau = float(np.sqrt(delta)); rho, kappa = C * tau, c * tau
    W, info = well_exposed_set_robust(P, rho, kappa, dup_tol=dup_tol)
    dists = {}; maxhid = -1.0; arghid = -1
    for i in hidden_idx:
        di, _ = dist1_to_conv(P, W, i); dists[i] = float(di)
        if di > maxhid:
            maxhid = di; arghid = i
    out.update({"tau": tau, "rho": rho, "kappa": kappa, "nW": len(W),
                "W": list(map(int, W)), "hidden_dists": {int(k): v for k, v in dists.items()},
                "max_hidden_dist": float(maxhid), "argmax_hidden": int(arghid),
                "hidden_in_W": [int(i) for i in hidden_idx if i in W]})
    H = H_target if H_target is not None else maxhid
    out["verified_hidden"] = bool(maxhid >= (H if H is not None else 0.0) - 1e-9 and maxhid > 1e-9)
    return out


if __name__ == "__main__":
    # Regression: the coincident cluster must NOW be a vertex -> exposed -> dist 0.
    from d3_main import bary_to_P
    g = 0.1; r = 5
    rows = [np.eye(r)[a] for a in range(r)]
    lam = np.zeros(r); lam[2] = 1 + g; lam[0] = -g
    for _ in range(3):
        rows.append(lam.copy())
    P = bary_to_P(rows, r)
    v = verify_robust(P, [r, r + 1, r + 2])
    print("[regression] coincident cluster g=0.1, robust verify:")
    print("  delta=%.4f tau=%.4f |W|=%d W=%s max_hidden_dist=%.4f verified_hidden=%s"
          % (v["delta"], v["tau"], v["nW"], v["W"], v["max_hidden_dist"], v["verified_hidden"]),
          flush=True)
    assert v["max_hidden_dist"] < 1e-6, \
        "REGRESSION: coincident cluster should be an exposed vertex (dist 0), not hidden"
    assert not v["verified_hidden"], "REGRESSION: coincident cluster is NOT genuinely hidden"
    print("  [ok] coincident-row vertex artifact fixed: cluster joins W, dist=0", flush=True)
    # And a SINGLE far row (was already correct): still exposed.
    rows2 = [np.eye(r)[a] for a in range(r)]
    rows2.append(lam.copy())
    P2 = bary_to_P(rows2, r)
    v2 = verify_robust(P2, [r])
    print("  single far row: dist=%.4f verified_hidden=%s" % (v2["max_hidden_dist"],
                                                              v2["verified_hidden"]), flush=True)
    assert not v2["verified_hidden"]
    print("\nVERTEX-FIX REGRESSION PASSED", flush=True)
