<!--
ROLE: the bird's-eye onboarding document for the classical-portfolio work — the document
a fresh agent should read FIRST (before kernel-conjecture.tex, before the dossier).
Plain language, self-contained, no jargon without definition. Written 2026-06-11 at the
close of the waves-14..23 campaign; statuses are dated. Maintained in lockstep with the
frontier (rewrite the STATUS sections when a result changes).
-->

# The classical problem — a bird's-eye overview

## 0. Why this exists, in one paragraph

The parent project generalises Kitaev's theorem on almost-idempotent quantum channels
from completely positive maps to merely positive maps (see `PRD.md`). The **classical
(commutative) case** of that programme is a concrete, self-contained matrix problem:
what do *exactly idempotent* matrices that are *almost* stochastic look like? It is the
proving ground for the whole Layer-1 "approximate structure implies nearby exact
structure" philosophy, and it carries two open problems of the main registry
(`op-classical`, `op-exposed-hull`). After ~20 waves and dozens of delegated workers (~85 archived
verdict files) it has become the project's most developed front. This document is the map.

## 1. The objects, with no jargon

Everything happens with real n-by-n matrices P satisfying TWO exact constraints and one
relaxed one:

- **Exactly idempotent:** P² = P. Not approximately — exactly. This is the single
  strongest structural fact we have, and the campaign's hard-won lesson is that proofs
  fail unless they exploit it deeply (§4.7).
- **Rows sum to one:** P·1 = 1, exactly.
- **Almost nonnegative:** entries may be slightly negative. The deficiency budget is
  **δ ("delta") := the largest total negative mass in any single row**
  (δ = max_i Σ_j max(−P_ij, 0)). A genuine stochastic matrix has δ = 0. We care about
  small δ. A derived scale used everywhere: **τ := √δ**.

At δ = 0, these matrices are completely classified (a classical theorem of
Högnäs–Mukherjea, source pinned locally in `refs/hognas-mukherjea-2011/`, Thm 1.16):
after permuting indices, the rows organise into k "recurrent blocks" — within each
block all rows are identical probability rows supported on that block — plus
"transient" rows that are convex mixtures of the block rows. So at δ = 0 the geometry of the rows (as points in R^n) is: **k distinct extreme
points, everything else inside their convex hull** (this convex-geometry rendering is
a derived consequence; H-M's literal statement is the block/proportional normal form). We call this family the **H-M normal forms**; it is the δ = 0
locus that everything is measured against.

### The geometric quantities

Treat each row p_i of P as a point in R^n with the ℓ¹ (sum of absolute values)
distance.

- A row vertex v is **visible** if an affine function h certifies it from outside:
  h(p_v) = 0, 0 ≤ h ≤ 1 on all rows, and h ≥ κ on every row at ℓ¹-distance ≥ ρ from
  p_v ("you can see it from outside with a flat light, with a quantitative margin").
  IMPORTANT: this is *scale-dependent* — the formal parameters are ρ = 4τ and
  κ = τ/4, and rows closer than ρ are exempt from the margin (see
  `kernel-conjecture.tex` and `definitions/def-exposed.md` for the exact form); the
  strict classical notion of an exposed point is only the δ = 0 limit of this. Geometrically coincident duplicate
  rows count as a single point ("multiplicity-correct"). **W** is the set of visible
  row points; **C_W = conv(W)** is their convex hull.
- A row that is a vertex of the row polytope but NOT visible is **hidden** — meaning
  it fails the scale-dependent margin condition above (not merely "no functional
  exposes it strictly"). Hidden vertices are the troublemakers: they stick out of the
  hull with no robust certificate.
- The **height H** of the configuration is how far the worst row sticks out:
  H = max_i dist₁(p_i, C_W). At δ = 0, H = 0 (every row is in the hull of the block
  rows, which are all visible).
- For a hidden row v, **σ̃_v ("sigma-tilde")** is the total positive mass that row v
  places on columns j whose rows p_j lie strictly outside C_W — INCLUDING j = v
  itself when p_v is outside (the certified record instances lean on this
  self-coefficient). It measures how much of v's weight sits on outsiders, itself
  included.

### The conjectures, plainly

Two statements at different strengths — keep them apart:

- **The formal KERNEL CONJECTURE (what the registry chain actually needs).** There
  are universal δ₀, B such that for δ ≤ δ₀: W is nonempty, and every hidden row
  vertex with σ̃ > √δ lies within B·√δ of C_W. Note the √δ scales throughout — this
  is the precise statement in `kernel-conjecture.tex` (Conjecture 1), and it is what
  feeds the proved chain below.
- **The LINEAR LAW (the campaign's stronger working target).** Every exactly
  idempotent, row-sum-one matrix with small negative budget δ satisfies **H ≤ C·δ**
  for a universal constant C. In words: *you cannot buy height except by paying
  negative mass, at a fixed exchange rate.* This implies the Kernel Conjecture with
  room to spare, and it is what the evidence supports: across the entire record
  (67,000+ verified exact instances over six campaigns) every instance satisfies
  δ ≳ H/2; the locally worst observed ratio is H/δ = 2.000000000013. The constant 2
  is empirical/conjectured, not proved globally.
- **What it buys.** Kernel Conjecture ⇒ HLC (a "high-shell localization" lemma —
  hidden vertices cannot be high) ⇒ `op-exposed-hull` (every row is O(√δ)-close to
  the hull of the visible rows) ⇒ `op-classical` (the classical stability theorem the
  parent project needs). The downstream arrows are proved or proved-modulo-recorded-
  audits; the missing formal input is the Kernel Conjecture. See
  `report/kernel-conjecture.tex` for the precise statements and the per-link ledger.
- **Related W-free target.** "Every such P is within C·√δ of an H-M normal form in
  the Baake–Sumner normal-form distance" (the audited W-free formulation,
  `w105_wfree` / `w11_wfree_audit`). CAUTION: the naive strengthening "O(δ)-close in
  full matrix distance" is REFUTED (registry lemma `ex-hume`) — height H obeys a
  linear law empirically, full matrix distance does not. This W-free form is a
  *target*, not proved equivalent to the Kernel Conjecture — check
  `kernel-conjecture.tex` before treating it as interchangeable.

### Two scales that matter

- **The corner scale δ* = (2−√3)² ≈ 0.0718.** Above it ("large δ"), tall hidden
  configurations exist: we have certified exact instances with a hidden vertex,
  σ̃/τ ≈ 1.55 and H/τ ≈ 0.10 at δ ≈ 0.233 (`experiments/out/w17_cert_audit/`). Below
  the corner ("small δ" — the regime that matters for the parent project) the record
  is empty: max H/τ over hidden vertices collapses like 2δ/τ as δ → 0. All conjectures
  live below the corner; instances above it constrain proofs but refute nothing that
  matters.
- **Heights are tiny in absolute terms either way:** the linear law H ≤ 2δ holds on
  every instance ever produced, above and below the corner.

## 2. Where things live (the file map)

| What | Where |
|---|---|
| THIS overview (start here) | `agent-A/explorations/classical-portfolio/OVERVIEW.md` |
| Precise statements + evidence ledger + dead-route list (~15k tokens) | `report/kernel-conjecture.tex` (in this directory; PDF alongside). NOTE: it retains the path-product "working form" (Conjecture 2 family) with its cloning caveats; the ACTIVE attack has moved to the variety programme (§4.7 here) |
| "The dossier": the full campaign log, wave by wave (append-only, large; read the FINAL/most-recent sections first — search "WAVE 18", "w23") | `notes/wave5-sigma-wall-parallel.md` |
| Every worker's verdict, archived verbatim | `notes/swarm-answers/*.md` (~85 archived verdict files) |
| Numerics, instances, certified counterexamples | `experiments/out/` |
| The 49-page self-contained report (day-2 state; superseded on frontier items by this doc) | `report/main.pdf` |
| Delegation how-to (codex CLI) | `docs/codex-delegation.md` (REPO ROOT docs/, not this directory) |
| Task state | `bd ready`; the kernel bead is `aipm-3u6` |

Conventions used throughout: δ = row negative mass (NOT entrywise), τ = √δ,
multiplicity-correct vertices (duplicate rows = one point), ℓ¹ row distances,
max-row-sum operator norm.

Mini-glossary of project-internal terms used below (one-liners; details in the parent
repo's `PRD.md`/`CLAUDE.md`): **op-classical / op-exposed-hull** = open problems in
the parent project's result registry (`argument/`); **HLC** = the "high-shell
localization" lemma named above; **registry/af** = the parent project's canonical
proof layers (one-line contracts + machine-checked adversarial proof workspaces);
**Recipe A→B** = the gated procedure for promoting exploration-lane results into
those canonical layers (reviewer ≠ author); **bd** = the issue tracker (`bd ready`);
**hostile audit** = an independent worker tasked to BREAK a claimed proof before we
record it as proved.

## 3. The frontier in one box (2026-06-11)

> **Proved and independently audited** (the "variety programme", §4.7): four lemmas —
> the tangent-cone lemma (the infinitesimal linear law, constant 2, dimension-free),
> the ambient fixed-mass visibility lemma, the mass-removed boundary-recoding lemma,
> and the stratified distance-to-locus bound.
>
> **The immediate open piece:** the ASSEMBLY of those four into the LOCAL linear law
> (H ≤ C_loc·δ near the H-M family). A first assembly was claimed and then BROKEN by
> its hostile audit (2026-06-11): the visibility hypotheses fail at the chosen base
> by factors 12.8–128 on a concrete nearest-branch test (`w23_loj_audit.md`). The
> local law itself is NOT refuted — the gap is constructing an arc/base choice whose
> hypotheses actually hold.
>
> **Behind it, the standing gap to the full small-δ statement:** the GLOBAL question
> — must every exactly idempotent matrix with small δ lie near the H-M family at
> all? (The W-free target above.)
>
> **A fresh lead on the global question (user discovery, 2026-06-11):** H-M
> **Theorem 1.12** — the theorem directly after the nonnegative classification — is
> an exact structure theorem for arbitrary REAL (signed) idempotent matrices, with a
> converse: proportional-row classes + explicit signed sum rules, valid at every δ.
> The campaign had never read it (§4.9); a dedicated worker is on it.

## 4. The strategy map — everything tried, and how it died or lives

Each entry: the idea in plain terms → outcome → pointer. "Died" entries are permanent
constraints: do not re-walk them without new input.

### 4.1 The LP / visibility frame (the gravitational well)
Treat hiddenness as a linear-programming statement (a functional that fails to expose).
**Meta-finding (wave 10):** five independent strategy families, when they used "v is
hidden" as a hypothesis, collapsed into the SAME linear program — the normal cone of
the hiddenness constraint IS the LP dual cone. Within that frame, an explicit death
certificate (the "pushed witness") shows LP support-cleanup cannot close the problem.
**Consequence: a proof must either fight inside this one LP, or avoid hiddenness as a
hypothesis entirely.** → dossier "WAVE 10", `notes/swarm-answers/` t1–t10.

### 4.2 Ten classical strategy kinds (wave 10) — all dead or absorbed
Induction on n, probabilistic coupling, rank-complement algebra, extremal/KKT,
sum-of-squares on strata, discharging, Lyapunov functions, minimax games, homotopy
continuation, Birkhoff contraction. All ten died or collapsed (five collapsed into the LP frame of 4.1); the table with
each death point is in the dossier ("WAVE 10 — the 10-strategy-kind swarm"). Two
left lasting tools behind: t10's Birkhoff finisher (→ 4.3) and the LP-collapse
meta-finding itself (→ 4.1).

### 4.3 The component finisher (PROVED) and the path-product programme (DEAD END, instructively)
**Proved (under explicit hypotheses):** if a group of mutually-communicating shallow rows
is CLOSED (positive mass stays inside), has all its internal positive transition weights
bounded below ("a fat component"), and its collapse radius beats the exposure threshold,
then exact idempotence + a projective contraction argument (no spectral gap needed)
forces all its rows to collapse together and become visible — contradicting hiddenness.
The analytic (as opposed to measured) closure of the shallow band remains a recorded
caveat. Also proved and
audited: such closed components are automatically aperiodic (exact idempotence forbids
period ≥ 2 for δ < 1/4). → `w12_comp_finisher`, `w15_periodic(+_audit)`.
**The dead programme around it:** "path-product floor" conjectures tried to feed the
finisher by lower-bounding products of transition weights along paths. Killed twice
over: (a) the **cloning obstruction** — duplicating an index preserves every geometric
quantity and exact idempotence but makes raw path products arbitrarily small, so any
index-level path-product statement is false-or-vacuous (→ `w15_prover`,
`w15_clone_audit`); (b) even the repaired quotient (multiplicity-correct) version
stalls at an "anti-splitting" step — aggregate mass cannot be pinned into a single
component; two independent provers died at the same estimate (→ `w16_quotient`,
`w16_barrier`). The boundary-identity rescue (exact identities B² − B = −EC etc.)
gives only upper budgets, never lower bounds — height cancels (→ `w19_boundary`).

### 4.4 Certificates and SOS — structurally blocked
- Chain-local scalar certificates: **impossible** — the scalar shadow of the thin-chain
  inequality is FALSE (exact rational witnesses at every tested chain length L = 2..5), so any proof
  must use genuine matrix/realization structure (→ `w15_sos`).
- SOS modulo the idempotent ideal: well-posed, but the hiddenness side-conditions
  resist polynomial encoding (the same LP collapse as 4.1, one level up); smallest
  hidden geometry is at (n,k) = (4,3) (→ `w18_sos_ideal`).

### 4.5 Numerics and counterexample search — the empirical spine
Six campaigns, 67k+ verified exact instances, three independent generators, plus
dedicated refuter agents with template families. Outcomes: the **linear law fits the
entire record**; the once-conjectured √δ "floor" was a corner artifact (the **corner
theorem**: exact constants τ* = 2−√3, wall H/τ = 2(2−√3) ≈ 0.536); the σ̃-gate and
then the joint antecedent (σ̃ > τ AND H > 0.1τ) were both realized ABOVE the corner by
nonlinear optimization and **certified exact** (rationalized, hiddenness decided beyond
floating point) — resetting which statements can be claimed at large δ, while leaving
the small-δ regime empty as ever. → `experiments/out/w15_refuter, w16_*, w17_*`,
dossier d8–d14 sections.

### 4.6 The δ=0 proof autopsy (Högnäs–Mukherjea) — what survives signing
The actual classical proof was dissected step by step against OUR perturbation
(exactness free, only positivity perturbed). Most of its mechanism is **sign-rigid**
(zero-sum closure, zero-pattern symmetry, positive diagonal — each fails under signed
cancellation, with explicit counterexamples), but two steps are **sign-robust** and
became workhorses: exact row reproduction (every row is reproduced by its own
positive successors up to (2+4δ)·ν_i) and the post-collapse equal-input
specialization. → `w14_autopsy`, `w15_audit`, `w15_hmloci` (loci byte-pinned).

### 4.7 THE VARIETY PROGRAMME (the current frontier — and the lesson of the campaign)
User-prompted insight (2026-06-11): every prior attack consumed P² = P only through
weak corollaries. Treating the constraint set {P² = P, P1 = 1, rank k} as a geometric
object (a smooth homogeneous space with explicit charts; the H-M family = its δ = 0
locus, a finite union of smooth pieces) unlocked the present chain. All items below
are independently hostile-audited unless marked:

1. **Tangent-cone lemma** (`w19_tangent` + audit): at every H-M point, along every
   direction tangent to the idempotent variety, first-order height growth costs
   first-order negative mass at the exchange rate **2, independent of dimension** —
   the infinitesimal linear law. Avoids hiddenness as a hypothesis (so escapes 4.1);
   uses only clone-invariant quantities (so escapes 4.3's obstruction).
2. **Ambient fixed-mass visibility lemma** (`w20_curve` + `w20_t1_audit`): an explicit
   radius within which the visible vertices of an H-M point stay visible under
   row-wise perturbation — disarming, at fixed block masses, the recorded
   "compactness fails because visibility jumps in limits" dead route.
3. **Mass-removed boundary recoding (L1/L2)** (`w21_recode` + audit): when block
   masses degenerate, recode to a boundary normal form with all errors controlled by
   the TOTAL REMOVED MASS (never thresholds, never per-step sums — the audited form
   is the one-shot final-profile recode; the step-by-step version provably
   overcharges by a factor n).
4. **Stratified distance bound** (`w23_loj` + `w23_loj_audit`): squared chart-distance
   to the FULL δ = 0 locus is bounded by a constant times δ (audited; the
   promotable-zero enumeration must include induced transient-row entries). The
   fixed-single-piece version is FALSE — "support addition" directions move between
   pieces of the locus at zero cost (`w22_jet`).
5. **The LOCAL-LAW ASSEMBLY — OPEN.** The first attempt to combine 1–4 into
   H ≤ C_loc·δ near the H-M family was BROKEN by audit: its visibility hypotheses
   fail at the chosen recoded base (nearest-branch test, factors 12.8–128 —
   `w23_loj_audit`). Not a refutation of the law; the open problem is an arc/base
   construction whose hypotheses hold (candidate: recode to the NEAREST branch
   rather than the final profile, or prove visibility at the nearest locus point
   directly).

Negative knowledge with teeth, from the same programme: the fixed-base second-order
race is EMPTY (no counterexample seed exists in the dangerous directions — `w21_second`);
the cohomological Newton iteration fails at a precise point (the positivity projection
creates first-order diagonal error the variety retraction cannot absorb —
`w18_similarity`; this is the classical twin of the parent project's `op-layer1-gap`
obstruction); the left-fixed-vector proximity lemma is FALSE (exact n=4 family,
`w19_leftcone`).

### 4.8 Literature leads (acquired or to acquire)
The linear law restated: (i) a Łojasiewicz/error-bound statement for a semialgebraic
pair (what 4.7.4 partially delivers); (ii) quantitative stability of norm-one
("contractive") projections on ℓ∞ⁿ in the sense of Douglas–Ando — the H-M family IS
the norm-one case and our P has norm 1 + 2δ. Acquisition shopping list (Douglas 1965,
Ando 1966, Luo–Pang 1994, Flor 1969, Meyer 1989, Kato, Stewart–Sun) is a filed bead;
all such claims are UNVERIFIED LEADS until byte-pinned into `refs/` (repo law L1).
→ `w18_quadlit`.

### 4.9 H-M Theorem 1.12 — the signed structure theorem (NEW lead, worker in flight)
The source book contains, immediately after the nonnegative classification, a
structure theorem for arbitrary REAL idempotent matrices (Thm 1.12, txt ~:2245):
a partition {T, B, C₁..C_k} where each C_s is a class of mutually proportional rows
(rank-one restriction), the B-rows are explicit linear combinations of k
representative rows, with exact coefficient sum rules ((1.2): in-class sums equal 1;
(1.3): cross-class sums equal 0) — and a converse. This is EXACT at every δ (pure
linear algebra; the text warns the partition is non-unique), and the sum rules are
precisely the signed analogues of the "zero-sum closure" steps the δ=0 autopsy (4.6)
declared sign-rigid. The whole campaign missed it (the autopsies targeted Thms 1.11,
1.16, 2.2). Candidate payoff: an algebraic route to the GLOBAL gap — quantify how
near-positivity forces the C_s classes toward equal-input blocks and the B-rows
toward convex mixtures, possibly giving the nearest H-M point constructively (and
bypassing the broken assembly's visibility issue). VERDICT (`w25_hm112`): PARTIALLY —
the right global coordinate system, with a 4-lemma candidate chain to the global gap
(P ≈ 0.48, the highest credence yet); the naive nearest-point construction fails on a
precise obstruction (exact proportional classes can SPLIT a limiting recurrent block —
coefficients blow up like 1/δ; the MERGED stratum point is 2δ-close), which is the
same nearest-branch/merging phenomenon that broke the local-law assembly. Synthesis:
1.12 coordinates + the audited recoding/merging theory + clip/normalize. STATUS
(end of 2026-06-11): the clustered-conditioning lemma (L2) is PROVED AND AUDITED in
dimension-free form (η = √δ clustering; max-volume actual-row basis gives coefficient
bound A = 1 — the initial rank-dependent bound was an artifact, `w26_cluster` +
`w26_cluster_audit`). The bridge then cascaded through three
further reductions (each wave proving partials and naming the next statement —
`w27_concentration`: O(δ) support-concentration refuted, true scale √δ;
`w28_face`: reduced to the representative displacement lemma; `w29_displacement`:
general-row version refuted at δ=0, max-volume form numerically bounded;
`w30_telescope` + `w30_maxvol`: TWO INDEPENDENT reductions converging on one
inequality with matching constants). THE CAMPAIGN'S SINGLE NAMED OPEN (as of the end
of 2026-06-11) is the **transverse coefficient tax**:
Σⱼ(P_{u_s j})₊·Σ_{t≠s}(−a_t(j))₊ ≤ C_μ·δ — rows positively fed by a max-volume
representative cannot carry much negative foreign-coefficient mass. It vanishes at
δ=0 (coefficients are convex there); proving it closes, in sequence: the displacement
lemma → the face estimate (Markov step, written) → the L4 assembly → the GLOBAL
W-free O(√δ) theorem feeding `op-exposed-hull` → `op-classical`. Prover in flight
(`w31_tax`).


## 5. What a future agent should do (and not do)

1. **Read order:** the repo gate files first (`PRD.md` → `CLAUDE.md` → root
   `HANDOFF.md` — repo law §0), then within the classical lane: this file →
   `report/kernel-conjecture.tex` (precise statements + the evidence/constraints
   ledger §5) → the dossier's FINAL sections → `bd ready`.
2. **The frontier task is §4.7.5**: repair the local-law assembly (an arc/base
   construction whose visibility hypotheses hold — the audit's nearest-branch
   failure data in `experiments/out/w23_loj_audit/` is the concrete constraint set).
   Behind it: the GLOBAL gap (§3), dimension-freeness of the local constants, and
   Recipe A→B banking of the audited chain into the registry/af layers.
3. **Do not re-walk the dead list** (4.1–4.4 deaths, the dead-route items in
   kernel-conjecture.tex §5) without genuinely new input. Every one has a named,
   archived death certificate.
4. **Every new proof claim gets a fresh hostile audit by a different worker before it
   is recorded as proved.** This protocol caught real errors in this campaign at least
   six times (constants, invalid iteration schemes, false sharpness claims, a
   fabricated-quote risk class). Discovering a failure is success.
5. **Work clone-invariantly** (quotient by duplicate rows; never atom-level path
   products) and **avoid hiddenness as a hypothesis** where possible (4.1).
6. Orchestration practicalities: codex delegation cheatsheet in
   `docs/codex-delegation.md`; archive every worker verdict into
   `notes/swarm-answers/` immediately (tmp is volatile); long worker artifacts go to
   `proof.md`/`audit_report.md`, never `answer.md` (capture collision); commit + push
   every harvest.
