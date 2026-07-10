# W63 creative wave — DECOMPOSE the I horn (isotropic co-top web exclusion)

You are a fresh, independent proof strategist-prover. Your workspace is this
directory: the full registry snapshot (`argument/`, `definitions/`) + context docs
(`context/`). Everything you produce stays INSIDE this directory. Deliverable:
`DECOMPOSITION-I.md`. Status discipline (L0): every node you propose is
`conjecture`/proposed until proved elsewhere; you promote nothing here. If you can
fully prove a routine node inline, write the proof in an appendix and STILL tag the
node proposed — a separate hostile verifier decides.

## THE OBJECTIVE FUNCTION (user mandate, binding)

**Decomposition into lower-complexity pieces.** Success is NOT "prove I in one
shot". Success is a tree in which:
- routine nodes are near-mechanical consequences of the banked proved/T0 interface;
- each remaining creative node retains a PROPER quantitative subclass of I's
  hypothesis class, or outputs a constant-complexity package (one scalar, one
  constructed pair, one measure statistic) — strictly less than all of I;
- the assembly implication (your nodes ⟹ I) is written with quantifiers threaded
  explicitly.
Legitimate decomposition instruments: case analysis on structure (with the case
predicate stated as a clone-invariant inequality whose boundary is owned by a named
node); probabilistic/averaging arguments IF they respect the walls below (no witness
averaging, no Jensen promotion of atom separation to barycenter separation);
extraction of quantitative sub-lemmas whose conjunction implies I; weakening I to a
tallness-threshold version (H > K*tau for larger K, or an H/tau-dependent gamma_I)
if that is what a clean mechanism actually delivers — SAY SO honestly and record the
exact statement lost. The W56 one-hard-leaf wall is certified dead: do NOT funnel
everything into one residual restatement of I.

## Target — node I, verbatim pinned contract

`conj-w62-isotropic-cotop-web-exclusion` (context/DECOMPOSITION-W62-L5.md §1,
node I; read that file FIRST and adopt ALL its shared notation: L5 datum, fibers Q,
m_Q, S, q_A, G_v, Sh_v, E_c, K_v^loc, omega, r_omega, scalar width Omega(omega),
Z_v, Y_v, D_0 = 2+4*delta, tau = sqrt(delta)):

> There are universal gamma_I > 0 and delta_I in (0,1/4] with the following
> property. Let (P,v,A) be an L5 datum with 0 < delta <= delta_I and S >= c_m, put
> omega_Q := P_v^+({Q}) 1_{G_v}(Q), and suppose that for every c in K_v^loc,
>
>   P_v^+(E_c ∩ Sh_v) < (1/16) tau S,   P_v^+(E_c ∩ G_v) >= (1/16) tau S,
>
> while ||r_omega - p_v||_1 < 1/8 and Omega(omega) < 1/16. Then
> Z_v(q_A) >= gamma_I * tau.

I owns strict low drift and strict low width; sibling C owns both equality
boundaries. The for-all-centers hypothesis precedes the ONE existential output y
(via Z_v); no y_c may be selected or averaged.

## The proved interface you must consume (all in `argument/`)

Proved at L5 (W62 routine batch — proofs in context/PROOFS-W62-L5-BATCH.md):
- `lem-l5-mass-barycenter-dualization` (R0): the minimax equals S*Z_v(q_A).
- `lem-l5-top-face-ray-formula` (R1): Z_v(q) = min_{Lambda>=0, c in C_W}
  (||p_v - q + Lambda(p_v - c)||_1 - Lambda*H), attained. Failure of I's conclusion
  hands you ONE outward ray certificate (Lambda_0, c_0) for q_A with value < gamma_I*tau.
- `lem-l5-positive-flow-foldback` (R2): top-owned one-step positive flow allocation,
  error 2*delta*(1+delta)*M.
- `lem-l5-universal-exterior-payer` (R3): P_v^+(E_c) >= tau*S/8 for EVERY c in K(P),
  below the ceiling delta_E = min(1/16,(c_m/8)^2).

af-validated (T0) engine bank and geometry (consumable as rigorous):
- `lem-hx-transverse-moment-identity`, `lem-hx-signed-variation-ledger`,
  `lem-hx-financing-floor` (CORRECTED A > 0 form — read the shard, not W60 memory),
  `lem-hx-forced-exterior-coupling`, `lem-hx-robust-scalar-starvation`.
- `lem-top-support-dual-face`, `lem-top-deficit-price` (the moment cap
  ∫ z_y d omega <= delta*D_0 for every y in Y_v — an UPPER budget only),
  `lem-hiddenness-dual-witness`, `lem-always-tight-dual-support`,
  `lem-positive-exposedness-margin`, `lem-optimal-face-conic-reduction`,
  `lem-cotop-witness-pinning`, `obs-height-collapse`, `lem-halo-collapse`.

The two exact tallness inequalities (the ONLY tallness budgets you may use):

    H(1 - sigma_v) <= nu_v * D_0,
    H(1 - sigma_g) <= (sigma_v - sigma_g) * tau/4 + nu_v * D_0.

Tallness context: H > 16*tau has been the binding wall in THREE consecutive
independent refuter searches (context/2026-07-10-W61-deciders-and-elevation.md and
context/i-horn-refuter/). A winning mechanism plausibly must consume H > 16*tau
quantitatively; a node that never uses tallness should say why it can afford not to.

## Adverse-calibration fixtures (context/i-horn-refuter/)

The exact-rational refuter batch (README, REPORT, certificates.json, search.py):
heavy summit-axis spike, growing low-width dual-simplex fan, tall completions of the
W61 graft/financer and W55 A0=5 plateau — all BLOCKED, each at a named gate
(tallness thrice; the width gate Omega < 1/16 independently repels the fan, which
has exact width -> 3/4). Every node you propose must be checked against these
shapes: state per fixture which hypothesis excludes it or which node handles it.
The likeliest death of I (from the W62 tree): an exact high-dimensional
sign-cube/dual-simplex plateau whose mean stays near p_v, scalar width < 1/16, and
the same web pays every exterior demand. Your decomposition should isolate exactly
where such a plateau would have to fight tallness.

## Hard constraints (node I interface discipline + walls)

- Signed picture only; clone-invariant (full-fiber) quantities only; frame-free.
- No 1/t*(v) in any constant; `lem-positive-exposedness-margin` legalizes small-beta
  geography only.
- The reduced co-top witness (`lem-cotop-witness-pinning`) is geography only — never
  identified with P_v^+ (coefficient overlap is NOT implied; lambda*P != p_v).
- FORBIDDEN: invoking `lem-hx-financing-floor` on the pair (p_v, r_omega) after
  letting the separation vanish (I's hypothesis makes it vanish); reversing the W37
  dual inequality (never turn an upper exposedness bound into a lower one); witness
  averaging / averaging y_c's (W54); Jensen; raw-index path products (cloning);
  exists-exact-max-volume selectors / favorable-ray-minimizer selection (R1 gives an
  attained certificate with NO tie structure); coefficient-only LP cleanup;
  summing pairwise engine demands without an R2 foldback (kill-list item 3).
- context/FINDINGS.md dead routes are ABSOLUTE. Audit every node against them.

## Deliverable format — `DECOMPOSITION-I.md` (the format that worked three times)

0. **Binding-gap verdict** (<= 1 page): name the true hard core of I. Candidates to
   adjudicate honestly: (i) a whole-measure transport dual (integrate the unit
   transverse moments of the pairs (p_v, p_Q) against omega-bar, combine sign unions
   via the signed-variation ledger + R2 + tallness — the W62 sketch's proposal);
   (ii) a completion obstruction (an internally reproducing low-width web cannot be
   exactly idempotent AND tall — compare `lem-starvation-completion-obstruction`);
   (iii) a second-moment / width-amplification mechanism (low width + uniform
   exterior floor forces a contradiction with the R3 payer geometry); (iv) something
   better. Defend against the W62 §I(b) sketch.
1. **The tree**: per node — (a) pinned contract (SINGLE minimal statement, signed
   picture, clone-invariant; af-elevation-shaped: no 'hence' clauses); (b) mechanism
   sketch naming exact banked tools; (c) honest price (difficulty, likeliest death,
   evidence both ways); (d) interface check (quantifier order, no selectors, which
   strict/equality boundaries the node owns); (e) fallback.
2. **The assembly implication**: your nodes ⟹ I, quantifiers explicit, constants
   threaded (gamma_I as an explicit min/combination of node constants).
3. **Kill-list check**: PASS/FAIL per node against every named wall above + the
   FINDINGS dead routes; one line of why each.
4. **Recommended dispatch order**: routine batch first; cheap L3 decider shapes
   (concrete refuter families with exact target inequalities) before creative spend;
   creative nodes last, highest-information first.

Do not touch `argument/` or `definitions/`. Write ONLY `DECOMPOSITION-I.md` (and an
optional `APPENDIX-I-proofs.md` for inline routine proofs).
