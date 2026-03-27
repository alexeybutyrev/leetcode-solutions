# Problem: Detect Capital
# Language: python3
# Runtime: 32 ms
# Memory: 14.1 MB

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()
