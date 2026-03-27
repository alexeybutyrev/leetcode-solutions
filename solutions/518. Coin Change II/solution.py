# Problem: Coin Change II
# Language: python3
# Runtime: 140 ms
# Memory: 14.5 MB

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        count = [inf] * (amount+1)
        
        dp[0] = 1
        for c in coins:
            for a in range(c, amount+1):
                dp[a] += dp[a-c]
        
        return dp[-1]
            