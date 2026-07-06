#!/usr/bin/env python3
"""W20 orchestrator recompute — ALGEBRAIC side of the headline matrix, from the printed values alone.

Scope (session-9 discipline): idempotence, row sums, delta, and the g-arithmetic GIVEN the
worker-asserted halo set G_{1/4} = {5}. The geometric certifications (W, dist_1 to conv W, the
determination of G) remain worker-asserted and are NOT recomputed here.

Headline: worker A's zoo maximum of the visible-row harmonic observable at a = 1/4 —
g_w = 7/80 at row 4 of the rank-5 genuine-self instance (I007), (g/tau)^2 = 105/569;
hidden-top companion sigma_g(5) = 5991/80000.
"""

from fractions import Fraction as F

# I007 = w19_rank5_genuine_self, verbatim from
# runs/2026-07-06-w20-g-zoo-measurement/data/worker-a-report.md ("### I007").
I007 = [
    ["6409/6400", "-69/32000", "-1/64", "3/16000", "-341/16000", "3/80"],
    ["3/8000", "39977/40000", "-1/240", "1/20000", "-341/60000", "1/100"],
    ["3/1280", "-23/6400", "187/192", "1/3200", "-341/9600", "1/16"],
    ["1/2560", "-23/38400", "-5/1152", "19201/19200", "-341/57600", "1/96"],
    ["21/6400", "-161/32000", "-7/192", "7/16000", "45613/48000", "7/80"],
    ["-222027/6400000", "1702207/32000000", "74009/192000", "-74009/16000000", "25237069/48000000", "5991/80000"],
]

CHECKS = []


def check(cond, msg):
    if not cond:
        raise AssertionError("FAIL: " + msg)
    CHECKS.append(msg)


def main():
    P = [[F(x) for x in row] for row in I007]
    n = len(P)

    # Idempotence + row sums (algebraic, printed matrix alone).
    P2 = [[sum(P[i][k] * P[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    check(P2 == P, "I007: P^2 = P exactly")
    check(all(sum(row) == 1 for row in P), "I007: all row sums are 1")

    # delta = max row negative mass.
    negs = [sum(-x for x in row if x < 0) for row in P]
    check(max(negs) == F(3983, 96000), "I007: delta = 3983/96000")

    # Worker-asserted halo set at a = 1/4: G = {5}. g := P * 1_G = column 5 of P.
    G = [5]
    g = [sum(P[i][j] for j in G) for i in range(n)]
    Pg = [sum(P[i][k] * g[k] for k in range(n)) for i in range(n)]
    check(Pg == g, "I007: harmonicity P*g = g exactly (G = {5} worker-asserted)")
    check(g[4] == F(7, 80), "I007: visible-row headline g_4 = 7/80")
    check(max(P[5][5], F(0)) == F(5991, 80000), "I007: sigma_g(5) = pos(P[5][5]) = 5991/80000")

    # Sandwich at the deep row: sigma_g(5) - nu_5 <= g_5 <= sigma_g(5).
    check(F(5991, 80000) - negs[5] <= g[5] <= F(5991, 80000), "I007: sandwich at row 5")

    # (g/tau)^2 = g^2/delta = 105/569 for the headline row.
    check(g[4] * g[4] / F(3983, 96000) == F(105, 569), "I007: (g_4/tau)^2 = 105/569")

    for msg in CHECKS:
        print("[orch-check]", msg)
    print("[orch-check] geometric side (W = [0..4], dists, G determination) is worker-asserted, not recomputed here")
    print("OK: W20 orchestrator recompute — all", len(CHECKS), "algebraic checks passed")


if __name__ == "__main__":
    main()
