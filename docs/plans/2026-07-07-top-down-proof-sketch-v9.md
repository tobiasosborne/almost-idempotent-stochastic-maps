<!--
ROLE: the top-down, breadth-first FULL proof sketch of op-classical, VERSION 9 (session 11,
  round 5) — THE CANONICAL STRATEGIC MAP. Supersedes
  docs/plans/2026-07-07-top-down-proof-sketch-v8.md (kept intact for line citations) after
  waves W34-W38 (commits de2659f, 103b780, ca32fd2, ac9288a, d1392bb) and af elevations #2-#3
  (072c97f: lem-genuine-disintegration 18th; 2a01032: lem-top-concentration 19th).
STEWARDSHIP CONTRACT (binding, 2026-07-06): reconcile after every banked wave; retire with
  certificates; re-price; supersede by dated file; update pins on filename change.
STATUS DISCIPLINE (L0): a SKETCH — promotes nothing. Tags as in v8.
MEASURE OF PROGRESS: unscoped/unpriced surface SHRINKING.
PROVENANCE: v8 + docs/waves/2026-07-07-W34/W35/W36/W37 (+ W38 pending its verifier at this
  file's first commit) + FINDINGS 2026-07-07 entries.
-->

# Top-down proof sketch v9: op-classical (2026-07-07, session 11 round 5)

## THEOREM (op-classical) — unchanged. TRUNK — unchanged from v8
(<2>5, <2>6 reviewed; <2>7 = the only unreviewed trunk link + the small loose-delta lemma;
<2>4 = the Kernel input, split as below).

## THE FIVE-ROUTE CONVERGENCE (the session's terminal picture)

Every mechanism family attacked this session bottoms out on ONE conjecture:

> **conj-near-cluster-absorption** (to be registered on VAG's verdict; = the residual content
> of [[conj-low-slab-cap]]): in the tall regime, a hidden top cannot keep >= 1 - theta_0 of
> its positive mass on its RHO-NEAR DEEP CLUSTER (rows within 4*tau of p_v at depth > a*tau)
> — heavy near-cluster mass forces exposedness of some cluster-side vertex.

The five routes and their exact walls (all reviewed/certified; FINDINGS 2026-07-07):
1. Witness coupling (W26/W29): depth-Markov pins >94% witness mass deep+far; NO comparison
   between lambda and P_vj^+ exists (VP/VW-confirmed honest limits).
2. CS/pincer (W32/W33): P_v^+{h >= s} <= nu/s (SHARP); mass at h = 0 (self/cluster) invisible
   to every admissible functional; the pencil is non-infeasible.
3. Collapse family (W34): depth-d collapse with exact correction; ALL collapse tools are
   one-directional (push sigma_a UP); the g-max ledger concentrates mass on near-max-g rows.
4. Absorption/proximity (W35/W36): received mass = proximity but proximity NEVER reaches the
   exposedness-exempt scale (D(theta+4tau) > rho at theta = 0); the certified transition shows
   absorption spends the RHO-HALO EXEMPTION (t* = ratio of circuit coefficients; far-set jump).
5. Dual certificates + residual cancellation (W37/W38): t* <= nu/L_F (SHARP) but upper bounds
   cannot be run backward through hiddenness; the self-cluster residual split cancels the
   far-deep term EXACTLY — S = 1 - O(tau) pure clusters are CONSISTENT with every banked
   identity. Plus the technical catch: def-exposed is VALUE-normalized (no Lipschitz bound) —
   near rows need a conditioning lemma before any exposer transfer.

**Levers for the next attack round (priced, none yet tried):**
(a) the value-vs-Lipschitz CONDITIONING lemma (make near-row LPs comparable under a depth
    condition — the missing hinge of the cluster interlock);
(b) the W36 exact transition family as a local model (absorption is exact there; perturb);
(c) the deepest-vertex extremal choice (kills the C_a^> escape identically);
(d) W-nonemptiness anchor tension (an all-hidden cluster has NO visible anchors for its
    witnesses — the W30/W31 convergence, still unexploited inside the cluster mode);
(e) quotient/cloning: a pure rho-near cluster is quotient-close to a SINGLE vertex with a
    heavy self-loop — what does exact idempotence say about the quotient object itself
    (lem-self-defect-shadow is the first brick, pending VAG)?

## ROUTE A chain status (all reviewed or rigorous EXCEPT the one conjecture)

conj-near-cluster-absorption (+ far-mass handling via pincer/witness at a theta-split)
=> conj-low-slab-cap => [lem-cs-low-slab-pincer, reviewed] sigma_a <= 1-theta
=> [lem-parametric-halo-collapse, RIGOROUS] H <= (K_a/theta)*tau
=> Kernel height clause at B = K_a/theta => [lem-kernel-implies-hlc, reviewed] HLC
=> [lem-hlc-implies-exposed-hull, reviewed] op-exposed-hull (pinned-delta)
=> [<2>7, mod-audit] op-classical.
Kernel(i) (W-nonemptiness): delta=0 / simplex / rank<=2 reviewed; rank>=3 OPEN, sharing the
cluster mechanism (lever d).

## Rigour ladder (aism-88r queue)

af-validated: **19** (NEW: lem-genuine-disintegration #18, lem-top-concentration #19 — three
of four g-bootstrap steps L0). LIVE: lem-hiddenness-dual-witness (orchestration #4). QUEUE:
lem-cs-low-slab-pincer, lem-harmonic-affine-bridge, lem-row-far-dual-certificate (all
deps-none, few-line proofs), then the depth-Markov/companion/depth-d family.

## RETIRED in this redraw (new items; 1-19 as in v8)

20. **The lambda*P hybrid as an amplifier** (W37): feasible but non-amplifying
    (lem-hybrid-dual-certificate). Do not re-run substitution waves without a new
    normalization idea.
21. **The renormalized self-cluster residual route** (W38, pending VAG): the far-deep term
    cancels exactly; S = 1 - O(tau) is consistent. Do not re-run the naive split.
22. **Dual-certificate capping of hidden row mass** (W37): upper bounds on t* cannot cap
    row mass under hiddenness — the direction is a wall, recorded.

## THE OPEN LEDGER v9

1. **conj-near-cluster-absorption** — THE Route-A input (five-route convergence). [OPEN;
   levers a-e priced above]
2. W-nonemptiness rank >= 3 (Kernel(i)) — same mechanism, lever (d). [OPEN]
3. Trunk <2>7 (three DC4 gaps + stochasticity interface). [mod-audit; next mandatory trunk
   item, aism-23b]
4. The loose-delta robustness lemma. [small]
5. af elevation queue. [in progress, one at a time; 19 done]
6. Route B alpha->1 [held]; arm E [fallback]; refs (aism-5de, aism-1nh); report labels
   (aism-av0, 30+ shards warn-level).

## Unscoped surface remaining

- conj-near-cluster-absorption's mechanism — the ONLY unscoped mathematics (levers a-e are
  scoped attacks; the mechanism itself is open).
- The conditioning lemma (lever a) — scoped, unattempted.
- Trunk <2>7 audit scope; the loose-delta lemma; everything else as in v8.

## How to keep this alive — as in v8 (pins: HANDOFF, CLAUDE.md router, bd memory).
