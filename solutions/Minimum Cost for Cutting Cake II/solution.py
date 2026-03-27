# Problem: Minimum Cost for Cutting Cake II
# Language: python3
# Runtime: 3501 ms
# Memory: 49.7 MB

class Solution:
    def minimumCost(self, m: int, n: int, H: List[int], V: List[int]) -> int:
        
        h = []

        for x in H:
            heappush(h, (-x,0))
        
        for x in V:
            heappush(h, (-x,1))
        
        x = 1
        y = 1
        ans = 0
        while h:
            v, p = heappop(h)
            v *= -1
            if p:
                ans += v * x
                y +=1
            else:
                ans += v * y
                x +=1
        
        return ans