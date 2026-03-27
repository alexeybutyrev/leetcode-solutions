# Problem: Minimum Insertion Steps to Make a String Palindrome
# Language: python3
# Runtime: 868 ms
# Memory: 183.1 MB

class Solution:
    def minInsertions(self, S: str) -> int:
        @cache
        def dp(i,j):
            if i >= j: return 0
            return dp(i+1,j-1) if S[i] == S[j] else min(1 + dp(i+1,j), 1 + dp(i,j-1))
        
        return dp(0,len(S) - 1)