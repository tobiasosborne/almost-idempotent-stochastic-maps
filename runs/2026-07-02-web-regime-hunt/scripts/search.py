#!/usr/bin/env python3
"""Randomized EXACT search over signed idempotents (LambdaC builder) for hidden
   vertices maximizing H/tau and sigma~/tau. Tracks the joint-antecedent frontier.
   Exact throughout; floats only for ranking/printing. Usage: python3 search.py SEED NSAMP"""
import sys, random
from fractions import Fraction as F
from pipeline import analyze, is_idempotent, delta
from gen import build_from_LambdaC

seed = int(sys.argv[1]) if len(sys.argv) > 1 else 0
NS = int(sys.argv[2]) if len(sys.argv) > 2 else 1500
random.seed(seed)

DENS = [2, 3, 4, 5, 6, 8, 10, 12, 16, 20, 25, 40, 100]

def rq(lo, hi):
    d = random.choice(DENS)
    n = random.randint(lo * d, hi * d)
    return F(n, d)

def rand_C(m, k):
    """m hidden rows, each a signed combo over k archetypes summing to 1, near-corner biased."""
    C = []
    for _ in range(m):
        # pick a 'home' corner, put ~1 there, small +/- spread on others (small negativity)
        home = random.randrange(k)
        row = [F(0)] * k
        # small perturbation budget
        spread = rq(0, 1) * F(1, random.choice([2, 3, 4, 6, 10]))  # in [0, ~0.5]
        # distribute spread as signed to a few other coords
        others = [t for t in range(k) if t != home]
        random.shuffle(others)
        used = F(0)
        for t in others:
            if used >= spread or random.random() < 0.3:
                continue
            amt = rq(0, 1) * (spread - used)
            sign = random.choice([F(1), F(-1), F(-1)])  # bias negative to make it poke out
            row[t] += sign * amt
            used += abs(amt)
        row[home] = F(1) - sum(row)
        C.append(row)
    return C

best = {"H": None, "sig": None, "joint": None}
records = []
kept = 0
for it in range(NS):
    k = random.choice([2, 2, 3, 3, 4])
    m = random.choice([1, 2, 2, 3, 3, 4])
    C = rand_C(m, k)
    R2 = [[rq(0, 1) * F(1, random.choice([4, 10, 20, 50, 100])) for _ in range(m)] for _ in range(k)]
    try:
        P, R, _ = build_from_LambdaC(C, R2)
    except Exception:
        continue
    ok, _, _ = is_idempotent(P)
    if not ok:
        continue
    d, _ = delta(P)
    if d == 0 or d > F(1, 4):
        continue
    res = analyze(P, verbose=False)
    if "note" in res or not res["hidden"]:
        continue
    kept += 1
    for v in res["hidden"]:
        s = res["sigma_tilde"][v]; dv = res["dists"][v]
        # exact ratios via squares; store floats for ranking
        rec = dict(k=k, m=m, delta=d, v=v, sig=s, distv=dv,
                   Ho=float(dv) / float(d) ** 0.5, so=float(s) / float(d) ** 0.5,
                   sig_gt_tau=(s * s > d), dist_gt_tau=(dv * dv > d),
                   Hd=float(dv) / float(d), C=C, R2=R2)
        records.append(rec)
        if best["H"] is None or rec["Ho"] > best["H"]["Ho"]:
            best["H"] = rec
        if best["sig"] is None or rec["so"] > best["sig"]["so"]:
            best["sig"] = rec
        if rec["sig_gt_tau"] and (best["joint"] is None or rec["Ho"] > best["joint"]["Ho"]):
            best["joint"] = rec

print(f"seed={seed} samples={NS} kept(with hidden)={kept} hidden-vertex records={len(records)}")
def show(tag, r):
    if r is None:
        print(f"  {tag}: NONE"); return
    print(f"  {tag}: k={r['k']} m={r['m']} delta={float(r['delta']):.5f} v={r['v']} "
          f"H/tau={r['Ho']:.4f}(>1:{r['dist_gt_tau']}) sig/tau={r['so']:.4f}(>1:{r['sig_gt_tau']}) H/delta={r['Hd']:.4f}")
show("max H/tau ", best["H"])
show("max sig/tau", best["sig"])
show("joint(sig>tau) max H/tau", best["joint"])
# also report max H/delta (linear-law probe)
if records:
    mHd = max(records, key=lambda r: r["Hd"])
    show("max H/delta (linear-law probe)", mHd)
