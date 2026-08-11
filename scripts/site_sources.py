#!/usr/bin/env python3
"""
site_sources.py — canonical-source PARSERS for the site data layer (Phase 1, slate J of
docs/plans/2026-08-11-communication-artifacts-plan.md; design principle P1 "truth from canon,
enforced": every number on every surface is generated from repo data, never hand-entered).

Read-only. Stdlib only. Deterministic (no timestamps, no commit SHAs, no network).

Each function returns plain data for scripts/gen-site-data.py to project into site/data/*.json:
  registry()          argument/lemmas/*.md   (delegated to scripts/argument.py — ONE parser, L2)
  definitions()       definitions/def-*.md   (check-defs.py field conventions + body text)
  ledger_events()     proofs/*/ledger/*.json (af event tallies)
  workspaces()        proofs/*/              (seeded vs exported/validated)
  learnings()         docs/LEARNINGS.md      (dated retraction entries; HTML-comment template excluded)
  run_bundles()       runs/<date>-<slug>/    (headline finding, verbatim from the README)
  frontier()          .frontier/log.jsonl    (wave log + the T0-over-time series)
  refs_manifest()     refs/manifest/checksums.sha256
  externals()         proofs/*/externals/*.json (delegated to scripts/check-refs.py)

NOTHING here judges truth: these are transcriptions of the canonical record (CLAUDE.md L0/L1).
"""
import importlib.util
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"


def _load(path, name):
    """Import a hyphenated script (check-refs.py) as a module — stdlib importlib."""
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ---------- Layer 1: the argument registry (reuse argument.py's parser, never a second one) ----------

def registry(root=ROOT):
    """The parsed registry shards, exactly as the linker sees them: list of frontmatter dicts
    with id/kind/status/af/owner/contract/defs/deps/routes (+ provenance/workspace when present)."""
    if str(SCRIPTS) not in sys.path:
        sys.path.insert(0, str(SCRIPTS))
    import argument  # noqa: PLC0415 — the canonical registry parser
    lemmas, errors = argument.parse_registry(pathlib.Path(root) / "argument")
    return lemmas, errors, argument


# ---------- Layer 0: definitions ----------

def definitions(root=ROOT):
    """definitions/def-*.md -> [{id, term, aliases, kind, status, source, locus, consensus, body}]
    using check-defs.py's frontmatter parser (its field conventions are canonical)."""
    cd = _load(SCRIPTS / "check-defs.py", "check_defs_mod")
    out = []
    for path in sorted((pathlib.Path(root) / "definitions").glob("def-*.md")):
        errs = []
        fm, body = cd.parse_frontmatter(path, errs)
        if fm is None:
            continue
        out.append({
            "id": fm.get("id", path.stem),
            "term": fm.get("term", ""),
            "aliases": [a.strip() for a in (fm.get("aliases", "") or "").split(";") if a.strip()],
            "kind": fm.get("kind", ""),
            "status": fm.get("status", ""),
            "source": fm.get("source", ""),
            "locus": fm.get("locus", ""),
            "consensus": fm.get("consensus", ""),
            "body": body.strip(),
        })
    return out


# ---------- Layer 2: af workspaces + ledgers ----------

def ledger_events(root=ROOT):
    """Tally every proofs/<ws>/ledger/*.json event by its "type" field.
    Returns (counts_by_type, files_read, unparseable)."""
    counts, files, bad = {}, 0, 0
    for f in sorted((pathlib.Path(root) / "proofs").glob("*/ledger/*.json")):
        files += 1
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            bad += 1
            continue
        for ev in data if isinstance(data, list) else [data]:
            if isinstance(ev, dict):
                counts[ev.get("type", "unknown")] = counts.get(ev.get("type", "unknown"), 0) + 1
    return counts, files, bad


def workspaces(root=ROOT):
    """proofs/<id>/ -> {total, with_ledger, exported} (exported == an export.md exists, i.e. the
    tree reached a clean root validation and was exported)."""
    pdir = pathlib.Path(root) / "proofs"
    dirs = sorted(d for d in pdir.iterdir() if d.is_dir()) if pdir.is_dir() else []
    return {
        "total": len(dirs),
        "with_ledger": sum(1 for d in dirs if (d / "ledger").is_dir()),
        "exported": sum(1 for d in dirs if (d / "export.md").is_file()),
        "ids": [d.name for d in dirs],
        "exported_ids": [d.name for d in dirs if (d / "export.md").is_file()],
    }


def externals(root=ROOT):
    """Verdict tally over proofs/*/externals/*.json, computed by check-refs.py itself (so the
    site can never disagree with the gate): {total, byte_matched, imports, no_quote, ...}."""
    cr = _load(SCRIPTS / "check-refs.py", "check_refs_mod")
    rows, fails, _ = cr.check_refs(proofs_dir=pathlib.Path(root) / "proofs")
    tally = {}
    for r in rows:
        tally[r["verdict"]] = tally.get(r["verdict"], 0) + 1
    return {
        "total": len(rows),
        "byte_matched_quotes": tally.get("pass", 0),
        "workspace_imports": tally.get("skip_import", 0),
        "no_quote": tally.get("skip_noquote", 0),
        "absent_acknowledged": tally.get("skip_absent_ack", 0),
        "failed": fails,
    }


# ---------- the backstop: docs/LEARNINGS.md ----------

_COMMENT_RE = re.compile(r"<!--.*?-->", re.S)
_HEAD_RE = re.compile(r"^## (\d{4}-\d{2}-\d{2})([^—\n]*)—\s*(.*)$")
_BULLET_RE = re.compile(r"^- \*\*(.+?):\*\*\s*(.*)$")
_FIELD_KEY = {"claimed": "claimed", "why wrong": "why_wrong", "caught by": "caught_by",
              "resolution": "resolution"}


def _field_key(label):
    """'Why wrong (in part)' -> why_wrong; unknown labels keep a slugged key under `extra`."""
    base = label.split("(")[0].strip().lower()
    return _FIELD_KEY.get(base), re.sub(r"[^a-z0-9]+", "_", label.strip().lower()).strip("_")


def learnings(root=ROOT):
    """docs/LEARNINGS.md -> [{date, title, qualifier, claimed, why_wrong, caught_by, resolution,
    extra}]. HTML comments (the entry TEMPLATE and the role header) are stripped first, so the
    template's `## YYYY-MM-DD` line is NOT counted as a retraction."""
    path = pathlib.Path(root) / "docs" / "LEARNINGS.md"
    if not path.is_file():
        return []
    text = _COMMENT_RE.sub("", path.read_text(encoding="utf-8"))
    entries, cur, field, buf = [], None, None, []

    def flush():
        if cur is not None and field is not None:
            body = "\n".join(buf).strip()
            key, slug = field
            (cur if key else cur["extra"])[key or slug] = body

    for line in text.splitlines():
        h = _HEAD_RE.match(line)
        if h:
            flush()
            cur, field, buf = {"date": h.group(1), "qualifier": h.group(2).strip(),
                               "title": h.group(3).strip(), "claimed": "", "why_wrong": "",
                               "caught_by": "", "resolution": "", "extra": {}}, None, []
            entries.append(cur)
            continue
        if cur is None:
            continue
        b = _BULLET_RE.match(line)
        if b:
            flush()
            field, buf = _field_key(b.group(1)), [b.group(2)]
        elif field is not None:
            buf.append(line.strip())
    flush()
    return entries


# ---------- L3 evidence: runs/ ----------

_HEADLINE_HEAD_RE = re.compile(r"^#{2,4}\s+.*(headline|finding)", re.I)
_SKIP_LINE_RE = re.compile(r"^\s*$|^\s*[-*_]{3,}\s*$|^```")


def _headline(readme_text):
    """The bundle's stated headline finding, verbatim: the first non-empty prose line under the
    first `## ... Headline/Finding ...` heading; else the first prose line after the `# ` title."""
    lines = readme_text.splitlines()
    starts = [i for i, l in enumerate(lines) if _HEADLINE_HEAD_RE.match(l)]
    start = (starts[0] + 1) if starts else next((i + 1 for i, l in enumerate(lines)
                                                 if l.startswith("# ")), 0)
    para = []
    for l in lines[start:]:
        if _SKIP_LINE_RE.match(l):
            if para:
                break
            continue
        if l.startswith("#"):
            break
        para.append(l.strip())
        if len(" ".join(para)) > 300:
            break
    out = " ".join(para).strip()
    return (out[:300].rstrip() + "…") if len(out) > 300 else out


def run_bundles(root=ROOT):
    """runs/<YYYY-MM-DD>-<slug>/ -> [{bundle, date, slug, title, headline}] (README.md is the
    schema doc, not a bundle — check-runs.py's SKIP rule)."""
    rdir = pathlib.Path(root) / "runs"
    out = []
    for d in sorted(p for p in rdir.iterdir() if p.is_dir()) if rdir.is_dir() else []:
        m = re.match(r"^(\d{4}-\d{2}-\d{2})-(.+)$", d.name)
        readme = d / "README.md"
        text = readme.read_text(encoding="utf-8") if readme.is_file() else ""
        title = next((l[2:].strip() for l in text.splitlines() if l.startswith("# ")), "")
        out.append({"bundle": d.name,
                    "date": m.group(1) if m else "",
                    "slug": m.group(2) if m else d.name,
                    "title": title,
                    "headline": _headline(text)})
    return out


# ---------- the controller: .frontier/log.jsonl ----------

# Liberal T0 extraction: "T0 34", "T0 at 34", "T0 29 -> 31", "T0 156->157", "T0 #30", "T0 = 42".
# The chain's LAST integer is the value AFTER the wave. Three-digit cap excludes years/dates.
# A parenthesized count ("T0 (199 -> 200)", "T0 (200/374)") counts ONLY when the digits close the
# parenthetical — "rows are now all T0 (7 polar results...)" is prose, not a count (cycle 755).
_CHAIN = r"(?:[ \t]*(?:->|→|-＞|to)[ \t]*\d{1,3})*"
_T0_RE = re.compile(r"T0\b[ \t]*(?:"
                    r"\(\d{1,3}" + _CHAIN + r"(?=[)/,])"
                    r"|(?:@|=|:|#|at|is|now|to|->|→|-＞)?[ \t]*\d{1,3}" + _CHAIN +
                    r")")
_INT_RE = re.compile(r"\d{1,3}")


def _t0_of(note, max_t0):
    """The last T0 count mentioned in a note, or None. `max_t0` bounds implausible captures."""
    val = None
    for m in _T0_RE.finditer(note or ""):
        n = int(_INT_RE.findall(m.group(0))[-1])
        if 1 <= n <= max_t0:
            val = n
    return val


def frontier(root=ROOT, note_chars=400, max_t0=400):
    """.frontier/log.jsonl -> (entries, t0_timeline). Entries keep {ts, cycle, arm, outcome,
    note (truncated)}; the timeline is the {ts, cycle, t0} points parsed out of the notes — the
    campaign-replay series, de-banking dips included (T0 can go DOWN: retractions are recorded)."""
    path = pathlib.Path(root) / ".frontier" / "log.jsonl"
    entries, timeline = [], []
    if not path.is_file():
        return entries, timeline
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            d = json.loads(line)
        except ValueError:
            continue
        note = d.get("note") or ""
        entries.append({"ts": d.get("ts", ""), "cycle": d.get("cycle"), "arm": d.get("arm"),
                        "outcome": d.get("outcome", ""),
                        "note": note[:note_chars] + ("…" if len(note) > note_chars else "")})
        t0 = _t0_of(note, max_t0)
        if t0 is not None:
            timeline.append({"ts": d.get("ts", ""), "cycle": d.get("cycle"), "t0": t0})
    return entries, timeline


# ---------- ground truth: refs/ ----------

def refs_manifest(root=ROOT):
    """refs/manifest/checksums.sha256 -> {sources: [source-id], pinned_files: n, present_files: n}."""
    refs = pathlib.Path(root) / "refs"
    man = refs / "manifest" / "checksums.sha256"
    sources, pinned, present = set(), 0, 0
    for line in man.read_text(encoding="utf-8").splitlines() if man.is_file() else []:
        m = re.match(r"^([0-9a-f]{64})( \*|  )(.+)$", line.strip("\n"))
        if not m:
            continue
        p = m.group(3)[2:] if m.group(3).startswith("./") else m.group(3)
        pinned += 1
        if "/" in p:
            sources.add(p.split("/", 1)[0])
        if (refs / p).is_file():
            present += 1
    return {"sources": sorted(sources), "pinned_files": pinned, "present_files": present}
