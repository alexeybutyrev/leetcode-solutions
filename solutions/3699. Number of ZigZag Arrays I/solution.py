# Problem: Number of ZigZag Arrays I
# Language: python3
# Runtime: 3461 ms
# Memory: 18.1 MB

class Solution:
    def zigZagArrays(self, N: int, L: int, R: int) -> int:
        MOD = 10**9 + 7
        R -= L


        dp = [1] * (R + 1)

        for i in range(1,N):
            pre = 0
            if i & 1:
                for j in range(R+1):
                    pre2 = pre + dp[j]
                    dp[j] = pre
                    pre = pre2 % MOD
            else:
                for j in range(R,-1,-1):
                    pre2 = pre + dp[j]
                    dp[j] = pre
                    pre = pre2 % MOD
        return 2 * sum(dp) % MOD