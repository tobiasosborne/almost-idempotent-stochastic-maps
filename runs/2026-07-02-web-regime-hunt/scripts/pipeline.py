#!/usr/bin/env python3
"""
pipeline.py -- EXACT (Fraction) implementation of the kernel-conjecture measurement pipeline.

Mirrors docs/ingest/experiments/{d1_infra,d3_vertexfix}.py, but every decision is exact
rational.  Definitions taken verbatim from docs/ingest/report/kernel-conjecture.tex:

  delta(P)          = max_i sum_j max(-P_ij, 0)                          (def:esi)
  tau=sqrt(delta), rho=4 tau, kappa=tau/4                                (def:scales)
  row vertex v      : p_v not in conv{p_j : p_j != p_v}                  (def:vertex)
  admissible exposer for v: affine h, h(p_v)=0, 0<=h(p_j)<=1 all rows    (def:exposed)
  t*(v)             = sup_h  min{ h(p_j) : ||p_j-p_v||_1 >= rho }        (def:exposed)
  v (rho,kappa)-exposed iff t*(v) >= kappa ; W = exposed row vertices    (def:exposed)
  H                 = max_i dist_1(p_i, conv{p_w: w in W})               (def:height)
  sigma~_v          = sum_{j: dist(p_j,C_W)>0} max(P_vj,0)               (def:sigt)

ALL comparisons against irrational tau are done by squaring rationals:
  ||d||_1 >= rho=4 tau  <=>  ||d||_1^2 >= 16 delta      (||d||_1>=0)
  t* >= kappa=tau/4     <=>  16 t*^2 >= delta   (and t*>=0)
  sigma~ > tau          <=>  sigma~^2 > delta   (sigma~>=0)
  H     > B tau         <=>  H^2 > B^2 delta
so 'entering the web regime' is an EXACT rational predicate.
"""
from fractions import Fraction as F
from exact_lp import linprog_exact


def as_F(P):
    return [[F(x) for x in row] for row in P]


def matmul(A, B):
    n = len(A); m = len(B[0]); k = len(B)
    return [[sum(A[i][t] * B[t][j] for t in range(k)) for j in range(m)] for i in range(n)]


def is_idempotent(P):
    n = len(P)
    P2 = matmul(P, P)
    idem = all(P2[i][j] == P[i][j] for i in range(n) for j in range(n))
    rowsum = all(sum(P[i]) == 1 for i in range(n))
    return idem and rowsum, idem, rowsum


def delta(P):
    n = len(P)
    negs = [sum(max(-P[i][j], F(0)) for j in range(n)) for i in range(n)]
    return max(negs), negs


def l1(a, b):
    return sum(abs(a[i] - b[i]) for i in range(len(a)))


def is_row_vertex(P, i, dup_tol=F(0)):
    """v=p_i is a vertex iff it is NOT a convex combination of the geometrically
       DISTINCT other rows (exact; dup rows dropped)."""
    n = len(P); d = n
    v = P[i]
    others = [k for k in range(n) if k != i and l1(P[k], v) > dup_tol]
    if not others:
        return True, F(0)
    m = len(others)
    # min sum t_j  s.t.  sum_k lam_k A[k] - v = r,  -t<=r<=t, lam>=0 sum=1
    nv = m + d
    c = [F(0)] * m + [F(1)] * d
    A_ub = []; b_ub = []
    for j in range(d):
        rp = [F(0)] * nv
        for kk in range(m):
            rp[kk] = P[others[kk]][j]
        rp[m + j] = F(-1)
        A_ub.append(rp); b_ub.append(v[j])
        rn = [F(0)] * nv
        for kk in range(m):
            rn[kk] = -P[others[kk]][j]
        rn[m + j] = F(-1)
        A_ub.append(rn); b_ub.append(-v[j])
    A_eq = [[F(1)] * m + [F(0)] * d]; b_eq = [F(1)]
    bounds = [(F(0), None)] * m + [(F(0), None)] * d
    r = linprog_exact(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds)
    if r["status"] != "optimal":
        return True, None
    return (r["fun"] > 0), r["fun"]


def exposed_tstar(P, i, delta_val):
    """Exact t*(v): max t s.t. affine h, h(p_i)=0, 0<=h(p_k)<=1 all k, h(p_k)>=t for far k.
       far k := ||p_k-p_i||_1^2 >= 16 delta  (i.e. >= rho).  Returns (tstar or None-if-inf).
       Variables: a(d) free, b free, t (<=1, free below)."""
    n = len(P); d = n
    di2 = [l1(P[k], P[i]) for k in range(n)]  # exact ell1 dists
    far = [k for k in range(n) if k != i and di2[k] * di2[k] >= 16 * delta_val]
    if not far:
        return None  # vacuously exposable, t*=+inf
    nv = d + 1 + 1  # a(d), b, t
    c = [F(0)] * (d + 1) + [F(-1)]  # min -t
    A_ub = []; b_ub = []
    def hvec(k):
        row = [F(0)] * nv
        for j in range(d):
            row[j] = P[k][j]
        row[d] = F(1)
        return row
    for k in range(n):
        hk = hvec(k)
        A_ub.append(hk[:]); b_ub.append(F(1))               # h<=1
        A_ub.append([-x for x in hk]); b_ub.append(F(0))    # h>=0
    for k in far:
        hk = hvec(k)
        row = [-x for x in hk]
        row[-1] = F(1)
        A_ub.append(row); b_ub.append(F(0))                 # -h + t <= 0 => h>=t
    A_eq = [hvec(i)]; b_eq = [F(0)]                          # h(p_i)=0
    bounds = [(None, None)] * (d + 1) + [(None, F(1))]      # a,b free; t<=1
    r = linprog_exact(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds)
    assert r["status"] == "optimal", f"exposedness LP not optimal: {r['status']}"
    return -r["fun"]


def visible_set(P, delta_val):
    """W = exposed row vertices (exact).  Returns (W list, info dict)."""
    n = len(P)
    W = []; info = {}
    for i in range(n):
        vert, verr = is_row_vertex(P, i)
        if not vert:
            info[i] = {"vertex": False}
            continue
        ts = exposed_tstar(P, i, delta_val)
        if ts is None:
            exposed = True  # vacuous (+inf margin)
            info[i] = {"vertex": True, "tstar": None, "exposed": True}
        else:
            # t* >= kappa=tau/4 <=> ts>=0 and 16 ts^2 >= delta
            exposed = (ts >= 0) and (16 * ts * ts >= delta_val)
            info[i] = {"vertex": True, "tstar": ts, "exposed": exposed}
        if exposed:
            W.append(i)
    return W, info


def dist1_to_conv(P, W, i):
    """exact dist_1(p_i, conv{p_w:w in W}) via LP. Returns (dist, lambdas)."""
    n = len(P); d = n
    if not W:
        return None, None
    v = P[i]; m = len(W)
    nv = m + d
    c = [F(0)] * m + [F(1)] * d
    A_ub = []; b_ub = []
    for j in range(d):
        rp = [F(0)] * nv
        for kk in range(m):
            rp[kk] = P[W[kk]][j]
        rp[m + j] = F(-1)
        A_ub.append(rp); b_ub.append(v[j])
        rn = [F(0)] * nv
        for kk in range(m):
            rn[kk] = -P[W[kk]][j]
        rn[m + j] = F(-1)
        A_ub.append(rn); b_ub.append(-v[j])
    A_eq = [[F(1)] * m + [F(0)] * d]; b_eq = [F(1)]
    bounds = [(F(0), None)] * m + [(F(0), None)] * d
    r = linprog_exact(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds)
    if r["status"] != "optimal":
        return None, None
    return r["fun"], r["x"][:m]


def analyze(P, label="", verbose=True):
    """Full exact analysis.  Returns dict of exact invariants."""
    P = as_F(P)
    n = len(P)
    ok, idem, rowsum = is_idempotent(P)
    dval, negs = delta(P)
    res = {"label": label, "n": n, "idem_exact": idem, "rowsum_exact": rowsum,
           "delta": dval}
    if not ok:
        res["ERROR"] = "not exact idempotent"
        return res
    if dval == 0:
        res["note"] = "delta=0 (stochastic idempotent)"
        return res
    W, info = visible_set(P, dval)
    res["W"] = W
    res["info"] = info
    # dist of every row to conv W (=> height)
    dists = []
    for i in range(n):
        di, _ = dist1_to_conv(P, W, i)
        dists.append(di)
    res["dists"] = dists
    H = max(d for d in dists if d is not None)
    res["H"] = H
    res["argmaxH"] = max(range(n), key=lambda i: dists[i])
    # invisible mass sigma~_v for each row v:
    #  columns j with dist(p_j, C_W) > 0
    outside = [j for j in range(n) if dists[j] is not None and dists[j] > 0]
    res["outside_cols"] = outside
    sigt = []
    for v in range(n):
        s = sum(max(P[v][j], F(0)) for j in outside)
        sigt.append(s)
    res["sigma_tilde"] = sigt
    # regime predicates (exact): sigma~ > tau <=> sigma~^2 > delta
    res["sigma_over_tau_sq"] = [(s * s, dval) for s in sigt]  # compare s^2 vs delta
    res["hidden"] = [i for i in range(n) if not info.get(i, {}).get("exposed", False)
                     and info.get(i, {}).get("vertex", False)]
    if verbose:
        print(f"=== {label} ===")
        print(f"  n={n} idempotent_exact={idem} rowsum_exact={rowsum}")
        print(f"  delta = {dval} = {float(dval):.6e}   tau=sqrt(delta)={float(dval)**0.5:.6e}")
        print(f"  W (visible) = {W}")
        print(f"  vertices = {[i for i in range(n) if info.get(i,{}).get('vertex')]}")
        print(f"  hidden vertices = {res['hidden']}")
        print(f"  H = {H} = {float(H):.6e}   H/tau = {float(H)/float(dval)**0.5:.6f}")
        print(f"  argmax H = row {res['argmaxH']}")
        tau = float(dval) ** 0.5
        for v in res['hidden']:
            s = sigt[v]
            print(f"    hidden v={v}: sigma~={s}={float(s):.6e}  sigma~/tau={float(s)/tau:.6f}"
                  f"  dist(v,convW)={dists[v]}  H_v/tau={float(dists[v])/tau:.6f}"
                  f"  [sigma~>tau? {s*s>dval}]  [dist>tau? {dists[v]**2>dval}]")
    return res


def clone_row(P, r, weights):
    """Split index r into len(weights) duplicates via P_hat_{ab}=alpha_b P_{pi(a),pi(b)}.
       weights: list of Fraction summing to 1 (fiber weights for the new columns).
       Returns the cloned (n+M-1)x(n+M-1) exact matrix.  A clone-invariance sanity test."""
    P = as_F(P)
    n = len(P)
    M = len(weights)
    assert sum(weights) == 1
    # new index order: rows 0..r-1, then M copies of r, then r+1..n-1
    old_of = []  # map new index -> old index
    fiber_w = []  # map new index -> weight if in fiber else 1
    for i in range(n):
        if i == r:
            for b in range(M):
                old_of.append(r); fiber_w.append(weights[b])
        else:
            old_of.append(i); fiber_w.append(F(1))
    N = len(old_of)
    Ph = [[fiber_w[b] * P[old_of[a]][old_of[b]] for b in range(N)] for a in range(N)]
    return Ph
