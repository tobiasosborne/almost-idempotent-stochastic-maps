You are a research mathematician resuming an INTERRUPTED decomposition task. Your
workspace is self-contained; everything you need is in the current directory. Work
entirely inside it.

## THE SITUATION

A previous architect (killed mid-run, not for any mathematical fault) was executing the
task specified in `target.md` (READ IT FIRST — its STATUS DISCIPLINE, HARD CONSTRAINTS,
MANDATORY RED TESTS, and DELIVERABLE FORMAT are all binding on you verbatim). It
completed §1 (pinned target + proved-input audit) and §2 (a candidate DAG shape) of
`DECOMPOSITION.md`, leaving §3 (THE LEAVES), §4 (THE ASSEMBLY), §5 (COVERAGE CHECK),
§6 (HONEST ASSESSMENT) as stubs. The file `decomposition-PARTIAL.md` is the frozen
copy of that partial; `DECOMPOSITION.md` is your working copy (currently identical).
The previous worker's full session log is `prior-architect-session-log.txt` — it may
contain useful leaf reasoning beyond what §1-§2 record; mine it, but treat everything
in it as AUTHOR-CLAIM draft, not established.

## YOUR TASK

Complete `DECOMPOSITION.md`: write §3, §4, §5, §6 per target.md's DELIVERABLE FORMAT,
editing §1-§2 wherever your completed leaves require it. The deliverable is judged as
ONE document — a fresh hostile verifier will attack the final file with no knowledge
of the interruption.

## CREATIVE LICENSE (new user directive, binding)

You are NOT bound to the inherited §2 DAG shape (L-S selector -> L-V same-carrier
reproduction -> L-P discard/horn split -> H-SCCO). It is a candidate, not a
commitment. THINK OUTSIDE THE BOX:

- If while writing the leaves you find the inherited shape forces a restatement leaf,
  an unprovable constant, or a wall violation, REDESIGN the DAG — partially or wholly —
  and say so in §6 (one line on what you replaced and why).
- Actively consider unconventional mechanisms before settling: exact idempotence used
  at UNUSUAL rows (web rows, carrier vertices, zero-face rows — not just v); LP-duality
  run in the OPPOSITE direction (infeasibility certificates as objects); global
  completion/factorization obstructions (P = L*B, B*L = I); extremal/variational
  selection of the counterexample (minimal delta, minimal web mass, extreme barycenter)
  and what stationarity forces; perturbation/exchange arguments that move mass and
  track delta exactly; induction on the number of geometrically distinct row vertices.
- The goal metric is SURFACE REDUCTION: every leaf strictly smaller than SL1a, as many
  EASY/MEDIUM as possible, at most ONE flagged HARD leaf with its own
  further-decomposition path sketched one level down.
- Creativity is NOT license to violate the banked walls: the HARD CONSTRAINTS in
  target.md (Prop-D pairing wall, W55 dead routes, B6 scale gap, clone-invariance,
  explicit constants) and the dead-route certificates in context/FINDINGS.md remain
  absolute. Out-of-the-box means NEW mechanisms, not re-walking certified dead ones.

## NON-NEGOTIABLE DISCIPLINE (from target.md, restated)

- Only `status: proved` shards in `argument/` are usable premises; quote the consumed
  clause verbatim at the point of use, with the shard id.
- `status: conjecture` shards are OPEN; never premises (unless a leaf is explicitly
  conditional and says so in its statement).
- Every statement dimension-free and clone-invariant (row points / distinct row
  vertices / coefficient-mass sums; never raw index counts).
- Every constant explicit, tied back to SL1a's verbatim constants with conversion
  arithmetic in §4.
- Run every leaf and the assembly against ALL the MANDATORY RED TESTS in target.md and
  record each outcome in §3/§5.
- Apply the RESTATEMENT TEST to every leaf and record the verdict.

## PROCESS

1. Read target.md fully. Read DECOMPOSITION.md §1-§2. Read context/l2-attack.md (the
   key prior art), then the other context/ docs as needed per target.md's RESOURCES
   order. Consult argument/ shards as you cite them (140 shards; grep by id).
2. Mine prior-architect-session-log.txt for the dead worker's §3 draft reasoning.
3. Write §3-§6 INCREMENTALLY into DECOMPOSITION.md (small edits, save often — do NOT
   hold the document in your head for one big write).
4. Self-check pass: re-verify the assembly's constant arithmetic line by line; check
   §2's tree matches the final leaves; check every red test has a recorded outcome.

Your FINAL MESSAGE must be exactly: first line
`VERDICT: <DECOMPOSED-ALL-TIER2 | DECOMPOSED-WITH-ONE-HARD | BLOCKED — one-sentence qualifier>`,
then one paragraph summarizing the final DAG shape and leaf count, and (if you
redesigned) one sentence on what changed versus the inherited §2.
