#!/usr/bin/env python3
"""Problem 6: Sum Square Difference

The sum of the squares of the first ten natural numbers is

    1^2 + 2^2 + ... + 10^2 = 385.

The square of the sum of the first ten natural numbers is

    (1 + 2 + ... + 10)^2 = 55^2 = 3025.

Hence, the difference between the sum of the squares of the first ten natural numbers and the square of the sum is

    3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

https://projecteuler.net/problem=6
"""


def sum_square_difference(n: int):
    return 0.25 * n**4 + n**3 / 6 - 0.25 * n**2 - n / 6


if __name__ == "__main__":
    print(
        f"For checking: difference of sum of squares and square of sum for n = 10: {int(sum_square_difference(10))}"
    )
    print(
        f"For checking: difference of sum of squares and square of sum for n = 100: {int(sum_square_difference(100))}"
    )
