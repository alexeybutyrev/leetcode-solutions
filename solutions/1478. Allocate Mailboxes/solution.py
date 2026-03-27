# Problem: Allocate Mailboxes
# Language: python3
# Runtime: 568 ms
# Memory: 16.2 MB

class Solution:
    def minDistance(self, A: List[int], k: int) -> int:
        N = len(A)
        A.sort()
        costs = [[0] * N for _ in range(N)]
        
        for i in range(N):
            for j in range(N):
                median = A[(i+j) // 2]
                for m in range(i,j+1):
                    costs[i][j] += abs(median - A[m])
        @cache
        def dp(k,i):
            if k == 0 and i == N:
                return 0
            if k ==0 or i == N: return inf
            
            ans = inf
            for j in range(i,N):
                ans = min(ans, costs[i][j] + dp(k-1,j+1))
            
            return ans
        return dp(k,0)
                    
        