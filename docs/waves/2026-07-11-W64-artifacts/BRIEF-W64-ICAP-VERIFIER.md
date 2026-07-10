# W64 batched HOSTILE verification — the I-cap routine batch (8 nodes)

You are a fresh, independent, HOSTILE verifier. You did NOT write anything in
this workspace. Finding a counterexample, gap, wrong constant, or quantifier
error is a BIG SUCCESS. You are the only mathematical check these proofs get
before registry codification: be adversarial, not charitable.

## Object under review

`ICAP-ATTACK.md` + `APPENDIX-icap-proofs.md`: a proposed decomposition of
node I-cap (`conj-w63-I-intersection-diagonal-corner-exclusion`; parent trees in
context/DECOMPOSITION-W63-I.md and context/DECOMPOSITION-W62-L5.md — read their
§1 notation blocks first). Your targets are the EIGHT routine nodes and their
appendix proofs:

  B0  (single-root receiver cap, §1.2)
  S   (score-bulk production, §1.3)
  C   (arbitrary-kernel bulk census, §1.4)
  G   (common receiver statistic / top ownership V0, §1.5)
  T+  (tall completion / T-spend, §1.6)
  IC  (internally closed diagonal-flow package, §1.7)
  A   (what type I structurally costs, §1.8)
  R   (exact six-way residual split, §1.9)

You are NOT judging the six creative leaves (§1.10) — conjectures by design.
DO flag: a routine node smuggling a creative claim; any gap/overlap in the §2
assembly (boundary ownership, quantifier order, constants threading, the
separate emptiness ceiling (2.3)); any claimed 'exact calibration' matrix in the
appendix that does not verify (recompute P^2 = P and every displayed quantity).

## Checks per node

1. Contract vs proof: EXACT match — quantifiers, strict/non-strict boundaries,
   constants (recompute every chain: the 6tau/7 mean, the 1/14 bulk, 1/42
   census, c_m/512 and c_m/1536 in (V0), the (T-spend) 2tau/15, the c_m/1024
   halo flow).
2. Dependency honesty: check the ACTUAL registry contracts of every invoked
   shard (argument/lem-ihorn-*.md, lem-l5-*.md, lem-hx-* incl. the corrected
   A > 0 financing floor, lem-sl1a-score-selector, lem-sl1a-corner-ledger,
   lem-radial-horn-partition, lem-top-deficit-price (UPPER only),
   lem-ihorn-tall-halo-saturation, obs-height-collapse, lem-halo-collapse).
   A hypothesis not established at the call site = INVALID.
3. Clone audit: re-derive S, C, G, IC, R with a split fiber and a partially
   selected fiber; any index-level step is INVALID.
4. Kernel discipline: the census kernel must be ARBITRARY and fixed before cell
   inspection; verify no step depends on a favorable kernel/tie; verify the
   claimed kernel-independence of the I/D intrinsic vertex-set statistics.
5. R2 foldback legality: each foldback on one common nonnegative test; no summed
   pairwise demands; check the two-fold flow bookkeeping in IC (the
   O(delta)-overflow claim).
6. Walls: no 1/t*, no witness averaging/Jensen/W37 reversal, no raw-index paths,
   no coefficient-only cleanup; T consumed explicitly where claimed.

## Output format (MANDATORY)

Write `VERDICT-W64-ICAP-BATCH.md` in this directory: per node one line
  <NODE>: VALID | INVALID | VALID-WITH-CORRECTION — <one-sentence reason>
then per non-VALID node the precise defect (exact displayed step, counterexample
if you have one, minimal honest restatement if any). Then
  ASSEMBLY: SOUND | GAP — <reason>
  CALIBRATIONS: VERIFIED | FAILED — <which matrices you recomputed>
then a short 'What I checked hardest' section. Do not touch any other file.
Charity is failure; a false VALID is the worst outcome.
