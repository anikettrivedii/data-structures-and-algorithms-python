"""
Problem: Number of Common Factors
Platform: LeetCode
Approach: Compute GCD, then count its divisors
Time Complexity: O(sqrt(gcd(a, b)))
Space Complexity: O(1)
"""

from math import gcd

def number_of_common_factors(a: int, b: int) -> int:
    g = gcd(a, b)
    count = 0

    i = 1
    while i * i <= g:
        if g % i == 0:
            count += 1
            if i != g // i:
                count += 1
        i += 1

    return count
