# Problem: Minimum Path Cost in a Grid
# Language: python3
# Runtime: 3789 ms
# Memory: 19.6 MB

class Solution:
    def minPathCost(self, A: List[List[int]], moveCost: List[List[int]]) -> int:

        N = len(A)
        M = len(A[0])
        
        q = []
        for a in A[0]:
            heappush(q,(a,1,a))
        
        ans = inf
        d = [[inf] * M for _ in range(N+1)]
        
        
        while q:
            s,i,a = heappop(q)
            if s > ans:
                continue
                
            if i == N:
                ans = min(ans, s)
                continue
                
            for j,c in enumerate(moveCost[a]):
                s0 = s + A[i][j] + c
                if d[i+1][j] > s0 and s0 < ans:
                    d[i+1][j] = s0
                    heappush(q,(s0,i+1,A[i][j]))
        return ans