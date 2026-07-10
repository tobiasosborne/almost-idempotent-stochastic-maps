#!/usr/bin/env python3
"""Register the parametric af-validated banking oracle for one result (aism-lah).

Usage: python3 scripts/register-oracle.py <rid>

Appends the STANDARD af-validated oracle entry for <rid> to config.oracles in
.frontier/portfolio.json (fr's bank-gate oracle registry — `fr help oracles`), then prints
the `fr verify` command that earns the banked verdict. The entry shape mirrors every
existing af-* entry: name af-<rid>; cmd = python3 + the absolute path of
scripts/oracles/af-validated.py + <rid>; inputs = the absolute paths of proofs/<rid>/ledger
and argument/lemmas/<rid>.md (fr hash-binds the verdict to these, so it goes stale if the
ledger or shard change).

Guarantees:
  * IDEMPOTENT — if an af-<rid> entry already exists, nothing is written (a same-name entry
    with a DIFFERENT shape is reported loudly and left untouched; resolve by hand).
  * APPEND-ONLY — this script changes nothing in portfolio.json except adding the one entry.
    portfolio.json is serialized as json.dumps(..., indent=2) with no trailing newline (fr's
    own on-disk format, byte-verified before writing); if the on-disk format ever drifts from
    that, the script refuses to rewrite rather than reformat the whole file.
  * PRECONDITIONS — the registry shard argument/lemmas/<rid>.md and the af workspace ledger
    proofs/<rid>/ledger must both exist (the oracle re-reads that ledger at verify time).
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PORTFOLIO = ROOT / ".frontier" / "portfolio.json"


def oracle_entry(rid):
    """The standard parametric af-validated oracle shape (absolute paths, matching every
    existing af-* entry in config.oracles)."""
    return {
        "name": f"af-{rid}",
        "cmd": ["python3", str(ROOT / "scripts" / "oracles" / "af-validated.py"), rid],
        "inputs": [str(ROOT / "proofs" / rid / "ledger"),
                   str(ROOT / "argument" / "lemmas" / f"{rid}.md")],
    }


def main(argv):
    if len(argv) != 1 or argv[0].startswith("-"):
        print("usage: python3 scripts/register-oracle.py <rid>", file=sys.stderr)
        return 2
    rid = argv[0]
    shard = ROOT / "argument" / "lemmas" / f"{rid}.md"
    ledger = ROOT / "proofs" / rid / "ledger"
    if not shard.is_file():
        print(f"ERROR: no registry shard {shard} — register the result (Layer 1) first",
              file=sys.stderr)
        return 1
    if not ledger.is_dir():
        print(f"ERROR: no af ledger at {ledger} — seed/orchestrate the workspace first",
              file=sys.stderr)
        return 1
    raw = PORTFOLIO.read_text(encoding="utf-8")
    data = json.loads(raw)
    oracles = data.setdefault("config", {}).setdefault("oracles", [])
    entry = oracle_entry(rid)
    existing = next((o for o in oracles if o.get("name") == entry["name"]), None)
    if existing is not None:
        if existing != entry:
            print(f"ERROR: an oracle named {entry['name']} already exists with a DIFFERENT "
                  f"shape — left untouched; reconcile it by hand:", file=sys.stderr)
            print(json.dumps(existing, indent=2), file=sys.stderr)
            return 1
        print(f"already registered: {entry['name']} (idempotent no-op)")
    else:
        # Append-only safety: portfolio.json must round-trip byte-identically through the
        # serialization we write, so adding ONE entry provably touches nothing else.
        if json.dumps(json.loads(raw), indent=2) != raw:
            print("ERROR: .frontier/portfolio.json is not in the expected "
                  "json.dumps(indent=2) format — refusing to rewrite (it would reformat "
                  "more than the appended entry). Add the entry by hand or fix the format.",
                  file=sys.stderr)
            return 1
        oracles.append(entry)
        tmp = PORTFOLIO.with_name(PORTFOLIO.name + ".tmp")
        tmp.write_text(json.dumps(data, indent=2), encoding="utf-8")
        tmp.replace(PORTFOLIO)
        print(f"registered oracle {entry['name']} in {PORTFOLIO}")
    print("next (the bank gate — the ONLY way to earn a banked verdict):")
    print(f"  fr verify proofs/{rid}/export.md --oracle af-{rid}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
