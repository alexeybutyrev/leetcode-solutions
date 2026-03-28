# Problem: Number of Dice Rolls With Target Sum
# Language: python3
# Runtime: 212 ms
# Memory: 14.8 MB

class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        MOD = 10 ** 9 + 7
        if target > f * d or target < d:
            return 0
        
        dp = [[0] * (f * d) for _ in range(d)]

        for i in range(f):
            dp[0][i] = 1

        for dice in range(1,d):
            for face in range(dice, (dice+1) * f):
                for b in range(1,f+1):
                    if face - b >= 0:
                        dp[dice][face] += dp[dice-1][face - b]
        
        return dp[-1][target-1] % MOD