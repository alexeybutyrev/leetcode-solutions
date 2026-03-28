# Problem: Longest Palindromic Subsequence
# Language: python3
# Runtime: 416 ms
# Memory: 21.4 MB

class Solution:
    def longestPalindromeSubseq(self, S: str) -> int:
        
        @cache
        def dp(s):
            
            ans = 0
            for c in set(s):
                l,r = s.find(c), s.rfind(c)
                
                ans = max(ans, 1 if l == r else 2 + dp(s[l+1:r]))
            return ans
                
        return dp(S) 
                    
                