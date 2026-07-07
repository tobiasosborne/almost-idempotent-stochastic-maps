---
id: obs-rank3-t1-boundary
kind: obstruction
contract: Rank-3 T/O boundary census: the exact rank-3 signed idempotent W41 HEIGHT+A (delta = 9859/400000) realizes always-tight T/O hull-intersection FAILURE at both positive-mass near hidden rows of its hidden top while lying OUTSIDE the tall-heavy width-4 hypotheses (H < 4*tau, G_4 empty); the W41 TOP-preserving instance (delta = 49/2000) and the W29 frontier instance (delta = 99/8000) satisfy the intersection at every positive-mass near hidden row of their hidden tops, with exact convex certificates.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-exposed; def-height
deps: lem-optimal-face-alpha-free-characterization
status: proved
af: none
provenance: W44 wave (docs/waves/2026-07-07-W44-t1-intersection.md): fresh-codex prover (worker AU, exact rational LPs incl. secondary whole-face LPs) + SEPARATE fresh-codex hostile verifier (VAU, VALID — fully independent implementation, vertex enumeration in h-value space via P h = h, whole-face tightness by min/max of each h_k over the forced optimal face; all three instances recomputed exactly); run bundle runs/2026-07-07-w44-rank3-boundary/ (two independent verifiers, both PASS on orchestrator rerun)
owner: A
---

**Role (why the hypotheses of the terminal node are load-bearing).** Empty always-tight
hull intersections DO occur at rank 3 — but in the entire banked exact record only OUTSIDE
the tall-heavy class, while every in-class instance satisfies [[conj-zero-face-elimination]]'s
intersection horn with exact certificates. Together with [[obs-realized-alpha-blowup]]
(minimum reduced alpha 100 at H/tau = 1/505) this pins the class boundary as exactly the
live question and kills any hope of dropping tallness/heaviness from the terminal conjecture.

**Honest scope.** Three instances — a census, not a theorem. The open rank-3 statement is
the named candidate lem-rank3-cluster-uniform-optimal-face-interlacing (sketch v12 route (a)).

**Rigour tier.** Exact finite certificates, independently recomputed (L5 review of a finite
computation); the general claim it gestures at remains CONJECTURE. NOT af-validated.
