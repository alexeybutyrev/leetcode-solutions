# Problem: Collecting Chocolates
# Language: python3
# Runtime: 3651 ms
# Memory: 16.4 MB

class Solution:
    def minCost(self, A: List[int], x: int) -> int:
        N = len(A)
        ans = [x * k for k in range(N)]
        
        for i in range(N):
            cur = A[i]
            for k in range(N):
                cur = min(cur, A[i-k])
                ans[k] += cur
        return min(ans)