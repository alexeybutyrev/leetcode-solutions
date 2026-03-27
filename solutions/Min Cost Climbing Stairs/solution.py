# Problem: Min Cost Climbing Stairs
# Language: python3
# Runtime: 45 ms
# Memory: 16.4 MB

class Solution:
    def minCostClimbingStairs(self, A: List[int]) -> int:
        
        
        A.append(0)
        a,b = A[0], A[1]
        
        for x in A[2:]:
            b,a = min(b + x, a + x), b
        
        return b