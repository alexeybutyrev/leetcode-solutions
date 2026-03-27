# Problem: Maximum Product After K Increments
# Language: python3
# Runtime: 2392 ms
# Memory: 24.6 MB

class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        h = []
        for a in nums:
            heappush(h,a)
        
        for _ in range(k):
            heappush(h, heappop(h) + 1)
        
        ans = 1
        for a in h:
            ans *= a
            ans %= MOD
        return ans