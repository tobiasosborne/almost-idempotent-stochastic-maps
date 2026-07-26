#!/usr/bin/env python3
r"""
gen-report-defs.py — render definitions/*.md (Layer 0, the canonical vocabulary) into the
generated LaTeX definition environments that the report's definitions section \inputs.

WHY THIS EXISTS (CLAUDE.md L2 — "one canonical definition; drift is death").
The report was unreadable because its lemma shards name `def-<slug>` terms that were never
stated in the document.  The naive fix — hand-writing the definitions into a report shard —
would create a SECOND statement of every term and is exactly the drift L2 forbids.  So the
report content is a DETERMINISTIC PROJECTION of the shards, in the same spirit as the
generated argument/INDEX.md and argument/DAG.md: the shard stays the single source of truth,
this script renders it, and `--check` fails the gate when the committed render is stale.

OUTPUT (default report/generated/defs/, all files GENERATED — never hand-edit):
  _all.tex                          loader: rendering macros (\providecommand-guarded) + \input
                                    of the layer files, in reading order
  layer-1-classical-picture.tex     one \begin{definition} ... \end{definition} + provenance
  layer-2-approximate-cstar.tex     block per shard, grouped by conceptual layer
  layer-3-internal-packages.tex
  MANIFEST.md                       the id -> layer/order/label/kind/status/provenance table
                                    (a lookup twin of definitions/INDEX.md, for humans and for
                                    the DAG generator)
The prose that frames this material is HAND-WRITTEN and lives in the report shard
report/sections/00a_definitions.tex; that shard \inputs generated/defs/_all.  Prose refers to
definitions, never restates them.

READING ORDER (deterministic; no per-definition hand curation anywhere in this file).
1. DEPENDENCY GRAPH.  For each shard we read only its *statement region* — the body up to the
   first `**Notes`/`**Provenance`/`**Status`/`**Notation`/`**Scope`/`**Specialization`/
   `**Ratification` run-in label — and take every `[[def-...]]` crosslink in it as an edge
   "this definition USES that one".  Links in the Notes/provenance tail are see-also pointers
   and are deliberately NOT edges (they are frequently mutual and carry no reading order).
2. LAYERS (conceptual grouping, derived from the data, not curated):
     layer 1  the LARGEST connected component of the undirected statement graph (ties broken by
              the lexicographically smallest member id).  In this repo that is the classical
              signed/stochastic picture — the component every classical-geometry term hangs off.
     layer 2  of what remains, every shard with `kind: cited` — vocabulary transcribed from a
              pinned refs/ source (here: the approximate-C* material).
     layer 3  everything else: project-internal packaging (`consensus`/`original`) that does not
              attach to the layer-1 component.
   A shard migrates automatically when its crosslinks or kind change; nothing here names a
   definition by hand.
3. ORDER WITHIN A LAYER.  Statement-graph edges are cyclic in general (def-stochastic and
   def-signed-idempotent define each other), so we condense strongly connected components
   (Tarjan) and emit the condensation in dependency-first topological order, breaking ties by
   the smallest member id and ordering members inside an SCC by id.  Cross-layer edges are
   ignored for ordering (they are reported in the manifest instead).

CROSSLINK SCHEME.  Every rendered definition gets \hypertarget{def:<slug>}{} and
\label{def:<slug>}, where <slug> is the shard id with its FIRST hyphen turned into a colon
(def-co-top -> def:co-top) — the repo-wide id->label transform that scripts/check-provenance.py
already uses (`labels_of`).  Lemma shards may therefore write \Cref{def:co-top}, and the DAG
page may link to the same anchors.  Inside a rendered statement:
  [[def-x|text]] / [[def-x]]  -> \hyperref[def:x]{...}
  [[lem-x]] etc.              -> \hyperref[<report label>]{\texttt{lem-x}} when the registry
                                 shard is anchored in report/ (its `provenance: report <label>`
                                 token, or the id transform, resolves to a \label in
                                 report/sections/*.tex), else plain \texttt{lem-x}.
  --dag-anchors                -> additionally link unanchored registry ids to \hyperref[dag:<id>]
                                 (OFF by default: emitting a \ref to a label that does not exist
                                 yet would be an undefined reference, which check-provenance
                                 --build promotes to a hard error.  Turn it on in the same commit
                                 that lands scripts/gen-report-dag.py).
Each definition also carries a pointer line: the canonical shard path, the registry results that
import it (report-anchored ones hyperlinked), and the DAG/index twins.

MARKDOWN -> LATEX, AND THE HONEST FALLBACK.  Shard bodies are markdown with LaTeX-ish math.  The
converter protects code spans and math spans FIRST (their bytes are never rewritten except for
the unicode table below), then escapes LaTeX specials in the remaining prose, then applies the
markdown constructs actually in use (run-in bold, emphasis, bullet lists, fenced source blocks).
A block that does not convert CLEANLY — unbalanced math delimiters, a stray backslash outside
math, an unmapped non-ASCII character, unbalanced braces in the emitted LaTeX, or a math span
that uses a macro the report preamble does not define (a source-private \eps, \calA, …) — is NOT patched
up and NOT silently mangled: it is emitted as a faithful byte-verbatim quote instead, the
definition is flagged in the rendered output with a visible rendering note, and the fallback is
listed on stdout and in MANIFEST.md.  Fenced ```blocks``` (the byte-verbatim source text of a
`cited` shard) are ALWAYS quoted verbatim, one detokenized line at a time inside the house
rule-delimited quote block (the \contractquote pattern of report/main.tex), so long source lines
wrap instead of running off the page.

CLI
  python3 scripts/gen-report-defs.py                 # (re)write report/generated/defs/
  python3 scripts/gen-report-defs.py --check         # exit 1 if the committed render is STALE
  python3 scripts/gen-report-defs.py --out DIR       # render elsewhere (build tests)
  python3 scripts/gen-report-defs.py --root DIR      # treat DIR as the repo root
  python3 scripts/gen-report-defs.py --dag-anchors   # link unanchored ids to dag:<id> anchors
Stdlib only; output depends on nothing but the repo contents (no timestamps, no dict order).
"""
import argparse
import os
import pathlib
import re
import sys
import unicodedata

# ---------------------------------------------------------------- configuration

DEF_DIR_NAME = "definitions"
LEM_DIR_NAME = os.path.join("argument", "lemmas")
SECTIONS_NAME = os.path.join("report", "sections")
DEFAULT_OUT = os.path.join("report", "generated", "defs")

GEN_WARNING = (
    "% GENERATED by scripts/gen-report-defs.py — DO NOT HAND-EDIT.\n"
    "% Single source of truth: definitions/<id>.md (CLAUDE.md L2).  Re-render with\n"
    "%   python3 scripts/gen-report-defs.py\n"
    "% The gate `python3 scripts/gen-report-defs.py --check` fails when this file is stale.\n"
)

# Layer titles/keys are fixed so the generated FILE NAMES never change with the data; which
# shard lands in which layer is computed (see module docstring, "READING ORDER").
LAYERS = [
    ("classical-picture", "The classical picture: the signed and stochastic vocabulary"),
    ("approximate-cstar", "The approximate $C^{*}$-algebra vocabulary (transcribed from the pinned source)"),
    ("internal-packages", "Project-internal packaging: hypothesis data and derived notation"),
]
LAYER_FILE = {key: f"layer-{i+1}-{key}.tex" for i, (key, _t) in enumerate(LAYERS)}

# Run-in bold labels that close the *statement region* of a shard body (see docstring).
TAIL_LABEL_RE = re.compile(
    r"\*\*(?:Notes|Provenance|Status|Notation|Scope|Specialization|Specialisation|Ratification)"
)

REGISTRY_PREFIXES = ("lem-", "thm-", "prop-", "cor-", "conj-", "op-", "obs-", "ex-")

# Unicode -> LaTeX.  Sequences first (longest match wins); the combining-tilde pair must be
# mapped as a unit.  Text mode gets $-wrapped math; math mode gets the bare macro.
UNICODE_MATH = [
    ("\u03c3\u0303", r"\widetilde\sigma"),   # σ̃
    ("\u03b4", r"\delta"),
    ("\u03c3", r"\sigma"),
    ("\u03c1", r"\rho"),
    ("\u03ba", r"\kappa"),
    ("\u03b5", r"\varepsilon"),
    ("\u03b7", r"\eta"),
    ("\u2113", r"\ell"),
    ("\u221e", r"\infty"),
    ("\u2192", r"\to"),
]
UNICODE_TEXT = [
    ("\u2014", "---"),
    ("\u2013", "--"),
    ("\u00a7", r"\S{}"),
] + [(u, "$" + m + "$") for u, m in UNICODE_MATH]

# Typographic normalisations applied to escaped PROSE (never to math, code or verbatim source):
# the shards write the C*-algebra star as a bare ASCII asterisk in term names and prose
# ("ε-C*-algebra"), which LaTeX would set as a raised text asterisk and which the markdown
# emphasis rule would otherwise see as an unpaired marker.
NORMALISATIONS = [
    (re.compile(r"\bC\*(?=-|\s|\)|,|;|\.|$)"), "$C^{*}$"),
]

ESCAPES = {
    "&": r"\&", "%": r"\%", "#": r"\#", "_": r"\_", "{": r"\{", "}": r"\}",
    "$": r"\$", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}",
    "<": r"\textless{}", ">": r"\textgreater{}",
}

PH_OPEN, PH_CLOSE = "\x00", "\x01"          # placeholder sentinels (never appear in sources)

# Math spans are passed through byte-identically, so a shard that quotes the SOURCE's private
# macros (\eps, \calA, \Ma, …) inside real math would not compile.  Every control sequence in a
# math span is therefore checked against: this base list of standard LaTeX/amsmath/amssymb
# commands, plus everything report/main.tex defines (parsed at run time).  Anything else makes
# the block fall back to a byte-verbatim quote — never a silent mangling, never a broken build.
# A standard command missing from this list only costs a (reported) verbatim fallback.
BASE_MACROS = set("""
alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa lambda mu nu xi
pi varpi rho varrho sigma varsigma tau upsilon phi varphi chi psi omega Gamma Delta Theta Lambda
Xi Pi Sigma Upsilon Phi Psi Omega ell hbar imath jmath aleph infty emptyset varnothing nabla
partial forall exists neg top bot angle triangle prime circ bullet cdot cdots ldots dots vdots
ddots dotsc dotsb times div pm mp ast star dagger ddagger oplus ominus otimes oslash odot cap
cup sqcap sqcup vee wedge setminus wr diamond bigcap bigcup bigoplus bigotimes bigwedge bigvee
sum prod coprod int oint iint bigsqcup le leq ge geq ne neq equiv sim simeq cong approx asymp
propto ll gg subset supset subseteq supseteq subsetneq sqsubseteq in ni notin perp mid parallel
models vdash dashv leftarrow rightarrow leftrightarrow Leftarrow Rightarrow Leftrightarrow to
gets mapsto longmapsto longrightarrow longleftarrow hookrightarrow uparrow downarrow implies
iff colon frac dfrac tfrac binom dbinom tbinom sqrt overline underline widetilde widehat
overbrace underbrace overset underset stackrel substack tilde hat bar vec dot ddot check acute
grave breve mathring not left right big Big bigg Bigg bigl bigr Bigl Bigr biggl biggr Biggl
Biggr lVert rVert lvert rvert langle rangle lceil rceil lfloor rfloor vert Vert backslash
mathbb mathbf mathcal mathfrak mathrm mathsf mathtt mathit mathnormal boldsymbol bm text textup
textbf textit texttt textrm textsf emph operatorname operatorname* limits nolimits displaystyle
textstyle scriptstyle scriptscriptstyle max min sup inf lim limsup liminf arg deg det dim exp
gcd hom ker log ln lg sin cos tan cot sec csc sinh cosh tanh coth arcsin arccos arctan Pr
quad qquad hspace vspace smallskip medskip bigskip par noindent phantom hphantom vphantom mbox
hbox nonumber label ref eqref begin end array matrix pmatrix bmatrix vmatrix cases aligned
split gathered substack intertext mathstrut strut relax ldotp cdotp thinspace negthinspace mathbin mathrel mathop
mathord mathopen mathclose mathpunct mathinner nobreakspace allowbreak
""".split())

MACRO_DEF_RE = re.compile(
    r"\\(?:new|renew|provide)command\*?\s*\{?\\([A-Za-z]+)\}?"
    r"|\\DeclareMathOperator\*?\s*\{\\([A-Za-z]+)\}")


class Refuse(Exception):
    """Raised when a block cannot be converted cleanly; the caller quotes it verbatim."""


# ---------------------------------------------------------------- shard parsing

def parse_frontmatter(text):
    """Flat `key: value` YAML frontmatter -> dict (last wins), plus the remaining body."""
    if not text.startswith("---"):
        raise Refuse("no frontmatter")
    end = text.find("\n---", 3)
    if end == -1:
        raise Refuse("unterminated frontmatter")
    fm = {}
    for line in text[3:end].splitlines():
        if not line.strip() or line.lstrip().startswith("#") or ":" not in line:
            continue
        k, v = line.split(":", 1)
        fm[k.strip()] = v.strip()
    return fm, text[end + 4:].lstrip("\n")


def load_definitions(root):
    """definitions/def-*.md -> {id: {'fm':…, 'body':…, 'path':…}} (sorted, deterministic)."""
    out = {}
    for path in sorted((pathlib.Path(root) / DEF_DIR_NAME).glob("def-*.md")):
        fm, body = parse_frontmatter(path.read_text(encoding="utf-8-sig"))
        did = fm.get("id", path.stem)
        out[did] = {"fm": fm, "body": body,
                    "path": os.path.join(DEF_DIR_NAME, path.name)}
    return out


def load_registry(root):
    """argument/lemmas/*.md -> {id: frontmatter} (for the def -> results reverse index)."""
    out = {}
    lemdir = pathlib.Path(root) / LEM_DIR_NAME
    for path in sorted(lemdir.glob("*.md")) if lemdir.is_dir() else []:
        if path.name in ("README.md", "INDEX.md"):
            continue
        try:
            fm, _body = parse_frontmatter(path.read_text(encoding="utf-8-sig"))
        except Refuse:
            continue
        out[fm.get("id", path.stem)] = fm
    return out


def load_report_labels(root):
    r"""\label{} names live in report/sections/*.tex, ignoring %-commented lines."""
    labels = set()
    secs = pathlib.Path(root) / SECTIONS_NAME
    for path in sorted(secs.glob("*.tex")) if secs.is_dir() else []:
        for line in path.read_text(encoding="utf-8").splitlines():
            labels |= set(re.findall(r"\\label\{([a-z]+:[A-Za-z0-9-]+)\}", strip_tex_comment(line)))
    return labels


def load_allowed_macros(root):
    r"""BASE_MACROS plus every command report/main.tex defines (\newcommand/\DeclareMathOperator)."""
    allowed = set(BASE_MACROS)
    master = pathlib.Path(root) / "report" / "main.tex"
    if master.is_file():
        for line in master.read_text(encoding="utf-8").splitlines():
            for m in MACRO_DEF_RE.finditer(strip_tex_comment(line)):
                allowed.add(m.group(1) or m.group(2))
    return allowed


def strip_tex_comment(line):
    """Drop a TeX %-comment, honouring an escaped \\% (same rule as check-provenance.py)."""
    out, i = [], 0
    while i < len(line):
        if line[i] == "\\" and i + 1 < len(line):
            out.append(line[i:i + 2])
            i += 2
            continue
        if line[i] == "%":
            break
        out.append(line[i])
        i += 1
    return "".join(out)


def label_of(shard_id):
    """The repo-wide id -> report-label transform: first hyphen becomes a colon."""
    return shard_id.replace("-", ":", 1)


def report_label_of(reg_fm, texlabels):
    """The report label a registry shard is anchored at, or None (mirrors check-provenance)."""
    for lab in re.findall(r"report\s+([a-z]+:[A-Za-z0-9-]+)", reg_fm.get("provenance", "")):
        if lab in texlabels:
            return lab
    cand = label_of(reg_fm.get("id", ""))
    return cand if cand in texlabels else None


# ---------------------------------------------------------------- graph, layers, order

def statement_region(body):
    """The part of a shard body before the first Notes/Provenance/Status/... run-in label."""
    m = TAIL_LABEL_RE.search(body)
    return body[:m.start()] if m else body


def wikilinks(text):
    """Every [[target]] / [[target|display]] in `text`, in order of appearance."""
    return [(m.group(1), m.group(2)) for m in
            re.finditer(r"\[\[([A-Za-z0-9_-]+)(?:\|([^\]]*))?\]\]", text)]


def build_edges(defs):
    """{id: sorted deps} — 'uses' edges from statement-region [[def-...]] crosslinks."""
    edges = {}
    for did, d in defs.items():
        deps = {t for t, _disp in wikilinks(statement_region(d["body"]))
                if t in defs and t != did}
        edges[did] = sorted(deps)
    return edges


def components(defs, edges):
    """Connected components of the UNDIRECTED statement graph (list of sorted id lists)."""
    parent = {d: d for d in defs}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a in sorted(edges):
        for b in edges[a]:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[max(ra, rb)] = min(ra, rb)
    groups = {}
    for d in sorted(defs):
        groups.setdefault(find(d), []).append(d)
    return sorted(groups.values(), key=lambda g: (-len(g), g[0]))


def assign_layers(defs, edges):
    """{id: layer_key} by the documented, data-derived rule (see the module docstring)."""
    comps = components(defs, edges)
    core = set(comps[0]) if comps else set()
    layers = {}
    for did, d in defs.items():
        if did in core:
            layers[did] = LAYERS[0][0]
        elif d["fm"].get("kind") == "cited":
            layers[did] = LAYERS[1][0]
        else:
            layers[did] = LAYERS[2][0]
    return layers


def tarjan_scc(nodes, edges):
    """SCCs of the directed subgraph on `nodes` — iterative Tarjan, deterministic order."""
    index, low, on_stack, stack, order, result = {}, {}, set(), [], [0], []
    nodes = sorted(nodes)
    nodeset = set(nodes)
    for root in nodes:
        if root in index:
            continue
        work = [(root, 0)]
        while work:
            v, pi = work[-1]
            if pi == 0:
                index[v] = low[v] = order[0]
                order[0] += 1
                stack.append(v)
                on_stack.add(v)
            succs = [w for w in edges.get(v, []) if w in nodeset]
            if pi < len(succs):
                work[-1] = (v, pi + 1)
                w = succs[pi]
                if w not in index:
                    work.append((w, 0))
                elif w in on_stack:
                    low[v] = min(low[v], index[w])
                continue
            if low[v] == index[v]:
                comp = []
                while True:
                    w = stack.pop()
                    on_stack.discard(w)
                    comp.append(w)
                    if w == v:
                        break
                result.append(sorted(comp))
            work.pop()
            if work:
                u = work[-1][0]
                low[u] = min(low[u], low[v])
    return sorted(result, key=lambda c: c[0])


def order_layer(nodes, edges):
    """Dependency-first order inside a layer: SCC condensation, Kahn, min-id tie-break."""
    nodes = sorted(nodes)
    nodeset = set(nodes)
    sccs = tarjan_scc(nodes, edges)
    scc_of = {n: i for i, comp in enumerate(sccs) for n in comp}
    # deps[i] = the SCCs that SCC i uses and that must therefore be emitted first
    deps = {i: set() for i in range(len(sccs))}
    rdeps = {i: set() for i in range(len(sccs))}
    for i, comp in enumerate(sccs):
        for n in comp:
            for w in edges.get(n, []):
                if w in nodeset and scc_of[w] != i:
                    deps[i].add(scc_of[w])
                    rdeps[scc_of[w]].add(i)
    ready = sorted(i for i in deps if not deps[i])
    emitted, out = set(), []
    while ready:
        ready.sort(key=lambda i: sccs[i][0])
        i = ready.pop(0)
        emitted.add(i)
        out.extend(sccs[i])
        for j in sorted(rdeps[i]):
            if j not in emitted and deps[j] <= emitted and j not in ready:
                ready.append(j)
    for i, comp in enumerate(sccs):          # defensive: never drop a node
        if i not in emitted:
            out.extend(comp)
    return out


# ---------------------------------------------------------------- markdown -> latex

def _stash(store, latex):
    store.append(latex)
    return f"{PH_OPEN}{len(store) - 1}{PH_CLOSE}"


def _unstash(text, store):
    return re.sub(PH_OPEN + r"(\d+)" + PH_CLOSE, lambda m: store[int(m.group(1))], text)


def map_unicode(text, math_mode=False):
    table = UNICODE_MATH if math_mode else UNICODE_TEXT
    for src, dst in table:
        text = text.replace(src, dst)
    return text


def check_ascii(text, where):
    for ch in text:
        if ord(ch) > 127 and ch not in (PH_OPEN, PH_CLOSE):
            raise Refuse(f"unmapped non-ASCII {ch!r} (U+{ord(ch):04X}, "
                         f"{unicodedata.name(ch, '?')}) in {where}")


def convert_code_spans(text, store):
    """`code` -> \\texttt{...}, escaped by tt() (which survives backslashes, braces and _)."""
    def repl(m):
        code = m.group(1)
        return _stash(store, r"\texttt{" + tt(code) + "}")
    return re.sub(r"`([^`\n]+)`", repl, text)


def check_macros(math, allowed):
    """Every control sequence in a math span must be defined by the report preamble."""
    for m in re.finditer(r"\\([A-Za-z]+)", math):
        if m.group(1) not in allowed:
            raise Refuse(f"math uses \\{m.group(1)}, which report/main.tex does not define "
                         f"(a source-private macro?)")


def convert_math(text, store, ctx):
    """Protect $$…$$, \\[…\\], \\(…\\), $…$ — bytes preserved, unicode mapped in math mode."""
    def wrap(open_, close_):
        def repl(m):
            check_macros(m.group(1), ctx["macros"])
            return _stash(store, open_ + map_unicode(m.group(1), math_mode=True) + close_)
        return repl

    text = re.sub(r"\$\$(.+?)\$\$", wrap("\\[", "\\]"), text, flags=re.S)
    text = re.sub(r"\\\[(.+?)\\\]", wrap("\\[", "\\]"), text, flags=re.S)
    text = re.sub(r"\\\((.+?)\\\)", wrap("\\(", "\\)"), text, flags=re.S)
    text = re.sub(r"\$([^$]+?)\$", wrap("$", "$"), text, flags=re.S)
    if "$" in text:
        raise Refuse("unbalanced $ math delimiter")
    return text


def convert_links(text, store, ctx):
    """[[def-x|disp]] / [[lem-y]] -> hyperlinked LaTeX (see CROSSLINK SCHEME in the docstring)."""
    def repl(m):
        target, disp = m.group(1), m.group(2)
        if target in ctx["defs"]:
            body = convert_inline(disp, ctx) if disp else r"\texttt{" + tt(target) + "}"
            return _stash(store, r"\hyperref[" + label_of(target) + "]{" + body + "}")
        if target.startswith(REGISTRY_PREFIXES):
            shown = r"\texttt{" + tt(target) + "}"
            lab = ctx["anchor"].get(target)
            if lab:
                return _stash(store, r"\hyperref[" + lab + "]{" + shown + "}")
            if ctx["dag_anchors"] and target in ctx["registry"] \
                    and target in _dag_anchor_ids(ctx):
                return _stash(store, r"\hyperlink{dag:" + target + "}{" + shown + "}")
            return _stash(store, shown)
        return _stash(store, r"\texttt{" + tt(target) + "}")
    return re.sub(r"\[\[([A-Za-z0-9_-]+)(?:\|([^\]]*))?\]\]", repl, text)


def tt(text, breaks=True):
    r"""Escape a metadata string (an id, a path, a locus, a code span) for \texttt.

    Escape FIRST, then map unicode, so the mapping's own backslashes and braces survive; the
    mapped math is wrapped in \textnormal so a symbol is not asked of the typewriter family
    (which has no math shape).  With breaks=True, `\allowbreak` is inserted after the natural
    break characters of a path/identifier — without them a long locus is one unbreakable box
    and overflows the text block."""
    escaped = "".join(ESCAPES.get(ch, r"\textbackslash{}" if ch == "\\" else ch) for ch in text)
    out = collapse_adjacent_math(map_unicode(escaped))
    out = re.sub(r"\$([^$]+)\$", lambda m: r"\textnormal{$" + m.group(1) + "$}", out)
    if breaks:
        out = re.sub(r"(?<=[/\-.,;:])(?![\-.,;:\\])", r"\\allowbreak{}", out)
    return out


def collapse_adjacent_math(text):
    r"""Two abutting math spans ("$\ell$$\infty$", from a run of unicode math characters in a
    metadata string) are one span: "$\ell\infty$".  Display math has already been rewritten to
    \[…\] by this point, so a "$$" here can only be an abutment."""
    return text.replace("$$", "")


def escape_text(text):
    out = []
    for ch in text:
        if ch == "\\":
            raise Refuse("stray backslash outside math/code")
        out.append(ESCAPES.get(ch, ch))
    return "".join(out)


def convert_inline(text, ctx):
    """One run of markdown prose (no fences, no list structure) -> LaTeX."""
    store = []
    text = convert_code_spans(text, store)
    text = convert_links(text, store, ctx)
    text = convert_math(text, store, ctx)
    text = escape_text(text)
    for pattern, replacement in NORMALISATIONS:
        # stashed, so the replacement's own markup is not re-read by the rules below
        text = pattern.sub(lambda _m, r=replacement: _stash(store, r), text)
    # markdown emphasis (bold first: ** must not be eaten by the * rule)
    text = re.sub(r"\*\*(?=\S)(.+?)(?<=\S)\*\*", lambda m: r"\textbf{" + m.group(1) + "}", text, flags=re.S)
    # (emphasis and quoted spans routinely straddle a source line break, so both rules run
    #  with re.S; blocks are single paragraphs, so a match can never cross a blank line)
    text = re.sub(r"(?<![\w*])\*(?=\S)([^*]+?)(?<=\S)\*(?![\w*])",
                  lambda m: r"\emph{" + m.group(1) + "}", text, flags=re.S)
    if "*" in text:
        raise Refuse("unpaired markdown emphasis marker")
    text = re.sub(r'"([^"]+?)"', lambda m: "``" + m.group(1) + "''", text, flags=re.S)
    if '"' in text:
        raise Refuse("unpaired double quote")
    text = collapse_adjacent_math(map_unicode(text))
    check_ascii(text, "prose")
    text = _unstash(text, store)
    if text.count("{") != text.count("}"):
        raise Refuse("unbalanced braces in the rendered LaTeX")
    return re.sub(r"[ \t]+\n", "\n", text).strip()


def convert_paragraph(block, ctx):
    """A paragraph, or a `- `-bullet list, of markdown prose."""
    lines = block.split("\n")
    if lines[0].lstrip().startswith("- "):
        items, cur = [], None
        for line in lines:
            if line.lstrip().startswith("- "):
                if cur is not None:
                    items.append(cur)
                cur = line.lstrip()[2:]
            else:
                if cur is None:
                    raise Refuse("list continuation before any item")
                cur += "\n" + line.strip()
        if cur is not None:
            items.append(cur)
        body = "\n".join(r"\item " + convert_inline(it, ctx) for it in items)
        return "\\begin{itemize}\n" + body + "\n\\end{itemize}"
    return convert_inline(block, ctx)


def verbatim_quote(raw):
    r"""The house byte-verbatim presentation: one \detokenize'd line per source line inside the
    rule-delimited quote block (report/main.tex's \contractquote pattern), so that very long
    source lines wrap at spaces instead of running off the page.  Raises Refuse when a line is
    not \detokenize-safe (a `%`, unbalanced braces, a `#`, or an unmappable character), so the
    caller can drop to a plain verbatim environment."""
    out = ["\\begin{defsourcequote}"]
    for line in raw.split("\n"):
        if not line.strip():
            out.append(r"\defsourcegap")
            continue
        if "%" in line or "#" in line or line.count("{") != line.count("}"):
            raise Refuse("source line is not \\detokenize-safe")
        check_ascii(line, "verbatim source line")
        out.append(r"\defsourceline{" + line + "}")
    out.append("\\end{defsourcequote}")
    return "\n".join(out)


def plain_verbatim(raw):
    """Last-resort faithful quote: a plain verbatim environment (no wrapping, but unmangled)."""
    if any(ord(ch) > 127 for ch in raw):
        raw = map_unicode(raw)                     # verbatim cannot carry raw unicode
    body = "\n".join(line.replace("\\end{verbatim}", "\\end {verbatim}") for line in raw.split("\n"))
    return "\\begin{verbatim}\n" + body + "\n\\end{verbatim}"


def split_blocks(body):
    """Body -> [('fence', raw) | ('text', raw)] in order; blank-line separated paragraphs."""
    blocks, buf = [], []

    def flush():
        text = "\n".join(buf).strip("\n")
        buf.clear()
        for para in re.split(r"\n\s*\n", text):
            if para.strip():
                blocks.append(("text", para.strip("\n")))

    in_fence, fence = False, []
    for line in body.split("\n"):
        if line.startswith("```"):
            if in_fence:
                blocks.append(("fence", "\n".join(fence)))
                fence, in_fence = [], False
            else:
                flush()
                in_fence = True
            continue
        (fence if in_fence else buf).append(line)
    if in_fence:                                    # unterminated fence: keep the bytes
        blocks.append(("fence", "\n".join(fence)))
    flush()
    return blocks


def render_body(did, body, ctx):
    """Render a shard body; returns (latex, [fallback reasons])."""
    chunks, fallbacks = [], []
    for kind, raw in split_blocks(body):
        if kind == "fence":
            try:
                chunks.append(verbatim_quote(raw))
            except Refuse as exc:
                fallbacks.append(f"source block quoted with plain verbatim ({exc})")
                chunks.append(plain_verbatim(raw))
            continue
        try:
            chunks.append(convert_paragraph(raw, ctx))
        except Refuse as exc:
            fallbacks.append(f"block quoted verbatim ({exc}): {raw.strip()[:60]!r}")
            try:
                chunks.append(verbatim_quote(raw))
            except Refuse:
                chunks.append(plain_verbatim(raw))
    return "\n\n".join(chunks), fallbacks


# ---------------------------------------------------------------- rendering

KIND_GLOSS = {
    "cited": "cited (byte-matched to a pinned source under \\texttt{refs/})",
    "consensus": "consensus (project-internal, agreed; no single external source)",
    "original": "original (introduced by this project)",
}


def render_meta(did, d, ctx):
    """The provenance/pointer block printed under a definition (footnotesize, quiet)."""
    fm = d["fm"]
    kind = fm.get("kind", "?")
    lines = []
    lines.append(r"\textbf{Kind.} " + KIND_GLOSS.get(kind, tt(kind))
                 + r"; \texttt{status: " + tt(fm.get("status", "?")) + "}.")

    prov = [r"\textbf{Provenance.} \texttt{source: " + tt(fm.get("source", "?")) + "}"]
    if fm.get("locus"):
        prov.append(r"locus \texttt{" + tt(fm["locus"]) + "}")
    sha = fm.get("sha256", "-")
    if kind == "cited" and sha and sha != "-":
        prov.append(r"\textsc{sha256} prefix \texttt{" + tt(sha) + "}")
    elif sha in ("-", "", None):
        prov.append("no source hash (not a literature transcription)")
    if fm.get("consensus"):
        prov.append("record: " + tt(fm["consensus"]))
    lines.append("; ".join(prov) + ".")

    users = ctx["users"].get(did, [])
    anchored = [(u, ctx["anchor"][u]) for u in users if u in ctx["anchor"]]
    if anchored:
        shown = anchored[:6]
        rendered = ", ".join(r"\hyperref[" + lab + r"]{\texttt{" + tt(u) + "}}" for u, lab in shown)
        more = ""
        if len(anchored) > len(shown):
            more = f" and {len(anchored) - len(shown)} further reproduced result" \
                   + ("s" if len(anchored) - len(shown) != 1 else "")
        lines.append(r"\textbf{Used in this report by} " + rendered + more
                     + f" ({len(users)} registry result" + ("s" if len(users) != 1 else "")
                     + r" import it in total; see \texttt{argument/INDEX.md}).")
    elif users:
        lines.append(r"\textbf{Used by} " + str(len(users)) + " registry result"
                     + ("s" if len(users) != 1 else "")
                     + r", none of them reproduced in this report (exploration track; see "
                     + r"\texttt{argument/INDEX.md} and \texttt{report/UNWIRED.md}).")
    else:
        lines.append(r"\textbf{Used by} no registry result yet "
                     r"(vocabulary registered ahead of the argument).")

    lines.append(r"\textbf{Canonical shard.} \texttt{" + tt(d["path"])
                 + r"}; twins: \texttt{definitions/INDEX.md}, \texttt{argument/DAG.md}.")
    if ctx["fallbacks"].get(did):
        lines.append(r"\textbf{Rendering note.} " + str(len(ctx["fallbacks"][did]))
                     + " block(s) of this shard could not be typeset cleanly and are shown "
                     + "byte-verbatim above; see \\texttt{report/generated/defs/MANIFEST.md}.")
    return "\\begin{defnote}\n" + "\n\\par\n".join(lines) + "\n\\end{defnote}"


def render_definition(did, d, ctx):
    fm = d["fm"]
    body, fallbacks = render_body(did, d["body"], ctx)
    ctx["fallbacks"][did] = fallbacks
    term = convert_inline(fm.get("term", did), ctx)
    aliases = fm.get("aliases", "").strip()
    head = [f"%% ---- {did} " + "-" * max(4, 66 - len(did)),
            r"\hypertarget{" + label_of(did) + "}{}%",
            r"\begin{definition}[" + term + r"\normalfont{} (\texttt{" + tt(did) + "})]"
            + r"\label{" + label_of(did) + "}"]
    if aliases:
        head.append(r"\emph{Aliases:} " + convert_inline(aliases, ctx) + r"\par\smallskip")
    head.append(body)
    head.append(r"\end{definition}")
    head.append(render_meta(did, d, ctx))
    return "\n".join(head)


MACROS = r"""
% --- rendering macros for the generated definitions (\providecommand: report/main.tex may
% --- override them; the visual language mirrors \contractquote there) -------------------
\ifdefined\defsourcequote\else
  \newenvironment{defsourcequote}{%
    \par\addvspace{0.5\baselineskip}\footnotesize
    \noindent\hrulefill\par\nobreak\vspace{0.35ex}%
    \ttfamily\frenchspacing\raggedright\sloppy}%
   {\par\vspace{0.35ex}\noindent\hrulefill\par\addvspace{0.5\baselineskip}}
\fi
\providecommand{\defsourceline}[1]{\noindent\detokenize{#1}\par}
\providecommand{\defsourcegap}{\par\addvspace{0.4\baselineskip}}
\ifdefined\defnote\else
  \newenvironment{defnote}{%
    \par\addvspace{0.35\baselineskip}\footnotesize\raggedright\sloppy
    \noindent\ignorespaces}%
   {\par\addvspace{0.5\baselineskip}}
\fi
""".strip("\n")


def render_layer_file(key, title, ids, defs, ctx):
    parts = [GEN_WARNING, f"% Layer file: {title}",
             r"\subsection*{" + title + "}", ""]
    for did in ids:
        parts.append(render_definition(did, defs[did], ctx))
        parts.append("")
    return "\n".join(parts).rstrip("\n") + "\n"


def render_all_file(order_by_layer):
    parts = [GEN_WARNING, MACROS, ""]
    for key, title in LAYERS:
        if not order_by_layer.get(key):
            continue
        parts.append(f"% {title}")
        parts.append(r"\input{generated/defs/" + LAYER_FILE[key][:-4] + "}")
        parts.append("")
    return "\n".join(parts).rstrip("\n") + "\n"


def render_manifest(order_by_layer, defs, ctx):
    rows = ["<!-- GENERATED by scripts/gen-report-defs.py — do not hand-edit. -->",
            "# Generated report definitions — manifest",
            "",
            "Reading order, layer assignment and rendering status of every `definitions/*.md`",
            "shard projected into the report.  The shard is the single source of truth (CLAUDE.md",
            "L2); this table and the `.tex` files beside it are a deterministic projection of it.",
            ""]
    n = 0
    for key, title in LAYERS:
        ids = order_by_layer.get(key, [])
        if not ids:
            continue
        rows += [f"## {title}", "",
                 "| # | id | label | kind | status | source | locus | sha256 | registry uses | in report |",
                 "|---|---|---|---|---|---|---|---|---|---|"]
        for did in ids:
            n += 1
            fm = defs[did]["fm"]
            users = ctx["users"].get(did, [])
            anchored = [u for u in users if u in ctx["anchor"]]
            rows.append("| {} | `{}` | `{}` | {} | {} | `{}` | `{}` | `{}` | {} | {} |".format(
                n, did, label_of(did), fm.get("kind", "?"), fm.get("status", "?"),
                fm.get("source", "?"), fm.get("locus", "").replace("|", "\\|"),
                fm.get("sha256", "-"), len(users), len(anchored)))
        rows.append("")
    fb = {k: v for k, v in ctx["fallbacks"].items() if v}
    rows += ["## Rendering fallbacks", ""]
    if not fb:
        rows += ["None: every block of every shard converted cleanly to typeset LaTeX.", ""]
    else:
        rows += ["Blocks that did not convert cleanly are quoted byte-verbatim instead of being",
                 "reshaped (see the generator docstring).  One bullet per affected shard:", ""]
        for did in sorted(fb):
            for reason in fb[did]:
                rows.append(f"- `{did}` — {reason}")
        rows.append("")
    return "\n".join(rows)


# ---------------------------------------------------------------- driver

def _dag_anchor_ids(ctx):
    """ids that actually carry a \hypertarget{dag:<id>} in the generated DAG atlas.
    Linking an id without an anchor is an undefined reference (hard build error):
    the atlas is deliberately scoped to the Route-F landing chain, so defs may
    reference registry ids outside it — those render unlinked. Cached on ctx."""
    if "_dag_ids" not in ctx:
        ids = set()
        dag_dir = ctx["root"] / "report" / "generated" / "dag"
        if dag_dir.is_dir():
            pat = re.compile(r"\\hypertarget\{dag:([^}]+)\}")
            for f in sorted(dag_dir.glob("*.tex")):
                ids.update(pat.findall(f.read_text(encoding="utf-8")))
        ctx["_dag_ids"] = ids
    return ctx["_dag_ids"]


def build(root, dag_anchors=False):
    """Compute every output file: {relative filename: text}.  Pure w.r.t. the filesystem read."""
    defs = load_definitions(root)
    registry = load_registry(root)
    texlabels = load_report_labels(root)
    edges = build_edges(defs)
    layers = assign_layers(defs, edges)

    users = {did: [] for did in defs}
    for rid in sorted(registry):
        for tok in re.split(r"[;,\s]+", registry[rid].get("defs", "")):
            if tok in users:
                users[tok].append(rid)
    anchor = {}
    for rid, fm in registry.items():
        lab = report_label_of(fm, texlabels)
        if lab:
            anchor[rid] = lab

    ctx = {"defs": defs, "registry": registry, "users": users, "anchor": anchor,
           "macros": load_allowed_macros(root), "root": pathlib.Path(root),
           "dag_anchors": dag_anchors, "fallbacks": {}}

    order_by_layer = {}
    for key, _title in LAYERS:
        ids = [d for d in sorted(defs) if layers[d] == key]
        order_by_layer[key] = order_layer(ids, edges)

    files = {}
    for key, title in LAYERS:
        ids = order_by_layer.get(key, [])
        if ids:
            files[LAYER_FILE[key]] = render_layer_file(key, title, ids, defs, ctx)
    files["_all.tex"] = render_all_file(order_by_layer)
    files["MANIFEST.md"] = render_manifest(order_by_layer, defs, ctx)
    return files, ctx


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1],
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true",
                    help="exit non-zero if the committed render differs from a fresh one")
    ap.add_argument("--root", default=str(pathlib.Path(__file__).resolve().parent.parent),
                    help="repo root (default: the parent of scripts/)")
    ap.add_argument("--out", default=None, help=f"output directory (default: {DEFAULT_OUT})")
    ap.add_argument("--dag-anchors", action="store_true",
                    help="link unanchored registry ids to dag:<id> anchors (needs gen-report-dag)")
    args = ap.parse_args(argv)

    root = pathlib.Path(args.root).resolve()
    out = pathlib.Path(args.out) if args.out else root / DEFAULT_OUT
    files, ctx = build(root, dag_anchors=args.dag_anchors)

    fallbacks = sorted((did, r) for did, rs in ctx["fallbacks"].items() for r in rs)
    ndefs = sum(1 for _ in (root / DEF_DIR_NAME).glob("def-*.md"))

    if args.check:
        problems = []
        if not out.is_dir():
            problems.append(f"{out} does not exist")
        else:
            for name, text in sorted(files.items()):
                path = out / name
                if not path.is_file():
                    problems.append(f"missing generated file {name}")
                elif path.read_text(encoding="utf-8") != text:
                    problems.append(f"{name} is STALE")
            expected = set(files)
            for path in sorted(out.iterdir()):
                if path.is_file() and path.name not in expected:
                    problems.append(f"unexpected file {path.name} in the generated directory")
        if problems:
            print("gen-report-defs --check: FAILED — run `python3 scripts/gen-report-defs.py`",
                  file=sys.stderr)
            for p in problems:
                print(f"  ! {p}", file=sys.stderr)
            return 1
        print(f"gen-report-defs --check: OK ({ndefs} definitions, {len(files)} generated files, "
              f"{len(fallbacks)} verbatim fallback block(s))")
        return 0

    out.mkdir(parents=True, exist_ok=True)
    for name, text in sorted(files.items()):
        (out / name).write_text(text, encoding="utf-8")
    for path in sorted(out.iterdir()):
        if path.is_file() and path.name not in files:
            print(f"gen-report-defs: NOTE stale file left in place: {path}", file=sys.stderr)
    print(f"gen-report-defs: wrote {len(files)} file(s) to {out} ({ndefs} definitions)")
    for did, reason in fallbacks:
        print(f"  fallback: {did} — {reason}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
