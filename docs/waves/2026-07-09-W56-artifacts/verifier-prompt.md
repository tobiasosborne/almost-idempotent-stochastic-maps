You are a HOSTILE verifier. Finding a counterexample, a gap, an arithmetic error, a
restatement leaf, or a wall violation is a BIG SUCCESS for you — that is your job. You
have NO stake in this document being right; assume it is wrong and try to prove that.

Your workspace is self-contained. The document under attack is `DECOMPOSITION.md`: a
claimed decomposition of the conjecture SL1a (`conj-straddling-web-exclusion`, pinned
verbatim in `target.md`) into an acyclic DAG of candidate lemmas ("leaves") plus an
assembly claiming (all leaves) => SL1a. The task specification the author was bound by
is `target.md` — its STATUS DISCIPLINE, HARD CONSTRAINTS, MANDATORY RED TESTS, and
DELIVERABLE FORMAT define what "valid" means. `context/` holds the prior art and the
dead-route certificates (FINDINGS.md); `argument/` holds the 140 registry shards
(ONLY `status: proved` shards are established facts); `definitions/` + 
`context/CONVENTIONS.md` hold the vocabulary.

ATTACK CHECKLIST (work through ALL of it; do not stop at the first kill):

1. ASSEMBLY SOUNDNESS: re-derive §4 line by line. Does (all leaves) => SL1a actually
   follow, with the stated constants? Check every inequality's arithmetic by hand.
   Check the constant conversion back to SL1a's verbatim constants (2.2*tau radius,
   (16/13)*kappa exposer bound, depth band H-4*tau, H > 16*tau, rho = 4*tau,
   delta_bar = 2^-16 if used).
2. QUOTED-CLAUSE FIDELITY: for every cited proved shard, open the shard in argument/
   and check the quoted clause is really there, really says what is used, and its
   hypotheses are really satisfied at the point of use.
3. EXHAUSTIVENESS: is every counterexample instance routed to exactly one path?
   Boundary ownership at every split? Any uncovered configuration?
4. WALL VIOLATIONS: does any leaf or assembly step secretly route through
   (lambda,Phi_v)-pairings alone (Prop-D wall, context/l2-attack.md §2.4)? Any W55
   dead route (lambda*P = p_v identification; dual multipliers as transition mass;
   thin/thick single-moment split; untyped "some web member is exposed")? Any
   quantification over mutually-rho-far families (B6 scale gap)? Any raw-index /
   clone-variant quantity? Any use of a status:conjecture shard as a premise?
5. RESTATEMENT TEST, adversarially: for each leaf, try to DERIVE SL1a (or L2-core, or
   the huddle charge) from that leaf alone in one or two lines. If you can, the leaf
   is a restatement and the decomposition FAILS its objective.
6. RED TESTS, re-run yourself (do not trust the recorded outcomes): (a) Proposition E
   two-point counterweight; (b) the W55 exact starvation gadget A0=5, g=5*tau — for
   each leaf, does the gadget (or its co-top analogue) satisfy the leaf's hypotheses,
   and does the recorded answer hold? (c) clone splitting + transient-row extension
   stability of every leaf; (d) the known-family coverage claims in §5.
7. TIER GRADING HONESTY: for each EASY/MEDIUM leaf, is the exhibited mechanism really
   plausibly routine, or is hardness hidden (e.g. an innocuous-looking "select" or
   "there exists a vertex representation such that" that smuggles the whole problem)?
   At most ONE leaf may be HARD, and it must come with a strictly smaller
   configuration space (check the claimed removal is real) and a one-level-deeper
   decomposition sketch (check it is not vacuous).
8. VACUITY: could a leaf be vacuously true (empty hypothesis class) or vacuously
   unusable (hypotheses never satisfiable in the assembly's context)?

Write your findings INCREMENTALLY to `VERDICT-W56.md` in the workspace root:
numbered findings, each with severity (FATAL / MAJOR / MINOR / NOTE), the exact
location (section + quoted line), and the concrete failure (for arithmetic: the
numbers; for gaps: the missing step; for restatements: the one-line derivation).

Your FINAL MESSAGE must be exactly: first line
`VERDICT: <VALID | VALID-WITH-CORRECTIONS | INVALID — one-sentence qualifier>`,
then a one-paragraph justification, then (if VALID-WITH-CORRECTIONS) the numbered
list of REQUIRED corrections, each one concrete enough to apply mechanically.
