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

TWO OWNER DIRECTIVES GOVERN THE OUTPUT (2026-07-26).

  (1) TYPESET-FIRST.  EVERY rendered definition's PRIMARY display is a properly typeset
      amsthm `definition` body — real math, real prose.  Byte-verbatim monospace is NEVER
      the definition; it is demoted to a small, clearly-labelled "Source check
      (byte-verbatim)" block printed AFTER the statement, as the second check.
      Where does the typeset statement come from?  A deterministic, shard-driven rule:
        (a) the shard's harmonised `**Statement …**` section if it has one (it exists
            precisely to be the readable form), else
        (b) the shard's byte-verbatim `**Byte-verbatim source text.**` fenced blocks,
            translated to compilable LaTeX by the MACRO-TRANSLATION TABLE below.
      A fragment that cannot be translated with confidence is NEVER guessed at: the part
      that does translate is typeset, and the rest is flagged LOUDLY in the rendered page
      (a `defflag` block) and listed in MANIFEST.md.  Meaning is never silently altered.

  (2) SCOPED TO THE CURRENT PROOF STRATEGY.  Only definitions the live Route-F landing
      chain actually needs are rendered.  "The chain" is not re-derived here: this script
      IMPORTS scripts/gen-report-dag.py and reuses its `select_subgraph()` verbatim, so the
      atlas and the vocabulary can never disagree about what the strategy is.  The rendered
      set is the union of
        (a) the `defs:` imports of every registry shard in that subgraph,
        (b) the `defs:` imports of every registry shard reproduced in report/sections/,
        (c) the transitive [[def-…]] statement-region crosslink closure of (a) U (b),
      and everything outside it is dropped, with an honest generated paragraph at the end of
      the section naming the dropped ids.

OUTPUT (default report/generated/defs/, all files GENERATED — never hand-edit):
  _all.tex                          loader: rendering macros (\providecommand-guarded) +
                                    \input of the (non-empty) layer files, in reading order,
                                    + the out-of-scope paragraph
  layer-1-classical-picture.tex     one \begin{definition} … \end{definition} + provenance
  layer-2-approximate-cstar.tex     note + optional source-check block per shard, grouped by
  layer-3-internal-packages.tex     conceptual layer.  An EMPTY layer emits no file at all.
  MANIFEST.md                       the id -> layer/order/label/kind/status/provenance table
                                    (a lookup twin of definitions/INDEX.md, for humans and for
                                    the DAG generator) + the scope ledger + the flag list
The prose that frames this material is HAND-WRITTEN and lives in the report shard
report/sections/00a_definitions.tex; that shard \inputs generated/defs/_all.  Prose refers to
definitions, never restates them.

READING ORDER (deterministic; no per-definition hand curation anywhere in this file).
1. DEPENDENCY GRAPH.  For each shard we read only its *statement region* — the body up to the
   first `**Notes`/`**Provenance`/`**Status`/`**Notation`/`**Scope`/`**Specialization`/
   `**Ratification` run-in label — and take every `[[def-...]]` crosslink in it as an edge
   "this definition USES that one".  Links in the Notes/provenance tail are see-also pointers
   and are deliberately NOT edges (they are frequently mutual and carry no reading order).
   The same region rule defines the closure (c) of the scoping directive above.
2. LAYERS (conceptual grouping, derived from the data, not curated), computed on the
   IN-SCOPE set only:
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
  [[def-x|text]] / [[def-x]]  -> \hyperref[def:x]{...}  IF def-x is itself rendered; a link to
                                 an out-of-scope definition would dangle, so it degrades to a
                                 plain \texttt{def-x}.
  [[lem-x]] etc.              -> \hyperref[<report label>]{\texttt{lem-x}} when the registry
                                 shard is anchored in report/ (its `provenance: report <label>`
                                 token, or the id transform, resolves to a \label in
                                 report/sections/*.tex), else plain \texttt{lem-x}.
  --dag-anchors                -> additionally link unanchored registry ids to \hyperref[dag:<id>]
                                 (OFF by default: emitting a \ref to a label that does not exist
                                 yet would be an undefined reference, which check-provenance
                                 --build promotes to a hard error.  Both gate invocations pass
                                 it; only ids that really carry a dag: hypertarget are linked.)
Each definition also carries a pointer line: the canonical shard path, the registry results that
import it (report-anchored ones hyperlinked), and the DAG/index twins.

MARKDOWN -> LATEX.  Shard bodies are markdown with LaTeX-ish math.  The converter protects code
spans and math spans FIRST (their bytes are never rewritten except for the unicode table and the
macro-translation table below), then escapes LaTeX specials in the remaining prose, then applies
the markdown constructs actually in use (run-in bold, emphasis, bullet lists).  A block that does
not convert CLEANLY — unbalanced math delimiters, a stray backslash outside math, an unmapped
non-ASCII character, unbalanced braces in the emitted LaTeX, or a math span that still uses an
undefined macro after translation — is NOT patched up and NOT silently mangled: it is emitted as
a faithful byte-verbatim quote instead, the definition carries a visible flag, and the fallback
is listed on stdout and in MANIFEST.md.

CLI
  python3 scripts/gen-report-defs.py                 # (re)write report/generated/defs/
  python3 scripts/gen-report-defs.py --check         # exit 1 if the committed render is STALE
  python3 scripts/gen-report-defs.py --out DIR       # render elsewhere (build tests)
  python3 scripts/gen-report-defs.py --root DIR      # treat DIR as the repo root
  python3 scripts/gen-report-defs.py --dag-anchors   # link unanchored ids to dag:<id> anchors
  python3 scripts/gen-report-defs.py --scope-report  # print the scope ledger, write nothing
Stdlib only (the single non-stdlib import is the repo's own scripts/gen-report-dag.py); output
depends on nothing but the repo contents (no timestamps, no dict order).
"""
import argparse
import importlib.util
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
DAG_GENERATOR = os.path.join("scripts", "gen-report-dag.py")

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

# The three section kinds a shard body is split into.  A label is recognised ONLY from this
# closed vocabulary, so a mid-paragraph run-in bold (`**cluster vertex**`, `**top-deficit**`)
# is never mistaken for a section heading.
SEC_STATEMENT_RE = re.compile(r"^\*\*Statement[^*]*\*\*", re.M)
SEC_SOURCE_RE = re.compile(r"^\*\*Byte-verbatim source text\.\*\*", re.M)
SEC_TAIL_RE = re.compile(
    r"^\*\*(?:Notes|Provenance|Status|Notation|Scope|Specialization|Specialisation|"
    r"Ratification)[^*]*\*\*", re.M)

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

# Every control sequence that survives into emitted LaTeX is checked against: this base list of
# standard LaTeX/amsmath/amssymb commands, plus everything report/main.tex defines (parsed at
# run time).  Anything else makes the block fall back to a byte-verbatim quote — never a silent
# mangling, never a broken build.  A standard command missing from this list only costs a
# (reported) verbatim fallback.
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
mathord mathopen mathclose mathpunct mathinner nobreakspace allowbreak mkern mskip
""".split())

MACRO_DEF_RE = re.compile(
    r"\\(?:new|renew|provide)command\*?\s*\{?\\([A-Za-z]+)\}?"
    r"|\\DeclareMathOperator\*?\s*\{\\([A-Za-z]+)\}")


# ======================================================================================
# THE MACRO-TRANSLATION TABLE  (version 1)
# ======================================================================================
# WHY.  A `cited` shard quotes the pinned source's OWN TeX, which is written in that source's
# private macro dialect (\eps, \calA, \Co, \Ma{n}, …).  Those macros are not defined in
# report/main.tex, so the quoted bytes cannot be typeset as-is.  Before this table existed the
# generator's only honest option was to print the bytes in a detokenized monospace block — which
# is faithful but unreadable, and made the byte-verbatim quote *be* the definition.
#
# WHAT IT IS.  An EXPLICIT, DETERMINISTIC, AUDITABLE substitution table: source macro name ->
# the expansion the SOURCE ITSELF gives it, written in commands report/main.tex already has.
# Every mapping below is byte-checked against the pinned source's own preamble:
#     refs/kitaev-2405.02434/approximate_algebras.tex   (sha256 prefix e7eb512a2ec2438d)
# and the source line number that defines it is recorded on the row.  Nothing here is invented;
# a translation is a change of SPELLING, never of meaning.  Two deliberate, documented glyph-only
# deviations are listed under "KNOWN GLYPH-ONLY DEVIATIONS" at the end of the table.
#
# HOW IT IS APPLIED.
#   * to a `cited` shard's fenced source-TeX block: the WHOLE table (those bytes are the
#     source's, so \Co there means the source's \Co);
#   * to a math span inside project-written markdown prose: only the rows whose macro name
#     report/main.tex does NOT itself define.  report/main.tex defines \Co, \Ha, \Img, \Ker and
#     \sgn with its own (different, argument-taking) meanings, and a project-authored statement
#     that writes \Co{P}{Q} means the REPORT's macro.  Translating it would be exactly the silent
#     meaning change this table exists to avoid, so those rows are held back there.
#
# AFTER TRANSLATION the result is validated (macros defined, braces balanced, $ balanced, no #,
# no bare _ ^ & outside math, ASCII only).  A block that fails validation is NOT emitted as
# mathematics: the definition carries a loud on-page flag and the bytes go to the source check.
TRANSLATION_TABLE_VERSION = 1

# --- rows with no argument: \<name> -> replacement -------------------------------------
# (macro, replacement, source line in approximate_algebras.tex, the source's own definition)
MACRO_TABLE_0 = [
    # --- blackboard-bold and calligraphic alphabets ------------------------------------
    ("RR",       r"\mathbb{R}",              47, r"\newcommand{\RR}{\mathbb{R}}"),
    ("CC",       r"\mathbb{C}",              48, r"\newcommand{\CC}{\mathbb{C}}"),
    ("calA",     r"\mathcal{A}",             50, r"\newcommand{\calA}{\mathcal{A}}"),
    ("calB",     r"\mathcal{B}",             51, r"\newcommand{\calB}{\mathcal{B}}"),
    ("calS",     r"\mathcal{S}",             68, r"\newcommand{\calS}{\mathcal{S}}"),
    # --- upright operator letters (compressions, corners, bounded maps) ----------------
    ("Bo",       r"\mathbf{B}",             107, r"\newcommand{\Bo}{\mathbf{B}}"),
    ("La",       r"\mathrm{L}",             108, r"\newcommand{\La}{\mathrm{L}}"),
    ("Ra",       r"\mathrm{R}",             109, r"\newcommand{\Ra}{\mathrm{R}}"),
    ("Co",       r"\mathrm{C}",             110, r"\newcommand{\Co}{\mathrm{C}}"),
    ("Ha",       r"\mathrm{H}",             111, r"\newcommand{\Ha}{\mathrm{H}}"),
    ("Euc",      r"\mathrm{E}",             116, r"\newcommand{\Euc}{\mathrm{E}}"),
    # --- named operators (\DeclareMathOperator -> \operatorname, identical semantics) ---
    ("Ker",      r"\operatorname{Ker}",      88, r"\DeclareMathOperator{\Ker}{Ker}"),
    ("Img",      r"\operatorname{Im}",       89, r"\DeclareMathOperator{\Img}{Im}"),
    ("Tr",       r"\operatorname{Tr}",       92, r"\DeclareMathOperator{\Tr}{Tr}"),
    ("sgn",      r"\operatorname{sgn}",      93, r"\DeclareMathOperator{\sgn}{sgn}"),
    ("ind",      r"\operatorname{ind}",      96, r"\DeclareMathOperator{\ind}{ind}"),
    ("Ta",       r"\operatorname{T}",        97, r"\DeclareMathOperator{\Ta}{T}"),
    # --- accents, spacing, products, delimiters ----------------------------------------
    ("wt",       r"\widetilde",             117, r"\newcommand{\wt}{\widetilde}"),
    ("ts",       r"\mkern1mu",               77, r"\newcommand{\ts}{\mkern1mu}"),
    ("hotimes",  r"\mathbin{\hat{\otimes}}", 85, r"\newcommand{\hotimes}{\mathbin{\hat{\otimes}}}"),
    ("blangle",  r"\bigl\langle",           120, r"\newcommand{\blangle}{\bigl\langle}"),
    ("brangle",  r"\bigr\rangle",           121, r"\newcommand{\brangle}{\bigr\rangle}"),
    # --- greek shorthand ----------------------------------------------------------------
    ("eps",      r"\varepsilon",            126, r"\newcommand{\eps}{\varepsilon}"),
    # --- KERNEL NORMALIZATION (separate section in the manifest; NOT a source-defined mapping) ---
    # Hostile table audit 2026-07-26: this row's claim is limited to math-mode glyph
    # equivalence in the LaTeX2e kernel; it is NOT "the expansion the source itself gives".
    # \dag is the LaTeX2e kernel's dagger (\dagger in math mode); the source does not redefine
    # it.  Mapped to \dagger so the check below sees a command it knows.  Same glyph, same slot.
    ("dag",      r"\dagger",                 -1, r"LaTeX2e kernel: \dag = \dagger in math mode"),
]

# --- rows that consume braced arguments: \<name>{a}{b} -> template % (a, b) -------------
# (macro, nargs, python format template, source line, the source's own definition)
MACRO_TABLE_N = [
    ("bbraket", 2, r"\bigl\langle{%s},\mkern1mu{%s}\bigr\rangle", 124,
     r"\newcommand*{\bbraket}[2]{\blangle{#1},\mkern1mu{#2}\brangle}  (\blangle/\brangle inlined)"),
    ("braket",  2, r"\langle{%s},{%s}\rangle", 123,
     r"\newcommand*{\braket}[2]{\langle{#1},{#2}\rangle}"),
    ("Ma",      1, r"\mathbf{M}_{%s}", 118,
     r"\newcommand*{\Ma}[1]{\mathbf{M}_{#1}}"),
]

# --- structural rewrites (not macro expansions; documented one by one) ------------------
# \label{k}          DROPPED.  A source label defines an anchor in the SOURCE document; keeping
#                    it would either clash with our own labels or dangle.  Nothing is lost: the
#                    key is still visible in the byte-verbatim source check below the statement.
# \ref{k}/\eqref{k}  Rendered as the source's own key in brackets, \textup{[\texttt{k}]}, NEVER as
#                    a live \ref (which would be an undefined reference and a hard build error).
#                    The reader can find the key in the pinned source.
# \begin{equation}   Starred: \begin{equation*}.  We strip the source's labels, so an equation
# \begin{alignat}{n} number here would be an un-referenceable decoration in OUR numbering.  The
# \begin{align} …    starred forms are mathematically identical.  Column specifiers ({n} after
#                    alignat) are left untouched.
# \begin{Definition} Theorem-environment DELIMITERS of the source (Definition/Lemma/Proposition/
# \begin{Lemma} …    Remark/…) are dropped, opening and closing independently, so an excerpt that
#                    quotes only the head of a source environment cannot unbalance our LaTeX.
#                    Dropping the delimiter drops only the source's own numbering and framing;
#                    the shard's Status/Provenance prose is where the shard records what part of
#                    a source environment it does and does not adopt.
# any other env      REFUSED (flagged, verbatim) — never guessed at.
MATH_ENVS_TO_STAR = ("equation", "align", "alignat", "gather", "multline", "flalign")
MATH_ENVS_KEEP = ("equation*", "align*", "alignat*", "gather*", "multline*", "flalign*",
                  "aligned", "split", "gathered", "cases", "array", "matrix", "pmatrix",
                  "bmatrix", "vmatrix", "Bmatrix", "smallmatrix")
PROSE_ENVS_KEEP = ("itemize", "enumerate", "center")
THEOREM_ENVS_TO_DROP = ("Definition", "Lemma", "Proposition", "Theorem", "Corollary",
                        "Remark", "Example", "Proof", "Conjecture", "Claim", "Notation",
                        "definition", "lemma", "proposition", "theorem", "corollary",
                        "remark", "example", "proof")
ALIGN_FAMILY = ("align", "alignat", "flalign", "array", "matrix", "cases", "aligned",
                "split", "gathered", "smallmatrix", "pmatrix", "bmatrix", "vmatrix", "Bmatrix")

# --- KNOWN GLYPH-ONLY DEVIATIONS (declared, not hidden) ---------------------------------
# 1. The source does `\renewcommand{\le}{\leqslant}` and `\renewcommand{\ge}{\geqslant}`
#    (lines 131-132).  We leave \le and \ge alone: the slanted glyph is a house style of that
#    paper, the relation is the same, and \le/\ge are what the rest of this lab-book uses.
# 2. \ts is the source's 1mu thin space (line 77).  We emit \mkern1mu, i.e. the source's own
#    expansion, so even the spacing is unchanged.
DEVIATIONS = [
    (r"\le, \ge", r"the source renews these to \leqslant / \geqslant (lines 131-132); "
                  r"we keep the upright \le / \ge --- the same relation, this lab-book's glyph"),
]


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


def load_main_macros(root):
    r"""Just the commands report/main.tex itself defines (\newcommand/\DeclareMathOperator)."""
    defined = set()
    master = pathlib.Path(root) / "report" / "main.tex"
    if master.is_file():
        for line in master.read_text(encoding="utf-8").splitlines():
            for m in MACRO_DEF_RE.finditer(strip_tex_comment(line)):
                defined.add(m.group(1) or m.group(2))
    return defined


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
        if a not in parent:
            continue
        for b in edges[a]:
            if b not in parent:
                continue
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


# ---------------------------------------------------------------- scope (directive 2)

def load_dag_generator(root):
    """Import scripts/gen-report-dag.py (never re-implement its subgraph rule); None if absent."""
    path = pathlib.Path(root) / DAG_GENERATOR
    if not path.is_file():
        return None
    spec = importlib.util.spec_from_file_location("_gen_report_dag", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def strategy_scope(root, defs, edges):
    """The definitions the CURRENT PROOF STRATEGY needs; see the module docstring, directive 2.

    Returns (rendered_ids:set, dropped_ids:sorted list, provenance:dict).  If the DAG generator
    is unavailable (a stripped test tree) the scope degrades OPENLY to "everything", recorded in
    the provenance dict, rather than silently dropping material.
    """
    mod = load_dag_generator(root)
    if mod is None:
        return set(defs), [], {"mode": "unscoped (scripts/gen-report-dag.py not found)",
                               "subgraph": 0, "anchored": 0, "seed": 0}
    reg = mod.Registry(pathlib.Path(root))
    nodes, _edges = mod.select_subgraph(reg)
    seed = set()
    for rid in nodes:                                  # (a) the Route-F landing subgraph
        seed |= set(reg.by[rid].get("defs", []))
    anchored = sorted(rid for rid in reg.by if reg.report_label(rid))
    for rid in anchored:                               # (b) the reproduced report lemma shards
        seed |= set(reg.by[rid].get("defs", []))
    seed = {d for d in seed if d in defs}
    keep = set(seed)                                   # (c) statement-region crosslink closure
    stack = sorted(keep)
    while stack:
        n = stack.pop()
        for d in edges.get(n, []):
            if d in defs and d not in keep:
                keep.add(d)
                stack.append(d)
    return keep, sorted(set(defs) - keep), {
        "mode": "Route-F landing chain (scripts/gen-report-dag.py select_subgraph)",
        "subgraph": len(nodes), "anchored": len(anchored), "seed": len(seed)}


# ---------------------------------------------------------------- macro translation

_TRANS_0 = sorted(MACRO_TABLE_0, key=lambda r: (-len(r[0]), r[0]))
_TRANS_N = sorted(MACRO_TABLE_N, key=lambda r: (-len(r[0]), r[0]))
_REF_RE = re.compile(r"\\(?:eq)?ref\{([^}]*)\}")
_LABEL_RE = re.compile(r"\\label\{[^}]*\}")
# A \label on a line of its own must take the WHOLE line with it: leaving the blank line behind
# inserts a \par, which is fatal inside an alignat/gather body ("Paragraph ended before
# \alignat* was complete").  Whole-line labels are stripped first, inline ones after.
_LABEL_LINE_RE = re.compile(r"(?m)^[ \t]*\\label\{[^}]*\}[ \t]*\n")
_BEGIN_RE = re.compile(r"\\begin\{([A-Za-z*]+)\}")
_END_RE = re.compile(r"\\end\{([A-Za-z*]+)\}")


def _braced_arg(text, i):
    """Read one balanced {...} argument starting at text[i]; returns (arg, next_index)."""
    while i < len(text) and text[i] in " \t\n":
        i += 1
    if i >= len(text) or text[i] != "{":
        raise Refuse("macro-translation: a table macro is used without a braced argument")
    depth, j = 0, i
    while j < len(text):
        if text[j] == "\\":
            j += 2
            continue
        if text[j] == "{":
            depth += 1
        elif text[j] == "}":
            depth -= 1
            if depth == 0:
                return text[i + 1:j], j + 1
        j += 1
    raise Refuse("macro-translation: unbalanced braces in a macro argument")


def _apply_narg(text, name, nargs, template, fired):
    pat = re.compile(r"\\" + name + r"(?![A-Za-z])")
    out, pos = [], 0
    while True:
        m = pat.search(text, pos)
        if not m:
            out.append(text[pos:])
            return "".join(out)
        out.append(text[pos:m.start()])
        i = m.end()
        args = []
        for _ in range(nargs):
            a, i = _braced_arg(text, i)
            args.append(a)
        out.append(template % tuple(args))
        fired.add("\\" + name)
        pos = i


def _tt_key(key):
    """A source label/ref key, escaped for \\texttt."""
    return "".join(ESCAPES.get(ch, r"\textbackslash{}" if ch == "\\" else ch) for ch in key)


def translate_macros(text, held_back=frozenset()):
    """Apply the macro-translation table.  Returns (text, fired:set of '\\name').

    `held_back` names rows that must NOT fire here (see "HOW IT IS APPLIED" on the table).
    """
    fired = set()
    for name, nargs, template, _line, _srcdef in _TRANS_N:
        if name in held_back or ("\\" + name) not in text:
            continue
        text = _apply_narg(text, name, nargs, template, fired)
    for name, repl, _line, _srcdef in _TRANS_0:
        if name in held_back:
            continue
        pat = re.compile(r"\\" + name + r"(?![A-Za-z])")
        if pat.search(text):
            text = pat.sub(lambda _m, r=repl: r, text)
            fired.add("\\" + name)
    return text, fired


def translate_structure(text):
    """Apply the structural rewrites of the table.  Returns (text, notes:set)."""
    notes = set()
    if _LABEL_RE.search(text):
        text = _LABEL_LINE_RE.sub("", text)
        text = _LABEL_RE.sub("", text)
        notes.add("source-internal " + r"\label" + "s dropped")
    if _REF_RE.search(text):
        text = _REF_RE.sub(
            lambda m: r"\textup{[\texttt{" + _tt_key(m.group(1)) + "}]}", text)
        notes.add("source cross-reference keys shown in brackets")

    def begin(m):
        env = m.group(1)
        if env in MATH_ENVS_TO_STAR:
            notes.add("display environments unnumbered (labels are stripped)")
            return r"\begin{" + env + "*}"
        if env in MATH_ENVS_KEEP or env in PROSE_ENVS_KEEP:
            return m.group(0)
        if env in THEOREM_ENVS_TO_DROP:
            notes.add("source theorem-environment delimiters dropped")
            return ""
        raise Refuse(f"macro-translation: unknown environment {env!r}")

    def end(m):
        env = m.group(1)
        if env in MATH_ENVS_TO_STAR:
            return r"\end{" + env + "*}"
        if env in MATH_ENVS_KEEP or env in PROSE_ENVS_KEEP:
            return m.group(0)
        if env in THEOREM_ENVS_TO_DROP:
            return ""
        raise Refuse(f"macro-translation: unknown environment {env!r}")

    text = _BEGIN_RE.sub(begin, text)
    text = _END_RE.sub(end, text)
    return text, notes


def _strip_math_regions(text):
    """Blank out every math region so the remainder can be checked as text mode."""
    out = text
    for env in sorted({e.rstrip("*") for e in
                       MATH_ENVS_TO_STAR + MATH_ENVS_KEEP + ALIGN_FAMILY}):
        out = re.sub(r"\\begin\{" + env + r"\*?\}.*?\\end\{" + env + r"\*?\}", " ", out,
                     flags=re.S)
    out = re.sub(r"\$\$.*?\$\$", " ", out, flags=re.S)
    out = re.sub(r"\\\[.*?\\\]", " ", out, flags=re.S)
    out = re.sub(r"\\\(.*?\\\)", " ", out, flags=re.S)
    out = re.sub(r"\$[^$]*\$", " ", out, flags=re.S)
    return out


def validate_latex(text, allowed, where):
    """Refuse anything that could break the build or change meaning.  Silence is never an option."""
    check_ascii(text, where)
    if "#" in text:
        raise Refuse("a '#' survives translation (a macro parameter would break the build)")
    for m in re.finditer(r"\\([A-Za-z]+)", text):
        if m.group(1) not in allowed:
            raise Refuse(f"\\{m.group(1)} is not defined by report/main.tex and is not in the "
                         f"translation table (a source-private macro?)")
    if text.count("{") != text.count("}"):
        raise Refuse("unbalanced braces after translation")
    if text.count("$") % 2:
        raise Refuse("unbalanced $ math delimiter after translation")
    residue = _strip_math_regions(text)
    for ch, why in (("&", "alignment tab"), ("_", "subscript"), ("^", "superscript")):
        if re.search(r"(?<!\\)" + re.escape(ch), residue):
            raise Refuse(f"a bare '{ch}' ({why}) survives outside math mode")
    return text


_MATH_DELIM_RE = re.compile(r"\$|\\\(|\\\[|\\begin\{[A-Za-z]+\*?\}")


def translate_source_block(raw, allowed, held_back=frozenset()):
    """Source TeX -> compilable LaTeX.  Returns (latex, fired:set, notes:set); raises Refuse.

    A fenced source block is one of exactly two things, told apart by a crisp, mechanical test —
    does the block contain ANY math delimiter or environment of its own (`$`, `\\(`, `\\[`,
    `\\begin{…}`)?

      YES -> source PROSE that contains mathematics.  It is already complete LaTeX and is
             emitted as text-mode material.
      NO  -> the naked BODY of a source display: the shard quoted the interior of the source's
             own `equation`/`gather` and elided the wrapper (see e.g.
             def-theta-idempotent-approximation, whose loci 505-510/517-520/527-528 sit inside
             `\\begin{gather}`/`\\begin{equation}` in the pinned source).  Such a body has no
             legal reading in text mode, so it is restored to a display environment — `gather*`,
             which is exactly what a `\\\\`-separated run of independent display lines is.  The
             restoration is RECORDED in the definition's translation note, never silent.

    Either way the result is validated afterwards; a misjudged block therefore fails loudly
    instead of shipping.
    """
    text, fired = translate_macros(raw, held_back=held_back)
    text, notes = translate_structure(text)
    text = map_unicode(text)
    if not _MATH_DELIM_RE.search(text):
        text = "\\begin{gather*}\n" + text.strip() + "\n\\end{gather*}"
        notes.add("the shard quotes the naked body of a source display; "
                  "restored to a display environment")
    validate_latex(text, allowed, "translated source block")
    return text.strip(), fired, notes


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


def convert_math(text, store, ctx):
    """Protect $$…$$, \\[…\\], \\(…\\), $…$ — bytes preserved but for the unicode and macro tables.

    A math span written in project prose is translated with the HELD-BACK table (see the table's
    "HOW IT IS APPLIED"): rows whose macro report/main.tex defines itself are left alone there.
    """
    def wrap(open_, close_):
        def repl(m):
            math = map_unicode(m.group(1), math_mode=True)
            math, fired = translate_macros(math, held_back=ctx["held_back"])
            ctx["fired"].update(fired)
            for cs in re.finditer(r"\\([A-Za-z]+)", math):
                if cs.group(1) not in ctx["macros"]:
                    raise Refuse(f"math uses \\{cs.group(1)}, which report/main.tex does not "
                                 f"define and the translation table does not cover")
            return _stash(store, open_ + math + close_)
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
            if target in ctx["rendered"]:
                return _stash(store, r"\hyperref[" + label_of(target) + "]{" + body + "}")
            # out of the current proof strategy's scope: rendered nowhere, so never linked
            return _stash(store, body)
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
    rule-delimited quote block, so that very long source lines wrap at spaces instead of running
    off the page.  Raises Refuse when a line is not \detokenize-safe (a `%`, unbalanced braces,
    a `#`, or an unmappable character), so the caller can drop to a plain verbatim environment."""
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


def quote_source(raw):
    """The byte-verbatim rendering of one source block, in whichever form is safe."""
    try:
        return verbatim_quote(raw)
    except Refuse:
        return plain_verbatim(raw)


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


# ---------------------------------------------------------------- shard sectioning

def split_sections(body):
    """Shard body -> ordered [(kind, text)] with kind in {'statement','source','tail','lead'}.

    Boundaries come from the CLOSED label vocabulary above, so an emphasised term at the start
    of a line inside a statement is never mistaken for a section heading.
    """
    marks = []
    for kind, rx in (("statement", SEC_STATEMENT_RE), ("source", SEC_SOURCE_RE),
                     ("tail", SEC_TAIL_RE)):
        for m in rx.finditer(body):
            marks.append((m.start(), kind))
    marks.sort()
    out = []
    if not marks:
        return [("lead", body)] if body.strip() else []
    if body[:marks[0][0]].strip():
        out.append(("lead", body[:marks[0][0]].strip("\n")))
    for i, (pos, kind) in enumerate(marks):
        end = marks[i + 1][0] if i + 1 < len(marks) else len(body)
        chunk = body[pos:end].strip("\n")
        if chunk.strip():
            out.append((kind, chunk))
    return out


def strip_section_label(text, rx):
    """Drop the run-in bold label that opens a section (it is re-supplied by the renderer)."""
    m = rx.match(text)
    return text[m.end():].lstrip(" \n") if m else text


# ---------------------------------------------------------------- rendering

KIND_GLOSS = {
    "cited": "cited (byte-matched to a pinned source under \\texttt{refs/})",
    "consensus": "consensus (project-internal, agreed; no single external source)",
    "original": "original (introduced by this project)",
}


def render_markdown(chunks, ctx, flags, what):
    """Render a list of markdown chunks; a chunk that refuses is quoted verbatim and FLAGGED."""
    out = []
    for chunk in chunks:
        for kind, raw in split_blocks(chunk):
            if kind == "fence":
                flags.append(f"{what}: a fenced block is quoted byte-verbatim (not typeset)")
                out.append(quote_source(raw))
                continue
            try:
                out.append(convert_paragraph(raw, ctx))
            except Refuse as exc:
                flags.append(f"{what}: a paragraph did not typeset ({exc}) — "
                             f"{raw.strip()[:60]!r}")
                out.append(flag_block(f"This paragraph could not be typeset: {exc}. "
                                      f"Its bytes follow, unaltered."))
                out.append(quote_source(raw))
    return "\n\n".join(out)


def flag_block(message):
    r"""A LOUD, on-page flag.  Nothing is ever quietly dropped or quietly reshaped."""
    return "\\begin{defflag}\n" + tex_sentence(message) + "\n\\end{defflag}"


def tex_sentence(text):
    """Escape a generator-authored sentence (never shard content) for LaTeX text mode."""
    return "".join(ESCAPES.get(ch, r"\textbackslash{}" if ch == "\\" else ch) for ch in text)


def render_statement(did, d, ctx):
    """The PRIMARY typeset body of a definition (directive 1).  Returns (latex, info)."""
    secs = split_sections(d["body"])
    flags = []
    stmts = [strip_section_label(t, SEC_STATEMENT_RE) for k, t in secs if k == "statement"]
    leads = [t for k, t in secs if k == "lead"]
    sources = [t for k, t in secs if k == "source"]
    tails = [t for k, t in secs if k == "tail"]
    info = {"origin": None, "fired": set(), "notes": set(), "flags": flags,
            "source_blocks": [], "tails": tails}

    # The byte-verbatim section of a `cited` shard, kept in reading order: its fenced blocks are
    # the source's bytes, and any prose between them is the shard's own caption for them.
    source_seq = []
    for chunk in sources:
        for kind, raw in split_blocks(chunk):
            if kind == "fence":
                info["source_blocks"].append(raw)
                source_seq.append(("fence", raw))
            elif raw.strip() and not SEC_SOURCE_RE.match(raw):
                source_seq.append(("text", raw))

    # (a) the shard's own harmonised statement, when it has one — it exists to be the readable
    #     form, so it always wins.
    if stmts or leads:
        info["origin"] = "shard"
        return render_markdown(leads + stmts, ctx, flags, "statement"), info

    # (b) otherwise TYPESET THE SOURCE TeX through the macro-translation table, keeping the
    #     shard's captions in place around the displays they introduce.
    info["origin"] = "translated"
    parts = []
    for kind, raw in source_seq:
        if kind == "text":
            parts.append(render_markdown([raw], ctx, flags, "source caption"))
            continue
        try:
            latex, fired, notes = translate_source_block(raw, ctx["macros"])
            info["fired"] |= fired
            info["notes"] |= notes
            parts.append(latex)
        except Refuse as exc:
            flags.append(f"source block NOT typeset ({exc})")
            parts.append(flag_block(
                "This fragment of the pinned source could not be translated into typeset "
                "mathematics without risking a change of meaning (" + str(exc) + "). It is "
                "therefore left untranslated; its bytes are in the source check below."))
    if not parts:
        info["origin"] = "empty"
        flags.append("the shard body carries neither a Statement section nor source text")
        parts.append(flag_block("This shard carries no statement and no source text."))
    return "\n\n".join(p for p in parts if p.strip()), info


def render_meta(did, d, ctx, info):
    """The compact provenance block printed under a definition (footnotesize, quiet)."""
    fm = d["fm"]
    kind = fm.get("kind", "?")
    lines = []

    aliases = fm.get("aliases", "").strip()
    head = r"\textbf{Kind.} " + KIND_GLOSS.get(kind, tt(kind)) \
        + r"; \texttt{status: " + tt(fm.get("status", "?")) + "}."
    if aliases:
        head += r"\quad\textbf{Aliases.} " + convert_inline(aliases, ctx) + "."
    lines.append(head)

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

    if info["origin"] == "translated":
        fired = ", ".join(r"\texttt{" + tt(f) + "}" for f in sorted(info["fired"]))
        note = (r"\textbf{Typeset from the source.} The statement above is the pinned source's "
                r"own text, set by \emph{macro-translation table v"
                + str(TRANSLATION_TABLE_VERSION)
                + r"} of \texttt{scripts/gen-report-defs.py} --- spelling only, never meaning")
        if fired:
            note += ": " + fired
        extra = sorted(info["notes"])
        if extra:
            note += "; " + "; ".join(tex_sentence(n) for n in extra)
        note += ". The byte-verbatim source is reproduced below as the second check."
        lines.append(note)

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

    # The shard's own Notes/Status/Scope/Notation tail is METADATA, not the definition: it is
    # rendered here, small and after the statement, with its run-in bold label kept.
    tail = render_markdown(info["tails"], ctx, info["flags"], "shard note")
    if tail.strip():
        lines.append(tail)

    if info["flags"]:
        lines.append(r"\textbf{Rendering note.} " + str(len(info["flags"]))
                     + " block(s) of this shard are flagged above; see "
                     + r"\texttt{report/generated/defs/MANIFEST.md}.")
    return "\\begin{defnote}\n" + "\n\\par\n".join(lines) + "\n\\end{defnote}"


def render_source_check(did, d, info):
    """The demoted second check: the shard's byte-verbatim source text, clearly labelled."""
    if not info["source_blocks"]:
        return ""
    fm = d["fm"]
    where = fm.get("source", "?")
    if fm.get("locus"):
        where += ", " + fm["locus"]
    out = [r"\defsourcecheckhead{Source check (byte-verbatim) --- \texttt{" + tt(where) + "}}"]
    out += [quote_source(raw) for raw in info["source_blocks"]]
    return "\n".join(out)


def render_definition(did, d, ctx):
    fm = d["fm"]
    body, info = render_statement(did, d, ctx)
    ctx["info"][did] = info
    term = convert_inline(fm.get("term", did), ctx)
    parts = [f"%% ---- {did} " + "-" * max(4, 66 - len(did)),
             r"\hypertarget{" + label_of(did) + "}{}%",
             r"\begin{definition}[" + term + r"\normalfont{} (\texttt{" + tt(did) + "})]"
             + r"\label{" + label_of(did) + "}",
             body,
             r"\end{definition}",
             render_meta(did, d, ctx, info)]
    check = render_source_check(did, d, info)
    if check:
        parts.append(check)
    return "\n".join(p for p in parts if p)


MACROS = r"""
% --- rendering macros for the generated definitions (\providecommand: report/main.tex may
% --- override them).  Three visual registers, in descending loudness:
% ---   definition  : the amsthm statement — THE definition (typeset, full size)
% ---   defnote     : the compact provenance/pointer line beneath it (footnotesize)
% ---   defsource*  : the demoted byte-verbatim SECOND CHECK (scriptsize, rule-delimited)
% --- plus defflag, the loud on-page marker for anything the generator would not typeset.
\ifdefined\defsourcequote\else
  \newenvironment{defsourcequote}{%
    \par\addvspace{0.35\baselineskip}\scriptsize
    \noindent\hrulefill\par\nobreak\vspace{0.3ex}%
    \ttfamily\frenchspacing\raggedright\sloppy}%
   {\par\vspace{0.3ex}\noindent\hrulefill\par\addvspace{0.5\baselineskip}}
\fi
\providecommand{\defsourceline}[1]{\noindent\detokenize{#1}\par}
\providecommand{\defsourcegap}{\par\addvspace{0.4\baselineskip}}
\providecommand{\defsourcecheckhead}[1]{%
  \par\addvspace{0.35\baselineskip}\nobreak
  \noindent{\footnotesize\scshape #1}\par\nobreak}
\ifdefined\defnote\else
  \newenvironment{defnote}{%
    \par\addvspace{0.35\baselineskip}\footnotesize\raggedright\sloppy
    \noindent\ignorespaces}%
   {\par\addvspace{0.5\baselineskip}}
\fi
\ifdefined\defflag\else
  \newenvironment{defflag}{%
    \par\addvspace{0.4\baselineskip}\footnotesize\raggedright\sloppy
    \noindent\hrulefill\par\nobreak\vspace{0.3ex}%
    \noindent\textbf{NOT TYPESET.}\enspace\ignorespaces}%
   {\par\vspace{0.3ex}\noindent\hrulefill\par\addvspace{0.4\baselineskip}}
\fi
""".strip("\n")


def render_layer_file(key, title, ids, defs, ctx):
    parts = [GEN_WARNING, f"% Layer file: {title}",
             r"\subsection*{" + title + "}", ""]
    for did in ids:
        parts.append(render_definition(did, defs[did], ctx))
        parts.append("")
    return "\n".join(parts).rstrip("\n") + "\n"


def render_out_of_scope(dropped):
    """The honest closing paragraph of the section (directive 2)."""
    if not dropped:
        return ["% every canonical definition is inside the current proof strategy's closure",
                r"\par\addvspace{0.8\baselineskip}\noindent",
                r"Every canonical definition in \texttt{definitions/} lies inside the current "
                r"proof strategy's dependency closure; none is withheld.", ""]
    n = len(dropped)
    noun = "definitions" if n != 1 else "definition"
    verb = "are" if n != 1 else "is"
    they = "They remain" if n != 1 else "It remains"
    ids = ", ".join(r"\texttt{" + tt(d) + "}" for d in dropped)
    return ["% out-of-scope definitions (directive: render only what the strategy needs)",
            r"\par\addvspace{0.8\baselineskip}\noindent",
            f"{n} further canonical {noun} in \\texttt{{definitions/}} {verb} outside the "
            f"current proof strategy's dependency closure and {verb} not rendered here. "
            + f"{they} canonical --- the shard is the single source of truth either way --- and "
              r"reachable at the shard path and through \texttt{definitions/INDEX.md}:",
            r"{\footnotesize\par\smallskip\noindent " + ids + r"\par}", ""]


def render_all_file(order_by_layer, dropped):
    parts = [GEN_WARNING, MACROS, ""]
    for key, title in LAYERS:
        if not order_by_layer.get(key):
            continue
        parts.append(f"% {title}")
        parts.append(r"\input{generated/defs/" + LAYER_FILE[key][:-4] + "}")
        parts.append("")
    parts += render_out_of_scope(dropped)
    return "\n".join(parts).rstrip("\n") + "\n"


def render_manifest(order_by_layer, defs, ctx, dropped, scope):
    rows = ["<!-- GENERATED by scripts/gen-report-defs.py — do not hand-edit. -->",
            "# Generated report definitions — manifest",
            "",
            "Reading order, layer assignment and rendering status of every `definitions/*.md`",
            "shard projected into the report.  The shard is the single source of truth (CLAUDE.md",
            "L2); this table and the `.tex` files beside it are a deterministic projection of it.",
            "",
            "## Scope (directive: render only what the current proof strategy needs)",
            "",
            f"- selection rule: **{scope['mode']}**",
            f"- registry results in the strategy subgraph: **{scope['subgraph']}**; "
            f"registry results anchored in `report/sections/`: **{scope['anchored']}**",
            f"- definitions they import directly: **{scope['seed']}**; after the statement-region",
            f"  `[[def-…]]` closure: **{len(defs)}** rendered, **{len(dropped)}** dropped",
            ""]
    if dropped:
        rows += ["Dropped (outside the closure; canonical, just not reproduced here):", ""]
        rows += [f"- `{d}`" for d in dropped]
        rows.append("")
    n = 0
    for key, title in LAYERS:
        ids = order_by_layer.get(key, [])
        if not ids:
            continue
        rows += [f"## {title}", "",
                 "| # | id | label | kind | status | statement | source check | source | locus | sha256 | registry uses | in report |",
                 "|---|---|---|---|---|---|---|---|---|---|---|---|"]
        for did in ids:
            n += 1
            fm = defs[did]["fm"]
            info = ctx["info"][did]
            users = ctx["users"].get(did, [])
            anchored = [u for u in users if u in ctx["anchor"]]
            rows.append("| {} | `{}` | `{}` | {} | {} | {} | {} | `{}` | `{}` | `{}` | {} | {} |".format(
                n, did, label_of(did), fm.get("kind", "?"), fm.get("status", "?"),
                {"shard": "shard statement",
                 "translated": f"translated (table v{TRANSLATION_TABLE_VERSION})",
                 "empty": "**MISSING**"}.get(info["origin"], info["origin"]),
                len(info["source_blocks"]) or "—",
                fm.get("source", "?"), fm.get("locus", "").replace("|", "\\|"),
                fm.get("sha256", "-"), len(users), len(anchored)))
        rows.append("")

    rows += ["## Macro-translation table v%d" % TRANSLATION_TABLE_VERSION, "",
             "Every mapping in THIS table is the expansion the pinned source itself gives the macro",
             "(`refs/kitaev-2405.02434/approximate_algebras.tex`, sha256 prefix `e7eb512a2ec2438d`);",
             "the source line that defines it is quoted.  Translation changes spelling, never meaning.",
             "",
             "| source macro | rendered as | source line | the source's own definition |",
             "|---|---|---|---|"]
    for name, repl, line, srcdef in sorted(MACRO_TABLE_0, key=lambda r: r[0].lower()):
        if line <= 0:
            continue  # kernel normalizations: separate section below (hostile audit 2026-07-26)
        rows.append("| `\\{}` | `{}` | {} | `{}` |".format(name, repl, line, srcdef))
    for name, nargs, template, line, srcdef in sorted(MACRO_TABLE_N, key=lambda r: r[0].lower()):
        shown = template.replace("%s", "#1", 1).replace("%s", "#2", 1)
        rows.append("| `\\{}` ({} arg{}) | `{}` | {} | `{}` |".format(
            name, nargs, "s" if nargs != 1 else "", shown, line, srcdef))
    kern = [(n, r, d) for n, r, l, d in MACRO_TABLE_0 if l <= 0]
    if kern:
        rows += ["", "### Kernel normalization (NOT source-defined; claim limited to math-mode glyph equivalence)", ""]
        for n, r, d in sorted(kern):
            rows.append("- `\\{}` -> `{}` --- {}".format(n, r, d))
    rows += ["", "Structural rewrites: `\\label{…}` dropped; `\\ref{k}`/`\\eqref{k}` shown as the",
             "source's own key in brackets (never a live `\\ref`, which would dangle); display",
             "environments starred (labels are stripped, so a number would be un-referenceable);",
             "source theorem-environment delimiters dropped, opening and closing independently.",
             "Declared glyph-only deviations:", ""]
    for what, why in DEVIATIONS:
        rows.append(f"- `{what}` — {why}")
    rows += ["", "Held back in project-written prose math (report/main.tex defines these itself,",
             "with different, argument-taking meanings): "
             + ", ".join("`\\" + n + "`" for n in sorted(ctx["held_back"])) + ".", ""]

    flags = {k: v["flags"] for k, v in ctx["info"].items() if v["flags"]}
    rows += ["## Flags", ""]
    if not flags:
        rows += ["None: every rendered definition has a fully typeset statement.", ""]
    else:
        rows += ["Anything the generator would not typeset is flagged LOUDLY on the page as well",
                 "as here.  One bullet per affected shard:", ""]
        for did in sorted(flags):
            for reason in flags[did]:
                rows.append(f"- `{did}` — {reason}")
        rows.append("")
    return "\n".join(rows)


# ---------------------------------------------------------------- driver

def _dag_anchor_ids(ctx):
    """ids that actually carry a \\hypertarget{dag:<id>} in the generated DAG atlas.
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
    all_defs = load_definitions(root)
    registry = load_registry(root)
    texlabels = load_report_labels(root)
    all_edges = build_edges(all_defs)

    keep, dropped, scope = strategy_scope(root, all_defs, all_edges)
    defs = {k: v for k, v in all_defs.items() if k in keep}
    edges = {k: [d for d in v if d in keep] for k, v in all_edges.items() if k in keep}
    layers = assign_layers(defs, edges)

    users = {did: [] for did in all_defs}
    for rid in sorted(registry):
        for tok in re.split(r"[;,\s]+", registry[rid].get("defs", "")):
            if tok in users:
                users[tok].append(rid)
    anchor = {}
    for rid, fm in registry.items():
        lab = report_label_of(fm, texlabels)
        if lab:
            anchor[rid] = lab

    main_macros = load_main_macros(root)
    table_names = {r[0] for r in MACRO_TABLE_0} | {r[0] for r in MACRO_TABLE_N}
    ctx = {"defs": all_defs, "rendered": set(defs), "registry": registry, "users": users,
           "anchor": anchor, "macros": BASE_MACROS | main_macros, "root": pathlib.Path(root),
           "held_back": table_names & main_macros, "dag_anchors": dag_anchors,
           "info": {}, "fired": set()}

    order_by_layer = {}
    for key, _title in LAYERS:
        ids = [d for d in sorted(defs) if layers[d] == key]
        order_by_layer[key] = order_layer(ids, edges)

    files = {}
    for key, title in LAYERS:
        ids = order_by_layer.get(key, [])
        if ids:
            files[LAYER_FILE[key]] = render_layer_file(key, title, ids, defs, ctx)
    files["_all.tex"] = render_all_file(order_by_layer, dropped)
    files["MANIFEST.md"] = render_manifest(order_by_layer, defs, ctx, dropped, scope)
    return files, ctx, dropped, scope


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
    ap.add_argument("--scope-report", action="store_true",
                    help="print the scope ledger and the per-definition statement origin; write nothing")
    args = ap.parse_args(argv)

    root = pathlib.Path(args.root).resolve()
    out = pathlib.Path(args.out) if args.out else root / DEFAULT_OUT
    files, ctx, dropped, scope = build(root, dag_anchors=args.dag_anchors)

    flags = sorted((did, r) for did, v in ctx["info"].items() for r in v["flags"])
    nrender = len(ctx["info"])
    ntotal = sum(1 for _ in (root / DEF_DIR_NAME).glob("def-*.md"))
    ntrans = sum(1 for v in ctx["info"].values() if v["origin"] == "translated")

    if args.scope_report:
        print(f"scope rule: {scope['mode']}")
        print(f"  strategy subgraph results : {scope['subgraph']}")
        print(f"  report-anchored results   : {scope['anchored']}")
        print(f"  definitions rendered      : {nrender} of {ntotal}")
        print(f"  definitions dropped       : {len(dropped)} ({', '.join(dropped) or '-'})")
        for did in sorted(ctx["info"]):
            v = ctx["info"][did]
            print(f"    {did:42s} {v['origin']:11s} "
                  f"source-blocks={len(v['source_blocks'])} flags={len(v['flags'])}")
        return 0

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
        print(f"gen-report-defs --check: OK ({nrender} of {ntotal} definitions in the strategy "
              f"scope, {ntrans} typeset via translation table v{TRANSLATION_TABLE_VERSION}, "
              f"{len(files)} generated files, {len(flags)} flag(s))")
        return 0

    out.mkdir(parents=True, exist_ok=True)
    for name, text in sorted(files.items()):
        (out / name).write_text(text, encoding="utf-8")
    for path in sorted(out.iterdir()):
        if path.is_file() and path.name not in files:
            print(f"gen-report-defs: NOTE stale file left in place: {path}", file=sys.stderr)
    print(f"gen-report-defs: wrote {len(files)} file(s) to {out} "
          f"({nrender} of {ntotal} definitions rendered, {len(dropped)} out of scope, "
          f"{ntrans} typeset via translation table v{TRANSLATION_TABLE_VERSION})")
    for did, reason in flags:
        print(f"  flag: {did} — {reason}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
