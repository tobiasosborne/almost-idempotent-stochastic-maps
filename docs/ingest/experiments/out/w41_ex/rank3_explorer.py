#!/usr/bin/env python3
"""Exact rank-3 chart explorer for w41_ex.

Rows of L are affine coordinates with row sum 1.  B is any exact left inverse
of L, so P=L B is row-stochastic and idempotent.  The script enumerates all
actual-row bases in the theta=1/2 class, computes Phi_s and S*_s, compares
candidate selectors, and generates exact random/adversarial rank-3 instances.
"""
from __future__ import annotations

import itertools
import json
import random
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Iterable

import sympy as sp


THETA = sp.Rational(1, 2)
DELTA0 = sp.Rational(1, 4)


def pos(x: sp.Expr) -> sp.Expr:
    x = sp.factor(x)
    return x if x > 0 else sp.Integer(0)


def neg(x: sp.Expr) -> sp.Expr:
    x = sp.factor(x)
    return -x if x < 0 else sp.Integer(0)


def qstr(x: sp.Expr) -> str:
    return str(sp.factor(x))


def fkey(x: sp.Expr) -> Fraction:
    return Fraction(str(sp.factor(x)))


def row_neg(row: Iterable[sp.Expr]) -> sp.Expr:
    return sp.factor(sum(neg(x) for x in row))


def delta_of(P: sp.Matrix) -> sp.Expr:
    return max(row_neg(P.row(i)) for i in range(P.rows))


def checks(L: sp.Matrix, B: sp.Matrix, P: sp.Matrix) -> dict[str, bool]:
    return {
        "BL": bool(sp.simplify(B * L - sp.eye(L.cols)) == sp.zeros(L.cols, L.cols)),
        "P2": bool(sp.simplify(P * P - P) == sp.zeros(P.rows, P.cols)),
        "rowsum": all(sp.simplify(sum(P.row(i)) - 1) == 0 for i in range(P.rows)),
    }


def coeffs(L: sp.Matrix, basis: tuple[int, ...]) -> sp.Matrix:
    return sp.simplify(L * L[list(basis), :].inv())


def all_bases_by_volume(L: sp.Matrix) -> tuple[sp.Expr, dict[sp.Expr, list[tuple[int, ...]]]]:
    by_vol: dict[sp.Expr, list[tuple[int, ...]]] = {}
    for basis in itertools.combinations(range(L.rows), L.cols):
        d = sp.factor(L[list(basis), :].det())
        if d == 0:
            continue
        by_vol.setdefault(abs(d), []).append(basis)
    if not by_vol:
        raise ValueError("no nonsingular actual-row basis")
    return max(by_vol), by_vol


def theta_bases(L: sp.Matrix, theta: sp.Expr = THETA) -> tuple[sp.Expr, list[tuple[int, ...]]]:
    best, by_vol = all_bases_by_volume(L)
    bases: list[tuple[int, ...]] = []
    for vol, bs in by_vol.items():
        if vol >= theta * best:
            bases.extend(bs)
    return best, sorted(bases)


def per_row(Arow: list[sp.Expr], s: int) -> tuple[sp.Expr, sp.Expr, sp.Expr, sp.Expr, sp.Expr]:
    lam = sp.factor(1 - Arow[s])
    mu = sp.factor(sum(neg(Arow[t]) for t in range(len(Arow)) if t != s))
    sigma = sp.factor(sum(pos(Arow[t]) for t in range(len(Arow)) if t != s))
    E = pos(mu - lam)
    g = sp.factor(sigma + 2 * neg(lam))
    return lam, mu, sigma, E, g


def chart_metrics(P: sp.Matrix, L: sp.Matrix, basis: tuple[int, ...]) -> dict[str, object]:
    A = coeffs(L, basis)
    sf: list[sp.Expr] = []
    sstar: list[sp.Expr] = []
    splus: list[sp.Expr] = []
    V: list[sp.Expr] = []
    Dpos: list[sp.Expr] = []
    Dneg: list[sp.Expr] = []
    defs: list[sp.Expr] = []
    factor_fail: list[object] = []
    max_abs_a = max(abs(x) for x in list(A))
    total_neg = sp.factor(sum(neg(x) for x in list(A)))
    min_coeff = min(list(A))
    for s, u in enumerate(basis):
        SF = SS = SP = VV = DP = DN = DF = sp.Integer(0)
        for j in range(P.cols):
            beta = sp.factor(P[u, j])
            bp = pos(beta)
            bn = neg(beta)
            lam, _mu, sigma, E, g = per_row(list(A.row(j)), s)
            if sp.simplify(g - (E + 2 * pos(lam))) > 0:
                factor_fail.append(["point", s, int(u), j, qstr(lam), qstr(sigma), qstr(E), qstr(g)])
            DF += beta * lam
            if bp:
                SF += bp * E
                SP += bp * sigma
                SS += bp * g
                VV += bp * neg(lam)
                DP += bp * pos(lam)
            if bn:
                DN += bn * lam
        sf.append(sp.factor(SF))
        splus.append(sp.factor(SP))
        sstar.append(sp.factor(SS))
        V.append(sp.factor(VV))
        Dpos.append(sp.factor(DP))
        Dneg.append(sp.factor(DN))
        defs.append(sp.factor(DF))
    return {
        "basis": list(basis),
        "phi_s": sf,
        "phi": max(sf),
        "sstar_s": sstar,
        "sstar_max": max(sstar),
        "splus_s": splus,
        "V_s": V,
        "Dpos_s": Dpos,
        "Dneg_s": Dneg,
        "def_s": defs,
        "max_abs_a": sp.factor(max_abs_a),
        "total_neg": total_neg,
        "min_coeff": sp.factor(min_coeff),
        "factor_point_ok": not factor_fail,
        "factor_fail": factor_fail[:3],
    }


def enumerate_charts(P: sp.Matrix, L: sp.Matrix, theta: sp.Expr = THETA) -> tuple[sp.Expr, list[dict[str, object]]]:
    best, bases = theta_bases(L, theta)
    charts = [chart_metrics(P, L, b) for b in bases]
    charts.sort(key=lambda c: (fkey(c["phi"]), tuple(c["basis"])))
    return best, charts


def select_candidates(charts: list[dict[str, object]], best_vol: sp.Expr, L: sp.Matrix) -> dict[str, dict[str, object]]:
    volumes = {tuple(c["basis"]): abs(sp.factor(L[c["basis"], :].det())) for c in charts}
    maxvol = [c for c in charts if volumes[tuple(c["basis"])] == best_vol]
    out: dict[str, dict[str, object]] = {}
    out["phi_argmin"] = min(charts, key=lambda c: (fkey(c["phi"]), tuple(c["basis"])))
    out["max_volume_best_phi"] = min(maxvol, key=lambda c: (fkey(c["phi"]), tuple(c["basis"])))
    out["max_volume_worst_phi"] = max(maxvol, key=lambda c: (fkey(c["phi"]), tuple(c["basis"])))
    out["peeled_most_convex"] = max(
        charts,
        key=lambda c: (fkey(c["min_coeff"]), fkey(volumes[tuple(c["basis"])]), -fkey(c["phi"]), tuple([-x for x in c["basis"]])),
    )
    out["min_total_neg"] = min(charts, key=lambda c: (fkey(c["total_neg"]), -fkey(volumes[tuple(c["basis"])]), fkey(c["phi"]), tuple(c["basis"])))
    return out


def left_inverse_from_basis(L: sp.Matrix, basis: tuple[int, ...]) -> sp.Matrix:
    inv = L[list(basis), :].inv()
    B = sp.zeros(L.cols, L.rows)
    for local_col, row_index in enumerate(basis):
        for r in range(L.cols):
            B[r, row_index] = inv[r, local_col]
    return sp.simplify(B)


def convex_mixture_left_inverse(L: sp.Matrix, weighted_bases: list[tuple[sp.Expr, tuple[int, ...]]]) -> sp.Matrix:
    B = sp.zeros(L.cols, L.rows)
    for w, basis in weighted_bases:
        B += w * left_inverse_from_basis(L, basis)
    return sp.simplify(B)


def transverse_pair(a: sp.Expr, mass: sp.Expr = sp.Integer(1)) -> tuple[sp.Matrix, sp.Matrix]:
    L = sp.Matrix(
        [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1],
            [1, a, -a],
            [1, -a, a],
        ]
    )
    c = sp.factor(a / (1 + 4 * a * a))
    B = sp.Matrix(
        [
            [1 - mass, 0, 0, mass / 2, mass / 2],
            [0, 1 - 2 * a * c, 2 * a * c, c, -c],
            [0, 2 * a * c, 1 - 2 * a * c, -c, c],
        ]
    )
    return L, sp.simplify(B)


def staircase_m1(eps: sp.Expr | None = None) -> tuple[sp.Matrix, sp.Matrix]:
    sigma = [0, 1, -1]
    rows = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    xp = [sp.Integer(0)] * 3
    xm = [sp.Integer(0)] * 3
    if eps is None:
        xp[0] = xm[0] = 1
        for t in range(1, 3):
            xp[t] = sp.Rational(sigma[t], 2)
            xm[t] = -sp.Rational(sigma[t], 2)
    else:
        h = 1 - eps
        d = eps / 2
        xp[0] = xm[0] = h
        for t in range(1, 3):
            xp[t] = d + sp.Rational(sigma[t], 2)
            xm[t] = d - sp.Rational(sigma[t], 2)
    rows += [xp, xm]
    L = sp.Matrix(rows)
    B = sp.zeros(3, 5)
    if eps is not None:
        B[0, 0] = eps
        B[0, 1] = B[0, 2] = -eps / 2
    B[0, 3] = B[0, 4] = sp.Rational(1, 2)
    for r in range(1, 3):
        for t in range(1, 3):
            B[r, t] = (1 if r == t else 0) - sp.Rational(sigma[r] * sigma[t], 2)
        B[r, 3] = sp.Rational(sigma[r], 2)
        B[r, 4] = -sp.Rational(sigma[r], 2)
    return L, sp.simplify(B)


def no_center_rank3(a: sp.Expr = sp.Rational(1, 100), mode: str = "symmetric") -> tuple[sp.Matrix, sp.Matrix]:
    L = sp.Matrix(
        [
            [0, 1, 0],
            [0, 0, 1],
            [1, a, -a],
            [1, -a, a],
        ]
    )
    if mode == "symmetric":
        symbols = sp.symbols("b0:3_0:4")
        Bsym = sp.Matrix(3, 4, symbols)
        eqs = []
        BL = Bsym * L
        for i in range(3):
            for j in range(3):
                eqs.append(sp.Eq(BL[i, j], 1 if i == j else 0))
        eqs.append(sp.Eq(Bsym[0, 2], sp.Rational(1, 2)))
        eqs.append(sp.Eq(Bsym[0, 3], sp.Rational(1, 2)))
        sol = sp.solve(eqs, list(Bsym), dict=True)[0]
        B = Bsym.subs(sol).subs({x: 0 for x in Bsym if x not in sol})
    else:
        B = left_inverse_from_basis(L, (0, 1, 2))
    return L, sp.simplify(B)


def rank3_analog_dense_pair(a: sp.Expr = sp.Rational(1, 4), mass: sp.Expr = sp.Integer(1)) -> tuple[sp.Matrix, sp.Matrix]:
    return transverse_pair(a, mass)


def polygon_rows(points: list[tuple[sp.Expr, sp.Expr]]) -> sp.Matrix:
    return sp.Matrix([[1 - x - y, x, y] for x, y in points])


def regular_windmill(radius_num: int = 1, radius_den: int = 3, inner_num: int = 1, inner_den: int = 20) -> sp.Matrix:
    # Rational substitute for a three-blade windmill around the barycenter.
    r = sp.Rational(radius_num, radius_den)
    q = sp.Rational(inner_num, inner_den)
    pts = [
        (sp.Rational(1, 3) + r, sp.Rational(1, 3)),
        (sp.Rational(1, 3), sp.Rational(1, 3) + r),
        (sp.Rational(1, 3) - r, sp.Rational(1, 3) - r),
        (sp.Rational(1, 3) + q, sp.Rational(1, 3) - 2 * q),
        (sp.Rational(1, 3) - 2 * q, sp.Rational(1, 3) + q),
        (sp.Rational(1, 3) + q, sp.Rational(1, 3) + q),
    ]
    return polygon_rows(pts)


def near_degenerate_rows(t: sp.Expr = sp.Rational(1, 20), h: sp.Expr = sp.Rational(1, 12)) -> sp.Matrix:
    pts = [
        (0, 0),
        (1, 0),
        (t, h),
        (sp.Rational(1, 2), -h / 2),
        (1 - t, h),
        (sp.Rational(1, 2), h),
    ]
    return polygon_rows(pts)


def random_L(rng: random.Random, n: int, den: int = 12, spread: int = 4) -> sp.Matrix:
    pts: list[tuple[sp.Expr, sp.Expr]] = []
    forced = [(0, 0), (1, 0), (0, 1)]
    for x, y in forced[: min(3, n)]:
        pts.append((sp.Rational(x), sp.Rational(y)))
    while len(pts) < n:
        x = sp.Rational(rng.randint(-spread, den + spread), den)
        y = sp.Rational(rng.randint(-spread, den + spread), den)
        if (x, y) not in pts:
            pts.append((x, y))
    return polygon_rows(pts)


def basis_mixture_instance(L: sp.Matrix, bases: list[tuple[int, ...]], weights: list[sp.Expr]) -> sp.Matrix:
    total = sum(weights)
    weighted = [(sp.factor(w / total), b) for w, b in zip(weights, bases)]
    return convex_mixture_left_inverse(L, weighted)


@dataclass
class Instance:
    name: str
    L: sp.Matrix
    B: sp.Matrix
    tag: str


def summarize_instance(inst: Instance) -> dict[str, object] | None:
    L, B = inst.L, inst.B
    P = sp.simplify(L * B)
    delta = delta_of(P)
    if delta == 0:
        # Keep zero-delta only if Phi is also zero; ratio is otherwise infinite.
        pass
    best_vol, charts = enumerate_charts(P, L)
    cands = select_candidates(charts, best_vol, L)
    factor_global_ok = True
    for c in charts:
        for s, val in enumerate(c["sstar_s"]):
            bound = sp.factor(2 * c["phi_s"][s] + 6 * delta)
            if sp.simplify(val - bound) > 0:
                factor_global_ok = False
    ratio = lambda x: "inf" if delta == 0 and x != 0 else ("0" if delta == 0 else qstr(sp.factor(x / delta)))
    cand_summary: dict[str, object] = {}
    for key, c in cands.items():
        cand_summary[key] = {
            "basis": c["basis"],
            "phi": qstr(c["phi"]),
            "phi_over_delta": ratio(c["phi"]),
            "sstar_max_over_delta": ratio(c["sstar_max"]),
            "total_neg": qstr(c["total_neg"]),
            "min_coeff": qstr(c["min_coeff"]),
        }
    phi = cands["phi_argmin"]["phi"]
    return {
        "name": inst.name,
        "tag": inst.tag,
        "n": L.rows,
        "delta": qstr(delta),
        "delta_ok": bool(delta <= DELTA0),
        "max_volume": qstr(best_vol),
        "theta_class_size": len(charts),
        "checks": checks(L, B, P),
        "factor_global_ok": factor_global_ok,
        "phi_min": qstr(phi),
        "phi_min_over_delta": ratio(phi),
        "sstar_at_phi_argmin_over_delta": ratio(cands["phi_argmin"]["sstar_max"]),
        "candidates": cand_summary,
    }


def mandatory_instances() -> list[Instance]:
    out: list[Instance] = []
    for a in [sp.Rational(1, 8), sp.Rational(1, 4)]:
        L, B = transverse_pair(a)
        out.append(Instance(f"transverse_pair_a{qstr(a).replace('/', '_')}", L, B, "known_rank3"))
    L, B = rank3_analog_dense_pair(sp.Rational(1, 4))
    out.append(Instance("dense_pair_rank3_restriction_transverse_a1_4", L, B, "known_restricted"))
    L, B = staircase_m1()
    out.append(Instance("staircase_m1_rank3_delta1_2", L, B, "known_rank3_outside_delta0"))
    L, B = staircase_m1(sp.Rational(1, 1000))
    out.append(Instance("perturbed_staircase_m1_eps1_1000_delta1_2", L, B, "known_rank3_outside_delta0"))
    for a in [sp.Rational(1, 100), sp.Rational(1, 4)]:
        L, B = no_center_rank3(a, "symmetric")
        out.append(Instance(f"no_center_rank3_a{qstr(a).replace('/', '_')}", L, B, "known_rank3"))
    return out


def random_instances(count: int = 220) -> list[Instance]:
    rng = random.Random(41003)
    out: list[Instance] = []
    attempts = 0
    while len(out) < count and attempts < count * 80:
        attempts += 1
        n = rng.randint(5, 9)
        L = random_L(rng, n, den=rng.choice([8, 10, 12, 16]), spread=rng.choice([1, 2, 3]))
        try:
            best, by_vol = all_bases_by_volume(L)
        except ValueError:
            continue
        all_bases = [b for bs in by_vol.values() for b in bs]
        # Bias toward high-volume bases so delta usually lands below 1/4.
        sorted_bases = sorted(all_bases, key=lambda b: abs(L[list(b), :].det()), reverse=True)
        m = rng.choice([1, 1, 2, 3])
        bases = rng.sample(sorted_bases[: min(len(sorted_bases), 10)], k=min(m, len(sorted_bases[:10])))
        weights = [sp.Rational(rng.randint(1, 5), rng.randint(1, 5)) for _ in bases]
        B = basis_mixture_instance(L, bases, weights)
        P = sp.simplify(L * B)
        delta = delta_of(P)
        if delta <= DELTA0 and checks(L, B, P)["BL"] and checks(L, B, P)["P2"]:
            out.append(Instance(f"random_exact_{len(out):03d}", L, B, "random"))
    return out


def adversarial_instances() -> list[Instance]:
    out: list[Instance] = []
    # Windmills and near-degenerate clouds with left inverses supported on high-volume triangles.
    templates = [
        ("windmill_r1_3_q1_20", regular_windmill(sp.Integer(1), sp.Integer(3), sp.Integer(1), sp.Integer(20))),
        ("windmill_r1_4_q1_12", regular_windmill(sp.Integer(1), sp.Integer(4), sp.Integer(1), sp.Integer(12))),
        ("near_degenerate_t1_20_h1_12", near_degenerate_rows(sp.Rational(1, 20), sp.Rational(1, 12))),
        ("near_degenerate_t1_50_h1_20", near_degenerate_rows(sp.Rational(1, 50), sp.Rational(1, 20))),
    ]
    for name, L in templates:
        best, by_vol = all_bases_by_volume(L)
        bases = sorted([b for v, bs in by_vol.items() if v >= THETA * best for b in bs])
        # Try single high-volume charts and small mixtures.
        for idx, b in enumerate(bases[:8]):
            B = left_inverse_from_basis(L, b)
            out.append(Instance(f"{name}_basis_{idx}", L, B, "adversarial_basis"))
        for idx, combo in enumerate(itertools.combinations(bases[:6], 2)):
            B = basis_mixture_instance(L, list(combo), [sp.Rational(1, 2), sp.Rational(1, 2)])
            out.append(Instance(f"{name}_mix2_{idx}", L, B, "adversarial_mix"))
    # Hand-tuned outside rows around the standard simplex, filtered later by delta.
    param_sets = [
        (sp.Rational(1, 5), sp.Rational(1, 20)),
        (sp.Rational(1, 4), sp.Rational(1, 30)),
        (sp.Rational(1, 6), sp.Rational(1, 12)),
        (sp.Rational(1, 8), sp.Rational(1, 40)),
    ]
    for a, e in param_sets:
        rows = sp.Matrix(
            [
                [1, 0, 0],
                [0, 1, 0],
                [0, 0, 1],
                [1 - e, 1 + a, -a],
                [-a, 1 - e, 1 + a],
                [1 + a, -a, 1 - e],
                [1 - e, -a, 1 + a],
                [1 + a, 1 - e, -a],
                [-a, 1 + a, 1 - e],
            ]
        )
        # Normalize row sums to 1 by subtracting excess from the first coordinate.
        fixed_rows = []
        for i in range(rows.rows):
            r = list(rows.row(i))
            excess = sum(r) - 1
            r[0] -= excess
            fixed_rows.append(r)
        L = sp.Matrix(fixed_rows)
        best, by_vol = all_bases_by_volume(L)
        bases = sorted([b for v, bs in by_vol.items() if v >= THETA * best for b in bs])
        for idx, combo in enumerate(itertools.combinations(bases[:7], 2)):
            B = basis_mixture_instance(L, list(combo), [sp.Rational(2, 3), sp.Rational(1, 3)])
            out.append(Instance(f"cyclic_outside_a{qstr(a).replace('/', '_')}_e{qstr(e).replace('/', '_')}_{idx}", L, B, "adversarial_cyclic"))
        standard = (0, 1, 2)
        if abs(L[list(standard), :].det()) != 0:
            out.append(
                Instance(
                    f"cyclic_outside_a{qstr(a).replace('/', '_')}_e{qstr(e).replace('/', '_')}_standard",
                    L,
                    left_inverse_from_basis(L, standard),
                    "adversarial_cyclic_standard",
                )
            )
            for idx, b in enumerate(bases[:8]):
                if b == standard:
                    continue
            for w in [sp.Rational(3, 4), sp.Rational(7, 8), sp.Rational(15, 16)]:
                    B = basis_mixture_instance(L, [standard, b], [w, 1 - w])
                    out.append(
                        Instance(
                            f"cyclic_outside_a{qstr(a).replace('/', '_')}_e{qstr(e).replace('/', '_')}_stdmix_{idx}_{qstr(w).replace('/', '_')}",
                            L,
                            B,
                            "adversarial_cyclic_standard_mix",
                        )
                    )
    # Balanced cyclic rows around each simplex edge, with the standard simplex
    # left inverse.  Here delta is exactly a, but max-volume triangles may use
    # the outside rows.
    for a in [
        sp.Rational(1, 4),
        sp.Rational(1, 5),
        sp.Rational(1, 6),
        sp.Rational(1, 8),
        sp.Rational(1, 10),
        sp.Rational(1, 12),
        sp.Rational(1, 16),
        sp.Rational(1, 20),
    ]:
        L = sp.Matrix(
            [
                [1, 0, 0],
                [0, 1, 0],
                [0, 0, 1],
                [1, a, -a],
                [1, -a, a],
                [-a, 1, a],
                [a, 1, -a],
                [-a, a, 1],
                [a, -a, 1],
            ]
        )
        standard = (0, 1, 2)
        out.append(Instance(f"balanced_cyclic_standard_a{qstr(a).replace('/', '_')}", L, left_inverse_from_basis(L, standard), "adversarial_balanced_cyclic"))
        best, by_vol = all_bases_by_volume(L)
        bases = sorted([b for v, bs in by_vol.items() if v >= THETA * best for b in bs])
        for idx, b in enumerate(bases[:5]):
            if b == standard:
                continue
            B = basis_mixture_instance(L, [standard, b], [sp.Rational(15, 16), sp.Rational(1, 16)])
            out.append(Instance(f"balanced_cyclic_stdmix_a{qstr(a).replace('/', '_')}_{idx}", L, B, "adversarial_balanced_cyclic_mix"))
    # Scaled no-center rank-3 path, including several exact small-delta choices.
    for a in [
        sp.Rational(1, 100),
        sp.Rational(1, 80),
        sp.Rational(1, 60),
        sp.Rational(1, 50),
        sp.Rational(1, 40),
        sp.Rational(1, 30),
        sp.Rational(1, 25),
        sp.Rational(1, 20),
        sp.Rational(1, 16),
        sp.Rational(1, 12),
        sp.Rational(1, 10),
        sp.Rational(1, 8),
        sp.Rational(1, 6),
        sp.Rational(1, 5),
        sp.Rational(1, 4),
    ]:
        L, B = no_center_rank3(a, "symmetric")
        out.append(Instance(f"no_center_rank3_fixed_a{qstr(a).replace('/', '_')}", L, B, "adversarial_no_center"))
    return out


def run_suite() -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    instances = mandatory_instances() + random_instances(220) + adversarial_instances()
    for inst in instances:
        try:
            rec = summarize_instance(inst)
        except Exception as exc:  # keep the suite running; failures are reported.
            rec = {"name": inst.name, "tag": inst.tag, "error": repr(exc)}
        if rec is not None:
            records.append(rec)
    return records


def main() -> None:
    records = run_suite()
    Path("rank3_results.json").write_text(json.dumps(records, indent=2, sort_keys=True))
    usable = [r for r in records if "error" not in r and r.get("delta_ok")]
    mandatory = [r for r in records if "error" not in r and str(r.get("tag", "")).startswith("known")]
    adversarial = [r for r in usable if str(r.get("tag", "")).startswith("adversarial")]
    randoms = [r for r in usable if r.get("tag") == "random"]
    worst = max(usable, key=lambda r: Fraction(str(r["phi_min_over_delta"]).replace("inf", "999999999"))) if usable else None
    lines = [
        f"total_records={len(records)} usable_delta_le_1_4={len(usable)} random_delta_le_1_4={len(randoms)} adversarial_delta_le_1_4={len(adversarial)}",
        f"factorization_checked_all={all(r.get('factor_global_ok', False) for r in records if 'error' not in r)}",
    ]
    if worst:
        lines.append(
            f"worst_delta_ok={worst['name']} tag={worst['tag']} delta={worst['delta']} "
            f"phi_min/delta={worst['phi_min_over_delta']} theta_class={worst['theta_class_size']} "
            f"basis={worst['candidates']['phi_argmin']['basis']}"
        )
    lines.append("mandatory:")
    for r in mandatory:
        lines.append(
            f"  {r['name']}: delta={r['delta']} delta_ok={r['delta_ok']} "
            f"phi_min/d={r['phi_min_over_delta']} maxvol_best/d={r['candidates']['max_volume_best_phi']['phi_over_delta']} "
            f"peeled/d={r['candidates']['peeled_most_convex']['phi_over_delta']} "
            f"negmass/d={r['candidates']['min_total_neg']['phi_over_delta']}"
        )
    lines.append("top_delta_ok:")
    for r in sorted(usable, key=lambda z: Fraction(str(z["phi_min_over_delta"]).replace("inf", "999999999")), reverse=True)[:20]:
        lines.append(
            f"  {r['name']}: tag={r['tag']} delta={r['delta']} "
            f"phi_min/d={r['phi_min_over_delta']} maxvol_best/d={r['candidates']['max_volume_best_phi']['phi_over_delta']} "
            f"peeled/d={r['candidates']['peeled_most_convex']['phi_over_delta']} "
            f"negmass/d={r['candidates']['min_total_neg']['phi_over_delta']}"
        )
    Path("rank3_results.txt").write_text("\n".join(lines) + "\n")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
