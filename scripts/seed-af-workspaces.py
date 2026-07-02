#!/usr/bin/env python3
"""Bootstrap: stand up one af (Adversarial Proof Framework) Layer-2 workspace per
*provable* registry result. Idempotent; NOT a gate — a one-time/repeatable bootstrap
that documents how proofs/<id>/ was created (auditable provenance).

For each argument/lemmas/<id>.md whose kind != open-problem:
  - if proofs/<id>/ledger/ is absent, run:  af init -d proofs/<id> -c <contract> -a orchestrator
  - verify the round-trip: normalize(`af get 1`.statement) == normalize(contract)
    (the SAME normalize the linker's contract-match uses: " ".join(s.split()))
  - on verified success, flip the shard's `af: none` -> `af: seeded`

Open-problem shards are skipped (an open problem has no proof to formalise).
Usage:
  python3 scripts/seed-af-workspaces.py [<id> | all]   # default: all
Exits non-zero if any workspace fails its round-trip check.
"""
import json
import os
import pathlib
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
ARG_DIR = ROOT / "argument" / "lemmas"
AF = os.environ.get("AF") or shutil.which("af") or "/home/tobias/Projects/vibefeld/af"
AUTHOR = "orchestrator"


def normalize(s):
    return " ".join((s or "").split())


def parse_frontmatter(text):
    """Return (dict, frontmatter_line_list, body_start_index). Flat YAML, first-colon split."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("no frontmatter")
    end = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
    fm = {}
    for ln in lines[1:end]:
        if ":" in ln:
            k, v = ln.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm, lines, end


def flip_af_seeded(path, lines, fm_end):
    """Replace the single `af: none` line inside the frontmatter with `af: seeded`."""
    for i in range(1, fm_end):
        if lines[i].strip() == "af: none":
            lines[i] = lines[i].replace("af: none", "af: seeded")
            path.write_text("\n".join(lines) + "\n", encoding="utf-8")
            return True
    return False


def af_root_statement(wsdir):
    out = subprocess.run([AF, "get", "1", "-d", str(wsdir), "-f", "json"],
                         capture_output=True, text=True, timeout=30)
    if out.returncode != 0:
        raise RuntimeError(f"af get 1 failed: {out.stderr.strip()}")
    return json.loads(out.stdout).get("statement", "")


def seed_one(path, only=None):
    text = path.read_text(encoding="utf-8")
    fm, lines, fm_end = parse_frontmatter(text)
    lid = fm.get("id", path.stem)
    if only and only != "all" and only != lid:
        return None
    if fm.get("kind") == "open-problem":
        return (lid, "skip", "open-problem (no proof to formalise)")
    contract = fm.get("contract", "")
    ws = fm.get("workspace") or f"proofs/{lid}"
    wsdir = ROOT / ws
    created = False
    if not (wsdir / "ledger").exists():
        wsdir.parent.mkdir(parents=True, exist_ok=True)
        r = subprocess.run([AF, "init", "-d", str(wsdir), "-c", contract, "-a", AUTHOR],
                           capture_output=True, text=True, timeout=60)
        if r.returncode != 0:
            return (lid, "FAIL", f"af init: {r.stderr.strip() or r.stdout.strip()}")
        created = True
    # round-trip verification against the registry contract (linker's invariant)
    try:
        stmt = af_root_statement(wsdir)
    except Exception as e:
        return (lid, "FAIL", str(e))
    if normalize(stmt) != normalize(contract):
        return (lid, "FAIL", "round-trip mismatch: af root conjecture != contract")
    # flip af: none -> seeded (idempotent: already-seeded shards have no `af: none` line)
    flipped = flip_af_seeded(path, lines, fm_end)
    state = "seeded(new)" if created else ("seeded(existing)" if flipped else "already-seeded")
    return (lid, "OK", state)


def main(argv):
    only = argv[0] if argv else "all"
    results = []
    for path in sorted(ARG_DIR.glob("*.md")):
        if path.name in ("README.md", "INDEX.md"):
            continue
        res = seed_one(path, only)
        if res:
            results.append(res)
    width = max((len(r[0]) for r in results), default=10)
    fails = 0
    for lid, status, detail in results:
        if status == "FAIL":
            fails += 1
        print(f"  {status:5}  {lid:<{width}}  {detail}")
    seeded = sum(1 for _, s, _ in results if s == "OK")
    print(f"\nseed-af: {seeded} ok, {fails} failed, "
          f"{sum(1 for _, s, _ in results if s == 'skip')} skipped (af binary: {AF})")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
