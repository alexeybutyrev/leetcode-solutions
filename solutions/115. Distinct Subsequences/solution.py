# Problem: Distinct Subsequences
# Language: python3
# Runtime: 40 ms
# Memory: 19.5 MB

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        N = len(s)
        M = len(t)
                
        if M >= N:
            return 1 if s == t else 0
        
        @cache
        def dp(i,j):
            if j == M:
                return 1
            
            # if we hit the end of line or have not enough symbols in s return 0
            if N - i < M - j:
                return 0
            
            # if symbols match move to the next in t otherwise count = 0
            count1 = dp(i+1,j+1) if s[i] == t[j] else 0
            # you can alwayse skip and move on
            count2 = dp(i+1,j)
            
            return count1 + count2
    
        return dp(0,0)
        
                