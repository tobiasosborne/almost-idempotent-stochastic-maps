You are a research mathematician performing a careful EXTRACTION-AND-REPAIR pass. Your
workspace is self-contained; work only in it.

## THE SITUATION

`DECOMPOSITION-v2.md` is a decomposition attempt on the conjecture SL1a
(`conj-straddling-web-exclusion`; pinned verbatim in `target.md`, whose STATUS
DISCIPLINE and HARD CONSTRAINTS bind you). It was judged INVALID by a hostile verifier
(`VERDICT-W56-R2.md`, 15 findings) — as was its predecessor (`DECOMPOSITION.md`,
verdict `VERDICT-W56.md`). The INVALID verdicts concern the HARD-leaf objective; both
verifiers explicitly CONFIRMED substantial routine material by independent
re-derivation. Your job is to extract that confirmed material into standalone
registry-shard drafts, applying the verifiers' corrections, so it can be banked and
the residual surface codified honestly. You are NOT asked to fix the hard leaf.

## WHAT TO EXTRACT (guided by the verdicts; re-derive everything yourself — if you
## cannot complete a proof honestly, mark the shard BLOCKED and say exactly where)

A. PROVED-CANDIDATE lemma shards, each with a fully self-contained statement AND
   complete proof (consuming only `status: proved` registry shards in `argument/`,
   quoted verbatim at point of use, plus elementary arguments):
   1. The affine barycenter identity of §1.0 — WEAKENED per round-2 finding 7: affine
      integrals only; delete the false "interchangeable in every statement" claim.
   2. L-M's well-definedness content per round-2 finding 11 ONLY (the clone-invariant
      integers (V,R) exist, are finite, lex-minimum attained, clone splitting
      preserves them) — IF you judge it independently reusable; otherwise drop it
      (minimality itself is a certified dead route — do not build on it).
   3. L-S (score selector), as a standalone lemma: hypotheses = SL1a counterexample
      data, conclusion = the selected-row existence with its exact constants.
   4. L-C (coupled coefficient-kernel corner): the Gamma_f(C_f) > 1/2 ledger with the
      exact constants both verifiers re-derived; universal over legal kernels
      (round-2 finding 13's accepted formulation).
   5. L-P (radial horn partition), with the corrected Proposition-E red-test wording
      (round-2 finding 15) and boundary ownership.
   6. H-D1 (the capacity kill: c_r >= 1/16 shipping forces tau >= 1/64, contradicting
      tau <= 1/256).
   7. THE REDUCTION LEMMA (the wave's main prize): a conditional lemma in the form
      "if [the three cell-exclusion conjectures below] then SL1a", assembled exactly
      as §4's derivation + §2.1's existence-plus-universality routing (accepted by
      round-2 finding 13), with the finding-8 constant correction (7/13 vs 7/100 —
      recompute honestly) and every constant tied to SL1a's verbatim ones.
   Apply ALL relevant MINOR corrections from both verdicts. Do not include anything
   that either verdict killed (the antipode, minimality-as-hypothesis, the censoring
   step, the H-I recursion, the H-D far-side max-principle channel).

B. CONJECTURE shards for the three residual cells (H-D, H-I, H-X of §3), each as a
   SINGLE minimal fully-quantified contract (one sentence, one mathematical statement,
   no 'hence' clauses, no compound corollaries — af-elevation style), with the
   round-2 finding-9 repair: refuter criteria must demand delta -> 0 families, not
   single instances. Strip any hypothesis the verdicts showed unused (the horn label
   where its consumer was judged aspirational — round-2 finding 10 — unless the cell
   statement genuinely needs it; decide per cell and record why). The three cells
   must still visibly partition the residual: state the partition in the reduction
   lemma's proof, not inside the cell contracts.

C. `extraction/DEAD-ROUTES.md` — draft FINDINGS.md entries (dated 2026-07-10, with
   one-line death certificates citing the verdict finding numbers) for: (i) the
   one-hard-leaf-after-free-preprocessing objective (any retained-class terminal leaf
   is a restatement — r1-F1, r2-F1); (ii) lex-(V,R) minimal-counterexample
   stratification (free preprocessing, unused minimality, transient-row instability —
   r2-F1/F3/F11); (iii) lem-censoring-exactness at freight-row blocks without the
   ||A|| < 1 hypothesis (r2-F4); (iv) second-generation L-C recursion (hypotheses
   unsatisfiable at second web rows — r2-F5); (v) the max-principle far-side return
   channel (sign unconstrained off T(u); = the W55 carrier-coincidence obstruction —
   r2-F6).

## FORMAT

`argument-README.md` is the registry shard schema; existing shards in `argument/` are
examples. Write ONE file per shard in `extraction/`: `lem-<slug>.md` /
`conj-<slug>.md` with front matter (id, contract = the one-line statement, defs, deps
(the proved shards consumed), status: proved-candidate or conjecture, owner: W56-extraction)
and body (statement, full proof for lemmas, notes). Choose short descriptive slugs
(e.g. lem-sl1a-score-selector, lem-sl1a-corner-ledger, conj-sl1a-deep-diagonal-cell...).
Every statement dimension-free and clone-invariant; every constant explicit. Write
INCREMENTALLY (small writes).

## STATUS DISCIPLINE

Everything you write is AUTHOR-CLAIM. A separate fresh hostile verifier will attack
each extracted proof with no memory of this exchange; write each shard so it survives
alone (self-contained, no references to "the document" or "§4" — inline what you
need).

## FINAL MESSAGE (raw data for the orchestrator)

First line exactly: `EXTRACTED: <n> lemma drafts, <m> conjecture drafts, <k> BLOCKED`
then one line per shard: `<filename> — <one-line contract> — <OK|BLOCKED: reason>`.
