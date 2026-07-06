#!/usr/bin/env python3
"""W25 orchestrator recompute — worker N's insufficiency certificate, from the printed values alone.

Scope: full algebraic recomputation of the 3x3 model (idempotence, row sums, nu, exact point
distances to the single labeled-visible row, g = P*1_G, harmonicity, sandwich, the labeled facts
F2/F3/F4 the model claims to satisfy) PLUS direct evaluation of the explicit exposer h(x) =
(100/101)*x_0 that shows the labeled-hidden top is (rho,kappa)-EXPOSED in the true geometry —
the certified violated fact. Everything here is evaluation of printed rationals; no worker
assertion is trusted.
"""

from fractions import Fraction as F

W_ROW = [F(1), F(0), F(0)]           # w (labeled visible)
V_ROW = [F(0), F(1), F(0)]           # v (labeled hidden top)
S_ROW = [F(101, 100), F(-1, 100), F(0)]  # s (band row)
P = [W_ROW, V_ROW, S_ROW]
DELTA = F(1, 100)          # tau = 1/10 exactly (delta is a perfect square of 1/10)
TAU = F(1, 10)

CHECKS = []


def check(cond, msg):
    if not cond:
        raise AssertionError("FAIL: " + msg)
    CHECKS.append(msg)


def l1(a, b):
    return sum(abs(x - y) for x, y in zip(a, b))


def main():
    n = 3
    P2 = [[sum(P[i][k] * P[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    check(P2 == P, "model: P^2 = P exactly")
    check(all(sum(r) == 1 for r in P), "model: row sums 1")
    negs = [sum(-x for x in r if x < 0) for r in P]
    check(max(negs) == DELTA, "model: delta = 1/100 (tau = 1/10)")
    check(DELTA < (F(17) - 12 * F(141421356237, 100000000000)) / 2 + F(1, 10**6),
          "model: delta below the delta_1 window (rational sandwich of 12*sqrt2)")
    # exact check of delta < (17 - 12*sqrt2)/2  <=>  17 - 2*delta > 12*sqrt2  <=>  (17-2*delta)^2 > 288
    check((17 - 2 * DELTA) ** 2 > 288, "model: delta < (17-12*sqrt2)/2 exactly (squared form)")

    # True point distances to conv{p_w} = the single point p_w.
    d = [l1(row, W_ROW) for row in P]
    check(d == [F(0), F(2), F(1, 50)], "model: true distances (0, 2, 1/50) to the labeled C_W")
    H_label = d[1]
    check(H_label > 13 * TAU, "model: labeled H = 2 > 13*tau = 13/10")

    # g = P * 1_G with labeled G_4 = {v} (index 1): column 1 of P.
    g = [P[i][1] for i in range(n)]
    check(g == [F(0), F(1), F(-1, 100)], "model: g = (0, 1, -1/100)")
    Pg = [sum(P[i][k] * g[k] for k in range(n)) for i in range(n)]
    check(Pg == g, "model: harmonicity P*g = g exactly")
    check(g[1] > F(1, 2) - DELTA, "model: labeled-hidden top has g > 1/2 - delta (F2 conclusion)")
    check(-negs[0] <= g[0] <= 4 * TAU, "model: labeled-visible row within [-nu, 4*tau] (F3 conclusion)")
    check(g[2] >= -negs[2], "model: band row within its sandwich floor")

    # The violated true-fact: v is actually (rho,kappa)-exposed. h(x) = (100/101)*x_0.
    def h(x):
        return F(100, 101) * x[0]
    vals = [h(row) for row in P]
    check(vals == [F(100, 101), F(0), F(1)], "exposer: h values (100/101, 0, 1)")
    check(h(V_ROW) == 0, "exposer: h(p_v) = 0")
    check(all(F(0) <= x <= F(1) for x in vals), "exposer: 0 <= h <= 1 on all rows (admissible)")
    rho, kappa = 4 * TAU, TAU / 4
    far = [i for i in range(n) if l1(P[i], V_ROW) >= rho]
    check(far == [0, 2], "exposer: far set (dist >= rho = 2/5) is {w, s}")
    margin = min(vals[i] for i in far)
    check(margin == F(100, 101) and margin >= kappa,
          "exposer: far margin 100/101 >= kappa = 1/40 — v is (rho,kappa)-EXPOSED in true geometry")

    for m in CHECKS:
        print("[orch-check]", m)
    print("OK: W25 orchestrator recompute — all", len(CHECKS), "checks passed;")
    print("    the scalar fact-set holds under the labels while true exposedness contradicts the")
    print("    'hidden' label — the certified insufficiency stands on printed values alone.")


if __name__ == "__main__":
    main()
