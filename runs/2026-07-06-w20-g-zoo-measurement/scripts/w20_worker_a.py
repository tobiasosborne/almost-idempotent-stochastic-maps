#!/usr/bin/env python3
"""W20 worker A: exact measurement of g = P*1_G across the certified zoo.

All certificate arithmetic is fractions.Fraction.  Floats appear only as
parenthetical intuition in the generated markdown report.
"""

from __future__ import annotations

import importlib.util
import math
import sys
from dataclasses import dataclass, field
from functools import cmp_to_key
from fractions import Fraction as F
from pathlib import Path
from typing import Callable, Iterable


sys.dont_write_bytecode = True

ROOT = Path(__file__).resolve().parents[3]
BUNDLE = Path(__file__).resolve().parents[1]
OUT = BUNDLE / "data" / "worker-a-report.md"
WEB = ROOT / "runs/2026-07-02-web-regime-hunt/scripts"
W19 = ROOT / "runs/2026-07-06-w19-sigma-frontier/scripts/w19_worker_a.py"
DOOR = ROOT / "runs/2026-07-05-door-ratio-census/scripts/door_ratio_decider.py"

sys.path.insert(0, str(WEB))

import gen as webgen  # noqa: E402
import pipeline as pipe  # noqa: E402


HALOS: tuple[F, ...] = (F(1, 4), F(1), F(2), F(4), F(5), F(6))
WORKABLE_HALOS: tuple[F, ...] = (F(4), F(5), F(6))
ASSERTS: list[str] = []
ASSERT_COUNTS: dict[str, int] = {"harmonicity": 0, "sandwich_rows": 0}


def load_py(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def hard_assert(cond: bool, msg: str, *, record: bool = True) -> None:
    if not cond:
        raise AssertionError(msg)
    if record:
        ASSERTS.append(msg)


def pos(x: F) -> F:
    return x if x > 0 else F(0)


def neg(x: F) -> F:
    return -x if x < 0 else F(0)


def fstr(x: F | None) -> str:
    if x is None:
        return "NA"
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def fq(x: F | None, digits: int = 8) -> str:
    if x is None:
        return "NA"
    return f"`{fstr(x)}` ({float(x):.{digits}g})"


def fl(x: float, digits: int = 8) -> str:
    return f"{x:.{digits}g}"


def alabel(a: F) -> str:
    return fstr(a)


def ratio_float(x: F, delta: F) -> float:
    return float(x) / math.sqrt(float(delta))


def ratio_expr(x: F, delta: F) -> str:
    return f"`{fstr(x)}/sqrt({fstr(delta)})` ({ratio_float(x, delta):.8g})"


def ratio_square_expr(x: F, delta: F) -> str:
    if x < 0:
        return f"-sqrt(`{fstr(x * x / delta)}`)"
    return f"sqrt(`{fstr(x * x / delta)}`)"


def cmp_ratio_values(x: F, dx: F, y: F, dy: F) -> int:
    """Compare x/sqrt(dx) with y/sqrt(dy), exactly."""
    if x == 0 and y == 0:
        return 0
    if x >= 0 and y < 0:
        return 1
    if x < 0 and y >= 0:
        return -1
    if x >= 0 and y >= 0:
        lhs = x * x * dy
        rhs = y * y * dx
        return (lhs > rhs) - (lhs < rhs)
    # Both are negative: -A/sqrt(dx) > -B/sqrt(dy) iff A/sqrt(dx) < B/sqrt(dy).
    lhs = x * x * dy
    rhs = y * y * dx
    return (lhs < rhs) - (lhs > rhs)


def mat_key(P: list[list[F]]) -> tuple[tuple[F, ...], ...]:
    return tuple(tuple(row) for row in P)


def mat_str(P: list[list[F]]) -> str:
    rows = []
    for row in P:
        rows.append("[" + ", ".join(f'"{fstr(x)}"' for x in row) + "]")
    return "[\n  " + ",\n  ".join(rows) + "\n]"


@dataclass(frozen=True)
class SourceInstance:
    label: str
    group: str
    source: str
    P: list[list[F]]


@dataclass
class SkipRecord:
    label: str
    group: str
    source: str
    reason: str


@dataclass
class Geometry:
    gid: str
    label: str
    group: str
    source: str
    P: list[list[F]]
    delta: F
    negs: tuple[F, ...]
    W: tuple[int, ...]
    info: dict
    dists: tuple[F, ...]
    H: F
    hidden_vertices: tuple[int, ...]
    top_vertices: tuple[int, ...]
    aliases: list[tuple[str, str, str]] = field(default_factory=list)

    @property
    def n(self) -> int:
        return len(self.P)


@dataclass
class Measurement:
    geom: Geometry
    a: F
    G: tuple[int, ...]
    band: tuple[int, ...]
    g: tuple[F, ...]
    sigma: tuple[F, ...]


@dataclass(frozen=True)
class RowHit:
    geom: Geometry
    a: F
    row: int
    value: F
    kind: str
    extra: str = ""


def certify_geometry(src: SourceInstance, gid: str) -> Geometry | SkipRecord:
    P = pipe.as_F(src.P)
    try:
        ok, idem, rowsum = pipe.is_idempotent(P)
        if not (ok and idem and rowsum):
            return SkipRecord(src.label, src.group, src.source, "not exact signed idempotent")
        d, negs = pipe.delta(P)
        if d == 0:
            return SkipRecord(src.label, src.group, src.source, "delta=0")
        if d > F(1, 4):
            return SkipRecord(src.label, src.group, src.source, f"delta>{fstr(F(1, 4))}: {fstr(d)}")
        W, info = pipe.visible_set(P, d)
        if not W:
            return SkipRecord(src.label, src.group, src.source, "W empty")
        dists_raw = [pipe.dist1_to_conv(P, W, i)[0] for i in range(len(P))]
        if any(x is None for x in dists_raw):
            return SkipRecord(src.label, src.group, src.source, "distance LP returned None")
        dists = tuple(x for x in dists_raw if x is not None)
        H = max(dists)
        hidden = tuple(
            i
            for i in range(len(P))
            if info.get(i, {}).get("vertex") and not info.get(i, {}).get("exposed")
        )
        tops = tuple(i for i in hidden if H > 0 and dists[i] == H)
        return Geometry(
            gid=gid,
            label=src.label,
            group=src.group,
            source=src.source,
            P=P,
            delta=d,
            negs=tuple(negs),
            W=tuple(W),
            info=info,
            dists=dists,
            H=H,
            hidden_vertices=hidden,
            top_vertices=tops,
            aliases=[(src.label, src.group, src.source)],
        )
    except Exception as exc:  # Broad by design: this is a harvest skip, not a theorem.
        return SkipRecord(src.label, src.group, src.source, f"analysis error: {type(exc).__name__}: {exc}")


def measure_g(geom: Geometry, a: F) -> Measurement:
    threshold = a * a * geom.delta
    G = tuple(j for j, dist in enumerate(geom.dists) if dist > 0 and dist * dist > threshold)
    band = tuple(j for j, dist in enumerate(geom.dists) if dist > 0 and dist * dist <= threshold)
    g = tuple(sum(geom.P[i][j] for j in G) for i in range(geom.n))
    sigma = tuple(sum(pos(geom.P[i][j]) for j in G) for i in range(geom.n))

    Pg = tuple(sum(geom.P[i][j] * g[j] for j in range(geom.n)) for i in range(geom.n))
    hard_assert(Pg == g, f"{geom.gid}/{geom.label} a={alabel(a)}: P*g == g exactly", record=False)
    ASSERT_COUNTS["harmonicity"] += 1
    for v in range(geom.n):
        hard_assert(
            sigma[v] - geom.negs[v] <= g[v] <= sigma[v],
            f"{geom.gid}/{geom.label} a={alabel(a)} row {v}: sigma-nu <= g <= sigma",
            record=False,
        )
        ASSERT_COUNTS["sandwich_rows"] += 1
    return Measurement(geom=geom, a=a, G=G, band=band, g=g, sigma=sigma)


def build_lambdac(C: list[list[F]], R2: list[list[F]]) -> list[list[F]]:
    P, _R, _C = webgen.build_from_LambdaC(C, R2)
    return P


def harvest_sources() -> tuple[list[SourceInstance], list[SkipRecord], dict[str, int]]:
    sources: list[SourceInstance] = []
    harvest_skips: list[SkipRecord] = []
    loaded_counts: dict[str, int] = {}

    def add(label: str, group: str, source: str, P: list[list[F]]) -> None:
        sources.append(SourceInstance(label=label, group=group, source=source, P=pipe.as_F(P)))
        loaded_counts[group] = loaded_counts.get(group, 0) + 1

    w19 = load_py(W19, "w19_worker_a_for_w20a")
    calibs = dict(w19.calibration_instances())
    add("w19_halo_nonrobust_witness", "W19", "w19_worker_a:calibration_sigma_halo_nonrobust", calibs["calibration_sigma_halo_nonrobust"]["P"])
    add("w19_rank3_genuine_partner", "W19", "w19_worker_a:rank3_genuine_partner", calibs["rank3_genuine_partner"]["P"])
    for m in (2, 4, 8):
        add(f"w19_duplicate_split_m{m}_q5_84", "W19", "w19_worker_a:duplicate_split_instance(q=5/84)", w19.duplicate_split_instance(m, F(5, 84))["P"])
    add("w19_duplicate_split_m2_q1_16_absorption", "W19", "w19_worker_a:duplicate_split_instance(q=1/16)", w19.duplicate_split_instance(2, F(1, 16))["P"])
    add("w19_rank5_genuine_self", "W19", "w19_worker_a:rank5_genuine_self", w19.rank5_genuine_self()["P"])
    relaxed_P, _relaxed_mass = w19.solve_relaxed_cycle_lp()
    add("w19_rank3_relaxed_cycle_lp_optimizer", "W19", "w19_worker_a:solve_relaxed_cycle_lp", relaxed_P)

    cap_instances = {
        "sigma_cap_A_max_genuine_self": (
            [[F(-3, 80), F(23, 400), F(5, 12), F(-1, 200), F(341, 600)]],
            [[F(3, 80)], [F(1, 100)], [F(1, 16)], [F(1, 96)], [F(7, 80)]],
            "certify_best.py:A_C/A_R2",
        ),
        "sigma_cap_B_maxH_genuine_partner": (
            [[F(1, 2), F(-1, 20), F(11, 20)], [F(257, 400), F(-7, 200), F(157, 400)]],
            [[F(9, 200), F(1, 80)], [F(1, 200), F(1, 200)], [F(11, 160), F(1, 100)]],
            "certify_best.py:B_C/B_R2",
        ),
        "sigma_cap_C_halo_nonrobust_selfmass": (
            [[F(28, 25), F(1, 200), F(0), F(-1, 8)]],
            [[F(-49, 800)], [F(-1, 6)], [F(-1, 8)], [F(-33, 800)]],
            "halo_bound_check.py:C_selfmass",
        ),
    }
    for label, (C, R2, source) in cap_instances.items():
        add(label, "sigma-cap-refuter", source, build_lambdac(C, R2))

    door = load_py(DOOR, "door_ratio_decider_for_w20a")
    add("web_regime_s5_calibration", "web-regime-hunt", "calibrate_s5.py:build_s5_exact", door.build_s5_exact())
    p = F(1, 40)
    rho = F(1, 100)
    x = p / 3
    C = [[F(1, 2) - x, F(1, 2) + x + p, -p], [F(1, 2) + x, F(1, 2) - x + p, -p]]
    R2 = [[rho, rho], [rho, rho], [rho, rho]]
    add("web_regime_headline_delta_49_2000", "web-regime-hunt", "verify_instance.py generator", build_lambdac(C, R2))

    door_raw = []
    door_funcs: list[tuple[str, Callable[[], Iterable]]] = [
        ("instances_from_rank3_suite", door.instances_from_rank3_suite),
        ("instances_from_json_bundles", door.instances_from_json_bundles),
        ("instances_fresh_lambdac", door.instances_fresh_lambdac),
    ]
    for fname, fn in door_funcs:
        try:
            items = list(fn())
            door_raw.extend(items)
            loaded_counts[f"door:{fname}:raw"] = len(items)
        except Exception as exc:
            harvest_skips.append(SkipRecord(fname, "door-ratio census", fname, f"harvest error: {type(exc).__name__}: {exc}"))
    try:
        door_unique = door.unique_instances(door_raw)
    except Exception as exc:
        door_unique = []
        harvest_skips.append(SkipRecord("unique_instances", "door-ratio census", "door_ratio_decider.py", f"dedupe error: {type(exc).__name__}: {exc}"))
    loaded_counts["door-ratio census"] = len(door_unique)
    for inst in door_unique:
        try:
            P = door.P_of(inst.L, inst.B, inst.label)
            sources.append(SourceInstance(label=f"door_{inst.label}", group="door-ratio census", source=inst.source, P=pipe.as_F(P)))
        except Exception as exc:
            harvest_skips.append(SkipRecord(inst.label, "door-ratio census", inst.source, f"P construction error: {type(exc).__name__}: {exc}"))

    return sources, harvest_skips, loaded_counts


def certify_and_deduplicate(sources: list[SourceInstance], harvest_skips: list[SkipRecord]) -> tuple[list[Geometry], list[SourceInstance], list[SkipRecord]]:
    geoms: list[Geometry] = []
    covered_sources: list[SourceInstance] = []
    skips = list(harvest_skips)
    by_key: dict[tuple[tuple[F, ...], ...], Geometry] = {}
    next_id = 1
    for src in sources:
        maybe = certify_geometry(src, f"I{next_id:03d}")
        if isinstance(maybe, SkipRecord):
            skips.append(maybe)
            continue
        covered_sources.append(src)
        key = mat_key(maybe.P)
        if key in by_key:
            by_key[key].aliases.extend(maybe.aliases)
        else:
            maybe.gid = f"I{next_id:03d}"
            by_key[key] = maybe
            geoms.append(maybe)
            next_id += 1
    return geoms, covered_sources, skips


def all_measurements(geoms: list[Geometry]) -> dict[tuple[str, F], Measurement]:
    out: dict[tuple[str, F], Measurement] = {}
    for geom in geoms:
        for a in HALOS:
            out[(geom.gid, a)] = measure_g(geom, a)
    return out


def hidden_top_sigma_at(meas: Measurement, row: int) -> F:
    return meas.sigma[row]


def run_calibration_asserts(geoms: list[Geometry], measurements: dict[tuple[str, F], Measurement]) -> None:
    by_alias: dict[str, Geometry] = {}
    for geom in geoms:
        for label, _group, _source in geom.aliases:
            by_alias[label] = geom

    c = by_alias["w19_halo_nonrobust_witness"]
    m = measurements[(c.gid, F(1, 4))]
    hard_assert(c.delta == F(252559, 1280000), "calibration halo-nonrobust: delta=252559/1280000")
    hard_assert(bool(c.top_vertices), "calibration halo-nonrobust: has a hidden top")
    hard_assert(any(hidden_top_sigma_at(m, v) == 0 for v in c.top_vertices), "calibration halo-nonrobust: sigma_g=0 at a hidden top")

    r3 = by_alias["w19_rank3_genuine_partner"]
    m = measurements[(r3.gid, F(1, 4))]
    hard_assert(r3.delta == F(74551, 1600000), "rank-3 genuine partner: delta=74551/1600000")
    hard_assert(3 in r3.top_vertices, "rank-3 genuine partner: row 3 is a hidden top")
    hard_assert(m.sigma[3] == F(229, 3200), "rank-3 genuine partner: sigma_g(row 3)=229/3200")

    r5 = by_alias["w19_rank5_genuine_self"]
    m = measurements[(r5.gid, F(1, 4))]
    hard_assert(r5.delta == F(3983, 96000), "rank-5 genuine self: delta=3983/96000")
    hard_assert(5 in r5.top_vertices, "rank-5 genuine self: row 5 is a hidden top")
    hard_assert(m.sigma[5] == F(5991, 80000), "rank-5 genuine self: sigma_g(row 5)=5991/80000")

    for split_m in (2, 4, 8):
        g = by_alias[f"w19_duplicate_split_m{split_m}_q5_84"]
        m = measurements[(g.gid, F(1, 4))]
        hard_assert(g.delta == F(1, 16), f"duplicate split m={split_m}: delta=1/16")
        hard_assert(g.H == F(1, 10), f"duplicate split m={split_m}: H=1/10")
        hard_assert(bool(g.top_vertices), f"duplicate split m={split_m}: hidden tops nonempty")
        hard_assert(all(m.sigma[v] == F(5, 84) for v in g.top_vertices), f"duplicate split m={split_m}: each hidden top sigma_g=5/84")


def rowhit_cmp_ratio(a: RowHit, b: RowHit) -> int:
    return cmp_ratio_values(a.value, a.geom.delta, b.value, b.geom.delta)


def sort_ratio_desc(rows: list[RowHit]) -> list[RowHit]:
    return sorted(rows, key=cmp_to_key(lambda x, y: -rowhit_cmp_ratio(x, y)))


def max_by_value(rows: list[RowHit]) -> RowHit | None:
    return max(rows, key=lambda r: r.value, default=None)


def min_by_value(rows: list[RowHit]) -> RowHit | None:
    return min(rows, key=lambda r: r.value, default=None)


def row_loc(hit: RowHit | None) -> str:
    if hit is None:
        return "NA"
    aliases = "; ".join(f"{lab} [{grp}]" for lab, grp, _src in hit.geom.aliases[:3])
    more = "" if len(hit.geom.aliases) <= 3 else f"; +{len(hit.geom.aliases) - 3} aliases"
    return f"`{hit.geom.gid}` row `{hit.row}` ({aliases}{more})"


def value_cell(hit: RowHit | None) -> str:
    if hit is None:
        return "NA"
    return fq(hit.value)


def ratio_cell(hit: RowHit | None) -> str:
    if hit is None:
        return "NA"
    return ratio_expr(hit.value, hit.geom.delta)


def measurement_rows_for_a(geoms: list[Geometry], measurements: dict[tuple[str, F], Measurement], a: F) -> dict[str, list[RowHit]]:
    visible: list[RowHit] = []
    band: list[RowHit] = []
    hidden_tops: list[RowHit] = []
    global_rows: list[RowHit] = []
    hidden_sigma: list[RowHit] = []
    hidden_gap: list[RowHit] = []
    for geom in geoms:
        meas = measurements[(geom.gid, a)]
        for w in geom.W:
            visible.append(RowHit(geom, a, w, meas.g[w], "visible-g"))
        for j in meas.band:
            band.append(RowHit(geom, a, j, meas.g[j], "band-g"))
        for i in range(geom.n):
            global_rows.append(RowHit(geom, a, i, meas.g[i], "global-g"))
        for v in geom.top_vertices:
            hidden_tops.append(RowHit(geom, a, v, meas.g[v], "hidden-top-g"))
            hidden_sigma.append(RowHit(geom, a, v, meas.sigma[v], "hidden-top-sigma"))
            hidden_gap.append(RowHit(geom, a, v, meas.sigma[v] - meas.g[v], "hidden-top-gap"))
    return {
        "visible": visible,
        "band": band,
        "hidden_tops": hidden_tops,
        "global": global_rows,
        "hidden_sigma": hidden_sigma,
        "hidden_gap": hidden_gap,
    }


def table_top_visible_ratio(rows: list[RowHit], limit: int = 5) -> list[str]:
    lines = [
        "| rank | a | instance | row | g_w | g_w/tau | (g_w/tau)^2 exact | aliases |",
        "|---:|---:|---|---:|---:|---:|---:|---|",
    ]
    for rank, hit in enumerate(sort_ratio_desc(rows)[:limit], start=1):
        aliases = "; ".join(f"{lab} [{grp}]" for lab, grp, _src in hit.geom.aliases[:4])
        if len(hit.geom.aliases) > 4:
            aliases += f"; +{len(hit.geom.aliases) - 4}"
        lines.append(
            f"| {rank} | {alabel(hit.a)} | `{hit.geom.gid}` | {hit.row} | {fq(hit.value)} | "
            f"{ratio_expr(hit.value, hit.geom.delta)} | {ratio_square_expr(hit.value, hit.geom.delta)} | {aliases} |"
        )
    if len(lines) == 2:
        lines.append("| NA | NA | NA | NA | NA | NA | NA | NA |")
    return lines


def row_table(hits: list[RowHit], value_name: str, limit: int = 8) -> list[str]:
    lines = [
        f"| rank | a | instance | row | {value_name} | aliases |",
        "|---:|---:|---|---:|---:|---|",
    ]
    for rank, hit in enumerate(hits[:limit], start=1):
        aliases = "; ".join(f"{lab} [{grp}]" for lab, grp, _src in hit.geom.aliases[:3])
        if len(hit.geom.aliases) > 3:
            aliases += f"; +{len(hit.geom.aliases) - 3}"
        lines.append(f"| {rank} | {alabel(hit.a)} | `{hit.geom.gid}` | {hit.row} | {fq(hit.value)} | {aliases} |")
    if len(lines) == 2:
        lines.append("| NA | NA | NA | NA | NA | NA |")
    return lines


def hidden_comparison_table(hits: list[RowHit], measurements: dict[tuple[str, F], Measurement], limit: int = 10) -> list[str]:
    lines = [
        "| rank | a | instance | top row | g_v | sigma_g(v) | sigma-g gap | nu_v | aliases |",
        "|---:|---:|---|---:|---:|---:|---:|---:|---|",
    ]
    for rank, hit in enumerate(hits[:limit], start=1):
        meas = measurements[(hit.geom.gid, hit.a)]
        v = hit.row
        aliases = "; ".join(f"{lab} [{grp}]" for lab, grp, _src in hit.geom.aliases[:3])
        if len(hit.geom.aliases) > 3:
            aliases += f"; +{len(hit.geom.aliases) - 3}"
        lines.append(
            f"| {rank} | {alabel(hit.a)} | `{hit.geom.gid}` | {v} | {fq(meas.g[v])} | "
            f"{fq(meas.sigma[v])} | {fq(meas.sigma[v] - meas.g[v])} | {fq(hit.geom.negs[v])} | {aliases} |"
        )
    if len(lines) == 2:
        lines.append("| NA | NA | NA | NA | NA | NA | NA | NA | NA |")
    return lines


def group_counts(items: Iterable, key_fn: Callable) -> dict[str, int]:
    out: dict[str, int] = {}
    for item in items:
        k = key_fn(item)
        out[k] = out.get(k, 0) + 1
    return out


def build_report(
    geoms: list[Geometry],
    covered_sources: list[SourceInstance],
    skips: list[SkipRecord],
    loaded_counts: dict[str, int],
    measurements: dict[tuple[str, F], Measurement],
) -> str:
    per_a = {a: measurement_rows_for_a(geoms, measurements, a) for a in HALOS}

    all_workable_visible: list[RowHit] = []
    for a in WORKABLE_HALOS:
        all_workable_visible.extend(per_a[a]["visible"])
    workable_top = sort_ratio_desc(all_workable_visible)[0] if all_workable_visible else None

    k2_hits: list[RowHit] = []
    for a in WORKABLE_HALOS:
        k2_hits.extend(hit for hit in per_a[a]["band"] if hit.value >= F(1, 2))

    any_global_half: list[RowHit] = []
    for a in HALOS:
        any_global_half.extend(hit for hit in per_a[a]["global"] if hit.value >= F(1, 2))

    if k2_hits:
        verdict = f"KILL-K2-REALIZED (band row g={fstr(max_by_value(k2_hits).value)} at a={alabel(max_by_value(k2_hits).a)})"
    else:
        top = workable_top
        assert top is not None
        verdict = f"LEMMA-A-SUPPORTED (sup g_w/tau = {ratio_float(top.value, top.geom.delta):.8g} at a={alabel(top.a)})"

    headline_geoms: dict[str, Geometry] = {}
    for a in HALOS:
        rows = per_a[a]
        for hit in [
            max_by_value(rows["visible"]),
            sort_ratio_desc(rows["visible"])[0] if rows["visible"] else None,
            min_by_value(rows["visible"]),
            max_by_value(rows["band"]),
            max_by_value(rows["global"]),
            max_by_value(rows["hidden_sigma"]),
            max_by_value(rows["hidden_gap"]),
        ]:
            if hit is not None:
                headline_geoms[hit.geom.gid] = hit.geom
    for hit in sort_ratio_desc(all_workable_visible)[:5]:
        headline_geoms[hit.geom.gid] = hit.geom
    for hit in k2_hits[:5] + any_global_half[:5]:
        headline_geoms[hit.geom.gid] = hit.geom
    for geom in geoms:
        if any(label.startswith("w19_") or label.startswith("sigma_cap_") or label.startswith("web_regime_") for label, _grp, _src in geom.aliases):
            headline_geoms[geom.gid] = geom

    lines: list[str] = []
    lines.append(verdict)
    lines.append("")
    lines.append("# W20 Worker A — exact g-zoo measurement")
    lines.append("")
    lines.append("Tier legend: [T0] repo definition/banked pipeline fact; [T1] exact computation, hard-asserted; [T2] structured read/non-realization; [T3] heuristic.")
    lines.append("")
    lines.append("## Rerun")
    lines.append("")
    lines.append("```bash")
    lines.append("python3 runs/2026-07-06-w20-g-zoo-measurement/scripts/w20_worker_a.py")
    lines.append("```")
    lines.append("")
    lines.append("## Implemented exact predicates")
    lines.append("")
    lines.append("- [T0/T1] `W(P)`, row vertices, exposedness, and `dist_1(row,conv W)` are computed with the banked exact `pipeline.py` LP routines.")
    lines.append("- [T1] For halo width `a`, `G_a={j: d_j>a*tau}` is decided by the exact strict predicate `d_j>0 and d_j^2>a^2*delta`.")
    lines.append("- [T1] `g=P*1_G` and `sigma_g(v)=sum_{j in G} max(P_vj,0)` are exact rational row sums.")
    lines.append("- [T1] Every measured `(instance,a)` hard-asserts `P*g=g` and `sigma_g(v)-nu_v <= g_v <= sigma_g(v)` for every row.")
    lines.append("")

    lines.append("## Coverage")
    lines.append("")
    lines.append(f"- [T1] Source entries attempted after construction: `{len(covered_sources) + len(skips)}`; raw loader counts `{loaded_counts}`.")
    lines.append(f"- [T1] Covered qualifying source entries (`0<delta<=1/4`, `W!=empty`): `{len(covered_sources)}`.")
    lines.append(f"- [T1] Unique exact matrices measured after de-duplication: `{len(geoms)}`.")
    lines.append(f"- [T1] Exact `(unique matrix, halo width)` measurements: `{len(geoms) * len(HALOS)}`.")
    covered_by_group = group_counts(covered_sources, lambda s: s.group)
    skipped_by_group = group_counts(skips, lambda s: s.group)
    lines.append(f"- [T1] Covered by group: `{covered_by_group}`.")
    lines.append(f"- [T1/T2] Skipped/not qualifying by group: `{skipped_by_group}`. These are not silent skips; reasons are listed below.")
    lines.append("")
    lines.append("Covered source entries:")
    lines.append("")
    lines.append("| group | count |")
    lines.append("|---|---:|")
    for group, count in sorted(covered_by_group.items()):
        lines.append(f"| {group} | {count} |")
    lines.append("")
    lines.append("Skipped or non-qualifying source entries:")
    lines.append("")
    lines.append("| group | label | reason |")
    lines.append("|---|---|---|")
    if skips:
        for s in skips:
            lines.append(f"| {s.group} | `{s.label}` | {s.reason} |")
    else:
        lines.append("| NA | NA | NA |")
    lines.append("")
    lines.append("Covered labels by unique measured matrix:")
    lines.append("")
    lines.append("| id | n | delta | H | W | hidden tops | aliases |")
    lines.append("|---|---:|---:|---:|---|---|---|")
    for geom in geoms:
        aliases = "; ".join(f"{lab} [{grp}]" for lab, grp, _src in geom.aliases)
        lines.append(
            f"| `{geom.gid}` | {geom.n} | {fq(geom.delta)} | {fq(geom.H)} | {list(geom.W)} | "
            f"{list(geom.top_vertices)} | {aliases} |"
        )
    lines.append("")

    lines.append("## Aggregate tables per halo width")
    lines.append("")
    lines.append("| a | |G_a| max | visible max g_w | visible max g_w/tau | visible min g_w | band max g | global max g | any global g>=1/2? |")
    lines.append("|---:|---:|---:|---:|---:|---:|---:|---|")
    for a in HALOS:
        rows = per_a[a]
        max_G = max(len(measurements[(geom.gid, a)].G) for geom in geoms) if geoms else 0
        vis_max = max_by_value(rows["visible"])
        vis_ratio = sort_ratio_desc(rows["visible"])[0] if rows["visible"] else None
        vis_min = min_by_value(rows["visible"])
        band_max = max_by_value(rows["band"])
        glob_max = max_by_value(rows["global"])
        global_half = any(hit.value >= F(1, 2) for hit in rows["global"])
        lines.append(
            f"| {alabel(a)} | {max_G} | {value_cell(vis_max)} at {row_loc(vis_max)} | "
            f"{ratio_cell(vis_ratio)} at {row_loc(vis_ratio)} | {value_cell(vis_min)} at {row_loc(vis_min)} | "
            f"{value_cell(band_max)} at {row_loc(band_max)} | {value_cell(glob_max)} at {row_loc(glob_max)} | {global_half} |"
        )
    lines.append("")

    lines.append("## Lemma-A empirical test: visible rows")
    lines.append("")
    lines.append("[T1] Top visible-row values of `g_w/tau`; exact ordering used square comparisons, floats are display only.")
    lines.append("")
    lines.extend(table_top_visible_ratio([hit for a in HALOS for hit in per_a[a]["visible"]], limit=10))
    lines.append("")
    lines.append("[T1/T2] Workable halo widths `a in {4,5,6}` only:")
    lines.append("")
    lines.extend(table_top_visible_ratio(all_workable_visible, limit=5))
    lines.append("")

    lines.append("## Band rows")
    lines.append("")
    lines.append("[T1] Rows in the band satisfy `0<d_j<=a*tau`, i.e. `d_j^2<=a^2*delta` with positive distance.")
    lines.append("")
    lines.extend(row_table([max_by_value(per_a[a]["band"]) for a in HALOS if max_by_value(per_a[a]["band"]) is not None], "max band g", limit=12))
    lines.append("")

    lines.append("## Hidden tops")
    lines.append("")
    lines.append("[T1] Hidden-top comparison uses the signed `g_v`, the positive companion `sigma_g(v)`, and the exact gap `sigma_g(v)-g_v` (negative mass on `G_a`, bounded by `nu_v`).")
    lines.append("")
    for a in HALOS:
        lines.append(f"### a = {alabel(a)}")
        lines.append("")
        hidden_by_sigma = sorted(per_a[a]["hidden_sigma"], key=lambda h: h.value, reverse=True)
        lines.extend(hidden_comparison_table(hidden_by_sigma, measurements, limit=8))
        lines.append("")

    lines.append("## Global g>=1/2 scan")
    lines.append("")
    if any_global_half:
        lines.append(f"- [T1] Rows with `g>=1/2` were found: `{len(any_global_half)}`.")
        lines.extend(row_table(sorted(any_global_half, key=lambda h: h.value, reverse=True), "g", limit=12))
    else:
        lines.append("- [T1/T2] No measured row in the covered zoo reached `g>=1/2` at any requested halo width. This is not an emptiness theorem.")
    lines.append("")

    lines.append("## Kill scan")
    lines.append("")
    if workable_top is not None:
        lines.append(
            f"- [T1/T2] K1 nearest miss: max visible `g_w/tau` for `a in {{4,5,6}}` is "
            f"{ratio_expr(workable_top.value, workable_top.geom.delta)} at `{workable_top.geom.gid}` row `{workable_top.row}`, a={alabel(workable_top.a)}."
        )
    if k2_hits:
        best_k2 = max_by_value(k2_hits)
        assert best_k2 is not None
        local_visible = sort_ratio_desc([h for h in per_a[best_k2.a]["visible"] if h.geom.gid == best_k2.geom.gid])
        local_vis = local_visible[0] if local_visible else None
        lines.append(
            f"- [T1] K2 realized candidate: band row `{best_k2.row}` in `{best_k2.geom.gid}` has "
            f"`g={fstr(best_k2.value)}` at a={alabel(best_k2.a)}; local visible max is {ratio_cell(local_vis)}."
        )
    else:
        all_band = [hit for a in WORKABLE_HALOS for hit in per_a[a]["band"]]
        nearest = max_by_value(all_band)
        if nearest is not None:
            local_visible = sort_ratio_desc([h for h in per_a[nearest.a]["visible"] if h.geom.gid == nearest.geom.gid])
            local_vis = local_visible[0] if local_visible else None
            lines.append(
                f"- [T1/T2] K2 nearest miss: max band `g` for `a in {{4,5,6}}` is {fq(nearest.value)} "
                f"at `{nearest.geom.gid}` row `{nearest.row}`, a={alabel(nearest.a)}, margin to `1/2` is {fq(F(1, 2) - nearest.value)}; "
                f"local visible max is {ratio_cell(local_vis)}."
            )
        else:
            lines.append("- [T1/T2] K2 nearest miss: no positive-distance band rows existed at `a in {4,5,6}` in the covered zoo.")
    lines.append("- [T2] No failed search is being promoted to an emptiness claim; the statement is only about this harvested certified zoo.")
    lines.append("")

    lines.append("## Calibration hard asserts")
    lines.append("")
    lines.append(f"- [T1] Harmonicity asserts passed: `{ASSERT_COUNTS['harmonicity']}` exact `(instance,a)` checks.")
    lines.append(f"- [T1] Sandwich asserts passed: `{ASSERT_COUNTS['sandwich_rows']}` exact row checks.")
    for msg in ASSERTS:
        lines.append(f"- [T1] {msg}")
    lines.append("")

    lines.append("## Headline/extreme matrices")
    lines.append("")
    lines.append("[T1] Full exact `P` matrices for every headline/extreme instance referenced above.")
    lines.append("")
    for gid in sorted(headline_geoms):
        geom = headline_geoms[gid]
        lines.append(f"### {geom.gid}: {geom.label}")
        lines.append("")
        aliases = "; ".join(f"{lab} [{grp}; {src}]" for lab, grp, src in geom.aliases)
        lines.append(f"- aliases: {aliases}")
        lines.append(f"- delta={fstr(geom.delta)}, H={fstr(geom.H)}, W={list(geom.W)}, hidden_tops={list(geom.top_vertices)}")
        lines.append("")
        lines.append("```python")
        lines.append(mat_str(geom.P))
        lines.append("```")
        lines.append("")

    return "\n".join(lines) + "\n"


def main() -> None:
    sources, harvest_skips, loaded_counts = harvest_sources()
    geoms, covered_sources, skips = certify_and_deduplicate(sources, harvest_skips)
    measurements = all_measurements(geoms)
    run_calibration_asserts(geoms, measurements)
    report = build_report(geoms, covered_sources, skips, loaded_counts, measurements)
    OUT.write_text(report)
    print(report)


if __name__ == "__main__":
    main()
