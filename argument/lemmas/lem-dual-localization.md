---
id: lem-dual-localization
kind: open-problem
contract: (SUPERSEDED by conj-skinny-shadow-cap, 2026-07-04; trivially true as stated) Frame-free dual localization: reproduce ||Ebar||_1 >= H from P^2=P WITHOUT the canonical simplex frame (the exact inequality Route B loses in the skinny mu->1 regime); this is the single genuine gap in the frame-free proof of the linear law delta >= H/2 that would feed op-exposed-hull.
defs: def-height; def-signed-idempotent
deps: 
status: obstruction
af: none
provenance: docs/ingest (classical-portfolio; contracts verbatim from ../almost-idempotent-positive-maps/argument/lemmas or report/kernel-conjecture.tex); superseded per docs/waves/2026-07-02-B1-dual-localization.md sec 6 + bd aism-136 codex verifier note (user decision 2026-07-04)
owner: A
workspace: proofs/lem-dual-localization
---

**RETIRED (2026-07-04, user decision on aism-136).** The transcribed contract is **trivially
true as stated**: once `v1 = Lbar + Ebar` with `Lbar` in the visible hull, `H <= dist_1(p_v1,
C_W) <= ||Ebar||_1` is a distance tautology requiring no idempotence (arm B wave 1, sec 6;
independently confirmed by a read-only codex verifier, 2026-07-02 — caveat: repo-`H` needs
`conv A` inside `C_W`, else `+eta` slack). The upstream source
(`DELIVERABLE2_asq_proof.md:86`) mislabelled this tautology as the exactness content. The
intended open content — the skinny mutual-shadow degeneracy — is now carried by
[[conj-skinny-shadow-cap]]; the "reproduce `||Ebar||_1 >= H`" framing was the pure
convex-shadow-composition dead route in disguise (the needed direction of control there is
`||Ebar||_1 <= C*delta`, which FAILS exactly at `M+_deep ~ 0` per `obs-deep-leakage`).

Kept as an obstruction record so the id, the fr arm-B trail, and the ingest cross-references
stay resolvable; see `docs/LEARNINGS.md` (2026-07-04) for the retirement entry. Do not
re-open this contract; attack [[conj-skinny-shadow-cap]] or the arm-B sigma-cap instead.
