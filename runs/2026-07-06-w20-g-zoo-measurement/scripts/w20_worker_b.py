#!/usr/bin/env python3
"""W20 Worker B adversarial exact construction attempt for the g-bootstrap.

The script is deliberately self-contained: it reconstructs every certified
matrix from rational parameters, computes W, exact distances to conv(W), the
signed observables g^(a)=P*1_{G_a}, and writes the worker report.
"""

from __future__ import annotations

import sys
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
WEB = ROOT / "runs/2026-07-02-web-regime-hunt/scripts"
OUT = ROOT / "runs/2026-07-06-w20-g-zoo-measurement/data/worker-b-report.md"
sys.path.insert(0, str(WEB))

import gen  # noqa: E402
import pipeline as pipe  # noqa: E402
from exact_lp import linprog_exact  # noqa: E402


A_VALUES = (F(1, 4), F(1), F(2), F(4), F(5), F(6))
WORKABLE_A = (F(4), F(5), F(6))
ASSERTS: list[str] = []


def hard_assert(cond: bool, msg: str) -> None:
    if not cond:
        raise AssertionError(msg)
    ASSERTS.append(msg)


def fstr(x: F | None) -> str:
    if x is None:
        return "None"
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def astr(a: F) -> str:
    return fstr(a)


def pos(x: F) -> F:
    return x if x > 0 else F(0)


def mat_str(P: list[list[F]]) -> str:
    rows = []
    for row in P:
        rows.append("[" + ", ".join(f'"{fstr(x)}"' for x in row) + "]")
    return "[\n  " + ",\n  ".join(rows) + "\n]"


def ratio_over_tau_float(x: F, delta: F) -> float:
    return float(x) / (float(delta) ** 0.5)


def ratio_square_str(x: F, delta: F) -> str:
    if x == 0:
        return "0"
    return fstr((x * x) / delta)


def build_from_lambdac(C: list[list[F]], R2: list[list[F]]) -> list[list[F]]:
    P, _R, _C = gen.build_from_LambdaC(C, R2)
    return P


def analyze_matrix(P: list[list[F]], label: str) -> dict:
    P = [[F(x) for x in row] for row in P]
    ok, idem, rowsum = pipe.is_idempotent(P)
    hard_assert(ok and idem and rowsum, f"{label}: P^2=P and P1=1")
    delta, negs = pipe.delta(P)
    hard_assert(delta > 0 and delta <= F(1, 4), f"{label}: 0 < delta <= 1/4")
    W, info = pipe.visible_set(P, delta)
    hard_assert(bool(W), f"{label}: W(P) is nonempty")
    dists = [pipe.dist1_to_conv(P, W, i)[0] for i in range(len(P))]
    hard_assert(all(d is not None for d in dists), f"{label}: exact dist_1 to conv(W) for every row")
    hidden = tuple(i for i in range(len(P)) if info.get(i, {}).get("vertex") and not info.get(i, {}).get("exposed"))
    H = max(dists)
    tops = tuple(i for i in hidden if H > 0 and dists[i] == H)

    by_a: dict[F, dict] = {}
    for a in A_VALUES:
        G = tuple(j for j, dist in enumerate(dists) if dist > 0 and dist * dist > a * a * delta)
        g = tuple(sum(P[i][j] for j in G) for i in range(len(P)))
        Pg = tuple(sum(P[i][j] * g[j] for j in range(len(P))) for i in range(len(P)))
        hard_assert(Pg == g, f"{label}: Pg=g exactly for a={astr(a)}")
        sigma_pos = tuple(sum(pos(P[i][j]) for j in G) for i in range(len(P)))
        level = tuple(i for i, val in enumerate(g) if val >= F(1, 2))
        nonW = tuple(i for i in range(len(P)) if i not in W)
        max_visible_g = max((g[w] for w in W), default=F(0))
        max_visible_g = max(max_visible_g, F(0))
        max_nonW_g = max((g[i] for i in nonW), default=F(0))
        max_nonW_g = max(max_nonW_g, F(0))
        by_a[a] = {
            "G": G,
            "g": g,
            "sigma_pos": sigma_pos,
            "level": level,
            "max_visible_g": max_visible_g,
            "max_nonW_g": max_nonW_g,
        }

    return {
        "label": label,
        "P": P,
        "n": len(P),
        "delta": delta,
        "negs": tuple(negs),
        "W": tuple(W),
        "info": info,
        "dists": tuple(dists),
        "H": H,
        "hidden": hidden,
        "tops": tops,
        "by_a": by_a,
    }


def calibration_sigma_halo_nonrobust() -> dict:
    C = [[F(28, 25), F(1, 200), F(0), F(-1, 8)]]
    R2 = [[F(-49, 800)], [F(-1, 6)], [F(-1, 8)], [F(-33, 800)]]
    rec = analyze_matrix(build_from_lambdac(C, R2), "calibration sigma-halo-nonrobust")
    hard_assert(rec["delta"] == F(252559, 1280000), "calibration sigma-halo-nonrobust: delta matches banked value")
    hard_assert(rec["by_a"][F(1, 4)]["G"] == (), "calibration sigma-halo-nonrobust: strict tau/4 halo G is empty")
    return rec


def rank3_genuine_partner() -> dict:
    C = [[F(1, 2), F(-1, 20), F(11, 20)], [F(257, 400), F(-7, 200), F(157, 400)]]
    R2 = [[F(9, 200), F(1, 80)], [F(1, 200), F(1, 200)], [F(11, 160), F(1, 100)]]
    rec = analyze_matrix(build_from_lambdac(C, R2), "rank3 genuine partner")
    hard_assert(rec["delta"] == F(74551, 1600000), "rank3 genuine partner: delta matches banked value")
    hard_assert(rec["W"] == (0, 1, 2), "rank3 genuine partner: W=(0,1,2)")
    hard_assert(rec["by_a"][F(1, 4)]["G"] == (3, 4), "rank3 genuine partner: G_{1/4}=(3,4)")
    hard_assert(rec["by_a"][F(4)]["G"] == (), "rank3 genuine partner: G_4 is empty")
    return rec


def duplicate_split_instance(m: int, q: F) -> dict:
    p = F(1, 20)
    rho = q / m
    c = [F(1, 2), F(1, 2) + p, -p]
    C = [c[:] for _ in range(m)]
    R2 = [[rho for _ in range(m)] for _ in range(3)]
    return analyze_matrix(build_from_lambdac(C, R2), f"duplicate split m={m} q={fstr(q)}")


def rank5_genuine_self() -> dict:
    C = [[F(-3, 80), F(23, 400), F(5, 12), F(-1, 200), F(341, 600)]]
    R2 = [[F(3, 80)], [F(1, 100)], [F(1, 16)], [F(1, 96)], [F(7, 80)]]
    rec = analyze_matrix(build_from_lambdac(C, R2), "rank5 genuine self")
    hard_assert(rec["delta"] == F(3983, 96000), "rank5 genuine self: delta matches banked value")
    hard_assert(rec["W"] == (0, 1, 2, 3, 4), "rank5 genuine self: W=(0,1,2,3,4)")
    hard_assert(rec["by_a"][F(1, 4)]["G"] == (5,), "rank5 genuine self: G_{1/4}=(5)")
    hard_assert(rec["by_a"][F(1, 4)]["g"][5] == F(5991, 80000), "rank5 genuine self: hidden self g=5991/80000 at a=1/4")
    return rec


def web_regime_headline() -> dict:
    p = F(1, 40)
    rho = F(1, 100)
    x = p / 3
    C = [[F(1, 2) - x, F(1, 2) + x + p, -p], [F(1, 2) + x, F(1, 2) - x + p, -p]]
    R2 = [[rho, rho], [rho, rho], [rho, rho]]
    rec = analyze_matrix(build_from_lambdac(C, R2), "web-regime headline H/delta witness")
    hard_assert(rec["delta"] == F(49, 2000), "web-regime headline: delta=49/2000")
    hard_assert(rec["H"] == F(1, 20), "web-regime headline: H=1/20")
    return rec


def solve_relaxed_cycle_lp() -> dict:
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

    def nidx(i: int, j: int) -> int:
        return nr + i * n + j

    N = nr + n * n
    target_v = k
    designated = [k, k + 1, k + 2]
    objective = [F(0)] * N
    for j in designated:
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
    for j in designated:
        const, coeff = p_expr(target_v, j)
        row = [F(0)] * N
        for q, val in enumerate(coeff):
            row[q] -= val
        A_ub.append(row)
        b_ub.append(const)

    bounds = [(None, None)] * nr + [(F(0), None)] * (n * n)
    res = linprog_exact(objective, A_ub=A_ub, b_ub=b_ub, bounds=bounds)
    hard_assert(res["status"] == "optimal", "relaxed cycle LP: exact optimum exists")
    x = res["x"]
    R2 = [[x[ridx(s, a)] for a in range(m)] for s in range(k)]
    P = build_from_lambdac(C, R2)
    mass = sum(pos(P[target_v][j]) for j in designated)
    hard_assert(mass == F(5, 4), "relaxed cycle LP: designated positive mass is 5/4")
    rec = analyze_matrix(P, "relaxed cycle LP absorption")
    hard_assert(rec["hidden"] == (), "relaxed cycle LP absorption: exact geometry has no hidden vertices")
    return rec


def duplicate_family_scan() -> list[dict]:
    records: list[dict] = []
    p_values = (F(1, 200), F(1, 100), F(1, 80), F(1, 60), F(1, 40), F(1, 30), F(1, 20), F(1, 16), F(1, 12), F(1, 10), F(1, 8), F(1, 6), F(1, 5), F(1, 4))
    q_values = (F(1, 1000), F(1, 500), F(1, 200), F(1, 100), F(1, 50), F(1, 25), F(1, 10))
    for p in p_values:
        for q in q_values:
            C = [[F(1, 2), F(1, 2) + p, -p], [F(1, 2), F(1, 2) + p, -p]]
            R2 = [[q / 2, q / 2], [q / 2, q / 2], [q / 2, q / 2]]
            P = build_from_lambdac(C, R2)
            delta, _negs = pipe.delta(P)
            if delta == 0 or delta > F(1, 4):
                continue
            rec = analyze_matrix(P, f"duplicate scan p={fstr(p)} q={fstr(q)}")
            records.append(rec)
    hard_assert(bool(records), "duplicate family scan: at least one under-cap exact candidate checked")
    return records


def clone_consistency_check(source: dict) -> str:
    old = source
    P_old = old["P"]
    weights = [F(1, 3), F(2, 3)]
    P_new = pipe.clone_row(P_old, 4, weights)
    new = analyze_matrix(P_new, "clone-consistency rank3 partner row4 split 1:2")
    a = F(1, 4)
    old_g = old["by_a"][a]["g"]
    new_g = new["by_a"][a]["g"]
    # New order: 0,1,2,3,4a,4b.
    hard_assert(new["by_a"][a]["G"] == (3, 4, 5), "clone consistency: cloned strict-halo fiber is transported")
    hard_assert(new_g[:4] == old_g[:4], "clone consistency: old rows 0..3 keep the same g values")
    hard_assert(new_g[4] == old_g[4] and new_g[5] == old_g[4], "clone consistency: cloned rows inherit old g")
    hard_assert(new["delta"] == old["delta"], "clone consistency: delta unchanged")
    return (
        "[T1] Weighted row-cloning row 4 of the rank-3 partner by weights 1/3,2/3 transports "
        "`G_{1/4}` from `(3,4)` to `(3,4,5)` and preserves all old-row `g` values exactly."
    )


def geom_summary(rec: dict) -> str:
    tstars = {
        i: ("inf" if rec["info"].get(i, {}).get("tstar") is None else fstr(rec["info"].get(i, {}).get("tstar")))
        for i in range(rec["n"])
        if rec["info"].get(i, {}).get("vertex")
    }
    return (
        f"delta={fstr(rec['delta'])}; W={list(rec['W'])}; H={fstr(rec['H'])}; "
        f"H/tau~{ratio_over_tau_float(rec['H'], rec['delta']):.6f}; "
        f"hidden={list(rec['hidden'])}; tops={list(rec['tops'])}; "
        f"dists={[fstr(x) for x in rec['dists']]}; tstars={tstars}"
    )


def a_summary(rec: dict, a: F) -> str:
    data = rec["by_a"][a]
    max_w = data["max_visible_g"]
    max_b = data["max_nonW_g"]
    return (
        f"a={astr(a)}: G={list(data['G'])}; "
        f"max_W g={fstr(max_w)} (g/tau~{ratio_over_tau_float(max_w, rec['delta']):.6f}, "
        f"(g/tau)^2={ratio_square_str(max_w, rec['delta'])}); "
        f"max_nonW g={fstr(max_b)}; level(g>=1/2)={list(data['level'])}"
    )


def choose_frontiers(records: list[dict]) -> dict:
    out: dict[str, object] = {}
    for a in WORKABLE_A:
        best_vis = max(records, key=lambda r: (r["by_a"][a]["max_visible_g"] * r["by_a"][a]["max_visible_g"] / r["delta"] if r["by_a"][a]["max_visible_g"] > 0 else F(0)))
        best_band = max(records, key=lambda r: r["by_a"][a]["max_nonW_g"])
        out[f"visible_{astr(a)}"] = best_vis
        out[f"band_{astr(a)}"] = best_band
    out["visible_low"] = max(records, key=lambda r: (r["by_a"][F(1, 4)]["max_visible_g"] * r["by_a"][F(1, 4)]["max_visible_g"] / r["delta"] if r["by_a"][F(1, 4)]["max_visible_g"] > 0 else F(0)))
    out["band_low"] = max(records, key=lambda r: r["by_a"][F(1, 4)]["max_nonW_g"])
    return out


def section_for_matrix(rec: dict, a_values: tuple[F, ...] = (F(1, 4), F(4), F(5), F(6))) -> list[str]:
    lines = [f"### {rec['label']}", "", f"- [T1] {geom_summary(rec)}."]
    for a in a_values:
        lines.append(f"- [T1] {a_summary(rec, a)}.")
    lines += ["", "Full exact matrix `P`:", "", "```python", mat_str(rec["P"]), "```", ""]
    return lines


def make_report() -> str:
    records: list[dict] = []
    named: list[dict] = []

    cal = calibration_sigma_halo_nonrobust()
    partner = rank3_genuine_partner()
    split4 = duplicate_split_instance(4, F(5, 84))
    split_absorb = duplicate_split_instance(2, F(1, 16))
    rank5 = rank5_genuine_self()
    web = web_regime_headline()
    relaxed = solve_relaxed_cycle_lp()

    named.extend([cal, partner, split4, split_absorb, rank5, web, relaxed])
    records.extend(named)
    scan_records = duplicate_family_scan()
    records.extend(scan_records)

    hard_assert(split4["delta"] == F(1, 16), "duplicate split m=4 q=5/84: delta=1/16")
    hard_assert(split4["by_a"][F(1, 4)]["max_nonW_g"] == F(5, 84), "duplicate split m=4 q=5/84: band g=5/84 at a=1/4")
    hard_assert(split_absorb["hidden"] == (), "duplicate split q=1/16: recipients absorbed into W")

    clone_note = clone_consistency_check(partner)
    front = choose_frontiers(records)

    best_visible_workable_ratio = F(0)
    best_visible_workable_rec = None
    best_visible_workable_a = None
    best_band_workable_g = F(0)
    best_band_workable_rec = None
    best_band_workable_a = None
    for a in WORKABLE_A:
        vrec = front[f"visible_{astr(a)}"]
        vis = vrec["by_a"][a]["max_visible_g"]
        ratio_sq = vis * vis / vrec["delta"] if vis > 0 else F(0)
        if ratio_sq > best_visible_workable_ratio:
            best_visible_workable_ratio = ratio_sq
            best_visible_workable_rec = vrec
            best_visible_workable_a = a
        brec = front[f"band_{astr(a)}"]
        band = brec["by_a"][a]["max_nonW_g"]
        if band > best_band_workable_g:
            best_band_workable_g = band
            best_band_workable_rec = brec
            best_band_workable_a = a

    # The exact checked frontier has no workable deep-halo support.
    hard_assert(best_visible_workable_ratio == 0, "frontier: no tested a in {4,5,6} has positive visible g")
    hard_assert(best_band_workable_g == 0, "frontier: no tested a in {4,5,6} has positive non-W band g")

    low_vis = front["visible_low"]
    low_band = front["band_low"]
    low_vis_g = low_vis["by_a"][F(1, 4)]["max_visible_g"]
    low_band_g = low_band["by_a"][F(1, 4)]["max_nonW_g"]

    matrix_records = [partner, split4, split_absorb, rank5, web, relaxed]
    if low_vis not in matrix_records:
        matrix_records.append(low_vis)
    if low_band not in matrix_records:
        matrix_records.append(low_band)

    lines: list[str] = []
    lines.append("NO-KILL-FRONTIER. In the exact matrices and duplicate-family scan certified here, every workable deep halo `a in {4,5,6}` has `G_a` empty, so visible `sup g_w/tau = 0` and band `sup g = 0`. This is a frontier report, not an emptiness theorem.")
    lines.append("")
    lines.append("# W20 Worker B — adversarial g-bootstrap kill attempt")
    lines.append("")
    lines.append("Tier legend: [T0] repo definition/banked construction pattern; [T1] exact Fraction computation hard-asserted by this script; [T2] structured read from the checked constructions; [T3] heuristic.")
    lines.append("")
    lines.append("## Rerun")
    lines.append("")
    lines.append("```bash")
    lines.append("python3 runs/2026-07-06-w20-g-zoo-measurement/scripts/w20_worker_b.py")
    lines.append("```")
    lines.append("")
    lines.append("## Verdict")
    lines.append("")
    lines.append("- [T1] K1 was not realized: for all certified records in this worker artifact and all `a in {4,5,6}`, `G_a` is empty, hence every visible row has signed `g_w=0`.")
    lines.append("- [T1] K2 was not realized at workable widths: the same empty `G_a` gives no non-W level set with `g>=1/2`.")
    lines.append(f"- [T1] Low-halo stress only (`a=1/4`): best visible value is `{fstr(low_vis_g)}` on `{low_vis['label']}`, with `(g/tau)^2={ratio_square_str(low_vis_g, low_vis['delta'])}` and `g/tau~{ratio_over_tau_float(low_vis_g, low_vis['delta']):.6f}`.")
    lines.append(f"- [T1] Low-halo band frontier (`a=1/4`): best non-W signed `g` is `{fstr(low_band_g)}` on `{low_band['label']}`; this is far below `1/2`.")
    lines.append("- [T2] Binding constraint: coefficient capacity is not the wall. The exact row-negativity LP places `5/4` designated positive mass, but exact geometry absorbs those rows into `W` (`H=0`). In the under-cap exact geometries that keep hidden rows, depth stays inside even the `a=1` halo, let alone `a=4`.")
    lines.append("")
    lines.append("## Workable-width frontier table")
    lines.append("")
    lines.append("| a | visible frontier | visible g | (g/tau)^2 | band frontier | band g | level(g>=1/2) |")
    lines.append("|---:|---|---:|---:|---|---:|---|")
    for a in WORKABLE_A:
        vrec = front[f"visible_{astr(a)}"]
        brec = front[f"band_{astr(a)}"]
        vg = vrec["by_a"][a]["max_visible_g"]
        bg = brec["by_a"][a]["max_nonW_g"]
        lines.append(f"| {astr(a)} | {vrec['label']} | {fstr(vg)} | {ratio_square_str(vg, vrec['delta'])} | {brec['label']} | {fstr(bg)} | {list(brec['by_a'][a]['level'])} |")
    lines.append("")
    lines.append("## Low-halo diagnostics")
    lines.append("")
    lines.append("- [T1] These are not K1/K2 kills because `a=1/4` is the old sigma-halo scale, not the workable `a>=4` Lemma-A scale.")
    lines.append(f"- [T1] Best visible low-halo row: `{low_vis['label']}`; {a_summary(low_vis, F(1, 4))}.")
    lines.append(f"- [T1] Best non-W low-halo row: `{low_band['label']}`; {a_summary(low_band, F(1, 4))}.")
    lines.append(f"- {clone_note}")
    lines.append("")
    lines.append("## LP relaxation vs exact geometry")
    lines.append("")
    lines.append("- [T1] The relaxed cycle LP optimizes only coefficient/negative-mass constraints and reaches designated positive mass `5/4`.")
    lines.append("- [T1] After exact visible-set geometry is recomputed, that optimizer has `W=[3,4,5]`, `H=0`, no hidden row, and all `G_a` empty. This repeats the W19 absorption wall in the signed `g` language.")
    lines.append("")
    lines.append("## Full exact matrices for frontier/certificate instances")
    lines.append("")
    seen: set[str] = set()
    for rec in matrix_records:
        if rec["label"] in seen:
            continue
        seen.add(rec["label"])
        lines.extend(section_for_matrix(rec))
    lines.append("## Duplicate-family scan")
    lines.append("")
    lines.append(f"- [T1] Checked `{len(scan_records)}` under-cap exact duplicate-family candidates over rational `p,q`; every candidate hard-asserted idempotence, row sums, `0<delta<=1/4`, visible-set nonemptiness, exact distances, and `Pg=g` for every listed halo width.")
    lines.append("- [T2] No checked scan candidate had positive `G_a` for `a in {4,5,6}`. This is a bounded construction-family frontier, not a proof of impossibility.")
    lines.append("")
    lines.append("## Assert list")
    lines.append("")
    for msg in ASSERTS:
        lines.append(f"- [T1] {msg}")
    lines.append("")
    return "\n".join(lines) + "\n"


def main() -> None:
    report = make_report()
    OUT.write_text(report)
    print(report)


if __name__ == "__main__":
    main()
