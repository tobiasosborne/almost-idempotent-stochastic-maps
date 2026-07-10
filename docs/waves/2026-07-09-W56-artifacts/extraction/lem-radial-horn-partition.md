---
id: lem-radial-horn-partition
kind: lemma
contract: 'For every finite nonnegative measure Gamma on pairs of row points, every row point v, every tau > 0, and every set C with Gamma(C) > 1/2, exactly one alternative holds: the C-mass with ||p_u-p_v||_1 >= 4tau is at least 1/4, or that far mass is less than 1/4 and the complementary C-mass with ||p_u-p_v||_1 < 4tau is greater than 1/4.'
defs: 
deps: 
status: proved-candidate
owner: W56-extraction
---

# Radial horn partition

## Statement

Let \(\Gamma\) be a finite nonnegative measure on pairs of row points \((x,u)\), let \(v\) be a row point, let \(\tau>0\), and let \(C\) satisfy \(\Gamma(C)>1/2\).  Exactly one of the following alternatives holds:

\[
 \tag{F}
 \Gamma\{(x,u)\in C:\|p_u-p_v\|_1\ge4\tau\}\ge\frac14,
\]

or

\[
 \tag{N}
 \begin{gathered}
 \Gamma\{(x,u)\in C:\|p_u-p_v\|_1\ge4\tau\}<\frac14,\\
 \Gamma\{(x,u)\in C:\|p_u-p_v\|_1<4\tau\}>\frac14.
 \end{gathered}
\]

Thus distance equality belongs to the far cell and mass equality at \(1/4\) belongs to (F).

## Proof

The predicates \(\|p_u-p_v\|_1\ge4\tau\) and \(\|p_u-p_v\|_1<4\tau\) partition \(C\).  If (F) holds, (N) fails by its first inequality.  If (F) fails, the far mass is strictly less than \(1/4\), so the complementary near mass is
\[
 \Gamma(C)-\Gamma(C\cap\mathrm{far})
 >\frac12-\frac14=\frac14.
\]
Then (N) holds.  The alternatives are therefore exhaustive and disjoint.

## Notes

The Proposition-E two-point counterweight can satisfy this standalone lemma after diagonal lifting: the lemma has no co-top or depth hypothesis and merely assigns a cell.  It is excluded only in the intended assembled use, where \(C\) is the coefficient-kernel corner and both coordinates obey \(z<4\tau\), which forces strict depth \(>H-4\tau\).  Splitting an atom into clones preserves all displayed mass sums, and appending a transient row does not create a boundary gap in this literal two-cell partition.
