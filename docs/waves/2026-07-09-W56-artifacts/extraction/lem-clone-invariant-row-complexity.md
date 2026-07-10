---
id: lem-clone-invariant-row-complexity
kind: lemma
contract: For every finite exact signed idempotent P, the numbers R(P) of geometrically distinct row points and V(P) of extreme points of their row polytope are finite positive integers invariant under clone splitting, and every nonempty collection of finite exact signed idempotents contains a member attaining the lexicographic minimum of (V(P),R(P)).
defs: def-signed-idempotent; def-negative-mass
deps: 
status: proved-candidate
owner: W56-extraction
---

# Clone-invariant row complexity

## Statement

For a finite exact signed idempotent \(P\), coalesce equal rows and let \(R(P)\) be the number of resulting geometrically distinct row points and \(V(P)\) the number of extreme points of their convex hull.  Then \(V(P)\) and \(R(P)\) are finite positive integers, they are unchanged by any clone splitting that changes only the multiplicities of the same geometric row points under the natural coordinate identification, and every nonempty collection \(\mathcal C\) of finite exact signed idempotents contains a member attaining
\[
 \min_{P\in\mathcal C}^{\mathrm{lex}}(V(P),R(P)).
\]

## Proof

A finite matrix has a finite nonempty row set.  Coalescing equal rows therefore leaves a finite nonempty set of row points, so \(R(P)\) is a positive integer.  The convex hull of a finite nonempty set is a nonempty polytope; its extreme points form a nonempty subset of that finite generating set.  Hence \(V(P)\) is also a finite positive integer.

A clone splitting, in the stated geometric sense, replaces one or more occurrences of a row point by coincident occurrences and does not add or remove a geometrically distinct row point.  Thus the coalesced row-point set is unchanged.  Its convex hull and its extreme-point set are consequently unchanged, proving invariance of both \(R\) and \(V\).

Now let \(\mathcal C\neq\varnothing\).  The nonempty subset
\[
 \{V(P):P\in\mathcal C\}\subseteq\mathbb N
\]
has a least element \(V_0\).  Among matrices in \(\mathcal C\) with \(V(P)=V_0\), the nonempty set of integers \(\{R(P)\}\) has a least element \(R_0\).  By the definitions of these two sets, some \(P_0\in\mathcal C\) realizes \((V_0,R_0)\), which is the lexicographic minimum.

## Notes

This lemma only banks well-definedness, clone invariance, and integer attainment.  It supplies no useful minimal-counterexample hypothesis: a transient-row extension can preserve \(V\) while increasing \(R\), and the round-2 verifier found no valid descendant that consumes minimality.
