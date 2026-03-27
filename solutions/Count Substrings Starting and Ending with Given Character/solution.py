# Problem: Count Substrings Starting and Ending with Given Character
# Language: python3
# Runtime: 26 ms
# Memory: 17.5 MB

class Solution:
    def countSubstrings(self, s: str, c: str) -> int:
        c = s.count(c)
        
        return c * (c + 1) // 2