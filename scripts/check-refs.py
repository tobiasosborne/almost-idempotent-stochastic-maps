#!/usr/bin/env python3
"""
check-refs.py — provenance-enforcement gate for af-workspace externals (Layer 2).

THE FAILURE MODE THIS GUARDS AGAINST: an af BUILD prover FABRICATES a "VERBATIM" quote —
attributing a paraphrase of a true fact to a refs/ locus where that exact text does NOT appear.
This gate string-matches every claimed verbatim quote back to its LOCAL refs/ source (L1 — ground
truth before claims; byte-verbatim modulo whitespace/markdown-formatting noise) and FAILS the build
if the words don't match.

Each af external lives at proofs/<ws>/externals/<hash>.json and has a "name" (e.g. GT-bhsa-jc) and a
freeform "source" string. Three kinds:
  (a) IMPORT external  — "source" references a prior proofs/<ws> validated lemma with NO refs/ locus.
                         verdict = skip_import (it imports a validated lemma, not a refs quote).
  (b) refs-quote       — "source" cites a refs/<path> locus AND contains a quoted verbatim string.
                         verdict = pass / fail  (we CHECK the quote against the refs file).
  (c) no quote         — neither an import nor an extractable refs quote.  verdict = skip_noquote (WARN).

Matching (tuned to tolerate line-wrap / whitespace / markdown-emphasis noise but CATCH word-level
fabrications): normalize quote and refs text by unifying markdown dollar-escaping (\\$ -> $), dropping
markdown emphasis asterisks (* — pure formatting, never a load-bearing word), and collapsing every
whitespace run to a single space. LaTeX commands and $ are KEPT (fabrications often differ there).
Then require a DISTINCTIVE long contiguous chunk of the normalized quote (the whole quote, else the
longest >= MIN_RUN-char contiguous run) to appear as a substring of the normalized refs file. The
locus line number is advisory — extractions span lines, so we search the whole file but record the locus.

Usage:
  python3 scripts/check-refs.py            # audit; prints per-external verdicts + summary
  python3 scripts/check-refs.py --check    # same; exit non-zero iff any FAIL (the gate mode)
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PROOFS = ROOT / "proofs"

MIN_RUN = 40  # a matched contiguous chunk must be at least this long to count as "distinctive"

# A refs/ locus inside a freeform source string, e.g. refs/hos/joa-m.md:2300 or
# refs/kitaev-2405.02434/approximate_algebras.tex:503-532
_REFS_RE = re.compile(r'refs/[A-Za-z0-9_./\-]+(?::[\d,\-]+)?')
# A proofs/<ws> reference (an IMPORT of a prior validated lemma)
_PROOFS_RE = re.compile(r'proofs/[A-Za-z0-9_-]+')


def normalize(s):
    """Collapse formatting/whitespace noise but preserve the actual WORDS (and LaTeX/$).

    - \\$  -> $    (markdown dollar-escaping is noise, not a different symbol)
    - *    -> ''   (markdown emphasis markers are formatting, never a load-bearing word)
    - any whitespace run -> a single space; strip ends
    LaTeX command names (\\circ, \\tilde, \\ge, ...) and $ are KEPT — fabrications differ in WORDS.
    """
    s = s.replace('\\$', '$')
    s = s.replace('*', '')
    s = re.sub(r'\s+', ' ', s)
    return s.strip()


def extract_quote(src):
    """Heuristic extraction of the claimed verbatim quote from a freeform source string.

    Prefer the run inside double-quotes following 'VERBATIM'; else the longest double-quoted run.
    Returns the raw (un-normalized) quote, or None if there is no double-quoted text.
    """
    m = re.search(r'VERBATIM[^"]*"(.*?)"', src, re.S)
    if m:
        return m.group(1)
    cands = re.findall(r'"(.*?)"', src, re.S)
    cands = [c for c in cands if c.strip()]
    return max(cands, key=len) if cands else None


def longest_run_match(qn, tn, min_run=MIN_RUN):
    """Does a distinctive contiguous chunk of normalized quote qn appear in normalized refs text tn?

    Returns (matched: bool, chunk: str|None). For a short quote (< min_run) we require the WHOLE
    quote to match (so we never wave through a too-short, non-distinctive fragment). Otherwise we
    accept if the whole quote matches, else the longest contiguous run of length >= min_run matches.
    """
    if not qn:
        return False, None
    if len(qn) < min_run:
        return (qn in tn), (qn if qn in tn else None)
    if qn in tn:
        return True, qn
    # Longest matching contiguous run, length from len(qn) down to min_run. Break as soon as we find
    # one (longest first). Cheap early-out: if no min_run-length window matches at all, it's a fail.
    L = len(qn)
    for length in range(L, min_run - 1, -1):
        for start in range(0, L - length + 1):
            chunk = qn[start:start + length]
            if chunk in tn:
                return True, chunk
    return False, None


def refs_file_for(refs_locus):
    """refs/<path>:<lines> -> (filepath_str, file_exists). The line range is advisory (stripped)."""
    fp = re.sub(r':[\d,\-]+$', '', refs_locus).rstrip(':;,')
    p = ROOT / fp
    return fp, p, p.is_file()


def classify_and_check(name, src, _cache):
    """Return a dict {verdict, refs_locus, claimed_quote_snippet, note} for one external.

    verdict in {pass, fail, skip_import, skip_noquote}.
    """
    proofs_ref = _PROOFS_RE.search(src)
    m = _REFS_RE.search(src)
    refs_locus = m.group(0) if m else None
    quote = extract_quote(src)
    has_quote = bool(quote and quote.strip())

    # (a) IMPORT external: references a proofs/ workspace and has NO refs/ locus.
    if proofs_ref and not refs_locus:
        return {"verdict": "skip_import", "refs_locus": None,
                "claimed_quote_snippet": "", "note": f"imports {proofs_ref.group(0)}"}

    # (c) no extractable refs quote -> skip_noquote (WARN).
    if not (refs_locus and has_quote):
        why = []
        if not refs_locus:
            why.append("no refs/ locus")
        if not has_quote:
            why.append("no double-quoted verbatim text")
        return {"verdict": "skip_noquote", "refs_locus": refs_locus,
                "claimed_quote_snippet": "", "note": "; ".join(why)}

    # (b) refs-quote external -> CHECK it.
    fp, path, exists = refs_file_for(refs_locus)
    if not exists:
        return {"verdict": "skip_noquote", "refs_locus": refs_locus,
                "claimed_quote_snippet": "",
                "note": f"refs file {fp} ABSENT (payload gitignored?) — cannot verify"}

    if fp not in _cache:
        _cache[fp] = normalize(path.read_text(encoding="utf-8"))
    tn = _cache[fp]
    qn = normalize(quote)
    ok, chunk = longest_run_match(qn, tn)
    if ok:
        return {"verdict": "pass", "refs_locus": refs_locus,
                "claimed_quote_snippet": "", "note": f"matched {len(chunk)}-char run"}
    return {"verdict": "fail", "refs_locus": refs_locus,
            "claimed_quote_snippet": qn[:160],
            "note": "claimed VERBATIM quote NOT found in refs file (word-level mismatch / fabrication)"}


def check_refs(proofs_dir=PROOFS):
    """Walk every proofs/<ws>/externals/*.json. Return (rows, fail_count, skip_count).

    rows: list of {workspace, external, refs_locus, verdict, claimed_quote_snippet, note}.
    """
    rows = []
    cache = {}
    if not proofs_dir.is_dir():
        return rows, 0, 0
    for ws_dir in sorted(p for p in proofs_dir.iterdir() if p.is_dir()):
        exdir = ws_dir / "externals"
        if not exdir.is_dir():
            continue
        for f in sorted(exdir.glob("*.json")):
            try:
                d = json.loads(f.read_text(encoding="utf-8"))
            except Exception as e:  # noqa: BLE001
                rows.append({"workspace": ws_dir.name, "external": f.name,
                             "refs_locus": None, "verdict": "fail",
                             "claimed_quote_snippet": "", "note": f"unparseable JSON: {e}"})
                continue
            name = d.get("name", f.stem)
            src = d.get("source", "") or ""
            res = classify_and_check(name, src, cache)
            res.update({"workspace": ws_dir.name, "external": name})
            rows.append(res)
    fail_count = sum(1 for r in rows if r["verdict"] == "fail")
    skip_count = sum(1 for r in rows if r["verdict"].startswith("skip"))
    return rows, fail_count, skip_count


def main(argv):
    check_mode = "--check" in argv
    rows, fail_count, skip_count = check_refs()
    symbol = {"pass": "PASS ", "fail": "FAIL ",
              "skip_import": "skip ", "skip_noquote": "WARN "}
    for r in rows:
        line = (f"[{symbol.get(r['verdict'], '?????')}] {r['workspace']:38s} "
                f"{r['external']:24s} {r['verdict']:12s} {r['refs_locus'] or '-'}")
        print(line)
        if r["verdict"] == "fail":
            print(f"           ! {r['note']}")
            if r["claimed_quote_snippet"]:
                print(f"           ! claimed: {r['claimed_quote_snippet']!r}")
        elif r["verdict"] == "skip_noquote":
            print(f"           (warn) {r['note']}")
    total = len(rows)
    print(f"\ncheck-refs: {total} externals, {fail_count} failed, {skip_count} skipped")
    if check_mode and fail_count:
        print("check-refs: FAILED — fabricated/mismatched verbatim quote(s) above.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
