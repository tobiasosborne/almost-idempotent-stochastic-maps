# HOSTILE AUDIT — consumer-chain repair

**Date:** 2026-08-01

**Auditor role:** fresh independent hostile auditor; not the design author.

**Epistemic status:** audit only; non-rigorous. No registry, definition, proof
workspace, status, report, script, or source is changed.

**Final disposition:** **DESIGN-REFUTED / DO NOT RATIFY AS WRITTEN.** The two
one-dimensional-image insertions and the proposed typed M19-R conclusion are
mathematically well-shaped. The design nevertheless (i) confirms a serious
latent gap in banked M25, (ii) recommends the more invasive option without
charging the cascade correctly, (iii) falsely attributes dependency-contract
staleness to `check-refs.py`, (iv) misses direct monotonicity and scalar-provider
imports in M26/M28, and (v) misses the same unimported monotonicity inference in
the already banked M19-S2 and M19-S3 certificates. The last item expands the T0
repair beyond the brief's frozen-row scope and requires user escalation.

## F1 — SERIOUS: M25's banked validation has a genuine latent gap

The design is correct on the priority question. In
`proofs/lem-maincb-one-class-extension/export.md`, node `1.1.2.2` says that
M19-R preserves bijectivity, "so" the output is a current reset isomorphism;
node `1.1.3.2` says the output is "bijective and hence an extended
isomorphism." Neither inference is valid from the registered external.

The locked `def-extended-delta-inclusion` makes an extended isomorphism a
bijective **extended inclusion**. The data-only `def-maincb-reset-state`
separates the recorded number `d_R` from the supplied inclusion/isomorphism
tag. Old M19-R exports only the number bound, unit bound, conditional
bijectivity, and unchanged signature/amplifications. It does not export an
extended-inclusion assertion. M25 imports exactly that old root contract in
`externals/25114e693d8262b4.json`; it does not import M19-R's internal node
`1.2`, where the M02 iterate is in fact typed as an extended
`K_floor*epsilon_R`-inclusion.

**Exact correction:** immediately treat M25 as non-rigorous pending repair;
freshly re-seed/re-validate it with a provider that exports the same output map
as an extended inclusion/isomorphism. Replace both invalid steps by direct
applications of that exported typed conclusion. M25's root contract need not
change. This is not bookkeeping: the current banked certificate does not prove
its root from its registered premises.

## F2 — MAJOR: reverse the strengthen-versus-bridge recommendation

The design's comparison hides the common and differential costs. Once F1 is
accepted, **both** options pay for M25 demotion/re-validation. The remaining
comparison is:

| Cost | Strengthen M19-R | New same-witness bridge |
|---|---:|---:|
| M25 repair | common | common |
| typed-provider proof | re-validate a demoted banked M19-R | validate one new row |
| M18 import | manual external refresh/audit | untouched |
| canonical provider | improved | old provider remains under-typed |

The proof burden of the new row is essentially the M19-R re-validation burden,
but it avoids mutating a banked provider and avoids touching M18. Under this
round's conservative frozen-T0 constraint, the bridge is therefore the lower
risk recommendation. Canonical-provider cleanliness is real, but it is not
worth the extra banked-contract cascade in this scoped repair.

**Exact correction:** leave M19-R and M18 byte-unchanged; add
`lem-maincb-reset-output-typing`, a new typed-reset row whose one-line contract
is the design's proposed strengthened M19-R contract verbatim:

```text
contract: After first fixing the universal e_it,K_disp,K_floor witnesses of lem-maincb-improvement-iteration and epsilon_max^cb,delta_max^cb,c0^0 witnesses of lem-maincb-error-improvement, there are universal 0 < C_unit < infinity and epsilon_unit,delta_unit,a_unit > 0 furnished by the third clause of prop_delta_hominc and its implicit quantifier convention such that, for every D >= 1 and every def-maincb-witness-ledger datum W with W.c0_cb >= max{c0^0,K_floor,C_unit*(K_floor+1)} and W.r_reset <= min{epsilon_max^cb,delta_max^cb/D,e_it/(D+1),epsilon_unit,delta_unit/max{1,K_floor},a_unit/((1+K_disp)*D),[2*(1+K_disp)*D]^{-1}}, every explicit raw call into an extended epsilon_R-C*-corner A_R at scale 0 <= t <= W.r_reset whose literal map u_R:B_R->A_R is an extended D*t-inclusion and satisfies ||u_R(I_{B_R})-u_{A_R}|| <= D*t and epsilon_R <= t admits an error-improved map v_R:B_R->A_R that satisfies d_R <= W.c0_cb*epsilon_R and ||v_R(I_{B_R})-u_{A_R}|| <= W.c0_cb*epsilon_R, is an extended W.c0_cb*epsilon_R-inclusion, is an extended W.c0_cb*epsilon_R-isomorphism when u_R is bijective, and leaves the source, target corner, and amplification form unchanged.
```

Use M19-R's definitions and the direct dependencies
`lem-maincb-improvement-iteration; lem-maincb-error-improvement;
lem-maincb-extended-inclusion-monotone`, plus the same registered
`GT-kitaev-prop-delta-hominc` external; do not depend on M19-R itself.
Its proof must construct one literal M02 iterate, apply
`lem-maincb-extended-inclusion-monotone` to that same map, derive the unit
estimate and conditional bijectivity for that same map, and never substitute
M03's separate existential witness. M21, M23, M25, and M26 should import this
row. If the user instead prioritizes canonical interface cleanup and explicitly
ratifies the larger cascade, the design's strengthened M19-R contract itself is
sound and may be used, but the cost statement must still be corrected as below.

## F3 — MAJOR: `check-refs.py` does not stale dependency imports

The design's M18 mechanics are false. In `scripts/check-refs.py:113-122`, any
external source containing `proofs/<id>` and no `refs/` locus returns
`skip_import`. The checker never compares the imported statement with the
current registry contract and never reads the JSON `content_hash`. Thus a
M19-R contract change leaves both M25's and M18's old import JSON green under
`check-refs.py`. `argument.py` checks a workspace's own root against its own
registry contract; it also does not check consumer import strings against
current dependency contracts.

M18's mathematical use is unchanged: its export node `1.11` uses M19-R only
for the same constants, thresholds, eligibility, and conditional bijectivity.
A stronger conclusion cannot invalidate that use.

**Exact correction if strengthening is chosen:** call the M18 JSON stale only
under the repository's manual literal-import convention, not under
`check-refs`; refresh/re-register it to the stronger current contract and
perform an affected-premise audit. Do **not** claim that the gate forces a
fresh M18 proof or demotion. Fresh re-validation would be a policy choice, not
a consequence of `check-refs.py` or of logic. Add a separate regression gate
later if automatic dependency-contract freshness is desired.

## F4 — VALID contracts, INCOMPLETE wiring: M26 and M27

The proposed M26 and M27 lines make exactly the required F-A repair: they tie
`with one-dimensional atomic images` to the same displayed `w` that defines
the partition images. This meets both M19-S3's hypothesis and
`lem-maincb-cross-datum-bijectivity`'s one-dimensional `P_j` hypothesis.
Every other contract clause is retained. M27 carries the same fixed `A,w`
through a finite induction and passes M26's `ENV+RI+UI` invariant without
class-count accumulation. Its conclusion still matches M28's complete-family
input. Keep both proposed contract lines.

The wiring is incomplete, however. To apply the cross-datum bijectivity bridge
inside M26 at `t_3=W.K3*epsilon`, the proof must turn the supplied extended
`W.c0_cb*epsilon`-inclusion `w` into an extended `t_3`-inclusion. The scalar
ledger gives `W.c0_cb*epsilon <= t_3`, but the inclusion implication is exactly
the theorem `lem-maincb-extended-inclusion-monotone`; neither a numerical bound
nor a transitive dependency exports it.

**Exact correction:** add `lem-maincb-extended-inclusion-monotone` directly to
M26's `deps`, and use it on the same displayed `w` before invoking
`lem-maincb-cross-datum-bijectivity`. Replace M26's M19-R import/application by
the new typed bridge from F2 (or the strengthened M19-R if that option is
ratified). M27 needs no new direct dependency beyond repaired M26.

## F5 — SERIOUS: the same monotonicity gap is already latent in M19-S2 and M19-S3

This is omitted from the design and expands the cascade. The repository's own
M18-monotonicity brief records verifier findings that
`def-extended-delta-inclusion` alone does not export defect monotonicity and
that the validated micro-row must be imported explicitly. Nevertheless:

- `proofs/lem-maincb-stage2-call-envelope/export.md`, node `1.4`, infers that
  `w` is a non-unital extended `t_2`-inclusion merely from
  `W.c0_cb*epsilon <= t_2`; M19-S2 does not depend on or import the monotonicity
  row.
- `proofs/lem-maincb-stage3-call-envelope/export.md`, node `1.3.3`, explicitly
  says "tolerance monotonicity turns" `w` into the required extended
  `t_3`-inclusion; M19-S3 likewise does not depend on or import the row.

These are the same inference that challenge `ch-7fbfdb721ff63497` rejected in
M21 and the same fact factored for M18. The two banked validations therefore
have an unregistered-premise gap under the repository's exact-input standard.
M25 consumes M19-S2 and M26 consumes M19-S3, so merely adding monotonicity to
the consumers does not cure the provider certificates.

**Exact correction:** escalate beyond this brief; temporarily demote and
freshly re-validate M19-S2 and M19-S3 with a direct
`lem-maincb-extended-inclusion-monotone` dependency, replacing the quoted
steps by explicit citations to the same `w`. Their contracts remain
byte-identical. Re-audit their downstream status transaction before banking.
Until this happens, the claimed T0 consumer chain is not rigorous even after
F-A/F-B.

## F6 — survey correction: M28 needs two direct providers

The contracts of M21, M22, M23, M24, and M28 can all stand. The design's
all-YES survey is nevertheless incomplete at dependency level:

| Row | Correct verdict and exact wiring |
|---|---|
| M21 | Contract stands. Bind `t:=epsilon`; add direct `lem-maincb-witness-arithmetic` access for the same M18-supplied `W` to obtain `W.r_reset<=e_0`; import the typed-reset bridge. |
| M22 | Contract and deps stand once M21 lands. M20 supplies the positive lower-norm regime and the dimension bound is unchanged. |
| M23 | Contract stands. Import the typed-reset bridge and use its exact `W.c0_cb*epsilon` output on the same Stage-1 literal witness. |
| M24 | Contract and deps stand once M23 lands; its `dim S_{P_j}=1` output is exactly the atomic-image hypothesis used downstream. |
| M28 | Contract stands, but add direct deps on `lem-maincb-extended-inclusion-monotone` and `lem-maincb-witness-arithmetic`. The first transports M27's local isomorphism tolerance `d_J<=W.c0_cb*epsilon_J` to `W.c0_cb*W.K_call*epsilon`; the second exports the same-ledger formula `W.K_call=max{1,L+1,...}` needed for the final unit telescope. M18/M20 do not export both facts. |

After those additions, the structural interface is correct: M24 gives the
one-dimensional atoms, repaired/re-validated M25 supplies one reset per class,
repaired M27 iterates repaired M26, and M28 alone joins the two inductions.

## F7 — budgets and re-seed corrections

- **Typed-reset bridge:** use the proposed M19-R re-validation budget
  `9 / 3 / 13`; it is the same proof obligation under a new id.
- **M25:** keep `7 / 2 / 17`, but classify it as a substantive repair, not an
  external refresh. Rebuild both nodes `1.1.2.2` and `1.1.3.2` from the typed
  provider. The geometric/ENV induction survives only in substance.
- **M26:** keep `9 / 3 / 13` only if the direct monotonicity citation is folded
  into the cross-bijectivity application; otherwise raise the target by one,
  never the hard cap silently. Archive the class-reflexivity workaround.
- **M27:** `7 / 2 / 11` remains credible; carry the global atomic hypothesis and
  exact `ENV+RI+UI` predicate.
- **M21/M23:** the proposed budgets remain credible after adding the exact
  provider imports stated in F6.
- **M19-S2/M19-S3:** absent from the design's budget ledger but mandatory under
  F5. Re-seed under their existing scoped caps, adding one monotonicity external
  and replacing only the affected inference; a cap hit remains a factoring
  stop.
- **M18:** delete the proposed `5 / 2 / 16` "refresh" budget unless the user
  separately orders fresh re-validation. A JSON refresh plus premise audit is
  not a five-node proof.

## Risk register after correction

1. The typed bridge may accidentally take inclusion from M02 and unit or
   bijectivity from a different existential map. Name one literal map in every
   conclusion.
2. M26 may attach the atomic hypothesis or monotonicity conversion to a map
   other than the displayed partition map `w`. Keep `A,w` fixed throughout.
3. M27 may lose the global atomic hypothesis or sum errors across merges. Its
   induction state must remain exactly `ENV+RI+UI`.
4. M28 may cite only the numerical inequality on `d_J` without transporting
   the extended-isomorphism predicate, or may use `K_call>=L+1` without the
   same-ledger provider. Import both rows in F6 explicitly.
5. A green `check-refs` run may be mistaken for dependency-external freshness.
   It provides no such guarantee.

**Corrected landing decision:** first ratify the scope expansion for the M19-S2,
M19-S3, and M25 latent-gap repairs. Prefer the new typed-reset bridge; retain
the proposed M26/M27 contracts; add the direct dependencies in F4/F6; then
freshly verify the affected T0 rows and proceed M21--M28. Do not land the
design's stated M19-R/M18/M25 cascade as written.
