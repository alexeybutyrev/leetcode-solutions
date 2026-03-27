# Problem: Valid Anagram
# Language: python3
# Runtime: 28 ms
# Memory: 14.5 MB

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)