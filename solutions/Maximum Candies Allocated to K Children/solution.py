# Problem: Maximum Candies Allocated to K Children
# Language: python3
# Runtime: 597 ms
# Memory: 29.8 MB

class Solution:
    def maximumCandies(self, A: List[int], k: int) -> int:
        if k == 1:
            return max(A)
        def cand(x):
            ans = 0
            for a in A:
                ans += a // x
                
            return ans >= k
        
        lo = 1
        hi = sum(A)
        
        while lo < hi:
            mid = lo + hi >> 1
            
            if cand(mid):
                lo =  mid + 1
            else:
                hi = mid
        
        #print(cand(lo))
        return lo - 1