---
id: lem-affine-barycenter-identity
kind: lemma
contract: For every probability measure lambda on a finite set of row points with barycenter b and every real-valued affine function a on their ambient finite-dimensional affine space, the affine integral satisfies integral a(p_x) d lambda(x) = a(b).
defs: 
deps: 
status: proved
af: none
provenance: W56 wave (docs/waves/2026-07-09-W56-artifacts/): extracted from the twice-hostile-verified routine material of DECOMPOSITION-v2 (verdict-round1.md, verdict-round2.md); per-shard fresh hostile codex verdict in verdict-extraction.md (4 VALID + 6 VALID-WITH-CORRECTIONS, corrections applied and re-listed in the wave doc); reviewer != author throughout.
owner: B
---

# Affine barycenter identity

## Statement

For every probability measure \(\lambda\) on a finite set of row points, with
\[
 b:=\int p_x\,d\lambda(x),
\]
and every real-valued affine function \(a\) on their ambient finite-dimensional affine space,
\[
 \int a(p_x)\,d\lambda(x)=a(b).
\]

## Proof

Write \(a(y)=L(y)+c\), where \(L\) is linear and \(c\) is constant.  Linearity of a finite sum and the fact that \(\lambda\) has total mass one give
\[
 \int a(p_x)\,d\lambda(x)
 =L\!\left(\int p_x\,d\lambda(x)\right)+c\int 1\,d\lambda
 =L(b)+c
 =a(b).
\]
This proves the identity.

## Notes

The conclusion concerns affine integrals only.  It does not assert that measures having the same barycenter have the same masses on nonlinear sublevel sets.  Aggregating or splitting weights among coincident row points leaves both sides unchanged, so the statement is clone-invariant; appending a zero coordinate to every point preserves it as well.
