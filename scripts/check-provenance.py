#!/usr/bin/env python3
r"""
check-provenance.py — report <-> argument-registry sync gate (the Phase-2b "CI for the paper").

THE FAILURE MODE THIS GUARDS AGAINST: the human-readable report (report/sections/*.tex +
report/PROVENANCE.md) silently DRIFTS from the machine-checked argument (argument/lemmas/*.md +
proofs/). A lemma gets renamed, validated, downgraded, or removed in the registry, but the paper still
references the old label / still calls a now-proved result "open" / still cites a now-edited source by a
stale hash — and nobody notices because nothing compares the two. This gate compares them.

THE JOIN KEY. A registry shard's `provenance:` line carries a `report <label>` token (e.g.
`provenance: bridge md:301-372; report lem:bridge-squarehole`). That token is the authoritative
registry->report link (the ids are NOT a string transform: lem-square-hole-almost-positive maps to
lem:bridge-squarehole). When a shard lacks the token we fall back to the first-hyphen->colon transform
(lem-P-properties -> lem:P-properties) iff that label exists in the .tex.

CHECKS (errors block the commit; warnings are surfaced but do not):
  ERROR  forward labels     every registry `report <label>` token resolves to a \label{} in sections/*.tex
  ERROR  claim labels       every report/PROVENANCE.md per-claim row label resolves to a \label{}
  ERROR  claim sources      every per-claim row cites a Source key defined in the source registry
  ERROR  hash freshness     every IN-REPO source-registry file's sha256[:16] matches the recorded hash
                            (every source ROW is hashed, even when a key is reused for two files)
  ERROR  sha format         every source-registry sha is exactly 16 lowercase hex
  ERROR  status OVERCLAIM   a registry status=open result framed as proved/benchmark (never `open`) in
                            tab:status — the project's #1 guarded failure mode (a confident WRONG claim)
  ERROR  build (--build)    `latexmk` compiles the report AND the log has no undefined references
  WARN   reverse labels     a report result-label (thm/lem/prop/cor/op/obs/ex:) with no registry backref
  WARN   anchor             a registry result mapping to ZERO report labels (dropped/unlinked statement)
  WARN   coverage           a report-facing registry result with no per-claim PROVENANCE row
  WARN   status underclaim  a proved/validated result framed ONLY `open` in tab:status
  WARN   parse integrity    a `|`-data line in a recognized PROVENANCE block that failed to parse, or a
                            duplicate source key — i.e. a row that would otherwise be SILENTLY dropped
  WARN   absent payloads    source files gitignored/absent locally (hash unverifiable) — summarised
  WARN   stale abs path     a source-registry path is an absolute /home/... path, not refs/-relative

LIMITATIONS (the known false-green surface — a green run does NOT certify these; do not over-trust it):
  * STATEMENT TEXT is not checked. The gate joins label<->label only; it never compares a registry
    `contract` to the report theorem body, so a weakened hypothesis or a sqrt(eta)<->eta change drifts
    green. The registry `contract` remains the single source of truth; this gate guards the *wiring*.
  * STATUS drift is seen only for results tab:status actually \Cref's (a curated subset; range rows like
    `\Cref{a}--\ref{b}` cover only the endpoints). A flip on an un-listed result is not caught.
  * proofs/ af-validation state is not read here (the argument linker owns that).
  * HASH freshness only covers IN-REPO source files; gitignored/external payloads (~1/3 of sources) only
    warn — an edit to one of those is not hash-detectable from this clone.

Pure check functions (unit-tested in scripts/tests/test_check_provenance.py) take parsed inputs so they
run on synthetic fixtures; main() builds those inputs from the filesystem and (for --build) latexmk.

Usage:
  python3 scripts/check-provenance.py            # semantic checks only; per-check report + summary
  python3 scripts/check-provenance.py --check    # same; exit non-zero iff any ERROR (the gate mode)
  python3 scripts/check-provenance.py --build     # also compile the report (latexmk) into a scratch dir
"""
import hashlib
import pathlib
import re
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
ARG_DIR = ROOT / "argument"
SECTIONS = ROOT / "report" / "sections"
PROVENANCE = ROOT / "report" / "PROVENANCE.md"
REPORT_DIR = ROOT / "report"
BUILD_DIR = REPORT_DIR / ".build"

LABEL = r"[a-z]+:[A-Za-z0-9-]+"             # slugs may carry uppercase (lem:P-properties)
LABEL_RE = re.compile(r"\\label\{(" + LABEL + r")\}")
REPORT_TOK = re.compile(r"report\s+(" + LABEL + r")")
RESULT_KINDS = {"thm", "lem", "prop", "cor", "op", "obs", "ex"}
# Source-cell tokens that are markers/external citations, NOT internal source-registry keys.
SOURCE_ALLOW = {"ORIGINAL", "OPEN", "ELEMENTARY", "EXTRACT", "PDF", "CONSENSUS", "MODEL", "V", "I", "O"}
# A registry key is an ALL-CAPS-namespace token (HOS, KIT, A-FIT, ES-P05, TS3, B-NPPS). Splitting on
# separators and matching the WHOLE token means mixed-case external citations (Kadison1952, JvNW1934)
# are never mistaken for keys.
_KEY_TOKEN = re.compile(r"[A-Z0-9][A-Z0-9-]*")
_EXTERN_YEAR = re.compile(r"[A-Z]+[0-9]{3,}")   # an all-caps citation+year, not a key


# ---------------- parsing ----------------

def strip_tex_comment(line):
    """Drop a TeX %-comment to end-of-line, honouring an escaped \\%. Pure (one line in, one out)."""
    out = []
    i = 0
    while i < len(line):
        c = line[i]
        if c == "\\" and i + 1 < len(line):
            out.append(line[i:i + 2])
            i += 2
            continue
        if c == "%":
            break
        out.append(c)
        i += 1
    return "".join(out)


def _frontmatter(path):
    text = path.read_text(encoding="utf-8-sig")   # utf-8-sig strips a leading BOM
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    fm = {}
    for line in text[3:end].splitlines():
        line = line.rstrip()
        if not line or line.lstrip().startswith("#") or ":" not in line:
            continue
        k, v = line.split(":", 1)
        fm[k.strip()] = v.strip()
    return fm


def parse_registry(arg_dir=ARG_DIR):
    """Read argument/lemmas/*.md -> [{id,status,af,provenance,kind}, ...]."""
    out = []
    lemdir = pathlib.Path(arg_dir) / "lemmas"
    for path in sorted(lemdir.glob("*.md")) if lemdir.exists() else []:
        if path.name in ("README.md", "INDEX.md"):
            continue
        fm = _frontmatter(path)
        if fm is None:
            continue
        fm.setdefault("id", path.stem)
        out.append(fm)
    return out


def tex_labels(sections=SECTIONS):
    """\\label{} names defined in sections/*.tex, EXCLUDING any inside a %-comment (a commented-out
    \\label must not count as a live label, else a commented-out result reads as still present)."""
    labels = set()
    sections = pathlib.Path(sections)
    for f in sorted(sections.glob("*.tex")) if sections.exists() else []:
        for line in f.read_text(encoding="utf-8").splitlines():
            labels |= set(LABEL_RE.findall(strip_tex_comment(line)))
    return labels


def _md_cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def _is_data_row(cells, header):
    """A markdown '|'-line that is neither the column header nor a |---| separator."""
    return cells and cells[0] not in header and not (set(cells[0]) <= set("-: "))


def parse_provenance(prov_path=PROVENANCE):
    """Parse report/PROVENANCE.md. Returns a dict with:
      source_registry: {key: (path, sha)}     — last-wins, used for claim-source membership
      source_rows:     [(key, path, sha), ...] — EVERY row, used for hashing (a reused key hashes BOTH)
      claim_rows:      [(label, source_cell), ...]
      parse_warnings:  [str, ...]              — a recognized data row that failed to parse, or a dup key
                                                 (so a would-be SILENT drop is surfaced, not swallowed)
    """
    prov_path = pathlib.Path(prov_path)
    out = {"source_registry": {}, "source_rows": [], "claim_rows": [], "parse_warnings": []}
    if not prov_path.exists():
        return out
    text = prov_path.read_text(encoding="utf-8-sig")

    if "## Ground-truth source registry" in text:
        blk = text.split("## Ground-truth source registry", 1)[1].split("\n## ", 1)[0]
        for line in blk.splitlines():
            if not line.strip().startswith("|"):
                continue
            cells = _md_cells(line)
            if not _is_data_row(cells, ("Key",)) or len(cells) < 3:
                continue
            km = re.search(r"`([^`]+)`", cells[0])
            pm = re.search(r"`([^`]+)`", cells[1])
            sm = re.search(r"`?([0-9a-f]{6,})`?", cells[2])
            if not (km and pm and sm):
                out["parse_warnings"].append(f"unparseable source-registry row: {line.strip()[:70]}")
                continue
            key, path, sha = km.group(1).strip(), pm.group(1).strip(), sm.group(1).strip()
            if key in out["source_registry"] and out["source_registry"][key] != (path, sha):
                out["parse_warnings"].append(f"source key '{key}' is defined twice (both rows are hashed)")
            out["source_registry"][key] = (path, sha)
            out["source_rows"].append((key, path, sha))

    if "## Per-claim ledger" in text:
        blk = text.split("## Per-claim ledger", 1)[1]
        for line in blk.splitlines():
            if not line.strip().startswith("|"):
                continue
            cells = _md_cells(line)
            if not _is_data_row(cells, ("Report label",)) or len(cells) < 2:
                continue
            if re.fullmatch(LABEL, cells[0]):
                out["claim_rows"].append((cells[0], cells[1]))
            else:
                out["parse_warnings"].append(f"per-claim row label not a clean label, row skipped: {cells[0]!r}")
    return out


def status_table_rows(sections=SECTIONS):
    """Parse the tab:status table in 11-discussion.tex -> [(status_cell_lower, [labels]), ...]."""
    f = pathlib.Path(sections) / "11-discussion.tex"
    if not f.is_file():
        return []
    text = f.read_text(encoding="utf-8")
    if r"\label{tab:status}" not in text or r"\midrule" not in text:
        return []
    body = text.split(r"\label{tab:status}", 1)[0]
    body = body[body.rfind(r"\midrule") + len(r"\midrule"):]
    body = body.split(r"\bottomrule", 1)[0]
    body = "\n".join(strip_tex_comment(ln) for ln in body.splitlines())  # drop %-comments first
    rows = []
    for raw in body.split(r"\\"):
        cols = re.split(r"(?<!\\)&", raw)   # column separator is an UNescaped & (a literal \& is text)
        if len(cols) < 2:
            continue
        status_cell = cols[1].strip().lower()
        labels = re.findall(r"\\(?:Cref|ref)\{(" + LABEL + r")\}", raw)
        if labels:
            rows.append((status_cell, labels))
    return rows


# ---------------- join ----------------

def labels_of(shard, texlabels):
    """Report labels a registry shard maps to: explicit `report <label>` tokens, plus the
    first-hyphen->colon transform of its id iff that label exists in the .tex."""
    labs = set(REPORT_TOK.findall(shard.get("provenance", "")))
    cand = shard["id"].replace("-", ":", 1)
    if cand in texlabels:
        labs.add(cand)
    return labs


# ---------------- pure checks ----------------

def check_forward_labels(shards, texlabels):
    errors = []
    for s in shards:
        for lab in REPORT_TOK.findall(s.get("provenance", "")):
            if lab not in texlabels:
                errors.append(f"{s['id']}: provenance names report '{lab}' but no \\label{{{lab}}} in sections/")
    return errors


def check_reverse_labels(shards, texlabels):
    linked = set()
    for s in shards:
        linked |= labels_of(s, texlabels)
    warnings = []
    for lab in sorted(texlabels):
        if lab.split(":")[0] in RESULT_KINDS and lab not in linked:
            warnings.append(f"report \\label{{{lab}}} has no registry result backing it (orphan statement?)")
    return warnings


def check_claim_labels(claim_rows, texlabels):
    errors = []
    for lab, _src in claim_rows:
        if lab not in texlabels:
            errors.append(f"PROVENANCE per-claim row '{lab}' has no \\label{{{lab}}} in sections/ (stale ledger row)")
    return errors


def check_claim_sources(claim_rows, source_registry):
    keys = set(source_registry)
    errors = []
    for lab, src in claim_rows:
        for tok in re.split(r"[\s/,;()|]+", src):   # include ; and | so 'HOS;GHOST' splits
            tok = tok.strip().strip("`")
            if len(tok) < 2 or tok in SOURCE_ALLOW or tok in keys:
                continue
            if _KEY_TOKEN.fullmatch(tok) and not _EXTERN_YEAR.fullmatch(tok):
                errors.append(f"PROVENANCE row '{lab}': Source key '{tok}' not in the source registry")
    return errors


def check_coverage(shards, claim_rows, texlabels):
    claim_labels = {lab for lab, _ in claim_rows}
    warnings = []
    for s in shards:
        labs = labels_of(s, texlabels)
        if labs and not (labs & claim_labels):
            warnings.append(f"{s['id']} (report {sorted(labs)}): no per-claim PROVENANCE row")
    return warnings


def check_status_drift(status_rows, shards, texlabels):
    """Compare registry status to how tab:status frames each result. Returns (errors, warnings).

    OVERCLAIM (status=open framed only non-open) is an ERROR — it is the project's #1 guarded failure
    mode (a confident WRONG claim: the paper calling an open problem 'proved'). UNDERCLAIM (a proved/
    validated result framed only 'open') is a WARNING. The form is "a consistent row must exist": a
    result Cref'd by several rows (e.g. op-npps, which is both its own open row AND the condition of a
    'proved, cond.' row) is fine as long as one row frames it consistently with the registry."""
    id_of_label = {}
    for s in shards:
        for lab in labels_of(s, texlabels):
            id_of_label[lab] = s["id"]
    status_of = {s["id"]: s.get("status") for s in shards}
    af_of = {s["id"]: s.get("af", "none") for s in shards}
    cells_of = {}
    for cell, labels in status_rows:
        for lab in labels:
            rid = id_of_label.get(lab)
            if rid:
                cells_of.setdefault(rid, set()).add(cell)
    errors, warnings = [], []
    for rid, cells in cells_of.items():
        any_open = any(c == "open" for c in cells)
        any_nonopen = any(c != "open" for c in cells)
        if status_of.get(rid) == "open" and not any_open:
            errors.append(f"OVERCLAIM {rid}: registry status=open but tab:status frames it {sorted(cells)} "
                          f"(never 'open') — the paper claims an open result is settled")
        if (af_of.get(rid) == "validated" or status_of.get(rid) == "proved") and not any_nonopen:
            warnings.append(f"{rid}: registry {status_of.get(rid)}/{af_of.get(rid)} but tab:status frames it only 'open'")
    return errors, warnings


def check_anchor(shards, texlabels):
    """A registry result that maps to ZERO report labels (no `report <label>` token and no id-transform
    hit) is an unanchored/dropped statement — surfaced as a WARN (catches a whole-section cut or a new
    shard never wired into the paper). Today every shard anchors, so this is silent until something drops."""
    warnings = []
    for s in shards:
        if not labels_of(s, texlabels):
            warnings.append(f"{s['id']}: maps to NO report label (dropped from the paper, or never wired in)")
    return warnings


def check_source_hashes(source_rows, root=ROOT, tracked=None):
    """Recompute sha256[:16] of EVERY canonical source row. Returns (errors, warnings).

    `source_rows` is the [(key, path, sha), ...] list (so a key reused for two files hashes BOTH);
    a {key: (path, sha)} dict is also accepted for unit-testing convenience.

    `tracked`, when given, is the set of git-tracked repo-relative paths. Hash-freshness HARD-ERRORS
    only on TRACKED (committed) sources, so the verdict is identical in a clean CI checkout and on a
    developer's populated tree; gitignored/untracked/absent payloads only WARN (they are not canonical
    and cannot be checked from a clean checkout). With tracked=None every present file is hashed (the
    unit-test convenience)."""
    if isinstance(source_rows, dict):
        source_rows = [(k, p, s) for k, (p, s) in source_rows.items()]
    root = pathlib.Path(root)
    errors, warnings, unverifiable = [], [], []
    for key, path, sha in source_rows:
        if not re.fullmatch(r"[0-9a-f]{16}", sha):
            errors.append(f"source '{key}': sha '{sha}' is not 16 lowercase hex")
            continue
        if path.startswith("/"):
            warnings.append(f"source '{key}': absolute path '{path}' (not refs/-relative); hash unverifiable")
            continue
        if tracked is not None and path not in tracked:
            unverifiable.append(key)   # gitignored/untracked => not canonical => warn, never block
            continue
        p = root / path
        if not p.is_file():
            unverifiable.append(key)
            continue
        actual = hashlib.sha256(p.read_bytes()).hexdigest()[:16]
        if actual != sha:
            errors.append(f"source '{key}': recorded {sha} != actual {actual} ({path}) — file edited, hash stale")
    if unverifiable:
        warnings.append(f"{len(unverifiable)} source payload(s) not hash-verifiable here "
                        f"(gitignored/untracked/absent — not in a clean checkout): "
                        + ", ".join(sorted(set(unverifiable))))
    return errors, warnings


def git_tracked(root=ROOT):
    """Set of git-tracked repo-relative paths, or None if git is unavailable / not a repo. Lets
    check_source_hashes hard-error only on committed (canonical) sources."""
    try:
        out = subprocess.run(["git", "-C", str(root), "ls-files"],
                             capture_output=True, text=True, timeout=30)
    except Exception:   # noqa: BLE001
        return None
    return set(out.stdout.splitlines()) if out.returncode == 0 else None


# ---------------- integration: latexmk build ----------------

def scan_build_log(txt):
    """Pure: scan a latexmk/pdflatex .log for drift signals. Returns (errors, warnings).

    An UNDEFINED reference is the load-bearing drift: a \\Cref/\\ref to a label that was renamed or
    removed in the report (or pointed at a registry id the paper never defined). latexmk -halt-on-error
    does NOT fail on these (they are warnings), so we promote them to errors here."""
    errors, warnings = [], []
    if "There were undefined references" in txt or re.search(r"Reference `[^']+' on page", txt):
        refs = sorted(set(re.findall(r"Reference `([^']+)' on page", txt)))
        errors.append("report has UNDEFINED references (dangling \\ref/\\Cref to a renamed/removed label): "
                      + (", ".join(refs) if refs else "(see report/.build/main.log)"))
    if "There were undefined citations" in txt or re.search(r"Citation `[^']+' on page", txt):
        warnings.append("report has undefined citations (missing .bib entries)")
    return errors, warnings


def run_build(report_dir=REPORT_DIR, build_dir=BUILD_DIR):
    """Compile the report into a scratch dir (never touches the tracked main.pdf), then scan_build_log.
    Returns (errors, warnings). Skips with a warning if latexmk is absent."""
    report_dir = pathlib.Path(report_dir)
    if not shutil.which("latexmk"):
        return [], ["latexmk not on PATH — report build SKIPPED (cannot verify the paper compiles)"]
    build_dir = pathlib.Path(build_dir)
    build_dir.mkdir(parents=True, exist_ok=True)
    try:
        proc = subprocess.run(
            ["latexmk", "-pdf", "-interaction=nonstopmode", "-halt-on-error",
             f"-output-directory={build_dir}", "main.tex"],
            cwd=str(report_dir), capture_output=True, text=True, timeout=600)
    except subprocess.TimeoutExpired:
        return ["latexmk timed out after 600s compiling report/main.tex"], []
    if proc.returncode != 0:
        tail = "\n".join((proc.stdout or "").splitlines()[-15:])
        return ["latexmk failed to compile report/main.tex:\n" + tail], []
    log = build_dir / "main.log"
    if log.is_file():
        return scan_build_log(log.read_text(encoding="utf-8", errors="replace"))
    return [], []


# ---------------- main ----------------

def run_semantic():
    shards = parse_registry()
    texlabels = tex_labels()
    prov = parse_provenance()
    claim_rows = prov["claim_rows"]
    src_reg = prov["source_registry"]

    errors, warnings = [], []
    groups = []  # (name, errs, warns) for the per-check report

    def grp(name, errs=(), warns=()):
        errs, warns = list(errs), list(warns)
        groups.append((name, errs, warns))
        errors.extend(errs)
        warnings.extend(warns)

    grp("forward labels", check_forward_labels(shards, texlabels))
    grp("claim labels", check_claim_labels(claim_rows, texlabels))
    grp("claim sources", check_claim_sources(claim_rows, src_reg))
    he, hw = check_source_hashes(prov["source_rows"], tracked=git_tracked())
    grp("hash freshness", he, hw)
    se, sw = check_status_drift(status_table_rows(), shards, texlabels)
    grp("status drift", se, sw)
    grp("anchor", (), check_anchor(shards, texlabels))
    grp("reverse labels", (), check_reverse_labels(shards, texlabels))
    grp("coverage", (), check_coverage(shards, claim_rows, texlabels))
    grp("parse integrity", (), prov["parse_warnings"])
    return shards, texlabels, prov, groups, errors, warnings


def main(argv):
    argv = list(argv)
    check_mode = "--check" in argv
    do_build = "--build" in argv

    shards, texlabels, prov, groups, errors, warnings = run_semantic()

    if do_build:
        be, bw = run_build()
        groups.append(("build (latexmk)", be, bw))
        errors.extend(be)
        warnings.extend(bw)

    for name, errs, warns in groups:
        sym = "FAIL" if errs else ("warn" if warns else "OK  ")
        print(f"[{sym}] {name}")
        for w in warns:
            print(f"        (warn) {w}")
        for e in errs:
            print(f"        ! {e}")

    print(f"\ncheck-provenance: {len(shards)} registry results, {len(prov['claim_rows'])} claim rows, "
          f"{len(texlabels)} tex labels — {len(errors)} errors, {len(warnings)} warnings")
    if check_mode and errors:
        print("check-provenance: FAILED — report/registry drift above.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
