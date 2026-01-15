"""
Problem:
LeetCode 344 - Reverse String
Given an array of characters s, reverse the array in-place.
You must modify the input array using O(1) extra memory.

Approach:
- Use recursion with two pointers (left and right).
- Base case: stop recursion when left >= right.
- Swap characters at left and right indices.
- Recursively call the function by moving left forward and right backward.
- The string is reversed in-place during recursive stack unwinding.

Time Complexity:
O(n)
- Each character is involved in exactly one swap.

Space Complexity:
O(n)
- Due to recursion call stack.
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        def helper(left, right):
            if left >= right:
                return

            s[left], s[right] = s[right], s[left]
            helper(left + 1, right - 1)

        helper(0, len(s) - 1)
