# W68 prover — repair the assembly bridge (lem-huddle-charge-assembly)

You are a fresh, independent prover. Your workspace is this directory: the
full registry snapshot (`argument/`, `definitions/`) + context docs
(`context/`). Everything you produce stays INSIDE this directory. Status
discipline (L0): everything you produce is proposed until hostile-verified;
you promote nothing.

## The situation (read these in order)

1. `argument/lemmas/lem-huddle-charge-assembly.md` — the assembly bridge,
   currently status: stated, hostile-verdicted INVALID.
2. `context/verdict-bridges.md` §2 — the INVALID verdict. It is PRECISE about
   the two failures and it spells out the exact repair recipe (its final
   paragraphs). Treat that recipe as the specification.
3. `context/l2-attack.md` §§2.6-2.7 (with §0-1 for notation and Theorem B) —
   the prose derivation that must become a registry lemma.
4. `context/BRIEF-W62-STRATEGIST.md` (the pinned L5-GAP-1 statement) and
   `context/DECOMPOSITION-W62-L5.md` §pinned-target — the L5 statement the
   registry's lem-l5-* interface attacks; your conj-l5-gap-1 must be
   verbatim-consistent with BOTH the verdict's item 2 and this pinned form.

## TASK — produce REPAIR-W68-bridge.md containing exactly three parts

### Part 1 — `conj-l5-gap-1` (registration, no proof)

Draft the shard: kind conjecture, single minimal contract (no 'hence'
clauses), exactly the verdict's repair item 2 == the W62 pinned statement:
universal c_5 > 0 and, for every fixed universal c_m > 0, a universal
delta_5 > 0 such that whenever 0 < delta(P) <= delta_5, P is an exact signed
idempotent with nonempty visible set W, v is a hidden top vertex with
H > 16*tau, and A subset {j : ||p_j - p_v||_1 >= 4*tau,
dist_1(p_j, conv W) > H - 8*tau} satisfies sum_{j in A} max(P_vj,0) >= c_m,
then some top support functional phi at v satisfies
sum_{j in A} max(P_vj,0)*(H - phi(p_j)) >= c_5*c_m*tau.
Check every symbol against definitions/ and the lem-l5-* shards; body notes
that the W62/W63/W64/W65/W67 lem-l5-*/lem-ihorn-*/lem-icap-*/lem-dcap-*/
lem-aesc-* interface is this conjecture's reduction tree, and that the
POINTWISE form does NOT imply it by averaging (simplex obstruction, FINDINGS).

### Part 2 — `lem-intersection-branch-production` (statement + COMPLETE proof)

The missing Branch-II production implication (verdict repair item 1),
following l2-attack §§2.6-2.7 but INDEPENDENTLY checked line-by-line:

Contract (draft it as a single minimal statement): for every exact signed
idempotent P with 0 < delta(P) <= delta_B (state the explicit universal
delta_B your proof needs; 1/4 appears sufficient), nonempty visible set,
hidden top vertex v of height H > 16*tau, t*(v) in (0, kappa), and
conv{p_f - p_v : f in T(v)} intersecting t*(v)*conv{p_i - p_v : i in O(v)}
(the L2-core configuration — pin it VERBATIM to the configuration named in
lem-l2-core-collapse's contract), P admits either
(i) a probability measure forbidden by conj-straddling-web-exclusion's
    contract (probability measure on rows simultaneously rho-far
    (||p_f - p_v||_1 >= 4*tau) and co-top (dist_1(p_f, conv W) > H - 4*tau),
    barycenter within 2.2*tau of p_v, average <= (16/13)*kappa under every
    admissible exposer at v), or
(ii) a sub-probability measure forbidden by
    conj-shallow-counterweight-exclusion's contract (total mass >=
    tau/(2+4*delta) on rows rho-far and shallow (dist_1 <= H - 4*tau),
    average <= kappa under every admissible exposer).

Proof from the PROVED registry interface: lem-optimal-face-conic-reduction
(the alpha-free reduced optimal display), lem-intersection-witness-confinement
(B1-B5 — open the shard, quote its full contract, and check every clause you
consume, especially the co-top mass clause you use for mu < 3/16 and the
barycenter/exposer clauses), plus the §2.7 case split at mu vs tau/D
(D = 2+4*delta; equality ownership: state which case owns mu = tau/D and make
the SL1b mass clause match with the correct strict/weak inequality). Every
constant's arithmetic displayed ((16/13)*(3/2+delta) <= 28/13 < 2.2 at
delta <= 1/4, etc.). HYPOTHESIS HONESTY: if the derivation needs any fact NOT
in a proved shard's contract (e.g. t*(v) < kappa for hidden tops, or
nonemptiness of T(v)/O(v) under the intersection hypothesis), either derive
it from a proved shard you name, or record a clearly marked DEFECT block —
do NOT paper over. Also verify the SL1a/SL1b contract constants you target
are exactly the registered ones (2.2*tau, (16/13)*kappa, tau/(2+4*delta),
kappa) — any mismatch is a DEFECT with the correction.

### Part 3 — the repaired `lem-huddle-charge-assembly` (contract + COMPLETE conditional proof)

Rewrite the bridge as the verdict's explicitly conditional two-branch
statement and prove it:

- Contract: IF conj-straddling-web-exclusion (ceiling delta_a),
  conj-shallow-counterweight-exclusion (delta_b), conj-cotop-web-coupling
  (delta_c, constant c_*), and conj-l5-gap-1 (c_5; delta_5 at c_m = c_*/2)
  all hold, THEN with delta_0 = min{delta_a, delta_b, delta_c, delta_5(c_*/2),
  delta_B, 1/4, (c_5*c_*/6)^2} (verify this list and the exponent against
  your own proof; the verdict proposes (c_5*c_*/6)^2 — recompute), no exact
  signed idempotent P with 0 < delta(P) <= delta_0, nonempty visible set, and
  hidden top vertex v of height H > 16*tau carries near-cluster coefficient
  mass sum_{j : ||p_j - p_v||_1 < 4*tau, dist_1(p_j, conv W) > 16*tau}
  max(P_vj, 0) >= 7/8. Keep the (a, theta_0) = (16, 1/8) reading and the
  containment note (H > 16*tau contains the H > 172*tau regime of
  conj-near-cluster-absorption) in the BODY, not the contract.
- Proof, two branches over the always-tight hulls at v (state who owns the
  boundary/degenerate cases):
  (I) intersecting (the L2-core configuration): t*(v) > 0 from
      lem-positive-exposedness-margin + nonemptiness of the far set for a
      hidden top (name the proved shard or derive it; DEFECT if unavailable),
      then Part 2 produces the SL1a- or SL1b-forbidden object, contradicting
      the assumed conjectures.
  (II) disjoint: conj-cotop-web-coupling gives S_A >= c_* on
      A = {j : ||p_j - p_v||_1 >= 4*tau, d_j > H - 8*tau} (open that
      conjecture shard and check its hypothesis block: does it need the
      7/8 near-cluster mass ("heavy")? thread the hypothesis honestly);
      conj-l5-gap-1 at c_m = c_*/2 gives a top support functional with
      far-deep charge >= c_5*(c_*/2)*tau; lem-top-deficit-price gives the
      opposite bound <= delta*(2+4*delta) <= 3*tau^2 at delta <= 1/4
      (verify against that shard's actual contract); contradiction for
      delta below your stated ceiling.
  State explicitly why the two branches are exhaustive, and the exact deps
  list for the repaired shard (drop lem-l2-core-collapse if your proof does
  not consume it; the verdict suggests the production route makes it
  unnecessary — decide and say so).

## Rules

- Signed picture; clone-invariant full-fiber quantities; no 1/t*; conic
  coefficients are geography, not transitions; context/FINDINGS.md dead
  routes ABSOLUTE — in particular do NOT use the averaged-witness mechanism
  (lem-intersection-witness-confinement caps it; the verdict names this as a
  dead repair).
- Every consumed shard: open it, quote the hypothesis clauses you use.
- DEFECT discipline: a gap found and named is a success; a gap papered over
  is the cardinal sin.
- Write ONLY REPAIR-W68-bridge.md (Parts 1-3, with the two draft shard
  frontmatters for Part 1/Part 2 and the redrafted frontmatter for Part 3
  included as fenced blocks). Do not touch argument/ or definitions/.
