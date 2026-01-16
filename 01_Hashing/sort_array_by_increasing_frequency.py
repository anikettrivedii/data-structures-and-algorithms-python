"""
Problem: Sort Array by Increasing Frequency
Platform: LeetCode
Approach: Frequency map + custom sorting
Time Complexity: O(n log n)
Space Complexity: O(n)
"""

def frequency_sort(nums):
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    nums.sort(key=lambda x: (freq[x], -x))
    return nums
