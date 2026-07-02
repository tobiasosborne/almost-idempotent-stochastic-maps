#!/usr/bin/env python3
"""Audit Step B:  V_s <= Phi_s / 2, where
   V_s   = sum_j beta_+(j) (-lambda(j))_+
   Phi_s = sum_j beta_+(j) E(j),   E = (sigma - 2 lambda)_+.
Claim: per-row, beta_+(-lambda)_+ <= beta_+ E / 2.  Need: (-lambda)_+ <= E/2 whenever beta_+>0.
Equivalently 2(-lambda)_+ <= E for ALL rows (beta_+>=0 just scales).
"""
import sympy as sp
sigma = sp.Symbol('sigma', nonnegative=True)
lam   = sp.Symbol('lam', real=True)
E = sp.Max(sigma - 2*lam, 0)
lhs = 2*sp.Max(-lam, 0)
# check 2(-lam)_+ <= E
print("=== Step B per-row: 2(-lambda)_+ <= E = (sigma-2 lambda)_+ ? ===")
print("  Case lam>=0: LHS=0 <= E (E>=0). OK.")
print("  Case lam<0:  LHS=-2 lam = 2|lam|.  E=(sigma-2 lam)_+ = sigma+2|lam| (sigma>=0).")
print("               E - LHS = sigma + 2|lam| - 2|lam| = sigma >= 0. OK (slack = sigma).")
# numeric sweep incl sigma=0
import random; random.seed(3); worst=None
for _ in range(20000):
    s=sp.Rational(random.randint(0,6),random.randint(1,3))
    l=sp.Rational(random.randint(-6,6),random.randint(1,3))
    Ev=max(s-2*l,0); L=2*max(-l,0); d=Ev-L
    if worst is None or d<worst[0]: worst=(d,s,l,Ev,L)
    if d<0: print("  VIOLATION sigma=%s lam=%s E=%s LHS=%s"%(s,l,Ev,L))
print("  min(E - 2(-lam)_+) over 20000 pts =", worst[0], "at sigma=%s lam=%s"%(worst[1],worst[2]))
print("  => 2(-lambda)_+ <= E pointwise (equality iff sigma=0 on overshoot rows).")
print("  => V_s = sum beta_+ (-lam)_+ <= (1/2) sum beta_+ E = Phi_s/2.  CONFIRMED.")
