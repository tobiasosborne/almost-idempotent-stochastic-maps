<!--
ROLE: catalogue of ground-truth reference sources for this repo — citation, local path, role, integrity hash.
UPDATE POLICY: append a row when a source is added; never rewrite a hash without re-deriving it from the
bytes on disk. Authoritative hashes live in refs/manifest/checksums.sha256; the fetch recipe in
refs/manifest/sources.lock.json. A source is PINNED only once its bytes exist locally and a real SHA256
was computed — never fabricate a hash.
-->

# SOURCES — ground-truth reference registry

**Policy.** Every `cited` definition and every byte-verified result names a `source-id` here. The payload
under `refs/<source-id>/` is **gitignored** (copyright + size); only this catalogue, `checksums.sha256`,
and `sources.lock.json` are tracked, so provenance is auditable from a clean checkout and reconstructable
with `python3 scripts/fetch-refs.py`. A `cited` claim's quote must **byte-match** its source at the recorded
locus (`check-refs.py`); the recorded SHA256 pins the exact bytes. Verify integrity from the store root:
`cd refs && sha256sum -c manifest/checksums.sha256`.

## Source registry

| source-id | citation | locator | retrieved | local path | key file (sha256-16) | role |
|-----------|----------|---------|-----------|------------|----------------------|------|
| `baake-sumner-2007.11433` | Baake, Sumner, *On equal-input and monotone Markov matrices*, J. Appl. Probab. (2022), DOI 10.1017/apr.2021.39 | arXiv:2007.11433 [math.PR] | 2026-07-02 | `refs/baake-sumner-2007.11433/equal-fin.tex` | `f358c71c066293f8` | idempotent Markov-matrix structure — the commutative case (`op-classical` / `def-stochastic` / `thm-simplex`); arXiv e-print reproducible |
| `hognas-mukherjea` | G. Högnäs, A. Mukherjea, *Probability Measures on Semigroups*, 2nd ed., Springer 2011, ISBN 978-0-387-77548-7 | Springer (Probability and Its Applications) | 2026-06-11 | `refs/hognas-mukherjea/hognas-mukherjea-2011.pdf` (+ `.txt`) | `d74844072a1b96a2` | the δ=0 classification anchor — idempotent probability measures (Thms 1.11 / 1.12 / 1.16); copyright, cache-only |
| `kitaev-2405.02434` | A. Kitaev, *Almost-idempotent quantum channels and approximate C\*-algebras*, arXiv:2405.02434v2 (Feb 2025) | arXiv:2405.02434 [math.OA] | 2026-07-23 | `refs/kitaev-2405.02434/approximate_algebras.tex` (+ `source.tar.gz`) | `e7eb512a2ec2438d` | Route F (fr arm FH) sole import — `th_factorization` (tex:2730, "Thm 12.3"): two-sided O(η) UCP factorization through a finite-dim C\*-algebra with tensor-extended approximate multiplicativity; arXiv e-print reproducible + byte-verified |
| `salzmann-bergh-datta-2405.01532` | R. Salzmann, B. Bergh, N. Datta, *Robustness of Fixed Points of Quantum Channels and Application to Approximate Quantum Markov Chains*, arXiv:2405.01532 (May 2024) | arXiv:2405.01532 [quant-ph] | 2026-07-23 | `refs/salzmann-bergh-datta-2405.01532/FixedPoints.tex` (+ full e-print) | `d4d1e6f9d2afd837` | sharp dimension-free √ε fixed-point repair (thm:FixClassical + optimality remark) — the depolarizing-blend mechanism + the √η-sharpness external anchor (`ex-hume` cross-check); arXiv e-print reproducible |
| `hatcher-algebraic-topology` | A. Hatcher, *Algebraic Topology*, Cambridge Univ. Press 2002 (author's free canonical PDF, 560pp printing) | https://pi.math.cornell.edu/~hatcher/AT/AT.pdf | 2026-07-26 | `refs/hatcher-algebraic-topology/AT.pdf` (+ `.txt`) | `bebb3032bf9021b9` | Stage-1 topology rows: top cohomology (Thm 3.26 + UCT; Cor 3.39), Künneth cross-product (Thm 3.15 — NOT 3.16 in this printing), Hopf structure (Thm 3C.4); URL-reproducible |
| `cairns-1935` | S. S. Cairns, *Triangulation of the manifold of class one*, Bull. Amer. Math. Soc. 41(8) (1935), 549–552 | AMS open journal archive (see lock) | 2026-07-26 | `refs/cairns-1935/cairns-triangulation-1935.pdf` (+ `.txt`) | `2b36c50098bf57da` | Stage-1 topology row `lem-topology-finite-triangulation` (unnumbered THEOREM, p. 549); URL-reproducible; byte-identical to the Project Euclid copy |
| `arkowitz-brown-2004` | M. Arkowitz, R. F. Brown, *The Lefschetz–Hopf theorem and axioms for the Lefschetz number*, Fixed Point Theory Appl. 2004:1, 1–11 (Hindawi OA) | https://link.springer.com/content/pdf/10.1155/S1687182004308120.pdf | 2026-07-26 | `refs/arkowitz-brown-2004/arkowitz-brown-lefschetz-hopf-2004.pdf` (+ `.txt`) | `63da10be018c802f` | Stage-1 topology row `lem-topology-lefschetz-hopf` (Thm 1.2, maximal-simplex form); URL-reproducible (open access) |
| `lee-smooth-manifolds` | J. M. Lee, *Introduction to Smooth Manifolds*, 2nd ed., Springer GTM 218, 2012 | SpringerLink (TIB institutional access) | 2026-07-26 | `refs/lee-smooth-manifolds/lee-smooth-manifolds-2ed.pdf` (+ `.txt`) | `1460301b65117af4` | Stage-1 topology row `lem-topology-quotient-manifold` (Thm 21.10, Quotient Manifold Theorem); copyright, cache-only |
| `granas-dugundji` | A. Granas, J. Dugundji, *Fixed Point Theory*, Springer Monographs in Mathematics, 2003 | SpringerLink (TIB institutional access) | 2026-07-26 | `refs/granas-dugundji/granas-dugundji-fixed-point-theory.pdf` (+ `.txt`) | `49a75a2e443a3075` | Stage-1 topology row `lem-topology-local-index-sign` (Thms (8.4) p.267 + (8.5) pp.328–329); copyright, cache-only |
| `munkres-elementary-differential-topology` | J. R. Munkres, *Elementary Differential Topology*, rev. ed., Annals of Mathematics Studies 54, Princeton UP, 1966 | user-supplied scanned copy (no public URL; copyright, cache-only) | 2026-07-26 | `refs/munkres-elementary-differential-topology/munkres-elementary-differential-topology.pdf` (+ `.txt`) | `7157fa3f5b9876d7` | Stage-1 topology row `lem-topology-finite-triangulation` (Thm 10.6, p.103: every non-bounded C^r manifold has a C^r triangulation) — replaces the Cairns 1935 route, whose class-one/allowable definitions Cairns delegates to Veblen-Whitehead 1932 (not in refs/); scanned typewriter original, per-page tesseract OCR, Thm 10.6 visually confirmed against the page image |

**Provenance status (this ingest).** Both sources are FOUND-AND-PINNED: the bytes exist locally and the
recorded 16-hex prefixes are real SHA256 values computed from the on-disk files (they byte-match the
copies carried over from `almost-idempotent-positive-maps/refs/`).

- `baake-sumner-2007.11433/equal-fin.tex` — `f358c71c066293f8`. Fetch-reproducible: `sources.lock.json`
  pins it as an `arxiv-eprint-member` of arXiv `2007.11433`, so `fetch-refs.py` rebuilds and hash-verifies
  it on any clone (a wrong/hallucinated file cannot match the official arXiv source, so the hash-match
  independently certifies genuineness).
- `hognas-mukherjea` — `.pdf` `d74844072a1b96a2`, `.txt` `ac5e74eb1c346c24`. **Cache-only** (copyrighted;
  no public reproducible source). `sources.lock.json` marks both files `fetch: null` with note
  "acquire manually"; restore from a content-addressed cache you control (`$EXTPROP_REFS_CACHE/<sha256>`)
  seeded once via `python3 scripts/fetch-refs.py --populate-cache <dir>`.

## hognas-mukherjea

G. Högnäs and A. Mukherjea, *Probability Measures on Semigroups: Convolution Products, Random Walks, and
Random Matrices*, 2nd ed., Springer Probability and Its Applications, 2011. ISBN 978-0-387-77548-7. **The
δ=0 anchor's proof source**: the structure theorem for idempotent probability measures (§2.2, "Invariant
and Idempotent Probability Measures"; Thms 1.11/1.12/1.16) — the result Baake–Sumner
(`baake-sumner-2007.11433`) cite without proof for the classification of idempotent Markov matrices.
Acquired by the user (2026-06-11, personal download). Files: `hognas-mukherjea-2011.pdf` (user-supplied) +
`hognas-mukherjea-2011.txt` (local `pdftotext -layout` extraction — greppable loci; byte-quote against the
`.txt`). Cache-only (copyrighted; no public fetch).

## kitaev-2405.02434

A. Kitaev, *Almost-idempotent quantum channels and approximate C\*-algebras*, arXiv:2405.02434v2
[math.OA] (v2, Feb 2025). **The Route-F import source** (fr arm FH, W73): the factorization theorem
`th_factorization` (tex line 2730; §"Approximate factorization through a C\* algebra", the final
subsection of §12 "Almost-idempotent UCP maps") — for UCP Φ with ‖Φ²−Φ‖_cb ≤ η, a finite-dim
C\*-algebra B and UCP Δ, Υ with ‖ΔΥ−Φ‖_cb ≤ O(η) and the tensor-extended approximate
multiplicativity ‖Υ_n(Δ_n(X)Δ_n(Y)) − XY‖ ≤ O(η)‖X‖‖Y‖ (implying ‖ΥΔ−1_B‖_cb ≤ O(η)). Also the
open-problem statement (§1.2) that op-classical's noncommutative generalization is unresolved.
Files: `approximate_algebras.tex` (the paper source; **byte-identical to the official arXiv v2
e-print member — verified 2026-07-23 by direct download and SHA256 match**, `e7eb512a2ec2438d…`) +
`source.tar.gz` (the full e-print bundle; **byte-identical to `https://arxiv.org/e-print/2405.02434`**,
`aed5b4c9ba0d6214…`). Provenance chain: copied from the sibling implementation repo
`../almost-idempotent-channels/paper/` (whose `paper/FINDINGS.md` logs known typos/proof-gaps in the
source — notably C14: the Δ′ CP-ization at tex:2786-2796 is exactly-CP only for exact homomorphisms,
O(η²) Choi negativity measured at multi-block η>0, repairable within the theorem's O(η) spec; and
D1/D2/D4: Lefschetz–Hopf non-constructive step, unstated universal constants, outline-level proof).
Those sibling findings are `stated` context for the W73b audit, not verified content of this repo.

## salzmann-bergh-datta-2405.01532

R. Salzmann, B. Bergh, N. Datta, *Robustness of Fixed Points of Quantum Channels and Application to
Approximate Quantum Markov Chains*, arXiv:2405.01532 [quant-ph] (May 2024). **The sharp dimension-free
√ε fixed-point-repair anchor**: `thm:FixedPointQuantum` + `thm:FixClassical` (FixedPoints.tex:310/322 —
classical states/channels, f(d,ε)=g(d,ε)=√ε, explicitly dimension-INdependent per the remark at
FixedPoints.tex:337) with the optimality remark (FixedPoints.tex:339). Mechanism: depolarizing-blend
contraction (Lemma PertUniqueFix). Role: (i) the multi-block blend pattern for Route P/F fallbacks;
(ii) the external √η-sharpness anchor already named by `ex-hume`'s shard. Files: full arXiv e-print
(`2405.01532.tar.gz`, **byte-identical to `https://arxiv.org/e-print/2405.01532` — downloaded directly
2026-07-23**, `2ed2319f598376ed…`) + the extracted key members (`main.tex`, `FixedPoints.tex`,
`Definitions_and_Setup.tex`, `Preliminaries.tex`, `Introduction.tex`).


## hatcher-algebraic-topology / cairns-1935 / arkowitz-brown-2004 / lee-smooth-manifolds / granas-dugundji (Stage-1 topology promotion, 2026-07-26)

The five Stage-1 topology sources of `DESIGN-FUDW-DECOMP-v4.1.md` §2.3/§4.2, promoted together
from `refs-staging/` (acquisition log: `docs/plans/2026-07-26-refs-staging-ACQUIRED-snapshot.md`,
loci-pinning verdicts: the R-arm harvest of 2026-07-26). Hatcher/Cairns/Arkowitz–Brown are
URL-reproducible open access; Lee and Granas–Dugundji are copyrighted Springer books acquired via
TIB institutional access (cache-only, `fetch: null`). Exact theorem loci and hypothesis-match
verdicts are recorded in the seven `lem-topology-*` registry shards. Locus corrections vs the
design register: Künneth is Thm 3.15 (not 3.16) in the canonical Hatcher printing; the
Arkowitz–Brown Lefschetz–Hopf theorem carries the maximal-simplex hypothesis (contract narrowed
accordingly, user-ratified-by-delegation 2026-07-26).
