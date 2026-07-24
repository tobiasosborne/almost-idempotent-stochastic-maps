---
id: lem-compcb-entrywise-compression-naturality
kind: lemma
contract: Entrywise compression naturality: there is a universal e_nat > 0 such that, whenever e = delta+epsilon <= e_nat, Q is a delta-projection in an extended epsilon-C*-algebra A, n >= 1, and E_{11} is the (1,1) matrix unit of M_n, every Z in A satisfies Co_{I_n tensor Q, I_n tensor Q}(E_{11} tensor Z) = E_{11} tensor Co_Q(Z).
defs: def-extended-epsilon-cstar-algebra; def-delta-projection; def-compressed-corner; def-theta-idempotent-approximation
deps: lem-compcb-amplified-compression; lem-compcb-amplification-naturality
status: proved
af: validated
provenance: factored out of proofs/lem-hcb-column-hilbert-squared per the 3rd-stall tripwire (2026-07-25, challenge ch-bbab9bd04b44dd6b node 1.3.1.4 — statement extracted mechanically from the challenge text); UNPROVED here pending its own af pass
owner: A
workspace: proofs/lem-compcb-entrywise-compression-naturality
---

**Status.** `stated` — the exact identity named by the blocking challenge in
orchestration #12 (the E_{11}-slot naturality of the compression map, sharper
than the validated 1_{M_n}-amplification clause of
[[lem-compcb-amplified-compression]]). Factored per the campaign's 3rd-stall
tripwire rule; the af pass is the proof.

**Mechanism sketch (not a proof).** The compression operator at the amplified
corner is built from left/right multiplications by I_n tensor Q, which act
slotwise on E_{11} tensor Z, plus the theta power series
([[lem-compcb-amplification-naturality]] pattern applied at the slot level).
