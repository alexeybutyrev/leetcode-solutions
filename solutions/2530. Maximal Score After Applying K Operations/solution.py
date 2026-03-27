# Problem: Maximal Score After Applying K Operations
# Language: python3
# Runtime: 746 ms
# Memory: 31.4 MB

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        h = []
        
        for x in nums:
            heappush(h,-x)
            
        ans = 0
        while h and k:
            x = heappop(h)
            x *= -1
            ans += x
            heappush(h, -ceil(x/3))
            k-=1
        return ans
            