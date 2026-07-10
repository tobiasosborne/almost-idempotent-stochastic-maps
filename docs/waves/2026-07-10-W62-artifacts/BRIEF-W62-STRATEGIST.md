# W62 strategist — decompose L5-GAP-1 (the dual-face mass minimax) into lower-complexity pieces

You are a fresh, independent proof STRATEGIST. Your workspace is this directory: the
full registry snapshot (`argument/`, `definitions/`) + context docs (`context/`).
Everything you produce stays INSIDE this directory. Deliverable: `DECOMPOSITION.md`.
This is a STRATEGY artifact (status discipline L0): every proposed node is
`conjecture`/proposed until proved; you promote nothing and prove nothing here.

## Target

**L5-GAP-1 (bd aism-vuc), the dual-face mass minimax.** Setting (signed picture;
delta = delta(P), tau = sqrt(delta)): P an exact signed idempotent, visible set W
nonempty with hull C_W, hidden top vertex v of height H > 16*tau, d_j =
dist_1(p_j, C_W), w_j = max(P_vj, 0). For every

    A subset { j : ||p_j - p_v||_1 >= 4*tau, d_j > H - 8*tau }  with  S_A = sum_A w_j >= c_m,

prove there exist universal c_5, delta_0 > 0 such that for delta <= delta_0 some top
support functional phi at v has

    sum_{j in A} w_j * (H - phi(p_j)) >= c_5 * tau * c_m.

Read `context/l5-answer.md` FIRST and take its reduction as your anchor: by
`lem-top-support-dual-face` the statement is a LINEAR minimax over the top dual face
Y_v = { y : ||y||_inf <= 1, y.p_v - h_C(y) = H } (phi_y(x) = y.x - h_C(y)); the
mass-weighted target follows from a universal-size extreme-cover of Y_v (the
artifact's CONDITIONAL COVER LEMMA, already proved there: N functionals covering all
far-deep deficits at level eta*tau give c_5 = eta/N). The W54 verdict was BLOCKED
exactly on: no proved shard supplies a dimension-free mass-minimax / finite-cover
input. The POINTWISE form is `conj-summit-cylinder-exclusion`; it does NOT imply the
mass form by averaging — the SIMPLEX OBSTRUCTION (see the W54 docs and FINDINGS) kills
naive averaging.

## Why this is newly attackable (read these)

The W61-validated engine bank (all af-validated, T0, consumable as rigorous):
- `lem-hx-financing-floor` (A > 0 corrected form) + `lem-hx-forced-exterior-coupling`:
  two rows/row-hull points at l1-separation l must jointly finance ~ l/(2+4delta)
  positive mass OUTSIDE every ball — the first forced LOWER bound on far positive
  financing. A is rho-far from v (||p_j - p_v||_1 >= 4*tau) with positive v-mass: the
  engine speaks directly to the (v, p_j) geometry.
- `lem-hx-transverse-moment-identity` + `lem-hx-signed-variation-ledger`: basis-free
  unit moment + sign-union budget converter (rank-free, slab-free).
- Also banked and relevant: `lem-top-support-dual-face`, `lem-cotop-witness-pinning`,
  `lem-top-deficit-price`, `lem-hiddenness-dual-witness`, `lem-always-tight-dual-support`,
  `obs-height-collapse`, `lem-halo-collapse` (af-validated), the W61 tallness signal
  (context/2026-07-10-W61-deciders-and-elevation.md: in both W61 refuter searches
  TALLNESS H > 16*tau was the binding wall — L5's hypothesis class LIVES in the tall
  regime; a winning mechanism plausibly must consume tallness quantitatively).

## Your job

Produce `DECOMPOSITION.md` in the W60 format (see the sketch's description of the
route-fork trees; the format that worked twice):

0. **Binding-gap verdict** — name what you judge the true hard core of L5-GAP-1
   (finite cover of Y_v? a one-functional construction? a mass-transport dual? an
   engine-demand pairing?) and defend it in <= 1 page against the l5-answer analysis.
1. **The tree** — decompose into the smallest set of nodes such that (a) routine
   nodes are near-mechanical consequences of banked T0/proved shards, (b) each
   creative-hard node retains a PROPER quantitative subclass or outputs a
   constant-complexity package (the W56 one-hard-leaf wall is certified dead — do
   not funnel everything into one residual restatement), (c) every node gets:
   (a) pinned contract (single minimal mathematical statement, signed picture,
   clone-invariant quantities only), (b) mechanism sketch naming the exact banked
   tools consumed, (c) honest price (difficulty + likeliest death + evidence both
   ways), (d) interface check (quantifier order, no selectors unless constructed,
   no frame-specific step), (e) fallback.
2. **The assembly implication** — the exact statement-level chain from your nodes to
   L5-GAP-1, quantifiers threaded explicitly; name what each sibling owns.
3. **Kill-list check** — audit every node against `context/FINDINGS.md` dead routes
   and walls (raw-index path products/cloning; the simplex averaging obstruction;
   W53 affine-pairing blind spot; W54 witness-averaging and t*-free discipline; W37
   dual-direction wall; exists-exact-max-volume selectors; Jensen; coefficient-only
   LP cleanup; the W56 one-hard-leaf wall). State PASS/FAIL per node with one line
   of why.
4. **Recommended dispatch order** — routine batch first (af-elevation-shaped single
   minimal contracts), cheap L3 deciders before creative spend (name concrete
   refuter shapes!), creative nodes last with the highest-information one first.

## Constraints and discipline

- SIGNED picture throughout; no stochastic crossing (that goes through
  lem-classical-equiv only, and you should not need it).
- All quantities clone-invariant (full row-point fibers, affine functionals on row
  points, l1 distances); the cloning obstruction cuts both ways.
- Do NOT re-walk FINDINGS dead routes; if a node smells like one, kill it yourself
  and say so.
- Bonus (only if it genuinely falls out): note whether your nodes also serve
  `conj-summit-cylinder-exclusion` (the pointwise sibling) or the L6.5
  `conj-cotop-web-coupling` demand side — L5 is double-valued (it is also the
  unregistered premise of the huddle assembly bridge, bd aism-pus), so interfaces
  that pay twice are worth a sentence.
- Work entirely inside this directory. Final answer: your §0 binding-gap verdict +
  the node list with difficulty tags, <= 1 paragraph.
