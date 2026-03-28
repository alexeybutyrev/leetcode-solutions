# Problem: Best Time to Buy and Sell Stock with Transaction Fee
# Language: python3
# Runtime: 672 ms
# Memory: 21.1 MB

class Solution:
    def maxProfit(self, A: List[int], fee: int) -> int:
        N = len(A)
        cash, hold = 0, -A[0]
        
        for i in range(1,N):
            cash = max(cash, hold + A[i] - fee)
            hold = max(hold, cash - A[i])
        
        return cash