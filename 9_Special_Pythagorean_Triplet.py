#!/usr/bin/env python3
"""Problem 9: Special Pythagorean Triplet

A Pythagorean triplet is a set of three natural numbers ,a < b < c, for which

    a^2 + b^2 = c^2.

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.

Find the product abc.

https://projecteuler.net/problem=9
"""


def pythagorean_triplet(n: int) -> tuple[int, int, int]:
    for a in range(1, n - 1):
        for b in range(a + 1, n):
            c = n - a - b
            if a**2 + b**2 == c**2:
                return a, b, c


if __name__ == "__main__":
    triplet = pythagorean_triplet(1000)
    print(f"Pythagorean triplet where a + b + c = 1000: {triplet}")
    print(f"Product: {triplet[0] * triplet[1] * triplet[2]}")
