# Problem: Find Anagram Mappings
# Language: python3
# Runtime: 24 ms
# Memory: 14.1 MB

class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        res = []
        for a in A:
            res.append(B.index(a))
        return res