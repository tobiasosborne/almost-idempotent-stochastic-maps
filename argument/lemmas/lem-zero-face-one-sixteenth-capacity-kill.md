---
id: lem-zero-face-one-sixteenth-capacity-kill
kind: lemma
contract: For every exact signed idempotent P with 0 < delta(P) <= 2^(-16), every hidden geometrically distinct row vertex u, every optimal exposer h* at u, and every row z with h*(p_z) = 0, the positive row-z coefficient mass sent to {j:h*(p_j) >= sqrt(delta(P))/4} is strictly less than 1/16.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed
deps: lem-zero-face-capacity-kill
status: proved
af: none
provenance: W56 wave (docs/waves/2026-07-09-W56-artifacts/): extracted from the twice-hostile-verified routine material of DECOMPOSITION-v2 (verdict-round1.md, verdict-round2.md); per-shard fresh hostile codex verdict in verdict-extraction.md (4 VALID + 6 VALID-WITH-CORRECTIONS, corrections applied and re-listed in the wave doc); reviewer != author throughout.
owner: B
---

# Zero-face one-sixteenth capacity kill

## Statement

Let \(P\) be an exact signed idempotent with \(0<\delta:=\delta(P)\le2^{-16}\), put \(\tau:=\sqrt\delta\) and \(\kappa:=\tau/4\), let \(u\) be a hidden geometrically distinct row vertex, let \(h^*\) be an optimal exposer at \(u\), and let \(z\) be any row with \(h^*(p_z)=0\).  Then
\[
 \sum_{j:h^*(p_j)\ge\kappa}\max(P_{zj},0)<\frac1{16}.
\]

## Proof

Assume instead that the displayed shipping is at least \(1/16\).  We consume the following proved contract of `lem-zero-face-capacity-kill` verbatim:

> “Zero-face capacity kill: for an exact signed idempotent P with delta(P) > 0, a hidden geometrically distinct row vertex u, an optimal exposer h* at u, a row z with h*(p_z) = 0, and c_r > 0 with sum over {j : h*(p_j) >= kappa} of max(P_zj, 0) >= c_r (kappa = tau/4, tau = sqrt(delta)): c_r*kappa <= nu_z <= delta(P), where nu_z is the row-z negative mass; in particular no such configuration exists for 0 < delta < (c_r/4)^2.”

Apply it with \(c_r=1/16\).  Its ledger gives
\[
 \frac1{16}\frac\tau4=\frac\tau{64}\le\delta=\tau^2.
\]
Because \(\tau>0\), division by \(\tau\) forces \(\tau\ge1/64\).  But \(\delta\le2^{-16}\) gives \(\tau\le2^{-8}=1/256\), a contradiction.  Hence the shipping is strictly less than \(1/16\).

## Notes

No disjoint-hull, separator, relative-interior, or horn hypothesis is needed for this capacity consequence.  The statement is dimension-free and clone-invariant because the shipping quantity is a coefficient-mass sum over a value-defined row set.
