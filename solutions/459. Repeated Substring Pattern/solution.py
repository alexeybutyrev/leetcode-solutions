# Problem: Repeated Substring Pattern
# Language: python3
# Runtime: 43 ms
# Memory: 16.2 MB

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        t = s + s
        if s in t[1:-1]:
            return True
        return False
            