# Problem: Largest 1-Bordered Square
# Language: python3
# Runtime: 332 ms
# Memory: 14.5 MB

class Solution:
    def largest1BorderedSquare(self, A: List[List[int]]) -> int:
        R = deepcopy(A)
        C = deepcopy(A)
        N, M = len(A), len(A[0])
        for r in R:
            for i in range(1,len(r)):
                if r[i-1] and r[i]:
                    r[i] += r[i-1]
        
        
        for j in range(M):
            for i in range(1,N):
                if C[i][j] and C[i-1][j]:
                    C[i][j] += C[i-1][j]
        ans = 0
        
        for r in range(min(N,M),0,-1):
            for i in range(N-r+1):
                for j in range(M-r+1):
                     if (R[i][j + r - 1] >= r and 
                         R[i + r - 1][j + r - 1] >= r and
                         C[i + r - 1][j + r - 1] >= r and 
                         C[i + r - 1][j] >= r 
                        ):
                            return r * r
        
        return ans
                        