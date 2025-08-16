//
// Problem 1: Multiples of 3 or 5
// If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
// The sum of these multiples is 24.
//
// Find the sum of all the multiples of 3 or 5 below 1000.
//
// https://projecteuler.net/problem=1
//

#include <iostream>
#include <list>
#include <set>
#include <math.h>

int calculate_sum_of_multiples(const int n, const std::set<int>& multiples) {
    int sum_of_multiples = 0;
    std::list<int> common_multiples;

    for(const int multiple : multiples) {
        sum_of_multiples += static_cast<int>(0.5 * static_cast<float>(multiple) * std::pow(static_cast<float>(n-1)/static_cast<float>(multiple), 2) + static_cast<float>(n - 1)/static_cast<float>(multiple));
    }

    return sum_of_multiples;
}

int main() {
    const std::set<int> multiples = {3, 5};
    std::cout << "Sum of multiples: " << calculate_sum_of_multiples(1000, multiples);
    return 0;
}
