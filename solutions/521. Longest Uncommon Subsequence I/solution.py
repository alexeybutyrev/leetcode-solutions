# Problem: Longest Uncommon Subsequence I
# Language: python3
# Runtime: 35 ms
# Memory: 16.2 MB

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        return -1 if a == b else max(len(a),len(b))
                
                