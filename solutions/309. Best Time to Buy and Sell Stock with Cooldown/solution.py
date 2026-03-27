# Problem: Best Time to Buy and Sell Stock with Cooldown
# Language: python3
# Runtime: 32 ms
# Memory: 14.6 MB

class Solution:
    def maxProfit(self, A: List[int]) -> int:
        N = len(A)
        
        reset, hold, sold = 0, -inf, -inf
        
        for a in A:
            pre = sold
            sold = a + hold
            
            hold = max(hold, reset - a)
            
            reset = max(reset, pre)
        
        return max(sold,reset)