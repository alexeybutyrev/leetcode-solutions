# Problem: Minimum Speed to Arrive on Time
# Language: python3
# Runtime: 3684 ms
# Memory: 28.5 MB

class Solution:
    def minSpeedOnTime(self, A: List[int], hour: float) -> int:
        n = len(A)
        def f(speed):
            return A[-1] / speed + sum( (A[i] + speed - 1) // speed for i in range(n - 1))

        lo, hi = 1, 10_000_001
        
        while lo < hi:
            mid = lo + (hi - lo) // 2
            
            if f(mid) <= hour:
                hi = mid - 1
            else:
                lo = mid + 1
        
        if f(lo) <= hour:
            return lo
        if f(lo+1) <= hour:
            return lo + 1
        
        return -1