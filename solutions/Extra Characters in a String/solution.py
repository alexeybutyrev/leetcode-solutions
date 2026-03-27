# Problem: Extra Characters in a String
# Language: python3
# Runtime: 233 ms
# Memory: 16.9 MB

class Solution:
    def minExtraChar(self, S: str, D: List[str]) -> int:
        N = len(S)
        @cache
        def dfs(i):
            if i == N: return 0
            ans = 1 + dfs(i+1)
            for w in D:
                if S[i:].startswith(w):
                    ans = min(ans, dfs(i + len(w)))
            return ans
        return dfs(0)
        