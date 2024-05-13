"""
Problem:

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 24.

Find the sum of all the multiples of 3 or 5 below 1000.

https://projecteuler.net/problem=1
"""


def calculate_sum_of_multiples(n: int, multiples: list[int]):
    print(f"Calculating sum of multiples {multiples} for {n}.")

    sum_of_multiples = 0

    common_multiples = []

    for j in multiples:
        common_multiples.append([i * j for i in multiples])
        common_multiples_test = [i * j for i in multiples if j != i]
        print(common_multiples_test)
        print(set(*common_multiples))

    for multiple in sorted(multiples):
        # second part is the sum of all natural numbers from 1 up to n
        sum_of_multiples += int(
            multiple * 0.5 * (((n - 1) // multiple) ** 2 + (n - 1) // multiple)
        )

    return sum_of_multiples


if __name__ == "__main__":
    print(calculate_sum_of_multiples(10, [3, 5, 6]))
