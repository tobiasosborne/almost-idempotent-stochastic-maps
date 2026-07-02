#!/usr/bin/env python3
"""Corrected (DEF) decomposition + the critical Dneg magnitude bound.

Notation: beta = beta_+ - bm where beta_+ = max(beta,0)>=0, bm = max(-beta,0)>=0.
          lambda = lam_+ - lm where lam_+ = max(lam,0)>=0, lm = max(-lam,0)>=0.
"""
import sympy as sp, random

n = 4
betas = sp.symbols('b0:%d' % n, real=True)
lams  = sp.symbols('l0:%d' % n, real=True)
def P(x): return sp.Max(x, 0)
def N(x): return sp.Max(-x, 0)

DEF  = sum(betas[j]*lams[j] for j in range(n))                 # hypothesis: = 0
Dpos = sum(P(betas[j])*P(lams[j]) for j in range(n))
V    = sum(P(betas[j])*N(lams[j]) for j in range(n))
# Dneg defined as the proof's "sum (P)_- lambda" interpreted as MAGNITUDE bm times lambda
Dneg = sum(N(betas[j])*lams[j] for j in range(n))             # bm * lambda

# claim: DEF = Dpos - V - Dneg
gap = DEF - (Dpos - V - Dneg)
random.seed(2); ok=True
for _ in range(3000):
    subs={betas[j]:sp.Rational(random.randint(-5,5),random.randint(1,4)) for j in range(n)}
    subs.update({lams[j]:sp.Rational(random.randint(-9,9),random.randint(1,3)) for j in range(n)})
    if sp.nsimplify(gap.subs(subs))!=0: ok=False; print("MISMATCH",subs,gap.subs(subs)); break
print("Step A (corrected): DEF = Dpos - V - Dneg with Dneg=sum bm*lambda :", "OK" if ok else "FAIL")
print("  => DEF=0 gives  Dpos = V + Dneg.\n")

# ---- The magnitude bound on Dneg = sum_j bm(j) lambda(j) ----
# bm(j) >= 0, sum_j bm(j) <= delta  (negative mass of row u_s).
# lambda(j) in [-1, 3] at theta=1/2 (since a_s in [-2,2] => lambda=1-a_s in [-1,3]).
# Dneg = sum bm(j) lambda(j).  Each term bm(j) lambda(j) in [bm(j)*(-1), bm(j)*3] = [-bm, 3bm].
# UPPER bound (the direction the proof needs): Dneg <= sum bm(j)*3 = 3 * sum bm <= 3 delta.
print("Step C (corrected sign): Dneg = sum bm(j) lambda(j), bm>=0, sum bm<=delta, lambda<=3")
print("  => Dneg <= 3 * sum bm <= 3 delta.   UPPER bound 3 delta is CORRECT.")
print("  (Lower bound Dneg >= -1*delta = -delta.)")
print("  My earlier script had a sign flip in Dneg; the proof's 3 delta is right.\n")

# Sanity: is lambda<=3 the relevant cap, or could lambda exceed 3 if a_s<-2 somewhere?
print("Box check: theta=1/2 => Vol(U)>=Vol_max/2 => Cramer |a_t(j)|<=2 for ALL t,j.")
print("  In particular |a_s(j)|<=2 => lambda=1-a_s in [1-2,1+2]=[-1,3]. Confirmed range.")
print("  Note: lambda CAN reach 3 (when a_s=-2) and CAN reach -1 (a_s=2).")
