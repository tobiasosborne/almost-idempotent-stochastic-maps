#!/usr/bin/env python3
"""W21 Worker D: exact REFUTE-side certificates for Lemma A.

The script recomputes every reported quantity over Q.  Irrational comparisons
with tau=sqrt(delta) use squared rational inequalities.
"""

from __future__ import annotations

import math
import sys
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WEB = ROOT / "runs/2026-07-02-web-regime-hunt/scripts"
sys.path.insert(0, str(WEB))

import gen  # noqa: E402
import pipeline as pipe  # noqa: E402


A_VALUES = (F(1, 4), F(1), F(2), F(4), F(5), F(6))
ASSERTS: list[str] = []


def hard_assert(cond: bool, msg: str) -> None:
    if not cond:
        raise AssertionError(msg)
    ASSERTS.append(msg)


def fstr(x: F | None) -> str:
    if x is None:
        return "None"
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def ratio_float(num: F, delta: F) -> float:
    return float(num) / math.sqrt(float(delta)) if delta else 0.0


def ksq(num: F, delta: F) -> F:
    return (num * num) / delta if delta else F(0)


def mat_str(P: list[list[F]]) -> str:
    rows = []
    for row in P:
        rows.append("[" + ", ".join(f'"{fstr(x)}"' for x in row) + "]")
    return "[\n  " + ",\n  ".join(rows) + "\n]"


def pos(x: F) -> F:
    return x if x > 0 else F(0)


@dataclass(frozen=True)
class HaloBest:
    a: F
    G: tuple[int, ...]
    w: int | None
    g: F
    far_pos: F


def rank5_scaled(lam: F) -> list[list[F]]:
    """Scaled version of the banked rank-5 genuine-self geometry."""
    C = [[F(-3, 80), F(23, 400), F(5, 12), F(-1, 200), F(341, 600)]]
    base_R2 = [[F(3, 80)], [F(1, 100)], [F(1, 16)], [F(1, 96)], [F(7, 80)]]
    R2 = [[lam * row[0]] for row in base_R2]
    P, _R, _C = gen.build_from_LambdaC(C, R2)
    return P


def analyze_matrix(P: list[list[F]], label: str) -> dict:
    P = pipe.as_F(P)
    ok, idem, rowsum = pipe.is_idempotent(P)
    hard_assert(ok and idem and rowsum, f"{label}: P^2=P and every row sum is 1")

    delta, negs = pipe.delta(P)
    hard_assert(delta > 0, f"{label}: delta(P)>0")
    hard_assert(delta <= F(1, 4), f"{label}: delta(P)<=1/4")

    W, info = pipe.visible_set(P, delta)
    hard_assert(bool(W), f"{label}: W(P) is nonempty")
    for w in W:
        hard_assert(info[w]["vertex"] and info[w]["exposed"], f"{label}: row {w} is visible")

    dists: list[F] = []
    lambdas: list[list[F] | None] = []
    for i in range(len(P)):
        dist, lam = pipe.dist1_to_conv(P, W, i)
        hard_assert(dist is not None, f"{label}: dist_1(row {i}, conv W) is LP-certified")
        dists.append(dist)
        lambdas.append(lam)

    best_by_a: dict[F, HaloBest] = {}
    for a in A_VALUES:
        G = tuple(j for j, dist in enumerate(dists) if dist > 0 and dist * dist > a * a * delta)
        if not G:
            best_by_a[a] = HaloBest(a=a, G=G, w=None, g=F(0), far_pos=F(0))
            continue
        vals = []
        for w in W:
            g = sum(P[w][j] for j in G)
            far_pos = sum(pos(P[w][j]) for j in G)
            vals.append((g, far_pos, w))
            if a >= 4 and g > 0:
                hard_assert(g * g <= 16 * delta, f"{label}: visible row {w} has g<=4*tau at a={fstr(a)}")
        g, far_pos, w = max(vals, key=lambda item: (item[0], item[1], -item[2]))
        best_by_a[a] = HaloBest(a=a, G=G, w=w, g=g, far_pos=far_pos)

    return {
        "label": label,
        "P": P,
        "n": len(P),
        "delta": delta,
        "negs": tuple(negs),
        "W": tuple(W),
        "info": info,
        "dists": tuple(dists),
        "lambdas": tuple(lambdas),
        "H": max(dists),
        "best_by_a": best_by_a,
    }


def tstar_table(info: dict) -> dict[int, str]:
    out: dict[int, str] = {}
    for i, row in info.items():
        if row.get("vertex"):
            out[i] = "inf" if row.get("tstar") is None else fstr(row.get("tstar"))
    return out


def summarize(g: dict) -> str:
    return (
        f"delta={fstr(g['delta'])}; W={list(g['W'])}; H={fstr(g['H'])}; "
        f"dists={[fstr(x) for x in g['dists']]}; negs={[fstr(x) for x in g['negs']]}; "
        f"tstars={tstar_table(g['info'])}"
    )


def table_row(a: F, rec: dict, best: HaloBest) -> str:
    if best.w is None:
        return (
            f"| {fstr(a)} | `{rec['label']}` | {list(best.G)} | - | 0 | 0 | 0.000000 | 0 |"
        )
    return (
        f"| {fstr(a)} | `{rec['label']}` | {list(best.G)} | {best.w} | "
        f"{fstr(best.g)} | {fstr(ksq(best.g, rec['delta']))} | "
        f"{ratio_float(best.g, rec['delta']):.6f} | {fstr(best.far_pos)} |"
    )


def make_report() -> str:
    frontier = analyze_matrix(rank5_scaled(F(7, 5)), "scaled-rank5-lambda-7/5")
    absorption = analyze_matrix(rank5_scaled(F(29, 20)), "scaled-rank5-lambda-29/20-absorption")

    b14 = frontier["best_by_a"][F(1, 4)]
    hard_assert(frontier["delta"] == F(27881, 480000), "frontier: delta=27881/480000")
    hard_assert(frontier["W"] == (0, 1, 2, 3, 4), "frontier: W=(0,1,2,3,4)")
    hard_assert(frontier["dists"][5] == F(20760213, 244997300), "frontier: exact d_5 value")
    hard_assert(b14.G == (5,), "frontier: G_{1/4}={5}")
    hard_assert(b14.w == 4, "frontier: best visible row at a=1/4 is w=4")
    hard_assert(b14.g == F(49, 400), "frontier: g^{(1/4)}_4=49/400")
    hard_assert(b14.far_pos == F(49, 400), "frontier: positive far-mass equals 49/400")
    hard_assert(frontier["dists"][5] * frontier["dists"][5] <= frontier["delta"], "frontier: d_5<=tau, so G_a is empty for a>=1")
    for a in (F(1), F(2), F(4), F(5), F(6)):
        hard_assert(frontier["best_by_a"][a].G == (), f"frontier: G_{fstr(a)} is empty")

    hard_assert(absorption["delta"] == F(115507, 1920000), "absorption: delta=115507/1920000")
    hard_assert(absorption["W"] == (0, 1, 2, 3, 4, 5), "absorption: row 5 is absorbed into W")
    hard_assert(absorption["H"] == 0, "absorption: H=0 after row 5 becomes visible")
    for a in A_VALUES:
        hard_assert(absorption["best_by_a"][a].G == (), f"absorption: G_{fstr(a)} is empty")

    records = [frontier, absorption]
    best_frontier: dict[F, tuple[dict, HaloBest]] = {}
    for a in A_VALUES:
        best_frontier[a] = max(
            ((rec, rec["best_by_a"][a]) for rec in records),
            key=lambda item: (ksq(item[1].g, item[0]["delta"]), item[1].g),
        )

    large_best = max(best_frontier[a][1].g for a in (F(4), F(5), F(6)))
    small = best_frontier[F(1, 4)]

    lines: list[str] = []
    lines.append(
        "NOT-REFUTED-FRONTIER (sup g_w/tau = 0 on the certified a>=4 frontier; "
        f"small-a frontier: a=1/4, K^2={fstr(ksq(small[1].g, small[0]['delta']))}, "
        f"K={ratio_float(small[1].g, small[0]['delta']):.6f})"
    )
    lines.append("")
    lines.append("# W21 Worker D -- Lemma A REFUTE-side exact report")
    lines.append("")
    lines.append("Tier legend: [T0] repo definition or banked exact pipeline; [T1] exact computation hard-asserted by this script; [T2] structured read from these certificates; [T3] heuristic/search intuition.")
    lines.append("")
    lines.append("## Verdict")
    lines.append("")
    lines.append("- [T1] No certified refutation was realized for Lemma A at `a in {4,5,6}`: the certified frontier has `G_a=empty` and hence `sup_{w in W} g_w/tau=0` for those widths.")
    lines.append(f"- [T1] The best small-halo certificate is `a=1/4`, `w=4`, `G={{5}}`, `g=49/400`, `delta=27881/480000`, so `K^2={fstr(ksq(small[1].g, small[0]['delta']))}` and `K={ratio_float(small[1].g, small[0]['delta']):.6f}`.")
    lines.append("- [T2] Binding constraint named: exposedness absorption. In the same one-parameter rank-5 geometry, increasing the tail scale from `lambda=7/5` to `lambda=29/20` makes row 5 visible, so `C_W` absorbs it and every halo set becomes empty.")
    lines.append("- [T2] This is not an emptiness theorem. It is a deterministic exact frontier for the constructions certified here, plus an absorption comparison explaining why the attempted high-mass continuation fails.")
    lines.append("")
    lines.append("## Exact Frontier Table")
    lines.append("")
    lines.append("| a | certificate | G_a | best visible w | g_w | K^2=g_w^2/delta | K=g_w/tau | positive far-mass |")
    lines.append("|---:|---|---|---:|---:|---:|---:|---:|")
    for a in A_VALUES:
        rec, best = best_frontier[a]
        lines.append(table_row(a, rec, best))
    lines.append("")
    lines.append("## Certified Instances")
    lines.append("")
    for rec in records:
        lines.append(f"### {rec['label']}")
        lines.append("")
        lines.append(f"- [T1] `{summarize(rec)}`.")
        for a in A_VALUES:
            best = rec["best_by_a"][a]
            if best.w is None:
                lines.append(f"- [T1] `a={fstr(a)}`: `G_a={list(best.G)}`, best visible `g=0`.")
            else:
                lines.append(
                    f"- [T1] `a={fstr(a)}`: `G_a={list(best.G)}`, best visible row `w={best.w}`, "
                    f"`g={fstr(best.g)}`, `K^2={fstr(ksq(best.g, rec['delta']))}`, "
                    f"`K={ratio_float(best.g, rec['delta']):.6f}`, positive far-mass `{fstr(best.far_pos)}`."
                )
        lines.append("")
        lines.append("Full exact matrix `P`:")
        lines.append("")
        lines.append("```python")
        lines.append(mat_str(rec["P"]))
        lines.append("```")
        lines.append("")
    lines.append("## Large-Halo Obstruction Read")
    lines.append("")
    lines.append("- [T2] For `a>=4`, any `j in G_a` is `rho`-far from every visible `w`, because `p_w in C_W` and `dist_1(p_j,p_w) >= dist_1(p_j,C_W) > a*tau >= 4*tau = rho`.")
    lines.append("- [T2] Thus the intended `delta/kappa=4*tau` exposedness cancellation barrier is exactly the active mechanism to beat. The certified constructions here did not even enter that large-halo regime; before the tail can be enlarged, the recipient is absorbed into `W`.")
    lines.append(f"- [T1] Hard-asserted large-width certified value: `max_{{a in {{4,5,6}}, w in W}} g_w = {fstr(large_best)}` on these matrices.")
    lines.append("")
    lines.append("## Hard Assert List")
    lines.append("")
    for msg in ASSERTS:
        lines.append(f"- [T1] {msg}")
    return "\n".join(lines) + "\n"


def main() -> None:
    report = make_report()
    out = Path(__file__).resolve().parents[1] / "data" / "worker-d-report.md"
    out.write_text(report)
    print(report)


if __name__ == "__main__":
    main()
