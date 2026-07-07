---
id: lem-always-tight-dual-support
kind: lemma
contract: Always-tight dual support: for the exposedness LP at a hidden geometrically distinct row vertex u of an exact signed idempotent P with delta(P) > 0 and nonempty visible set, every optimal hiddenness dual witness (lambda, alpha, beta), after deleting redundant centered-zero constraints, has supp(lambda) contained in T, supp(beta) contained in O, and supp(alpha) contained in Z, where T, O, Z are the rho-far, upper-box, and lower-box constraint families tight on the WHOLE primal optimal face; T is nonempty, and O is nonempty if and only if t*(u) > 0.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed
deps: lem-hiddenness-dual-witness
status: proved
af: none
provenance: W44 wave (docs/waves/2026-07-07-W44-t1-intersection.md): TWO independent fresh-codex provers (AR and AS, identical core proof — pair the witness balance with any optimal exposer h to get the complementarity identity sum lambda_f(h_f - t*) + sum alpha_i h_i + sum beta_i(1 - h_i) = 0 with every summand nonnegative) + SEPARATE fresh-codex hostile verifier (VAR, VALID-WITH-CORRECTIONS — the redundant-centered-zero caveat: if redundant centered zero constraints are retained, arbitrary alpha can be added on d_v = 0 rows without changing the balance, hence the "reduced witness" clause; O-empty edge: t* = 0 makes h = 0 optimal; exact edge fixtures incl. rank-3 singleton T/O, t* = 0, duplicate centered rows)
owner: A
---

**Role.** Upgrades [[lem-optimal-face-alpha-free-characterization]]'s T/O description to full
witness-support localization: the ONLY constraints any optimal witness can charge are the
always-tight families, and the alpha-carriers are exactly the always-tight zero-face rows Z.
This is the vocabulary in which the terminal node is now posed (kill or bound the Z-mass).

**Fixture (VAR-recomputed, exact).** The obs-realized-alpha-blowup family member with
eps = t = 1/100: P rows (1,0,0,0), (10099/10000, 0, 1/10000, -1/100), (0,0,1,0), (0,0,0,1);
delta = 1/100, at v = 1: t* = 1/100, T = {4}, O = {3}, zero-face row 2, and
d_4 + 100*d_2 = (1/100)*d_3 — MINIMUM reduced alpha mass exactly 100. LP-only alpha control
is impossible (the instance is far outside tall-heavy: H/tau = 1/505).

**Rigour tier.** In-repo paper proof, two independent provers + fresh hostile review (L5).
NOT af-validated, NOT L0. Elevation candidate (short complementarity proof, deps validated).
