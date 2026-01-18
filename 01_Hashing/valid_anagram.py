"""
Problem: Valid Anagram
Platform: LeetCode (242)
Approach: Character frequency comparison using hashmap
Time Complexity: O(n)
Space Complexity: O(1) (since alphabet size is constant)
"""

def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in t:
        if ch not in freq:
            return False
        freq[ch] -= 1
        if freq[ch] == 0:
            del freq[ch]

    return len(freq) == 0
