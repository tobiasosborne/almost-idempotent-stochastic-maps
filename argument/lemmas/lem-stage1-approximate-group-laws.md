---
id: lem-stage1-approximate-group-laws
kind: lemma
contract: Quantitative approximate group laws: there exist universal C_grp, C_pol >= 1, kappa_pol in (0, 1/2] such that for every finite-dimensional exact-unit epsilon_r-C*-algebra and delta > 0 satisfying C_pol*(epsilon_r + delta) <= kappa_pol and C_grp*epsilon_r < delta - C_pol*(epsilon_r*delta + delta^2), the inverse u_delta of the polar map defines C^1 maps mu(U, V) = u_delta(U bold-dot V), sigma(U) = u_delta(U^dagger) on all of calU, with mu(J, U) = mu(U, J) = U, sigma(J) = J, ||mu(U, V) - U bold-dot V|| <= C_grp*epsilon_r, ||sigma(U) - U^dagger|| <= C_grp*epsilon_r, ||mu(mu(U, V), W) - mu(U, mu(V, W))|| <= C_grp*epsilon_r, ||mu(sigma(U), U) - J|| <= C_grp*epsilon_r, and ||mu(U, sigma(U)) - J|| <= C_grp*epsilon_r.
defs: def-approximate-unitary-space; def-epsilon-cstar-algebra
deps: lem-stage1-group-domain-membership; lem-stage1-group-closeness; lem-stage1-polar-retraction; lem-stage1-polar-coherence-naturality
status: stated
af: none
provenance: DESIGN-S1-POLAR-v6.md sect-3 row 6, landed verbatim (LaTeX flattened to registry ASCII; incl. the v6 finite-dimensional domain restriction, audit-v5 sect-6 option 1); AUDIT-S1-POLAR-v6.md LAND; ratified W78 package sect-5 step 2 (W80). CORRECTED provenance (design sect-3): the two closeness estimates derive from TeX 845-868 plus lem-stage1-polar-retraction; only the three group defects are literal at TeX 872-874; basepoint identities at 876-878.
owner: A
---

**Status.** `stated` candidate transcribed VERBATIM from the audited
`DESIGN-S1-POLAR-v6.md` §3 row 6 (final verdict LAND; carries the v6
finite-dimensional insertion). Not proved in-repo.

**Factoring (2026-07-27, balloon repair).** The first elevation ABORTED
[BALLOON] (60 live nodes > cap 52; ledger retained in git history at the
abort commit). Per the tripwire protocol the PROOF was factored — the
contract above is byte-unchanged — into two sub-lemmas per
`DESIGN-S1-GROUP-FACTORING.md` (hostile-endorsed
AUDIT-S1-GROUP-FACTORING.md, LAND-WITH-CORRECTIONS applied):
`lem-stage1-group-domain-membership` + `lem-stage1-group-closeness`
(deps line updated to the design §2.3 exact text). Re-elevation per the
design §5.3 parent skeleton (11-node target, 12 hard cap): witnesses
synchronized by proof-body maxima/minima (monotone in both guards);
basepoint identities + the three defect telescopes proved here; every
estimate <=, endpoint-safe at epsilon_r = 0. Re-seed AFTER both children
validate (audit (f): children before parent).

**Derivation obligation (design §4).** Prove U bold-dot V, U^dagger in
S_delta, including right-invertibility, from TeX 845–868 and
`lem-stage1-polar-retraction`. Derive the two closeness estimates there;
telescope a fixed number of associators for the three defects literally
printed at 872–874.
