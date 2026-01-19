"""
Problem: Power of Two
Platform: LeetCode (231)
Approach: Recursively divide by 2
Time Complexity: O(log n)
Space Complexity: O(log n) due to recursion stack
"""

def is_power_of_two(n: int) -> bool:
    if n == 1:
        return True
    if n <= 0 or n % 2 != 0:
        return False
    return is_power_of_two(n // 2)
