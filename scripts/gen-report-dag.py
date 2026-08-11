#!/usr/bin/env python3
r"""
gen-report-dag.py — generate the report's ROUTE-F PROOF-CHAIN ATLAS (LaTeX/TikZ) from the
argument registry shards.

WHAT IT DRAWS.  NOT the whole 262-result registry (unreadable, and most of it is not on the
landing path).  It draws exactly the sub-DAG that carries the argument landing `op-classical`:

    SUBGRAPH  =  transitive closure, along registry `deps:` and `routes:` edges, of
                 { op-classical }  U  ROUTE_F_SEEDS

where ROUTE_F_SEEDS are the Route-F families named in the live proof strategy
(docs/plans/CURRENT.md): lem-routef-*, lem-thmainext-*, lem-stage1-*, lem-maincb-*,
lem-extcb*, lem-hcb*, lem-compcb-*, lem-topology-*, conj-hcb, conj-extcb, the Kitaev
repair/audit rows, lem-prh(+sharpness), prop-f2-t1-equivalence, lem-classical-equiv, ex-hume.
The seeds keep the whole Route-F front on the page even where a family does not (yet) reach
the root through registry edges; any composition the live strategy reserves but has NOT wired
into the registry is drawn as a design-pending GAP link (see GAP_EDGE_CANDIDATES below), so the atlas
shows exactly where — if anywhere — the chain is still open.  Both the GAP set and every
status sentence in the generated prose are DERIVED from the shards at generation time; no
status claim is hardcoded here.

SOURCE OF TRUTH.  argument/lemmas/*.md, parsed by scripts/argument.py's own parser
(imported, never re-implemented) — so this atlas and the generated Mermaid twin
argument/DAG.md can never disagree about the data.  Node colour classes come from
argument.proof_class(), the SAME function that colours the Mermaid graph.

DETERMINISM.  No timestamps, no randomness, no environment reads.  Every iteration is over a
sorted collection; every coordinate is rounded to 3 decimals.  Re-running on unchanged shards
reproduces the output byte-for-byte; `--check` fails if the committed output would differ.

ANCHORS (the crosslink contract; documented in the generated section and in report/README.md):
    dag:<registry-id>     \hypertarget on the result's node in the atlas   (e.g. dag:lem-prh)
    dag:<definition-id>   \hypertarget on the definition's row             (e.g. dag:def-height)
    dag:phase:<key>       \hypertarget on a phase heading                  (e.g. dag:phase:comp)
    sec:argument-dag, tab:dag-legend, tab:dag-index, tab:dag-defs, fig:dag-<key>   \label's
Link INTO the atlas from anywhere in the report with \dagref{<id>} / \dagdef{<id>}
(defined in the generated preamble).  The atlas links BACK to a result's report statement
whenever the registry shard's `provenance:` names one (`report <label>`), or when the
first-hyphen->colon transform of the id is a \label that exists in report/sections/.

USAGE
    python3 scripts/gen-report-dag.py            # (re)write the generated files
    python3 scripts/gen-report-dag.py --check    # exit 1 if any committed file is STALE
    python3 scripts/gen-report-dag.py --stats    # print the subgraph statistics, write nothing
    python3 scripts/gen-report-dag.py --repo DIR --out-root DIR   # read/write elsewhere (testing)

OUTPUTS (all carry a "% GENERATED - do not hand-edit" header)
    report/sections/39_argument_dag.tex   the lab-book shard (\section + prose + \input's)
    report/generated/dag/preamble.tex     packages, colours, TikZ styles, \dagref/\dagdef
    report/generated/dag/legend.tex       status legend + honest rigour ladder + statistics
    report/generated/dag/overview.tex     the WHOLE subgraph, layered, landscape
    report/generated/dag/phases.tex       one landscape detail page per phase
    report/generated/dag/index.tex        longtable index of every node (anchors + backlinks)
    report/generated/dag/definitions.tex  longtable index of every definition used

Stdlib only.  The single non-stdlib import is the repo's own scripts/argument.py (stdlib only
itself), imported deliberately so the shard parser and the colour classes cannot drift.
"""
import argparse
import collections
import math
import pathlib
import re
import sys

# --------------------------------------------------------------------------------------
# repo wiring
# --------------------------------------------------------------------------------------

DEFAULT_ROOT = pathlib.Path(__file__).resolve().parent.parent


def load_argument_module(repo_root):
    """Import the repo's scripts/argument.py (the canonical shard parser + colour classes)."""
    scripts = str(pathlib.Path(repo_root).resolve() / "scripts")
    if scripts not in sys.path:
        sys.path.insert(0, scripts)
    import argument  # noqa: E402  (importing does not run main())
    return argument


# --------------------------------------------------------------------------------------
# SUBGRAPH SELECTION  (edit here to re-scope the atlas)
# --------------------------------------------------------------------------------------

ROOT_ID = "op-classical"

# Route-F family prefixes: every registry id starting with one of these is a seed.
ROUTE_F_PREFIXES = (
    "lem-routef-", "lem-thmainext-", "lem-stage1-", "lem-maincb-",
    "lem-extcb", "lem-hcb", "lem-compcb-", "lem-topology-",
)
# Individually named seeds (families of one).
ROUTE_F_IDS = (
    "conj-hcb", "conj-extcb",
    "lem-kitaev-almost-idemp-audit", "lem-kitaev-diagonal-repair", "cor-kitaev-diagonal-cpization",
    "lem-prh", "lem-prh-sharpness", "prop-f2-t1-equivalence",
    "lem-classical-equiv", "ex-hume",
)

# DESIGN-PENDING ("GAP") EDGES.  These are NOT registry `deps:` edges.  They are the
# compositions the live proof strategy reserves but has not yet wired into the registry, and
# the atlas draws them in a loud, dashed, vermillion style so the reader sees exactly where the
# chain is still open.  Each row carries its provenance; keep this list MINIMAL and sourced.
# A candidate row is dropped automatically once the registry itself connects u to v (see
# live_gap_edges): a wired composition is no longer design-pending, and drawing it would be a
# false status claim.  So the list below is a set of CANDIDATES, not an assertion.
GAP_EDGE_CANDIDATES = [
    ("lem-routef-k-ledger", "op-classical",
     "phase 5 (bd aism-y81y): F0 codification + root composition; "
     "docs/plans/CURRENT.md (v33 \\S The live campaign frontier: PHASE 4 "
     "preliminaries, elevation order and phase-5 root composition)"),
    ("lem-routef-prh-finish", "lem-routef-k-ledger",
     "the registered F2/F3 rows close the stochastic-retract bridge and "
     "``compose literally with lem-routef-prh-finish''; docs/plans/CURRENT.md (v33 \\S UNCHANGED)"),
]

# PHASES.  Ordered; first matching prefix wins; unmatched ids fall through to the last phase.
# (key, title, short, prefixes)
PHASES = [
    ("comp", "Phase A --- COMP-CB / H-CB corner tower", "COMP/H-CB",
     ("lem-compcb-", "lem-hcb", "conj-hcb")),
    ("ext", "Phase B --- EXT-CB corner extension", "EXT-CB",
     ("lem-extcb", "conj-extcb")),
    ("stage1", "Phase C --- Stage-1 reset, topology leaves \\& the Kitaev repair", "Stage-1/topology",
     ("lem-stage1-", "lem-topology-", "lem-kitaev-", "cor-kitaev-", "lem-thmainext-", "lem-maincb-")),
    ("routef", "Phase D --- Route F bridges, PRH \\& the $K$-ledger", "Route F",
     ("lem-routef-", "lem-prh", "prop-f2-t1")),
    ("root", "Phase E --- root, classical reduction \\& the exposed-hull spine", "root",
     ("op-classical", "op-exposed-hull", "op-hlc", "thm-classical-factorization",
      "prop-approx-simplex", "thm-cluster", "lem-classical-equiv", "ex-hume",
      "conj-kernel", "lem-kernel-implies-hlc", "lem-hlc-implies-exposed-hull",
      "lem-min-a-implies-height")),
    ("trunk", "Phase F --- signed-geometry trunk (ancestors of the exposed-hull route)", "trunk",
     ()),   # catch-all
]
PHASE_ORDER = [p[0] for p in PHASES]
PHASE_TITLE = {p[0]: p[1] for p in PHASES}
PHASE_SHORT = {p[0]: p[2] for p in PHASES}
# A/B/C/... — the one-letter tag printed on every node so the overview page stays readable
# without a second colour channel (and matches the "Phase A ..." detail-page titles).
PHASE_LETTER = {p[0]: chr(ord("A") + i) for i, p in enumerate(PHASES)}

# --------------------------------------------------------------------------------------
# STATUS CLASSES  (keys are exactly argument.proof_class()'s outputs)
# --------------------------------------------------------------------------------------
# (key, LaTeX colour stem, fill RGB, stroke RGB, math glyph, short label, rigour rung, meaning)
# Palette: Okabe-Ito (colour-vision-deficiency safe).  Colour is NEVER the only channel: every
# node also carries a glyph and the spelled-out status, so the atlas reads correctly in
# greyscale and for every form of colour blindness.
STATUS_CLASSES = [
    ("validated", "DagVal",  (0xCC, 0xE8, 0xDE), (0x00, 0x9E, 0x73), r"\blacksquare",
     "af-validated", "RIGOROUS (L0 rung b)",
     "\\texttt{af: validated} --- root + every node validated by fresh codex verifiers, taint clean. "
     "The only rung this repo currently reaches."),
    ("cited", "DagCit",  (0xF3, 0xDD, 0xE8), (0xCC, 0x79, 0xA7), r"\blacklozenge",
     "cited", "RIGOROUS (L0 rung a)",
     "\\texttt{status: cited} --- byte-verbatim string-matched to a local published source under "
     "\\texttt{refs/}. (No result in this subgraph currently holds this rung.)"),
    ("proved", "DagPrv",  (0xD3, 0xE5, 0xF3), (0x00, 0x72, 0xB2), r"\bullet",
     "proved", "NOT rigorous",
     "\\texttt{status: proved} with \\texttt{af: none/seeded} --- a proof written in-repo that has "
     "NOT cleared an independent \\texttt{af} validation. Solid, but not L0."),
    ("seeded", "DagSee",  (0xFD, 0xF6, 0xCE), (0xB8, 0xA8, 0x00), r"\lozenge",
     "seeded", "NOT rigorous",
     "\\texttt{af: seeded} --- an \\texttt{af} workspace exists and the contract is pinned, but no "
     "validated tree yet."),
    ("nonrigorous", "DagNon", (0xFA, 0xEA, 0xCF), (0xE6, 0x9F, 0x00), r"\blacktriangle",
     "mod-audit / conj.", "NOT rigorous (flagged)",
     "\\texttt{proved-mod-audit} $\\cdot$ \\texttt{conjecture} $\\cdot$ \\texttt{heuristic} $\\cdot$ "
     "\\texttt{numerical} --- the workhorse rungs of the inherited campaign. Content, no independent check."),
    ("stated", "DagSta",  (0xE9, 0xE9, 0xE9), (0x7F, 0x7F, 0x7F), r"\circ",
     "stated", "NOT rigorous",
     "\\texttt{status: stated} --- transcribed from an upstream artifact, unchecked here."),
    ("open", "DagOpn",  (0xF8, 0xDC, 0xCB), (0xD5, 0x5E, 0x00), r"\bigstar",
     "OPEN", "OPEN",
     "\\texttt{status: open} or \\texttt{kind: open-problem} --- a live open question. "
     "(Whether the north star \\texttt{op-classical} is still one of these is stated, from the "
     "registry, in the honest-reading paragraph above.)"),
]
STATUS_INDEX = {c[0]: i for i, c in enumerate(STATUS_CLASSES)}
STATUS_STEM = {c[0]: c[1] for c in STATUS_CLASSES}
STATUS_GLYPH = {c[0]: c[4] for c in STATUS_CLASSES}
STATUS_SHORT = {c[0]: c[5] for c in STATUS_CLASSES}

# --------------------------------------------------------------------------------------
# LAYOUT PARAMETERS (cm).  Tuned so a band is at most ~1.05x the landscape text width, i.e.
# every atlas page renders at ~95-100% scale: node text stays legible.
# --------------------------------------------------------------------------------------
NODE_W = 2.62          # node text width
NODE_H = 0.98          # node minimum height
COL_PITCH = 3.32       # x distance between consecutive columns
ROW_PITCH = 1.46       # y distance between consecutive rows
# Boundary chips are SINGLE-LINE 5pt monospace (no wrapping, so they can never collide
# vertically); their id is abbreviated to the shortest COLLISION-FREE prefix length in
# [CHIP_MIN_CHARS, CHIP_MAX_CHARS] (see configure_chips), which keeps the chip column narrow
# without ever making two chips ambiguous.  Chips are hyperlinks: the full id is one click away.
GHOST_H = 0.38
GHOST_PITCH = 0.46     # y distance between chips
GHOST_ROWS = 12        # chips per boundary column (12 x 0.46 = 5.5cm ~ one band's height)
GHOST_RESERVE = 2      # boundary columns held back from a band's width budget
CHIP_MIN_CHARS = 28
CHIP_MAX_CHARS = 44
CHIP_CHAR_W = 0.101    # measured advance width of one 5pt monospace character, in cm
CHIP_PAD = 0.30        # chip border + inner separation
BAND_W = 23.8          # max natural band width before wrapping to the next band
BAND_GAP = 0.95        # vertical gap between stacked bands
PAGE_H = 13.6          # max natural page height before starting a new page
MAX_ROWS = 4           # max nodes stacked in one column before splitting into sub-columns
                       #   (kept small on purpose: short bands stack two-to-a-page, which
                       #    matches the landscape aspect ratio instead of wasting half a page)
BARY_PASSES = 6
RANK_PASSES = 24

GEN_HEADER = ("%% GENERATED by scripts/gen-report-dag.py --- do not hand-edit.\n"
              "%% Source of truth: argument/lemmas/*.md (parsed by scripts/argument.py).\n"
              "%% Regenerate: python3 scripts/gen-report-dag.py   |   Gate: --check (scripts/check-all.sh)\n")


# --------------------------------------------------------------------------------------
# small helpers
# --------------------------------------------------------------------------------------

def tex_escape(s):
    """Escape a plain string for LaTeX text mode."""
    out = []
    for ch in s:
        if ch in "\\":
            out.append(r"\textbackslash{}")
        elif ch in "&%$#_{}":
            out.append("\\" + ch)
        elif ch == "~":
            out.append(r"\textasciitilde{}")
        elif ch == "^":
            out.append(r"\textasciicircum{}")
        else:
            out.append(ch)
    return "".join(out)


def tt_id(rid):
    r"""A registry id typeset as breakable \texttt: hyphens become discretionary break points."""
    return r"\texttt{" + rid.replace("-", r"-\hspace{0pt}") + "}"


def fnum(x):
    return f"{x:.3f}".rstrip("0").rstrip(".") or "0"


# Chip abbreviation state, computed ONCE per run by configure_chips() (deterministic: it is a
# pure function of the sorted node set).  Kept module-level so both the layout geometry and the
# TikZ emitter see the same widths.
CHIP = {}
CHIP_COL_PITCH = [COL_PITCH]
CHIP_W = [2.9]


def configure_chips(nodes):
    """Pick the shortest collision-free abbreviation length for the boundary chips, and size the
    chip column from it.  Falls back to full ids (wider column) if no prefix length separates
    them — correctness before compactness."""
    nodes = sorted(nodes)
    chosen, labels = None, None
    for k in range(CHIP_MIN_CHARS, CHIP_MAX_CHARS + 1):
        cand = {n: (n if len(n) <= k else n[:k - 3] + "...") for n in nodes}
        if len(set(cand.values())) == len(nodes):
            chosen, labels = k, cand
            break
    if labels is None:
        chosen, labels = max((len(n) for n in nodes), default=CHIP_MAX_CHARS), {n: n for n in nodes}
    CHIP.clear()
    CHIP.update(labels)
    CHIP_W[0] = round(CHIP_CHAR_W * chosen + CHIP_PAD, 3)
    CHIP_COL_PITCH[0] = round(max(COL_PITCH, CHIP_W[0] + 0.16), 3)
    return chosen


# --------------------------------------------------------------------------------------
# registry model
# --------------------------------------------------------------------------------------

REPORT_TOK = re.compile(r"report\s+([a-z]+:[A-Za-z0-9-]+)")


class Registry:
    def __init__(self, repo_root):
        self.root = pathlib.Path(repo_root).resolve()
        self.A = load_argument_module(self.root)
        lemmas, errors = self.A.parse_registry(self.root / "argument")
        self.errors = errors
        self.lemmas = sorted(lemmas, key=lambda d: d.get("id", ""))
        self.by = {l["id"]: l for l in self.lemmas}
        self.def_ids = sorted(self.A.load_def_ids())
        self.defs = self._load_defs()
        self.tex_labels = self._load_tex_labels()

    def _load_defs(self):
        out = {}
        ddir = self.root / "definitions"
        for p in sorted(ddir.glob("*.md")) if ddir.exists() else []:
            if p.name in ("README.md", "INDEX.md"):
                continue
            fm = self.A._parse_frontmatter(p)
            if fm and fm.get("id"):
                out[fm["id"]] = fm
        return out

    def _load_tex_labels(self):
        r"""\label{}s already defined in report/sections/, EXCLUDING this generator's own shard
        (so the back-link set is a fixpoint, not a self-reference)."""
        labels = set()
        sec = self.root / "report" / "sections"
        for p in sorted(sec.glob("*.tex")) if sec.exists() else []:
            if p.name == SHARD_NAME:
                continue
            for line in p.read_text(encoding="utf-8").splitlines():
                line = line.split("%")[0] if not line.lstrip().startswith("%") else ""
                labels |= set(re.findall(r"\\label\{([a-z]+:[A-Za-z0-9-]+)\}", line))
        return labels

    def report_label(self, rid):
        """The report \\label a result maps to (argument.py/check-provenance.py join rule), or None."""
        l = self.by.get(rid, {})
        for lab in REPORT_TOK.findall(l.get("provenance", "") or ""):
            if lab in self.tex_labels:
                return lab
        cand = rid.replace("-", ":", 1)
        return cand if cand in self.tex_labels else None

    def dep_edges(self, l):
        """[(dep_id, kind)] for one shard: unconditional deps, then OR-route members."""
        out = [(d, "dep") for d in l.get("deps", [])]
        for i, r in enumerate(l.get("routes", []), 1):
            out += [(m, f"route{i}") for m in sorted(r)]
        return out


def live_gap_edges(reg, nodes, edges):
    """The GAP candidates that are STILL design-pending, derived from the registry.

    A candidate (u -> v) survives only if both endpoints are drawn AND the registry does not
    already carry u to v along `deps:`/`routes:` edges.  Once the composition is wired, the
    candidate is dropped: keeping it would assert "not yet wired" about an edge the registry
    has since closed."""
    succ = collections.defaultdict(set)
    for u, v, _k in edges:
        succ[u].add(v)

    def reaches(src, dst):
        seen, stack = {src}, [src]
        while stack:
            n = stack.pop()
            if n == dst:
                return True
            for m in sorted(succ[n]):
                if m not in seen:
                    seen.add(m)
                    stack.append(m)
        return False

    live = []
    for u, v, note in GAP_EDGE_CANDIDATES:
        if u in nodes and v in nodes and not reaches(u, v):
            live.append((u, v, note))
    return live


def select_subgraph(reg):
    """The Route-F landing sub-DAG: closure of {op-classical} U ROUTE_F_SEEDS over deps+routes.

    Returns (nodes, edges, gaps): `edges` carries the registry edges plus the still-live GAP
    links; `gaps` is the derived list of (u, v, note) rows the legend documents."""
    seeds = {i for i in reg.by if i.startswith(ROUTE_F_PREFIXES)}
    seeds |= {i for i in ROUTE_F_IDS if i in reg.by}
    if ROOT_ID in reg.by:
        seeds.add(ROOT_ID)
    seen, stack = set(seeds), sorted(seeds)
    while stack:
        n = stack.pop()
        for d, _k in reg.dep_edges(reg.by[n]):
            if d in reg.by and d not in seen:
                seen.add(d)
                stack.append(d)
    nodes = sorted(seen)
    edges = []
    for i in nodes:
        for d, kind in reg.dep_edges(reg.by[i]):
            if d in seen:
                edges.append((d, i, kind))
    edges = sorted(set(edges))
    gaps = live_gap_edges(reg, seen, edges)
    edges = sorted(set(edges) | {(u, v, "gap") for u, v, _n in gaps})
    return nodes, edges, gaps


def phase_of(rid):
    for key, _t, _s, prefixes in PHASES:
        if prefixes and rid.startswith(prefixes):
            return key
    return PHASES[-1][0]


# --------------------------------------------------------------------------------------
# LAYOUT ENGINE — deterministic Sugiyama (rank / dummy chains / barycentre / serpentine bands)
# --------------------------------------------------------------------------------------

class Layout:
    """Layered layout of a DAG, packed into bands and pages that fit a landscape text block.

    Produces `self.pages`: a list of pages; each page is a dict with
        "bands":  [ {"nodes": [(name, kind, x, y, payload)], "y0": float} ]
        "edges":  [ (from_name, to_name, kind) ]      -- all endpoints live on this page
        "w", "h": natural size in cm
    `kind` is one of "node" (a real result), "dummy" (an edge waypoint), "ghost" (a repeated
    boundary copy of a node that really lives in the previous band/page).
    """

    def __init__(self, nodes, edges, sort_key=None, max_rows=MAX_ROWS, band_w=BAND_W,
                 page_h=PAGE_H):
        self.nodes = list(nodes)
        self.edges = [e for e in edges if e[0] in set(nodes) and e[1] in set(nodes)]
        self.sort_key = sort_key or (lambda n: (n,))
        self.max_rows = max_rows
        self.band_w = band_w
        self.page_h = page_h
        self._rank()
        self._expand()
        self._order()
        self._pack()

    # ---- 1. layer assignment ----
    def _rank(self):
        r"""Longest-path (ASAP) ranking, then a deterministic median relaxation.

        Plain ASAP pins every source at layer 0, which makes a leaf feeding a depth-12 result
        span twelve layers; every such span costs a chain of dummy waypoints and the drawing
        drowns in them (here: 448 dummies for 110 nodes).  The relaxation slides each node
        inside its feasible window [max(pred)+1, min(succ)-1] towards the median of its
        neighbours, which is the cheap, deterministic stand-in for GraphViz's network-simplex
        ranking.  It typically removes ~80% of the waypoints and shortens every edge."""
        preds = collections.defaultdict(list)
        succs = collections.defaultdict(list)
        for u, v, _k in self.edges:
            preds[v].append(u)
            succs[u].append(v)
        rank, state = {}, {}

        def r(n):
            if n in rank:
                return rank[n]
            if state.get(n):          # defensive: a cycle would be a linker error upstream
                return 0
            state[n] = 1
            val = 0
            for p in sorted(preds[n]):
                val = max(val, r(p) + 1)
            state[n] = 0
            rank[n] = val
            return val

        for n in sorted(self.nodes):
            r(n)
        hi_cap = max(rank.values()) if rank else 0
        for _ in range(RANK_PASSES):
            moved = False
            for n in sorted(self.nodes):
                lo = max([rank[u] + 1 for u in preds[n]], default=0)
                hi = min([rank[w] - 1 for w in succs[n]], default=(lo if preds[n] or not succs[n]
                                                                   else hi_cap))
                if hi < lo:
                    hi = lo
                nbr = sorted([rank[u] for u in preds[n]] + [rank[w] for w in succs[n]])
                target = nbr[len(nbr) // 2] if nbr else lo
                new = min(max(target, lo), hi)
                if new != rank[n]:
                    rank[n] = new
                    moved = True
            if not moved:
                break
        base = min(rank.values()) if rank else 0
        self.rank = {n: rank[n] - base for n in rank}
        self.maxrank = max(self.rank.values()) if self.rank else 0

    # ---- 2. layer buckets ----
    def _expand(self):
        r"""No dummy waypoints.  A proper (dummy-chain) layering of this graph costs ~320
        waypoints for 110 results — five times as many boxes as content — and blows every band
        up to five sub-columns.  Instead, long edges are drawn directly as flat Bezier curves
        (they leave and enter horizontally, so they read as flow lines rather than as chords),
        and an edge whose source sits on an earlier band is reconnected through a dashed
        BOUNDARY CHIP repeated at the left of the band that owns its target.  Every page is
        therefore self-contained without a single fake node."""
        self.layers = collections.defaultdict(list)
        for n in sorted(self.nodes):
            self.layers[self.rank[n]].append(n)
        self.kind_of = {n: "node" for n in self.nodes}
        self.seg = sorted(self.edges)

    # ---- 3. ordering inside layers (barycentre, deterministic tie-break) ----
    def _order(self):
        succ, pred = collections.defaultdict(list), collections.defaultdict(list)
        for u, v, _k in self.seg:
            succ[u].append(v)
            pred[v].append(u)
        order = {}
        for lay in sorted(self.layers):
            order[lay] = sorted(self.layers[lay], key=lambda n: self._init_key(n))
        pos = {n: i for lay in order for i, n in enumerate(order[lay])}

        def sweep(layers_seq, nbr):
            for lay in layers_seq:
                bary = {}
                for n in order[lay]:
                    ns = [pos[m] for m in nbr[n] if m in pos]
                    bary[n] = (sum(ns) / len(ns)) if ns else pos[n]
                order[lay] = sorted(order[lay], key=lambda n: (round(bary[n], 6),
                                                              self._init_key(n)))
                for i, n in enumerate(order[lay]):
                    pos[n] = i

        keys = sorted(self.layers)
        for _ in range(BARY_PASSES):
            sweep(keys[1:], pred)
            sweep(list(reversed(keys[:-1])), succ)
        self.order = order

    def _init_key(self, n):
        if self.kind_of.get(n) == "dummy":
            # a dummy inherits the sort key of the edge target, then of the source, so a long
            # edge's waypoints stay next to the nodes they serve instead of wandering
            parts = n.split("__")            # ['', 'd', src, dst, layer]
            src, dst = parts[2], parts[3]
            return self.sort_key(dst) + self.sort_key(src) + ("~dummy",)
        return self.sort_key(n) + ("",)

    # ---- 4. columns -> bands -> pages, then coordinates ----
    def _pack(self):
        # 4a. split every layer into sub-columns of at most max_rows entries
        columns = []                 # [(layer, [names])]
        for lay in sorted(self.order):
            members = self.order[lay]
            if not members:
                continue
            nsub = max(1, math.ceil(len(members) / self.max_rows))
            per = math.ceil(len(members) / nsub)
            for s in range(nsub):
                chunk = members[s * per:(s + 1) * per]
                if chunk:
                    columns.append((lay, chunk))
        # 4b. group columns by layer, then greedily fill bands (never split a layer)
        by_layer = collections.OrderedDict()
        for lay, chunk in columns:
            by_layer.setdefault(lay, []).append(chunk)
        # Every band except the first also carries boundary chips, so its content budget is
        # shrunk by GHOST_RESERVE columns — otherwise the bands come out at different widths and
        # the whole page has to be scaled down to the widest one.
        bands, cur, cur_w = [], [], 0.0
        for lay, chunks in by_layer.items():
            w = len(chunks) * COL_PITCH
            budget = self.band_w - (0 if not bands else GHOST_RESERVE * CHIP_COL_PITCH[0])
            if cur and cur_w + w > budget:
                bands.append(cur)
                cur, cur_w = [], 0.0
            cur.append((lay, chunks))
            cur_w += w
        if cur:
            bands.append(cur)
        # 4c. lay bands out, repeating the previous band's last layer as ghosts
        self.pages = []
        page = {"bands": [], "edges": [], "w": 0.0, "h": 0.0}
        y_cursor = 0.0
        instance = {}                # (page_idx, band_idx, name) -> tikz name
        placed = []                  # per band: dict name -> tikz name
        for bi, band in enumerate(bands):
            own = {n for _l, chs in band for ch in chs for n in ch}
            cols = []
            if bi > 0:
                gh = sorted({u for u, v, _k in self.seg if v in own and u not in own},
                            key=self._init_key)
                if gh:
                    nsub = max(1, math.ceil(len(gh) / GHOST_ROWS))
                    per = math.ceil(len(gh) / nsub)
                    for s in range(nsub):
                        chunk = gh[s * per:(s + 1) * per]
                        if chunk:
                            cols.append(("ghost", chunk))
            for lay, chunks in band:
                for ch in chunks:
                    cols.append(("real", ch))
            band_h = max((len(ch) * (GHOST_PITCH if t == "ghost" else ROW_PITCH))
                         for t, ch in cols)
            if page["bands"] and y_cursor + band_h > self.page_h:
                self.pages.append(page)
                page = {"bands": [], "edges": [], "w": 0.0, "h": 0.0}
                y_cursor = 0.0
                # a fresh page repeats nothing extra: the ghost column above already did it
            names = {}
            realnames = {}
            entries = []
            x = 0.0
            for ctype, chunk in cols:
                pitch = GHOST_PITCH if ctype == "ghost" else ROW_PITCH
                y_top = -y_cursor - (band_h - len(chunk) * pitch) / 2.0
                for j, n in enumerate(chunk):
                    kind = "ghost" if ctype == "ghost" else self.kind_of.get(n, "node")
                    tname = "N%d_%d_%d" % (len(self.pages), len(page["bands"]), len(entries))
                    entries.append((tname, kind, round(x, 3),
                                    round(y_top - j * pitch, 3), n))
                    names.setdefault(n, tname)
                    if kind != "ghost":
                        realnames.setdefault(n, tname)
                x += CHIP_COL_PITCH[0] if ctype == "ghost" else COL_PITCH
            page["bands"].append({"nodes": entries, "y0": -y_cursor})
            page["w"] = max(page["w"], x)
            y_cursor += band_h + BAND_GAP
            page["h"] = max(page["h"], y_cursor)
            placed.append((names, realnames))
            instance[bi] = len(self.pages)
        if page["bands"]:
            self.pages.append(page)
        # 4d. every edge is drawn EXACTLY once, on the band that really owns its target; its
        #     source is the real node when that band has it, else the band's boundary chip.
        for u, v, kind in sorted(self.seg):
            for bi, (names, realnames) in enumerate(placed):
                if v in realnames and u in names:
                    self.pages[instance[bi]]["edges"].append((names[u], realnames[v], kind))
                    break
        for p in self.pages:
            p["edges"] = sorted(set(p["edges"]))


# --------------------------------------------------------------------------------------
# TikZ emission
# --------------------------------------------------------------------------------------

# Shard number: the atlas sits immediately BEFORE the status/outlook shard, which stays last
# (report/README.md house convention). 39 today; bump both this and SHARD_ID together if the
# shard order changes, and update report/README.md + report/SHARD_CATALOG.md in the same commit.
SHARD_NAME = "39_argument_dag.tex"
GEN_SUBDIR = pathlib.Path("report") / "generated" / "dag"


def node_body(reg, rid, cls, backlink):
    glyph = STATUS_GLYPH[cls]
    short = STATUS_SHORT[cls]
    tail = ""
    if backlink:
        tail = r"\,\hyperref[" + backlink + r"]{$\S$}"
    return (r"\hypertarget{dag:" + rid + "}{}" + tt_id(rid) + r"\\[-0.15em]"
            + r"{\dagstatus{$" + glyph + r"$\," + short
            + r"\,\dagphasetag{" + PHASE_LETTER[phase_of(rid)] + "}" + tail + "}}")


def emit_picture(reg, lay, page, cls_of, backlink_of):
    """One TikZ picture per Layout page.  Edges go on the BACKGROUND layer so a long
    dependency passes cleanly *behind* an intervening box instead of striking through its
    text — the single biggest legibility win in a dense layered drawing."""
    out = [r"\begin{tikzpicture}[dagpic]"]
    for band in page["bands"]:
        for tname, kind, x, y, n in band["nodes"]:
            if kind == "ghost":
                out.append(f"  \\node[dagghost] ({tname}) at ({fnum(x)},{fnum(y)}) "
                           f"{{\\hyperlink{{dag:{n}}}{{{tex_escape(CHIP.get(n, n))}}}}};")
            else:
                cls = cls_of[n]
                out.append(f"  \\node[dagnode,dag{STATUS_STEM[cls]}] ({tname}) "
                           f"at ({fnum(x)},{fnum(y)}) "
                           f"{{{node_body(reg, n, cls, backlink_of.get(n))}}};")
    if page["edges"]:
        out.append(r"  \begin{scope}[on background layer]")
        for a, b, kind in page["edges"]:
            style = {"dep": "dagedge", "gap": "daggap"}.get(kind, "dagroute")
            out.append(f"    \\draw[{style}] ({a}) to[out=0,in=180] ({b});")
        out.append(r"  \end{scope}")
    out.append(r"\end{tikzpicture}")
    return "\n".join(out)


def emit_figure_pages(reg, nodes, edges, cls_of, backlink_of, key, title, note):
    """A phase/overview figure: one landscape page per Layout page."""
    order_index = {p: i for i, p in enumerate(PHASE_ORDER)}

    def skey(n):
        return (f"{order_index[phase_of(n)]:02d}", f"{STATUS_INDEX[cls_of[n]]:02d}", n)

    lay = Layout(nodes, edges, sort_key=skey)
    out = []
    for pi, page in enumerate(lay.pages):
        out.append("")
        if pi == 0:
            out.append(r"\phantomsection\label{fig:dag-" + key + "}")
            out.append(r"\hypertarget{dag:phase:" + key + "}{}")
        head = title if pi == 0 else title + r" \textit{(cont.)}"
        out.append(r"\begin{center}\dagpagetitle{" + head + r"}\end{center}")
        if pi == 0 and note:
            out.append(r"{\dagnote " + note + r"\par}\vspace{0.35em}")
        out.append(r"\noindent\begin{adjustbox}{max width=\linewidth,"
                   r"max totalheight=0.90\textheight,center}")
        out.append(emit_picture(reg, lay, page, cls_of, backlink_of))
        out.append(r"\end{adjustbox}")
        out.append(r"\par\vfill\clearpage")
    return "\n".join(out), lay


# --------------------------------------------------------------------------------------
# generated files
# --------------------------------------------------------------------------------------

def file_preamble():
    lines = [GEN_HEADER,
             r"% Packages, colours, TikZ styles and crosslink macros for the argument-DAG atlas.",
             r"% \input from the PREAMBLE of report/main.tex (before \begin{document}).",
             r"\usepackage{pdflscape}",
             r"\usepackage{adjustbox}",
             r"\usepackage{xcolor}",
             r"\usepackage{tikz}",
             r"\usetikzlibrary{arrows.meta,shapes.geometric,backgrounds,fit}",
             "",
             r"% --- status palette (Okabe-Ito, colour-vision-deficiency safe) ------------------"]
    for key, stem, fill, stroke, _g, _s, _r, _m in STATUS_CLASSES:
        lines.append(r"\definecolor{%sFill}{RGB}{%d,%d,%d}" % (stem, *fill))
        lines.append(r"\definecolor{%sLine}{RGB}{%d,%d,%d}" % (stem, *stroke))
    lines += [
        r"\definecolor{DagEdge}{RGB}{130,138,148}",
        r"\definecolor{DagGap}{RGB}{213,94,0}",
        r"\definecolor{DagRoute}{RGB}{204,121,167}",
        "",
        r"% --- TikZ styles ---------------------------------------------------------------",
        r"\tikzset{",
        r"  dagpic/.style={>={Stealth[length=1.6mm,width=1.1mm]}, line cap=round,",
        r"                 every node/.append style={inner sep=0pt,outer sep=0pt}},",
        r"  dagnode/.style={rounded corners=1.6pt, draw, line width=0.55pt, inner sep=2.2pt,",
        r"                  text width=" + fnum(NODE_W) + r"cm, align=center, minimum height="
        + fnum(NODE_H) + r"cm,",
        r"                  font=\tiny, anchor=west},",
        r"  dagghost/.style={rounded corners=1.2pt, draw=black!32, dash pattern=on 1pt off 1pt,",
        r"                   line width=0.35pt, fill=black!3, text=black!58, inner xsep=2pt,",
        r"                   inner ysep=1pt, minimum width=" + fnum(CHIP_W[0]) + r"cm,",
        r"                   minimum height=" + fnum(GHOST_H) + r"cm, align=left,",
        r"                   font=\fontsize{5}{5.4}\selectfont\ttfamily, anchor=west},",
        r"  dagedge/.style={->, draw=DagEdge, line width=0.4pt, opacity=0.85,",
        r"                  shorten >=0.6pt, shorten <=0.6pt},",
        r"  dagroute/.style={->, draw=DagRoute, line width=0.5pt, dash pattern=on 2pt off 1.4pt,",
        r"                   shorten >=0.6pt, shorten <=0.6pt},",
        r"  daggap/.style={->, draw=DagGap, line width=0.8pt, dash pattern=on 3pt off 1.8pt,",
        r"                 shorten >=0.6pt, shorten <=0.6pt},",
        r"}",
    ]
    for key, stem, _f, _s, _g, _sh, _r, _m in STATUS_CLASSES:
        lines.append(r"\tikzset{dag%s/.style={fill=%sFill, draw=%sLine}}" % (stem, stem, stem))
    lines += [
        "",
        r"% --- text bits used inside the atlas -------------------------------------------",
        r"\newcommand{\dagstatus}[1]{{\fontsize{4.4}{5}\selectfont\color{black!72}#1}}",
        r"\newcommand{\dagphasetag}[1]{{\fontsize{4}{4.6}\selectfont\bfseries\color{black!45}[#1]}}",
        r"\newcommand{\dagpagetitle}[1]{{\normalsize\bfseries #1}}",
        r"\newcommand{\dagnote}{\footnotesize\color{black!70}}",
        r"\newcommand{\dagswatch}[1]{\tikz[baseline=-0.55ex]{\node[rounded corners=1.2pt,"
        r"draw,line width=0.5pt,minimum width=7mm,minimum height=3.1mm,#1]{};}}",
        "",
        r"% --- CROSSLINK API (use these anywhere in the report) --------------------------",
        r"%   \dagref{lem-prh}      -> jumps to the atlas node for a registry result",
        r"%   \dagdef{def-height}   -> jumps to the atlas row for a definition",
        r"%   \dagphase{comp}       -> jumps to a phase page",
        r"% Anchors are \hypertarget{dag:<id>}; the scheme is documented in the atlas section.",
        r"\newcommand{\dagref}[1]{\hyperlink{dag:#1}{\texttt{#1}}}",
        r"\newcommand{\dagdef}[1]{\hyperlink{dag:#1}{\texttt{#1}}}",
        r"\newcommand{\dagphase}[2]{\hyperlink{dag:phase:#1}{#2}}",
    ]
    return "\n".join(lines) + "\n"


def file_legend(reg, nodes, edges, cls_of, gaps):
    n = len(nodes)
    by_cls = collections.Counter(cls_of[i] for i in nodes)
    by_kind = collections.Counter(reg.by[i].get("kind", "?") for i in nodes)
    by_phase = collections.Counter(phase_of(i) for i in nodes)
    ekind = collections.Counter(k for _u, _v, k in edges)
    rigorous = by_cls.get("validated", 0) + by_cls.get("cited", 0)
    L = [GEN_HEADER,
         r"\subsection*{How to read the atlas}",
         r"\phantomsection\label{tab:dag-legend}",
         r"\noindent The colour of a node is its \emph{rigour rung} (\texttt{CLAUDE.md} L0), computed by "
         r"\texttt{scripts/argument.py}'s \texttt{proof\_class()} --- the same function that colours the "
         r"browsable Mermaid twin \texttt{argument/DAG.md}. Colour is never the only channel: each node "
         r"also carries a glyph and the spelled-out status, so the atlas survives greyscale printing and "
         r"every form of colour-vision deficiency.",
         "",
         r"\begingroup\small",
         r"\begin{longtable}{@{}c l l p{0.50\linewidth}@{}}",
         r"\toprule",
         r"& \textbf{class} & \textbf{rung} & \textbf{what it means} \\",
         r"\midrule",
         r"\endfirsthead",
         r"\toprule & \textbf{class} & \textbf{rung} & \textbf{what it means} \\ \midrule \endhead",
         r"\bottomrule",
         r"\endfoot"]
    for key, stem, _f, _s, glyph, short, rung, meaning in STATUS_CLASSES:
        cnt = by_cls.get(key, 0)
        L.append(r"\dagswatch{dag%s} & $%s$~%s\ (%d) & %s & %s \\[0.25em]"
                 % (stem, glyph, tex_escape(short), cnt, rung, meaning))
    L += [r"\end{longtable}", r"\endgroup", ""]
    L += [r"\noindent\textbf{Edges.}\quad",
          r"\tikz[baseline=-0.6ex]{\draw[dagedge](0,0)--(0.8,0);}~a registry \texttt{deps:} edge "
          r"(the dependency \emph{points at} the result that uses it);\quad",
          r"\tikz[baseline=-0.6ex]{\draw[dagroute](0,0)--(0.8,0);}~a member of an \texttt{routes:} "
          r"OR-route (\emph{any one} route discharges the shard --- here \texttt{op-hlc});\quad"]
    if gaps:
        L.append(r"\tikz[baseline=-0.6ex]{\draw[daggap](0,0)--(0.8,0);}~a \textbf{design-pending (GAP) "
                 r"composition}: \emph{not} a registry edge, reserved by the live strategy "
                 r"(\texttt{docs/plans/CURRENT.md}) and not yet wired.\quad")
    L += [r"Small dashed grey chips are "
          r"\emph{boundary copies} of a node that really lives on an earlier band or in another "
          r"phase; their id is abbreviated to the shortest unambiguous prefix and each is a "
          r"hyperlink to the real node.",
          "",
          r"\subsection*{The design-pending (GAP) links}", ""]
    if gaps:
        L += [r"\noindent The atlas exists to show \emph{where the chain is still open}. These links are "
              r"drawn but are \textbf{not} registry \texttt{deps:} edges --- nothing below may be read as "
              r"an established implication:", r"\begingroup\small",
              r"\begin{itemize}\setlength\itemsep{0pt}"]
        for u, v, note in gaps:
            L.append(r"\item \dagref{%s} $\dashrightarrow$ \dagref{%s} --- %s" % (u, v, note))
        L += [r"\end{itemize}\endgroup", ""]
    else:
        L += [r"\noindent \textbf{None.} Every composition the live strategy reserved is now carried "
              r"by registry \texttt{deps:}/\texttt{routes:} edges, so no design-pending link is drawn. "
              r"(The candidate list lives in \texttt{scripts/gen-report-dag.py}; a row is dropped "
              r"automatically once the registry connects its endpoints, and would reappear here if a "
              r"future rewire re-opened one.)", ""]
    L += [r"\subsection*{Statistics of the drawn subgraph}", r"\begingroup\small",
          r"\begin{longtable}{@{}l r l@{}}", r"\toprule",
          r"\textbf{quantity} & \textbf{value} & \textbf{note} \\ \midrule \endhead",
          r"\bottomrule \endfoot",
          r"results drawn & %d & of %d in the registry \\" % (n, len(reg.lemmas)),
          r"registry edges drawn & %d & \texttt{deps:} %d, OR-route members %d \\"
          % (sum(v for k, v in ekind.items() if k != "gap"), ekind.get("dep", 0),
             sum(v for k, v in ekind.items() if k.startswith("route"))),
          r"design-pending (GAP) links & %d & %s \\"
          % (ekind.get("gap", 0),
             r"drawn dashed; \emph{not} registry edges" if ekind.get("gap", 0)
             else r"none remain: every reserved composition is now a registry edge"),
          r"\textbf{rigorous (L0)} & \textbf{%d} & \texttt{af: validated} or \texttt{status: cited} "
          r"--- %s\%% of the chain \\" % (rigorous, fnum(round(100.0 * rigorous / max(1, n), 1))),
          r"non-rigorous & %d & everything else, flagged loudly by colour and glyph \\" % (n - rigorous),
          r"\midrule"]
    for key, _t, _s, _p in PHASES:
        L.append(r"phase \dagphase{%s}{%s} & %d & %s \\"
                 % (key, tex_escape(PHASE_SHORT[key]), by_phase.get(key, 0),
                    PHASE_TITLE[key].split("---")[-1].strip()))
    L.append(r"\midrule")
    for k in sorted(by_kind):
        L.append(r"\texttt{kind: %s} & %d & \\" % (tex_escape(k), by_kind[k]))
    L += [r"\end{longtable}", r"\endgroup", ""]
    return "\n".join(L) + "\n"


def file_overview(reg, nodes, edges, cls_of, backlink_of):
    note = (r"The complete Route-F landing chain: every registry result in the transitive "
            r"\texttt{deps:}/\texttt{routes:} closure of \texttt{op-classical} together with the "
            r"Route-F families. Dependencies flow \textbf{left to right}: a node sits one layer to the "
            r"right of its deepest prerequisite, so the north star \dagref{op-classical} is on the "
            r"far right of the last band. Bands read like text --- finish a band, drop to the next.")
    body, lay = emit_figure_pages(reg, nodes, edges, cls_of, backlink_of, "overview",
                                  r"The Route-F proof chain for \texttt{op-classical} "
                                  r"--- complete sub-DAG", note)
    return GEN_HEADER + r"\begin{landscape}" + "\n" + body + "\n" + r"\end{landscape}" + "\n", lay


def file_phases(reg, nodes, edges, cls_of, backlink_of):
    nodeset = set(nodes)
    out = [GEN_HEADER, r"\begin{landscape}"]
    for key, title, _short, _pre in PHASES:
        ms = sorted(i for i in nodes if phase_of(i) == key)
        if not ms:
            continue
        msset = set(ms)
        inner = [(u, v, k) for u, v, k in edges if u in msset and v in msset]
        ghosts_in = sorted({u for u, v, _k in edges if v in msset and u not in msset})
        ghosts_out = sorted({v for u, v, _k in edges if u in msset and v not in msset})
        sub_nodes = ms + ghosts_in + ghosts_out
        sub_edges = [(u, v, k) for u, v, k in edges
                     if (u in msset or v in msset) and u in set(sub_nodes) and v in set(sub_nodes)]
        cnt = collections.Counter(cls_of[i] for i in ms)
        bits = ", ".join(f"{cnt[c]} {STATUS_SHORT[c]}" for c, *_ in STATUS_CLASSES if cnt.get(c))
        note = (r"%d results (%s). Boundary nodes of neighbouring phases are drawn as small dashed "
                r"chips; click one to jump to its own page." % (len(ms), tex_escape(bits)))
        body, _lay = emit_figure_pages(reg, sub_nodes, sub_edges, cls_of, backlink_of,
                                       key, title, note)
        out.append(body)
    out.append(r"\end{landscape}")
    return "\n".join(out) + "\n"


def file_index(reg, nodes, edges, cls_of, backlink_of):
    indeg = collections.Counter(v for _u, v, _k in edges)
    outdeg = collections.Counter(u for u, _v, _k in edges)
    L = [GEN_HEADER, r"\begin{landscape}",
         r"\subsection*{Node index --- every result in the chain}",
         r"\phantomsection\label{tab:dag-index}",
         r"\noindent Anchors are \texttt{dag:\textless id\textgreater}. The \textbf{id} column links to "
         r"the node in the atlas; \textbf{report} links to the typeset statement in this lab-book when "
         r"one exists. Sorted by id (stable).",
         r"\begingroup\scriptsize",
         r"\begin{longtable}{@{}l l l l l r r l@{}}",
         r"\toprule",
         r"\textbf{id} & \textbf{phase} & \textbf{kind} & \textbf{status} & \textbf{af} & "
         r"\textbf{in} & \textbf{out} & \textbf{report} \\",
         r"\midrule\endfirsthead",
         r"\toprule \textbf{id} & \textbf{phase} & \textbf{kind} & \textbf{status} & \textbf{af} & "
         r"\textbf{in} & \textbf{out} & \textbf{report} \\ \midrule\endhead",
         r"\bottomrule\endfoot"]
    for rid in nodes:
        l = reg.by[rid]
        cls = cls_of[rid]
        lab = backlink_of.get(rid)
        rep = (r"\hyperref[" + lab + r"]{\S~" + tex_escape(lab) + "}") if lab else r"{\color{black!35}---}"
        L.append(r"\dagswatch{dag%s}~\hyperlink{dag:%s}{\texttt{%s}} & %s & %s & %s & %s & %d & %d & %s \\"
                 % (STATUS_STEM[cls], rid, tex_escape(rid),
                    tex_escape(PHASE_SHORT[phase_of(rid)]),
                    tex_escape(l.get("kind", "?")), tex_escape(l.get("status", "?")),
                    tex_escape(l.get("af", "none")),
                    indeg.get(rid, 0), outdeg.get(rid, 0), rep))
    L += [r"\end{longtable}", r"\endgroup", r"\end{landscape}", ""]
    return "\n".join(L) + "\n"


def file_definitions(reg, nodes, cls_of):
    use = collections.defaultdict(list)
    for rid in nodes:
        for d in reg.by[rid].get("defs", []):
            use[d].append(rid)
    L = [GEN_HEADER,
         r"\subsection*{Definition index --- the vocabulary the chain imports}",
         r"\phantomsection\label{tab:dag-defs}",
         r"\noindent One row per \texttt{definitions/} shard imported by a drawn result (L2: a term is "
         r"defined exactly once and only referenced elsewhere). Each row carries the anchor "
         r"\texttt{dag:\textless def-id\textgreater}, so the definitions section can link here with "
         r"\texttt{\textbackslash dagdef\{def-...\}} and this table links back to the results that use it.",
         r"\begingroup\scriptsize",
         r"\begin{longtable}{@{}l l r p{0.42\linewidth}@{}}",
         r"\toprule",
         r"\textbf{definition} & \textbf{status} & \textbf{uses} & \textbf{phases that import it} \\",
         r"\midrule\endfirsthead",
         r"\toprule \textbf{definition} & \textbf{status} & \textbf{uses} & "
         r"\textbf{phases that import it} \\ \midrule\endhead",
         r"\bottomrule\endfoot"]
    for did in sorted(use):
        fm = reg.defs.get(did, {})
        ph = collections.Counter(phase_of(r) for r in use[did])
        phs = ", ".join(f"{tex_escape(PHASE_SHORT[k])}~({ph[k]})" for k in PHASE_ORDER if ph.get(k))
        L.append(r"\hypertarget{dag:%s}{}\texttt{%s} & %s & %d & %s \\"
                 % (did, tex_escape(did), tex_escape(fm.get("status", "?")), len(use[did]), phs))
    L += [r"\end{longtable}", r"\endgroup", ""]
    unused = [d for d in reg.def_ids if d not in use]
    if unused:
        L.append(r"\noindent{\footnotesize\color{black!60}Definitions in \texttt{definitions/} not "
                 r"imported by any result on this chain (%d): %s.\par}"
                 % (len(unused), ", ".join(r"\texttt{" + tex_escape(d) + "}" for d in unused)))
    return "\n".join(L) + "\n"


SHARD_ID = "AISM-39-ARGUMENT-DAG"
SHARD_TITLE = "Argument-DAG atlas: the Route-F proof chain for op-classical"
SHARD_SUMMARIES = [
    "Generated atlas of the sub-DAG that carries the argument landing op-classical: the "
    "transitive deps/routes closure of the root together with the Route-F families, drawn "
    "layered and landscape, one detail page per phase.",
    "Nodes are colour- and glyph-coded by rigour rung (af-validated / cited / proved / seeded / "
    "proved-mod-audit-or-conjecture / stated / open) using the same proof_class function that "
    "colours the Mermaid twin argument/DAG.md, so the two views cannot disagree.",
    "Every node carries the anchor dag:<id> and links back to its report statement; any "
    "composition the live strategy reserves but the registry has not wired is drawn dashed as a "
    "design-pending GAP link and is explicitly NOT a registry edge.",
]
SHARD_KEYWORDS = ("argument DAG, atlas, Route F, op-classical, dependency graph, rigour ladder, "
                  "generated figure, crosslink anchors, GAP composition")


def root_status_sentence(reg, cls_of):
    r"""One clause about the north star's rung, DERIVED from its registry shard (never baked in).

    The atlas is regenerated whenever a shard's status/af changes, so this clause tracks the
    registry automatically instead of asserting a status that can go stale."""
    l = reg.by.get(ROOT_ID)
    if l is None:
        return r"\texttt{%s} is not present in the registry" % tex_escape(ROOT_ID)
    st, af = tex_escape(l.get("status", "?")), tex_escape(l.get("af", "none"))
    if cls_of.get(ROOT_ID) == "validated":
        return (r"the north star \dagref{%s} carries \texttt{status: %s} with \texttt{af: %s} --- "
                r"discharged at this repo's L0 rung (b), which is \emph{not} a Lean/mathlib proof"
                % (ROOT_ID, st, af))
    return (r"the north star \dagref{%s} carries \texttt{status: %s} (\texttt{af: %s}) and is "
            r"therefore not rigorous here" % (ROOT_ID, st, af))


def file_shard(reg, nodes, edges, cls_of):
    n = len(nodes)
    rig = sum(1 for i in nodes if cls_of[i] in ("validated", "cited"))
    gap = sum(1 for _u, _v, k in edges if k == "gap")
    if gap:
        gap_sentence = (r"The Route-F chain is deliberately included even where it does not reach "
                        r"the root through registry edges: that missing composition is the point, "
                        r"and it is drawn as %d dashed \textbf{design-pending (GAP)} link%s."
                        % (gap, "" if gap == 1 else "s"))
    else:
        gap_sentence = (r"Every composition the live strategy reserved is now carried by registry "
                        r"\texttt{deps:}/\texttt{routes:} edges, so no dashed "
                        r"\textbf{design-pending (GAP)} link is drawn.")
    # NOTE: single '%' — scripts/check-report-shards.sh matches '^% SHARD-...' exactly.
    L = [GEN_HEADER,
         "% SHARD-ID: " + SHARD_ID,
         "% SHARD-TITLE: " + SHARD_TITLE]
    for s in SHARD_SUMMARIES:
        L.append("% SHARD-SUMMARY: " + s)
    L += ["% SHARD-KEYWORDS: " + SHARD_KEYWORDS,
          "",
          r"\section{Argument-DAG atlas: the Route-F proof chain for \texorpdfstring{\texttt{op-classical}}"
          r"{op-classical}}",
          r"\phantomsection\label{sec:argument-dag}",
          "",
          r"This section is \textbf{generated} by \texttt{scripts/gen-report-dag.py} directly from the "
          r"registry shards \texttt{argument/lemmas/*.md} (parsed with \texttt{scripts/argument.py}'s own "
          r"parser) and is re-checked by \texttt{scripts/check-all.sh}: if a shard's \texttt{status}, "
          r"\texttt{af} state or \texttt{deps} change and this section is not regenerated, the gate fails. "
          r"It is therefore a live view of the argument, not a snapshot. Its browsable twin is "
          r"\texttt{argument/DAG.md} (Mermaid, also generated from the same shards, whole registry); this "
          r"atlas is the print/PDF view, restricted to the landing chain.",
          "",
          r"\paragraph{What is drawn.} Not the whole registry (%d results) --- only the sub-DAG that "
          r"carries the argument landing the north star: the transitive closure of \dagref{op-classical} "
          r"along \texttt{deps:} and \texttt{routes:} edges, \emph{together with} the Route-F families "
          r"named by the live strategy \texttt{docs/plans/CURRENT.md}. That is \textbf{%d results} and "
          r"%d edges. %s"
          % (len(reg.lemmas), n, len(edges), gap_sentence),
          "",
          r"\paragraph{Honest reading.} Of the %d results drawn, \textbf{%d are rigorous} in this repo's "
          r"sense (\texttt{af: validated}, or \texttt{cited} and byte-matched to \texttt{refs/}). "
          r"Everything else --- including every node coloured blue (\texttt{status: proved}) --- is a "
          r"prose proof that has \emph{not} cleared an independent \texttt{af} validation. As for the "
          r"root, %s. A path of coloured boxes from left to right is \emph{not} in itself a proof: only "
          r"the rung recorded on each node is, so read the nodes, not the arrows."
          % (n, rig, root_status_sentence(reg, cls_of)),
          "",
          r"\paragraph{Crosslinking (the anchor scheme).} Every drawn result carries the hypertarget "
          r"\texttt{dag:\textless registry-id\textgreater} on its node, and every imported definition "
          r"carries \texttt{dag:\textless def-id\textgreater} on its index row. From anywhere in this "
          r"lab-book, write \verb|\dagref{lem-prh}| or \verb|\dagdef{def-height}| to jump to the atlas, "
          r"and \verb|\dagphase{comp}{...}| to jump to a phase page. In the other direction, a node links "
          r"back (\S) to its typeset statement whenever the registry shard names one via its "
          r"\texttt{provenance:} \texttt{report \textless label\textgreater} token --- the same join key "
          r"\texttt{scripts/check-provenance.py} uses.",
          "",
          r"\input{generated/dag/legend}",
          r"\input{generated/dag/overview}",
          r"\input{generated/dag/phases}",
          r"\input{generated/dag/index}",
          r"\input{generated/dag/definitions}",
          ""]
    return "\n".join(L) + "\n"


# --------------------------------------------------------------------------------------
# driver
# --------------------------------------------------------------------------------------

def build(repo_root):
    reg = Registry(repo_root)
    nodes, edges, gaps = select_subgraph(reg)
    cls_of = {i: reg.A.proof_class(reg.by[i]) for i in nodes}
    backlink_of = {i: reg.report_label(i) for i in nodes}
    backlink_of = {k: v for k, v in backlink_of.items() if v}
    configure_chips(nodes)          # must precede the preamble (it sizes the chip style)
    files = {}
    files[str(GEN_SUBDIR / "preamble.tex")] = file_preamble()
    files[str(GEN_SUBDIR / "legend.tex")] = file_legend(reg, nodes, edges, cls_of, gaps)
    ov, _lay = file_overview(reg, nodes, edges, cls_of, backlink_of)
    files[str(GEN_SUBDIR / "overview.tex")] = ov
    files[str(GEN_SUBDIR / "phases.tex")] = file_phases(reg, nodes, edges, cls_of, backlink_of)
    files[str(GEN_SUBDIR / "index.tex")] = file_index(reg, nodes, edges, cls_of, backlink_of)
    files[str(GEN_SUBDIR / "definitions.tex")] = file_definitions(reg, nodes, cls_of)
    files[str(pathlib.Path("report") / "sections" / SHARD_NAME)] = file_shard(
        reg, nodes, edges, cls_of)
    return reg, nodes, edges, cls_of, files


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--repo", default=str(DEFAULT_ROOT), help="repo root to READ (default: this repo)")
    ap.add_argument("--out-root", default=None, help="tree to WRITE into (default: --repo)")
    ap.add_argument("--check", action="store_true",
                    help="exit 1 if any generated file on disk differs from a fresh render")
    ap.add_argument("--stats", action="store_true", help="print subgraph statistics; write nothing")
    a = ap.parse_args(argv)
    repo = pathlib.Path(a.repo).resolve()
    out = pathlib.Path(a.out_root).resolve() if a.out_root else repo

    reg, nodes, edges, cls_of, files = build(repo)
    for e in reg.errors:
        print(f"[gen-report-dag] registry parse warning: {e}")

    if a.stats:
        cnt = collections.Counter(cls_of[i] for i in nodes)
        ph = collections.Counter(phase_of(i) for i in nodes)
        ek = collections.Counter(k for _u, _v, k in edges)
        print(f"[gen-report-dag] {len(nodes)} results / {len(edges)} edges "
              f"(of {len(reg.lemmas)} in the registry)")
        print("  status classes:", dict(sorted(cnt.items())))
        print("  phases:        ", {k: ph.get(k, 0) for k in PHASE_ORDER})
        print("  edge kinds:    ", dict(sorted(ek.items())))
        return 0

    if a.check:
        stale = []
        for rel, text in sorted(files.items()):
            p = out / rel
            have = p.read_text(encoding="utf-8") if p.is_file() else None
            if have != text:
                stale.append(rel + (" (missing)" if have is None else " (differs)"))
        if stale:
            print("[gen-report-dag] STALE — the committed argument-DAG atlas does not match the "
                  "registry shards. Run: python3 scripts/gen-report-dag.py")
            for s in stale:
                print(f"  {s}")
            return 1
        print(f"[gen-report-dag] OK — atlas current ({len(nodes)} results, {len(edges)} edges, "
              f"{len(files)} generated files)")
        return 0

    for rel, text in sorted(files.items()):
        p = out / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
    print(f"[gen-report-dag] wrote {len(files)} files ({len(nodes)} results, {len(edges)} edges)")
    for rel in sorted(files):
        print(f"  {rel}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
