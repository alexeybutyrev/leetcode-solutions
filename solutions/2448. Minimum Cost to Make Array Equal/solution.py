# Problem: Minimum Cost to Make Array Equal
# Language: python3
# Runtime: 892 ms
# Memory: 31.8 MB

class Solution:
    def minCost(self, A: List[int], C: List[int]) -> int:

        @cache
        def count(x):
            ans = 0
            for a,c in zip(A,C):
                ans += abs(a-x) * c
            return ans
        
        lo = 0
        hi = max(A)+1
        
        while lo < hi:
            mid = lo + hi >> 1
            
            if  count(mid) <= count(mid + 1):
                hi = mid
            else:
                lo = mid + 1
                                
        return count(lo)
        