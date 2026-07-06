#!/usr/bin/env python3
"""W25 worker N: exact abstract model for the step-4 fact surface.

This is not a Kernel counterexample.  It is a certificate that the scalar
facts listed in the step-4 brief do not by themselves contradict a sustained
{g >= 1/2} web.  The model deliberately treats W and the depths d_j as
abstract labels; the final audit proves that the hidden top would actually be
visible under the canonical exposedness definition.
"""

from fractions import Fraction as F
from itertools import combinations


def q(x):
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def subsets(n):
    items = range(n)
    for r in range(n + 1):
        for c in combinations(items, r):
            yield set(c)


def matmul(A, B):
    return [
        [sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))]
        for i in range(len(A))
    ]


def matvec(A, x):
    return [sum(A[i][j] * x[j] for j in range(len(x))) for i in range(len(A))]


def indicator(n, S):
    return [F(1) if i in S else F(0) for i in range(n)]


def l1(a, b):
    return sum(abs(a[i] - b[i]) for i in range(len(a)))


def neg_mass(row):
    return sum(max(-x, F(0)) for x in row)


def pos_mass_on(row, S):
    return sum(max(row[j], F(0)) for j in S)


def signed_mass_on(row, S):
    return sum(row[j] for j in S)


def assert_delta_below_delta1(delta):
    # delta < (17 - 12*sqrt(2))/2
    # iff 12*sqrt(2) < 17 - 2*delta; both sides are positive here.
    rhs = F(17) - 2 * delta
    assert rhs > 0
    assert rhs * rhs > F(288)


def main():
    names = ["w", "v", "s"]

    # Exact signed idempotent coefficient matrix.
    # Rows w and v are basis rows; s = (1+delta) w - delta v.
    P = [
        [F(1), F(0), F(0)],
        [F(0), F(1), F(0)],
        [F(101, 100), F(-1, 100), F(0)],
    ]
    n = len(P)
    delta = F(1, 100)
    tau = F(1, 10)
    rho = 4 * tau
    kappa = tau / 4
    H = F(2)
    a = F(4)

    # Abstract step-4 labels.  They agree with distance to conv{p_w} for this
    # chosen W, but W is not the canonical visible set of the row geometry.
    W = {0}
    hidden_vertices = {1, 2}
    hidden_tops = {1}
    d = [F(0), H, F(1, 50)]

    assert tau * tau == delta
    assert_delta_below_delta1(delta)
    assert delta <= F(1, 4)

    # Generic row facts.
    assert all(sum(row) == 1 for row in P)
    assert matmul(P, P) == P
    nus = [neg_mass(row) for row in P]
    assert max(nus) == delta
    assert all(nu <= delta for nu in nus)

    for i, row in enumerate(P):
        pos = sum(max(x, F(0)) for x in row)
        assert pos == 1 + nus[i]

    diameter_cap = 2 + 4 * delta
    diameters = {}
    for i in range(n):
        for j in range(n):
            dij = l1(P[i], P[j])
            diameters[(i, j)] = dij
            assert dij <= diameter_cap

    # Distances to the abstract C_W = conv{p_w}; singleton hull, so exact l1.
    assert all(d[i] == l1(P[i], P[0]) for i in range(n))
    assert max(d) == H
    assert H > 13 * tau

    # Stronger than the requested sandwich/harmonicity: every fixed column set.
    for S in subsets(n):
        gS = matvec(P, indicator(n, S))
        assert matvec(P, gS) == gS
        for i in range(n):
            sigmaS = pos_mass_on(P[i], S)
            assert sigmaS - nus[i] <= gS[i] <= sigmaS

    G4 = {j for j in range(n) if d[j] > a * tau}
    assert G4 == {1}
    g = matvec(P, indicator(n, G4))
    assert matvec(P, g) == g

    # Lemma A conclusion on the abstract visible set.
    for w in W:
        assert -nus[w] <= g[w] <= 4 * tau

    # Parametric-collapse forced-mass conclusion for hidden tops.
    outside = {j for j in range(n) if d[j] > 0}
    for v in hidden_tops:
        sigma4 = pos_mass_on(P[v], G4)
        sigma = pos_mass_on(P[v], outside)
        assert H * (1 - sigma4) <= (sigma - sigma4) * a * tau + nus[v] * (2 + 4 * delta)
        assert sigma4 > F(1, 2)
        assert g[v] > F(1, 2) - delta

    # Step-3 disintegration conclusion with identity vertex representations.
    lambdas = [[F(1) if i == v else F(0) for v in range(n)] for i in range(n)]
    denom = H - a * tau
    assert denom > 0
    disintegration_rows = []
    for i in range(n):
        M = F(0)
        slack = F(0)
        support = []
        for j in G4:
            pplus = max(P[i][j], F(0))
            deep_weight = sum(lambdas[j][v] for v in range(n) if d[v] > a * tau)
            M += pplus * deep_weight
            slack += pplus * (H - d[j]) / denom
            for v in range(n):
                if pplus * lambdas[j][v] > 0:
                    support.append((j, v, pplus * lambdas[j][v]))
                    assert v in hidden_vertices
                    assert d[v] > a * tau
        assert g[i] <= M + slack
        if g[i] >= F(1, 2):
            assert M >= F(1, 2) - slack
        disintegration_rows.append((M, slack, support))

    # Audit the intentional violation of the true visible-set geometry.
    # Row v is a row vertex: any convex combination of w and s has first
    # coordinate at least 1, while p_v has first coordinate 0.
    assert P[1][0] == 0 and P[0][0] == 1 and P[2][0] > 1
    # Exposer h(x) = (100/101) * x_0 exposes v.  It is admissible on all rows
    # and has far-row margin 100/101, much larger than kappa=1/40.
    hvals = [F(100, 101) * row[0] for row in P]
    assert hvals[1] == 0
    assert all(F(0) <= hv <= F(1) for hv in hvals)
    far_from_v = [i for i in range(n) if i != 1 and l1(P[i], P[1]) >= rho]
    assert set(far_from_v) == {0, 2}
    assert min(hvals[i] for i in far_from_v) >= kappa

    print("W25 worker N exact certificate: PASS")
    print("constants:")
    print(f"  delta={q(delta)} tau={q(tau)} rho={q(rho)} kappa={q(kappa)} H={q(H)}")
    print(f"  H/(tau)={q(H / tau)} and 13*tau={q(13 * tau)}")
    print("matrix P:")
    for name, row in zip(names, P):
        print(f"  {name}: [{', '.join(q(x) for x in row)}]  nu={q(neg_mass(row))}")
    print(f"abstract W={sorted(W)} hidden_vertices={sorted(hidden_vertices)} hidden_tops={sorted(hidden_tops)}")
    print(f"depths d=[{', '.join(q(x) for x in d)}], G_4={sorted(G4)}")
    print(f"g=P*1_G4=[{', '.join(q(x) for x in g)}]")
    print("disintegration rows (M, slack, support j->v weight):")
    for i, (M, slack, support) in enumerate(disintegration_rows):
        sup = ", ".join(f"{names[j]}->{names[v]}:{q(w)}" for j, v, w in support) or "-"
        print(f"  {names[i]}: M={q(M)} slack={q(slack)} support={sup}")
    print("intentional violation:")
    print("  row v is actually (rho,kappa)-exposed by h(x)=100/101*x_0")
    print(f"  h values=[{', '.join(q(x) for x in hvals)}], far margin={q(min(hvals[i] for i in far_from_v))}")


if __name__ == "__main__":
    main()
