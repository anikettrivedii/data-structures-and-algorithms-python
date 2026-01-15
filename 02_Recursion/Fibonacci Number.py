"""
Problem:
LeetCode 509 - Fibonacci Number
Given an integer n, return the nth Fibonacci number where:
F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n > 1.

Approach:
- Use recursion based on the Fibonacci definition.
- Define base cases for n = 0 and n = 1.
- For all other values, recursively compute fib(n-1) and fib(n-2).
- This approach is simple and mirrors the mathematical formula directly.

Time Complexity:
O(2^n)
- Due to overlapping subproblems, each call branches into two recursive calls.

Space Complexity:
O(n)
- Recursive call stack can go up to depth n.
"""

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)
