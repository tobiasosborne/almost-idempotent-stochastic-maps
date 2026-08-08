---
id: ex-hume
kind: obstruction
contract: Disproved historical 3x3-family proposition: for every real s with 0<s<1, set v_s=(1,-1+s,-s), u_s=(1-s+s^2,-s,0)^T, P_s=I_3-u_s v_s^T, and delta_s=s^2; then P_s is a signed affine retraction with maximal row negative mass delta_s and, for every 3x3 stochastic idempotent E, ||P_s-E||_{infinity->infinity}=2s-2s^2+2s^3; as s->0, this claimed common value is 2*sqrt(delta_s)+O(delta_s); moreover, for every C>0 and beta>1/2 there exists a real s with 0<s<1 such that every 3x3 stochastic idempotent E satisfies ||P_s-E||_{infinity->infinity}>C*delta_s^beta.
defs: def-stochastic; def-signed-idempotent; def-negative-mass
deps:
status: disproved
af: none
provenance: RETRACTED 2026-08-08: the inherited contract quoted below is false as quantified; exact counterexample P_s versus I_3 recorded in this body, docs/LEARNINGS.md, and FINDINGS.md; docs/plans/2026-08-08-PAPER/AUDIT-PAPER.md finding 3 records a corrected distance-to-set candidate that remains non-rigorous; active sharpness successor cor-classical-sharpness is separate and subject to its own independent af elevation
owner: A
workspace: proofs/ex-hume
---

**DISPROVED HISTORICAL PROPOSITION (2026-08-08).** The former canonical
contract was, byte-verbatim:

> The explicit 3x3 family P_s=I-u_s v_s^T (v_s=(1,-1+s,-s), u_s=(1-s+s^2,-s,0)^T) is a signed affine retraction with neg mass delta=s^2 whose distance to every stochastic idempotent is 2s-2s^2+2s^3 = 2 sqrt(delta)+O(delta): no bound C delta^beta with beta>1/2 holds, so the exponent 1/2 in op-classical/op-npps is sharp.

That wording omitted the parameter domain and mathematical quantifiers,
left the limiting variable in `O(delta)` unstated, mixed in the out-of-scope
`op-npps`, and asserted one common distance to every stochastic idempotent.
The contract above makes the false proposition precise before disproving it.

**Exact counterexample to the per-idempotent equality.** Fix `0<s<1` and
write `a=1-s+s^2`.  The displayed vectors satisfy
`v_s^T 1=0` and `v_s^T u_s=1`; hence `P_s 1=1` and `P_s^2=P_s`.
The only negative entry of `P_s` is `(P_s)_{23}=-s^2`, so its maximal
row negative mass is exactly `delta_s=s^2`.  But `I_3` is a stochastic
idempotent and
\[
\lVert P_s-I_3\rVert_{\infty\to\infty}
=\lVert u_sv_s^{\mathsf T}\rVert_{\infty\to\infty}
=2a,
\]
while the claimed common value is
`2s-2s^2+2s^3=2sa`.  Their difference is
`2(1-s)a>0`.  Therefore the canonical proposition is false.

**Corrected candidate, not registered here.** The paper faithfulness audit
records the intended statement with `0<s<1`, distance to the **set** of
stochastic idempotents, row-normalized stochastic witnesses, and an explicit
for-every-idempotent lower bound.  This package neither proves nor promotes
that candidate.  Any later rescue of the historical 3x3 family must use a
separate design/audit/ratification round and initialize a fresh workspace.

**Active successor.** The in-scope T0 sharpness route is
[[cor-classical-sharpness]], via the direct stochastic 4x4 family of
[[lem-prh-sharpness]].
