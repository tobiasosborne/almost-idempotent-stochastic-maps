#!/usr/bin/env python3
"""Exact L3 numerics for richer (EX) shear-coupling families.

The constructor is the same LB template as the high-rank no-center run:
foreign unit rows, signed shear rows attached to one or more anchors, an exact
left inverse B with uniform anchor mass on each signed fan, and P = L B.  All
certified arithmetic is over SymPy rationals/integers; decimals are display
only.
"""
from __future__ import annotations

import csv
import itertools
from dataclasses import dataclass
from decimal import Decimal, getcontext
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "multiblock_coupling.csv"
A0 = sp.Rational(1, 100)


@dataclass(frozen=True)
class Case:
    family: str
    params: str
    anchors: int
    foreign: int
    groups: tuple[tuple[tuple[int, ...], ...], ...]
    certification: str
    expected_ratio: sp.Rational | None = None


def pos(x):
    return x if x > 0 else sp.Integer(0)


def neg(x):
    return -x if x < 0 else sp.Integer(0)


def qstr(x):
    return str(sp.factor(x))


def decstr(x, places=12):
    q = sp.Rational(x)
    getcontext().prec = places + 8
    d = Decimal(int(q.p)) / Decimal(int(q.q))
    return format(d.quantize(Decimal(1).scaleb(-places)), "f")


def vec(*entries):
    return tuple(sp.Integer(x) for x in entries)


def edge(f, u, v):
    w = [sp.Integer(0)] * f
    w[u] = 1
    w[v] = -1
    return tuple(w)


def ternary(f, u, v, t):
    w = [sp.Integer(0)] * f
    w[u] = 1
    w[v] = 1
    w[t] = -2
    return tuple(w)


def signed_closure(base):
    out = []
    for w in base:
        out.append(tuple(sp.Integer(x) for x in w))
        out.append(tuple(-sp.Integer(x) for x in w))
    return tuple(out)


def no_center_path_group(f):
    return signed_closure(edge(f, i, i + 1) for i in range(f - 1))


def star_group(f, center=0):
    return signed_closure(edge(f, center, v) for v in range(f) if v != center)


def complete_group(f):
    return signed_closure(edge(f, u, v) for u in range(f) for v in range(u + 1, f))


def complete_bipartite_group(left, right):
    f = left + right
    return signed_closure(edge(f, u, left + v) for u in range(left) for v in range(right))


def ternary_all_group(f):
    base = []
    for t in range(f):
        others = [i for i in range(f) if i != t]
        for u, v in itertools.combinations(others, 2):
            base.append(ternary(f, u, v, t))
    return signed_closure(base)


def cycle_skip_group(f):
    base = []
    for i in range(f):
        base.append(edge(f, i, (i + 1) % f))
        base.append(edge(f, i, (i + 2) % f))
    # Deduplicate before adding signs; small f can make skip edges repeat.
    base = sorted(set(base))
    return signed_closure(base)


def check_group_zero_average(group):
    f = len(group[0])
    return all(sum(w[i] for w in group) == 0 for i in range(f))


def build_LB(case, a=A0):
    g, f = case.anchors, case.foreign
    rows = []
    row_meta = []
    for i in range(f):
        row = [sp.Integer(0)] * (g + f)
        row[g + i] = 1
        rows.append(row)
        row_meta.append(("unit", i, None))
    for h, group in enumerate(case.groups):
        if not group:
            raise SystemExit(f"{case.family}: empty anchor group {h}")
        if not check_group_zero_average(group):
            raise SystemExit(f"{case.family}: group {h} does not average to zero")
        for w_idx, w in enumerate(group):
            row = [sp.Integer(0)] * (g + f)
            row[h] = 1
            for i, val in enumerate(w):
                row[g + i] = a * val
            rows.append(row)
            row_meta.append(("signed", h, w_idx))
    L = sp.Matrix(rows)
    B = sp.zeros(g + f, len(rows))
    for i in range(f):
        B[g + i, i] = 1
    offset = f
    for h, group in enumerate(case.groups):
        mass = sp.Rational(1, len(group))
        for j in range(len(group)):
            B[h, offset + j] = mass
        offset += len(group)
    return L, B, row_meta


def p_row(case, row_index, a=A0):
    g, f = case.anchors, case.foreign
    n = f + sum(len(group) for group in case.groups)
    out = [sp.Integer(0)] * n
    if row_index < f:
        out[row_index] = 1
        return out
    offset = f
    for h, group in enumerate(case.groups):
        if row_index < offset + len(group):
            w = group[row_index - offset]
            mass = sp.Rational(1, len(group))
            for j in range(offset, offset + len(group)):
                out[j] += mass
            for i, val in enumerate(w):
                out[i] += a * val
            return [sp.factor(x) for x in out]
        offset += len(group)
    raise IndexError(row_index)


def row_neg(row):
    return sp.factor(sum(neg(x) for x in row))


def delta_of_case(case, a=A0):
    signed_negs = [sum(neg(x) for x in w) for group in case.groups for w in group]
    return sp.factor(a * max(signed_negs))


def actual_rows_count(case):
    return case.foreign + sum(len(group) for group in case.groups)


def group_offsets(case):
    offsets = []
    off = case.foreign
    for group in case.groups:
        offsets.append(off)
        off += len(group)
    return offsets


def reduced_bases(case):
    units = tuple(range(case.foreign))
    offsets = group_offsets(case)
    choices = [range(offsets[h], offsets[h] + len(case.groups[h])) for h in range(case.anchors)]
    return [units + tuple(picks) for picks in itertools.product(*choices)]


def max_shear_norm_sq(case):
    return max(sp.factor(sum(x * x for x in w)) for group in case.groups for w in group)


def max_neg_shear(case):
    return max(sp.factor(sum(neg(x) for x in w)) for group in case.groups for w in group)


def reduction_bound_ok(case, a=A0):
    # After selecting one signed row per anchor, every extra signed row costs one
    # omitted foreign unit.  Subtracting the anchor pivot leaves a foreign vector
    # with squared norm at most 4*R2, so Hadamard bounds each extra determinant
    # factor by a*sqrt(4*R2).
    r2 = max_shear_norm_sq(case)
    return sp.factor(4 * r2 * a * a) < sp.Rational(1, 4)


def neg_l1_diff(w, w0):
    return sp.factor(sum(neg(w[i] - w0[i]) for i in range(len(w))))


def pos_l1(w):
    return sp.factor(sum(pos(x) for x in w))


def best_reduced_chart_metrics(case, a=A0):
    """Exact closed-form scan over the certified reduced theta class.

    In a reduced chart the foreign unit rows are all pivots and each anchor
    contributes exactly one signed pivot w0.  Unit pivots have Phi=0.  For an
    anchor pivot, the only positive-beta rows with nonzero E are signed rows in
    the same anchor fan, giving

        Phi = a/|G| * sum_w neg_l1(w-w0).

    The extra S* contribution comes from positive foreign coefficients of w0.
    """
    delta = delta_of_case(case, a)
    offsets = group_offsets(case)
    per_anchor = []
    for h, group in enumerate(case.groups):
        candidates = []
        for idx, w0 in enumerate(group):
            phi = sp.factor(a * sum(neg_l1_diff(w, w0) for w in group) / len(group))
            sstar = sp.factor(phi + a * pos_l1(w0))
            candidates.append(
                {
                    "row_index": offsets[h] + idx,
                    "phi": phi,
                    "sstar": sstar,
                    "ratio": sp.factor(phi / delta),
                }
            )
        candidates.sort(key=lambda c: (sp.Rational(c["ratio"]), c["row_index"]))
        per_anchor.append(candidates)
    chosen = [cands[0] for cands in per_anchor]
    basis = tuple(range(case.foreign)) + tuple(c["row_index"] for c in chosen)
    return {
        "basis": basis,
        "phi": sp.factor(max(c["phi"] for c in chosen)),
        "sstar": sp.factor(max(c["sstar"] for c in chosen)),
        "ratio": sp.factor(max(c["ratio"] for c in chosen)),
        "per_anchor_min": [qstr(c["ratio"]) for c in chosen],
    }


def exact_checks(case, L, B, a=A0):
    k = L.cols
    bl_ok = sp.simplify(B * L - sp.eye(k)) == sp.zeros(k, k)
    b1_ok = all(sp.factor(sum(B.row(i)) - 1) == 0 for i in range(k))
    rowsum_L_ok = all(sp.factor(sum(L.row(i)) - 1) == 0 for i in range(L.rows))
    rowsum_P_ok = b1_ok and rowsum_L_ok
    p2_via_bl = bl_ok
    delta = delta_of_case(case, a)
    direct_delta = max(row_neg(p_row(case, i, a)) for i in range(actual_rows_count(case)))
    return {
        "BL": bl_ok,
        "B1": b1_ok,
        "L_rowsum": rowsum_L_ok,
        "P2_via_BL": p2_via_bl,
        "rowsum": rowsum_P_ok,
        "delta_direct": direct_delta == delta,
        "delta": delta,
    }


def certify_case(case, a=A0):
    L, B, _ = build_LB(case, a)
    checks = exact_checks(case, L, B, a)
    if not all(v for key, v in checks.items() if key != "delta"):
        raise SystemExit(f"failed exact checks for {case.family} {case.params}: {checks}")
    if checks["delta"] > sp.Rational(1, 4):
        raise SystemExit(f"delta cap failed for {case.family} {case.params}: {checks['delta']}")
    reduced = reduced_bases(case)
    if case.certification == "certified_reduction" and not reduction_bound_ok(case, a):
        raise SystemExit(f"Hadamard reduction bound failed for {case.family} {case.params}")

    star = best_reduced_chart_metrics(case, a)
    ratio = sp.factor(star["ratio"])
    if case.expected_ratio is not None and ratio != case.expected_ratio:
        raise SystemExit(
            f"calibration mismatch for {case.family} {case.params}: "
            f"got {ratio}, expected {case.expected_ratio}"
        )

    note_bits = [
        f"star={list(star['basis'])}",
        f"Sstar/delta={qstr(star['sstar'] / checks['delta'])}",
        f"per_anchor_min={star['per_anchor_min']}",
        f"max_neg_shear={qstr(max_neg_shear(case))}",
        f"max_shear_norm_sq={qstr(max_shear_norm_sq(case))}",
        f"checks={{BL:{checks['BL']}, P2_via_BL:{checks['P2_via_BL']}, rowsum:{checks['rowsum']}, delta_direct:{checks['delta_direct']}}}",
    ]
    if case.certification == "certified_reduction":
        note_bits.insert(
            0,
            f"Hadamard reduction: theta class is all foreign units plus one signed row per anchor; "
            f"4*R2*a^2={qstr(4 * max_shear_norm_sq(case) * a * a)}<1/4",
        )
    else:
        note_bits.insert(
            0,
            "reduced theta charts checked only; omitted bases not certified",
        )
    return {
        "family": case.family,
        "params": case.params,
        "k": L.cols,
        "n_rows": L.rows,
        "delta": checks["delta"],
        "ratio": ratio,
        "certification": case.certification,
        "charts_checked": len(reduced),
        "notes": "; ".join(note_bits),
    }


def cases():
    out = []

    # A2 calibration: rank k=10 means one anchor and f=9 foreign coordinates.
    f = 9
    out.append(
        Case(
            "calibration_no_center_path",
            "a=1/100; rank_k=10; reproduces A2 k=10",
            1,
            f,
            (no_center_path_group(f),),
            "certified_reduction",
            sp.Rational(7, 4),
        )
    )

    for f in [5, 9, 13, 19]:
        out.append(
            Case(
                "one_anchor_star_edges",
                f"a=1/100; foreign={f}; center=0",
                1,
                f,
                (star_group(f, 0),),
                "certified_reduction",
            )
        )

    for f in [4, 6, 8, 10]:
        out.append(
            Case(
                "one_anchor_complete_edges",
                f"a=1/100; foreign={f}; all unordered edges with signs",
                1,
                f,
                (complete_group(f),),
                "certified_reduction",
            )
        )

    for left, right in [(3, 3), (4, 4), (5, 5)]:
        out.append(
            Case(
                "one_anchor_complete_bipartite_edges",
                f"a=1/100; K_{{{left},{right}}}",
                1,
                left + right,
                (complete_bipartite_group(left, right),),
                "certified_reduction",
            )
        )

    for f in [5, 8, 12]:
        out.append(
            Case(
                "two_anchor_overlapping_stars",
                f"a=1/100; foreign={f}; centers=0,{f - 1}; overlapping leaves",
                2,
                f,
                (star_group(f, 0), star_group(f, f - 1)),
                "certified_reduction",
            )
        )

    for f in [4, 6, 8]:
        out.append(
            Case(
                "two_anchor_complete_vs_star",
                f"a=1/100; foreign={f}; anchor0=complete; anchor1=star(center=0)",
                2,
                f,
                (complete_group(f), star_group(f, 0)),
                "certified_reduction",
            )
        )

    for f in [4, 6, 8, 10]:
        out.append(
            Case(
                "one_anchor_ternary_all",
                f"a=1/100; foreign={f}; all e_u+e_v-2e_t triples with signs",
                1,
                f,
                (ternary_all_group(f),),
                "certified_reduction",
            )
        )

    for f in [7, 11, 15]:
        out.append(
            Case(
                "one_anchor_cycle_skip_edges",
                f"a=1/100; foreign={f}; cycle edges plus skip-2 chords",
                1,
                f,
                (cycle_skip_group(f),),
                "certified_reduction",
            )
        )

    return out


def main():
    rows = []
    for case in cases():
        print(f"certifying {case.family} {case.params}", flush=True)
        row = certify_case(case)
        rows.append(row)
        print(f"  -> Phi/delta={qstr(row['ratio'])} charts={row['charts_checked']}", flush=True)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(
            [
                "family",
                "params",
                "k",
                "n_rows",
                "delta_exact",
                "phi_over_delta_exact",
                "phi_over_delta_float",
                "certification",
                "charts_checked",
                "notes",
            ]
        )
        w.writerow(
            [
                "# caveat",
                "all rows are L3 numerical evidence, not rigorous proof of (EX)",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "floats are decimal display only",
            ]
        )
        for row in rows:
            w.writerow(
                [
                    row["family"],
                    row["params"],
                    row["k"],
                    row["n_rows"],
                    qstr(row["delta"]),
                    qstr(row["ratio"]),
                    decstr(row["ratio"]),
                    row["certification"],
                    row["charts_checked"],
                    row["notes"],
                ]
            )

    for row in rows:
        print(
            "family={family} params={params} k={k} n={n_rows} delta={delta} "
            "Phi/delta={ratio} cert={certification} charts={charts_checked}".format(
                **{**row, "delta": qstr(row["delta"]), "ratio": qstr(row["ratio"])}
            )
        )
    print(f"wrote {OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
