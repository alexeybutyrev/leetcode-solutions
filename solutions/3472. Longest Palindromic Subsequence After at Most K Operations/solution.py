# Problem: Longest Palindromic Subsequence After at Most K Operations
# Language: python3
# Runtime: 6404 ms
# Memory: 452.3 MB

class Solution:
    def longestPalindromicSubsequence(self, S: str, K: int) -> int:

        def f(x,y):
            d = abs(ord(x) - ord(y))
            d = min(d,26-d)
            return d
            
        @lru_cache(None)
        def dp(i,j,K):
            if i == j: return 1
            if i > j: return 0

            ans = max(dp(i+1,j,K), dp(i,j-1,K))
            
            d = f(S[i],S[j])
            if d <= K:
                ans = max(ans, 2 + dp(i+1,j-1,K-d))
            return ans

        return dp(0,len(S) - 1,K)