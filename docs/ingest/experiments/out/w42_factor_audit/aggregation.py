#!/usr/bin/env python3
"""Audit the GLOBAL aggregation steps of the w41 factorization.

Step A (DEF decomposition):
    0 = sum_j beta(j) lambda(j)
      = sum_j beta_+ lambda  - sum_j beta_- lambda            [beta = beta_+ - beta_-]
      = sum_j beta_+ lambda_+ - sum_j beta_+ (-lambda)_+ - sum_j beta_- lambda
    Define:
       Dpos = sum beta_+ lambda_+         (>=0)
       V    = sum beta_+ (-lambda)_+      (>=0)
       Dneg = sum beta_- lambda           ( = -sum (-beta)_+ lambda, sign varies )
    The proof writes 0 = Dpos - V - Dneg, i.e. Dpos = V + Dneg.
    CHECK the algebra and the SIGN convention of Dneg.

Step B (V <= Phi/2):  on rows with beta_+>0 contributing to V we have lambda<0,
    and there E = sigma + 2(-lambda) >= 2(-lambda), so beta_+(-lambda)_+ <= beta_+ E/2.
    Summing: V <= Phi/2.   CHECK whether E>=2(-lambda) really holds on ALL such rows.

Step C (Dneg <= 3 delta): Dneg = sum_j beta_-(j) lambda(j). With |lambda|<=3 (theta-half box)
    and sum_j beta_-(j) = sum_j(-beta)_+ <= delta, we get |Dneg| <= 3 delta.
    CHECK the box bound |lambda|<=3 vs the bound actually needed (Dneg uses lambda on the
    SUPPORT of beta_- = negative entries of row u_s).
"""
import sympy as sp

# ---- Step A: symbolic identity ----
print("=== Step A: (DEF) decomposition  Dpos = V + Dneg ===")
# Represent per-row beta and lambda symbolically over a tiny index set, verify the identity.
n = 4
betas = sp.symbols('b0:%d' % n, real=True)
lams  = sp.symbols('l0:%d' % n, real=True)

def P(x): return sp.Max(x, 0)
def N(x): return sp.Max(-x, 0)

DEF = sum(betas[j]*lams[j] for j in range(n))             # = 0 by hypothesis (we don't set =0; we decompose)
Dpos = sum(P(betas[j])*P(lams[j]) for j in range(n))
V    = sum(P(betas[j])*N(lams[j]) for j in range(n))
Dneg = sum((-N(betas[j]))*lams[j] for j in range(n))      # beta_- entries times lambda; beta_-(j) = -N(beta_j) (the signed negative part)

# proof's claim: DEF = Dpos - V - Dneg  (so that DEF=0 => Dpos = V + Dneg)
# Here Dneg as proof defines: Dneg_s := sum (P_{u_s j})_- lambda(j). The "_- " is the
# signed negative part = beta if beta<0 else 0 = -N(beta). So Dneg = sum (-N(beta)) lambda.
lhs = DEF
rhs = Dpos - V - Dneg
gap = sp.simplify(lhs - rhs)
print("  DEF - (Dpos - V - Dneg) simplifies to:", gap, " (expect 0)")

# numeric spot check
import random
random.seed(1)
ok = True
for _ in range(2000):
    subs = {}
    for j in range(n):
        subs[betas[j]] = sp.Rational(random.randint(-5,5), random.randint(1,4))
        subs[lams[j]]  = sp.Rational(random.randint(-9,9), random.randint(1,3))
    v = sp.nsimplify(lhs.subs(subs) - rhs.subs(subs))
    if v != 0:
        ok = False
        print("  NUM MISMATCH", subs, v); break
print("  numeric identity over 2000 random points:", "OK" if ok else "FAIL")

print("\n=== Step C sign/magnitude: Dneg = sum beta_-(j) lambda(j) ===")
print("  beta_-(j) <= 0, sum_j |beta_-(j)| <= delta. lambda in [-1,3] at theta=1/2.")
print("  Dneg = sum beta_-(j) lambda(j); each term beta_-(j)*lambda(j) in [beta_-*3, beta_-*(-1)]")
print("       = [-3|beta_-|, +1|beta_-|].  So Dneg in [-3 delta, +1 delta].")
print("  The proof needs Dpos = V + Dneg <= Phi/2 + 3 delta, i.e. uses Dneg <= 3 delta (UPPER).")
print("  UPPER bound on Dneg: Dneg = sum beta_-(j) lambda(j) with beta_-(j)<=0.")
print("     term is LARGEST (most positive) when lambda(j) is most NEGATIVE = -1.")
print("     => Dneg <= sum beta_-(j)*(-1) = sum |beta_-(j)| <= delta.   <-- only delta, not 3 delta!")
print("     term is most positive via lambda=+3 only if beta_-<0 times +3 = NEGATIVE. ")
print("  RECHECK: beta_-(j) <= 0. beta_-(j)*lambda(j):")
print("     lambda=+3: term = (<=0)*3 <= 0.")
print("     lambda=-1: term = (<=0)*(-1) = |beta_-|*1 >= 0  (positive, magnitude |beta_-|).")
print("  => max term value = |beta_-(j)| (at lambda=-1). Dneg <= sum|beta_-| <= delta.")
print("  So the UPPER bound is Dneg <= delta  (NOT 3 delta). |Dneg|<=3delta but the")
print("  needed direction is the +1 side, giving delta.")
