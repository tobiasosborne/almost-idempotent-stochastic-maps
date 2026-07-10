---
id: lem-hx-signed-variation-ledger
kind: lemma
contract: For every finite exact signed idempotent P, every ordered pair (a,b) of points of the row polytope K(P), and every set S of full row-point fibers, sum_{Q in S} |d_Q| <= a^+(S) + b^+(S) + nu(a) + nu(b), where d_Q = sum_{j in Q}(a_j - b_j), r^+(S) = sum_{Q in S} sum_{j in Q} max(r_j,0), and nu(r) = sum_j max(-r_j,0).
defs: def-signed-idempotent; def-negative-mass
deps: 
status: proved
af: none
provenance: W60 wave (docs/waves/2026-07-10-W60-artifacts/): codex prover (gpt-5.6-sol, high) PROOFS-W60-ENGINE.md §E2; fresh hostile codex verifier (gpt-5.6-sol, xhigh), batched verdict VERDICT-W60-ENGINE.md line 'E2: VALID'. Reviewer != author.
owner: B
---

**Role (W60 engine bank, 2/5).** The budget converter: localized fiber
\(d\)-variation is paid for by the two rows' positive mass ON the set plus their
own negative-mass budgets — each budget paid ONCE per sign-union, never per fiber
(the K-free pattern of W59 Claim 4, extended to synthetic rows and arbitrary fiber
sets). Retires the slab-side bookkeeping of the W59 §HONEST LIMITS gaps: no
coordinate slab is needed to control exterior variation.

**Statement.** For every finite exact signed idempotent \(P\), every ordered pair
\((a,b)\) of points of \(K(P)\), every set \(S\) of full row-point fibers:
\[ \sum_{Q\in S}|d_Q|\ \le\ a^+(S)+b^+(S)+\nu(a)+\nu(b). \]
Body-level addendum (proved in the source): the global bound
\(\sum_Q|d_Q|\le\lVert a-b\rVert_1\), and the synthetic-row facts \(qP=q\),
\(q\mathbf1=1\), \(\nu(q)\le\delta(P)\) for every \(q\in K(P)\) (convexity of
\(x\mapsto(-x)_+\)).

**Mechanism (one line).** Partition \(S\) by the sign of the aggregate \(d_Q\);
on each sign-union \(U_\pm\) (a genuine index subset) the subset budgets
\(-\nu(r)\le r(U)\le r^+(U)\) of the two mass-one rows close the bound.

**Scope.** Vacuously weak when the rows place little positive mass on \(S\) —
that is the point: it converts variation demands into positive-mass demands
(the confinement question). Clone-invariant. Signed picture.

**Rigour tier.** L5 (fresh hostile codex, batched W60 verdict). NOT af-validated.
af-elevation candidate. Consumer: [[lem-hx-financing-floor]].
