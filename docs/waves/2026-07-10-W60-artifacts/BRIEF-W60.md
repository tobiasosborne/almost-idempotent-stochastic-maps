# W60 STRATEGY BRIEF — decompose the H-X gap (T0 anchor -> conj-sl1a-off-diagonal-cell)

You are a proof STRATEGIST on an OPEN problem in the geometry of almost-idempotent
stochastic/signed matrices. Your output is a strategy sketch: it PROMOTES NOTHING and
must not claim any proof. You work only inside this workspace directory.

## The situation

- **Goal of the campaign (context/2026-07-10-top-down-proof-sketch-v23.md + v24):**
  prove `op-classical` (universal-constant sqrt(eta) stability of row-stochastic
  almost-idempotents). The live reduction is: op-classical <= op-exposed-hull <= HLC
  <= Kernel/(EX), and the Kernel route runs through the three-cell SL1a surface.
- **Tier-1 target of THIS wave:** `argument/conj-sl1a-off-diagonal-cell.md` (the H-X
  cell): a universal delta_X such that no selected-corner configuration
  (definitions/def-selected-corner.md) with delta(P) <= delta_X has a radial block
  B in {B_F, B_N} with Gamma_f(B) >= 1/4 and off-diagonal freight > 1/8.
- **The T0 anchor (af-validated, the ONLY rigorous mechanism on this front):**
  `argument/lem-starvation-completion-obstruction.md`, full proof in
  `context/PAPER-PROOF-w59.md`. One-line mechanism: exact idempotence at the pinned
  W55 display demands one unit of transverse moment (sum_j x_j*D_j = 1) while the
  actor hull plus the aggregated exterior sign-union row budgets supply only O(tau).
  K-free (any finite number of exterior zero-top slab-confined support fibers), at
  rank 3, tau <= 1/256.

## The four named gaps (verbatim scope limits, §HONEST LIMITS of PAPER-PROOF-w59.md)

1. **Rank > 3.** An exterior row can then have further transverse components, so the
   moment identity acquires extra terms that may cancel X_Q*D; neither the lever
   bound nor the two-coordinate moment close follows.
2. **Slab confinement.** `0 <= Y_Q <= 1` is used to make the p_v,p_o combination
   convex; an uncontrolled Y_Q introduces an uncontrolled lever.
3. **Fiberwise zero-top exterior support (c_Q = 0).** If an exterior support fiber
   has c_Q != 0, the three key identities acquire a top term and the sign-union
   budget no longer follows.
4. **The pinned tableau.** The exact pin ||p_z - p_v||_1 = tau, A in [4,6], and the
   coefficient display (c_v = 1-tau, c_w = tau+t, c_f = -t) drive the close; the
   upstream geometric reduction from a selected-corner datum to SOME such tableau is
   not established.

## YOUR OBJECTIVE FUNCTION (user directive, binding): DECOMPOSITION

Do NOT attempt to prove H-X in one shot. The deliverable is a DECOMPOSITION of the
T0->H-X gap into lower-complexity pieces. Admissible decomposition modes:

- **Task decomposition** — separate lemmas per gap, each isolating ONE mechanism
  (mechanism separation is mandated; the W56 wall certified that
  one-hard-leaf-after-free-preprocessing is DEAD — do not funnel everything into a
  single residual hard lemma).
- **Case-splitting** — e.g. by effective rank of the freight, by slab-escape mass, by
  near/far radial cell, by whether exterior top mass is above/below a threshold; each
  case its own small lemma, plus a small exhaustiveness lemma.
- **Probabilistic / averaging method** — e.g. an averaged or randomized choice of
  exposer h, vertex kernel xi, coordinate pair (D,E), or top functional phi, showing
  SOME choice lands in a tractable case; the existence statement is then a separate
  small lemma.
- **Multi-lemma assembly** — several small statements whose CONJUNCTION, via an
  explicit assembly implication you verify at the statement level, implies H-X or an
  explicitly named weakening that still feeds SL1a (if a weakening: state exactly
  what remains).

## Requirements for EVERY proposed node

(a) **Pinned contract** — ONE minimal mathematical sentence, registry style
    (no "hence" clauses, no compound corollaries; quantifiers explicit; universal
    constants named; states which picture — signed or stochastic).
(b) **Mechanism sketch** — why it is plausibly true AND provable at low complexity;
    name the proof tool (Farkas/LP duality, convexity, budget/ledger, averaging,
    compactness-free counting, etc.).
(c) **Honest price** — difficulty tier (routine / hard / creative-hard), the single
    most likely way it dies, and what evidence exists (cite registry ids or runs).
(d) **Interface check** — exact statement-level verification that the assembly
    implication holds: quantifier hygiene, clone-invariance (ONLY clone-invariant /
    quotient quantities are admissible — index-level path products are DEAD, see
    context/FINDINGS.md), no frame-specific -> frame-free leaps.
(e) **Fallback** — what replaces the node if it dies, or what weaker target survives.

## Hard constraints

- **context/FINDINGS.md dead routes are ABSOLUTE.** Read that file FIRST. If any node
  resembles a dead route, kill it yourself and say so in the kill-list.
- Only clone-invariant (quotient) quantities in any contract.
- Say per contract which picture (signed delta / stochastic eta) it lives in.
- The registry DAG must stay acyclic; name each node's intended `deps`.
- Statuses: every proposed node is `conjecture` until proved. Nothing you write
  promotes anything.

## DELIVERABLE

Write `DECOMPOSITION-W60.md` in the workspace root with sections:

0. **Binding-gap verdict** — which of the four gaps is THE binding one (the one whose
   resolution most reduces unscoped surface), with a one-paragraph argument.
1. **The tree** — <= 7 nodes, each with (a)-(e) above; a Mermaid or indented sketch of
   the implication structure.
2. **The assembly implication** — spelled out in full: the exact chain from the
   conjunction of your nodes (+ the T0 anchor + existing registry results, cited by
   id) to conj-sl1a-off-diagonal-cell (or the named weakening).
3. **Kill-list check** — node-by-node against FINDINGS dead routes and the W56 wall.
4. **Recommended dispatch order** — which node first and why; which are batchable
   routine vs creative.

Think OUTSIDE THE BOX (creativity mandate): the pinned-tableau gap in particular may
admit a reduction nobody has tried — e.g. a normalization/compactness-free extremal
argument selecting the tableau, an averaged tableau family, or a case-split making
the tableau pin unnecessary. Surprise us — but every node must still satisfy (a)-(e).
