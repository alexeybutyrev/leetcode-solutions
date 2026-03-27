# Problem: Maximum Size Subarray Sum Equals k
# Language: python3
# Runtime: 108 ms
# Memory: 17.5 MB

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        d = {0:-1}
        mx = 0
        s = 0
        for ind,n in enumerate(nums):
            s+=n
            if s-k in d:
                mx = max(mx, ind - d[s-k])
            
            if s not in d:
                d[s] = ind
            
        return mx