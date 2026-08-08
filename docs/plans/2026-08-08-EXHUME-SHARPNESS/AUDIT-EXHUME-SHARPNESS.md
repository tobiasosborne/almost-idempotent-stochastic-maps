VERDICT: REJECT

1. **FATAL — the proposed changed `ex-hume` shard fails the mandatory
   contract-quantifier audit.**  At
   `DESIGN-EXHUME-SHARPNESS.md:165-209`, especially the proposed contract at
   line 176, `s` has no domain or quantifier, `C` and `beta` are not
   quantified, the limiting variable in `O(delta)` is unstated, and the
   out-of-scope identifier `op-npps` remains in the canonical contract.  The
   design itself admits the omitted domain at lines 186-190, but nevertheless
   proposes retaining that malformed contract verbatim.  Marking an ambiguous,
   unbound sentence `disproved` does not turn it into a complete mathematical
   proposition.  This directly violates the audit brief's requirement that
   every symbol in every new/changed shard be bound.  A landable retraction must
   make the false proposition precise (including `0<s<1` and the literal
   per-idempotent equality/quantifiers), keep the old wording as a quoted
   historical record in the body, and then exhibit the counterexample.  This
   repair changes the design's explicit “contract retained verbatim” decision
   and therefore requires redesign/re-audit rather than an implementation-time
   improvisation.

2. **FATAL — the landing manifest is not closed under the `ex-hume`
   retraction, so executing it exactly leaves active canonical text asserting
   that a `disproved` row certifies sharpness.**  The incomplete sweep is at
   `DESIGN-EXHUME-SHARPNESS.md:416-500`.  In particular:

   - The manifest names `PRD.md`, `HANDOFF.md`, `README.md`, and only “any
     `FINDINGS.md` 2026-08-08 sharpness pointer” at lines 480-487.  It omits the
     current assertions in `AGENTS.md:105`, `CLAUDE.md:105`,
     `CONVENTIONS.md:57`, `FINDINGS.md:36-37`,
     `RESEARCH_NOTES.md:97,145`, and `refs/manifest/SOURCES.md:25,84`.
     `AGENTS.md` and `CLAUDE.md` must also remain byte-identical.
   - The registry itself has uncovered live consumers.  The nonvalidated
     `thm-rank-one` **contract** at `argument/lemmas/thm-rank-one.md:4` and its
     body at line 14 call `ex-hume` a sharp family.  The validated
     `op-classical` shard has a stale provenance assertion at
     `argument/lemmas/op-classical.md:10` and current-carrier assertions at
     lines 20-22, 28-29, and 33-35 (line 38 is historical but must remain
     visibly historical).  Design lines 457-461 authorize only “one body
     sentence,” which cannot repair all of these loci.  No validated contract
     or dependency needs to change, but all current body/provenance pointers do.
   - The ingest treatment is also incomplete.  Design lines 429-431 update
     only the `ex-hume` re-tag row, while `docs/ingest/README.md:114` still calls
     the family sharp through `thm-rank-one`, line 119 contains the false old
     quantifier, line 297 calls `ex-hume` the sharpness certificate, and
     `docs/ingest/OVERVIEW.md:98` says the now-disproved registry row refutes an
     `O(delta)` full-distance strengthening.
   - The report sweep itself is complete: the current direct hits are sections
     00, 02, 20, 23-29, 34-38, 41-44, 46, 48, 49, 49b, 50, 51, and 51b, exactly
     the set covered by design lines 465-479; `UNWIRED`, generated DAG, and
     generated statistics are also covered by lines 470-475 and 494-497.
     Historical plans/audits/waves, `.frontier`, `.beads`, `docs/worklog.md`,
     and the numerical run bundles may remain historical.  The numerical
     anchor at `INDEX.md:27`, the fixture provenance in
     `lem-signed-carre-du-champ`, and the negative statement in
     `lem-routef-f0-assembly` remain truthful if explicitly understood as
     historical matrix-family references, not as imports of the false
     sharpness contract.

   Consequence: after the proposed Stage D, the repository would still have
   mutually inconsistent canonical statements and would violate Rule 9.  This
   is not a documentation nicety: one omitted locus is another registry
   contract (`thm-rank-one`).

3. **HIGH — the literal falsity diagnosis is mathematically correct, but the
   proposed provenance disposition is only partially complete.**  For
   `0<s<1`, write `a=1-s+s^2`.  The displayed vectors satisfy
   `v_s^T 1=0` and `v_s^T u_s=1`, so `P_s=I-u_s v_s^T` has `P_s1=1` and
   `P_s^2=P_s`; its only negative entry is `(P_s)_{23}=-s^2`, hence its
   maximal row negative mass is exactly `s^2`.  But the stochastic idempotent
   `I_3` has
   `||P_s-I_3||_{infinity->infinity}=||u_sv_s^T||=2a`, whereas the old claimed
   value is `2sa=2s-2s^2+2s^3`; their difference is
   `2(1-s)a>0`.  Thus the literal assertion that the distance to *each*
   stochastic idempotent equals one common value is false.  The plan correctly
   deletes the stale `proofs/ex-hume` root (`DESIGN:205-209,421-424`), appends a
   `docs/LEARNINGS.md` retraction (`DESIGN:425-428`), and preserves the explicit
   3x3 matrices plus the corrected distance-to-set statement only as an
   unproved candidate (`DESIGN:192-198`).  It does not, however, explicitly
   require the dated `FINDINGS.md` record demanded by the audit brief, and its
   partial citation sweep leaves the historical family misdescribed elsewhere
   as detailed in finding 2.

4. **CLEARED — the 4x4 witness arithmetic and the every-idempotent lower bound
   are exact.**  From `PROOF-W74F-A-PRH.md:402-498`, with state order
   `(x_1,x_2,y_1,y_2)`,
   `A` has rows `(1,0),(0,1),(1-lambda,lambda),(lambda,1-lambda)` and `M` has
   rows `(1-lambda,0,lambda,0)` and `(0,1-lambda,0,lambda)`.  Hence
   `MA=[[1-lambda^2,lambda^2],[lambda^2,1-lambda^2]]` and, using the induced
   infinity norm as maximum row l1 norm,
   `||MA-I_2||=2lambda^2` exactly.  For `P=AM`, rows `x_1` and `y_1` are
   `mu_1` and `(1-lambda)mu_1+lambda mu_2`; the decoder supports are disjoint,
   so their l1 distance is `2lambda`.  If a stochastic idempotent `F` had
   `d=||P-F||<lambda`, then
   `f_{x_1x_1}>1-2lambda>0` and `f_{x_1y_1}>0`.  The row-coincidence lemma is
   valid: the support of row `x_1` is closed and has no inter-SCC edge under
   its positive stationary distribution, hence is one irreducible class with
   a unique stationary probability; therefore the `x_1` and `y_1` rows of
   `F` coincide.  The two row errors then give `2lambda<=2d`, a contradiction.
   Thus every `F` satisfies `||AM-F||>=lambda`.  This agrees with
   `VERDICT-W74F-BATCH.md:78-94` and independently survives audit.

5. **CLEARED — the stochastic defect computation, constants, directions, and
   negative exponent quantifiers are correct and af-dischargeable.**  The maps
   have probability rows, so `||A||=||M||=1`, `Q=AM` is row-stochastic, and
   associativity gives
   `Q^2-Q=A(MA-I_2)M`; submultiplicativity yields
   `||Q^2-Q||<=2lambda^2`.  Direct row arithmetic in fact gives equality, but
   the weaker direction in `DESIGN:133-144,304-312` is exactly what is needed.
   Given `C>0`, `eta_0>0`, and `beta>1/2`, choosing
   `0<lambda<min{1/(2sqrt(2)),sqrt(eta_0/2),
   (C*2^beta)^(-1/(2beta-1))}` and setting `eta=2lambda^2` gives
   `0<eta<min{eta_0,1/4}` and
   `C eta^beta=C*2^beta*lambda^(2beta)<lambda`.  Combined with the same
   witnesses' lower bound, this has the exact order
   `forall C,eta_0,beta>1/2; exists eta,Q; forall E` and refutes the proposed
   uniform estimate without quantifying over proofs or relying on a
   meta-level asymptotic assertion.  A verifier challenge based on actual
   defect versus the chosen upper-bound parameter also fails: the family
   satisfies the required `||Q^2-Q||<=eta` (indeed equality).

6. **CLEARED, subject to findings 1-2 — the new corollary's own registry
   wiring, seeding package, and budgets are sound.**  The proposed
   `cor-classical-sharpness` contract at `DESIGN:117-126` binds its mathematical
   variables, lands honestly as `stated/none`, has the single acyclic
   dependency `lem-prh-sharpness`, and is seeded only after that dependency is
   validated.  No validated row's contract or dependencies are edited.  The
   external source at `DESIGN:369-377` contains the literal
   `proofs/lem-prh-sharpness` path and the byte-identical frozen contract.  The
   designed counts are exactly 8 nodes and 6 nodes; their 3x endpoints are 24
   and 18, strictly below caps 26 and 20.  The fact census covers the explicit
   products, maximum-row-l1 norm, norm-one/contractivity, row-coincidence
   argument, scalar powers, and first-order witness reuse.  No
   infimum-over-a-set fact is consumed by either af target; the proposed 3x3
   distance-to-set equality is correctly quarantined rather than seeded.

7. **CLEARED — the paper action is mathematically consistent.**  Current
   `paper/main.tex:289-317` presents the corrected 3x3 distance-to-set formulas
   as the proof of sharpness, while its footnote at lines 70-76 says sharpness
   has only human audit.  Design lines 488-493 correctly require replacing that
   proof with the validated 4x4 PRH family plus the fully quantified corollary,
   changing the footnote to af-validated sharpness while retaining the truthful
   “no Lean/mathlib proof” boundary.  The old 3x3 formulas may be omitted or
   kept only as an explicitly non-T0 historical candidate.  The explanatory
   paragraph at `paper/main.tex:319-325` remains compatible with the 4x4
   witness because that witness makes the PRH square-root loss sharp directly.

8. **Risk ledger.**  Design risks 1, 2, 3, 4, and 9 survive the mathematical
   attacks (findings 4-5); risk 6 is correctly handled by deleting, never
   resuming, the stale workspace; risks 7 and 8 are correctly kept off the T0
   path; risk 11 has adequate cap headroom.  Risks 5 and 10 fail because the
   supersession/status sweep is incomplete (finding 2), and the changed
   `ex-hume` contract independently fails mandatory registry hygiene
   (finding 1).  Those failures are fatal even though the replacement 4x4
   mathematics is sound.
