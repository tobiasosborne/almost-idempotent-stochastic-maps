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
                         verdict = pass / fail  (we CHECK the quote against the refs file). An ABSENT
                         refs payload is verdict = fail (cannot byte-verify => cannot pass; aism-dbq).
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
import hashlib
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PROOFS = ROOT / "proofs"
ACK_FILE = ROOT / "refs" / "manifest" / "absent-acknowledged.json"

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
        # UN-VACUUM (aism-dbq): an external that CLAIMS a refs/ verbatim quote but whose payload is
        # absent cannot be byte-verified — so in --check it is a hard FAIL, never a silent skip. A
        # green run must never mean "we couldn't look". (Dep-IMPORTs that carry a proofs/<dep-id>
        # path and no refs locus are handled above as skip_import and are unaffected.)
        return {"verdict": "fail", "refs_locus": refs_locus, "absent_path": fp,
                "claimed_quote_snippet": "",
                "note": f"refs file {fp} ABSENT — a claimed VERBATIM refs quote cannot be byte-verified "
                        f"(fetch the payload into refs/ or remove the quote); L1 forbids an unverifiable pass"}

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


MANIFEST_FILE = ROOT / "refs" / "manifest" / "checksums.sha256"


def _parse_manifest(manifest_file):
    """STRICT sha256sum-format parser for checksums.sha256 — a TRUST INPUT for acknowledgments.

    Accepts only `<64-hex>` + two-char separator (`  ` text / ` *` binary) + path lines; a malformed
    non-blank line or a duplicate path ABORTS (fail-closed — never guess at a trust input). Paths
    are returned refs/-rooted, stripping exactly one leading './'. Filenames containing spaces are
    preserved verbatim (the path is everything after the separator, never a whitespace split)."""
    pinned = {}
    if not manifest_file.is_file():
        return pinned
    for i, line in enumerate(manifest_file.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        m = re.match(r'^([0-9a-f]{64})( \*|  )(.+)$', line)
        if not m:
            raise ValueError(f"checksums.sha256:{i}: malformed line {line!r} — "
                             f"refuse to load acknowledgments")
        sha, path = m.group(1), m.group(3)
        if path.startswith("./"):
            path = path[2:]
        key = "refs/" + path
        if key in pinned:
            raise ValueError(f"checksums.sha256:{i}: duplicate path {key!r} — refuse to load")
        pinned[key] = sha
    return pinned


def load_absent_acks(ack_file=ACK_FILE, manifest_file=MANIFEST_FILE):
    """Load refs/manifest/absent-acknowledged.json — the deliberately NARROW device-provisioning
    escape hatch over the aism-dbq un-vacuum rule (absent payload => hard FAIL).

    Returns {(refs_path, workspace, external_name): ack} covering ONLY entries whose payload is
    still absent, where each ack digest-binds ONE external: its JSON filename ('file') and the
    sha256 of its exact 'source' string ('source_sha256'). The caller must enforce both, so an
    altered quote, a renamed external, or a new file impersonating a listed name still hard-FAILs —
    an acknowledgment can never launder a NEW or MODIFIED quote.

    Load-time validation (fail-closed, ANY violation raises and kills the gate; ALL of it runs
    before the staleness check, so a malformed entry can never hide behind a present payload):
      - entry path must be canonical under refs/: segments 'refs/<seg>/...', no '', '.', '..'
        segments (rejects '//', '/./', traversal, trailing '/'), and its RESOLVED location (symlinks
        followed) must lie physically beneath refs/;
      - entry path must be PINNED in checksums.sha256 with EXACTLY the entry's sha256 — an
        acknowledgment can only ever cover a payload this repo committed to byte-for-byte;
      - every external must carry workspace/name/file/source_sha256.
    An entry whose payload is PRESENT is stale (verification has resumed): warn to remove it.
    """
    acks = {}
    if not ack_file.is_file():
        return acks
    pinned = _parse_manifest(manifest_file)
    refs_root = (ROOT / "refs").resolve()
    data = json.loads(ack_file.read_text(encoding="utf-8"))
    for e in data.get("entries", []):
        p = e["path"]
        segs = p.split("/")
        if segs[0] != "refs" or len(segs) < 2 or any(s in ("", ".", "..") for s in segs[1:]):
            raise ValueError(f"absent-acknowledged: non-canonical path {p!r} — refuse to load")
        rp = (ROOT / p).resolve()
        if refs_root != rp and refs_root not in rp.parents:
            raise ValueError(f"absent-acknowledged: {p!r} resolves outside refs/ "
                             f"({rp}) — refuse to load")
        if pinned.get(p) != e["sha256"]:
            raise ValueError(f"absent-acknowledged: {p!r} sha256 is not pinned in "
                             f"checksums.sha256 with the acknowledged hash — refuse to load")
        exts = e.get("externals", [])
        for ex in exts:
            if not all(k in ex for k in ("workspace", "name", "file", "source_sha256")):
                raise ValueError(f"absent-acknowledged: external {ex!r} lacks the digest binding "
                                 f"(workspace/name/file/source_sha256) — refuse to load")
        if (ROOT / p).is_file():
            print(f"check-refs: (warn) acknowledged-absent entry STALE — payload PRESENT again: "
                  f"{p}; byte-verification has resumed; REMOVE the entry "
                  f"(bead {e.get('restore_bead', '?')})")
            continue
        for ex in exts:
            acks[(p, ex["workspace"], ex["name"])] = {"file": ex["file"],
                                                      "source_sha256": ex["source_sha256"],
                                                      "restore_bead": e.get("restore_bead", "?")}
    return acks


def check_refs(proofs_dir=PROOFS, ack_file=ACK_FILE, manifest_file=MANIFEST_FILE):
    """Walk every proofs/<ws>/externals/*.json. Return (rows, fail_count, skip_count).

    rows: list of {workspace, external, refs_locus, verdict, claimed_quote_snippet, note}.
    """
    rows = []
    cache = {}
    acks = load_absent_acks(ack_file, manifest_file)
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
            if res["verdict"] == "fail" and res.get("absent_path"):
                ack = acks.get((res["absent_path"], ws_dir.name, name))
                # The rescue is DIGEST-BOUND: the external's JSON filename AND the sha256 of its
                # exact source string must match the acknowledgment. An altered quote, a renamed
                # external, or a new file reusing a listed name falls through and stays a hard FAIL.
                if ack and ack["file"] == f.name and \
                        ack["source_sha256"] == hashlib.sha256(src.encode("utf-8")).hexdigest():
                    res["verdict"] = "skip_absent_ack"
                    res["note"] = (f"payload {res['absent_path']} ABSENT but ACKNOWLEDGED "
                                   f"(repository-tracked policy, activated by local payload "
                                   f"absence: refs/manifest/absent-acknowledged.json; restore "
                                   f"bead {ack['restore_bead']}) — this exact external (filename + "
                                   f"source digest bound) was byte-verified before the payload went "
                                   f"absent; verification resumes automatically on restore")
            rows.append(res)
    fail_count = sum(1 for r in rows if r["verdict"] == "fail")
    skip_count = sum(1 for r in rows if r["verdict"].startswith("skip"))
    return rows, fail_count, skip_count


def main(argv):
    check_mode = "--check" in argv
    rows, fail_count, skip_count = check_refs()
    symbol = {"pass": "PASS ", "fail": "FAIL ",
              "skip_import": "skip ", "skip_noquote": "WARN ", "skip_absent_ack": "ACK! "}
    for r in rows:
        line = (f"[{symbol.get(r['verdict'], '?????')}] {r['workspace']:38s} "
                f"{r['external']:24s} {r['verdict']:12s} {r['refs_locus'] or '-'}")
        print(line)
        if r["verdict"] == "fail":
            print(f"           ! {r['note']}")
            if r["claimed_quote_snippet"]:
                print(f"           ! claimed: {r['claimed_quote_snippet']!r}")
        elif r["verdict"] in ("skip_noquote", "skip_absent_ack"):
            print(f"           (warn) {r['note']}")
    total = len(rows)
    ack_count = sum(1 for r in rows if r["verdict"] == "skip_absent_ack")
    ack_note = (f" (of which {ack_count} ACKNOWLEDGED-ABSENT — repository-tracked policy, "
                f"activated by local payload absence; see refs/manifest/absent-acknowledged.json)"
                if ack_count else "")
    print(f"\ncheck-refs: {total} externals, {fail_count} failed, {skip_count} skipped{ack_note}")
    if check_mode and fail_count:
        print("check-refs: FAILED — fabricated/mismatched verbatim quote(s) above.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
