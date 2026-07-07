---
id: lem-rank3-row-support-tight-spread-criterion
kind: lemma
contract: Rank-3 tight-spread criterion: for a rank-3 exact signed idempotent P and a hidden geometrically distinct row vertex u with t*(u) > 0, translating the level-line coordinate r by c*h (h an optimal exposer) preserves r_u = 0 and shifts the always-tight T interval and the scaled-O interval coordinates by the same c*t*(u); c can be chosen so that 0 lies in the scaled-O interval, and after that normalization, always-tight T rows on both sides of 0 force the T/O interval overlap (hence an alpha-free optimal display).
defs: def-signed-idempotent; def-exposed; def-visible-set
deps: lem-rank3-optimal-face-interval-reduction; lem-harmonic-line-coordinate-row-balance
status: proved
af: none
provenance: W49 wave (docs/waves/2026-07-07-W49-face-deciders.md): fresh-codex prover (worker BF) + SEPARATE fresh-codex hostile verifier (VBD, VALID — translation algebra checked; the normalization exists since t*(u) > 0 and O nonempty)
owner: A
---

**Role.** Reduces (F1) at rank 3 to: PROMOTE row-positive far balance-witnesses into the
always-tight family T (then row balance + this criterion give overlap). The promotion step
is the named residual — the tightness-promotion wall (FINDINGS 2026-07-07).
