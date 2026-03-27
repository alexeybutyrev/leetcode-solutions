# Problem: Minimum Removals to Achieve Target XOR
# Language: python3
# Runtime: 941 ms
# Memory: 347.9 MB

class Solution:
    def minRemovals(self, A: List[int], T: int) -> int:

        x = 0
        for a in A:
            x ^= a
        N = len(A)
        @cache
        def dp(mask, i):
            if mask == T: return 0
            if i == N: return inf

            # keep
            ans = dp(mask,i+1)
            # remove
            ans = min(ans, 1 + dp(mask ^ A[i], i+1))
            return ans

        ans = dp(x,0)
        return -1 if ans == inf else ans