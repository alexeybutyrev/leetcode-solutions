# Problem: Check If Two String Arrays are Equivalent
# Language: python3
# Runtime: 20 ms
# Memory: 14.1 MB

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)