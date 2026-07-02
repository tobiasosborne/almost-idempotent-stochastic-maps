#!/usr/bin/env python3
"""Maximize H/delta over hidden vertices (exact). Tests if H/delta is bounded (kernel-safe)
   or can grow (toward H>B*tau). Random seeds + coordinate hill-climb on rational params.
   Also tracks best JOINT (sigma~>tau) point. Usage: python3 exp6_maxHd.py SEED ITERS"""
import sys, random
from fractions import Fraction as F
from pipeline import analyze, delta, is_idempotent
from gen import build_from_LambdaC

seed = int(sys.argv[1]) if len(sys.argv) > 1 else 0
ITERS = int(sys.argv[2]) if len(sys.argv) > 2 else 2000
random.seed(seed)

def evalP(C, R2):
    """return (Hd, Ht, so, sig_gt_tau, delta, v) for the height-max hidden vertex, or None."""
    try:
        P, R, _ = build_from_LambdaC(C, R2)
    except Exception:
        return None
    if not is_idempotent(P)[0]:
        return None
    d, negs = delta(P)
    if d == 0 or d > F(1, 4):
        return None
    res = analyze(P, verbose=False)
    if "note" in res or not res["hidden"]:
        return None
    v = max(res["hidden"], key=lambda i: res["dists"][i])
    dv = res["dists"][v]; s = res["sigma_tilde"][v]
    if dv == 0:
        return None
    tau = float(d) ** 0.5
    return dict(Hd=float(dv) / float(d), Ht=float(dv) / tau, so=float(s) / tau,
                sig_gt_tau=(s * s > d), delta=d, v=v, C=C, R2=R2,
                H_gt_Btau=(dv * dv > F(536, 1000) ** 2 * d))

def rand_start():
    k = random.choice([2, 3, 3, 4])
    m = random.choice([1, 2, 2, 3])
    DEN = [2, 3, 4, 6, 8, 12, 20, 40]
    def rq(a, b):
        dd = random.choice(DEN); return F(random.randint(a * dd, b * dd), dd)
    C = []
    for _ in range(m):
        home = random.randrange(k)
        row = [F(0)] * k
        for t in range(k):
            if t != home:
                row[t] = random.choice([F(0), F(0), rq(-1, 1) * F(1, random.choice([2,4,8]))])
        row[home] = F(1) - sum(row)
        C.append(row)
    R2 = [[rq(-1, 1) * F(1, random.choice([4, 8, 20, 50, 100])) for _ in range(m)] for _ in range(k)]
    return C, R2

def perturb(C, R2, step):
    C = [r[:] for r in C]; R2 = [r[:] for r in R2]
    which = random.random()
    if which < 0.5:
        i = random.randrange(len(C)); j = random.randrange(len(C[0]))
        # keep row sum 1: adjust j and home
        delta_ = F(random.choice([-1, 1]), step)
        home = max(range(len(C[0])), key=lambda t: C[i][t])
        if j == home: return C, R2
        C[i][j] += delta_; C[i][home] -= delta_
    else:
        i = random.randrange(len(R2)); j = random.randrange(len(R2[0]))
        R2[i][j] += F(random.choice([-1, 1]), step)
    return C, R2

best = None
bestjoint = None
for it in range(ITERS):
    C, R2 = rand_start()
    cur = evalP(C, R2)
    if cur is None:
        continue
    # hill climb
    for _ in range(40):
        step = random.choice([4, 8, 16, 40, 100, 200])
        C2, R22 = perturb(cur["C"], cur["R2"], step)
        nxt = evalP(C2, R22)
        if nxt and nxt["Hd"] > cur["Hd"]:
            cur = nxt
    if best is None or cur["Hd"] > best["Hd"]:
        best = cur
    if cur["sig_gt_tau"] and (bestjoint is None or cur["Ht"] > bestjoint["Ht"]):
        bestjoint = cur

def show(t, r):
    if r is None: print(f"  {t}: NONE"); return
    print(f"  {t}: delta={float(r['delta']):.5f} H/delta={r['Hd']:.4f} H/tau={r['Ht']:.4f} "
          f"sig/tau={r['so']:.4f} sig>tau={r['sig_gt_tau']} H>Btau={r['H_gt_Btau']}")
    print(f"       C={[[str(x) for x in row] for row in r['C']]}")
    print(f"       R2={[[str(x) for x in row] for row in r['R2']]}")
print(f"seed={seed} iters={ITERS}")
show("MAX H/delta", best)
show("JOINT sig>tau maxH/tau", bestjoint)
