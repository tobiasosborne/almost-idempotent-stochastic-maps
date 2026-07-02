#!/usr/bin/env python3
"""Task 1: calibrate the exact pipeline on s5 (build_s5, d14_leakage.py:293-303).
   Recorded invariants: W={1,2,3}(1-idx)={0,1,2}(0-idx), hidden {4,5}={3,4},
   sigma~=1/2000, H=1/1000, delta=1841/1600000, g_5=0, forced_v=row 4(1-idx)=row 3.
   Also clone-invariance sanity check."""
from fractions import Fraction as F
from pipeline import analyze, clone_row, as_F, is_idempotent, delta, dist1_to_conv, visible_set


def build_s5_exact():
    return [
        [F(4000001, 4000000), F(-399, 8000000), F(-3603, 8000000), F(1801, 4000000), F(199, 4000000)],
        [F(1, 4000000), F(8001601, 8000000), F(-5603, 8000000), F(3801, 4000000), F(-1801, 4000000)],
        [F(1, 4000000), F(-2399, 8000000), F(7998397, 8000000), F(-199, 4000000), F(2199, 4000000)],
        [F(-1999, 4000000), F(1989, 40000), F(3801099, 4000000), F(0), F(1, 2000)],
        [F(-1999, 4000000), F(21999, 40000), F(1800099, 4000000), F(1, 2000), F(0)]]


P = build_s5_exact()
res = analyze(P, label="s5 (exact)")

print("\n--- checks vs recorded ---")
print("delta == 1841/1600000 :", res["delta"] == F(1841, 1600000), " got", res["delta"])
print("H     == 1/1000       :", res["H"] == F(1, 1000), " got", res["H"])
# recorded sigma~ = 1/2000 for the forced hidden vertex row 3 (0-idx)
print("sigma~[row3] == 1/2000:", res["sigma_tilde"][3] == F(1, 2000), " got", res["sigma_tilde"][3])
print("sigma~[row4]          :", res["sigma_tilde"][4])
print("W == [0,1,2]          :", res["W"] == [0, 1, 2], " got", res["W"])
print("hidden == [3,4]       :", sorted(res["hidden"]) == [3, 4], " got", res["hidden"])

# p4 - p5 separation (recorded 2003/2000)
sep = sum(abs(P[3][j] - P[4][j]) for j in range(5))
print("||p4-p5||_1 == 2003/2000:", sep == F(2003, 2000), " got", sep)

print("\n--- clone-invariance sanity: clone row 0 into 3 fibers (1/2,1/4,1/4) ---")
Pc = clone_row(P, 0, [F(1, 2), F(1, 4), F(1, 4)])
ok, idem, rs = is_idempotent(Pc)
print("cloned still exact idempotent:", ok)
dc, _ = delta(Pc)
print("delta invariant:", dc == res["delta"], " got", dc)
resc = analyze(Pc, label="s5 cloned row0 x3", verbose=False)
print("H invariant:", resc["H"] == res["H"], " got", resc["H"])
# sigma~ of the forced vertex: the forced vertex was row 3, now shifted by +2 (2 extra fibers before it)
# rows: [0a,0b,0c,1,2,3,4] -> forced hidden vertex is at new index 5
print("sigma~ of forced vertex invariant:",
      resc["sigma_tilde"][5] == res["sigma_tilde"][3], " got", resc["sigma_tilde"][5])
print("cloned hidden set:", resc["hidden"], " W:", resc["W"])
