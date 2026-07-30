---
id: lem-stage1-fresh-two-point-inclusion
kind: lemma
contract: There are universal C_pair<infinity and e_pair>0 such that every finite-dimensional extended epsilon_X-C*-algebra (calX,I_X,.,dagger) with 0<=epsilon_X<=e_pair and 1<dim_C calX<infinity contains nonvanishing C_pair*epsilon_X-projections P',P'' with P'+P''=I_X for which the linear map v^(2):C^2->calX, v^(2)(lambda,mu)=lambda*P'+mu*P'', is an extended C_pair*epsilon_X-inclusion, satisfies v^(2)(1,1)=I_X, and sends the standard projection basis Pi',Pi'' to P',P''.
defs: def-extended-epsilon-cstar-algebra; def-delta-projection; def-extended-delta-inclusion; def-operator-space; def-projection-basis
deps: lem-stage1-original-complementary-pair
status: proved
af: validated
workspace: proofs/lem-stage1-fresh-two-point-inclusion
provenance: DESIGN-S1-ENDGAME-v5.md sect-2 (landed verbatim); AUDIT-S1-ENDGAME-v5.md VERDICT LAND (zero corrections); user-ratified 2026-07-30
owner: A
---

**Status.** af-VALIDATED in-repo (2026-07-30): 12-node tree, root
`validated`, taint clean 12/12
(`proofs/lem-stage1-fresh-two-point-inclusion/export.md`; oracle pass;
tier routine, 12 nodes <= cap 14, budget 9/3/14 + open-challenge
resume at max-rounds 6). TWO challenges raised and repaired: (i) the
application of GT-kitaev-prop-delta-hominc had not established the
external's independent delta-smallness hypothesis — repaired by leaf
1.7.1 pinning e_up <= delta_max/(4*max{C_np,1}) so delta_n <=
delta_max and 2*delta_n < eta = 1/4; (ii) 1.8's level-uniform
coefficient rested on the then-pending 1.7 — repaired by leaf 1.8.1
supplying the explicit universal K with a hard validation dependency
on 1.7. Route (per the prover build summary): C2 pair -> canonical
amplifications v_n = id_{M_n} tensor v^(2) -> four-term multiplicative
defect identity -> uniform 1/4 lower modulus -> GT external ->
universal C_pair. G-S1 GATE: all three producers (C1, C2, C3) now T0.

**Build budget (BINDING on the af tree).** Design target/rounds/hard-cap:
9 / 3 / 14. The per-node skeleton is DESIGN-S1-ENDGAME-v5.md sect-4
(lem-stage1-fresh-two-point-inclusion); a hard-cap hit is a factoring stop, not a rounds bump. Constants
live in the proof body, never the contract.

**Provenance loci.** `refs/kitaev-2405.02434/approximate_algebras.tex:458,1192-1222,1419-1424`; external statement `:1194-1196`
