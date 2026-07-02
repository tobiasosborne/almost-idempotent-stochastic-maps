#!/usr/bin/env python3
"""Aggressive EXACT search: try to BEAT H/delta=2 (linear law) with a hidden vertex,
   and to enter the joint regime (sigma~>tau AND H>B*tau, B=0.536). Rich generators:
   tail mass (enables feeding/sigma~), webs, multi hidden rows, varied corner counts.
   Also verifies the collapse bound H <= nu*(2+4d)/(1-sigma~) per hidden vertex.
   Usage: python3 search2.py SEED NSAMP"""
import sys, random
from fractions import Fraction as F
from pipeline import analyze, is_idempotent, delta
from gen import build_from_LambdaC

seed = int(sys.argv[1]) if len(sys.argv) > 1 else 0
NS = int(sys.argv[2]) if len(sys.argv) > 2 else 4000
random.seed(seed)
B = 0.536

DEN = [2, 3, 4, 5, 6, 8, 10, 12, 16, 20, 30, 50]
def rq(a, b):
    d = random.choice(DEN); return F(random.randint(a * d, b * d), d)

def rand_C(m, k):
    C = []
    for _ in range(m):
        home = random.randrange(k)
        row = [F(0)] * k
        budget = rq(0, 1) * F(1, random.choice([1, 2, 3, 4, 6, 10]))
        used = F(0)
        for t in random.sample(range(k), k):
            if t == home: continue
            if used >= budget: break
            amt = rq(0, 1) * (budget - used)
            row[t] += random.choice([F(1), F(-1), F(-1), F(-2)]) * amt
            used += abs(amt)
        row[home] = F(1) - sum(row)
        C.append(row)
    return C

bestHd = None      # max H/delta
bestjoint = None   # sig>tau, max H/tau
bestHt = None      # max H/tau overall (hidden)
viol_collapse = 0
kept = 0
for it in range(NS):
    k = random.choice([2, 3, 3, 4, 4, 5])
    m = random.choice([1, 2, 2, 3, 3, 4, 5])
    C = rand_C(m, k)
    # tail mass: sometimes 0 (pure corner), sometimes small (feeding), sometimes structured
    mode = random.random()
    if mode < 0.3:
        R2 = [[F(0)] * m for _ in range(k)]
    else:
        scale = random.choice([4, 8, 20, 50])
        R2 = [[rq(0, 1) * F(1, scale) for _ in range(m)] for _ in range(k)]
    try:
        P, R, _ = build_from_LambdaC(C, R2)
    except Exception:
        continue
    if not is_idempotent(P)[0]:
        continue
    d, negs = delta(P)
    if d == 0 or d > F(1, 4):
        continue
    res = analyze(P, verbose=False)
    if "note" in res or not res["hidden"]:
        continue
    kept += 1
    tau = float(d) ** 0.5
    for v in res["hidden"]:
        s = res["sigma_tilde"][v]; dv = res["dists"][v]
        nu = negs[v]
        Hd = float(dv) / float(d); Ht = float(dv) / tau; so = float(s) / tau
        rec = dict(k=k, m=m, delta=d, v=v, sig=s, dv=dv, nu=nu, Hd=Hd, Ht=Ht, so=so,
                   sig_gt_tau=(s * s > d), H_gt_Btau=(dv * dv > F(536,1000)**2 * d),
                   C=[[str(x) for x in r] for r in C], R2=[[str(x) for x in r] for r in R2])
        # collapse bound check (exact): H*(1-sigma~) <= nu*(2+4d) ? only meaningful if sigma~<1
        if s < 1:
            lhs = dv * (1 - s); rhs = nu * (2 + 4 * d)
            if lhs > rhs:
                viol_collapse += 1
        if bestHd is None or Hd > bestHd["Hd"]: bestHd = rec
        if bestHt is None or Ht > bestHt["Ht"]: bestHt = rec
        if rec["sig_gt_tau"]:
            if bestjoint is None or Ht > bestjoint["Ht"]: bestjoint = rec

print(f"seed={seed} N={NS} kept(hidden)={kept} collapse-bound violations={viol_collapse}")
def show(t, r):
    if r is None: print(f"  {t}: NONE"); return
    print(f"  {t}: k={r['k']} m={r['m']} d={float(r['delta']):.5f} v={r['v']} "
          f"H/delta={r['Hd']:.4f} H/tau={r['Ht']:.4f} sig/tau={r['so']:.4f} "
          f"sig>tau={r['sig_gt_tau']} H>Btau={r['H_gt_Btau']}")
show("MAX H/delta (beat 2?)", bestHd)
show("MAX H/tau (hidden)   ", bestHt)
show("JOINT sig>tau, maxH/tau", bestjoint)
if bestHd and bestHd["Hd"] > 2.0 + 1e-12:
    print("  *** LINEAR LAW BEATEN *** dumping C,R2:")
    print("   C =", bestHd["C"]); print("   R2=", bestHd["R2"])
