#!/usr/bin/env python3
"""Problem 100: Arranged Probability

If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken
at random, it can be seen that the probability of taking two blue discs is

    P(BB) = (15/21) x (14/20) = 1/2

The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box
containing eighty-five blue discs and thirty-five red discs.
By finding the first arrangement to contain over 10^{12} = 1 00 000 000 000 discs in total, determine the number of
blue discs that the box would contain.

https://projecteuler.net/problem=100
"""


def find_number_of_blue_discs(n: int) -> int | None:
    for n_blue_discs in range(1, n + 1):
        if (n_blue_discs**2 - n_blue_discs) / (n**2 - n) == 0.5:
            return n_blue_discs

    return None


if __name__ == "__main__":
    print(find_number_of_blue_discs(int(1e12)))
