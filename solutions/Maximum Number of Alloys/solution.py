# Problem: Maximum Number of Alloys
# Language: python3
# Runtime: 573 ms
# Memory: 16.7 MB

class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        
        M = (1 + budget // min(cost)) + max(stock)
        def check(c,x):
            spend = 0
            for i,a in enumerate(c):
                spend += max(0,(a * x - stock[i])) * cost[i]
            return spend <= budget

        def find_units(c):
            lo, hi = 0, M 
            while lo < hi:
                mid = lo + hi >> 1
                if check(c, mid):
                    lo = mid + 1
                else:
                    hi = mid
                    
            if not check(c,lo):
                lo -= 1
            return lo
        
        ans = 0
        for c in composition:
            lans = find_units(c)
            ans = max(ans, lans)
        return ans