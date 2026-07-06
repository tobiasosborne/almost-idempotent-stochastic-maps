#!/usr/bin/env python3
"""W21 orchestrator recompute — ALGEBRAIC side of worker D's frontier matrices, printed values alone.

Scope (session-9 discipline): idempotence, row sums, delta, and the g-arithmetic GIVEN the
worker-asserted halo set G_{1/4} = {5} on the frontier instance. Geometric certifications
(W, dist_1 to conv W, t*, the determination of G, the absorption W-flip) remain worker-asserted.

Headline: the refuter's small-halo frontier certificate — visible row 4 with g = 49/400 at
a = 1/4, delta = 27881/480000, K^2 = (g/tau)^2 = 147/569 — and the algebraic side of the
lambda = 29/20 absorption companion.
"""

from fractions import Fraction as F

# scaled-rank5-lambda-7/5, verbatim from
# runs/2026-07-06-w21-lemma-a-decider/data/worker-d-report.md.
FRONTIER = [
    ["32063/32000", "-483/160000", "-7/320", "21/80000", "-2387/80000", "21/400"],
    ["21/40000", "199839/200000", "-7/1200", "7/100000", "-2387/300000", "7/500"],
    ["21/6400", "-161/32000", "185/192", "7/16000", "-2387/48000", "7/80"],
    ["7/12800", "-161/192000", "-7/1152", "96007/96000", "-2387/288000", "7/480"],
    ["147/32000", "-1127/160000", "-49/960", "49/80000", "223291/240000", "49/400"],
    ["-1074189/32000000", "8235449/160000000", "358063/960000", "-358063/80000000", "122099483/240000000", "41937/400000"],
]

# scaled-rank5-lambda-29/20-absorption, verbatim from the same report.
ABSORPTION = [
    ["128261/128000", "-2001/640000", "-29/1280", "87/320000", "-9889/320000", "87/1600"],
    ["87/160000", "799333/800000", "-29/4800", "29/400000", "-9889/1200000", "29/2000"],
    ["87/25600", "-667/128000", "739/768", "29/64000", "-9889/192000", "29/320"],
    ["29/51200", "-667/768000", "-29/4608", "384029/384000", "-9889/1152000", "29/1920"],
    ["609/128000", "-4669/640000", "-203/3840", "203/320000", "890777/960000", "203/1600"],
    ["-4278783/128000000", "32804003/640000000", "1426261/3840000", "-1426261/320000000", "486355001/960000000", "173739/1600000"],
]

CHECKS = []


def check(cond, msg):
    if not cond:
        raise AssertionError("FAIL: " + msg)
    CHECKS.append(msg)


def parse(M):
    return [[F(x) for x in row] for row in M]


def algebra(P, label, delta_expected):
    n = len(P)
    P2 = [[sum(P[i][k] * P[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    check(P2 == P, f"{label}: P^2 = P exactly")
    check(all(sum(row) == 1 for row in P), f"{label}: all row sums are 1")
    negs = [sum(-x for x in row if x < 0) for row in P]
    check(max(negs) == delta_expected, f"{label}: delta = {delta_expected}")
    return negs


def main():
    P = parse(FRONTIER)
    d = F(27881, 480000)
    negs = algebra(P, "frontier", d)

    # Worker-asserted G_{1/4} = {5}: g = column 5.
    n = len(P)
    g = [P[i][5] for i in range(n)]
    Pg = [sum(P[i][k] * g[k] for k in range(n)) for i in range(n)]
    check(Pg == g, "frontier: harmonicity P*g = g exactly (G = {5} worker-asserted)")
    check(g[4] == F(49, 400), "frontier: visible-row certificate g_4 = 49/400")
    check(g[4] * g[4] / d == F(147, 569), "frontier: K^2 = (g_4/tau)^2 = 147/569")
    check(g[4] * g[4] / d > F(1, 4), "frontier: K > 1/2 (the small-halo frontier beats the zoo's 0.43)")
    check(negs[4] == d, "frontier: the binding row negativity sits on the certificate row 4")

    P2m = parse(ABSORPTION)
    algebra(P2m, "absorption companion", F(115507, 1920000))

    for msg in CHECKS:
        print("[orch-check]", msg)
    print("[orch-check] geometric side (W, dists, t*, G determination, the W-flip) is worker-asserted, not recomputed here")
    print("OK: W21 orchestrator recompute — all", len(CHECKS), "algebraic checks passed")


if __name__ == "__main__":
    main()
