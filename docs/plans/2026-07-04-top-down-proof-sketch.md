<!--
*** SUPERSEDED 2026-07-05 by docs/plans/2026-07-05-top-down-proof-sketch-v2.md (session-8 DC1-DC4
decision-check wave: trunk equivalence unproved both directions; broad NSC disproved; K<1>6
assembly RED; fusion supported). Kept intact because banked artifacts cite v1 line numbers
(e.g. the DC4 gap table). Do not build new waves against THIS file. ***

ROLE: the top-down, breadth-first FULL proof sketch of op-classical (user-requested, session 7) —
  Lamport-style structured outline, highest hierarchy level only. The strategic map every wave and
  every DAG-wiring step should be built against.
STATUS DISCIPLINE (L0): this is a SKETCH — it promotes nothing. Every step carries an honest tag:
  [rigorous] = af-validated in-repo; [reviewed] = independent-codex-review-approved paper proof;
  [mod-audit] = inherited/unreviewed transcription work; [OPEN] = missing mechanism.
UPDATE POLICY: rewrite as the architecture changes (a superseded sketch moves to an appendix or is
  git-history); keep the four-open-mechanisms ledger current.
PROVENANCE: strategist synthesis at session-7 close (post: 4-lane audit, 7-lane literature sweep,
  deciders #1/#2, wave 13 both branches + review). Conversation-level; canonical record is THIS file.
-->

# Top-down proof sketch: op-classical (2026-07-04)

## THEOREM (op-classical)

There exist universal constants eta0, C > 0 (independent of dimension n) such that: for every
row-stochastic Q with ||Q^2-Q||_{inf->inf} <= eta <= eta0 there is a stochastic idempotent E with
||Q-E||_{inf->inf} <= C*sqrt(eta). The exponent 1/2 is optimal.

**Global objects.** ||.|| = max-row-l1. For signed P: delta(P) = max_i sum_j (P_ij)^- , nu_i = row-i
negative mass, k = rank, tau = sqrt(delta) (the exposedness window), W(P) = visible (nonnegative)
rows, H = l1-height above conv W. Chart machinery: actual-row chart U (k rows forming a row-space
basis), coordinates a_t(j), left-inverse masses beta_s(j) = P_{u_s j}, excess
E_s(j) = (mu_s(j) - lambda_s(j))^+, leakage Phi_s(U) = sum_j beta_s(j)^+ E_s(j), theta-half = Gram
volume >= 1/2 * max over actual-row charts.

## PROOF (main chain)

**<1>1. Signed normalization.** P := theta(2Q-I) (Riesz/sign-function calculus on the spectral
clusters near {0,1}) satisfies P^2 = P exactly, P.1 = 1, ||P-Q|| <= c1*eta, delta(P) <= c1*eta.
PROOF: spectrum of Q lies within O(eta) of {0,1} for eta < 1/4; the contour integral is a convergent
power series in Q^2-Q; exact idempotence is CHEAP (linear) — positivity is not; this is where the
problem starts. [rigorous: lem-classical-equiv; external anchor Kitaev arXiv:2405.02434 Prop 3.1]

**<1>2. Reduction to signed rounding.** Suffices: every exact signed idempotent P with row sums 1
and delta = delta(P) <= delta0 admits a stochastic idempotent E with ||P-E|| <= c2*sqrt(delta).
PROOF: triangle inequality through <1>1. [elementary]

**<1>3. Affine frame.** k = tr P; rows p_i live in a (k-1)-dim affine subspace with row reproduction
p_i = sum_j P_ij p_j; all subsequent quantities are actual-row barycentric and CLONE-INVARIANT (the
only known way past the cloning obstruction). [rigorous-elementary]

**<1>4. Chart normalization.** Fix U0 = a theta-half Phi-argmin chart. Coordinate box |a_t(j)| <= 2
for all rows/charts in the class.
PROOF: existence by finiteness; box = maxvol swap-determinant identity capped by theta-half. The
theta-half RELAXATION is essential: exact max-volume selection is exponentially inapproximable and
exists-exact-selector arguments are a recorded dead route. [rigorous-elementary; anchor
Goreinov-Tyrtyshnikov / Mikhalev-Oseledets arXiv:1502.07838]

**<1>5. THE CORE — chart leakage bound (EX).** LEMMA K: max_s Phi_s(U0) <= C0*delta.
[OPEN — the single deep input; own block below]

**<1>6. Coordinate cleansing.** For every pivot: S*_s(U0) <= 2*Phi_s(U0) + 6*delta <= (2C0+6)*delta
— in the U0-frame every row is within O(delta) (beta-weighted, per pivot) of the positive cone of
the chart rows, uniformly in n, k.
PROOF: lem-factorization [rigorous given K].

**<1>7. Height collapse / exposed hull.** Every hidden vertex with invisible mass sigma > tau has
H <= B*tau; hence ALL rows lie within O(tau) of conv W, and W organizes into k' <= k clusters
separated at scale >> tau.
PROOF: two-sided ledger. Upper side [rigorous]: obs-height-collapse / conj-halo-collapse
(H(1-sigma) <= nu(2+4delta)) — height requires sigma -> 1. Lower side (the sigma-door, closed BY
Lemma K via <1>6): hiding mass at height needs transverse negative coordinates in every theta-half
chart, priced at O(delta); height above tau needs financing >= sigma*H > tau^2 = delta —
contradiction. **The unique step where sqrt(delta) enters**: tau is the geometric mean of the
per-row budget delta and the O(1) simplex diameter — exactly where the sharpness example lives.
[mod-audit assembly (HLC / op-exposed-hull) + validated collapse; re-audit queued]

**<1>8. Rounding to an exact stochastic idempotent.** Partition c(i) = nearest cluster (well-defined:
separation >> tau >= ambiguity); pi_c = normalized positive part of the cluster representative;
E_{ij} = pi_{c(i)}(j). Then E^2 = E exactly and E stochastic.
PROOF: identical rows within classes reduce idempotence to pi_c concentrating on own-cluster
columns; off-cluster mass is O(delta) by <1>6 and removed EXACTLY by positive-part normalization.
Quantitative Hognas-Mukherjea/Flor structure (prop-approx-simplex + thm-cluster +
thm-classical-factorization). [mod-audit; no new mechanism given <1>6-<1>7]

**<1>9. Distance accounting.** ||P-E|| <= O(sqrt(delta)) [row-to-cluster] + O(delta) [representative
rounding] + O(sqrt(delta)) [within-class] <= c2*sqrt(delta). QED (main, given Lemma K).

**<1>10. Sharpness.** ex-hume 3x3 forces ||Q-E|| >= c*sqrt(eta). Independent sibling: SBD
arXiv:2405.01532 Rem 5.4. Mechanistic reading (2026-07-04 sweep): {E^2=E, E>=0, E1=1} is a quadratic
system with nonnegativity, DEGENERATE (complementarity sense) at the exposedness window — degenerate
Holder error bounds have sharp exponent exactly 1/2 (Luo-Pang 1994). [mod-audit + external anchors]

## LEMMA K ((EX) chart bound) — own top level

ASSUME: P exact signed idempotent, rank k >= 3, delta <= 1/4; U0 theta-half Phi-argmin; s maximal pivot.
PROVE: Phi_s(U0) <= C0*delta.

**<1>1. Row taxonomy.** Leaking rows (E_s(j) > 0) partition into: fan-financed (volume-permitted
negative coordinate), orphans (legal only through positive coordinates), self-supported (high own
coefficient). Exhaustive, clone-invariant. [definitional]

**<1>2. Fan horn.** Fan-financed leakage pays at bounded exchange rate against pivot negativity:
matched weights w = a_t(j)^-/mu_j telescope, constant <= 2+sqrt(2) (sharp).
PROOF: lem-fan-payment + lem-fan-payment-restricted [rigorous] through the fan-lift
(conj-degenerate-transport) [OPEN — genuine-gap risk; SBD reset-trick is the designated fallback
shape]. 

**<1>3. Orphan horn (RH).** OD <= C_RH*(G_class^- + S_-^mu + sum_{beta>0} beta*nu), C_RH >= 4 forced.
PROOF mechanism: legality-through-positive-coordinate forces a structural financier Gamma < 0 in the
class aggregate; orphan-orphan cancellation priced by own-negativity (G5 family saturates 4). The
budget is stable post-G6 (the three historical patches unify in the sum-beta-nu term). [OPEN
conjecture; exact floor + full certificate survival]

**<1>4. Self-support horn <= (PRT), the collateral skeleton.** Self-supported leaking rows trigger
the pivot-removing disjunction Phi_s(U0) <= max(Psi_j, Gamma_j) [rigorous]; the Gamma branch is
financed by: disjunction -> (CI) import (c>0 [rigorous]; c<0 [reviewed], equality form) -> import
reduction [mod-audit] -> cross-pivot cancellation [rigorous] -> [B <= K*delta] + [C <= 2delta box].
All links rigorous/reviewed except the B-lemma, which reduces [reviewed] to <1>5. The (V)/(Psi)
branches converge on the SAME principle: wave 13 proved chart-move comparisons cannot see the
carriers (all certified B-mass is volume-inadmissible). [rigorous/reviewed skeleton + OPEN charge]

**<1>5. NSC — the self-support charge (innermost open mechanism).**
B_{r,s} <= K0 * sum_{carriers} beta_r(i)^+ * nu_i(P).
PROOF mechanism to realize: cross-pivot cancellation balances carrier negative a_s-mass against
positive a_s-mass on other beta_r-positive rows; at an argmin with a clean high-self Gamma-branch
the balancing rows are boxed and high-self, so row reproduction cannot generate the balance for
free — the G6 escape (self-coefficient carrying chart negativity at low ambient cost) is exactly
the configuration the argmin pivots ONTO, and post-pivot the pattern re-prices with genuine nu on
the carriers. Empirics: K0 ~ 2.8 on all certified data; sup B/delta ~ 0.77764 (algebraic family-limit
law). This is wave 14. [OPEN]

**<1>6. Master decomposition (assembly).** Phi_s(U0) = fan + orphan + self-support parts (exact
partition of leaking rows); summing horns:
Phi_s <= (2+sqrt(2))*nu_s + C_RH*(G^- + S_-^mu + sum beta*nu) + (5K0/4 + 2)*delta <= C0*delta,
each budget term being <= (constant)*delta by definition. Rate-tolerant (G12: no step needs
o(delta)). MUST be codified as one shard so the linker sees the wiring. [OPEN as a written identity;
mechanical given <1>2-<1>5]

**<1>7. Rank generalization / dimension-freeness.** Every step is per-pivot, clone-invariant, boxed,
per-row-budgeted — no index/class counting; three-index arguments transfer with transverse set
{q not in {r,s}} unchanged (rank-4/5 exact evidence: disjunction + (CI) hold verbatim; plateau
bounded). Fallback: incremental class construction with a Kitaev-style error-reduction bootstrap
(delta-inclusion => O(eps)-inclusion) replacing the one-shot argmin by monotone refinement. [OPEN;
visible-break scenario empirically dead — runs/2026-07-04-rank4-transfer-decider/]

QED (Lemma K, given <1>2-lift, <1>3, <1>5, <1>6, <1>7).

## Substitution points (designated fallbacks, not hedges)

- NSC (K<1>5) resists => arm E replaces Lemma K wholesale: dimension-free Holder-1/2 error bound for
  the semialgebraic system {E^2=E, E>=0, E1=1} directly (uniformize Luo-Pang via row-stochasticity).
- Fan-lift (K<1>2) resists => SBD reset-trick regularization per class (arXiv:2405.01532 Lemma 5.5).
- Rank transfer (K<1>7) resists => the incremental bootstrap becomes primary.

## The honest ledger (compressed)

- **Rigorous today:** main <1>1, <1>3, <1>4, <1>6-engine; K <1>2-core (fan lemmas), K <1>4-skeleton.
- **Reviewed (paper-proof):** the c<0 import tool; the B-lemma => NSC reduction.
- **Mod-audit transcription work:** main <1>7 assembly, <1>8, <1>10.
- **Genuinely OPEN mechanisms — exactly FOUR:** NSC (K<1>5), the orphan budget (K<1>3), the fan-lift
  (K<1>2), and the master decomposition + rank transfer (K<1>6-7). Everything else is assembly.

## What this sketch is for

Wave design (each wave targets exactly one <.> step), the DAG-wiring issue (HLC shard + finisher
edges mirror main <1>5-<1>7 and K <1>6), and honest scoping: any claim of progress must name its
step here. A sketch promotes NOTHING (L0).
