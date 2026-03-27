# Problem: Best Time to Buy and Sell Stock IV
# Language: python3
# Runtime: 122 ms
# Memory: 14 MB

class Solution:
    def maxProfit(self, K: int, A: List[int]) -> int:
        if K ==0:
            return 0
        N = len(A)
        h = [inf] * K
        p = [0] * K
        
        for a in A:
            h[0] = min(a, h[0])
            p[0] = max(p[0], a - h[0])
            
            for i in range(1,K):
                h[i] = min(h[i], a - p[i-1])
                p[i] = max(p[i], a - h[i])
            
        
        return p[-1]