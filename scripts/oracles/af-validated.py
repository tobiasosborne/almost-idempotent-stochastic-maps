#!/usr/bin/env python3
"""Claim-specific fr banking oracle (FINDINGS 2026-07-01: never a coarse gate oracle).

Usage: af-validated.py <rid>     (claim text on stdin; exit 0 = PASS, 1 = FAIL)

PASS iff ALL of:
  1. the claim on stdin binds to exactly this result: it is the registry id <rid>, OR it equals /
     CONTAINS (whitespace-normalized) the full contract of argument/lemmas/<rid>.md. The contains
     form is the bank-gate path: `fr verify proofs/<rid>/export.md` resolves the path to the FILE
     CONTENT on stdin (and hash-binds staleness to it), and the af export embeds the root statement
     ≡ the contract. (The id form exists because fr's verdict filenames choke on
     full-contract-length claims — FINDINGS 2026-07-02.)
  2. the af workspace root statement (`af get 1`) ≡ that same contract (no drift);
  3. the af root epistemic_state is `validated`;
  4. every node's taint is `clean` (no unresolved taint anywhere in the tree).

The oracle's authority is the codex-built af ledger — an artifact external to the orchestrator
(reviewer ≠ author). It re-reads the ledger at verify time; fr additionally hash-binds the
verdict to the registered inputs, so it goes stale if the ledger or shard change.
"""
import json
import os
import pathlib
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
AF = os.environ.get("AF") or shutil.which("af") or "/home/tobias/go/bin/af"


def normalize(s):
    return " ".join((s or "").split())


def contract_of(rid):
    p = ROOT / "argument" / "lemmas" / f"{rid}.md"
    for ln in p.read_text(encoding="utf-8").splitlines():
        if ln.startswith("contract:"):
            return ln.split(":", 1)[1].strip()
    raise SystemExit(f"FAIL: no contract line in {p}")


def main():
    if len(sys.argv) != 2:
        print("usage: af-validated.py <rid>  (claim on stdin)", file=sys.stderr)
        return 1
    rid = sys.argv[1]
    ws = ROOT / "proofs" / rid
    claim = normalize(sys.stdin.read())
    contract = normalize(contract_of(rid))
    if claim != rid and contract not in claim:
        print(f"FAIL: claim neither the registry id {rid!r} nor a text containing its contract verbatim")
        return 1
    root = json.loads(subprocess.run(
        [AF, "get", "1", "-d", str(ws), "-f", "json"],
        capture_output=True, text=True, timeout=30, check=True).stdout)
    if normalize(root.get("statement")) != contract:
        print("FAIL: af root statement != registry contract (drift)")
        return 1
    if root.get("epistemic_state") != "validated":
        print(f"FAIL: af root epistemic_state = {root.get('epistemic_state')!r}, not validated")
        return 1
    stats = json.loads(subprocess.run(
        [AF, "status", "-d", str(ws), "-f", "json"],
        capture_output=True, text=True, timeout=30, check=True).stdout).get("statistics", {})
    taint = stats.get("taint_state", {}) or {}
    dirty = {k: v for k, v in taint.items() if k != "clean" and v}
    if dirty:
        print(f"FAIL: non-clean taint in tree: {dirty}")
        return 1
    print(f"PASS: {rid} af root validated, taint clean, claim == contract == af root")
    return 0


if __name__ == "__main__":
    sys.exit(main())
