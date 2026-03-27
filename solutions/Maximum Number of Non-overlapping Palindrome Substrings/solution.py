# Problem: Maximum Number of Non-overlapping Palindrome Substrings
# Language: python3
# Runtime: 61 ms
# Memory: 20.2 MB

class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        N = len(s)
        @cache
        def is_pali(x): 
            return x == x[::-1]
        @cache
        def dfs(i):
            if i + k > len(s):
                return 0
            ans = dfs(i+1)
            if is_pali(s[i:i+k]):
                ans = max(ans, 1 + dfs(i+k))
            if is_pali(s[i:i+k+1]):
                ans = max(ans, 1 + dfs(i+k+1))
            return ans
        return dfs(0)
                