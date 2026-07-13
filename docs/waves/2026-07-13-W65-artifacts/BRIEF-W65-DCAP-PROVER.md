# W65 creative wave — ATTACK the D-cap leaf (disjoint-diagonal corner exclusion)

You are a fresh, independent proof strategist-prover. Your workspace is this
directory: the full registry snapshot (`argument/`, `definitions/`) + context
docs (`context/`). Everything you produce stays INSIDE this directory.
Deliverable: `DCAP-ATTACK.md` (+ optional `APPENDIX-dcap-proofs.md`). Status
discipline (L0): everything you produce is proposed/`conjecture` until verified
elsewhere; you promote nothing.

## THE OBJECTIVE FUNCTION (user mandate, binding)

**Decomposition into lower-complexity pieces.** A full proof of D-cap is welcome
but NOT the success criterion. Success is EITHER:
(a) a decomposition of D-cap into routine nodes (near-mechanical on the proved
    interface) + strictly smaller creative residual(s), each a PROPER subclass or
    a constant-complexity package (the W56 one-hard-leaf wall is dead — no
    funnelling into one residual restatement); OR
(b) a proof of a quantitatively weakened D-cap (larger tallness threshold
    H > K*tau, or gamma depending on H/tau, or extra slab/rank hypotheses
    STRICTLY WEAKER than those of lem-starvation-completion-obstruction) with
    the exact loss recorded; OR
(c) a precise reduction of D-cap to a NAMED, isolated completion problem whose
    statement is strictly smaller than D-cap and comes with its own refuter
    shape.

## Target — verbatim pinned contract (DECOMPOSITION-W63-I.md §1.3, node D-cap)

`conj-w63-I-disjoint-diagonal-corner-exclusion`. Read
context/DECOMPOSITION-W63-I.md §§0-1.1 FIRST and adopt ALL its notation (I-base
datum, b = c_m/128, k_b, delta_rt, theta, lambda_A, the selected-corner
certificate (phi, h, f, eta) and M_X/M_I/M_D from def-selected-corner):

> There are universal gamma_dis > 0 and delta_dis in (0, delta_rt] such that
> every I-base datum d with 0 < delta <= delta_dis, ||r_omega - p_v||_1 < b*tau,
> Omega(omega) < b*tau, theta < tau/D_0, for which there exists an exhibited
> selected-corner certificate C in P(d) with M_X(C) <= 1/8, M_I(C) < 1/16, and
> M_D(C) > 1/16, satisfies Z_v(q_A) >= gamma_dis * tau.

By `lem-ihorn-priced-ray-package` (PROVED), Z_v(q_A) <= delta*D_0/S on the
I-base class — so proving D-cap means proving the hypothesis class is EMPTY
below a ceiling: an exact, tall, ultra-isotropic, thin-rim idempotent carrying
a disjoint-diagonal corner certificate CANNOT EXIST. Argue from that emptiness
framing whenever it is cleaner.

## The proved interface (shards in `argument/`; consult each shard's OWN hypothesis block)

The W63 batch (10/10 hostile-verified): `lem-ihorn-priced-ray-package`,
`lem-ihorn-tall-halo-saturation` (T: 1 - sigma_g < (4*tau/63)*(D_0 + tau/4)),
`lem-ihorn-dual-cotop-geography` (V: witness mass > 13/16 in G_v),
`lem-ihorn-universal-exterior-package`, `lem-ihorn-drift-payer-extraction`,
`lem-ihorn-width-payer-extraction`, `lem-ihorn-ultra-compression`,
`lem-ihorn-rim-sl1b-package`, `lem-ihorn-cotop-sl1a-package`,
`lem-ihorn-selected-corner-extraction`.

The NEW W64 batch (8/8 hostile-verified, codified in corrected form):
`lem-icap-score-bulk-production`, `lem-icap-kernel-bulk-census` (the
arbitrary-kernel X/I/D bulk census: one cell >= 1/42),
`lem-icap-common-receiver-ownership`, `lem-icap-single-root-receiver-cap`,
`lem-icap-tallness-spend` (explicit T-spend: shallow mass < 2*tau/15),
`lem-icap-closed-diagonal-flow`, `lem-icap-type-i-structural-cost` (a singleton
far-tight family is impossible — exactly why the natural plateau had M_I = 0),
`lem-icap-priority-residual-split` (priority-guarded six-way split). CAUTION:
several are stated on the I-cap hypothesis class; consume each ONLY where its
own hypothesis block is satisfied on your class. Where a census/statistic is
kernel-arbitrary it transfers; where it assumes M_I >= 1/16 it does NOT.

Plus the W62 batch (`lem-l5-*`), the af-validated engine bank (`lem-hx-*`,
incl. the corrected A > 0 financing floor and
`lem-hx-robust-scalar-starvation`), the SL1a machinery
(`lem-sl1a-score-selector`, `lem-sl1a-corner-ledger`,
`lem-radial-horn-partition`), `lem-optimal-face-conic-reduction`,
`lem-always-tight-dual-support`, `lem-positive-exposedness-margin`,
`lem-zero-face-localization`, `lem-cotop-witness-pinning`,
`lem-top-deficit-price` (UPPER budget only), `obs-height-collapse`,
`lem-halo-collapse`, and — THE closest proved relative of what D-cap needs —
`lem-starvation-completion-obstruction` (the rank-3/bounded-slab completion
obstruction: idempotence demands one unit of transverse moment vs O(tau)
supply).

The two exact tallness budgets (the ONLY ones): H(1-sigma_v) <= nu_v*D_0 and
H(1-sigma_g) <= (sigma_v-sigma_g)*tau/4 + nu_v*D_0.

## What the tree already says about D-cap (engage with it, then go deeper)

DECOMPOSITION-W63-I.md node D-cap (b)-(e): disjoint always-tight hulls supply a
strict separator and a zero-face conic term through
`lem-always-tight-dual-support` and `lem-optimal-face-conic-reduction`;
`lem-positive-exposedness-margin` gives t*(u) > 0, and
`lem-zero-face-localization` places the zero-face rows 4*tau-near the carrier
u. Because the corner ledger gives d_u > H - 4*tau, the 1-Lipschitz depth
function places them in the H - 8*tau co-top band. This is GEOGRAPHY ONLY; V
independently supplies the original top's far co-top witness geography. Use the
t*-free separator/corner machinery and the validated
transverse-moment/robust-starvation bank to obstruct completion. A legal use of
`lem-hx-robust-scalar-starvation` must first construct its actual row fiber,
A >= 4, O(delta) residual, and fiber-aggregate tail cap. The final
incompatibility must also use T's exact saturation and E at the same receiver
center; conic geography alone is not a tallness argument.

The recorded fallback: let g_u = d_1(K_T(u), K_O(u)) and split the D-mass at
g_u = tau, equality assigned to the large-gap cell. Large gap forces a constant
zero-face conic package; small gap outputs one near-intersection pair. Neither
branch asserts conic recurrence. (ICAP-ATTACK-W64.md §§1-4 built the analogous
D_gap/D_near branches INSIDE the I-cap class, with decider targets
P_v^+{u in U_D : g_u >= tau} >= c_m/3072 and the strict small-gap complement —
engage with that machinery; a hypothesis-honest unified treatment of the two
D-sides is welcome, but never silently enlarge either class.)

## The prime creative objective (why D-cap is ranked first)

`lem-starvation-completion-obstruction` is strong positive evidence for exactly
this cell: it kills the completion for rank-3 supports inside the pinned
actor/slab class. Its rank and slab hypotheses are PRECISELY what D-cap must
remove. The strongest known positive mechanism is bounded-slab + robust
starvation. The likely death recorded in the tree: a higher-rank support
escaping the slab while recycling the same conic geography. So the sharpest
question you must answer (in either direction):

**Can a tall exact idempotent's D-cell carrier family escape every bounded
slab?** Either (i) prove a slab-confinement lemma on the D cell (tall + ultra +
thin-rim + disjoint hulls forces the completion's transverse support into a
slab where the starvation obstruction applies — possibly after a case split at
g_u = tau), and D-cap reduces to a starvation generalization; or (ii) isolate
the escaping-support completion as a NAMED package with its own refuter shape
and exact structural costs.

## Fresh evidence you must consume (context/fixtures/)

The five refuter batches' convergent signal: tallness binds ALWAYS. The W63
six-shape batch (w63-six-shape-REPORT.md) shows the natural diagonal plateau
construction gets M_I = 0 EXACTLY and its certificate routes to the D cell —
**the D cell is where every natural exact construction actually LANDS**, so
D-cap owns the natural plateau threat. But every tested plateau fails tallness
by an order-one margin (the W55 A_0 = 5 plateau's direct completion has
order-one row negativity, about 5, not tau^2). Diagnose WHY: what does a
disjoint-hull diagonal certificate structurally COST a tall exact idempotent?
The W64 exact 4x4/8x8 calibrations (hostile-verified) show tall TOP OWNERSHIP,
not intersection, is the real obstruction on the I side — check whether the
same is true on the D side, and whether `lem-icap-type-i-structural-cost` has a
D-side analogue (what does a singleton/small far-tight DISJOINT family cost?).
Equally valuable: an explicit exact family that is tall-compatible in the D
cell (even short) — that sharpens the leaf instead.

## Hard constraints (interface discipline + walls; violations = instant reject)

- Signed picture; clone-invariant full-fiber quantities; frame-free constants.
- No 1/t*(v) or 1/t*(u); alpha-free displays used existentially as geography;
  the reduced witness NEVER identified with P_v^+ or eta (no lambda*P = p_v);
  conic coefficients are never interpreted as transitions.
- No witness/y_c averaging, no Jensen, no W37 dual reversal, no raw-index paths,
  no favorable minimizer/kernel/tie, no coefficient-only LP cleanup, no
  finite-cover main target, no summed pairwise engine demands without one R2
  foldback on a common nonnegative test, no freight censoring without a norm
  gap, no second-generation web recursion, no conic recurrence.
- Strict M_I < 1/16 belongs to D-cap; equality M_I = 1/16 belongs to I-cap;
  M_X = 1/8 belongs to the diagonal cells; the certificate was arbitrary before
  classification — no favorable-certificate selection.
- Every mechanism must show EXPLICITLY where T (or a parent height budget) is
  consumed — a ledger-only argument is rejected before review.
- context/FINDINGS.md dead routes are ABSOLUTE.

## Deliverable format — `DCAP-ATTACK.md`

0. **Verdict first** (<= 1 page): which of (a)/(b)/(c) you achieved, and the
   single sentence naming the hard core as you now see it.
1. **The tree / the argument**: per node — (a) pinned contract (single minimal
   statement, af-elevation-shaped); (b) mechanism naming exact banked tools;
   (c) honest price (difficulty, likeliest death, evidence both ways);
   (d) interface check (quantifier order, boundary ownership, no selectors);
   (e) fallback.
2. **Assembly**: nodes => D-cap (or the weakened/reduced statement), quantifiers
   and constants threaded explicitly.
3. **Kill-list check**: PASS/FAIL per node vs every wall above + FINDINGS.
4. **Dispatch order**: routine batch, L3 decider shapes (concrete, with exact
   target inequalities), creative residual(s) last.

Do not touch `argument/` or `definitions/`. Write ONLY the two named files.
