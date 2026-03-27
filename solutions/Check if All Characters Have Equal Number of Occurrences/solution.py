# Problem: Check if All Characters Have Equal Number of Occurrences
# Language: python3
# Runtime: 39 ms
# Memory: 14.3 MB

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:        
        return len(Counter(Counter(s).values())) == 1