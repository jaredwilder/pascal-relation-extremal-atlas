# Pascal-relation extremal atlas

For the order-`r` Pascal relation

\[
C_r:\qquad \sum_i(-1)^i\binom ri x_i=0,
\]

this repository studies finite avoidance sets, positional constructions, and exact small extremal values. A violation uses an injective assignment of distinct values to the coordinates; the variables are not assumed to be in monotone order.

## Exact gap criterion for `C_3`

Let `a<b<c<d` and write the consecutive gaps

\[
p=b-a,\qquad q=c-b,\qquad r=d-c.
\]

Then `{a,b,c,d}` admits a `C_3` violation if and only if at least one of

\[
p+r=2q,
\]
\[
p=3r,
\qquad
r=3p,
\]
\[
p=2q+3r,
\qquad
r=2q+3p
\]

holds.

This replaces a 24-permutation search by five linear tests on the gap word. It agrees with brute-force permutation checking on every quadruple in `[1,25]`.

## Least geometric bases

For the set `{B^n}`, the least tested base avoiding the order-`r` Pascal relation is

```text
r          1  2  3  4  5  6  7  8  9
least B    2  2  2  2  3  3  2  3  4
```

At `r=9`, independent searches over several exponent ranges agree that bases 2 and 3 admit violations while base 4 is free.

The generic dominance argument gives a much larger sufficient base of order `2^r`; the finite data above show that bound is far from sharp in small orders.

## Infinite-density transfer

If the exact maximum size of a relation-free subset of an interval of length `L` is `M`, then every infinite relation-free set has upper density at most

\[
M/L.
\]

For `C_3`, the exact finite value

\[
C_3(60)=12
\]

gives

\[
\boxed{\overline d(A)\le1/5}
\]

for every infinite `C_3`-free set `A`.

## Exact `C_3` table near 64

The recovered finite optimization gives

| `N` | 40–44 | 45–50 | 51–60 | 61–64 |
|---|---:|---:|---:|---:|
| maximum `C_3`-free size | 10 | 11 | 12 | 13 |

At `N=51`, one maximizing 12-set is

\[
\{1,4,6,8,11,24,28,41,44,46,48,51\}.
\]

Its gap sequence

```text
3,2,2,3,13,4,13,3,2,2,3
```

is palindromic.

## Cross-order birth examples

The smallest intervals in the recovered atlas supporting selected large relation-free sets include:

| relation | set size | least `N` | witness |
|---|---:|---:|---|
| `C_3` | 12 | 51 | `{1,4,6,8,11,24,28,41,44,46,48,51}` |
| `C_4` | 9 | 24 | `{1,4,5,8,11,20,21,23,24}` |
| `C_5` | 8 | 26 | `{1,3,9,17,19,22,25,26}` |
| `C_6` | 9 | 18 | `{1,2,4,8,9,11,15,16,18}` |

## Digit alphabets

For positional digit alphabets in bases 3 through 12, the recovered maximum alphabet sizes are

```text
C3 only     : 1,1,2,2,2,2,3,3,3,3
C2 and C3   : 1,1,2,2,2,2,3,2,3,3
```

The joint constraint therefore has a genuine dip at base 10 while bases 9, 11, and 12 admit three digits.

## Formal certificate

One finite `C_3` extremal statement was subsequently checked in Lean through an LRAT certificate. The theorem `C3Span50Semantic.span50` has axiom footprint

```text
[propext, Classical.choice, Quot.sound]
```

with no `sorryAx` and no `native_decide` in the final certificate path.

## Verification

```bash
python verify.py
```

The standard-library verifier reproduces the finite arithmetic and extremal checks packaged with this atlas.

Author: Jared Wilder. License: Apache-2.0.
