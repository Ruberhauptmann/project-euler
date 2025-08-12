#!/usr/bin/env python3
"""Problem 14: Longest Collatz Sequence

The following iterative sequence is defined for the set of positive integers:

    n -> n/2 (n is even)
    n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

    13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

https://projecteuler.net/problem=14
"""


def collatz_length(n: int):
    if n in values.keys():
        return values[n]

    if n % 2 == 0:
        values[n] = 1 + collatz_length(n // 2)
    else:
        values[n] = 2 + collatz_length((3 * n + 1) // 2)

    return values[n]


if __name__ == "__main__":
    limit = int(1e6)
    max_length = 0
    starting_number = 0
    values = {1: 1}
    for i in range(int(limit / 2), limit):
        length = collatz_length(i)
        if length > max_length:
            max_length = length
            starting_number = i

    print(f"Longest chain for {starting_number}, with length {max_length}")
