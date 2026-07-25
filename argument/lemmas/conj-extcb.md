---
id: conj-extcb
kind: lemma
contract: EXT-CB: there are universal C_ext < infinity and e_ext > 0 such that if e=delta+epsilon <= e_ext, P,Q are delta-projections in an extended epsilon-C*-algebra A with ||P+Q-I|| <= delta, v:M_r->S_P is an extended delta-isomorphism, dim S_Q=1 at level one, and S_{P,Q} is nonzero, then there is one map v_+:M_{r+1}->A whose every amplification is a C_ext*e-isomorphism; the same level-one unitary and the same four corner maps carry all amplification levels, with constants independent of r, n, and dim A.
defs: def-extended-epsilon-cstar-algebra; def-ha-map
deps: conj-hcb
status: proved-mod-audit
af: none
provenance: docs/plans/2026-07-24-W74F-wave2-artifacts/PROOF-W74F-F-EXTCB.md (prover); hostile verdict VERDICT-W74F-F-EXTCB.md (VALID-WITH-CORRECTIONS, no contract amendment; conj-hcb recorded as proof dependency per the verdict); decomposition DECOMP-W74F-C-THMAINEXT.md §3 EXT-CB
owner: A
workspace: proofs/conj-extcb
---

**Status.** Hostile-verified paper proof (fresh codex prover, separate
fresh hostile codex verifier, VALID-WITH-CORRECTIONS), hence
`proved-mod-audit`; not `af`-validated and not L0-rigorous.  The id keeps
its historical `conj-` slug; ids are stable.

**Proof shape (transcribed).** One level-one unitary
\(U_1:\mathbb C^r\to H_1\) from the exact-target APPROX-CB representation;
the three off-\(11\) corners are DEFINED by transporting one exact spatial
matrix-corner system through the level-one Ha inverses
(\(\gamma_{jk}=h_{jk}^{-1}\mu_{jk}\), \(\gamma_{11}=v\)), so their
amplified complete-closeness is exact and only the \(11\) corner carries
the APPROX-CB error; MERGE-CB closes.  The conditional H-CB inverse
clauses are triggered only after the level-one \(1/4\) lower modulus and
bijectivity are established (verifier-checked order).
\(C_{\rm ext}=C_{\rm merge}[1+5C_H+20C_{\rm app}(C_H+1)]\), independent of
\(r\), the amplification level, \(\dim\mathcal A\), and block data.

**Verifier correction (recorded, proof-level, not contract-level).** The
level-one close-idempotent normalization in EXTCB-1 (the `lem_add_dim`
corner is stated for \(\widehat P=v(I_r)\), with
\(\|\widehat P-P\|=O(e)\) and range identification by close idempotents)
must be explicit, and the selection threshold \(e_{\rm sel}\) must cover
it.  Universal-threshold only; no \(r\)- or level-dependence.

**Consequence.** With [[conj-hcb]] this closes BOTH gap nodes of the
W74F-C decomposition; `th_main_ext` now holds at the `proved-mod-audit`
rung through [[lem-thmainext-conditional]].  The unconditional end-to-end
\(K,\eta_K\) ledger for Route F remains separate open work.
