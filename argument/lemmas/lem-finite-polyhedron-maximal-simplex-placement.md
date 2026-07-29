---
id: lem-finite-polyhedron-maximal-simplex-placement
kind: lemma
contract: Every point of a finite polyhedron lies in a maximal simplex of its defining finite simplicial complex; therefore every finite fixed set does.
defs:
deps:
status: stated
af: seeded
workspace: proofs/lem-finite-polyhedron-maximal-simplex-placement
provenance: DESIGN-S1-POLAR-v6.md sect-5 (downstream row 6), landed verbatim; AUDIT-S1-POLAR-v6.md LAND; ratified W78 package sect-5 step 2 (W80). Algebra-independent finite-poset derivation; consumes none of the analytic rows.
owner: A
---

**Status.** `stated` candidate transcribed VERBATIM from the audited
`DESIGN-S1-POLAR-v6.md` §5 (final verdict LAND). Not proved in-repo;
af elevation per the design's projected budget 2/1. Algebra-independent:
a finite partially-ordered-set argument (every simplex is contained in a
maximal one; finitely many simplices), added by the audits as required
input 10 of the corrected `lem-stage1-extra-fixed-class` dependency list
(design §6).

**Build-granularity discipline (BINDING on the af tree).** The target is
the design's 2-node skeleton (budget 2/1): ONE node for the finite-poset
maximality argument (every simplex of a finite complex is contained in a
maximal simplex; every point of the polyhedron lies in some simplex),
ONE node specializing to the finite fixed set. BSc-level poset/simplicial
facts are common knowledge (L2) — no external registrations. Do NOT
sub-split.

**Elevation run 1 ABORTED [STUCK] 2026-07-29 — CONTRACT-AMBIGUITY
FINDING, user decision pending.** The fresh verifier cohort validated
the two skeleton nodes but challenged the ROOT (ch-074db338): the
contract's second clause "therefore every finite fixed set does" is
ambiguous — on the collective reading ("the entire finite set lies in
ONE maximal simplex") it is REFUTED by two isolated vertices; only the
pointwise reading ("each point of every finite fixed set lies in some
maximal simplex, possibly depending on the point") is entailed. The
prover's pointwise amendment of node 1 was then correctly challenged as
contract drift (ch-6ae93d5d: root no longer byte-matches the registry
contract). Per the design stop rule this is a CONTRACT change, not a
local proof repair -> returns to design/user (the contract was landed
verbatim from the audited DESIGN-S1-POLAR-v6 sect-5, so disambiguation
needs ratification; the design prose and the consumer
lem-stage1-extra-fixed-class intend the pointwise reading). Aborted-run
ledger discarded at workspace restore (the established balloon/stuck
precedent); classification preserved here and in the fr log. Status
remains stated/seeded — no rigour claim.
