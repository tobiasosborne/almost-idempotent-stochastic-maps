#!/usr/bin/env python3
"""W23 Worker I: A-GAP route (ii), below-width-4 Lemma A.

This is a deliberately small exact-check script.  It does not claim a search
exhaustion result; it records the proof obstruction and the concrete exact
families tested against a = 15/4.
"""

from __future__ import annotations

from fractions import Fraction as F
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[3]
SCRATCH = Path(__file__).resolve().parents[1]
WEB = ROOT / "runs/2026-07-02-web-regime-hunt/scripts"
sys.path.insert(0, str(WEB))

import gen  # noqa: E402
import pipeline as pipe  # noqa: E402


A = F(15, 4)
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
    return "[\n  " + ",\n  ".join(
        "[" + ", ".join(f'"{fstr(x)}"' for x in row) + "]" for row in P
    ) + "\n]"


def pos(x: F) -> F:
    return x if x > 0 else F(0)


def neg_mass(row: list[F]) -> F:
    return sum(pos(-x) for x in row)


def build_from_lambdac(C: list[list[F]], R2: list[list[F]]) -> list[list[F]]:
    P, _R, _C = gen.build_from_LambdaC(C, R2)
    return P


def hume(s: F) -> list[list[F]]:
    """The sharp rank-one family from ex-hume."""
    v = [F(1), -F(1) + s, -s]
    u = [F(1) - s + s * s, -s, F(0)]
    P: list[list[F]] = []
    for i in range(3):
        P.append([(F(1) if i == j else F(0)) - u[i] * v[j] for j in range(3)])
    return P


def rank3_partner() -> list[list[F]]:
    C = [[F(1, 2), F(-1, 20), F(11, 20)], [F(257, 400), F(-7, 200), F(157, 400)]]
    R2 = [[F(9, 200), F(1, 80)], [F(1, 200), F(1, 200)], [F(11, 160), F(1, 100)]]
    return build_from_lambdac(C, R2)


def rank5_genuine_self() -> list[list[F]]:
    C = [[F(-3, 80), F(23, 400), F(5, 12), F(-1, 200), F(341, 600)]]
    R2 = [[F(3, 80)], [F(1, 100)], [F(1, 16)], [F(1, 96)], [F(7, 80)]]
    return build_from_lambdac(C, R2)


def duplicate_split(m: int, q: F = F(5, 84)) -> list[list[F]]:
    p = F(1, 20)
    rho = q / m
    c = [F(1, 2), F(1, 2) + p, -p]
    C = [c[:] for _ in range(m)]
    R2 = [[rho for _ in range(m)] for _ in range(3)]
    return build_from_lambdac(C, R2)


def shallow_corner_ansatz(T: int = 1000, m: F = F(1, 2), c: F = F(19, 10)) -> tuple[list[list[F]], F]:
    """A failed exact ansatz for constant shell mass.

    In coordinate space, rows 3 and 4 sit on opposite sides of the e0 corner;
    row 0 puts total mass m on them and pays only a formal target negative
    correction delta0.  Exact analysis shows the actual negative mass inflates.
    """
    tau0 = F(1, T)
    delta0 = tau0 * tau0
    eta = 2 * delta0 / m
    s = c * tau0
    lam = [
        [F(1), F(0), F(0)],
        [F(0), F(1), F(0)],
        [F(0), F(0), F(1)],
        [F(1), -s, s],
        [F(1), s + eta, -s - eta],
    ]
    r0 = [1 - m, -delta0, delta0, m / 2, m / 2]
    r1 = [F(0), F(1), F(0), F(0), F(0)]
    r2 = [F(0), F(0), F(1), F(0), F(0)]
    R = [r0, r1, r2]
    hard_assert(pipe.matmul(R, lam) == [[F(1), F(0), F(0)], [F(0), F(1), F(0)], [F(0), F(0), F(1)]],
                "shallow-corner ansatz: R Lambda = I_3 exactly")
    return pipe.matmul(lam, R), delta0


def exact_geometry(P: list[list[F]], label: str) -> dict:
    P = pipe.as_F(P)
    ok, idem, rowsum = pipe.is_idempotent(P)
    hard_assert(ok and idem and rowsum, f"{label}: P^2=P and P1=1 exactly")
    delta, negs = pipe.delta(P)
    hard_assert(F(0) < delta <= F(1, 4), f"{label}: 0 < delta <= 1/4")
    W, info = pipe.visible_set(P, delta)
    hard_assert(bool(W), f"{label}: W(P) is nonempty")
    dists = [pipe.dist1_to_conv(P, W, i)[0] for i in range(len(P))]
    hard_assert(all(d is not None for d in dists), f"{label}: all distances to C_W computed exactly")
    H = max(dists)
    G = [j for j, d in enumerate(dists) if d * d > A * A * delta]
    g_by_w = {w: sum(P[w][j] for j in G) for w in W}
    shell_by_w = {
        w: [
            j for j, d in enumerate(dists)
            if d * d > A * A * delta and pipe.l1(P[j], P[w]) * pipe.l1(P[j], P[w]) < 16 * delta
        ]
        for w in W
    }
    return {
        "label": label,
        "P": P,
        "delta": delta,
        "negs": negs,
        "W": W,
        "info": info,
        "dists": dists,
        "H": H,
        "G": G,
        "g_by_w": g_by_w,
        "shell_by_w": shell_by_w,
    }


def ratio_sq(x: F, delta: F) -> str:
    return fstr((x * x) / delta)


def case_summary(g: dict) -> list[str]:
    delta = g["delta"]
    lines = [
        f"### {g['label']}",
        "",
        f"- [T1] delta = `{fstr(delta)}`; W = `{g['W']}`; H^2/delta = `{ratio_sq(g['H'], delta)}`.",
        f"- [T1] G_15/4 = `{g['G']}`; visible-row g-values = "
        + "`" + str({w: fstr(v) for w, v in g["g_by_w"].items()}) + "`.",
        f"- [T1] row negative masses = `{[fstr(x) for x in g['negs']]}`.",
        f"- [T1] dist(row,C_W)^2/delta = `{[ratio_sq(d, delta) for d in g['dists']]}`.",
    ]
    if any(g["shell_by_w"].values()):
        lines.append(f"- [T1] shell indices by visible row = `{g['shell_by_w']}`.")
    lines += [
        "",
        "Matrix:",
        "",
        "```python",
        mat_str(g["P"]),
        "```",
        "",
    ]
    return lines


def make_report() -> str:
    cases: list[dict] = []
    cases.append(exact_geometry(hume(F(1, 100)), "sharp Hume family s=1/100"))
    cases.append(exact_geometry(rank3_partner(), "W19 rank-3 genuine-partner anchor"))
    cases.append(exact_geometry(rank5_genuine_self(), "W19 rank-5 genuine-self anchor"))
    cases.append(exact_geometry(duplicate_split(4), "W19 duplicate-split m=4, q=5/84"))
    shallow_P, formal_delta = shallow_corner_ansatz()
    shallow = exact_geometry(shallow_P, "failed shallow-corner constant-mass ansatz")
    cases.append(shallow)

    hard_assert(all(g["G"] == [] for g in cases[:4]), "banked exact families tested here have empty G_15/4")
    hard_assert(shallow["delta"] > 100 * formal_delta,
                "shallow-corner ansatz: actual delta inflates by more than 100x over the formal target")
    hard_assert(shallow["G"] == [], "shallow-corner ansatz: G_15/4 is empty after exact visibility analysis")

    lines: list[str] = []
    lines.append(
        "OPEN-BOTH-SIDES (prove blocked at: shell S_w inside rho where the visible exposer has no lower bound; "
        "refute frontier: no exact family here enters G_{15/4}, and the shallow-corner ansatz is blocked by "
        "delta-inflation/exposedness absorption)"
    )
    lines.append("")
    lines.append("# W23 Worker I - A-GAP Route (ii)")
    lines.append("")
    lines.append("Tier legend: [T0] repo definition or established shard; [T1] exact computation by this script; [T2] proof-analysis consequence; [T3] heuristic frontier read.")
    lines.append("")
    lines.append("## Established imports")
    lines.append("")
    lines.append("- [T0] `def-visible-set`: tau = sqrt(delta), rho = 4 tau, kappa = tau/4; W is the set of (rho,kappa)-exposed row vertices.")
    lines.append("- [T0] `def-exposed`: an admissible exposer only has a guaranteed lower margin on rows with l1-distance at least rho from the vertex; rows inside the rho-ball are exempt.")
    lines.append("- [T0] `lem-visible-g-small`: for a >= 4, visible rows satisfy `-nu_w <= g_w <= 4*tau`; the only use of a >= 4 is `G_a subset {||p_j-p_w||_1 >= rho}`.")
    lines.append("- [T0] `obs-height-collapse` and `conj-halo-collapse` are af-validated hidden-top outgoing-mass inequalities; their hypotheses are about a hidden top vertex v and the row v, not incoming mass `P_wj` from a visible row.")
    lines.append("")
    lines.append("## Prove-side attempt")
    lines.append("")
    lines.append("- [T2] For a in (29/8,4), any uncontrolled index for a visible w lies in the annulus `a*tau < ||p_j-p_w||_1 < 4*tau`. The first inequality is just `p_w in C_W`; the second is the definition of the below-rho shell.")
    lines.append("- [T2] The original exposer pairing cannot price this annulus. Visibility gives an affine h with `h(p_j) >= kappa` only for rows at distance at least `rho = 4*tau`; the definition gives no positive lower bound for shell rows.")
    lines.append("- [T2] Pairing the exposer of w against the reproduction identity of a shell row j controls, at best, how row j sends mass to rho-far rows. It gives no reciprocal or column estimate for the incoming coefficient `P_wj`.")
    lines.append("- [T2] The af-validated height-collapse tools do not apply to an arbitrary shell index. If the shell row is non-vertex, it is outside their hypotheses; if it is a hidden vertex but not top, it is still outside their hypotheses; if a hidden top exists, the conclusions concern that top row's own positive mass split, not visible-row load on the shell.")
    lines.append("- [T2] The generic convex-distance residual bound is one-sided in the wrong direction for this task: signed reproduction can make the positive barycenter close to `C_W` while individual positive recipients lie outside `C_W`. Without a common separator for the whole shell, it does not yield `sum_{j in S_w} P_wj^+ = O(tau)`.")
    lines.append("")
    lines.append("Conclusion of the proof attempt: I do not have a valid below-4 proof. The missing estimate is exactly an incoming shell-mass cap")
    lines.append("`sum_{j: dist(p_j,C_W)>a*tau, ||p_j-p_w||_1<4*tau} P_wj^+ <= C(a)*tau` for visible w.")
    lines.append("")
    lines.append("## Refute-side exact checks")
    lines.append("")
    lines.append("Rerun:")
    lines.append("")
    lines.append("```bash")
    lines.append("python3 runs/2026-07-06-w23-a-gap/scripts/w23_worker_i.py")
    lines.append("```")
    lines.append("")
    for g in cases:
        lines.extend(case_summary(g))
    lines.append("## Refute-side read")
    lines.append("")
    lines.append("- [T1] The sharp rank-one family, the W19 rank-3/rank-5 anchors, and the duplicate-split family all have `G_{15/4} = empty` under exact visibility and exact l1-distance predicates.")
    lines.append("- [T1] The shallow-corner ansatz realizes the desired formal row-0 pattern (constant mass on two near outside coordinate points with only a formal O(delta) correction), but exact row negativity inflates from the target `1/1000000` to `" + fstr(shallow["delta"]) + "`, and exact visibility makes `G_{15/4}` empty.")
    lines.append("- [T2] This identifies the binding refuter constraints: keep actual negative mass at O(epsilon^2), keep row distances to `C_W` at O(epsilon) in the band `(15/4,4)*tau`, and keep the recipient rows out of W while row w places non-O(tau) mass on them.")
    lines.append("- [T3] I did not obtain a counterexample or a degradation certificate. This is not an emptiness claim.")
    lines.append("")
    lines.append("## Assert list")
    lines.append("")
    for msg in ASSERTS:
        lines.append(f"- [T1] {msg}")
    lines.append("")
    return "\n".join(lines) + "\n"


def main() -> None:
    report = make_report()
    out = SCRATCH / "data/worker-i-report.md"
    out.write_text(report)
    print(report)


if __name__ == "__main__":
    main()
