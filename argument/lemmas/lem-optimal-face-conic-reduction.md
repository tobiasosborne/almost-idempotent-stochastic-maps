---
id: lem-optimal-face-conic-reduction
kind: lemma
contract: Optimal-face conic reduction: for the exposedness LP at a hidden geometrically distinct row vertex u of an exact signed idempotent P with t*(u) > 0, the reduced optimal hiddenness dual witnesses are exactly the displays sum over f in T of lambda_f*(p_f - p_u) + sum over z in Z of a_z*(p_z - p_u) = t*(u) * sum over i in O of gamma_i*(p_i - p_u), with lambda and gamma probability vectors supported on T and O and coefficients a_z >= 0 supported on Z (T, O, Z the always-tight families); a display with all a_z = 0 exists if and only if conv{p_f - p_u : f in T} intersects t*(u)*conv{p_i - p_u : i in O}.
defs: def-signed-idempotent; def-visible-set; def-exposed
deps: lem-always-tight-dual-support; lem-optimal-face-alpha-free-characterization
status: proved
af: none
provenance: W44 wave (docs/waves/2026-07-07-W44-t1-intersection.md): fresh-codex prover (worker AS — Goldman-Tucker strict complementarity after deleting redundant centered-zero constraints, relative-interior tight set = always-tight set, then rewriting the witness balance after support localization) + SEPARATE fresh-codex hostile verifier (VAR, VALID-WITH-CORRECTIONS — the a_z = 0 clause is EXISTENTIAL (there exists a display), not universal; clone-deletion legitimacy checked: deleting centered clone-zero constraints does not change the primal optimal face, duplicate nonzero rows restore by splitting multipliers)
owner: A
---

**Role (THE terminal question, exact form).** The residual-cancellation / (T1) question is
now EXACTLY: eliminate the zero-face conic term (all a_z = 0 — the intersection case) or
bound it universally (sum a_z <= A_0 — the bounded-gauge case) under tall/heavy/near-cluster
hypotheses. [[conj-zero-face-elimination]] is that statement; [[obs-realized-alpha-blowup]]
shows the unconditional version is false (min reduced alpha 100 realized outside tall-heavy).

**Rigour tier.** In-repo paper proof with fresh hostile review (L5). NOT af-validated, NOT
L0. Prime elevation candidate together with [[lem-always-tight-dual-support]].
