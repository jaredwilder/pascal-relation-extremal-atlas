#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Recomputes the four results this repository states in its own voice.

    python verify.py

Standard library only. Exit 0 means everything reproduced.

Semantics: a C_r violation is ANY injective assignment of distinct values to
the coordinates, not a monotone tuple. Reading it as monotone gives different
numbers throughout.
"""
from __future__ import annotations

import sys
from itertools import combinations, permutations

FAILURES = []


def check(label, got, want):
    ok = got == want
    print("  %-54s %s" % (label, "PASS" if ok else "FAIL got=%r want=%r" % (got, want)))
    if not ok:
        FAILURES.append(label)


C3 = [1, -3, 3, -1]


def has_violation(values, coeffs=C3):
    for pe in permutations(values):
        if sum(c * v for c, v in zip(coeffs, pe)) == 0:
            return True
    return False


def gap_law(p, q, r):
    return (p + r == 2 * q) or (p == 3 * r) or (r == 3 * p) \
        or (p == 2 * q + 3 * r) or (r == 2 * q + 3 * p)


def test_gap_law(N=25):
    print("1. The five-species gap law for C3")
    tested = mismatch = 0
    for a, b, c, d in combinations(range(1, N + 1), 4):
        tested += 1
        if gap_law(b - a, c - b, d - c) != has_violation((a, b, c, d)):
            mismatch += 1
    check("quadruples tested in [1,%d]" % N, tested, 12650)
    check("mismatches against brute-force permutation search", mismatch, 0)


def pascal(r):
    row = [1]
    for i in range(r):
        row.append(row[-1] * (r - i) // (i + 1))
    return [((-1) ** i) * row[i] for i in range(r + 1)]


def base_violated(coeffs, B, maxexp):
    n = len(coeffs)
    for es in combinations(range(maxexp + 1), n):
        for pe in permutations(es):
            if sum(c * (B ** e) for c, e in zip(coeffs, pe)) == 0:
                return True
    return False


def test_least_base():
    print("2. The least geometric base per Pascal order")
    got = []
    for r in range(1, 9):
        co = pascal(r)
        for B in range(2, 9):
            if not base_violated(co, B, min(10, 3 + r)):
                got.append(B)
                break
    check("least base, r = 1..8", got[:8], [2, 2, 2, 2, 3, 3, 2, 3])
    print("     not monotone: 3 at r=5, back to 2 at r=7, 3 at r=8")
    print("     r >= 9 is contested between two sources and NOT settled here")
    print()
    print("   the published sufficient rule is 2^r + 1; the store's own")
    print("   dominance corollary gives 2^r. Both are violation-free:")
    for r in range(1, 9):
        co = pascal(r)
        check("  base 2^%d = %-5d is violation-free" % (r, 2 ** r),
              base_violated(co, 2 ** r, min(10, 3 + r)), False)


def test_density():
    print("3. The density bound that was never multiplied out")
    check("the applied bound 11/50", round(11 / 50, 4), 0.22)
    check("the available bound 12/60", round(12 / 60, 4), 0.2)
    check("12/60 is exactly 1/5", 12 * 5 == 60 * 1, True)


def max_avoiding(N, coeffs):
    n = len(coeffs)

    def ok(S):
        for quad in combinations(S, n):
            if has_violation(quad, coeffs):
                return False
        return True

    for size in range(N, 0, -1):
        for S in combinations(range(1, N + 1), size):
            if ok(S):
                return size
    return 0


def test_b_atlas():
    print("4. Non-monotonicity in b for [1, -b, b, -1]")
    for N, want in ((4, [3, 4, 3, 4, 4, 4]), (8, [5, 4, 5, 5, 5, 6])):
        row = [max_avoiding(N, [1, -b, b, -1]) for b in range(1, 7)]
        check("N = %d, b = 1..6" % N, row, want)
        drops = sum(1 for i in range(5) if row[i + 1] < row[i])
        check("  the row falls and rises again", drops >= 1, True)


def main():
    for fn in (test_gap_law, test_least_base, test_density, test_b_atlas):
        fn()
        print()
    if FAILURES:
        print("FAILED: %d check(s)" % len(FAILURES))
        for f in FAILURES:
            print("   " + f)
        return 1
    print("ALL CHECKS PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
