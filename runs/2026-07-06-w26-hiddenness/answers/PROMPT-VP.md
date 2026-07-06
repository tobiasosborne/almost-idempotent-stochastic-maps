# W26 Verifier VP — HOSTILE verification of worker P's claimed PARTIAL (hiddenness dual witness + top-slab companion)

You are a fresh, independent HOSTILE verifier in the repo
`/home/tobias/Projects/almost-idempotent-stochastic-maps` (signed-idempotent picture). A prover
claims two results. Your job is to try to BREAK them — finding a counterexample, a gap, or an
error is a BIG SUCCESS and exactly what you are paid for. Independently EXPAND every compressed
step yourself; do not take the prover's word for anything. Write nothing to the repo (scratch
under /tmp only).

## Read first (repo files)

- `definitions/def-signed-idempotent.md`, `def-negative-mass.md`, `def-visible-set.md`,
  `def-exposed.md`, `def-invisible-mass.md`, `def-height.md` — the ONLY ground truth.
- `argument/lemmas/lem-top-concentration.md` — its contract and proof sketch are importable
  (reviewed); the prover reuses its support functional phi.
- The prover's full answer (the object under attack):
  `/tmp/claude-1000/-home-tobias-Projects-almost-idempotent-stochastic-maps/87b0c685-fd9d-462c-a048-8f5bd73c906a/scratchpad/W26/ANSWER-P.md`

## The two claims under attack (as the prover states them)

CLAIM 1 (hiddenness LP-dual witness). For a hidden row vertex v (per def-exposed/def-visible-set:
t*(v) < kappa = tau/4, where t*(v) is the optimal margin of the exposedness LP over admissible
affine exposers h with h(p_v) = 0, 0 <= h(p_i) <= 1 on all rows, margin = min over rows f with
||p_f - p_v||_1 >= rho = 4*tau of h(p_f)), there exist lambda_f >= 0 (f in F_v, sum = 1),
alpha_i >= 0, beta_i >= 0 with B := sum_i beta_i < kappa and
sum_f lambda_f (p_f - p_v) + sum_i alpha_i (p_i - p_v) = sum_i beta_i (p_i - p_v).
Consequently, for every affine psi with psi(p_v) = 0 and 0 <= psi(p_i) <= E on all rows:
sum_f lambda_f psi(p_f) < kappa*E.

CLAIM 2 (top-slab companion). For a hidden top vertex v of height H > 13*tau in an exact signed
idempotent with 0 < delta <= (17-12*sqrt2)/2: some row f with ||p_f - p_v||_1 >= 4*tau has
d_f := dist_1(p_f, C_W) > H - (1/2 + delta)*tau > 4*tau (hence f in G_4), obtained by applying
Claim 1 with psi = H - phi, phi the ell1/ell-infty support functional at v (phi(p_v) = H,
phi <= 0 on C_W, 1-Lipschitz).

## Attack checklist (do ALL; add your own attacks)

1. **The LP formulation vs the definition shards.** Does the prover's LP EXACTLY encode t*(v)
   as `def-exposed`/`def-visible-set` define it (admissible exposer class, the margin, the
   rho-far index set F_v, kappa = tau/4)? Any drift (affine vs linear h, which rows the box
   constraint ranges over, vertices vs rows, merged duplicates) breaks everything downstream.
2. **Strong duality + attainment.** Derive the dual YOURSELF from scratch. Check feasibility
   and boundedness of the primal, that strong duality applies, that the strict inequality
   B < kappa survives (the prover needs a witness with B < kappa, not <=).
3. **The edge cases.** F_v empty (no rho-far rows); v not geometrically distinct (clones/merged
   duplicates); sigma-related degeneracies; delta -> 0. Does hiddenness even imply F_v nonempty
   under the shard definitions?
4. **The pairing step.** psi affine with psi(p_v) = 0 — verify the identity
   sum lambda psi(p_f) + sum alpha psi(p_i) = sum beta psi(p_i) really follows (linear part
   applied to the balance equation), and that dropping the alpha term is sign-legal.
5. **Claim 2's constants.** kappa*D = (tau/4)(2+4delta) = (1/2+delta)*tau — check. phi's
   properties from lem-top-concentration's contract only (or re-derive existence from ell1
   duality yourself). Check phi(p_f) <= d_f (is it <= d_f or <= H? derive the correct
   inequality and check the prover uses the right one). Check the numeric chain
   13 - (1/2 + delta) >= 4 + 6*sqrt2 > 4 at delta <= (17-12*sqrt2)/2 EXACTLY (symbolic, no
   decimals).
6. **Exact fixture test.** Build (or reuse from `runs/` bundles) at least one exact small
   instance with a hidden vertex; compute t*(v), the dual witness, and check Claim 1's
   inequality numerically in exact arithmetic (fractions). The banked rank-5 instance in
   `runs/2026-07-06-w25-step4-decider/` (worker-n-report) is a good target if usable.
7. **Scope honesty.** Does anything in the two claims quietly assume W nonempty, H > 0,
   delta > 0, or v a TOP vertex where the prover's text doesn't say so? List every hypothesis
   actually needed.

## Output discipline

- Do NOT run `fr` or `bd`. Do NOT `git commit`. Do NOT modify ANY repo file.
- Tier-tag your checks ([T0]/[T1]/[T2]); exact arithmetic only in fixture tests.
- Final answer BEGINS with one verdict line:
  `VALID (both claims; hypotheses as listed)` or `VALID-WITH-CORRECTIONS (...)` or
  `INVALID (claim N: reason)` — then your full independent derivation of the dual, the
  checklist results, the fixture computation, and the EXACT minimal hypothesis list for each
  claim (this becomes the registry contract if VALID).
