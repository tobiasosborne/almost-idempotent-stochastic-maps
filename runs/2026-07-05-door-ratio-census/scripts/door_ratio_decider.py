#!/usr/bin/env python3
"""Wave 17b door-ratio decider.

All certified quantities are exact Fractions.  Floats are used only in printed
rankings and never in predicates.  This file writes a markdown report to stdout
and to ANSWER.md in the same scratch directory.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import combinations, islice, product
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[3]  # re-home patch: bundle sits one level deeper than waves-scratch
SCRATCH = Path(__file__).resolve().parent
WEB = ROOT / "runs/2026-07-02-web-regime-hunt/scripts"
EX_ENUM = ROOT / "runs/2026-07-02-ex-enumeration-rehome/scripts"

sys.path.insert(0, str(WEB))
import pipeline as pipe  # noqa: E402
import gen as webgen  # noqa: E402


def load_py(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


r3 = load_py(EX_ENUM / "rank3_explorer.py", "rank3_explorer_w17b")

ASSERTS: list[str] = []


def hard_assert(cond: bool, msg: str) -> None:
    if not cond:
        raise AssertionError(msg)
    ASSERTS.append(msg)


def pos(x: F) -> F:
    return x if x > 0 else F(0)


def neg(x: F) -> F:
    return -x if x < 0 else F(0)


def fstr(x: F | None) -> str:
    if x is None:
        return "NA"
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def ffloat(x: F | None) -> str:
    if x is None:
        return "NA"
    return f"{float(x):.8g}"


def matmul(A: list[list[F]], B: list[list[F]]) -> list[list[F]]:
    return [
        [sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))]
        for i in range(len(A))
    ]


def eye(n: int) -> list[list[F]]:
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def det3(M: list[list[F]]) -> F:
    return (
        M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1])
        - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
        + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0])
    )


def inv3(A: list[list[F]]) -> list[list[F]]:
    d = det3(A)
    if d == 0:
        raise ValueError("singular 3x3")
    cof = [
        [
            A[1][1] * A[2][2] - A[1][2] * A[2][1],
            -(A[1][0] * A[2][2] - A[1][2] * A[2][0]),
            A[1][0] * A[2][1] - A[1][1] * A[2][0],
        ],
        [
            -(A[0][1] * A[2][2] - A[0][2] * A[2][1]),
            A[0][0] * A[2][2] - A[0][2] * A[2][0],
            -(A[0][0] * A[2][1] - A[0][1] * A[2][0]),
        ],
        [
            A[0][1] * A[1][2] - A[0][2] * A[1][1],
            -(A[0][0] * A[1][2] - A[0][2] * A[1][0]),
            A[0][0] * A[1][1] - A[0][1] * A[1][0],
        ],
    ]
    return [[cof[j][i] / d for j in range(3)] for i in range(3)]


def row_times_mat(row: list[F], M: list[list[F]]) -> list[F]:
    return [sum(row[k] * M[k][j] for k in range(3)) for j in range(3)]


def coordinates(L: list[list[F]], U: tuple[int, int, int], i: int) -> tuple[F, F, F]:
    return tuple(row_times_mat(L[i], inv3([L[u] for u in U])))  # type: ignore[return-value]


def sp_matrix_to_frac(M) -> list[list[F]]:
    return [[F(str(M[i, j])) for j in range(M.cols)] for i in range(M.rows)]


def str_matrix_to_frac(M: list[list[str]]) -> list[list[F]]:
    return [[F(x) for x in row] for row in M]


def P_of(L: list[list[F]], B: list[list[F]], label: str) -> list[list[F]]:
    k = len(L[0])
    bl = matmul(B, L) == eye(k)
    P = matmul(L, B)
    ok, idem, rowsum = pipe.is_idempotent(P)
    hard_assert(bl and idem and rowsum and ok, f"{label}: B*L=I_{k}, P^2=P, and row sums=1 exactly")
    return P


def L_from_C(C: list[list[F]]) -> list[list[F]]:
    k = len(C[0])
    return eye(k) + C


@dataclass(frozen=True)
class Instance:
    label: str
    source: str
    L: list[list[F]]
    B: list[list[F]]


@dataclass(frozen=True)
class Chart:
    U: tuple[int, int, int]
    volume: F
    rel_volume: F
    coords: tuple[tuple[F, F, F], ...]
    phi_s: tuple[F, F, F]
    Phi: F
    sstar_s: tuple[F, F, F]
    sstar_max: F


@dataclass
class DoorRecord:
    label: str
    source: str
    n: int
    delta: F
    W: tuple[int, ...]
    H: F | None
    hidden_vertices: tuple[int, ...]
    top_vertices: tuple[int, ...]
    halo_cols: tuple[int, ...]
    v: int
    sigma_raw: F
    sigma_g: F
    numerator: F
    ratio: F | None
    argmins: tuple[tuple[int, int, int], ...]
    argmin_contains_v: bool
    zero_pivot_mass: F
    zero_pivot_fraction: F | None
    attaining_chart: tuple[int, int, int] | None
    attaining_pivot: int | None


def per_row_quantities(a: tuple[F, F, F], s: int) -> tuple[F, F, F, F, F]:
    lam = 1 - a[s]
    mu = sum(neg(a[t]) for t in range(3) if t != s)
    sigma = sum(pos(a[t]) for t in range(3) if t != s)
    E = pos(mu - lam)
    sstar_atom = sigma + 2 * neg(lam)
    return lam, mu, sigma, E, sstar_atom


def chart_data(L: list[list[F]], P: list[list[F]], delta: F, label: str) -> tuple[list[Chart], list[Chart]]:
    vols: dict[tuple[int, int, int], F] = {}
    for U in combinations(range(len(L)), 3):
        vol = abs(det3([L[u] for u in U]))
        if vol > 0:
            vols[U] = vol
    hard_assert(bool(vols), f"{label}: at least one actual-row basis")
    vmax = max(vols.values())
    charts: list[Chart] = []
    factor_checks = 0
    factor_failures: list[tuple[tuple[int, int, int], int, F, F, F]] = []
    for U, vol in sorted(vols.items()):
        coords = tuple(coordinates(L, U, i) for i in range(len(L)))
        phi: list[F] = []
        sstar: list[F] = []
        for s in range(3):
            ph = F(0)
            ss = F(0)
            for j, a in enumerate(coords):
                _lam, _mu, _sigma, E, atom = per_row_quantities(a, s)
                beta_pos = pos(P[U[s]][j])
                ph += beta_pos * E
                ss += beta_pos * atom
            phi.append(ph)
            sstar.append(ss)
            if 2 * vol >= vmax:
                factor_checks += 1
                bound = 2 * ph + 6 * delta
                if ss > bound:
                    factor_failures.append((U, s, ss, ph, bound))
        charts.append(
            Chart(
                U=U,
                volume=vol,
                rel_volume=vol / vmax,
                coords=coords,
                phi_s=(phi[0], phi[1], phi[2]),
                Phi=max(phi),
                sstar_s=(sstar[0], sstar[1], sstar[2]),
                sstar_max=max(sstar),
            )
        )
    hard_assert(not factor_failures, f"{label}: factorization holds on {factor_checks} theta chart-pivots")
    theta = [c for c in charts if 2 * c.volume >= vmax]
    hard_assert(bool(theta), f"{label}: theta-half chart set nonempty")
    best = min(c.Phi for c in theta)
    argmins = [c for c in theta if c.Phi == best]
    hard_assert(bool(argmins), f"{label}: theta-half Phi-argmin set nonempty")
    return charts, argmins


def kernel_geometry(P: list[list[F]], label: str) -> dict:
    d, negs = pipe.delta(P)
    if d == 0:
        return {"delta": d, "negs": negs, "W": [], "info": {}, "dists": [], "H": None}
    W, info = pipe.visible_set(P, d)
    if not W:
        return {"delta": d, "negs": negs, "W": [], "info": info, "dists": [], "H": None}
    dists = [pipe.dist1_to_conv(P, W, i)[0] for i in range(len(P))]
    hard_assert(all(x is not None for x in dists), f"{label}: every row has exact dist_1 to conv W")
    H = max(dists)
    hidden = tuple(i for i in range(len(P)) if info.get(i, {}).get("vertex") and not info.get(i, {}).get("exposed"))
    tops = tuple(i for i in hidden if dists[i] == H and H > 0)
    outside = tuple(j for j, dist in enumerate(dists) if dist is not None and dist > 0)
    halo = tuple(j for j, dist in enumerate(dists) if dist is not None and 16 * dist * dist >= d)
    sigma_raw = {
        v: sum(pos(P[v][j]) for j in outside)
        for v in range(len(P))
    }
    sigma_g = {
        v: sum(pos(P[v][j]) for j in halo)
        for v in range(len(P))
    }
    return {
        "delta": d,
        "negs": negs,
        "W": tuple(W),
        "info": info,
        "dists": tuple(dists),
        "H": H,
        "hidden": hidden,
        "tops": tops,
        "outside": outside,
        "halo": halo,
        "sigma_raw": sigma_raw,
        "sigma_g": sigma_g,
    }


def analyze_instance(inst: Instance) -> tuple[list[DoorRecord], dict]:
    P = P_of(inst.L, inst.B, inst.label)
    geom = kernel_geometry(P, inst.label)
    d = geom["delta"]
    stats = {
        "label": inst.label,
        "source": inst.source,
        "delta": d,
        "cap": d > 0 and d <= F(1, 4),
        "W_nonempty": bool(geom["W"]),
        "hidden_top_count": len(geom.get("tops", ())),
        "error": None,
    }
    if not stats["cap"] or not geom["W"] or geom["H"] is None:
        return [], stats
    if not geom["tops"]:
        return [], stats
    charts, argmins = chart_data(inst.L, P, d, inst.label)
    numerator = max(c.sstar_max for c in argmins)
    att_chart = None
    att_pivot = None
    for c in argmins:
        for s, val in enumerate(c.sstar_s):
            if val == numerator:
                att_chart = c.U
                att_pivot = s
                break
        if att_chart is not None:
            break
    H = geom["H"]
    assert H is not None
    out: list[DoorRecord] = []
    for v in geom["tops"]:
        sigma_g = geom["sigma_g"][v]
        denom = sigma_g * H
        ratio = numerator / denom if denom > 0 else None
        argmin_contains_v = any(v in c.U for c in argmins)
        zero_mass_best = F(0)
        zero_frac_best: F | None = None
        for c in argmins:
            zero_cols = [j for j in geom["halo"] if all(P[u][j] <= 0 for u in c.U)]
            zm = sum(pos(P[v][j]) for j in zero_cols)
            if zm > zero_mass_best:
                zero_mass_best = zm
        if sigma_g > 0:
            zero_frac_best = zero_mass_best / sigma_g
        out.append(
            DoorRecord(
                label=inst.label,
                source=inst.source,
                n=len(P),
                delta=d,
                W=geom["W"],
                H=H,
                hidden_vertices=geom["hidden"],
                top_vertices=geom["tops"],
                halo_cols=geom["halo"],
                v=v,
                sigma_raw=geom["sigma_raw"][v],
                sigma_g=sigma_g,
                numerator=numerator,
                ratio=ratio,
                argmins=tuple(c.U for c in argmins),
                argmin_contains_v=argmin_contains_v,
                zero_pivot_mass=zero_mass_best,
                zero_pivot_fraction=zero_frac_best,
                attaining_chart=att_chart,
                attaining_pivot=att_pivot,
            )
        )
    return out, stats


def build_s5_exact() -> list[list[F]]:
    return [
        [F(4000001, 4000000), F(-399, 8000000), F(-3603, 8000000), F(1801, 4000000), F(199, 4000000)],
        [F(1, 4000000), F(8001601, 8000000), F(-5603, 8000000), F(3801, 4000000), F(-1801, 4000000)],
        [F(1, 4000000), F(-2399, 8000000), F(7998397, 8000000), F(-199, 4000000), F(2199, 4000000)],
        [F(-1999, 4000000), F(1989, 40000), F(3801099, 4000000), F(0), F(1, 2000)],
        [F(-1999, 4000000), F(21999, 40000), F(1800099, 4000000), F(1, 2000), F(0)],
    ]


def calibrations() -> list[str]:
    lines: list[str] = []

    s5 = build_s5_exact()
    g = kernel_geometry(s5, "calibration:s5")
    hard_assert(g["delta"] == F(1841, 1600000), "calibration s5: delta=1841/1600000")
    hard_assert(g["H"] == F(1, 1000), "calibration s5: H=1/1000")
    hard_assert(g["W"] == (0, 1, 2), "calibration s5: W=(0,1,2)")
    hard_assert(g["hidden"] == (3, 4), "calibration s5: hidden=(3,4)")
    hard_assert(g["sigma_raw"][3] == F(1, 2000), "calibration s5: sigma_raw(row3)=1/2000")
    lines.append(
        f"- [T0] s5 calibration: delta={fstr(g['delta'])}, W={list(g['W'])}, "
        f"H={fstr(g['H'])}, sigma_raw(row3)={fstr(g['sigma_raw'][3])}, "
        f"sigma_g(row3)={fstr(g['sigma_g'][3])}."
    )

    p = F(1, 40)
    rho = F(1, 100)
    x = p / 3
    C = [[F(1, 2) - x, F(1, 2) + x + p, -p], [F(1, 2) + x, F(1, 2) - x + p, -p]]
    R2 = [[rho, rho], [rho, rho], [rho, rho]]
    P, _R, _C = webgen.build_from_LambdaC(C, R2)
    h = kernel_geometry(P, "calibration:web-headline")
    hard_assert(h["delta"] == F(49, 2000), "calibration web-headline: delta=49/2000")
    hard_assert(h["H"] == F(1, 20), "calibration web-headline: H=1/20")
    hard_assert(h["W"] == (0, 1, 2), "calibration web-headline: W=(0,1,2)")
    lines.append(
        f"- [T0] web-headline calibration: delta={fstr(h['delta'])}, W={list(h['W'])}, "
        f"H={fstr(h['H'])}, hidden tops={list(h['tops'])}."
    )

    C4 = [[F(28, 25), F(1, 200), F(0), F(-1, 8)]]
    R24 = [[F(-49, 800)], [F(-1, 6)], [F(-1, 8)], [F(-33, 800)]]
    P4, _R4, _C4 = webgen.build_from_LambdaC(C4, R24)
    c = kernel_geometry(P4, "calibration:sigma-halo-nonrobust")
    hit = [
        v for v in c["tops"]
        if c["sigma_raw"][v] == F(5343, 5000) and c["sigma_g"][v] == 0
    ]
    hard_assert(c["delta"] == F(252559, 1280000), "calibration sigma witness: delta=252559/1280000")
    hard_assert(bool(hit), "calibration sigma witness: hidden top with raw sigma=5343/5000 and sigma_g=0")
    lines.append(
        f"- [T0] sigma-halo calibration: delta={fstr(c['delta'])}, top={hit[0]}, "
        f"sigma_raw={fstr(c['sigma_raw'][hit[0]])}, sigma_g={fstr(c['sigma_g'][hit[0]])}."
    )
    return lines


def instances_from_rank3_suite() -> Iterable[Instance]:
    for inst in r3.mandatory_instances():
        yield Instance(inst.name, f"rank3_explorer:{inst.tag}", sp_matrix_to_frac(inst.L), sp_matrix_to_frac(inst.B))
    for inst in islice(r3.adversarial_instances(), 160):
        yield Instance(inst.name, f"rank3_explorer:{inst.tag}", sp_matrix_to_frac(inst.L), sp_matrix_to_frac(inst.B))
    for inst in r3.random_instances(60):
        yield Instance(inst.name, f"rank3_explorer:{inst.tag}", sp_matrix_to_frac(inst.L), sp_matrix_to_frac(inst.B))


def walk_dicts(obj):
    if isinstance(obj, dict):
        yield obj
        for val in obj.values():
            yield from walk_dicts(val)
    elif isinstance(obj, list):
        for val in obj:
            yield from walk_dicts(val)


def instances_from_json_bundles() -> Iterable[Instance]:
    paths = [
        ROOT / "runs/2026-07-04-b-amplifier-hunt/data/certified_points.json",
        ROOT / "runs/2026-07-04-small-delta-b-sweep/data/certified_points.json",
        ROOT / "runs/2026-07-05-nsc-zero-denominator-refuter/data/nsc_certificates.json",
        ROOT / "runs/2026-07-05-w16-clean-block-b/data/certified_points.json",
        ROOT / "runs/2026-07-05-w16-clean-block-b/data/identity_certificate.json",
    ]
    seen: set[tuple] = set()
    for path in paths:
        data = json.loads(path.read_text())
        for idx, d in enumerate(walk_dicts(data)):
            if "L" not in d:
                continue
            Bkey = "B_left" if "B_left" in d else ("B" if "B" in d else None)
            if Bkey is None:
                continue
            L = str_matrix_to_frac(d["L"])
            B = str_matrix_to_frac(d[Bkey])
            if not L or len(L[0]) != 3:
                continue
            if len(B) != 3:
                continue
            key = (tuple(tuple(r) for r in L), tuple(tuple(r) for r in B))
            if key in seen:
                continue
            seen.add(key)
            yield Instance(f"{path.parent.parent.name}:json:{idx}", f"json:{path.parent.parent.name}", L, B)


def instances_fresh_lambdac() -> Iterable[Instance]:
    # One hidden row: screened toward high self-mass.  Exact geometry decides if
    # it is still hidden and outside the tau/4 halo.
    vals = [F(-1, 4), F(-1, 6), F(-1, 8), F(0), F(1, 20), F(1, 10), F(1, 5), F(1, 3), F(1, 2), F(3, 4), F(1)]
    a_vals = [F(1, 100), F(1, 50), F(1, 25), F(1, 12), F(1, 8), F(1, 6), F(1, 4), F(1, 3)]
    emitted = 0
    emitted_by_a = {a: 0 for a in a_vals}
    for a in a_vals:
        patterns = [
            [1 + a, -a, 0],
            [1 + a, 0, -a],
            [-a, 1 + a, 0],
            [0, 1 + a, -a],
            [-a, 0, 1 + a],
            [0, -a, 1 + a],
        ]
        for C0 in patterns:
            for r0, r1, r2 in product(vals, repeat=3):
                C = [[F(x) for x in C0]]
                R2 = [[r0], [r1], [r2]]
                P, R, _C = webgen.build_from_LambdaC(C, R2)
                d, _ = pipe.delta(P)
                if d == 0 or d > F(1, 4):
                    continue
                if P[3][3] <= F(1, 2):
                    continue
                if emitted_by_a[a] >= 8:
                    continue
                yield Instance(f"fresh-one-hidden-a{fstr(a)}-{emitted}", "fresh:one-hidden-high-self", L_from_C(C), R)
                emitted += 1
                emitted_by_a[a] += 1
                if emitted >= 70:
                    return

    # Two hidden rows: include web-style and outside-coordinate pairs at several
    # dilution scales.
    count = 0
    for p in [F(1, 100), F(1, 80), F(1, 40), F(1, 20), F(1, 10)]:
        for xmul in [F(0), F(1, 4), F(1, 3), F(1, 2), F(1)]:
            x = xmul * p
            C = [[F(1, 2) - x, F(1, 2) + x + p, -p], [F(1, 2) + x, F(1, 2) - x + p, -p]]
            for rho in [F(1, 200), F(1, 100), F(1, 50), F(1, 20), F(1, 10), F(1, 5)]:
                R2 = [[rho, rho], [rho, rho], [rho, rho]]
                _P, R, _C = webgen.build_from_LambdaC(C, R2)
                yield Instance(f"fresh-web-p{fstr(p)}-x{xmul}-rho{fstr(rho)}", "fresh:web-pair", L_from_C(C), R)
                count += 1
    for a in [F(1, 50), F(1, 25), F(1, 12), F(1, 8), F(1, 6), F(1, 4)]:
        C_patterns = [
            [[1 + a, -a, 0], [0, 1 + a, -a]],
            [[1 + a, -a, 0], [-a, 1 + a, 0]],
            [[1 + a, 0, -a], [0, 1 + a, -a]],
        ]
        R_patterns = [
            [[F(1, 2), F(0)], [F(-1, 8), F(1, 2)], [F(0), F(-1, 8)]],
            [[F(3, 4), F(0)], [F(-1, 4), F(1, 2)], [F(0), F(-1, 4)]],
            [[F(1, 5), F(1, 10)], [F(1, 10), F(1, 5)], [F(-1, 8), F(-1, 8)]],
        ]
        for C in C_patterns:
            for R2 in R_patterns:
                _P, R, _C = webgen.build_from_LambdaC(C, R2)
                yield Instance(f"fresh-two-hidden-a{fstr(a)}-{count}", "fresh:two-hidden", L_from_C(C), R)
                count += 1


def unique_instances(instances: Iterable[Instance]) -> list[Instance]:
    out: list[Instance] = []
    seen: set[tuple] = set()
    for inst in instances:
        key = (tuple(tuple(r) for r in inst.L), tuple(tuple(r) for r in inst.B))
        if key in seen:
            continue
        seen.add(key)
        out.append(inst)
    return out


def topn(records: list[DoorRecord], key, n: int = 5) -> list[DoorRecord]:
    return sorted(records, key=key, reverse=True)[:n]


def row_for_record(r: DoorRecord) -> str:
    ratio = fstr(r.ratio) if r.ratio is not None else "undefined"
    ratio_float = ffloat(r.ratio) if r.ratio is not None else "NA"
    zero_frac = fstr(r.zero_pivot_fraction) if r.zero_pivot_fraction is not None else "NA"
    return (
        f"| `{r.label}` | {r.source} | {r.n} | {fstr(r.delta)} | {list(r.W)} | {fstr(r.H)} | "
        f"{r.v} | {fstr(r.sigma_raw)} | {fstr(r.sigma_g)} | {fstr(r.numerator)} | "
        f"{ratio} ({ratio_float}) | {list(r.argmins)} | {r.argmin_contains_v} | "
        f"{fstr(r.zero_pivot_mass)} / {zero_frac} |"
    )


def run() -> str:
    calib_lines = calibrations()

    insts = unique_instances(
        list(instances_from_rank3_suite())
        + list(instances_from_json_bundles())
        + list(instances_fresh_lambdac())
    )
    records: list[DoorRecord] = []
    stats: list[dict] = []
    errors: list[str] = []
    for inst in insts:
        try:
            recs, st = analyze_instance(inst)
            records.extend(recs)
            stats.append(st)
        except Exception as exc:
            errors.append(f"{inst.label}: {type(exc).__name__}: {exc}")

    cap_count = sum(1 for s in stats if s["cap"])
    W_count = sum(1 for s in stats if s["cap"] and s["W_nonempty"])
    hidden_inst_count = sum(1 for s in stats if s["cap"] and s["hidden_top_count"] > 0)
    hidden_top_count = len(records)
    high = [r for r in records if r.sigma_g > F(1, 2)]
    positive_halo = [r for r in records if r.sigma_g > 0]
    d3 = [r for r in records if r.argmin_contains_v]
    d5 = [r for r in records if r.zero_pivot_mass > 0]

    max_sigma = max(records, key=lambda r: (r.sigma_g, r.sigma_raw, r.H or F(0))) if records else None
    max_raw = max(records, key=lambda r: (r.sigma_raw, r.sigma_g, r.H or F(0))) if records else None
    min_ratio = min((r for r in high if r.ratio is not None), key=lambda r: r.ratio, default=None)
    min_pos_ratio = min((r for r in positive_halo if r.ratio is not None), key=lambda r: r.ratio, default=None)

    lines: list[str] = []
    lines.append("# Wave 17b Door-Ratio Decider Report")
    lines.append("")
    lines.append("Tier legend: T0 = exact local certificate or repo locus; T1 = exact computation from T0 definitions; T2 = search verdict/gap; T3 = speculation. No tracked files were edited; scratch only.")
    lines.append("")
    lines.append("## Rerun")
    lines.append("")
    lines.append("```bash")
    lines.append("python3 waves-scratch/w17b-door-ratio/door_ratio_decider.py")
    lines.append("```")
    lines.append("")
    lines.append("## Implemented Exact Predicates")
    lines.append("")
    lines.append("- [T0/T1] `W(P)` uses the repo exact LP pipeline: row vertices, admissible exposers, far rows by `dist_1^2 >= 16*delta`, and exposedness by `16*t*^2 >= delta`.")
    lines.append("- [T0/T1] `H` is exact `dist_1(row, conv W)` by rational LP.")
    lines.append("- [T0/T1] `sigma_g(v)` is the halo-robust invisible mass `sum_j max(P_vj,0)` over recipients with `dist_1(p_j,C_W) >= tau/4`, certified by `16*dist_j^2 >= delta`.")
    lines.append("- [T0/T1] theta-half charts are actual-row rank-3 bases with determinant volume at least half of maximum; `Phi_s` and `S*_s` follow `lem-factorization` verbatim.")
    lines.append("- [T1] Door ratio is `max_{theta-half Phi-argmin U, pivot s} S*_s(U)/(sigma_g(v)*H)` when the denominator is positive.")
    lines.append("")
    lines.append("## Calibration Hard Asserts")
    lines.append("")
    lines.extend(calib_lines)
    lines.append("")
    lines.append("## Census")
    lines.append("")
    lines.append(f"- [T1] rank-3 candidate instances loaded: `{len(insts)}`.")
    lines.append(f"- [T1] exact analyses completed: `{len(stats)}`; analysis errors/skips: `{len(errors)}`.")
    lines.append(f"- [T1] certified with `0 < delta <= 1/4`: `{cap_count}`.")
    lines.append(f"- [T1] certified with nonempty `W`: `{W_count}`.")
    lines.append(f"- [T1] certified instances with at least one hidden top vertex: `{hidden_inst_count}`.")
    lines.append(f"- [T1] certified hidden top vertices measured: `{hidden_top_count}`.")
    lines.append(f"- [T1] hidden top vertices with `sigma_g > 0`: `{len(positive_halo)}`.")
    lines.append(f"- [T1] hidden top vertices entering the D1 door regime `sigma_g > 1/2`: `{len(high)}`.")
    lines.append(f"- [T1] D3 chart-visibility failures (`Phi`-argmin contains hidden top): `{len(d3)}`.")
    lines.append(f"- [T1] D5 zero-pivot-visibility halo mass examples: `{len(d5)}`.")
    lines.append("")

    if max_sigma:
        lines.append("## Closest High-Halo Records")
        lines.append("")
        lines.append("| label | source | n | delta | W | H | v | sigma_raw | sigma_g | max S* | R_door | argmins | D3? | zero-pivot mass / fraction |")
        lines.append("|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---|---|---:|")
        for r in topn(records, key=lambda x: (x.sigma_g, x.sigma_raw, x.H or F(0)), n=8):
            lines.append(row_for_record(r))
        lines.append("")

    if min_pos_ratio:
        lines.append("## Smallest Positive-Halo Ratios")
        lines.append("")
        lines.append("| label | source | n | delta | W | H | v | sigma_raw | sigma_g | max S* | R_door | argmins | D3? | zero-pivot mass / fraction |")
        lines.append("|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---|---|---:|")
        for r in sorted((r for r in positive_halo if r.ratio is not None), key=lambda x: x.ratio)[:8]:
            lines.append(row_for_record(r))
        lines.append("")

    if d3:
        lines.append("## D3 Chart-Visibility Failure Certificates")
        lines.append("")
        lines.append("| label | source | n | delta | W | H | v | sigma_raw | sigma_g | max S* | R_door | argmins | D3? | zero-pivot mass / fraction |")
        lines.append("|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---|---|---:|")
        for r in topn(d3, key=lambda x: (x.sigma_g, x.H or F(0), x.sigma_raw), n=8):
            lines.append(row_for_record(r))
        lines.append("")

    if d5:
        lines.append("## D5 Zero-Pivot Visibility Certificates")
        lines.append("")
        lines.append("| label | source | n | delta | W | H | v | sigma_raw | sigma_g | max S* | R_door | argmins | D3? | zero-pivot mass / fraction |")
        lines.append("|---|---|---:|---:|---|---:|---:|---:|---:|---:|---:|---|---|---:|")
        for r in topn(d5, key=lambda x: (x.zero_pivot_fraction or F(0), x.zero_pivot_mass, x.sigma_g), n=8):
            lines.append(row_for_record(r))
        lines.append("")

    lines.append("## Verdict")
    lines.append("")
    if high and min_ratio is not None:
        lines.append(f"**[T2] DOOR SUPPORTED on this certified census, not proved.** The high-halo regime was entered `{len(high)}` times; the smallest certified high-regime ratio was `{fstr(min_ratio.ratio)}` on `{min_ratio.label}`.")
    else:
        lines.append("**[T2] REGIME-EMPTY-SO-FAR.** This run did not certify a single rank-3 hidden top vertex with `sigma_g > 1/2` under `delta <= 1/4`. This is not an emptiness theorem.")
    if max_sigma:
        lines.append(f"**[T1] Best certified halo mass was `sigma_g={fstr(max_sigma.sigma_g)}`** on `{max_sigma.label}` (raw sigma `{fstr(max_sigma.sigma_raw)}`, `H={fstr(max_sigma.H)}`).")
    if max_raw:
        lines.append(f"**[T1] Largest raw invisible mass was `sigma_raw={fstr(max_raw.sigma_raw)}`** on `{max_raw.label}`, but its halo mass was `sigma_g={fstr(max_raw.sigma_g)}`.")
    lines.append("**[T2] The door ratio itself is therefore undecided in the intended high-halo branch.** The search is informative mainly because the numerator machinery is easy to measure, while realizing the denominator condition `sigma_g>1/2` remains the bottleneck.")
    lines.append("")
    lines.append("## Hard Assert List")
    lines.append("")
    for msg in ASSERTS:
        lines.append(f"- {msg}")
    if errors:
        lines.append("")
        lines.append("## Non-Certified Errors")
        lines.append("")
        for e in errors[:20]:
            lines.append(f"- {e}")
        if len(errors) > 20:
            lines.append(f"- ... {len(errors) - 20} more")
    lines.append("")
    lines.append("## Next Experiment")
    lines.append("")
    lines.append("[T2] Replace broad family search with an exact feasibility/optimization loop for `sigma_g>1/2`: fix rank-3 `Lambda=[I;C]`, impose a candidate hidden-top/visible-set combinatorial type and `tau/4` halo membership, then solve for `R2` with linear constraints plus exact branch-and-bound on the quadratic threshold comparisons. The current brute-force grids mostly rediscover that high self-mass makes the row visible or leaves it inside the halo.")
    lines.append("")

    report = "\n".join(lines)
    (SCRATCH / "ANSWER.md").write_text(report + "\n")
    return report


if __name__ == "__main__":
    print(run())
