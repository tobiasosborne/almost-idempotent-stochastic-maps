---
id: lem-l5-positive-flow-foldback
kind: lemma
contract: For every finite exact signed idempotent P, every row index v, every nonnegative full-fiber submeasure m with m_Q <= sum_{j in Q} max(P_vj, 0) for every full row-point fiber Q, and every function g from the full row-point fibers to [0, M], sum_Q m_Q * sum_R sum_{k in R} max(P_Qk, 0)*g_R <= sum_R sum_{k in R} max(P_vk, 0)*g_R + 2*delta(P)*(1 + delta(P))*M, where P_Qk denotes the common value P_ik for i in Q.
defs: def-signed-idempotent; def-negative-mass
deps: lem-mass-split
status: proved
af: none
provenance: W62 wave (docs/waves/2026-07-10-W62-artifacts/): codex prover (gpt-5.6-sol, high) PROOFS-W62-L5-BATCH.md §R2; fresh hostile batched codex verifier (gpt-5.6-sol, xhigh), verdict VERDICT-W62-L5-BATCH.md line 'R2: VALID' (the six-term sign expansion R2.4 recomputed directly; delta = 0 reduces to exact stochastic flow conservation). Reviewer != author.
owner: B
---

**Role (W62 L5 batch, 3/4 — same-carrier positive-flow allocation).** One
aggregate application of \(P^2=P\) at row \(v\): the selected actors' one-step
positive outflow, weighted by any top-owned submeasure, cannot exceed row \(v\)'s
own positive mass on the same receiver set plus an \(O(\delta)\) leak. This is the
allocation step that prevents a reusable actor payer from being charged repeatedly
— the mandatory precursor to any aggregate lower bound built from pairwise engine
demands (kill-list item 3 of `DECOMPOSITION-W62-L5.md`).

**Mechanism (one line).** Expand \(P_v=P_vP\), split the row-\(v\) coefficients
into the submeasure part, the positive remainder, and the negative part
([[lem-mass-split]] for the budgets); the \(m\)-mass lost to negative receivers
cancels against the same \(m\)-mass removed from the positive remainder; the
surviving error is \(\le2\delta(1+\delta)M\).

**Honest scope (verifier-mandated).** An aggregate full-fiber inequality with the
positive part taken BEFORE receiver-fiber aggregation; it is not a pointwise
path-product estimate and gives no probabilistic interpretation to signed
coefficients. Universal in \(g\) (consumers instantiate indicators or dual
deficits). Signed picture; clone-invariant.

**Rigour tier.** L5 (fresh hostile batched codex verdict, W62). NOT af-validated.
af-elevation-shaped. Consumers: [[lem-l5-universal-exterior-payer]]; the S/C/I
horns.
