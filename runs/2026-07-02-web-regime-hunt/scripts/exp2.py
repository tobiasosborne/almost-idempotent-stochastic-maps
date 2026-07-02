#!/usr/bin/env python3
"""Explore with build_from_LambdaC. Confirm H=2delta on pure corner, then dilute."""
from fractions import Fraction as F
from pipeline import analyze, is_idempotent, delta
from gen import build_from_LambdaC


def rep(P, label, verbose=False):
    ok, _, _ = is_idempotent(P)
    if not ok:
        print(f"  {label}: NOT IDEMPOTENT"); return None
    res = analyze(P, label=label, verbose=verbose)
    if "note" in res:
        print(f"  {label}: delta=0"); return None
    d = res["delta"]; H = res["H"]
    tau2 = float(d) ** 0.5
    hb = None
    for v in res["hidden"]:
        s = res["sigma_tilde"][v]; dv = res["dists"][v]
        rec = dict(v=v, sig=s, distv=dv, sig_gt_tau=(s * s > d), dist_gt_tau=(dv * dv > d),
                   so=float(s) / tau2, do=float(dv) / tau2)
        if hb is None or dv > hb["distv"]:
            hb = rec
    print(f"  {label}: delta={float(d):.5f} H/tau={float(H)/tau2:.4f} H/delta={float(H)/float(d):.4f}"
          f" nW={len(res['W'])} hidden={res['hidden']}"
          + (f" | topv={hb['v']} sig/tau={hb['so']:.3f}(>1:{hb['sig_gt_tau']}) dist/tau={hb['do']:.3f}(>1:{hb['dist_gt_tau']})" if hb else " | no hidden vertex"))
    return res


print("### pure corner: C = signed combos, R2 = 0-ish (tail tiny) => expect H=2delta ###")
# k=3 corners, 2 hidden rows each reaching out along an edge.
C = [[F(1) + F(1,5), F(-1,5), F(0)],       # hidden row reaches beyond corner 1 (N=1/5)
     [F(0), F(1) + F(1,5), F(-1,5)]]
R2 = [[F(1,1000), F(1,1000)], [F(1,1000), F(1,1000)], [F(1,1000), F(1,1000)]]   # k=3 x m=2
rep(build_from_LambdaC(C, R2)[0], "pure-ish corner k=3 N=1/5")

print("\n### DILUTION scan: fix C negativity, grow tail mass R2 to cancel entry-negativity ###")
# k=2, hidden v = (1+N)r1 - N r2. Add 1 tail coord. R2 = [[a],[b]] archetype tail mass.
# Idea: make r1,r2 share tail mass so v's negative entries partly cancel.
N = F(2, 5)
C = [[F(1) + N, -N]]     # 1 hidden row
for a in [F(0), F(1,20), F(1,10), F(1,5), F(3,10), F(2,5), F(1,2)]:
    R2 = [[a], [a]]   # both archetypes put mass 'a' on the shared tail coord
    P, R, _ = build_from_LambdaC(C, R2)
    rep(P, f"dilute N=2/5 tail a={a}")

print("\n### DILUTION with ANTI-correlated tail (r1 tail high, r2 tail 0) ###")
for a in [F(0), F(1,10), F(1,5), F(3,10), F(2,5)]:
    R2 = [[a], [F(0)]]
    P, R, _ = build_from_LambdaC(C, R2)
    rep(P, f"dilute N=2/5 tail r1={a},r2=0")

print("\n### push N large (deep reach) at fixed small tail ###")
for Nn,Nd in [(1,2),(1,1),(2,1),(3,1),(5,1)]:
    N = F(Nn,Nd)
    C = [[F(1)+N, -N]]
    R2=[[F(1,100)],[F(1,100)]]
    P,R,_ = build_from_LambdaC(C,R2)
    rep(P, f"reach N={N} tail=1/100")
