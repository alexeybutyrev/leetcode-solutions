# Problem: Percentage of Letter in String
# Language: python3
# Runtime: 37 ms
# Memory: 13.8 MB

class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        return floor(Counter(s)[letter] * 100 / len(s))