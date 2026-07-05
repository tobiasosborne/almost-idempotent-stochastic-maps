---
id: conj-kernel
kind: open-problem
contract: (CONJECTURE) Kernel Conjecture: there are universal delta_0>0 and B<inf (n-free) such that every exact signed idempotent P with neg mass delta(P) <= delta_0 has W(P) nonempty and every hidden row vertex v with invisible mass sigma~_v > tau=sqrt(delta) satisfies dist_1(p_v, conv{p_w : w in W}) <= B tau. This single open input closes op-exposed-hull (via the hull-linear cap HLC) and hence op-classical.
defs: def-signed-idempotent; def-negative-mass; def-visible-set; def-invisible-mass; def-height
deps: 
status: conjecture
af: none
provenance: docs/ingest (classical-portfolio; contracts verbatim from ../almost-idempotent-positive-maps/argument/lemmas or report/kernel-conjecture.tex)
owner: A
workspace: proofs/conj-kernel
---

**THE theorem-facing input** (user decision 2026-07-05, adopting the DC4 redraw): the recorded
route `Kernel => HLC => op-exposed-hull => op-classical` is short-proof + mod-audit, priced link
by link in `docs/waves/2026-07-05-DC4-equiv-assembly-audit.md`. The complementary branch
(sigma~_v <= tau) is already a theorem upstream; this is the missing branch. [[conj-ex]] is a
SEPARATE conjectural attack route — no proved edge between the two in either direction (DC4;
never write "equivalently"). Evidence only (67k instances) -> `numerical`, never a proof
(`FINDINGS.md`).
