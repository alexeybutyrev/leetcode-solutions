# Problem: Final Prices With a Special Discount in a Shop
# Language: python3
# Runtime: 112 ms
# Memory: 13.9 MB

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        res = []
        n = len(prices)
        for i in range(n):
            v = prices[i]
            for j in range(i+1,n):
                if prices[j] <= prices[i]:
                    v -= prices[j]
                    break
            res.append(v)
        
        return res
                
            