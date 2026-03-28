# Problem: Decode Ways
# Language: python3
# Runtime: 24 ms
# Memory: 14.5 MB

class Solution:
    def numDecodings(self, s: str) -> int:
        
        N = len(s)
        if not s or s.startswith("0"):
            return 0
        @lru_cache(None)
        def count(i):
            if i == N:
                return 1
            if s[i] == "0":
                return 0
            if i < N - 1 and ((s[i] == "2" and s[i+1] in ["0","1","2","3","4","5","6"]) or s[i] == "1"):
                return count(i+1) + count(i+2)
            else:
                return count(i+1)
        
        return count(0)
    