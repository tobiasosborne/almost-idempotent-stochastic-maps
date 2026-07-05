#!/usr/bin/env python3
"""Wave 16b exact-rational D_J/B floor decider.

This is a scratch worker artifact.  It writes only under
waves-scratch/w16b-dj-floor/.  It proves no theorem; it certifies exact
instances and records the remaining floor question honestly.
"""

from __future__ import annotations

import csv
import json
import sys
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRATCH = ROOT / "waves-scratch" / "w16b-dj-floor"
DATA = ROOT / "runs" / "2026-07-05-w16-clean-block-b" / "data" / "certified_points.json"
RUN_SCRIPTS = ROOT / "runs" / "2026-07-05-w16-clean-block-b" / "scripts"
sys.path.insert(0, str(RUN_SCRIPTS))

import w16_b_restricted as w  # noqa: E402


CSV_OUT = SCRATCH / "floor_table.csv"
JSON_OUT = SCRATCH / "floor_certificates.json"
REPORT_OUT = SCRATCH / "REPORT.md"


def fstr(x: F) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def parse_matrix(rows: list[list[str]]) -> list[list[F]]:
    return [[F(x) for x in row] for row in rows]


def direct_fe_identity(
    P: list[list[F]],
    coords: tuple[tuple[F, F, F], ...],
    U: tuple[int, int, int],
    r: int,
    s: int,
) -> dict:
    beta = P[U[r]]
    x = [coords[i][s] for i in range(len(P))]
    xpos = [w.pos(v) for v in x]
    W = [w.neg(v) for v in x]
    J = [i for i in range(len(P)) if beta[i] > 0 and x[i] < 0]

    Bmass = sum(beta[i] * W[i] for i in J)
    assert Bmass == w.B_mass(P, coords, U, r, s)

    for i in J:
        assert x[i] == sum(P[i][k] * x[k] for k in range(len(P)))

    A_in = {k: sum(beta[i] * w.pos(P[i][k]) for i in J) for k in J}
    coeffs = {k: beta[k] - A_in[k] for k in J}
    lhs_terms = {k: W[k] * coeffs[k] for k in J}
    D = sum(lhs_terms.values())

    S = F(0)
    source_terms = {}
    for i in J:
        pieces = {
            "self_negative": -w.neg(P[i][i]) * W[i],
            "internal_negative_transfer": F(0),
            "external_positive_to_negative_coord": F(0),
            "external_negative_to_positive_coord": F(0),
            "external_positive_to_positive_coord": F(0),
            "external_negative_to_negative_coord": F(0),
        }
        total_i = pieces["self_negative"]
        for k in range(len(P)):
            if k == i:
                continue
            if k in J:
                term = -w.neg(P[i][k]) * W[k]
                pieces["internal_negative_transfer"] += term
                total_i += term
            else:
                terms = {
                    "external_positive_to_negative_coord": w.pos(P[i][k]) * W[k],
                    "external_negative_to_positive_coord": w.neg(P[i][k]) * xpos[k],
                    "external_positive_to_positive_coord": -w.pos(P[i][k]) * xpos[k],
                    "external_negative_to_negative_coord": -w.neg(P[i][k]) * W[k],
                }
                for key, term in terms.items():
                    pieces[key] += term
                    total_i += term
        source_terms[i] = {"unweighted": total_i, "weighted": beta[i] * total_i, **pieces}
        S += beta[i] * total_i

    assert D == S
    if Bmass > 0:
        # Explicit sign-kill check requested by the prompt.
        assert D > 0, (U, s, r, J, Bmass, D)

    return {
        "U": U,
        "s": s,
        "r": r,
        "J": J,
        "B": Bmass,
        "D": D,
        "S": S,
        "D_over_B": None if Bmass == 0 else D / Bmass,
        "coeffs": coeffs,
        "negative_coefficients": [k for k, c in coeffs.items() if c < 0],
        "A_in": A_in,
        "lhs_terms": lhs_terms,
        "source_terms": source_terms,
    }


def theta_summary(charts: list[w.ChartData]) -> tuple[list[w.ChartData], list[w.ChartData]]:
    theta = [c for c in charts if c.m >= F(1, 2)]
    assert theta
    best = min(c.Phi for c in theta)
    argmins = [c for c in theta if c.Phi == best]
    assert all(c.Phi >= best for c in theta)
    return theta, argmins


def branch_certificates(L: list[list[F]], P: list[list[F]], cd: w.ChartData, s: int) -> list[dict]:
    out = []
    for j in range(len(L)):
        if j in cd.U:
            continue
        try:
            br = w.branch_record(L, P, cd, s, j)
        except (AssertionError, ValueError, ZeroDivisionError):
            continue
        br["s"] = s
        if br["beta_s"] > 0 and (br["E_s"] > 0 or br["branch_type"] == "Gamma"):
            out.append(br)
    return out


def certify_instance(
    name: str,
    family: str,
    L: list[list[F]],
    Bleft: list[list[F]],
    expected_argmins: list[dict] | None = None,
    expected_clean: tuple[tuple[int, int, int], int, int] | None = None,
) -> dict:
    P = w.P_of(L, Bleft)
    delta = w.delta_of(P)
    assert F(0) < delta <= F(1, 4)

    charts = w.chart_data(L, P)
    theta, argmins = theta_summary(charts)
    argmin_rows = []
    all_floors = []
    clean_blocks = []

    if expected_argmins is not None:
        expected = {
            (
                tuple(a["U"]),
                F(a["m"]),
                tuple(F(x) for x in a["phi"]),
                F(a["Phi"]),
                tuple(a["pivots"]),
            )
            for a in expected_argmins
        }
        actual = {
            (
                c.U,
                c.m,
                c.phi,
                c.Phi,
                tuple(s for s in range(3) if c.phi[s] == c.Phi),
            )
            for c in argmins
        }
        assert expected == actual, name

    for cd in argmins:
        pivots = [s for s in range(3) if cd.phi[s] == cd.Phi]
        branches_by_s = {}
        for s in pivots:
            branches = branch_certificates(L, P, cd, s)
            branches_by_s[s] = branches
            for br in branches:
                if br["clean_gamma"]:
                    clean_blocks.append((cd.U, s, br["j"], br))
            for r in range(3):
                if r == s:
                    continue
                fe = direct_fe_identity(P, cd.coords, cd.U, r, s)
                fe["delta"] = delta
                fe["D_over_delta"] = fe["D"] / delta
                all_floors.append(fe)
        argmin_rows.append(
            {
                "U": cd.U,
                "m": cd.m,
                "phi": cd.phi,
                "Phi": cd.Phi,
                "pivots": pivots,
                "branches_by_s": branches_by_s,
            }
        )

    if expected_clean is not None:
        exp_U, exp_s, exp_j = expected_clean
        assert any(U == exp_U and s == exp_s and j == exp_j for U, s, j, _ in clean_blocks), name
    assert clean_blocks, name

    positive = [f for f in all_floors if f["B"] > 0]
    assert positive, name
    best_floor = min(positive, key=lambda f: f["D_over_B"])
    max_upper = max(positive, key=lambda f: f["D_over_delta"])

    return {
        "name": name,
        "family": family,
        "n": len(L),
        "delta": delta,
        "P": P,
        "theta_count": len(theta),
        "argmins": argmin_rows,
        "clean_blocks": clean_blocks,
        "floors": all_floors,
        "best_floor": best_floor,
        "max_upper": max_upper,
    }


def certify_bundle() -> list[dict]:
    data = json.loads(DATA.read_text())
    out = []
    for idx, point in enumerate(data["certified_points"]):
        L = parse_matrix(point["L"])
        Bleft = parse_matrix(point["B"])
        P = w.P_of(L, Bleft)
        assert P == parse_matrix(point["P"])
        assert w.delta_of(P) == F(point["delta"])
        rec = certify_instance(
            f"bundle-{idx}:{point['name']}",
            point["family"],
            L,
            Bleft,
            expected_argmins=point["argmins"],
            expected_clean=(tuple(point["U"]), point["s"], point["branch_j"]),
        )
        out.append(rec)
    return out


def low_floor_sequence() -> list[dict]:
    # Fresh exact family: same two-carrier/one-insert template, but not one of
    # the 9 bundle points.  The carrier self-entry is alpha=(1-p+e)v, hence
    # in the certified single-carrier rows D_J/B = 1-alpha.
    q = F(11, 1000)
    g = F(17, 1000)
    wgt = F(61, 1000)
    a = F(1, 125)
    y = F(2, 125)
    sequence = [
        (F(11, 200), F(3, 100), F(183, 200)),
        (F(13, 200), F(7, 200), F(187, 200)),
        (F(3, 40), F(1, 25), F(189, 200)),
        (F(17, 200), F(9, 200), F(19, 20)),
        (F(19, 200), F(1, 20), F(191, 200)),
        (F(21, 200), F(11, 200), F(24, 25)),
        (F(1, 8), F(13, 200), F(193, 200)),
        (F(29, 200), F(3, 40), F(97, 100)),
        (F(31, 200), F(2, 25), F(971, 1000)),
        (F(33, 200), F(17, 200), F(243, 250)),
        (F(37, 200), F(19, 200), F(487, 500)),
        (F(39, 200), F(1, 10), F(39, 40)),
        (F(41, 200), F(21, 200), F(122, 125)),
        (F(43, 200), F(11, 100), F(977, 1000)),
    ]
    out = []
    for p, e, alpha in sequence:
        c = 1 - p + e
        v = alpha / c
        L, Bleft = w.family_compensated_insert((p, e, q, g, v, wgt), (-a, F(1, 2) + a, F(1, 2)), (F(0), F(0), y))
        rec = certify_instance(
            f"fresh-alpha={fstr(alpha)}",
            "fresh-two-carrier-insert-alpha-sequence",
            L,
            Bleft,
            expected_clean=((0, 2, 4), 2, 1),
        )
        bf = rec["best_floor"]
        assert bf["U"] == (0, 2, 4)
        assert bf["s"] == 2
        assert bf["r"] == 1
        assert bf["J"] == [3]
        assert bf["D_over_B"] == 1 - alpha
        assert bf["B"] / rec["delta"] > F(1, 2)
        rec["params"] = {"p": p, "e": e, "q": q, "g": g, "v": v, "w": wgt, "a": a, "y": y, "alpha": alpha}
        out.append(rec)
    return out


def cap_probe_failures() -> list[dict]:
    # Focused failed probe from the final search: fixed q,g,w,a,y family,
    # p near the naive delta-cap balance.  These are finite negative
    # observations only, not a proof of absence.
    q = F(11, 1000)
    g = F(17, 1000)
    wgt = F(61, 1000)
    a = F(1, 125)
    y = F(2, 125)
    failures = []
    for alpha in [F(49, 50), F(99, 100), F(199, 200), F(999, 1000), F(1999, 2000)]:
        found = False
        for enum in range(50, 251, 5):
            e = F(enum, 1000)
            p_cap = (1 + e) / 5
            for off in [F(k, 1000) for k in range(-30, 6, 5)]:
                p = p_cap + off
                if p <= 0:
                    continue
                c = 1 - p + e
                v = alpha / c
                try:
                    L, Bleft = w.family_compensated_insert((p, e, q, g, v, wgt), (-a, F(1, 2) + a, F(1, 2)), (F(0), F(0), y))
                    certify_instance("cap-probe", "cap-probe", L, Bleft, expected_clean=((0, 2, 4), 2, 1))
                    found = True
                    break
                except (AssertionError, ValueError, ZeroDivisionError):
                    pass
            if found:
                break
        assert not found, alpha
        failures.append({"alpha": alpha, "tested_e_count": 41, "tested_offsets": 8})
    return failures


def jsonable(obj):
    if isinstance(obj, F):
        return fstr(obj)
    if isinstance(obj, tuple):
        return [jsonable(x) for x in obj]
    if isinstance(obj, list):
        return [jsonable(x) for x in obj]
    if isinstance(obj, dict):
        return {str(k): jsonable(v) for k, v in obj.items() if k != "P"}
    return obj


def flatten_rows(records: list[dict], source: str) -> list[dict]:
    rows = []
    for rec in records:
        for fe in rec["floors"]:
            rows.append(
                {
                    "source": source,
                    "name": rec["name"],
                    "family": rec["family"],
                    "n": rec["n"],
                    "delta": rec["delta"],
                    "theta_count": rec["theta_count"],
                    "U": fe["U"],
                    "s": fe["s"],
                    "r": fe["r"],
                    "J": fe["J"],
                    "B": fe["B"],
                    "D": fe["D"],
                    "S": fe["S"],
                    "D_over_B": fe["D_over_B"],
                    "D_over_delta": fe["D_over_delta"],
                    "negative_coefficients": fe["negative_coefficients"],
                }
            )
    return rows


def write_csv(rows: list[dict]) -> None:
    with CSV_OUT.open("w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "source",
                "name",
                "family",
                "n",
                "delta",
                "theta_count",
                "U",
                "s",
                "r",
                "J",
                "B",
                "D",
                "S",
                "D_over_B",
                "D_over_delta",
                "negative_coefficients",
            ],
        )
        writer.writeheader()
        for row in rows:
            writer.writerow({k: jsonable(v) for k, v in row.items()})


def report(bundle: list[dict], fresh: list[dict], cap_failures: list[dict], rows: list[dict]) -> str:
    positive = [r for r in rows if r["B"] > 0]
    certified_inf = min(positive, key=lambda r: r["D_over_B"])
    bundle_rows = flatten_rows(bundle, "bundle")
    bundle_positive = [r for r in bundle_rows if r["B"] > 0]
    bundle_inf = min(bundle_positive, key=lambda r: r["D_over_B"])
    max_upper = max(positive, key=lambda r: r["D_over_delta"])
    best_fresh = min(fresh, key=lambda r: r["best_floor"]["D_over_B"])
    bf = best_fresh["best_floor"]
    clean = best_fresh["clean_blocks"][0]
    br = clean[3]
    M = next(a for a in best_fresh["argmins"] if a["U"] == bf["U"])["Phi"]
    gamma_margin = br["Gamma"] - M
    psi_margin = M - br["Psi"]
    delta_slack = F(1, 4) - best_fresh["delta"]

    lines = [
        "# Wave 16b D_J/B Floor Decider",
        "",
        "Verdict: **UNDECIDED**.",
        "",
        "Status tags: T0 exact rational certificates for the listed instances; T1 use of the direct-FE identity; T2 adversarial read; no rigorous theorem.",
        "",
        "Rerun commands:",
        "",
        "```bash",
        "python3 waves-scratch/w16b-dj-floor/dj_floor_decider.py",
        "python3 -m py_compile waves-scratch/w16b-dj-floor/dj_floor_decider.py",
        "```",
        "",
        "## Bundle Recompute",
        "",
        f"All 9 certified clean-block bundle points were rebuilt from `L,B`: `B L=I_3`, `P=L B`, `P^2=P`, row sums `1`, and `delta<=1/4` were hard-asserted.",
        "For every theta-half argmin, every maximal pivot, and every transverse row, the script recomputed `D_J`, `B_{r,s}`, `D_J/B`, and `D_J/delta` and hard-asserted `D_J=S_J`.",
        "",
        f"Bundle positive-`B` infimum: `{fstr(bundle_inf['D_over_B'])}` at `{bundle_inf['name']}`, `U={tuple(bundle_inf['U'])}`, `s={bundle_inf['s']}`, `r={bundle_inf['r']}`, `J={bundle_inf['J']}`.",
        "The tied charts are included: the `(0,1,3)` side gives `203/400`; the `(0,2,4)` side gives `157/500`.",
        "No sign kill occurred: every certified positive-`B` row had `D_J>0`.",
        "For every bundle row below, the other transverse row is `r=0` with `J=empty`, `B=D=0`, and `D_J=S_J=0`; the positive transverse rows are:",
        "",
        "| point | argmin U | s | r | J | B | D_J=S_J | D_J/B | D_J/delta |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for row in bundle_positive:
        lines.append(
            f"| `{row['name']}` | `{tuple(row['U'])}` | `{row['s']}` | `{row['r']}` | `{row['J']}` | `{fstr(row['B'])}` | `{fstr(row['D'])}` | `{fstr(row['D_over_B'])}` | `{fstr(row['D_over_delta'])}` |"
        )
    lines.extend(
        [
        "",
        "## Adversarial Minimization",
        "",
        "The seed value `lambda=157/500` is not stable.  A fresh exact two-carrier-plus-insert sequence pushes the same single-carrier anatomy downward:",
        "",
        "| point | alpha=(1-p+e)v | D_J/B | B/delta | D_J/delta | delta |",
        "|---|---:|---:|---:|---:|---:|",
        ]
    )
    for rec in fresh:
        f = rec["best_floor"]
        params = rec["params"]
        lines.append(
            f"| `{rec['name']}` | `{fstr(params['alpha'])}` | `{fstr(f['D_over_B'])}` | `{fstr(f['B'] / rec['delta'])}` | `{fstr(f['D_over_delta'])}` | `{fstr(rec['delta'])}` |"
        )
    lines.extend(
        [
            "",
            f"Best certified fresh point: `{best_fresh['name']}` with parameters "
            f"`p={fstr(best_fresh['params']['p'])}`, `e={fstr(best_fresh['params']['e'])}`, "
            f"`q={fstr(best_fresh['params']['q'])}`, `g={fstr(best_fresh['params']['g'])}`, "
            f"`v={fstr(best_fresh['params']['v'])}`, `w={fstr(best_fresh['params']['w'])}`, "
            f"`a={fstr(best_fresh['params']['a'])}`, `y={fstr(best_fresh['params']['y'])}`.",
            f"It certifies `D_J/B={fstr(bf['D_over_B'])}` with `B/delta={fstr(bf['B'] / best_fresh['delta'])} > 1/2`; hence this is **not** a fake kill from `B` vanishing faster than `delta`.",
            f"Clean block: `U={tuple(bf['U'])}`, `s={bf['s']}`, `r={bf['r']}`, clean row `j={clean[2]}`, carrier set `J={bf['J']}`.",
            f"Margins at the best point: `delta` slack to cap is `{fstr(delta_slack)}`, `M-Psi={fstr(psi_margin)}`, `Gamma-M={fstr(gamma_margin)}`.",
            "",
            "The binding anatomy is therefore clear but not closed: in this family `D_J/B = 1-alpha` and `B/delta` stays near `1/2`, while the search approaches the `delta<=1/4` and maximal-pivot/clean-branch constraints.",
            "A focused finite cap-boundary probe found no certified clean points for `alpha in {49/50,99/100,199/200,999/1000,1999/2000}` in the tested local grid, but this is only T2 negative evidence.",
            "",
            "## Upper Side",
            "",
            f"Across all certified rows in this worker, the largest exact `D_J/delta` is `{fstr(max_upper['D_over_delta'])}` at `{max_upper['name']}`.",
            f"Thus the certified data are consistent with `D_J <= C delta` for `C={fstr(max_upper['D_over_delta'])}` on this finite set; no upper-side blow-up was observed.",
            "",
            "## Verdict",
            "",
            "FLOOR HOLDS is too strong: the certified infimum dropped from `157/500` to `23/1000` under exact clean-block certificates.",
            "FLOOR DEAD is also too strong: I did not certify `D_J/B -> 0` and found no point with `D_J <= 0 < B`.",
            "",
            "**UNDECIDED residual:** prove or refute whether the fresh alpha-family can be continued with `alpha -> 1` while preserving the clean block, capped theta-half argmin status, maximal pivot `s=2`, and `B/delta` bounded below.",
            "",
            "## Hard Asserts",
            "",
            "- Every certificate uses `fractions.Fraction`; floats are absent from asserted arithmetic.",
            "- For every matrix: `B L=I_3`, `P=L B`, `P^2=P`, row sums `1`, and `0<delta<=1/4`.",
            "- Complete theta-half enumeration is recomputed; argmins are exactly the charts with minimal `Phi` among `m>=1/2` charts.",
            "- For the 9 bundle points, recomputed argmin tuples `(U,m,phi,Phi,pivots)` exactly match the JSON bundle.",
            "- Clean Gamma block existence is hard-asserted at the stored bundle chart and at `U=(0,2,4), s=2, j=1` for every fresh point.",
            "- For every argmin/maximal-pivot/transverse row, row reproduction is asserted on every carrier and `D_J=S_J` is asserted.",
            "- Explicit sign-kill check: if `B>0`, then `D_J>0`; otherwise the script aborts.",
            "- Fresh alpha sequence asserts `J={3}`, `D_J/B=1-alpha`, and `B/delta>1/2`.",
            "",
            f"Machine-readable outputs: `{CSV_OUT}`, `{JSON_OUT}`.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    SCRATCH.mkdir(parents=True, exist_ok=True)
    bundle = certify_bundle()
    fresh = low_floor_sequence()
    cap_failures = cap_probe_failures()
    rows = flatten_rows(bundle, "bundle") + flatten_rows(fresh, "fresh")
    write_csv(rows)
    JSON_OUT.write_text(
        json.dumps(
            {
                "status": "T0 exact certificates; T1 identity; T2 minimization evidence; theorem undecided",
                "bundle": jsonable(bundle),
                "fresh": jsonable(fresh),
                "cap_probe_failures": jsonable(cap_failures),
                "rows": jsonable(rows),
            },
            indent=2,
            sort_keys=True,
        )
        + "\n"
    )
    REPORT_OUT.write_text(report(bundle, fresh, cap_failures, rows))
    print("[w16b-dj-floor] exact certificates OK")
    print(f"wrote {CSV_OUT}")
    print(f"wrote {JSON_OUT}")
    print(f"wrote {REPORT_OUT}")


if __name__ == "__main__":
    main()
