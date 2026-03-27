# Problem: Maximum Difference Between Increasing Elements
# Language: python3
# Runtime: 44 ms
# Memory: 14.5 MB

class Solution:
    def maximumDifference(self, A: List[int]) -> int:
        N = len(A)
        rm = A[-1]
        ans = -1
        for i in range(N-2,-1,-1):
            
            d = rm - A[i]
            if d > 0:
                ans = max(d, ans)
            rm = max(A[i],rm)
        return ans