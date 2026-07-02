#!/usr/bin/env python3
"""Deliberate 2-level web: hidden rows near an edge feeding each other (s5 scaled up).
   Deterministic scan over poke depth p and archetype tail rho. Track (delta, sigma~/tau,
   H/tau, hidden, collapse-bound). Tests whether feeding can push H past 2delta / into regime."""
from fractions import Fraction as F
from pipeline import analyze, delta, is_idempotent
from gen import build_from_LambdaC

print("k=3 corners + m=2 hidden rows near e1-e2 edge, archetypes carry tail rho (feeding).")
print("hidden rows: C0=(1/2-x, 1/2+x+p, -p), C1=(1/2+x, 1/2-x+p, -p) twin poke depth p")
print(f"{'p':>8} {'rho':>7} {'delta':>9} {'H/delta':>8} {'H/tau':>7} {'sig/tau(top)':>12} {'hidden':>10} {'collapse_ok':>11}")
best_joint = None
best_Hd = None
for p in [F(1,100), F(1,40), F(1,20), F(1,16), F(1,12)]:
    for rho in [F(0), F(1,100), F(1,20), F(1,8), F(1,4)]:
        x = p / 3
        C = [[F(1,2) - x, F(1,2) + x + p, -p],
             [F(1,2) + x, F(1,2) - x + p, -p]]
        R2 = [[rho, rho], [rho, rho], [rho, rho]]
        try:
            P, R, _ = build_from_LambdaC(C, R2)
        except Exception as e:
            continue
        if not is_idempotent(P)[0]:
            print(f"  p={p} rho={rho}: NOT IDEMPOTENT"); continue
        d, negs = delta(P)
        if d == 0:
            continue
        res = analyze(P, verbose=False)
        tau = float(d) ** 0.5
        hidden = res["hidden"]
        # top hidden by dist
        if hidden:
            v = max(hidden, key=lambda i: res["dists"][i])
            dv = res["dists"][v]; s = res["sigma_tilde"][v]; nu = negs[v]
            Hd = float(dv)/float(d); Ht = float(dv)/tau; so = float(s)/tau
            collapse_ok = True
            if s < 1:
                collapse_ok = (dv*(1-s) <= nu*(2+4*d))
            over = 'd>1/4!' if d > F(1,4) else ''
            print(f"{float(p):>8.4f} {float(rho):>7.3f} {float(d):>9.5f} {Hd:>8.3f} {Ht:>7.4f} "
                  f"{so:>12.4f} {str(hidden):>10} {str(collapse_ok):>11} {over}")
            if d <= F(1,4):
                if s*s > d and (best_joint is None or Ht > best_joint[1]):
                    best_joint = (float(p), Ht, so, Hd)
                if best_Hd is None or Hd > best_Hd[1]:
                    best_Hd = (float(p), Hd, so)
        else:
            print(f"{float(p):>8.4f} {float(rho):>7.3f} {float(d):>9.5f} {'--':>8} {'--':>7} {'--':>12} {'[]':>10}")
print("\nbest joint (sig>tau) H/tau:", best_joint)
print("best H/delta:", best_Hd)
