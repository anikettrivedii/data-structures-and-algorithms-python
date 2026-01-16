"""
Problem: Power of Three
Platform: LeetCode (326)
Approach: Recursion by dividing n by 3
Time Complexity: O(log₃ n)
Space Complexity: O(log₃ n) due to recursion stack
"""

def is_power_of_three(n: int) -> bool:
    if n == 1:
        return True
    if n <= 0 or n % 3 != 0:
        return False
    return is_power_of_three(n // 3)
