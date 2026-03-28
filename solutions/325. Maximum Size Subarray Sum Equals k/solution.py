# Problem: Maximum Size Subarray Sum Equals k
# Language: python3
# Runtime: 368 ms
# Memory: 50.7 MB

class Solution:
    def maxSubArrayLen(self, A: List[int], k: int) -> int:
        d = {0:-1}
        mx = 0
        s = 0
        for ind,n in enumerate(A):
            s+=n
            if s-k in d:
                mx = max(mx, ind - d[s-k])
            
            if s not in d:
                d[s] = ind
            
        return mx