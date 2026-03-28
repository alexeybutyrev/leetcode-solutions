# Problem: Peak Index in a Mountain Array
# Language: python3
# Runtime: 64 ms
# Memory: 15.5 MB

class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        
        def f(x):
            return A[x] > A[x-1]
            
        lo, hi = 0, len(A) -1
        while lo <= hi:
            x = lo + (hi - lo) // 2
            
            if f(x):
                lo = x + 1
            else:
                hi = x - 1
        
        return lo - 1
        