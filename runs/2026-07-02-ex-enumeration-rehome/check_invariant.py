#!/usr/bin/env python3
"""Local invariant for the inherited (EX) numerical record re-home.

This is deliberately small: it checks the exact-rational rank-3 (EX)
enumeration data and the hashes of the broad d8-d14 archived artifacts.
It is not a re-run of the full Gurobi/SciPy campaigns.
"""
from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "upstream"
RANK3 = DATA / "w41_ex" / "rank3_results.json"

EXPECTED_HASHES = {
    DATA / "d8_decision.json": "99de674015ccd911d56e63525df3fe0c309607c0bf984fd784e8b73b3e7de6bc",
    DATA / "d13_smalldelta.json": "f3bfb374ee4b8a3138b3c526aaaeccf0cb7acf517d4fa99807bd0eee08bd8e18",
    DATA / "d14_leakage.json": "60b93a7a4adf4d16f4061f08b566196f1b479a08ca561ef452675b7b78f15d2d",
    RANK3: "1ad85d427353a42013850d01e9d65dac1d2750e94666e8a372bf2abd36ea4933",
}

SPOT_CHECKS = {
    "transverse_pair_a1_8": ("2/17", "2/17", "1"),
    "transverse_pair_a1_4": ("1/5", "1/5", "1"),
    "no_center_rank3_a1_100": ("1/100", "1/100", "1"),
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def frac(text: str) -> Fraction:
    return Fraction(text)


def main() -> int:
    for path, expected in EXPECTED_HASHES.items():
        actual = sha256(path)
        if actual != expected:
            raise SystemExit(f"FAIL sha256 {path.relative_to(ROOT)} expected={expected} actual={actual}")

    records = json.loads(RANK3.read_text(encoding="utf-8"))
    by_name = {r["name"]: r for r in records}
    delta_ok = [r for r in records if r.get("delta_ok")]
    random_ok = [r for r in delta_ok if r.get("tag") == "random"]
    adversarial_ok = [r for r in delta_ok if str(r.get("tag", "")).startswith("adversarial")]
    factor_bad = [r["name"] for r in records if not r.get("factor_global_ok")]
    ex_bad = [
        r["name"]
        for r in delta_ok
        if frac(r["phi_min_over_delta"]) > 1
    ]
    worst_ratio = max(frac(r["phi_min_over_delta"]) for r in delta_ok)

    expected_counts = {
        "rank3_records": (len(records), 444),
        "delta_ok_records": (len(delta_ok), 278),
        "random_delta_ok": (len(random_ok), 220),
        "adversarial_delta_ok": (len(adversarial_ok), 53),
        "factorization_violations": (len(factor_bad), 0),
        "ex_violations_C0_1": (len(ex_bad), 0),
    }
    for label, (actual, expected) in expected_counts.items():
        if actual != expected:
            raise SystemExit(f"FAIL {label} expected={expected} actual={actual}")

    spot_lines = []
    for name, (delta, phi, ratio) in SPOT_CHECKS.items():
        r = by_name[name]
        recomputed = frac(r["phi_min"]) / frac(r["delta"])
        if (r["delta"], r["phi_min"], r["phi_min_over_delta"]) != (delta, phi, ratio):
            raise SystemExit(f"FAIL stored exact fields for {name}")
        if recomputed != frac(r["phi_min_over_delta"]):
            raise SystemExit(f"FAIL recomputed ratio for {name}: {recomputed}")
        spot_lines.append(f"{name}:delta={delta}:phi={phi}:ratio={recomputed}")

    print("PASS exact invariant")
    print(f"sha256_checked={len(EXPECTED_HASHES)}")
    print(f"rank3_records={len(records)}")
    print(f"delta_ok_records={len(delta_ok)}")
    print(f"random_delta_ok={len(random_ok)}")
    print(f"adversarial_delta_ok={len(adversarial_ok)}")
    print(f"ex_violations_C0_1={len(ex_bad)}")
    print(f"factorization_violations={len(factor_bad)}")
    print(f"worst_phi_min_over_delta={worst_ratio}")
    print("spot_checks=" + ";".join(spot_lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
