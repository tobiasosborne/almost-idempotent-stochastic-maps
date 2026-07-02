---
id: lem-mass-split
kind: lemma
contract: Mass split: for an exact signed idempotent P and any row index v, writing a_j = P_{vj}, a_j^+ = max(a_j, 0), a_j^- = max(-a_j, 0), and nu_v = sum_j a_j^-, one has sum_j a_j^+ = 1 + nu_v.
defs: def-signed-idempotent; def-negative-mass
deps: 
status: stated
af: none
provenance: factored out of proofs/conj-halo-collapse elevation run 1 (nodes 1.1.2, 1.1.3, 1.4.1.3.x — the bookkeeping the provers re-derived inline across siblings, trip cause of the BALLOON abort); the identity is row-sum bookkeeping from P 1 = 1 in def-signed-idempotent
owner: A
workspace: proofs/lem-mass-split
---

**Purpose (factoring, aism-q7e).** The pot-bookkeeping identity behind every mass split in the
halo-collapse argument: since row sums of an exact signed idempotent are 1
(`sum_j a_j = 1` from `P 1 = 1`), decomposing `a_j = a_j^+ - a_j^-` and summing gives
`sum_j a_j^+ = 1 + nu_v`. Elevation run 1 of [[conj-halo-collapse]] ballooned (49 > 40 nodes)
largely because this identity and its consequences were re-derived inline in multiple sibling
subtrees; it is factored here as a standalone dep so provers import it instead.

**Role:** dep of [[conj-halo-collapse]] (and available to any future ledger-style argument splitting
row-reproduction mass into pots).
