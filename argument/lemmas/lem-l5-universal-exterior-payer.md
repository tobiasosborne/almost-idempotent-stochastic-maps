---
id: lem-l5-universal-exterior-payer
kind: lemma
contract: For every c_m in (0,1), with delta_E(c_m) = min(1/16, (c_m/8)^2), every finite exact signed idempotent P with 0 < delta(P) <= delta_E(c_m), every row index v, and every nonnegative full-fiber submeasure m <= P_v^+ of mass S >= c_m supported on fibers Q with ||p_Q - p_v||_1 >= 4*sqrt(delta(P)) satisfy, for every point c of the row polytope K(P), P_v^+({R : ||p_R - c||_1 > 1/2}) >= sqrt(delta(P))*S/8, where P_v^+(F) = sum_{R in F} sum_{k in R} max(P_vk, 0).
defs: def-signed-idempotent; def-negative-mass
deps: lem-hx-forced-exterior-coupling; lem-l5-positive-flow-foldback
status: proved
af: none
provenance: W62 wave (docs/waves/2026-07-10-W62-artifacts/): codex prover (gpt-5.6-sol, high) PROOFS-W62-L5-BATCH.md §R3 (explicit ceiling R3.1, strengthening the strategist's suggested shape); fresh hostile batched codex verifier (gpt-5.6-sol, xhigh), verdict VERDICT-W62-L5-BATCH.md line 'R3: VALID' (allocation step named as the weakest accepted step; boundary arithmetic at ||p_Q - p_v||_1 = 4*tau and the strict > 1/2 exterior checked). Reviewer != author.
owner: B
---

**Role (W62 L5 batch, 4/4 — THE UNIVERSAL EXTERIOR PAYER).** The engine-demand
pairing the W54 L5 attack lacked: the af-validated two-row coupling floor
([[lem-hx-forced-exterior-coupling]]), charged pairwise over any far-supported
top-owned submeasure and folded back to row \(v\) by
[[lem-l5-positive-flow-foldback]], forces ROW \(v\) ITSELF to pay
\(\Omega(\tau S)\) positive mass outside EVERY half-ball. This upgrades a family
of unallocated pairwise demands into one owned, center-uniform lower bound.

**Mechanism (one line).** For each charged fiber \(Q\) the coupling gives
\(P_v^+(E_c)+P_Q^+(E_c)\ge\tau/(1+2\delta)-2\delta\); integrate against
\(m\), fold the actor term back with \(g=1_{E_c}\), and solve
\((1+S)V\ge S(\tau/(1+2\delta)-2\delta)-2\delta(1+\delta)\) below the explicit
ceiling.

**Honest scope (verifier-mandated).** The conclusion is per-center uniform ("for
every \(c\) separately"): it neither identifies one common exterior fiber nor
licenses summing demands over centers. The far boundary is \(\ge4\tau\) while the
exterior boundary is strictly \(>1/2\) (the banked coupling boundary). The ceiling
depends on the previously fixed mass threshold \(c_m\). Signed picture;
clone-invariant; no dimension, class-count, or selector input.

**Rigour tier.** L5 (fresh hostile batched codex verdict, W62). NOT af-validated.
af-elevation-shaped; PRIME candidate of this batch (first consumer of the
validated engine bank outside H-X). Consumers: the W62 assembly branch step (with
the S/C/I horns).
