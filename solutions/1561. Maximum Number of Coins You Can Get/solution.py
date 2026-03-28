# Problem: Maximum Number of Coins You Can Get
# Language: python3
# Runtime: 2504 ms
# Memory: 22.4 MB

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        print(piles)
        
        k = len(piles) // 3
        
        #count = piles[1]
        count = 0
        for i in range(k):   
            v1 = piles.pop(0)
            v2 = piles.pop(0)
            v3 = piles.pop()
            count += v2
            
        return count