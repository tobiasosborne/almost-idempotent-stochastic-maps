#!/usr/bin/env python3
"""Audit the POINTWISE estimate g(j) <= E(j) + 2(lambda)_+ by exhaustive sign casework,
and probe the per-step constants of the w41 factorization.

Definitions (per pivot s, per row j), with mu = sum_{t!=s}(-a_t)_+, sigma = sum_{t!=s}(a_t)_+:
  lambda = 1 - a_s
  E      = (mu - lambda)_+ = (sigma - 2 lambda)_+      [using identity lambda = sigma - mu]
  g      = sigma + 2(-lambda)_+

We verify g <= E + 2(lambda)_+ as an identity in the variables (sigma>=0, mu>=0, a_s real),
with the COUPLING lambda = sigma - mu enforced (this is the affine-coordinate sum-to-one fact).
"""
import sympy as sp

sigma, mu = sp.symbols('sigma mu', nonnegative=True)
lam = sigma - mu  # the coupling lambda = sigma - mu

def posexpr(x):
    return sp.Max(x, 0)

E = posexpr(sigma - 2*lam)          # = (mu - lam)_+ since sigma-2lam = mu-lam
g = sigma + 2*posexpr(-lam)
RHS = E + 2*posexpr(lam)

print("=== Pointwise identity check: g <= E + 2 lambda_+ (lambda=sigma-mu) ===")
diff = sp.simplify(RHS - g)
print("RHS - g =", diff)
# exhaustive sign cases
cases = []
for lam_sign in ['lam>=0', 'lam<0']:
    for sig_cmp in ['sigma>=2lam', 'sigma<2lam']:
        cases.append((lam_sign, sig_cmp))

print("\n--- Case analysis (substituting concrete representatives) ---")
import itertools
# pick sample points exercising each region (sigma>=0, mu>=0)
samples = []
for s_v in [sp.Rational(0), sp.Rational(1,3), 1, 2, 3, 5]:
    for m_v in [sp.Rational(0), sp.Rational(1,3), 1, 2, 3, 5]:
        samples.append((s_v, m_v))
maxgap = None
worst = None
for s_v, m_v in samples:
    l_v = s_v - m_v
    E_v = max(s_v - 2*l_v, 0)
    g_v = s_v + 2*max(-l_v, 0)
    rhs_v = E_v + 2*max(l_v, 0)
    gap = rhs_v - g_v
    if maxgap is None or gap < maxgap:
        maxgap = gap; worst = (s_v, m_v, l_v, E_v, g_v, rhs_v, gap)
    if gap < 0:
        print("  VIOLATION at sigma=%s mu=%s : g=%s RHS=%s" % (s_v, m_v, g_v, rhs_v))
print("min(RHS-g) over samples =", maxgap, " at (sigma,mu,lam,E,g,RHS,gap)=", worst)

# Symbolic proof of nonnegativity of RHS-g via region split
print("\n--- Symbolic region split of RHS - g ---")
a, b = sp.symbols('a b', positive=True)  # generic positive magnitudes
# region 1: lam>=0 and sigma>=2lam  => E=sigma-2lam, lam_+=lam, (-lam)_+=0
r1 = (sigma-2*lam) + 2*lam - sigma
print("  lam>=0, sigma>=2lam: RHS-g =", sp.simplify(r1), " (expect 0)")
# region 2: lam>=0 and sigma<2lam => E=0, lam_+=lam, (-lam)_+=0
r2 = 0 + 2*lam - sigma
print("  lam>=0, sigma<2lam:  RHS-g =", sp.simplify(r2), " = 2lam-sigma >0 in this region")
# region 3: lam<0 => E=sigma-2lam (sigma-2lam>0 since lam<0), lam_+=0, (-lam)_+=-lam
r3 = (sigma-2*lam) + 0 - (sigma + 2*(-lam))
print("  lam<0:               RHS-g =", sp.simplify(r3), " (expect 0)")
print("\n  => g <= E + 2 lambda_+ HOLDS with equality on lam<0 and on lam>=0&sigma>=2lam;")
print("     slack only where lam>=0 & sigma<2lam (there g=sigma<2lam, E=0).")
