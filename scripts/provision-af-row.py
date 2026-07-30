#!/usr/bin/env python3
"""Provision one seeded af workspace from its registry shard (session-38 parallel campaign).

Reads argument/lemmas/<rid>.md, then:
  - `af def-add <def> --file definitions/<def>.md` for every id in `defs:`;
  - `af add-external --name <dep> --source "imports validated registry lemma proofs/<dep> — <dep contract>"`
    for every id in `deps:` — REFUSING unless the dep shard says `af: validated` (or is `cited`).

Idempotent-ish: af rejects duplicate def names; reruns report and continue.
Usage: python3 scripts/provision-af-row.py <rid> [<rid> ...]
"""
import os, pathlib, re, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
AF = os.environ.get("AF") or str(pathlib.Path.home() / "go" / "bin" / "af")


def field(text, name):
    m = re.search(rf"^{name}: (.*)$", text, re.M)
    return m.group(1).strip() if m else ""


def provision(rid):
    shard = (ROOT / "argument" / "lemmas" / f"{rid}.md").read_text()
    ws = f"proofs/{rid}"
    defs = [d.strip() for d in field(shard, "defs").split(";") if d.strip()]
    deps = [d.strip() for d in field(shard, "deps").split(";") if d.strip()]
    for d in defs:
        f = ROOT / "definitions" / f"{d}.md"
        if not f.is_file():
            print(f"ERROR {rid}: missing definition shard {f}"); return False
        r = subprocess.run([AF, "def-add", d, "--file", str(f), "-d", ws], cwd=ROOT,
                           capture_output=True, text=True)
        print(f"  def {d}: {'ok' if r.returncode == 0 else r.stderr.strip()[:120]}")
    for dep in deps:
        dshard = (ROOT / "argument" / "lemmas" / f"{dep}.md").read_text()
        st = field(dshard, "af")
        if st != "validated":
            print(f"ERROR {rid}: dep {dep} is af:{st!r}, not validated — provision later"); return False
        contract = field(dshard, "contract")
        src = f"imports validated registry lemma proofs/{dep} — {contract}"
        r = subprocess.run([AF, "add-external", "-d", ws, "--name", dep, "--source", src],
                           cwd=ROOT, capture_output=True, text=True)
        print(f"  dep {dep}: {'ok' if r.returncode == 0 else r.stderr.strip()[:120]}")
    return True


if __name__ == "__main__":
    ok = all(provision(rid) for rid in sys.argv[1:])
    sys.exit(0 if ok else 1)
