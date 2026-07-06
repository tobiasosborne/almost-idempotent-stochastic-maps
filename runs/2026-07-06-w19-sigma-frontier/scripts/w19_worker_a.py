#!/usr/bin/env python3
"""W19 worker A exact-feasibility scratch report.

This script is intentionally scratch-only.  It reuses the repo's exact Fraction
pipeline and writes ANSWER-A.md.  Floats appear only in parenthetical intuition.
"""

from __future__ import annotations

import sys
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SCRATCH = Path(__file__).resolve().parent
WEB = ROOT / "runs/2026-07-02-web-regime-hunt/scripts"
sys.path.insert(0, str(WEB))

import gen  # noqa: E402
import pipeline as pipe  # noqa: E402
from exact_lp import linprog_exact  # noqa: E402


ASSERTS: list[str] = []


def hard_assert(cond: bool, msg: str) -> None:
    if not cond:
        raise AssertionError(msg)
    ASSERTS.append(msg)


def fstr(x: F | None) -> str:
    if x is None:
        return "None"
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def mat_str(P: list[list[F]]) -> str:
    rows = []
    for row in P:
        rows.append("[" + ", ".join(f'"{fstr(x)}"' for x in row) + "]")
    return "[\n  " + ",\n  ".join(rows) + "\n]"


def pos(x: F) -> F:
    return x if x > 0 else F(0)


def analyze_matrix(P: list[list[F]], label: str) -> dict:
    """Exact geometry from P alone, using strict halo threshold dist > tau/4."""
    ok, idem, rowsum = pipe.is_idempotent(P)
    hard_assert(ok and idem and rowsum, f"{label}: P^2=P and P1=1 from the printed matrix")
    d, negs = pipe.delta(P)
    hard_assert(d > 0 and d <= F(1, 4), f"{label}: 0 < delta <= 1/4")
    W, info = pipe.visible_set(P, d)
    hard_assert(bool(W), f"{label}: W(P) is nonempty")
    dists = [pipe.dist1_to_conv(P, W, i)[0] for i in range(len(P))]
    hard_assert(all(x is not None for x in dists), f"{label}: all row distances to conv W computed exactly")
    H = max(dists)
    hidden = tuple(i for i in range(len(P)) if info.get(i, {}).get("vertex") and not info.get(i, {}).get("exposed"))
    tops = tuple(i for i in hidden if H > 0 and dists[i] == H)
    halo = tuple(j for j, dist in enumerate(dists) if 16 * dist * dist > d)
    sigma_g = {v: sum(pos(P[v][j]) for j in halo) for v in tops}
    sigma_raw = {
        v: sum(pos(P[v][j]) for j, dist in enumerate(dists) if dist > 0)
        for v in range(len(P))
    }
    return {
        "P": P,
        "n": len(P),
        "delta": d,
        "negs": tuple(negs),
        "W": tuple(W),
        "info": info,
        "dists": tuple(dists),
        "H": H,
        "hidden": hidden,
        "tops": tops,
        "halo": halo,
        "sigma_g": sigma_g,
        "sigma_raw": sigma_raw,
    }


def build_from_lambdac(C: list[list[F]], R2: list[list[F]]) -> list[list[F]]:
    P, _R, _C = gen.build_from_LambdaC(C, R2)
    return P


def calibration_instances() -> list[tuple[str, dict]]:
    out: list[tuple[str, dict]] = []

    # Banked F2 raw-halo witness: huge raw self-mass, zero halo-robust mass.
    C = [[F(28, 25), F(1, 200), F(0), F(-1, 8)]]
    R2 = [[F(-49, 800)], [F(-1, 6)], [F(-1, 8)], [F(-33, 800)]]
    g = analyze_matrix(build_from_lambdac(C, R2), "calibration sigma-halo-nonrobust")
    hit = [v for v in g["tops"] if g["sigma_raw"][v] == F(5343, 5000) and g["sigma_g"][v] == 0]
    hard_assert(g["delta"] == F(252559, 1280000), "calibration: delta=252559/1280000")
    hard_assert(bool(hit), "calibration: raw sigma=5343/5000 and strict-halo sigma_g=0")
    out.append(("calibration_sigma_halo_nonrobust", g))

    # Banked F2 genuine-recipient rank-3 point with a distinct partner.
    C = [[F(1, 2), F(-1, 20), F(11, 20)], [F(257, 400), F(-7, 200), F(157, 400)]]
    R2 = [[F(9, 200), F(1, 80)], [F(1, 200), F(1, 200)], [F(11, 160), F(1, 100)]]
    g = analyze_matrix(build_from_lambdac(C, R2), "calibration rank3 genuine partner")
    hard_assert(g["delta"] == F(74551, 1600000), "rank3 partner: delta=74551/1600000")
    hard_assert(g["tops"] == (3,), "rank3 partner: hidden top is row 3")
    hard_assert(g["halo"] == (3, 4), "rank3 partner: strict-halo recipients are rows 3 and 4")
    hard_assert(g["sigma_g"][3] == F(229, 3200), "rank3 partner: sigma_g(row3)=229/3200")
    out.append(("rank3_genuine_partner", g))

    return out


def duplicate_split_instance(m: int, q: F) -> dict:
    """Rank-3 duplicate outside-recipient family.

    p=1/20, hidden-column total q=m*rho.  The certified hidden side below uses
    q=5/84.  The exposure failure comparison uses q=1/16.
    """
    p = F(1, 20)
    rho = q / m
    c = [F(1, 2), F(1, 2) + p, -p]
    C = [c[:] for _ in range(m)]
    R2 = [[rho for _ in range(m)] for _ in range(3)]
    return analyze_matrix(build_from_lambdac(C, R2), f"duplicate split m={m} q={q}")


def rank5_genuine_self() -> dict:
    C = [[F(-3, 80), F(23, 400), F(5, 12), F(-1, 200), F(341, 600)]]
    R2 = [[F(3, 80)], [F(1, 100)], [F(1, 16)], [F(1, 96)], [F(7, 80)]]
    g = analyze_matrix(build_from_lambdac(C, R2), "rank5 genuine self")
    hard_assert(g["delta"] == F(3983, 96000), "rank5 genuine self: delta=3983/96000")
    hard_assert(g["tops"] == (5,), "rank5 genuine self: hidden top is row 5")
    hard_assert(g["halo"] == (5,), "rank5 genuine self: strict-halo recipient is row 5")
    hard_assert(g["sigma_g"][5] == F(5991, 80000), "rank5 genuine self: sigma_g(row5)=5991/80000")
    return g


def solve_relaxed_cycle_lp() -> tuple[list[list[F]], F]:
    """Exact row-negativity LP for a rank-3, three-recipient cycle design.

    This deliberately omits exposedness constraints.  The optimizer can put
    mass 5/4 on the designated hidden columns, but the exact geometry then
    absorbs those columns into W, so no hidden top remains.
    """
    eps = F(1, 4)
    C = [[1 + eps, -eps, F(0)], [F(0), 1 + eps, -eps], [-eps, F(0), 1 + eps]]
    m, k = len(C), len(C[0])
    n = k + m
    nr = k * m

    def ridx(s: int, a: int) -> int:
        return s * m + a

    def p_expr(i: int, j: int) -> tuple[F, list[F]]:
        coeff = [F(0)] * nr
        const = F(0)
        if i < k:
            s = i
            if j < k:
                const = F(1) if s == j else F(0)
                for a in range(m):
                    coeff[ridx(s, a)] -= C[a][j]
            else:
                coeff[ridx(s, j - k)] += F(1)
        else:
            arow = i - k
            if j < k:
                const = C[arow][j]
                for b in range(m):
                    for s in range(k):
                        coeff[ridx(s, b)] -= C[arow][s] * C[b][j]
            else:
                b = j - k
                for s in range(k):
                    coeff[ridx(s, b)] += C[arow][s]
        return const, coeff

    # Variables: R2 entries, then row-entry negative-part witnesses.
    def nidx(i: int, j: int) -> int:
        return nr + i * n + j

    N = nr + n * n
    target_v = k
    J = [k, k + 1, k + 2]
    objective = [F(0)] * N
    for j in J:
        _const, coeff = p_expr(target_v, j)
        for q, val in enumerate(coeff):
            objective[q] -= val

    A_ub: list[list[F]] = []
    b_ub: list[F] = []
    for i in range(n):
        for j in range(n):
            const, coeff = p_expr(i, j)
            row = [F(0)] * N
            for q, val in enumerate(coeff):
                row[q] -= val
            row[nidx(i, j)] = F(-1)
            A_ub.append(row)
            b_ub.append(const)
            row = [F(0)] * N
            row[nidx(i, j)] = F(-1)
            A_ub.append(row)
            b_ub.append(F(0))
        row = [F(0)] * N
        for j in range(n):
            row[nidx(i, j)] = F(1)
        A_ub.append(row)
        b_ub.append(F(1, 4))
    for j in J:
        const, coeff = p_expr(target_v, j)
        row = [F(0)] * N
        for q, val in enumerate(coeff):
            row[q] -= val
        A_ub.append(row)
        b_ub.append(const)

    bounds = [(None, None)] * nr + [(F(0), None)] * (n * n)
    res = linprog_exact(objective, A_ub=A_ub, b_ub=b_ub, bounds=bounds)
    hard_assert(res["status"] == "optimal", "rank3 relaxed cycle LP: exact LP optimum exists")
    x = res["x"]
    R2 = [[x[ridx(s, a)] for a in range(m)] for s in range(k)]
    P = build_from_lambdac(C, R2)
    mass = sum(pos(P[target_v][j]) for j in J)
    hard_assert(mass == F(5, 4), "rank3 relaxed cycle LP: designated positive mass is 5/4")
    return P, mass


def summarize_geom(g: dict) -> str:
    sig = {k: fstr(v) for k, v in g["sigma_g"].items()}
    dists = [fstr(x) for x in g["dists"]]
    tstars = {
        i: ("inf" if g["info"].get(i, {}).get("tstar") is None else fstr(g["info"].get(i, {}).get("tstar")))
        for i in range(g["n"])
        if g["info"].get(i, {}).get("vertex")
    }
    return (
        f"delta={fstr(g['delta'])}; W={list(g['W'])}; H={fstr(g['H'])}; "
        f"hidden={list(g['hidden'])}; tops={list(g['tops'])}; halo={list(g['halo'])}; "
        f"sigma_g={sig}; dists={dists}; tstars={tstars}"
    )


def section_for_matrix(title: str, g: dict, binding: str) -> list[str]:
    return [
        f"### {title}",
        "",
        f"- [T1] Exact certificate: `{summarize_geom(g)}`.",
        f"- [T2] Binding constraint read: {binding}",
        "",
        "Full exact matrix `P`:",
        "",
        "```python",
        mat_str(g["P"]),
        "```",
        "",
    ]


def make_report() -> str:
    calibs = calibration_instances()

    split2 = duplicate_split_instance(2, F(5, 84))
    split4 = duplicate_split_instance(4, F(5, 84))
    split8 = duplicate_split_instance(8, F(5, 84))
    for m, g in [(2, split2), (4, split4), (8, split8)]:
        hard_assert(g["delta"] == F(1, 16), f"duplicate split m={m}: delta=1/16")
        hard_assert(g["W"] == (0, 1, 2), f"duplicate split m={m}: W=(0,1,2)")
        hard_assert(g["H"] == F(1, 10), f"duplicate split m={m}: H=1/10")
        hard_assert(all(g["sigma_g"][v] == F(5, 84) for v in g["tops"]), f"duplicate split m={m}: sigma_g=5/84")

    split_fail = duplicate_split_instance(2, F(1, 16))
    hard_assert(split_fail["hidden"] == (), "duplicate split q=1/16: recipients become visible; no hidden top")

    rank5 = rank5_genuine_self()

    relaxed_P, relaxed_mass = solve_relaxed_cycle_lp()
    relaxed_g = analyze_matrix(relaxed_P, "rank3 relaxed cycle LP optimum")
    hard_assert(relaxed_g["hidden"] == (), "rank3 relaxed cycle LP optimum: no hidden vertices after exact geometry")

    rank3_partner = dict(calibs)["rank3_genuine_partner"]
    sigma_best = max(F(5, 84), rank3_partner["sigma_g"][3], rank5["sigma_g"][5])
    hard_assert(sigma_best == F(5991, 80000), "best certified sigma_g in this worker report is 5991/80000")
    hard_assert(sigma_best < F(1, 2), "best certified sigma_g is below 1/2")

    lines: list[str] = []
    lines.append("NOT-REALIZED-HERE. Best certified strict-halo `sigma_g` in this worker report is `5991/80000` (rank 5, self-recipient), and the best rank-3 distinct-partner point is `229/3200`; both are far below `1/2`.")
    lines.append("This is not an emptiness claim: the exact row-negativity LP relaxation easily puts `5/4` mass on designated outside recipients, but exact geometry then makes those recipients visible (`H=0`), so the named binding constraint is exposedness/absorption rather than row-sum capacity.")
    lines.append("")
    lines.append("# W19 Worker A — Exact Feasibility Attack")
    lines.append("")
    lines.append("Tier legend: [T0] repo definition or banked exact pipeline; [T1] exact computation/assertion from printed rational matrices; [T2] structured non-realization read from these designs; [T3] heuristic interpretation.")
    lines.append("")
    lines.append("## Rerun")
    lines.append("")
    lines.append("```bash")
    lines.append("python3 runs/2026-07-06-w19-sigma-frontier/scripts/w19_worker_a.py")
    lines.append("```")
    lines.append("")
    lines.append("## Pipeline Calibration")
    lines.append("")
    for name, g in calibs:
        lines.append(f"- [T1] `{name}`: {summarize_geom(g)}.")
    lines.append("")
    lines.append("The first calibration is the banked F2 halo-nonrobust witness: raw invisible self-mass `5343/5000` but strict-halo `sigma_g=0`. The second is the banked rank-3 genuine-partner point, recomputed from its exact matrix.")
    lines.append("")
    lines.extend(section_for_matrix("Calibration matrix: sigma-halo nonrobust anchor", dict(calibs)["calibration_sigma_halo_nonrobust"], "raw self-mass can be huge, but here the strict-halo recipient set is empty."))

    lines.append("## Design 1 — Rank-3 Mass Splitting With Duplicate Outside Recipients")
    lines.append("")
    lines.append("Definition: `C_a=(1/2, 1/2+1/20, -1/20)` for all hidden recipients, `R2` has every hidden column equal to `rho`, and `q=m*rho` is the total hidden-column mass. For every hidden top row in the certified side, `sigma_g=q` because all hidden duplicate recipient columns lie at strict distance `> tau/4` from `conv W`.")
    lines.append("")
    lines.append("| m | rho | q=sigma_g | delta | H | W | hidden tops | binding |")
    lines.append("|---:|---:|---:|---:|---:|---|---|---|")
    for m, g in [(2, split2), (4, split4), (8, split8)]:
        rho = F(5, 84) / m
        lines.append(f"| {m} | {fstr(rho)} | {fstr(F(5,84))} | {fstr(g['delta'])} | {fstr(g['H'])} | {list(g['W'])} | {list(g['tops'])} | row-negativity scales with total `q`; splitting does not increase total hostable mass |")
    lines.append(f"| 2 | {fstr(F(1,32))} | attempted `1/16` | {fstr(split_fail['delta'])} | {fstr(split_fail['H'])} | {list(split_fail['W'])} | {list(split_fail['tops'])} | exposedness absorption: recipients enter W |")
    lines.append("")
    lines.append("- [T1] Certified side: `q=5/84`, `delta=1/16`, `H=1/10`, strict-halo recipients are exactly the hidden columns, and each hidden top has `sigma_g=5/84`.")
    lines.append("- [T2] Frontier read: increasing `q` from `5/84` to `1/16` does not hit the `delta<=1/4` cap; it flips the hidden recipients into `W`, making `H=0`. The active constraint is exposedness/absorption.")
    lines.extend(section_for_matrix("Best duplicate split point (m=4, q=5/84)", split4, "mass splitting across more recipient indices leaves total `sigma_g=q=5/84`; row negativity and exposedness depend on total q, not m."))
    lines.extend(section_for_matrix("Duplicate split absorption comparison (m=2, q=1/16)", split_fail, "raising total mass slightly makes the outside recipients visible, so there is no hidden top to count."))

    lines.append("## Design 2 — Rank-3 Distinct Genuine Partner Anchor")
    lines.append("")
    lines.append("- [T1] This banked exact point has two strict-halo recipients for the hidden top: self row 3 and distinct partner row 4. It is the best rank-3 distinct-recipient certificate in this report.")
    lines.extend(section_for_matrix("Rank-3 genuine-partner point", rank3_partner, "the distinct partner carries only `23/2000`; total `sigma_g=229/3200`, with row 3 negativity already close to the controlling budget."))

    lines.append("## Design 3 — Rank-5 One-Hidden Genuine Self Anchor")
    lines.append("")
    lines.append("- [T1] This is the largest certified strict-halo `sigma_g` in this worker report: `5991/80000`. The only strict-halo recipient is the hidden top itself.")
    lines.extend(section_for_matrix("Rank-5 genuine-self point", rank5, "self-mass can become genuine, but its amount is small once the row is kept hidden and outside the tau/4 halo."))

    lines.append("## Design 4 — Exact LP Relaxation Showing Why Optimization Alone Is Not Enough")
    lines.append("")
    lines.append("- [T1] Fixed rank-3 cycle design with three designated hidden recipients. Exact LP over free `R2` entries, with row negative masses constrained by `delta<=1/4` and designated coefficients constrained nonnegative, maximizes designated mass at `5/4`.")
    lines.append("- [T1] Exact geometry of the LP optimizer: " + summarize_geom(relaxed_g) + ".")
    lines.append("- [T2] Binding constraint: the optimizer's recipients become visible (`W=[3,4,5]`, `H=0`). Thus the missing condition is not coefficient capacity; it is keeping high-mass genuine recipients hidden/outside the exposed hull.")
    lines.append("")
    lines.append("Full exact LP optimizer matrix `P`:")
    lines.append("")
    lines.append("```python")
    lines.append(mat_str(relaxed_g["P"]))
    lines.append("```")
    lines.append("")

    lines.append("## Assert List")
    lines.append("")
    for msg in ASSERTS:
        lines.append(f"- [T1] {msg}")
    lines.append("")
    lines.append("## Verdict")
    lines.append("")
    lines.append("- [T2] `sigma_g > 1/2` was not realized here.")
    lines.append("- [T2] This is not an emptiness claim. The useful non-realization insight is that coefficient optimization has ample mass, but exact exposedness absorbs the high-mass recipients; in the certified hidden-top families, the frontier is instead controlled by exposedness/halo absorption and row-negativity scaling with total recipient mass.")
    return "\n".join(lines) + "\n"


def main() -> None:
    report = make_report()
    out = SCRATCH.parent / "data" / "worker-report.md"
    out.write_text(report)
    print(report)


if __name__ == "__main__":
    main()
