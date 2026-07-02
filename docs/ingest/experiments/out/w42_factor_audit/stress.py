#!/usr/bin/env python3
"""Targeted adversarial stress for S* <= 2 Phi + 6 delta:
   - small delta (inside 1/4) with many overshoot rows
   - delta exactly at 1/4 boundary
   - perturbed-staircase analog at delta=1/2 (OUTSIDE hypothesis): does lemma hold anyway?
   - rank-2 consistency (factorization should give S* <= 6 delta; rank-2 thm gives <=2 delta)
Also reports the TIGHTNESS (min slack) and whether equality 2Phi+6delta is approached.
"""
import itertools
from fractions import Fraction as F
import sympy as sp
from falsify import (rstoch_idem, is_idem_rstoch, delta_of, coeff_matrix,
                     metrics_for_pivot, all_theta_half_charts)

def report(L, B, label):
    P = rstoch_idem(L, B)
    if not is_idem_rstoch(P):
        print(f"[{label}] NOT a row-stochastic idempotent -- skipped"); return
    d = delta_of(P)
    charts = all_theta_half_charts(L)
    rows = []
    for basis in charts:
        A = coeff_matrix(L, basis)
        for s in range(L.cols):
            Phi, Sstar = metrics_for_pivot(P, A, basis, s)
            slack = sp.nsimplify(2*Phi + 6*d - Sstar)
            rows.append((slack, basis, s, Phi, Sstar))
    rows.sort(key=lambda t: F(str(t[0])))
    worst = rows[0]
    viol = [r for r in rows if F(str(r[0])) < 0]
    print(f"[{label}] delta={d}  charts={len(charts)}  min_slack={worst[0]} "
          f"(basis={worst[1]},s={worst[2]},Phi={worst[3]},S*={worst[4]})  "
          f"VIOLATIONS={len(viol)}")
    # also rank-2 special: report S*/delta worst
    if d != 0:
        ratios = [(F(str(r[4]))/F(str(d)), r) for r in rows]
        ratios.sort(key=lambda t: t[0], reverse=True)
        print(f"        worst S*/delta = {ratios[0][0]}  (must be <= 2*Phi/delta+6)")
    return viol

# ---- Perturbed staircase analog (the w38 refutation witness family) ----
# rank-2 staircase: rows are points on a line; build L (n x 2), row sums 1.
def staircase(n, eps):
    """rows at parameter positions t_i; affine coord (1-t, t). Perturb to create overshoot."""
    L = sp.zeros(n, 2)
    for i in range(n):
        t = sp.Rational(i, max(n-1,1))
        # perturb endpoints outward to force volume ties / overshoot
        if i == 0: t = -eps
        if i == n-1: t = 1 + eps
        L[i,0] = 1 - t; L[i,1] = t
    return L

def left_inv_two_rows(L, i, j):
    sub = L[[i,j],:]
    if sub.det()==0: return None
    Binv = sub.inv()
    B = sp.zeros(2, L.rows)
    B[:, i] = Binv[:,0]; B[:, j] = Binv[:,1]
    return B

print("=== Perturbed staircase (rank-2 line), various eps ===")
for n in [3,4,5]:
    for eps in [sp.Rational(1,1000), sp.Rational(1,10), sp.Rational(1,4), sp.Rational(1,2), 1]:
        L = staircase(n, eps)
        # choose interior-pair left inverse to create negative masses
        B = left_inv_two_rows(L, 0, n-1)
        if B is None: continue
        report(L, B, f"staircase n={n} eps={eps}")

print("\n=== rank-2 random with delta<=1/4: factorization vs rank-2 theorem (S*<=2delta) ===")
import random
rng = random.Random(7)
cnt_inside=0
for it in range(4000):
    n = rng.choice([3,4])
    # random 2-d affine points, keep delta small by tight spread
    L = sp.zeros(n,2)
    for i in range(n):
        if i<2:
            L[i,0]=sp.Integer(1) if i==0 else 0; L[i,1]=sp.Integer(0) if i==0 else 1
        else:
            t = sp.Rational(rng.randint(-2,4), rng.randint(2,6))
            L[i,0]=1-t; L[i,1]=t
    B = left_inv_two_rows(L, 0, 1)
    if B is None: continue
    P = rstoch_idem(L,B)
    if not is_idem_rstoch(P): continue
    d = delta_of(P)
    if d==0 or d>sp.Rational(1,4): continue
    cnt_inside+=1
    if cnt_inside<=6:
        report(L,B,f"rank2 inside it={it}")
print("rank-2 inside-delta instances tested:", cnt_inside)

print("\n=== Many-overshoot corner: cluster rows far outside a small base triangle (rank 3) ===")
def cluster3(scale):
    # 3 base vertices + 3 far points => any chart leaves some rows with big negative coords
    L = sp.Matrix([
        [1,0,0],[0,1,0],[0,0,1],
        [1-2*scale, scale, scale],
        [scale, 1-2*scale, scale],
        [scale, scale, 1-2*scale],
    ])
    return L
def left_inv_three(L, idx):
    sub=L[list(idx),:]
    if sub.det()==0: return None
    Binv=sub.inv(); B=sp.zeros(3,L.rows)
    for c,row in enumerate(idx):
        B[:,row]=Binv[:,c]
    return B
for scale in [sp.Rational(-1,2), sp.Rational(-1,4), sp.Rational(-1,8), sp.Rational(3,2), 2]:
    L=cluster3(scale)
    for idx in [(0,1,2),(3,4,5)]:
        B=left_inv_three(L,idx)
        if B is None: continue
        report(L,B,f"cluster3 scale={scale} inv={idx}")
