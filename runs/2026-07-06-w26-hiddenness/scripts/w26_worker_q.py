#!/usr/bin/env python3
"""Worker Q (W26): exact hiddenness audit for the step-4 obstruction surface.

This is an obstruction-side tool, not a proof.  It does three exact things:

1. Re-audits the W25 3x3 model under the canonical exposedness definition.
2. Computes both the primal t*(v) LP and an equivalent dual/gauge LP:
      a hidden vertex forces a convex combination of rho-far rows to lie
      within a small cone from p_v.
3. Searches small exact signed idempotents from the Lambda-C generator for an
   F0-F10-style sustained width-4 web with true hiddenness.

Search misses are reported as [T3] only; they are not emptiness claims.
"""

import argparse
import random
import sys
from fractions import Fraction as F
from pathlib import Path

sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parents[3]
PIPE = ROOT / "runs" / "2026-07-02-web-regime-hunt" / "scripts"
sys.path.insert(0, str(PIPE))

from exact_lp import linprog_exact  # noqa: E402
from gen import build_from_LambdaC  # noqa: E402
from pipeline import (  # noqa: E402
    analyze,
    delta,
    dist1_to_conv,
    exposed_tstar,
    is_idempotent,
    is_row_vertex,
    l1,
    matmul,
)


def q(x):
    if x is None:
        return "inf"
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def qvec(row):
    return "[" + ", ".join(q(x) for x in row) + "]"


def matvec(A, x):
    return [sum(A[i][j] * x[j] for j in range(len(x))) for i in range(len(A))]


def neg_mass(row):
    return sum(max(-x, F(0)) for x in row)


def pos_mass_on(row, cols):
    return sum(max(row[j], F(0)) for j in cols)


def gt_c_tau(x, c, d):
    """Exact x > c*sqrt(d), for x >= 0 and rational c,d."""
    return x >= 0 and x * x > c * c * d


def ge_kappa(tstar, d):
    """Exact t* >= sqrt(delta)/4."""
    if tstar is None:
        return True
    return tstar >= 0 and 16 * tstar * tstar >= d


def far_rows(P, v, d):
    return [j for j in range(len(P)) if j != v and l1(P[j], P[v]) ** 2 >= 16 * d]


def hiddenness_gauge_lp(P, v, d):
    """Dual/gauge LP equivalent to the exposedness margin t*(v).

    Minimize alpha = sum_i beta_i such that a convex combination q of rho-far
    rows satisfies

        q - p_v = sum_i beta_i (p_i - p_v),   beta_i >= 0.

    With mu the far-row convex weights, this is linear:

        sum_far mu_j p_j - sum_i beta_i (p_i - p_v) = p_v,
        sum_far mu_j = 1, mu,beta >= 0.

    The optimum alpha equals t*(v) by LP duality/minimax.  In particular,
    t*(v) < kappa gives a concrete convex-combo witness near p_v.
    """
    n = len(P)
    far = far_rows(P, v, d)
    if not far:
        return None

    m = len(far)
    nv = m + n
    c = [F(0)] * m + [F(1)] * n

    A_eq = []
    b_eq = []
    for coord in range(n):
        row = [F(0)] * nv
        for r, j in enumerate(far):
            row[r] = P[j][coord]
        for i in range(n):
            row[m + i] = -(P[i][coord] - P[v][coord])
        A_eq.append(row)
        b_eq.append(P[v][coord])

    A_eq.append([F(1)] * m + [F(0)] * n)
    b_eq.append(F(1))

    bounds = [(F(0), None)] * nv
    r = linprog_exact(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds)
    assert r["status"] == "optimal", r

    mu = r["x"][:m]
    beta = r["x"][m:]
    alpha = sum(beta)
    qfar = [sum(mu[k] * P[far[k]][coord] for k in range(m)) for coord in range(n)]
    cone = [
        P[v][coord] + sum(beta[i] * (P[i][coord] - P[v][coord]) for i in range(n))
        for coord in range(n)
    ]
    assert qfar == cone
    return {"alpha": alpha, "far": far, "mu": mu, "beta": beta, "q": qfar}


def vertex_repr_over_vertices(P, row_index, vertices):
    """Return one exact convex representation over given vertices, or None."""
    n = len(P)
    m = len(vertices)
    nv = m + n
    c = [F(0)] * m + [F(1)] * n
    A_ub = []
    b_ub = []
    for coord in range(n):
        rp = [F(0)] * nv
        rn = [F(0)] * nv
        for k, v in enumerate(vertices):
            rp[k] = P[v][coord]
            rn[k] = -P[v][coord]
        rp[m + coord] = F(-1)
        rn[m + coord] = F(-1)
        A_ub.append(rp)
        b_ub.append(P[row_index][coord])
        A_ub.append(rn)
        b_ub.append(-P[row_index][coord])
    A_eq = [[F(1)] * m + [F(0)] * n]
    b_eq = [F(1)]
    bounds = [(F(0), None)] * m + [(F(0), None)] * n
    r = linprog_exact(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds)
    if r["status"] != "optimal" or r["fun"] != 0:
        return None
    return r["x"][:m]


def disintegration_check(P, W, dists, G4, g, a=F(4)):
    """Exact check of the W24 disintegration conclusion using LP vertex reps."""
    n = len(P)
    H = max(dists)
    if H * H <= a * a * d_global(P):
        return False, "H <= a*tau"

    vertices = [i for i in range(n) if is_row_vertex(P, i)[0]]
    reps = {}
    for j in range(n):
        if j in vertices:
            reps[j] = [F(1) if v == j else F(0) for v in vertices]
        else:
            lam = vertex_repr_over_vertices(P, j, vertices)
            if lam is None:
                return False, f"no vertex representation for row {j}"
            reps[j] = lam

    denom = H - a * sqrt_placeholder(d_global(P))
    # The real denominator is irrational if delta is nonsquare.  For exact
    # search filtering we only use this routine when delta is a rational square.
    assert denom > 0

    out = []
    for i in range(n):
        M = F(0)
        slack = F(0)
        support = []
        for j in G4:
            pplus = max(P[i][j], F(0))
            deep_weight = F(0)
            for k, v in enumerate(vertices):
                if dists[v] * dists[v] > a * a * d_global(P):
                    deep_weight += reps[j][k]
                    if pplus * reps[j][k] > 0:
                        support.append((j, v, pplus * reps[j][k]))
            M += pplus * deep_weight
            slack += pplus * (H - dists[j]) / denom
        if g[i] > M + slack:
            return False, f"row {i} violates disintegration"
        out.append((M, slack, support))
    return True, out


def d_global(P):
    return delta(P)[0]


def sqrt_placeholder(d):
    """Exact sqrt for the square-delta examples used in disintegration display."""
    # Current constructed/audited examples use square deltas.  Random search uses
    # squared comparisons and does not call the irrational-denominator check.
    num = int(d.numerator ** 0.5)
    den = int(d.denominator ** 0.5)
    if num * num == d.numerator and den * den == d.denominator:
        return F(num, den)
    raise ValueError(f"delta is not a rational square: {d}")


def audit(P, names, label, show_matrix=False):
    n = len(P)
    ok, idem, rowsum = is_idempotent(P)
    assert ok, (idem, rowsum)
    d, nus = delta(P)
    res = analyze(P, label=label, verbose=False)
    W = res["W"]
    info = res["info"]
    dists = res["dists"]
    H = res["H"]
    vertices = [i for i in range(n) if info.get(i, {}).get("vertex")]
    hidden = res["hidden"]
    G4 = [j for j in range(n) if dists[j] is not None and dists[j] * dists[j] > 16 * d]
    g = matvec(P, [F(1) if j in G4 else F(0) for j in range(n)])
    assert matvec(P, g) == g

    top = [i for i in hidden if dists[i] == H]
    sustained = [i for i in top if g[i] >= F(1, 2)]
    visible_small = all(-nus[w] <= g[w] <= 4 * sqrt_placeholder(d) for w in W) if square_delta(d) else None
    tall13 = H * H > 169 * d
    delta1 = delta_below_delta1(d)

    gauges = {}
    for v in vertices:
        ts = exposed_tstar(P, v, d)
        gu = hiddenness_gauge_lp(P, v, d)
        if gu is not None:
            assert gu["alpha"] == ts, (v, gu["alpha"], ts)
        gauges[v] = (ts, gu)

    print(f"\n=== {label} ===")
    print(f"[T1] n={n} idempotent={idem} rowsum={rowsum} delta={q(d)}")
    print(f"[T1] W={fmt_names(W, names)} vertices={fmt_names(vertices, names)} hidden={fmt_names(hidden, names)}")
    print(f"[T1] H={q(H)} H^2/delta={q(H * H / d) if d else 'inf'} tall13={tall13} delta<delta1={delta1}")
    print(f"[T1] G4={fmt_names(G4, names)} g={qvec(g)} top_hidden={fmt_names(top, names)} sustained_top={fmt_names(sustained, names)}")
    print(f"[T1] visible_small={visible_small}")
    for v in vertices:
        ts, gu = gauges[v]
        cls = "VISIBLE" if ge_kappa(ts, d) else "HIDDEN"
        print(f"[T1] row {names[v]}: t*={q(ts)} class={cls} far={fmt_names(far_rows(P, v, d), names)}")
        if gu is not None and not ge_kappa(ts, d):
            D = max(l1(P[i], P[j]) for i in range(n) for j in range(n))
            dist_to_far_conv = l1(P[v], gu["q"])
            print(
                f"[T1]   dual alpha={q(gu['alpha'])}; "
                f"||p_v-q_far||_1={q(dist_to_far_conv)} <= alpha*D={q(gu['alpha'] * D)}"
            )
            print(f"[T1]   far mu={fmt_weighted(gu['far'], gu['mu'], names)}")
            print(f"[T1]   cone beta={fmt_weighted(range(n), gu['beta'], names)}")
    if show_matrix:
        print("[T1] matrix P:")
        for name, row, nu in zip(names, P, nus):
            print(f"  {name}: {qvec(row)}  nu={q(nu)}")

    bad = bool(W) and tall13 and bool(sustained)
    return {
        "P": P,
        "names": names,
        "delta": d,
        "W": W,
        "hidden": hidden,
        "H": H,
        "G4": G4,
        "g": g,
        "top": top,
        "sustained": sustained,
        "bad": bad,
        "delta1": delta1,
        "visible_small": visible_small,
        "gauges": gauges,
    }


def fmt_names(indices, names):
    return "[" + ", ".join(names[i] for i in indices) + "]"


def fmt_weighted(indices, weights, names):
    parts = []
    for i, w in zip(indices, weights):
        if w:
            parts.append(f"{names[i]}:{q(w)}")
    return "{" + ", ".join(parts) + "}"


def square_delta(d):
    try:
        sqrt_placeholder(d)
        return True
    except ValueError:
        return False


def delta_below_delta1(d):
    # d < (17 - 12*sqrt(2))/2 iff 12*sqrt(2) < 17 - 2d.
    rhs = F(17) - 2 * d
    return rhs > 0 and rhs * rhs > F(288)


def w25_model():
    P = [
        [F(1), F(0), F(0)],
        [F(0), F(1), F(0)],
        [F(101, 100), F(-1, 100), F(0)],
    ]
    return P, ["w", "v", "s"]


def known_hidden_family():
    # The exact hidden rank-5 style family from the web-regime pipeline.
    p = F(1, 40)
    rho = F(1, 100)
    x = p / 3
    C = [
        [F(1, 2) - x, F(1, 2) + x + p, -p],
        [F(1, 2) + x, F(1, 2) - x + p, -p],
    ]
    R2 = [[rho, rho], [rho, rho], [rho, rho]]
    P, _, _ = build_from_LambdaC(C, R2)
    return P, [f"r{i}" for i in range(len(P))]


def random_C(rng, m, k):
    denoms = [2, 3, 4, 5, 6, 8, 10, 12, 16, 20, 25, 40, 50, 100]
    C = []
    for _ in range(m):
        home = rng.randrange(k)
        row = [F(0)] * k
        budget_den = rng.choice([2, 3, 4, 6, 10, 20])
        budget = F(rng.randint(0, budget_den), budget_den)
        used = F(0)
        others = [j for j in range(k) if j != home]
        rng.shuffle(others)
        for j in others:
            if used >= budget:
                break
            den = rng.choice(denoms)
            raw = F(rng.randint(0, den), den)
            amt = raw * (budget - used)
            sign = rng.choice([F(1), F(-1), F(-1), F(-2)])
            row[j] += sign * amt
            used += abs(amt)
        row[home] = F(1) - sum(row)
        C.append(row)
    return C


def random_R2(rng, k, m):
    denoms = [10, 20, 50, 100, 200]
    mode = rng.random()
    if mode < 0.25:
        return [[F(0)] * m for _ in range(k)]
    scale = rng.choice([1, 2, 4, 8, 16])
    return [[F(rng.randint(0, den), den * scale) for _ in range(m)] for _ in range(k) for den in [rng.choice(denoms)]]


def search_small(seed=26017, samples=320):
    rng = random.Random(seed)
    best_Ht = None
    best_web = None
    hidden_records = 0
    audited = 0
    tall = 0
    in_delta1 = 0
    hidden_in_delta1 = 0
    tall_in_delta1 = 0
    found = None

    for _ in range(samples):
        k = rng.choice([2, 3, 3, 4, 4, 5])
        m = rng.choice([1, 2, 2, 3, 3, 4, 5])
        if k + m > 10:
            continue
        C = random_C(rng, m, k)
        R2 = random_R2(rng, k, m)
        try:
            P, _, _ = build_from_LambdaC(C, R2)
        except Exception:
            continue
        if not is_idempotent(P)[0]:
            continue
        d, _ = delta(P)
        if d == 0 or d > F(1, 4):
            continue
        audited += 1
        in_window = delta_below_delta1(d)
        if in_window:
            in_delta1 += 1
        try:
            res = analyze(P, verbose=False)
        except Exception:
            continue
        if "note" in res or not res["W"]:
            continue
        W = res["W"]
        hidden = res["hidden"]
        if not hidden:
            continue
        hidden_records += len(hidden)
        if in_window:
            hidden_in_delta1 += len(hidden)
        H = res["H"]
        G4 = [j for j, dj in enumerate(res["dists"]) if dj is not None and dj * dj > 16 * d]
        g = matvec(P, [F(1) if j in G4 else F(0) for j in range(len(P))])
        top = [i for i in hidden if res["dists"][i] == H]
        sustained = [i for i in top if g[i] >= F(1, 2)]
        rec = {
            "P": P,
            "k": k,
            "m": m,
            "delta": d,
            "H": H,
            "Ht2": H * H / d,
            "W": W,
            "hidden": hidden,
            "G4": G4,
            "g": g,
            "top": top,
            "sustained": sustained,
        }
        if H * H > 169 * d:
            tall += 1
            if in_window:
                tall_in_delta1 += 1
        if best_Ht is None or rec["Ht2"] > best_Ht["Ht2"]:
            best_Ht = rec
        if sustained and (best_web is None or rec["Ht2"] > best_web["Ht2"]):
            best_web = rec
        if W and H * H > 169 * d and sustained:
            found = rec
            break

    return {
        "seed": seed,
        "samples": samples,
        "audited": audited,
        "in_delta1": in_delta1,
        "hidden_records": hidden_records,
        "hidden_in_delta1": hidden_in_delta1,
        "tall": tall,
        "tall_in_delta1": tall_in_delta1,
        "found": found,
        "best_Ht": best_Ht,
        "best_web": best_web,
    }


def print_search_summary(summary):
    print("\n=== exact small-model search ===")
    print(
        f"[T3] seed={summary['seed']} samples={summary['samples']} "
        f"audited_idempotents={summary['audited']} hidden_vertex_records={summary['hidden_records']} "
        f"tall13_records={summary['tall']}"
    )
    print(
        f"[T3] delta-window audited={summary['in_delta1']} "
        f"hidden_vertex_records_in_window={summary['hidden_in_delta1']} "
        f"tall13_records_in_window={summary['tall_in_delta1']}"
    )
    if summary["found"] is None:
        print("[T3] no F0-F10 sustained tall web found in this bounded Lambda-C search")
    else:
        print("[T1] found a candidate sustained tall web")
    for tag in ["best_Ht", "best_web"]:
        rec = summary[tag]
        if rec is None:
            print(f"[T3] {tag}: none")
            continue
        names = [f"x{i}" for i in range(len(rec["P"]))]
        print(
            f"[T3] {tag}: n={len(rec['P'])} k={rec['k']} m={rec['m']} "
            f"delta={q(rec['delta'])} H={q(rec['H'])} H^2/delta={q(rec['Ht2'])} "
            f"H/tau~={float(rec['Ht2']) ** 0.5:.6f} "
            f"W={fmt_names(rec['W'], names)} hidden={fmt_names(rec['hidden'], names)} "
            f"G4={fmt_names(rec['G4'], names)} sustained_top={fmt_names(rec['sustained'], names)}"
        )
        print("[T3] matrix:")
        for name, row in zip(names, rec["P"]):
            print(f"  {name}: {qvec(row)}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=26017)
    parser.add_argument("--samples", type=int, default=1000)
    args = parser.parse_args()

    print("W26 Worker Q hiddenness obstruction audit")
    print("[T0] Hiddenness dual/gauge statement:")
    print(
        "[T0] t*(v) equals the minimum alpha for which a convex combination q of rho-far rows "
        "satisfies q-p_v=sum_i beta_i(p_i-p_v), beta_i>=0, sum beta_i=alpha."
    )
    print(
        "[T0] Hence t*(v)<kappa forces dist_1(p_v, conv(far_rows)) <= "
        "kappa*(2+4*delta)."
    )

    P25, names25 = w25_model()
    audit(P25, names25, "W25 3x3 under canonical geometry", show_matrix=True)

    Phid, nameshid = known_hidden_family()
    audit(Phid, nameshid, "known true-hidden rank-5 calibration", show_matrix=True)

    summary = search_small(seed=args.seed, samples=args.samples)
    print_search_summary(summary)
    if summary["found"] is not None:
        names = [f"c{i}" for i in range(len(summary["found"]["P"]))]
        audit(summary["found"]["P"], names, "FOUND candidate", show_matrix=True)


if __name__ == "__main__":
    main()
