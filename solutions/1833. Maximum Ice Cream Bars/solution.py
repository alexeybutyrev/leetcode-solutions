# Problem: Maximum Ice Cream Bars
# Language: python3
# Runtime: 796 ms
# Memory: 28 MB

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort(reverse = True)
        
        count = 0
        while costs and coins >= 0:
            
            coins -= costs.pop()
            if coins >= 0:
                count += 1
        
        return count
        