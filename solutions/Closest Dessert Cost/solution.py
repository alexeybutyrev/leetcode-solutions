# Problem: Closest Dessert Cost
# Language: python3
# Runtime: 272 ms
# Memory: 22.8 MB

class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], T: int) -> int:
        toppingCosts = toppingCosts 
        
        seen = {0}
        
        for t in toppingCosts:
            seen |= {x + t for x in seen} | {x + 2 * t for x in seen}
        
        
        seen = {b + x for x in seen for b in baseCosts}

        ans = baseCosts[0]
        for cost in seen:
            if (abs(cost - T) < abs(ans - T) or abs(cost - T) == abs(ans - T) and cost < ans):
                ans = cost
                
        return ans
        
        