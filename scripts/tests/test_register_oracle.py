#!/usr/bin/env python3
"""Red-green tests for scripts/register-oracle.py (aism-lah) — the fr bank-gate oracle
registrar. Exercises add + idempotent re-run + precondition failures against a temp
portfolio fixture, then a READ-ONLY duplicate-detection pass against the REAL
.frontier/portfolio.json (byte-compared before/after — never modified).
Run: python3 scripts/tests/test_register_oracle.py
"""
import contextlib
import importlib.util
import io
import json
import pathlib
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent


def load_ro():
    spec = importlib.util.spec_from_file_location(
        "register_oracle", ROOT / "scripts" / "register-oracle.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


passed = failed = 0


def check(name, cond):
    global passed, failed
    if cond:
        passed += 1
        print(f"PASS  {name}")
    else:
        failed += 1
        print(f"FAIL  {name}")


def run(mod, argv):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        rc = mod.main(argv)
    return rc, out.getvalue(), err.getvalue()


# ---------- temp fixture: add, idempotency, preconditions, append-only ----------
ro = load_ro()
with tempfile.TemporaryDirectory() as td:
    root = pathlib.Path(td)
    (root / ".frontier").mkdir()
    (root / "argument" / "lemmas").mkdir(parents=True)
    for rid in ("lem-t", "lem-conflict", "lem-noledger"):
        (root / "argument" / "lemmas" / f"{rid}.md").write_text(
            f"---\nid: {rid}\ncontract: C\n---\n", encoding="utf-8")
    for rid in ("lem-t", "lem-conflict"):
        (root / "proofs" / rid / "ledger").mkdir(parents=True)
    seed = {"goal": "g", "frontier": "f",
            "config": {"stale_threshold": 2,
                       "oracles": [{"name": "af-pre-existing",
                                    "cmd": ["python3", "/x/oracle.py", "pre-existing"],
                                    "inputs": ["/x/ledger"]}]},
            "arms": [{"id": "A"}]}
    portfolio = root / ".frontier" / "portfolio.json"
    portfolio.write_text(json.dumps(seed, indent=2), encoding="utf-8")   # fr's on-disk format
    ro.ROOT = root
    ro.PORTFOLIO = portfolio

    # add
    rc, out, err = run(ro, ["lem-t"])
    data = json.loads(portfolio.read_text(encoding="utf-8"))   # must stay valid JSON
    names = [o["name"] for o in data["config"]["oracles"]]
    entry = next(o for o in data["config"]["oracles"] if o["name"] == "af-lem-t")
    check("add: exit 0", rc == 0)
    check("add: entry appended after the existing one", names == ["af-pre-existing", "af-lem-t"])
    check("add: standard shape — cmd = python3 + ABSOLUTE oracle path + rid",
          entry["cmd"][0] == "python3"
          and entry["cmd"][1] == str(root / "scripts" / "oracles" / "af-validated.py")
          and entry["cmd"][2] == "lem-t")
    check("add: standard shape — inputs = [abs ledger, abs shard]",
          entry["inputs"] == [str(root / "proofs" / "lem-t" / "ledger"),
                              str(root / "argument" / "lemmas" / "lem-t.md")])
    check("add: APPEND-ONLY — everything else in the file untouched",
          data["goal"] == "g" and data["frontier"] == "f" and data["arms"] == [{"id": "A"}]
          and data["config"]["stale_threshold"] == 2
          and data["config"]["oracles"][0] == seed["config"]["oracles"][0])
    check("add: prints the fr verify command to run next",
          "fr verify proofs/lem-t/export.md --oracle af-lem-t" in out)

    # idempotent re-run (detect duplicate, no write)
    before = portfolio.read_bytes()
    rc2, out2, _ = run(ro, ["lem-t"])
    check("re-run: exit 0 and says already registered", rc2 == 0 and "already registered" in out2)
    check("re-run: file byte-identical (no duplicate appended)", portfolio.read_bytes() == before)
    check("re-run: still prints the fr verify command", "fr verify proofs/lem-t/" in out2)

    # preconditions
    rc3, _, err3 = run(ro, ["lem-ghost"])
    check("missing registry shard -> exit 1, no write",
          rc3 == 1 and "shard" in err3 and portfolio.read_bytes() == before)
    rc4, _, err4 = run(ro, ["lem-noledger"])
    check("missing af ledger -> exit 1, no write",
          rc4 == 1 and "ledger" in err4 and portfolio.read_bytes() == before)
    rc5, _, _ = run(ro, [])
    check("no args -> usage exit 2", rc5 == 2)

    # same name, DIFFERENT shape already present -> loud error, left untouched
    data["config"]["oracles"].append({"name": "af-lem-conflict", "cmd": ["other"], "inputs": []})
    portfolio.write_text(json.dumps(data, indent=2), encoding="utf-8")
    before = portfolio.read_bytes()
    rc6, _, err6 = run(ro, ["lem-conflict"])
    check("same-name different-shape entry -> exit 1, untouched",
          rc6 == 1 and "DIFFERENT" in err6 and portfolio.read_bytes() == before)

    # non-canonical serialization on disk -> refuse to rewrite (append-only guarantee)
    portfolio.write_text(json.dumps(seed, indent=4), encoding="utf-8")
    before = portfolio.read_bytes()
    rc7, _, err7 = run(ro, ["lem-t"])
    check("non-canonical portfolio format -> refuse to rewrite (exit 1, untouched)",
          rc7 == 1 and "format" in err7 and portfolio.read_bytes() == before)

# ---------- REAL portfolio.json: duplicate detection is a read-only no-op ----------
ro_real = load_ro()   # fresh module, real ROOT/PORTFOLIO
real = ro_real.PORTFOLIO
if real.exists() and (ro_real.ROOT / "proofs" / "lem-classical-equiv" / "ledger").is_dir():
    before = real.read_bytes()
    rc, out, err = run(ro_real, ["lem-classical-equiv"])   # registered long ago (worklog s1)
    check("real portfolio: existing oracle detected as duplicate (exit 0)",
          rc == 0 and "already registered" in out)
    check("real portfolio: byte-identical after the dry run", real.read_bytes() == before)
    check("real portfolio: still valid JSON", bool(json.loads(real.read_text(encoding="utf-8"))))
else:
    print("SKIP  real-portfolio duplicate check (fixture absent)")

print(f"\n{passed} passed, {failed} failed")
raise SystemExit(1 if failed else 0)
