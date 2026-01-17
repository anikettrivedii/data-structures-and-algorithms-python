"""
Problem:
LeetCode - Count Elements With Maximum Frequency
Given an array of positive integers nums, find the total number of elements
that appear with the maximum frequency.

Approach:
- Use a hash map (dictionary) to count the frequency of each number.
- Traverse the array and store frequencies using dictionary.get().
- Find the maximum frequency among all elements.
- Iterate through the frequency map and sum the frequencies of elements
  whose frequency equals the maximum frequency.
- Return the final count.

Time Complexity:
O(n)
- One pass to build the frequency map.
- One pass to find the maximum frequency.
- One pass to sum frequencies with maximum count.

Space Complexity:
O(n)
- Extra space used to store frequencies in the hash map.
"""

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        max_freq = max(freq.values())
        result = 0

        for val in freq.values():
            if val == max_freq:
                result += val

        return result
"""
Note:
This problem can also be solved using collections.Counter for more concise code.
A manual hash map is used here to clearly demonstrate the frequency-counting pattern.
This is the optimized approach.
"""
