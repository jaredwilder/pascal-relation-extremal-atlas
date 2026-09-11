# What the summaries left out

Author: Jared Wilder. First public timestamp: 2026-09-11.

Two ledger files summarise a computational round on the Pascal relations
`C_r: sum_i (-1)^i binom(r,i) x_i = 0`. The primary stores those summaries were written from hold
**seven** directories, and the highest tier supersedes both summaries.

This is the mathematics that did not reach either summary. Everything below was recomputed here from
scratch.

**Semantics.** A `C_r` violation is any injective assignment of distinct values to the coordinates,
not a monotone tuple. Reading it as monotone gives different numbers throughout.

---

## 1. A gap law that makes the whole family hand-checkable

For a sorted quadruple `a < b < c < d` with gaps `p = b-a`, `q = c-b`, `r = d-c`, the set
`{a,b,c,d}` admits a `C3` violation `x1 - 3x2 + 3x3 - x4 = 0` **if and only if**

```
p + r = 2q      or      p = 3r      or      r = 3p      or      p = 2q + 3r      or      r = 2q + 3p
```

Five species, nothing else. **Checked against brute-force permutation search on every quadruple in
`[1,25]`: 12,650 cases, 0 mismatches.**

This reduces membership from a search over 24 permutations to five linear tests on the gap word. It
was sitting in a Lean side-receipt and appears in neither summary.

## 2. The published base bound is exponentially far from least

For the Pascal relation of order `r`, the least geometric base `B` such that `{B^n}` contains no
violation, recomputed here for `r = 1..9`:

```
r                      1  2  3  4  5  6  7  8   9
least base             2  2  2  2  3  3  2  3   4
published rule 2^r+1   3  5  9 17 33 65 129 257 513
```

**The measured value is not monotone in `r`** — it rises to 3 at `r = 5`, falls back to 2 at
`r = 7`, then 3 at `r = 8` and 4 at `r = 9`. At `r = 9` the gap between the published rule and the
truth is a factor of 128.

### r = 9, settled

Two independent passes disagreed above `r = 8`. One reported the table continuing `4, 5, 4, 4` for
`r = 9..12`. The other reported that **no** base below 200 is free at `r = 9`.

A pruned depth-first search over injective exponent assignments settles `r = 9`:

| exponent range | base 2 | base 3 | base 4 | base 5 | base 6 | base 7 | base 8 |
|---|---|---|---|---|---|---|---|
| `0..9` | violated | violated | **free** | free | free | free | free |
| `0..11` | violated | violated | **free** | free | free | free | free |
| `0..13` | violated | violated | **free** | free | free | free | free |

**The least base at `r = 9` is 4.** The result is stable across all three exponent ranges, which
confirms the `4, 5, 4, 4` table at `r = 9` and refutes the claim that nothing below 200 is free.

The base-2 witness supplied by the second source is correct and only rules out base 2:

```
coeffs   [1, -9, 36, -84, 126, -126, 84, -36, 9, -1]
values   (2, 4, 8, 64, 16, 1, 256, 512, 32, 128)
sum      2 - 36 + 288 - 5376 + 2016 - 126 + 21504 - 18432 + 288 - 128  =  0
```

`r = 10..12` remains unverified here. The dominance argument gives an unconditional upper handle: at
`r = 9` the coefficients sum to 512 in absolute value, so base 513 is free, and the measured 4 sits
far below it.

### The same question has three different answers in the same store

| source | answer for order `r` |
|---|---|
| the published rule | `B_r = 2^r + 1` |
| the store's own sharper dominance corollary | `B_r = 2^r` |
| measured least base, `r = 1..9` | between **2 and 4** |

The dominance corollary is `B > max_j (sum_i |c_i| - |c_j|) / |c_j|`, which for Pascal gives `2^r`,
one less than the published rule. I confirmed base `2^r` is violation-free for `r = 1..8`.

**So `2^r + 1` is sufficient and not sharp, and it is not sharp by two separate margins.** For
`r = 1..8` the measured answer is smaller than either rule by an exponential factor: at `r = 8` the
published rule gives 257, the dominance corollary gives 256, and the least base is 3.

## 3. A density bound that was never multiplied out

The store proves a bootstrap: if the exact maximum on an interval of length `L` is `M`, then every
infinite relation-free set has upper density at most `M/L`.

It applies this with `C3(50) = 11`, giving `11/50 = 0.22`.

The apex tier of the same store contains `C3(60) = 12`. That gives

```
upper density <= 12/60 = 1/5
```

**Both halves were present and were never multiplied together**, because they sit in different
directories.

## 4. Three non-monotonicities in `b`, not one

For the relation `[1, -b, b, -1]`, the maximum subset size of `[1,N]` avoiding it, over `b = 1..6`:

```
N = 4    ->   3, 4, 3, 4, 4, 4
N = 8    ->   5, 4, 5, 5, 5, 6
N = 16   ->   6, 6, 6, 8, 7, 8
```

Recomputed here for `N = 4` and `N = 8`. Each row falls and rises again as `b` increases. **The
summaries carry only the `N = 4` row**; the full atlas spans `N = 4..20` and `b = 1..6`, 102 entries.

---

## Verified from the store, reported with its numbers

**The complete `C3` extremal table.**

| N | 40–44 | 45–50 | 51–60 | 61–64 |
|---|---|---|---|---|
| `C3(N)` | 10 | 11 | 12 | 13 |

At `N = 51` the unique maximizer is `{1,4,6,8,11,24,28,41,44,46,48,51}`, gap word
`[3,2,2,3,13,4,13,3,2,2,3]`, palindromic and summing to 50. The optimum census for `N = 45..51` is
`4, 10, 19, 52, 89, 178, 1`.

**A cross-order birth atlas**, of which one row lives in a directory the atlas file does not point
at:

| relation | m | min span | least N | witness |
|---|---|---|---|---|
| `C3 [1,-3,3,-1]` | 12 | 50 | 51 | `{1,4,6,8,11,24,28,41,44,46,48,51}` |
| `C4 [1,-4,6,-4,1]` | 9 | 23 | 24 | `{1,4,5,8,11,20,21,23,24}` |
| **`C5`** | 8 | 25 | 26 | `{1,3,9,17,19,22,25,26}` |
| `C6` | 9 | 17 | 18 | `{1,2,4,8,9,11,15,16,18}` |

The `C6` birth gap word `[1,2,4,1,2,4,1,2]` is cleanly periodic, unlike the palindromic `C3` ones.

**A digit-alphabet atlas for bases 3 to 12.** Maximum alphabet cardinality, `C3`-only:
`1,1,2,2,2,2,3,3,3,3`. Joint `C2 + C3`: `1,1,2,2,2,2,3,2,3,3` — **a dip to 2 at base 10** while bases
9, 11 and 12 all reach 3. The best density exponent is `log_9 3 = 1/2` exactly. No 4-element alphabet
survives in bases 9 to 12. The calibration set knew only base 9.

**An exact refutation at `N = 40`.** Proposed values `[8, 9, 10, 12]` for `b = 1..4`; measured
`[9, 9, 10, 12]`. The refuted `8` is the Sidon number, and the `b = 1` relation with four distinct
values is strictly weaker than Sidon because it misses 3-term progressions.

**Sidon is not Sidon-and-`C3`**, at exactly 14 values of `N <= 50`: the binding intervals are
`[26,27]`, `[35,40]`, `[45,50]`. Cross-checked two ways: the pure-Sidon column agrees with published
optimal Golomb ruler lengths at every `n >= 3` with zero mismatches, and the jump points 26, 35, 45
are exactly `L(7)+1`, `L(8)+1`, `L(9)+1`.

**The `C2`/`C3` interaction at `N = 9`** is fully classified: marginals 5 and 5, joint 4, with exactly
49 joint optima in 27 reflection orbits, point-incidence `(24,25,21,20,16,20,21,25,24)` — symmetric,
with the centre point 5 rarest — and all 126 five-subsets of `[9]` blocked.

---

## The Lean record: a wall, a closure, and a self-reversal

The round hit a `FORMALIZATION_WALL` — `bv_decide`, exit 124 at 900 seconds, target not proved,
0 sorry — while three lemmas were kernel-checked.

A later tier closed it. `C3Span50Semantic.span50` is kernel-checked via **447,254 LRAT additions**
over a 16,446-clause bridge, with `sorryAx: false`, `nativeDecide: false`, and axioms exactly
`[propext, Classical.choice, Quot.sound]`. It carries a measured LRAT-size comparison across five
cardinality encodings, from a sequential counter at 98.5 MB trimmed to a modulo-totalizer at
149.8 MB.

The same tier then files an invalidation that **reverses its own agent's stop** as "not a valid
terminal boundary."

## What the store says about its own novelty

The novelty dossier sets `absoluteNoveltyClaimed: false` and records that its own first pass
**conflated this relation with ordinary 3-term-progression avoidance**. It is a search-absence
record, not a priority claim.

The mechanism narratives in the round were model-proposed. The extremal numbers were not, and every
one quoted above was reproduced here without them.

## Not checked

The minimum motif cover (claimed optimal at size 24), the LRAT certificate itself, the
carry-automaton argument for all word lengths (digit checks here are bounded to length 5), and a
subtree the store already marks NO-GO on the grounds that no platform calibration exists.

## Verification

```bash
python verify.py
```

Standard library only.

## License

Apache-2.0.
