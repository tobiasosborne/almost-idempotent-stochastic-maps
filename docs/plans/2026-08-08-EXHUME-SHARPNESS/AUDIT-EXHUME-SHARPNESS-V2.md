VERDICT: REJECT

1. **FATAL — the claimed 50-locus manifest is still not closed: it omits a
   live canonical definition that attributes sharpness to the historical 3x3
   family.**  The closure claim is at
   `DESIGN-EXHUME-SHARPNESS-V2.md:31-49,551-633`, and the proposed landing
   sweep is at lines 748-799.  But
   `definitions/def-near-positive-projection.md:24-25` is a locked canonical
   shard and still says that the square-root exponent for near-positive-
   projection stability “is sharp (Hume's 3x3 family).”  Its generated report
   twin repeats that assertion at
   `report/generated/defs/layer-1-classical-picture.tex:448-449`.  Neither is
   one of loci 1-50, and merely regenerating the definitions layer cannot
   repair an unchanged source definition.  This is active, unqualified prose,
   not an exact historical quote, a matrix-family-only/non-import annotation,
   or a `disproved` status record.  It therefore also violates the design's
   own survivor test at lines 780-786 and its requirement at lines 767-771 to
   remove the uncitable eponym from active prose.  More substantively,
   `cor-classical-sharpness` proves sharpness in the stochastic defect
   parameter `eta`; it must not silently be substituted as a certificate for
   the definition's signed near-positive-projection `delta` statement.  The
   source definition needs an honestly scoped removal or non-rigorous
   historical qualification, with the generated twin refreshed and the
   definition-change/consensus implications expressly ratified.  Thus the
   advertised 50/50 census has at least a 51st canonical source locus, and
   executing the package exactly would leave the rigorous record internally
   inconsistent.

2. **CLEARED — round-1 finding 1 is repaired completely, and the literal
   counterexample checks.**  The proposed `ex-hume` shard at
   `DESIGN-EXHUME-SHARPNESS-V2.md:267-325` binds `0<s<1`, defines all four of
   `v_s,u_s,P_s,delta_s`, quantifies the claimed equality over every 3x3
   stochastic idempotent, specifies `s->0` for the big-O assertion, and binds
   `C,beta,s` in the final negative clause.  The out-of-scope `op-npps` clause
   is absent from the new contract and survives only inside the visibly
   historical quote.  That quote at lines 289-290 is byte-identical to the
   current `argument/lemmas/ex-hume.md:4` contract after stripping the
   frontmatter key.

   Independently, for `a=1-s+s^2`, one has `a-s=(1-s)^2>=0` and
   `||v_s||_1=2`; hence
   `||u_s v_s^T||_{infinity->infinity}=2 max{a,s}=2a`.  Also
   `v_s^T 1=0` and `v_s^T u_s=1`, so `P_s 1=1` and `P_s^2=P_s`; direct
   expansion shows that its only negative entry is `(P_s)_{23}=-s^2`.
   Since `I_3` is a stochastic idempotent,
   `||P_s-I_3||=2a`, whereas the claimed common value is `2sa`; their
   difference is exactly `2(1-s)a>0`.  The proposition is therefore false
   for every `0<s<1`, exactly as the body, proposed `docs/LEARNINGS.md` entry,
   and proposed dated `FINDINGS.md` record state.

3. **CLEARED — `disproved` is legal, unavailable to rigorous consumers, and
   terminal here.**  `scripts/argument.py:51-52` includes `disproved` in
   `MATH_STATUS`; `argument/README.md:30,66` documents it.  The availability
   rule at `scripts/argument.py:198-229,278-281` admits only
   `af: validated` or `status: cited`, explicitly excluding `disproved`, and
   the ready rule admits only `proved`/`consensus`.  Thus the proposed
   `disproved`/`af:none` row is neither an available premise nor a proof target.
   `python3 scripts/argument.py --show ex-hume` reports zero direct dependents
   and zero descendants; an independent search found no `deps:` or `routes:`
   edge to `ex-hume`.  In particular no T0 row depends on it.  The current
   `op-classical` and `thm-rank-one` wiki links are body prose, not DAG edges,
   and the v2 package repairs those pointers without adding an import.

4. **CLEARED SUBJECT TO FINDING 1 — every one of the design's enumerated 50
   actions is accounted for, and the sensitive consumer edits are properly
   bounded.**  The arithmetic of the table at
   `DESIGN-EXHUME-SHARPNESS-V2.md:551-633` is 20 non-report loci, 26 report
   shards, paper section 5, `INDEX.md`, and two registry annotations, totaling
   50.  The report list is exactly sections 00, 02, 20, 23-29, 34-38, 41-44,
   46, 48, 49, 49b, 50, 51, and 51b.  `AGENTS.md` and `CLAUDE.md` are presently
   byte-identical (matching SHA256), and loci 1-2 prescribe the same replacement
   plus an explicit `cmp` check.  The `thm-rank-one` old/new pair at
   `argument/lemmas/thm-rank-one.md:4,14` and v2 lines 327-344 removes exactly
   the false “sharp family” clause, leaves its other fields/status unchanged,
   and is repeatedly flagged for explicit user ratification.

   For the validated `op-classical` shard, loci 12-16 and the complete block at
   v2 lines 659-699 change only provenance/body pointers.  They leave the
   contract, `defs`, `deps`, `routes`, status, af state, owner, workspace, and
   ledger untouched, while preserving the W80 assignment as visibly
   superseded history.  The numerical `INDEX.md` anchor,
   `lem-signed-carre-du-champ` fixture, and
   `lem-routef-f0-assembly` negative reference receive the required explicit
   historical-matrix/non-import annotations.  Historical plans, audits,
   waves, run bundles, frontier/bead logs, and `docs/worklog.md` may remain
   historical.  The failure is not within these 50 dispositions; it is the
   omitted canonical definition in finding 1.

5. **CLEARED — all audit-cleared v1 mathematical/elevation material is
   preserved.**  Direct byte comparisons show that the complete
   `lem-prh-sharpness` landing text, complete `cor-classical-sharpness` landing
   text, verified-constants table body, both af skeletons, both seeding
   packages, the 20-item fact census, Stage B, and Stage C items 1-3 are
   byte-identical between v1 and v2.  The elevation-order/stop-rule content is
   also byte-identical; only its heading gained the required `(g)` label.  The
   workspace deletion sentence is preserved at v2 lines 323-325, and the
   paper-section-5 action is preserved verbatim at lines 772-777.  The declared
   changes are confined to the three audit repairs, the required
   `thm-rank-one` consumer correction, and associated manifest/status prose.

6. **CLEARED — the corollary, dependency boundary, seeding, and fact census
   survive the standard battery.**  The contract at
   `DESIGN-EXHUME-SHARPNESS-V2.md:212-266` has the order
   `for every C,eta_0,beta>1/2; there exist eta,Q; for every E`, lands honestly
   as `stated`/`af:none`, and has the single package dependency
   `lem-prh-sharpness`.  Its witnesses are the same existential `A_lambda,
   M_lambda` throughout.  With probability-vector rows, `||A||=||M||=1`,
   `Q=AM` is row-stochastic, and
   `Q^2-Q=A(MA-I_2)M`, giving defect at most `2 lambda^2`.  Choosing
   `lambda<(C 2^beta)^(-1/(2 beta-1))` gives the strict
   `C eta^beta<lambda` inequality, while the other two cutoffs give
   `eta<eta_0` and `eta<1/4`.  This is a concrete mathematical negative, not
   meta-quantification over proofs.

   The current `lem-prh-sharpness` registry contract, the proposed root, and
   the proposed external source are byte-exact.  The external uses the literal
   `proofs/lem-prh-sharpness` path and is registered only after its provider is
   T0.  The census covers matrix products, max-row-l1 norm, norm one,
   submultiplicativity, the self-contained row-coincidence proof, scalar real
   powers, and dependency-witness identity.  No infimum-over-a-set fact or
   signed/stochastic bridge is consumed by either target; the corrected 3x3
   distance-to-set candidate remains explicitly off-path.

7. **CLEARED — skeleton counts, caps, order, and the paper action are
   consistent.**  The first skeleton has 8 designed nodes and the second 6;
   their 3x endpoints are respectively 24 and 18, strictly below caps 26 and
   20.  The elevation order is re-audit, user ratification, retraction landing,
   first-target validation/banking, dependent-corollary validation/banking,
   then Rule-9 closure.  The no-resume rule for `proofs/ex-hume` and the
   staged T0 timing are explicit.  The paper action replaces the current
   non-T0 3x3 proof in `paper/main.tex:289-317` with the banked 4x4 family and
   quantified corollary, and changes the footnote at lines 70-76 from
   “sharpness ... human audit” to af-validated sharpness while retaining the
   truthful no-Lean boundary.  This agrees with round-1 finding 7 and the two
   contracts that would land.

8. **Round-1 and mandatory-attack disposition.**  Round-1 finding 1 is fully
   repaired (findings 2-3 above).  Round-1 finding 3 is fully repaired by the
   exact counterexample plus both dated records.  The mathematics and package
   mechanics cleared in round-1 findings 4-7 remain intact (findings 5-7
   above).  Round-1 finding 2 is repaired at every locus it originally named,
   but its underlying manifest-closure defect survives at the newly exposed
   canonical definition in finding 1; that one fatal survivor controls the
   verdict.  All ranked risks other than supersession/manifest closure survive
   attack: witness identity, row coincidence, direct defect, strict
   inequalities, workspace deletion, off-path 3x3 constants, and tree
   expansion are correctly handled.  The design must be revised and freshly
   re-audited before any sharding, seeding, promotion, or registry mutation.
