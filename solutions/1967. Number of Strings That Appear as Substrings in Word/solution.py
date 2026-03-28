# Problem: Number of Strings That Appear as Substrings in Word
# Language: python3
# Runtime: 50 ms
# Memory: 14.2 MB

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(w in word for w in patterns)