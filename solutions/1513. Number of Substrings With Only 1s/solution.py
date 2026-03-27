# Problem: Number of Substrings With Only 1s
# Language: python3
# Runtime: 15 ms
# Memory: 19.2 MB

class Solution:
    def numSub(self, s: str) -> int:
        ans = 0
        MOD = 10**9 + 7
        for x,l in groupby(s):
            if x == '1':
                ln = len(list(l))
                ans += ln * (ln + 1) >> 1
                ans %= MOD
        return ans