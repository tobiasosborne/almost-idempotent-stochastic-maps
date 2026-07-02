#!/usr/bin/env python3
"""Realize the budget/face-poke family as ACTUAL exact idempotents and confirm:
   (i) H=2delta, t*=delta/(1+delta), sigma~=0, hiddenness transition at corner scale;
   (ii) push sigma~ toward 1 and watch H (test the H <= nu(2+4d)/(1-sigma~) collapse).
   Exact throughout."""
from fractions import Fraction as F
from pipeline import analyze, is_idempotent, delta, exposed_tstar, visible_set
from gen import build_from_LambdaC


def realize(C_rows, m_tail=None, tail=F(0)):
    """k=3 corners + hidden rows given by C_rows (each a combo over 3 corners, sum 1).
       tail: tiny archetype tail mass (0 => pure corners, sigma~=0 possible)."""
    k = 3
    m = len(C_rows)
    R2 = [[tail for _ in range(m)] for _ in range(k)]
    return build_from_LambdaC(C_rows, R2)


print("### BUDGET FACE-POKE: single vertex past MID-EDGE (should be hidden, H=2delta) ###")
print("  v = 0.5 e1 + (0.5+depth) e2 - depth e3  (poke from mid e1-e2 edge)")
for depth in [F(1,1000), F(1,100), F(1,50), F(1,20), F(1,16), F(1,12), F(1,10), F(7,100), F(1,14)]:
    # single poke vertex + a twin to shield (twin at small gap)
    C = [[F(1,2), F(1,2) + depth, -depth]]
    P, R, _ = realize(C)
    ok, _, _ = is_idempotent(P)
    res = analyze(P, verbose=False)
    d = res["delta"]
    if d == 0:
        print(f"  depth={depth}: delta 0"); continue
    tau = float(d) ** 0.5
    Hd = float(res["H"]) / float(d)
    Ht = float(res["H"]) / tau
    # exposedness margin of the poke vertex (row 3)
    ts = exposed_tstar(P, 3, d)
    ishidden = 3 in res["hidden"]
    tsf = float(ts) if ts is not None else None
    kappa = tau / 4
    print(f"  depth={depth}: delta={float(d):.5f} H/delta={Hd:.3f} H/tau={Ht:.4f} "
          f"t*={tsf if tsf is None else round(tsf,5)} kappa={kappa:.5f} hidden(row3)={ishidden} "
          f"W={res['W']} verts={[i for i in range(len(P)) if res['info'].get(i,{}).get('vertex')]}")

print("\n### TWIN face-poke (two close vertices shielding each other) ###")
for depth in [F(1,100), F(1,20), F(1,14), F(1,12), F(1,10)]:
    gap = depth / 4
    C = [[F(1,2), F(1,2) + depth, -depth],
         [F(1,2) + gap, F(1,2) - gap + depth, -depth]]
    P, R, _ = realize(C)
    res = analyze(P, verbose=False)
    d = res["delta"]; tau = float(d) ** 0.5
    print(f"  depth={depth} gap={gap}: delta={float(d):.5f} H/delta={float(res['H'])/float(d):.3f} "
          f"H/tau={float(res['H'])/tau:.4f} hidden={res['hidden']} W={res['W']}")

print("\n### CONFIRM t* = delta/(1+delta) on the single mid-edge poke ###")
for depth in [F(1,100), F(1,50), F(1,20)]:
    C = [[F(1,2), F(1,2) + depth, -depth]]
    P, R, _ = realize(C)
    d, _ = delta(P)
    ts = exposed_tstar(P, 3, d)
    print(f"  depth={depth}: delta={d} t*={ts} delta/(1+delta)={d/(1+d)}  match={ts == d/(1+d) if ts else 'inf'}")
