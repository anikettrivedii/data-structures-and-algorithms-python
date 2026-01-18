"""
Problem: Contains Duplicate
Platform: LeetCode (217)
Approach: Frequency counting using hashmap
Time Complexity: O(n)
Space Complexity: O(n)
"""

def contains_duplicate(nums):
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1
        if freq[num] > 1:
            return True

    return False
