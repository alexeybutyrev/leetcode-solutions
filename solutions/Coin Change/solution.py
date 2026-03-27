# Problem: Coin Change
# Language: python3
# Runtime: 1092 ms
# Memory: 14.5 MB

from math import inf
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [inf] * (amount+1)
        
        dp[0] = 0

        
        for c in coins:
            for j in range(c,amount+1):
                    dp[j] = min(dp[j - c] + 1, dp[j])
        
        return -1 if dp[amount] == inf else dp[amount]
        
        
        
            
            
        
        