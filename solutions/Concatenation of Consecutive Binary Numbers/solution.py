# Problem: Concatenation of Consecutive Binary Numbers
# Language: python3
# Runtime: 746 ms
# Memory: 19.1 MB

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        l = 0
        ans = 0
        for i in range(1,n+1):
            if (i & (i - 1)) == 0:
                l += 1
            ans = ((ans << l) | i) % MOD

        return ans