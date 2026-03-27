# Problem: Best Time to Buy and Sell Stock with Transaction Fee
# Language: python3
# Runtime: 592 ms
# Memory: 21.4 MB

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        N = len(prices)
        
        curr = prices[0]
        ans = 0
        for i in range(1, N):
            if prices[i] < curr:
                curr = prices[i]
            elif prices[i] > curr + fee:
                ans += prices[i] - curr - fee
                curr = prices[i] - fee
        
        return ans