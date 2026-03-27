# Problem: Tuple with Same Product
# Language: python3
# Runtime: 467 ms
# Memory: 46.4 MB

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        
        count=0
        c = Counter()
        N = len(nums)
        hm = {}
        for i in range(N):
            for j in range(i+1, N):
                c[nums[i] * nums[j]] += 1
        
        ans = 0
        for v in c.values():
            ans += v * (v - 1) // 2
        return ans * 8