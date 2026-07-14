# W68 hostile verifier — the assembly-bridge repair (3 parts)

You are a fresh, independent HOSTILE verifier. You wrote NEITHER the original
bridge nor REPAIR-W68-bridge.md. Your job is to BREAK the repair. Finding a
counterexample, a gap, a wrong constant, a quantifier error, an illegal shard
consumption, or a DAG-semantics error is a BIG SUCCESS. Do NOT be charitable;
do NOT repair silently.

Workspace: registry snapshot (argument/, definitions/), context docs
(context/ — the original INVALID verdict is context/verdict-bridges.md §2 and
its repair recipe is your specification baseline; the source prose is
context/l2-attack.md §§2.6-2.7), and the object under attack,
REPAIR-W68-bridge.md (Parts 1-3).

TARGETS, in order:
  P1 conj-l5-gap-1                       (registration fidelity, no proof)
  P2 lem-intersection-branch-production  (statement + proof)
  P3 lem-huddle-charge-assembly repaired (contract + conditional proof)

MANDATORY HOSTILE CHECKS:
1. P1 fidelity: the contract must be verbatim-equivalent to BOTH the
   verdict-bridges.md repair item 2 AND the W62 pinned statement
   (context/BRIEF-W62-STRATEGIST.md; context/DECOMPOSITION-W62-L5.md).
   Quantifier order (c_5 before c_m? the verdict says "universal c_5 > 0
   and, for every fixed universal c_m > 0, a universal delta_5 > 0" — does
   P1 preserve exactly this order, and is it the order the W62 tree
   attacks?). ALSO RULE on P1's frontmatter deps
   (lem-l5-mass-barycenter-dualization etc.): in this registry, deps =
   imports the result CONSUMES. A conjecture statement consumes nothing it
   doesn't mention. Are these deps semantically legal DAG edges or should
   the shard have no deps (with the reduction-tree relation recorded in the
   body only)? Check how existing conj-* shards handle deps
   (conj-straddling-web-exclusion, conj-cotop-web-coupling, the
   conj-sl1a-* cells) and rule for consistency with the linker's semantics.
2. P2 hypothesis honesty — THE decisive check: open
   lem-intersection-witness-confinement and quote its FULL contract. The
   prover claims it contracts only B1-B4 and that the co-top mass clause
   ("B5" in l2-attack prose) is NOT contractual, and instead consumes proved
   lem-top-witness-third-actor for the co-top mass. Open
   lem-top-witness-third-actor: does its hypothesis block match what B1
   supplies (the small-beta witness), and does its conclusion supply the
   mass > 13/16 at depth > H - 4*tau (or whatever P2 actually needs — the
   mu < 3/16 bound)? Any mismatch of constants (13/16 vs 3/16 vs
   (1/2+delta)/4), depth thresholds (H - 4*tau), or witness normalizations
   is a potential INVALID. Also check lem-optimal-face-conic-reduction and
   lem-always-tight-dual-support consumption (does the intersection
   configuration guarantee the display P2 uses, with t*(v) in (0,kappa)
   as P2's hypothesis states — and is the L2-core configuration quoted
   VERBATIM from lem-l2-core-collapse?).
3. P2 arithmetic: the case split at mu vs tau/D (D = 2+4*delta), equality
   ownership consistent with the SL1b mass clause (>= tau/(2+4*delta) — does
   the case-(ii) output meet the WEAK inequality if mu = tau/D is owned by
   (ii), or is ownership assigned to (i)? exact match required); the
   barycenter chain ||beta_L|| <= (||beta|| + mu*||beta_S||)/(1-mu) — check
   the direction of this inequality derivation and each numeric step:
   (1/2+delta)*tau + (tau/D)*D = (3/2+delta)*tau, divided by (1-mu) with
   mu <= 3/16 gives factor 16/13; (16/13)*(3/2+delta) <= 28/13 < 2.2 at
   delta <= 1/4; the exposer average (16/13)*kappa; ||beta_S|| <= D (is the
   S-side barycenter really within D of p_v? rows are within diameter
   D = 2+4*delta of each other — check the exact bound used); h >= 0 on rows
   (is admissibility of exposers actually nonnegativity on rows? open the
   def shard).
4. P3 contract: explicitly conditional (all four conjectures as named
   premises with ceilings), delta_0 = min{...} list complete and each entry
   actually used in the proof; the conclusion's near-cluster set and the
   7/8 threshold exactly as in the original bridge / verdict; the
   (c_5*c_*/6)^2 (or the prover's corrected exponent) recomputed from the
   two branch inequalities (L5 charge >= c_5*(c_*/2)*tau vs
   lem-top-deficit-price <= delta*(2+4*delta) <= 3*tau^2 at delta <= 1/4:
   the contradiction needs 3*tau^2 < c_5*(c_*/2)*tau i.e.
   tau < c_5*c_*/6, i.e. delta < (c_5*c_*/6)^2 — verify the prover threads
   exactly this).
5. P3 branch (I): is t*(v) > 0 legally derived (hidden top => far set
   nonempty => lem-positive-exposedness-margin)? Open
   lem-positive-exposedness-margin and lem-hiddenness-dual-witness — do
   their hypothesis blocks hold at the bridge's hypotheses? Is t*(v) < kappa
   needed by P2's hypothesis, and if so where does the bridge get it? (This
   was a known soft spot — if the bridge cannot supply t* in (0,kappa), the
   intersection branch has a hole: rule explicitly.)
6. P3 branch (II): open conj-cotop-web-coupling — does its hypothesis block
   need the near-cluster mass >= 7/8 hypothesis ("heavy"), tallness, and
   disjointness exactly as threaded? Does its conclusion give S_A >= c_* on
   exactly the A that conj-l5-gap-1 consumes (d_j > H - 8*tau — depth
   threshold match!)? Open lem-top-deficit-price — is its bound stated for
   exactly the weighted far-deep sum used, for EVERY top support functional
   (the L5 phi included)?
7. Exhaustiveness of the two branches; boundary/degenerate ownership
   (empty T(v) or O(v); t*(v) = 0; hulls touching at a boundary point).
8. FINDINGS walls: no averaged-witness mechanism, no dead route resurrected.
9. Cross-consistency: P3's deps list vs what its proof actually consumes
   (lem-l2-core-collapse dropped — legal? the production route works at
   configuration level; confirm nothing implicit needs the equivalence);
   provenance/status fields sane; no 'hence' clauses in contracts.

DELIVERABLE: VERDICT-W68-bridge.md with one verdict line per part, EXACTLY:
    <P1|P2|P3> <shard-id>: VALID | VALID-WITH-CORRECTION | INVALID | UNDECIDED
then per-part findings (for corrections: the exact corrected text; for
INVALID: the irreparable gap with the failing line quoted), and a final
CROSS-CUTTING section (including the P1 deps-semantics ruling).

Write ONLY VERDICT-W68-bridge.md. You promote nothing.
