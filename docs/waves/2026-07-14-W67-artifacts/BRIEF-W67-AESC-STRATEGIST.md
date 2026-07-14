# W67 creative wave — ATTACK the A-esc leaf (actorization-escape exclusion)

You are a fresh, independent proof strategist-prover. Your workspace is this
directory: the full registry snapshot (`argument/`, `definitions/`) + context
docs (`context/`). Everything you produce stays INSIDE this directory.
Deliverable: `AESC-ATTACK.md` (+ optional `APPENDIX-aesc-proofs.md`). Status
discipline (L0): everything you produce is proposed/`conjecture` until
verified elsewhere; you promote nothing.

## THE OBJECTIVE FUNCTION (user mandate, binding)

**Decomposition into lower-complexity pieces.** A full proof of A-esc is
welcome but NOT the success criterion. Success is EITHER:
(a) a decomposition of A-esc into routine nodes (near-mechanical on the proved
    interface) + strictly smaller creative residual(s), each a PROPER subclass
    or a constant-complexity package (no funnelling into one residual
    restatement); OR
(b) a proof of a quantitatively weakened A-esc (e.g. the recorded fallback:
    assume at least 1/160 of eta_D* has an actor residual <= 3*delta — which
    REMOVES A-esc without imposing rank three or a bounded slab — or a larger
    escape distance K*delta, or gamma depending on H/tau) with the exact loss
    recorded; OR
(c) a precise reduction of A-esc to a NAMED, isolated problem whose statement
    is strictly smaller than A-esc and comes with its own refuter shape.

## Target — verbatim pinned contract (DCAP-ATTACK-W65.md §1.9)

`conj-w65-dcap-actorization-escape-exclusion`:

> Every target datum with the guarded priority package
> eta_D*(A_esc) >= 1/80 satisfies (0.1):
> Z_v(q_A) >= c_m*tau/64 - (c_m/16)*P_v^+(L_v),  L_v := {Q : d_Q <= tau/4}.

Read `context/DCAP-ATTACK-W65.md` IN FULL FIRST and adopt ALL its notation —
it adopts `context/DECOMPOSITION-W63-I.md` §§0-1.1 verbatim (I-base datum,
b = c_m/128, k_b, D_0, delta_rt, e_delta, theta, lambda_A, the selected-corner
certificate and M_X/M_I/M_D). The A-esc cell (1.9) is: carriers in the fixed
D-certificate's display field with g_u >= tau, A_u >= 4, ell_u >= tau/2, and
(after the exact normalization (1.6)-(1.7))
FOR EVERY actual row f:  ||p_f - p_u + A~_u(q~_u - p_u)||_1 > 3*delta.
The "target datum" carries the FULL pinned D-cap antecedent plus everything
the proved routine chain supplies: R0 (root closure: D-mass > 1/16, display
field, R2-closed receivers, g_u <= A_u*ell_u, the (R0.6) gauge implication),
B1-B4 (score-bulk transfer, arbitrary-kernel census, common ownership, tall
same-center packet: exact T-spend < 2*tau/15 + E once at p_{f*}), the realized
B5 top-owned overlay (verifier-corrected Xi_X form), and the R1 priority guard
(the first three cells have mass < 1/80).

## The proved interface (shards in `argument/`; consult each shard's OWN hypothesis block)

The SEVEN W65 D-cap nodes are PROVED registry shards: `lem-dcap-root-closure`,
`lem-dcap-score-bulk-transfer`, `lem-dcap-kernel-bulk-census`,
`lem-dcap-common-ownership`, `lem-dcap-tall-same-center-packet` (the exact
T-spend and the single-center E packet — this is where the c_m*tau/64 term
must come from), `lem-dcap-closed-overlay` (B5, corrected), and
`lem-dcap-five-way-completion-split` (R1). Consume them freely on the D-cap
class — they were rederived kernel-arbitrarily (hypothesis-honest; zero
lem-icap-* consumption). Plus: the W63 lem-ihorn-* bank (10), the W64
lem-icap-* bank (8 — CAUTION: several are stated on the I-cap class
M_I >= 1/16; consume each ONLY where its own hypothesis block holds), the W62
lem-l5-* bank (incl. `lem-l5-top-face-ray-formula`,
`lem-l5-universal-exterior-payer`), the af-validated engine bank (lem-hx-*,
incl. `lem-hx-robust-scalar-starvation` — rank- and slab-free once its actual
row fiber, A >= 4, O(delta) residual, and fiber-aggregate tail cap are
constructed; on A-esc the residual hypothesis FAILS BY DEFINITION, which is
exactly what makes this leaf the actorization-escape problem), the SL1a
machinery, `lem-optimal-face-conic-reduction`, `lem-always-tight-dual-support`,
`lem-positive-exposedness-margin`, `lem-zero-face-localization`,
`lem-starvation-completion-obstruction` (rank-3/bounded-slab; its hypotheses
are precisely what A-esc escapes — positive evidence, not consumable), and the
two exact tallness budgets (the ONLY ones): H(1-sigma_v) <= nu_v*D_0 and
H(1-sigma_g) <= (sigma_v-sigma_g)*tau/4 + nu_v*D_0.

## The sharp question (engage with it in either direction)

A-esc says: on constant D mass, the synthetic zero-face displacement
k_{T,u} - k_{O,u} = A~_u(q~_u - p_u) is a genuine convex-combination
displacement of tau-scale that NO actual row realizes to within 3*delta —
a constant field of missing actors. Exact idempotence means row u's image
point p_u·P is reproduced by the rows; the zero-face conic package says the
always-tight optimal faces T(u), O(u) are disjoint at gap g_u >= tau. The
mechanism sketch (W65 §1.9(b)): such a field must either create a common
exterior receiver at the single center p_{f*} (E finances c_m*tau/64) or pay
the B4 shallow budget. Your job: make this precise, decomposed, and priced —
or show exactly which named sub-case resists and why.

Candidate axes you may find useful (not mandates): split by whether the
missing-actor displacement field is coherent against one fixed clone-invariant
direction (a common-test R2 foldback is legal) vs incoherent/rotating; split
by whether the escaping support has bounded transverse moment against the
B4 center (starvation-type supply vs demand at p_{f*}); exploit that
idempotence forces p_u + A~_u(q~_u - p_u)-type points to be reproduced within
the row hull to accuracy O(delta) (make any such claim exact and honest —
this is where naive versions die; state which exact identity you use);
quantify over the actor-residual distribution retained by R1's fallback.

## Fresh decider evidence you MUST consume (context/fixtures/)

- `w66-dcap-decider-REPORT.md` + `w66-certificates.json` (NEW, this session):
  the five-leaf exact decider. KEY FACTS: (i) NO tested exact family even
  REACHES the A-esc window — the factorized W63 plateau routes to C0 first
  (ell/tau = 2*tau < 1/2 exactly); an A-esc refuter must hold ell_u >= tau/2
  on constant D mass while tall; (ii) tallness (H > 16*tau) binds for the
  SIXTH consecutive exact batch, and the decisive wall is tallness TOGETHER
  WITH a legal far selected mass and a nonempty ultra omega package;
  (iii) the leaf deficit D_leaf was NEVER made negative.
- `w63-six-shape-REPORT.md`: the D cell is where every natural exact
  construction LANDS; all short.
- `w57`/`w58` READMEs: the rank-3 and first-extra-vertex completion LPs are
  INFEASIBLE with exact Farkas certificates — the completion pressure is real
  at low rank; A-esc's whole threat is HIGH-RANK escape (its refuter is a
  growing-rank completion staying > 3*delta from every row displacement).
  Diagnose structurally: WHAT does growing rank buy the refuter, and what
  does it COST in row negativity / tallness / the D ledger? The W55 A0=5
  completion pays order-one finance negativity — is that cost universal along
  any actor-escape family? An explicit exact tall-compatible A-esc family
  (even partial) is equally valuable — it sharpens the leaf.

## Hard constraints (interface discipline + walls; violations = instant reject)

- Signed picture; clone-invariant full-fiber quantities; frame-free constants;
  row-point ell^1 geometry.
- No 1/t*(v) or 1/t*(u); alpha-free displays used existentially as geography;
  the reduced witness NEVER identified with P_v^+ or eta (no lambda*P = p_v);
  conic coefficients are never transitions; the synthetic actor is never
  vertexized; no favorable row/minimizer/kernel/tie/certificate selection.
- No witness/y_c averaging, no Jensen, no W37 dual reversal, no raw-index
  paths, no coefficient-only LP cleanup, no finite-cover main target, no
  summed pairwise engine demands without one R2 foldback on a common
  nonnegative test, no freight censoring without a norm gap, no
  second-generation web recursion, no conic recurrence.
- Boundary ownership per (1.9): g_u = tau gap side, A_u = 4 high side,
  ell_u = tau/2 the starvation window, residual equality 3*delta belongs to
  T-esc (so A-esc is the STRICT > 3*delta cell).
- **Every mechanism must show EXPLICITLY where T (or a parent height budget)
  is consumed, AND identify the exact line producing the c_m*tau/64 term from
  E at p_{f*}, AND the exact subtraction of (c_m/16)P_v^+(L_v) before B4 is
  applied. A ledger-only argument is rejected before review.**
- context/FINDINGS.md dead routes are ABSOLUTE.

## Deliverable format — `AESC-ATTACK.md`

0. **Verdict first** (<= 1 page): which of (a)/(b)/(c) you achieved, and the
   single sentence naming the hard core as you now see it.
1. **The tree / the argument**: per node — (a) pinned contract (single minimal
   statement, af-elevation-shaped; no 'hence' clauses); (b) mechanism naming
   exact banked tools; (c) honest price (difficulty, likeliest death, evidence
   both ways); (d) interface check (quantifier order, boundary ownership, no
   selectors); (e) fallback.
2. **Assembly**: nodes => A-esc (or the weakened/reduced statement),
   quantifiers and constants threaded explicitly.
3. **Kill-list check**: PASS/FAIL per node vs every wall above + FINDINGS.
4. **Dispatch order**: routine batch, L3 decider shapes (concrete, with exact
   target inequalities), creative residual(s) last.

Do not touch `argument/` or `definitions/`. Write ONLY the two named files.
