---
id: lem-hcb1-variational-identity
kind: lemma
contract: Amplified Ha variational identity: there is a universal e_var > 0 such that every H-CB datum with e <= e_var, every n >= 1, Z in M_n tensor S_{P,R}, X in M_{n,1} tensor S_{R,Q}, and Y in M_{n,1} tensor S_{P,Q} satisfy 2*<Y,(Ha^Q_{P,R})_n(Z)X-Z dot X>*Co_Q(Q)=(Y^dagger dot Z) dot X-Y^dagger dot (Z dot X).
defs: def-ha-map; def-hcb-datum
deps: lem-compcb-amplified-compression-identities; lem-hcb-column-hilbert-squared
status: proved
af: validated
provenance: PROOF-W74F-E-HCB.md §4; VERDICT-W74F-E-HCB.md HCB-1a (VALID); DESIGN-FUDW-DECOMP-v3.md §2.1; VERDICT-FUDW-DECOMP-V3.md §D; report lem:hcb1-variational-identity
owner: A
workspace: proofs/lem-hcb1-variational-identity
---

**Status.** `proved`; `af: validated` — root-validated, taint-clean
adversarial tree (mechanical ledger reflection; export at
`proofs/lem-hcb1-variational-identity/export.md`).

**Provenance.** `PROOF-W74F-E-HCB.md` §4 and
`VERDICT-W74F-E-HCB.md` HCB-1a; admitted by
`VERDICT-FUDW-DECOMP-V3.md` §D.

**Contract amendment (2026-07-25, orchestration #11 rebuild).** The codified
contract wrote the normalization factor as `u_Q`; the ratified `def-ha-map`
identity and the column-Hilbert displays use `wtQ = Co_Q(Q)` (challenges
ch-79dbd11b701aec54 / ch-3c8c2053db27229e / ch-233a4d4320264ee7). The factor
is now written explicitly as `Co_Q(Q)` — definitionally the same element (the
corner-algebra compressed unit `u_Q = Co_Q(Q)`), so no strengthening or
weakening; pure notation typing. Mechanical verdict-driven amendment
(standing precedent).
