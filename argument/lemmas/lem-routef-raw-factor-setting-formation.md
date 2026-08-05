---
id: lem-routef-raw-factor-setting-formation
kind: lemma
contract: Route F raw-factor setting formation: there exists one choice W_RF of the scalar header of def-routef-raw-factor-setting, independent of H, Phi, eta, dimension, amplification level, and block data, with C_theta=12*(sqrt(2)-1), C_A=20+(211/8)*C_theta, eta_A>0 and (C_A,eta_A) the fixed witnesses of lem-routef-ai-defect-linearization, C_E<infinity and epsilon_E>0 the fixed witnesses of lem-thmainext-conditional, rho_theta:=1/8, rho_AI:=eta_A, and all remaining named scalar quantities defined by (1.1)-(1.8), such that for every nonzero finite-dimensional Hilbert space H, every UCP map Phi:B(H)->B(H), and every eta with 0 <= eta <= rho_id^corr and ||Phi^2-Phi||_cb <= eta, there exist a finite-dimensional unital C*-algebra B, an extended C_E*epsilon_AI(eta)-isomorphism v:B->A, and a def-routef-raw-factor-setting datum S over this same W_RF whose fields are the displayed H,Phi,eta,B,v,u=v^(-1) and the canonical tilde-Phi,A,star,epsilon_AI(eta),tilde-Delta,tilde-Upsilon notation, with tilde-Phi^2=tilde-Phi, A an extended epsilon_AI(eta)-C*-algebra, and 0 <= epsilon_AI(eta) <= C_A*eta <= epsilon_E.
defs: def-routef-raw-factor-setting; def-ucp-map; def-extended-epsilon-cstar-algebra; def-extended-delta-inclusion
deps: lem-kitaev-almost-idemp-audit; lem-routef-ai-defect-linearization; lem-thmainext-conditional
status: stated
af: none
provenance: DESIGN-LEDGER-SETTING-RESCOPE-V2.md sect-2 (formation repair required by AUDIT-LEDGER-SETTING-RESCOPE.md findings 1-3); hostile re-audit AUDIT-LEDGER-SETTING-RESCOPE-V2.md verdict LAND-WITH-EXACT-CORRECTIONS (formation cleared, elevation phase mandated by its finding 3); user-ratified 2026-08-05; scalar ledger source DESIGN-LEDGER-DOMAINS-v2.md sect-1
owner: A
workspace: proofs/lem-routef-raw-factor-setting-formation
---

**Status.** `stated` (transcribed from the ratified rescope design, unchecked in-repo).
Landing promotes no definition, provider, or ledger result.

**Quantifier discipline.** The existential choice of `W_RF` precedes every input quantifier.
The same `eta_A, C_A, C_E, epsilon_E`, hence the same entire derived scalar ledger, is used
for every datum `S`. The input-specific existential contains `B, v, S` only; it cannot
reselect the global witnesses.

**Derivation obligation.** Fix the AI witnesses once and the MAIN witnesses once. For an
input in the displayed domain, `rho_id^corr` gives `eta <= rho_theta = 1/8 < 1/4`,
`eta <= rho_AI = eta_A`, and `C_A*eta <= epsilon_E`. Apply [[lem-kitaev-almost-idemp-audit]]
for exact idempotence, [[lem-routef-ai-defect-linearization]] for the extended
`epsilon_AI(eta)` structure and linear estimate, and [[lem-thmainext-conditional]] to that
same finite-dimensional range `A` for one `B, v`. Package these particular outputs as `S`;
no analytic conclusion may be inferred from [[def-routef-raw-factor-setting]] alone.

**Projected af budget (binding design target).** Target 10 live nodes / 3 verification
rounds / hard cap 14: root; one global-witness selection node; one scalar-header assembly
node; one radius extraction node; one Kitaev application; one AI application; one
finite-dimensional-range node; one MAIN application; one same-output `S` packaging node;
one quantifier/universality assembly node. Hitting 14 is a factoring stop, not permission
to enlarge the cap (AUDIT-LEDGER-SETTING-RESCOPE-V2.md finding 3: this workspace gets its
own seed/provision/elevate/bank phase BEFORE either live family continuation).
