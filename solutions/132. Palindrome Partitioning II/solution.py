# Problem: Palindrome Partitioning II
# Language: python3
# Runtime: 1664 ms
# Memory: 19.3 MB

class Solution:
    def minCut(self, s: str) -> int:
        ispali = lambda x: x==x[::-1]
        @cache
        def dp(s):
            n = len(s)
            if ispali(s):
                return 0
            c = inf
            for i in range(n):
                if ispali(s[:i+1]):
                    c = min(c, 1+dp(s[i+1:]))
            return c
        return dp(s)
                    
                    