#!/usr/bin/env python3
"""Independent numerical falsification of the factorization
       S*_s(U) <= 2 Phi_s(U) + 6 delta(P)
for EVERY pivot s and EVERY theta-1/2 chart U of a row-stochastic exactly-idempotent P.

INDEPENDENT GENERATOR (not the codex logic):  build P = C C^+ style row-stochastic
idempotents directly from an oblique projector onto a column space.

Construction: pick an r-dim subspace via an n x r matrix M with rows summing-compatible,
and a left inverse N (r x n, N M = I_r); set P = M N.  Then P^2 = M N M N = M N = P,
rank r.  Force row-stochastic by requiring P 1 = 1, i.e. M (N 1) = 1; we instead build P
abstractly and then REJECT non-row-stochastic / non-idempotent samples (exact rationals).

We also DIRECTLY sample row-stochastic idempotents via the spectral form:
   P = sum of rank-1 idempotent pieces is hard to keep stochastic; instead we use the
   ACTUAL-ROW (L,B) converse but with our OWN randomization and our OWN metric code,
   to be a genuinely independent re-implementation of the bookkeeping.
"""
from __future__ import annotations
import itertools, random
from fractions import Fraction as F
import sympy as sp

def rstoch_idem(L, B):
    """L: n x r (actual coords, row sums 1), B: r x n left inverse (B L = I). P=L B."""
    P = L * B
    return P

def is_idem_rstoch(P):
    n = P.rows
    if sp.simplify(P*P - P) != sp.zeros(n, n): return False
    for i in range(n):
        if sp.simplify(sum(P.row(i)) - 1) != 0: return False
    return True

def delta_of(P):
    n = P.rows
    d = sp.Integer(0)
    for i in range(n):
        m = sum(sp.Max(-P[i,j],0) for j in range(P.cols))
        d = sp.Max(d, m)
    return sp.nsimplify(d)

def coeff_matrix(L, basis):
    sub = L[list(basis), :]
    return L * sub.inv()

# ---- metric: independent re-derivation of Phi_s, S*_s ----
def metrics_for_pivot(P, A, basis, s):
    """A = coeff matrix (n x r); basis = chosen rows; s = pivot index into basis (0..r-1).
    beta(j) = P[basis[s], j]."""
    r = A.cols
    u = basis[s]
    Phi = sp.Integer(0); Splus = sp.Integer(0); Vpos = sp.Integer(0)
    for j in range(P.cols):
        beta = sp.nsimplify(P[u, j])
        bp = beta if beta > 0 else sp.Integer(0)
        # lambda, sigma for this row j relative to pivot column s
        a_s = A[j, s]
        lam = 1 - a_s
        sigma = sum((A[j,t] if A[j,t] > 0 else sp.Integer(0)) for t in range(r) if t != s)
        E = sigma - 2*lam
        E = E if E > 0 else sp.Integer(0)
        Phi   += bp * E
        Splus += bp * sigma
        Vpos  += bp * ((-lam) if (-lam) > 0 else sp.Integer(0))
    Sstar = Splus + 2*Vpos
    return sp.nsimplify(Phi), sp.nsimplify(Sstar)

def all_theta_half_charts(L):
    n, r = L.rows, L.cols
    vols = {}
    for basis in itertools.combinations(range(n), r):
        d = L[list(basis), :].det()
        if d == 0: continue
        vols[basis] = abs(d)
    if not vols: return []
    vmax = max(vols.values())
    return [b for b,v in vols.items() if 2*v >= vmax]  # Vol >= Vol_max/2

def test_P(L, B, label, allow_outside=False):
    P = rstoch_idem(L, B)
    if not is_idem_rstoch(P): return None
    d = delta_of(P)
    if d == 0: return ('ok', label, d, 0, None)  # trivial
    inside = (d <= sp.Rational(1,4))
    charts = all_theta_half_charts(L)
    worst = None
    for basis in charts:
        A = coeff_matrix(L, basis)
        # box check
        maxa = max(abs(A[i,j]) for i in range(A.rows) for j in range(A.cols))
        for s in range(L.cols):
            Phi, Sstar = metrics_for_pivot(P, A, basis, s)
            slack = sp.nsimplify(2*Phi + 6*d - Sstar)
            if worst is None or slack < worst[0]:
                worst = (slack, basis, s, Phi, Sstar, maxa)
            if slack < 0:
                return ('VIOLATION', label, d, len(charts),
                        dict(basis=basis, s=s, Phi=str(Phi), Sstar=str(Sstar),
                             slack=str(slack), maxa=str(maxa), inside=inside))
    return ('ok', label, d, len(charts), dict(min_slack=str(worst[0]), maxa=str(worst[5]),
            inside=inside))

# ----------------- generators -----------------
def rand_L_B(n, r, rng, denom=4, outside=False):
    """Random n x r L (row sums 1) and a random left inverse B."""
    # build L: first r rows = identity-ish vertices, rest random affine combos
    rows = []
    for i in range(n):
        if i < r:
            v = [sp.Integer(1) if k==i else sp.Integer(0) for k in range(r)]
        else:
            # random affine: weights summing to 1, allow negatives (=> negative P entries)
            spread = 6 if outside else 3
            w = [sp.Rational(rng.randint(-spread, spread), rng.randint(1, denom)) for _ in range(r-1)]
            w.append(1 - sum(w))
            v = w
        rows.append(v)
    L = sp.Matrix(rows)
    # B: pick r rows forming invertible block as a left-inverse seed, then randomize null space
    # simplest valid B: B = (S^T S)^-1 S^T won't be rational-friendly; use exact pseudo via
    # choosing r independent rows basis0 and setting B to invert them, zero elsewhere... but
    # that gives a specific P. To diversify, mix: B = block-inverse on a random r-subset.
    for _ in range(20):
        subset = tuple(sorted(rng.sample(range(n), r)))
        sub = L[list(subset), :]
        if sub.det() != 0:
            Binv = sub.inv()
            B = sp.zeros(r, n)
            for col_idx, row in enumerate(subset):
                for a in range(r):
                    B[a, row] = Binv[a, col_idx]
            return L, B
    return None, None

def main():
    rng = random.Random(20260613)
    results = {'violation': [], 'ok': 0, 'trivial': 0, 'inside_tested': 0, 'outside_tested':0}
    N = 600
    for it in range(N):
        outside = (it % 3 == 0)  # sample beyond boundary often
        n = rng.choice([3,4,5]); r = rng.choice([2,3])
        if r >= n: continue
        L, B = rand_L_B(n, r, rng, denom=rng.choice([2,3,4]), outside=outside)
        if L is None: continue
        res = test_P(L, B, f"rand_n{n}_r{r}_it{it}", allow_outside=True)
        if res is None: continue
        tag = res[0]
        if tag == 'VIOLATION':
            results['violation'].append(res[4] | {'d':str(res[2]),'label':res[1]})
            print("VIOLATION", res[1], res[4])
        elif res[2] == 0:
            results['trivial'] += 1
        else:
            results['ok'] += 1
            if res[4] and res[4].get('inside'): results['inside_tested'] += 1
            else: results['outside_tested'] += 1
    print("\n=== SUMMARY ===")
    print("ok (nontrivial):", results['ok'], " trivial:", results['trivial'])
    print("inside delta<=1/4:", results['inside_tested'], " outside:", results['outside_tested'])
    print("VIOLATIONS:", len(results['violation']))
    for v in results['violation'][:10]:
        print("  ", v)

if __name__ == '__main__':
    main()
