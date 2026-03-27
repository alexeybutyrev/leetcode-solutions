# Problem: Smallest Range I
# Language: python3
# Runtime: 186 ms
# Memory: 34.3 MB

from numpy import median
class Solution:
    def smallestRangeI(self, A: List[int], k: int) -> int:
        
        mn = min(A)
        mx = max(A)
        
        if mn + k < mx - k:
            return mx - mn - 2*k
        return 0
        