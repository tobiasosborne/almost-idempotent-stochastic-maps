---
id: lem-separator-zero-face-obstruction
kind: lemma
contract: Separator zero-face obstruction: for the exposedness LP at a hidden geometrically distinct row vertex u of an exact signed idempotent P with 0 < t*(u) < inf, a relative-interior optimal exposer h*, and nonempty always-tight far/upper families T, O: if conv{p_f - p_u : f in T} and t*(u)*conv{p_i - p_u : i in O} are disjoint, then for every strict linear separator ell and every m with max over i in O of ell(p_i - p_u) < m < (min over f in T of ell(p_f - p_u))/t*(u), the affine direction psi(p) = ell(p - p_u) - m*h*(p) satisfies psi(p_u) = 0, P psi = psi on row values, psi(p_f) > 0 for all f in T, psi(p_i) < 0 for all i in O, and there exists a nonclone row z with h*(p_z) = 0 and psi(p_z) < 0.
defs: def-signed-idempotent; def-visible-set; def-exposed
deps: lem-optimal-face-alpha-free-characterization; lem-harmonic-affine-bridge; lem-hiddenness-dual-witness
status: proved
af: none
provenance: W44 wave (docs/waves/2026-07-07-W44-t1-intersection.md): fresh-codex prover (worker AT — strong separation of the two compact hulls, then the perturbation h* + eps*psi: absence of a downhill zero-face row makes it feasible with objective t* + eps*gamma, gamma = min_T psi(p_f) > 0, contradicting optimality; clones of u have d = 0, h* = 0, psi = 0) + SEPARATE fresh-codex hostile verifier (VAT, VALID — LP bookkeeping, separation well-definedness incl. singletons/degenerate hulls, per-constraint-family perturbation feasibility with relative-interior slack handling the W42 some-but-not-all-optima failure mode, clone conventions, harmonicity via the affine bridge; exact non-vacuity fixture P = [[1,0,0,0],[0,1,0,0],[11,-21/2,0,1/2],[0,0,0,1]] with u = 0, t* = 1/2, T = {2}, O = {3}, blocker row 1)
owner: A
---

**Role (the (T2) bridge's missing piece, named).** If the terminal intersection FAILS at u,
the failure is certified by a P-harmonic affine direction psi whose only obstruction is a
nonclone zero-face row with negative value — a located, sign-definite object. The bridge to
(T2)/[[conj-zero-face-elimination]] is charging that blocker: in the tall heavy near-cluster
regime the blocker must either force outside-cluster shipping of positive mass or expose a
cluster vertex. The harmonicity Ppsi = psi ties the blocker to the top row's coefficient
ledger through one application of P (the hybrid-circuit object, [[lem-hybrid-dual-certificate]]).

**Rigour tier.** In-repo paper proof with fresh hostile review (L5). NOT af-validated, NOT
L0. Elevation candidate (self-contained LP argument; harmonic clause rides the validated bridge).
