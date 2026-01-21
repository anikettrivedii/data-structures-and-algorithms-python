"""
Problem: Two Sum
Platform: LeetCode (1)
Approach: Hash map to store seen values and indices
Time Complexity: O(n)
Space Complexity: O(n)
"""

def two_sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
