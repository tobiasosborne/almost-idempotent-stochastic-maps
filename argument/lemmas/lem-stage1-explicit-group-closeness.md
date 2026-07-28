---
id: lem-stage1-explicit-group-closeness
kind: lemma
contract: Explicit group-input polar closeness: there exist universal C_grp, C_pol >= 1, kappa_pol in (0, 1/2] such that for every finite-dimensional exact-unit epsilon_r-C*-algebra and delta > 0 satisfying C_pol*(epsilon_r + delta) <= kappa_pol and C_grp*epsilon_r < delta - C_pol*(epsilon_r*delta + delta^2), writing (u_delta, h_delta) for the unique inverse of Pi_delta: calU x B^{calH}_delta(J) -> S_delta := Pi_delta(calU x B^{calH}_delta(J)), Pi_delta(U, H) = U bold-dot H, the first inverse component u_delta:S_delta -> calU satisfies ||u_delta(U bold-dot V) - U bold-dot V|| <= C_grp*epsilon_r and ||u_delta(U^dagger) - U^dagger|| <= C_grp*epsilon_r for every U, V in calU.
defs: def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-polar-retraction
status: stated
af: none
provenance: DESIGN-13E-BINDER-v3.md sect-1.2, landed verbatim (W97 explicit-binder rebuild); AUDIT-13E-BINDER-v3.md (math endorsed; REJECT on process grounds repaired by v3.1/v3.2); AUDIT-13E-BINDER-v3.2.md VERDICT LAND; landing per audit-v3 finding 3.
owner: A
---

**Status.** `stated` candidate landed VERBATIM from the hostile-endorsed
W97 rebuild design (`DESIGN-13E-BINDER-v3.md` §1.2; elevation queue
row 2, target/hard cap 12/16). Binder-closed replacement bridge: for each
displayed input the proof first uses the typed factorization
X = u_delta(X) bold-dot h_delta(X) supplied by the same displayed polar
inverse, controls h_delta(X) - J, and returns to the first factor — it
never identifies two opaque first components by name. The sound anaphoric
child `lem-stage1-group-closeness` is evidence, not an external.
